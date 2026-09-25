from __future__ import annotations

import argparse
import json
import sys
from dataclasses import fields
from pathlib import Path
from typing import Any

from .activation import (
    build_activation_report,
    load_activation_oracle,
    render_activation_markdown,
)
from .models import RunRecord, RunState, ValidationError
from .validation import load_cases


def _record_from_dict(data: dict[str, Any]) -> RunRecord:
    allowed = {item.name for item in fields(RunRecord)}
    unknown = sorted(set(data) - allowed)
    if unknown:
        raise ValidationError(f"unknown run-record fields: {', '.join(unknown)}")
    values = dict(data)
    values["state"] = RunState(values["state"])
    values["raw_events"] = tuple(values.get("raw_events", ()))
    values["limitations"] = tuple(values.get("limitations", ()))
    return RunRecord(**values)


def _write_json(path: Path, payload: Any) -> None:
    if path.exists():
        raise ValidationError(f"refusing to overwrite report: {path.resolve()}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Evaluate top-level Marketing Agent Skills activation"
    )
    parser.add_argument("--cases", type=Path, required=True)
    parser.add_argument("--oracle", type=Path, required=True)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--markdown", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    try:
        args = _parser().parse_args(argv)
        records_path = args.results / "run-records.json"
        if not records_path.is_file():
            raise ValidationError(
                f"run-records.json not found: {records_path.resolve()}"
            )
        document = json.loads(records_path.read_text(encoding="utf-8"))
        if not isinstance(document, dict) or document.get("schema_version") != 1:
            raise ValidationError("unsupported run-record bundle")
        raw_runs = document.get("runs")
        if not isinstance(raw_runs, list):
            raise ValidationError("run-record bundle must contain a runs array")
        runs = [_record_from_dict(item) for item in raw_runs]

        report = build_activation_report(
            load_cases(args.cases),
            runs,
            load_activation_oracle(args.oracle),
            results_id=args.results.name,
        )
        _write_json(args.output, report)

        if args.markdown:
            if args.markdown.exists():
                raise ValidationError(
                    f"refusing to overwrite report: {args.markdown.resolve()}"
                )
            args.markdown.parent.mkdir(parents=True, exist_ok=True)
            args.markdown.write_text(
                render_activation_markdown(report),
                encoding="utf-8",
                newline="\n",
            )
        print(
            "PASS: evaluated "
            f"{report['skill_run_count']} skill-arm activation runs; "
            f"dispositions={report['disposition_counts']}"
        )
        return 0
    except (ValidationError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
