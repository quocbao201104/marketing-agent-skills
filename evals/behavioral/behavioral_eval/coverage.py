"""Report independently judged decision coverage, never inferred from route reads."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Iterable

from .models import CaseContract, RunRecord, RunState, ValidationError


SURFACE_STATES = {
    "resolved_by_evidence",
    "not_material_after_context",
    "bounded_by_limit",
    "still_unresolved",
    "not_assessable",
}
CLOSURES = {"complete", "partial", "awaiting_input", "not_assessable"}


def _keys(value: object, expected: set[str], label: str) -> None:
    if not isinstance(value, dict) or set(value) != expected:
        raise ValidationError(f"{label} requires exactly {sorted(expected)}")


def _text(value: object, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{label} must be non-empty text")


def load_coverage_oracle(path: Path) -> dict[str, dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    _keys(data, {"schema_version", "corpus_id", "description", "cases"}, "coverage oracle")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ValidationError("unsupported coverage oracle schema")
    _text(data["corpus_id"], "corpus_id")
    _text(data["description"], "description")
    if not isinstance(data["cases"], dict) or not data["cases"]:
        raise ValidationError("coverage oracle requires cases")
    for identity, surfaces in data["cases"].items():
        if "@" not in identity or not isinstance(surfaces, dict) or not surfaces:
            raise ValidationError("coverage case requires identity and surface questions")
        for surface_id, question in surfaces.items():
            _text(surface_id, "surface_id")
            _text(question, "surface question")
    return data["cases"]


def _validate_judgment(judgment: dict, case: CaseContract, run: RunRecord,
                       questions: dict[str, str]) -> None:
    _keys(judgment, {"blind_id", "answer_sha256", "closure", "surfaces"}, "coverage judgment")
    digest = hashlib.sha256((run.final_output or "").encode("utf-8")).hexdigest()
    if judgment["answer_sha256"] != digest:
        raise ValidationError("coverage judgment is bound to a different answer")
    if not isinstance(judgment["closure"], str) or judgment["closure"] not in CLOSURES:
        raise ValidationError("unsupported coverage closure")
    _keys(judgment["surfaces"], set(questions), "judged surfaces")
    for surface in judgment["surfaces"].values():
        _keys(surface, {"state", "material", "basis", "evidence"}, "surface judgment")
        state, material = surface["state"], surface["material"]
        if not isinstance(state, str) or state not in SURFACE_STATES:
            raise ValidationError("unsupported surface state")
        if material is not None and type(material) is not bool:
            raise ValidationError("surface material must be boolean or null")
        if state == "not_material_after_context" and material is not False:
            raise ValidationError("not-material surface requires material=false")
        if state == "bounded_by_limit" and material is not True:
            raise ValidationError("bounded surface requires material=true")
        if state == "not_assessable" and material is not None:
            raise ValidationError("not-assessable surface requires material=null")
        if state == "still_unresolved" and material is False:
            raise ValidationError("use not_material_after_context for immaterial uncertainty")
        if state == "resolved_by_evidence" and material is None:
            raise ValidationError("resolved surface requires assessed materiality")
        _text(surface["basis"], "surface basis")
        evidence = surface["evidence"]
        if not isinstance(evidence, list) or not evidence:
            raise ValidationError("surface judgment requires evidence anchors")
        for anchor in evidence:
            _keys(anchor, {"source", "quote"}, "evidence anchor")
            if anchor["source"] not in ("prompt", "answer"):
                raise ValidationError("evidence source must be prompt or answer")
            _text(anchor["quote"], "evidence quote")
            text = case.prompt if anchor["source"] == "prompt" else run.final_output or ""
            if anchor["quote"] not in text:
                raise ValidationError("coverage evidence quote not found in its source")


def build_coverage_report(
    cases: Iterable[CaseContract],
    runs: Iterable[RunRecord],
    oracle: dict[str, dict[str, str]],
    blind_index: dict,
    judgments: dict,
) -> dict:
    case_list, run_list = tuple(cases), tuple(runs)
    case_map = {case.identity: case for case in case_list}
    run_map = {run.run_id: run for run in run_list}
    if len(case_map) != len(case_list) or len(run_map) != len(run_list):
        raise ValidationError("duplicate coverage case or run identity")
    if set(case_map) != set(oracle):
        raise ValidationError("coverage oracle must exactly cover case identities")
    if any(run.case_identity not in case_map for run in run_list):
        raise ValidationError("coverage run references unknown case")
    _keys(blind_index, {"schema_version", "bindings"}, "blind index")
    _keys(judgments, {"schema_version", "judgments"}, "coverage judgments")
    for doc in (blind_index, judgments):
        if type(doc["schema_version"]) is not int or doc["schema_version"] != 1:
            raise ValidationError("unsupported coverage input schema")
    if not isinstance(blind_index["bindings"], list) or not isinstance(judgments["judgments"], list):
        raise ValidationError("coverage bindings and judgments must be lists")
    bindings: dict[str, str] = {}
    bound_runs: set[str] = set()
    for binding in blind_index["bindings"]:
        _keys(binding, {"blind_id", "run_id"}, "blind binding")
        blind_id, run_id = binding["blind_id"], binding["run_id"]
        _text(blind_id, "blind_id")
        _text(run_id, "run_id")
        if blind_id in bindings or run_id in bound_runs or run_id not in run_map:
            raise ValidationError("duplicate or unknown coverage blind binding")
        bindings[blind_id] = run_id
        bound_runs.add(run_id)
    by_run: dict[str, dict] = {}
    for judgment in judgments["judgments"]:
        _keys(judgment, {"blind_id", "answer_sha256", "closure", "surfaces"}, "coverage judgment")
        _text(judgment["blind_id"], "judgment blind_id")
        run_id = bindings.get(judgment["blind_id"])
        if run_id is None or run_id in by_run:
            raise ValidationError("duplicate or unknown coverage judgment")
        run = run_map[run_id]
        if run.state is not RunState.COMPLETED:
            raise ValidationError("coverage judgment requires a completed run")
        _validate_judgment(judgment, case_map[run.case_identity], run, oracle[run.case_identity])
        by_run[run_id] = judgment

    rows = []
    for run in run_list:
        judgment = by_run.get(run.run_id)
        neglected = []
        if run.state is not RunState.COMPLETED:
            disposition = "operationally_invalid"
        elif judgment is None:
            disposition = "unresolved"
        else:
            surfaces = judgment["surfaces"]
            open_material = [key for key, s in surfaces.items()
                             if s["state"] == "still_unresolved" and s["material"] is True]
            unknown = any(s["state"] == "not_assessable" or s["material"] is None
                          for s in surfaces.values())
            if judgment["closure"] == "complete" and open_material:
                neglected = open_material
                disposition = "premature_closure"
            elif judgment["closure"] == "not_assessable" or unknown:
                disposition = "unresolved"
            elif open_material or judgment["closure"] in {"partial", "awaiting_input"}:
                disposition = "open_dependency"
            else:
                disposition = "coverage_satisfied"
        rows.append({
            "run_id": run.run_id,
            "case_identity": run.case_identity,
            "profile_id": run.profile_id,
            "disposition": disposition,
            "neglected_surfaces": neglected,
            "closure": judgment["closure"] if judgment else None,
            "surfaces": judgment["surfaces"] if judgment else None,
        })
    return {
        "schema_version": 1,
        "purpose": "Decision coverage from independent evidence-anchored judgments; not route compliance or overall answer quality.",
        "counts": dict(Counter(row["disposition"] for row in rows)),
        "runs": rows,
    }
