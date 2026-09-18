from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from evals.behavioral.behavioral_eval.activation import (
    ActivationOracleCase,
    activation_observed,
    build_activation_report,
    classify_activation,
    load_activation_oracle,
)
from evals.behavioral.behavioral_eval.models import RunRecord, RunState
from evals.behavioral.behavioral_eval.validation import load_cases


ROOT = Path(__file__).resolve().parents[3]
CASES = ROOT / "evals" / "behavioral" / "cases" / "skill-activation-v1.json"
ORACLE = (
    ROOT
    / "evals"
    / "behavioral"
    / "oracles"
    / "skill-activation-v1.activation-oracle.json"
)


def command_event(command: str, exit_code: int = 0) -> dict:
    return {
        "type": "item.completed",
        "item": {
            "type": "command_execution",
            "command": command,
            "exit_code": exit_code,
        },
    }


def run(
    *,
    identity: str = "BEH-ACT-DIR-001@1.0.0",
    state: RunState = RunState.COMPLETED,
    events: tuple[dict, ...] = (),
) -> RunRecord:
    return RunRecord(
        run_id="RUN-ACT",
        case_identity=identity,
        profile_id="current-skill",
        state=state,
        started_at="2026-09-18T00:00:00Z",
        finished_at="2026-09-18T00:00:01Z",
        raw_events=events,
        final_output="answer",
    )


class ActivationObserverTests(unittest.TestCase):
    def test_skill_file_read_is_activation_observed(self) -> None:
        events = (
            command_event(
                "Get-Content -LiteralPath "
                "'.agents\\skills\\marketing-practitioner\\SKILL.md' -Raw"
            ),
        )
        self.assertTrue(activation_observed(events))

    def test_explicit_activation_event_is_observed(self) -> None:
        events = (
            {
                "type": "skill.activation.completed",
                "skill": "marketing-practitioner",
            },
        )
        self.assertTrue(activation_observed(events))

    def test_failed_skill_read_is_not_activation_observed(self) -> None:
        events = (
            command_event(
                "Get-Content -LiteralPath "
                "'.agents\\skills\\marketing-practitioner\\SKILL.md' -Raw",
                exit_code=1,
            ),
        )
        self.assertFalse(activation_observed(events))

    def test_required_observed_is_activation_ok(self) -> None:
        events = (
            command_event(
                "Get-Content -LiteralPath "
                "'.agents\\skills\\marketing-practitioner\\SKILL.md' -Raw"
            ),
        )
        result = classify_activation(
            run(events=events),
            ActivationOracleCase(
                identity="BEH-ACT-DIR-001@1.0.0",
                activation="required",
            ),
        )
        self.assertEqual("activation_ok", result["disposition"])

    def test_required_unobserved_is_miss(self) -> None:
        result = classify_activation(
            run(state=RunState.ACTIVATION_UNVERIFIED),
            ActivationOracleCase(
                identity="BEH-ACT-DIR-001@1.0.0",
                activation="required",
            ),
        )
        self.assertEqual("no_activation_observed", result["disposition"])

    def test_forbidden_observed_is_false_activation(self) -> None:
        events = (
            command_event(
                "Get-Content -LiteralPath "
                "'.agents\\skills\\marketing-practitioner\\SKILL.md' -Raw"
            ),
        )
        result = classify_activation(
            run(identity="BEH-ACT-ADJ-001@1.0.0", events=events),
            ActivationOracleCase(
                identity="BEH-ACT-ADJ-001@1.0.0",
                activation="forbidden",
            ),
        )
        self.assertEqual("false_activation", result["disposition"])

    def test_forbidden_unobserved_is_clean_negative(self) -> None:
        result = classify_activation(
            run(
                identity="BEH-ACT-ADJ-001@1.0.0",
                state=RunState.ACTIVATION_UNVERIFIED,
            ),
            ActivationOracleCase(
                identity="BEH-ACT-ADJ-001@1.0.0",
                activation="forbidden",
            ),
        )
        self.assertEqual(
            "no_false_activation_observed",
            result["disposition"],
        )

    def test_executor_failure_without_activation_is_invalid(self) -> None:
        result = classify_activation(
            run(state=RunState.EXECUTOR_FAILED),
            ActivationOracleCase(
                identity="BEH-ACT-DIR-001@1.0.0",
                activation="required",
            ),
        )
        self.assertEqual("operationally_invalid", result["disposition"])

    def test_oracle_exactly_covers_activation_corpus(self) -> None:
        cases = load_cases(CASES)
        oracle = load_activation_oracle(ORACLE)
        self.assertEqual({case.identity for case in cases}, set(oracle))
        self.assertEqual(24, len(cases))

    def test_report_separates_positive_and_negative_families(self) -> None:
        cases = load_cases(CASES)
        selected = [
            next(case for case in cases if case.case_id == "BEH-ACT-DIR-001"),
            next(case for case in cases if case.case_id == "BEH-ACT-ADJ-001"),
        ]
        oracle = load_activation_oracle(ORACLE)
        observed = (
            command_event(
                "Get-Content -LiteralPath "
                "'.agents\\skills\\marketing-practitioner\\SKILL.md' -Raw"
            ),
        )
        report = build_activation_report(
            selected,
            (
                run(events=observed),
                run(
                    identity="BEH-ACT-ADJ-001@1.0.0",
                    state=RunState.ACTIVATION_UNVERIFIED,
                ),
            ),
            {
                case.identity: oracle[case.identity]
                for case in selected
            },
            results_id="fixture",
        )
        self.assertEqual(1, report["disposition_counts"]["activation_ok"])
        self.assertEqual(
            1,
            report["disposition_counts"]["no_false_activation_observed"],
        )


if __name__ == "__main__":
    unittest.main()
