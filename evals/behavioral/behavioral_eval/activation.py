"""Evaluate top-level Marketing Agent Skills activation from sealed run events.

This lane is intentionally separate from answer and internal-route evaluation.
It observes whether the host activated the skill; it does not judge answer quality.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .models import CaseContract, RunRecord, RunState, ValidationError
from .trace import extract_skill_paths


ACTIVATION_ORACLE_SCHEMA_VERSION = 1
ACTIVATION_REPORT_SCHEMA_VERSION = 1
EXPECTATIONS = {"required", "forbidden"}
DISPOSITIONS = (
    "activation_ok",
    "no_activation_observed",
    "false_activation",
    "no_false_activation_observed",
    "operationally_invalid",
)


@dataclass(frozen=True)
class ActivationOracleCase:
    identity: str
    activation: str


def _exact_keys(data: dict[str, Any], expected: set[str], label: str) -> None:
    unknown = sorted(set(data) - expected)
    missing = sorted(expected - set(data))
    if unknown:
        raise ValidationError(f"unknown {label} fields: {', '.join(unknown)}")
    if missing:
        raise ValidationError(f"missing {label} fields: {', '.join(missing)}")


def load_activation_oracle(path: Path) -> dict[str, ActivationOracleCase]:
    document = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict):
        raise ValidationError("activation oracle must be an object")
    _exact_keys(
        document,
        {"schema_version", "corpus_id", "description", "cases"},
        "activation oracle",
    )
    if document["schema_version"] != ACTIVATION_ORACLE_SCHEMA_VERSION:
        raise ValidationError(
            f"unsupported activation oracle schema: {document['schema_version']!r}"
        )
    if not isinstance(document["corpus_id"], str) or not document["corpus_id"].strip():
        raise ValidationError("activation oracle corpus_id must be non-empty text")
    if not isinstance(document["description"], str) or not document["description"].strip():
        raise ValidationError("activation oracle description must be non-empty text")
    raw_cases = document["cases"]
    if not isinstance(raw_cases, dict) or not raw_cases:
        raise ValidationError("activation oracle cases must be a non-empty object")

    parsed: dict[str, ActivationOracleCase] = {}
    for identity, payload in raw_cases.items():
        if not isinstance(identity, str) or "@" not in identity:
            raise ValidationError(
                f"activation oracle case key must be case_id@version: {identity!r}"
            )
        if not isinstance(payload, dict):
            raise ValidationError(f"activation oracle case {identity} must be an object")
        _exact_keys(payload, {"activation"}, f"activation oracle case {identity}")
        expectation = payload["activation"]
        if expectation not in EXPECTATIONS:
            raise ValidationError(
                f"unsupported activation expectation for {identity}: {expectation!r}"
            )
        parsed[identity] = ActivationOracleCase(
            identity=identity,
            activation=expectation,
        )
    return parsed


def _walk_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from _walk_strings(child)
    elif isinstance(value, (list, tuple)):
        for child in value:
            yield from _walk_strings(child)


def activation_observed(events: tuple[dict[str, Any], ...]) -> bool:
    for event in events:
        event_type = str(event.get("type", "")).lower()
        values = " ".join(_walk_strings(event)).lower()
        if (
            "skill" in event_type
            and "activat" in event_type
            and "marketing-agent-skills" in values
        ):
            return True

        item = event.get("item")
        if not isinstance(item, dict):
            continue
        if event_type != "item.completed" or item.get("type") != "command_execution":
            continue
        if item.get("exit_code") != 0:
            continue
        if "skill.md" in extract_skill_paths(str(item.get("command", ""))):
            return True
    return False


def classify_activation(
    run: RunRecord,
    oracle: ActivationOracleCase,
) -> dict[str, Any]:
    observed = activation_observed(run.raw_events)

    if observed:
        disposition = (
            "activation_ok"
            if oracle.activation == "required"
            else "false_activation"
        )
    elif run.state in {RunState.COMPLETED, RunState.ACTIVATION_UNVERIFIED}:
        disposition = (
            "no_activation_observed"
            if oracle.activation == "required"
            else "no_false_activation_observed"
        )
    else:
        disposition = "operationally_invalid"

    return {
        "run_id": run.run_id,
        "case_identity": run.case_identity,
        "profile_id": run.profile_id,
        "expectation": oracle.activation,
        "activation_observed": observed,
        "run_state": run.state.value,
        "disposition": disposition,
    }


def build_activation_report(
    cases: Iterable[CaseContract],
    runs: Iterable[RunRecord],
    oracle: dict[str, ActivationOracleCase],
    *,
    results_id: str,
) -> dict[str, Any]:
    case_list = tuple(cases)
    case_map = {case.identity: case for case in case_list}
    if len(case_map) != len(case_list):
        raise ValidationError("activation cases contain duplicate identities")
    if set(case_map) != set(oracle):
        missing = sorted(set(case_map) - set(oracle))
        extra = sorted(set(oracle) - set(case_map))
        details = []
        if missing:
            details.append(f"missing oracle cases: {', '.join(missing)}")
        if extra:
            details.append(f"unknown oracle cases: {', '.join(extra)}")
        raise ValidationError("; ".join(details))

    rows: list[dict[str, Any]] = []
    for run in runs:
        if run.profile_id == "baseline":
            continue
        case = case_map.get(run.case_identity)
        if case is None:
            raise ValidationError(
                f"activation run references unknown case: {run.case_identity}"
            )
        row = classify_activation(run, oracle[run.case_identity])
        row["family"] = case.family
        rows.append(row)

    disposition_counts = Counter(row["disposition"] for row in rows)
    expectation_counts = Counter(row["expectation"] for row in rows)
    observed_counts = Counter(
        row["expectation"] for row in rows if row["activation_observed"]
    )
    family_rows: dict[str, dict[str, int]] = defaultdict(
        lambda: {
            "runs": 0,
            "activation_observed": 0,
            "activation_ok": 0,
            "no_activation_observed": 0,
            "false_activation": 0,
            "no_false_activation_observed": 0,
            "operationally_invalid": 0,
        }
    )
    for row in rows:
        bucket = family_rows[row["family"]]
        bucket["runs"] += 1
        if row["activation_observed"]:
            bucket["activation_observed"] += 1
        bucket[row["disposition"]] += 1

    return {
        "schema_version": ACTIVATION_REPORT_SCHEMA_VERSION,
        "results_id": results_id,
        "skill_run_count": len(rows),
        "expectation_counts": {
            name: expectation_counts.get(name, 0)
            for name in sorted(EXPECTATIONS)
        },
        "activation_observed_by_expectation": {
            name: observed_counts.get(name, 0)
            for name in sorted(EXPECTATIONS)
        },
        "disposition_counts": {
            name: disposition_counts.get(name, 0) for name in DISPOSITIONS
        },
        "families": dict(sorted(family_rows.items())),
        "runs": rows,
    }


def render_activation_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Skill Activation Report",
        "",
        f"Results: `{report['results_id']}`",
        "",
        "## Dispositions",
        "",
        "| Disposition | Count |",
        "| --- | ---: |",
    ]
    for name, count in report["disposition_counts"].items():
        lines.append(f"| {name} | {count} |")

    lines.extend(
        [
            "",
            "## Families",
            "",
            "| Family | Runs | Observed | OK | Miss | False activation | Clean negative | Invalid |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for family, row in report["families"].items():
        lines.append(
            "| "
            + " | ".join(
                [
                    family,
                    str(row["runs"]),
                    str(row["activation_observed"]),
                    str(row["activation_ok"]),
                    str(row["no_activation_observed"]),
                    str(row["false_activation"]),
                    str(row["no_false_activation_observed"]),
                    str(row["operationally_invalid"]),
                ]
            )
            + " |"
        )
    lines.append("")
    return "\n".join(lines)


__all__ = [
    "ActivationOracleCase",
    "activation_observed",
    "build_activation_report",
    "classify_activation",
    "load_activation_oracle",
    "render_activation_markdown",
]
