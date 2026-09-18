from __future__ import annotations

import copy
import hashlib
import unittest
from dataclasses import replace
from pathlib import Path

from evals.behavioral.behavioral_eval.coverage import build_coverage_report, load_coverage_oracle
from evals.behavioral.behavioral_eval.models import CaseContract, RunRecord, RunState, ValidationError
from evals.behavioral.behavioral_eval.report import build_report
from evals.behavioral.behavioral_eval.validation import load_cases


ROOT = Path(__file__).resolve().parents[3]


def fixture():
    case = CaseContract.from_dict({
        "case_id": "COV-TEST", "version": "1.0.0", "family": "coverage",
        "prompt": "Audience is fixed. Diagnose the measurement discrepancy.",
        "input_files": [], "hard_predicates": [{"type": "output_present"}],
        "review_criteria": ["Account for material uncertainty."],
        "forbidden_disclosures": [], "expected_relation": "skill_not_worse",
        "provenance": {"source": "fixture", "frozen_at_commit": "a" * 40},
    })
    run = RunRecord(
        run_id="RUN-1", case_identity=case.identity, profile_id="current-skill",
        state=RunState.COMPLETED, started_at="2026-09-18T00:00:00Z",
        finished_at="2026-09-18T00:00:01Z",
        final_output="The supplied evidence resolves measurement. Audience remains fixed.",
    )
    oracle = {case.identity: {"measurement": "Is the discrepancy resolved?",
                              "audience": "Could audience change the result?"}}
    index = {"schema_version": 1, "bindings": [{"blind_id": "BLIND-1", "run_id": run.run_id}]}
    surface = {"state": "resolved_by_evidence", "material": True,
               "basis": "Planted reviewer judgment for the fixture.",
               "evidence": [{"source": "answer", "quote": "resolves measurement"}]}
    judgment = {"blind_id": "BLIND-1", "answer_sha256": hashlib.sha256(run.final_output.encode()).hexdigest(),
                "closure": "complete", "surfaces": {"measurement": surface,
                "audience": {"state": "not_material_after_context", "material": False,
                    "basis": "The fixed audience does not require reconsideration in this fixture.",
                    "evidence": [{"source": "prompt", "quote": "Audience is fixed."}]}}}
    return case, run, oracle, index, {"schema_version": 1, "judgments": [judgment]}


class CoverageJudgmentTests(unittest.TestCase):
    def setUp(self):
        self.case, self.run, self.oracle, self.index, self.judgments = fixture()

    def result(self):
        return build_coverage_report([self.case], [self.run], self.oracle,
                                     self.index, self.judgments)["runs"][0]

    def surface(self):
        return self.judgments["judgments"][0]["surfaces"]["measurement"]

    def test_supplied_evidence_can_satisfy_coverage_without_route_reads(self):
        self.assertEqual((), self.run.raw_events)
        self.assertEqual("coverage_satisfied", self.result()["disposition"])

    def test_not_material_after_context_does_not_force_strategic_reopening(self):
        result = self.result()
        self.assertEqual("not_material_after_context", result["surfaces"]["audience"]["state"])
        self.assertEqual([], result["neglected_surfaces"])

    def test_route_reads_do_not_clear_a_judged_unresolved_material_question(self):
        self.run = replace(self.run, raw_events=({"type": "fixture_all_routes_loaded"},))
        self.surface()["state"] = "still_unresolved"
        self.assertEqual("premature_closure", self.result()["disposition"])
        self.assertEqual(["measurement"], self.result()["neglected_surfaces"])

    def test_asking_for_material_input_is_not_claimed_completion(self):
        self.surface()["state"] = "still_unresolved"
        self.judgments["judgments"][0]["closure"] = "awaiting_input"
        self.assertEqual("open_dependency", self.result()["disposition"])

    def test_partial_work_preserves_open_dependency_instead_of_passing(self):
        self.surface()["state"] = "still_unresolved"
        self.judgments["judgments"][0]["closure"] = "partial"
        self.assertEqual("open_dependency", self.result()["disposition"])

    def test_honest_limit_can_complete_a_bounded_result(self):
        self.surface()["state"] = "bounded_by_limit"
        self.assertEqual("coverage_satisfied", self.result()["disposition"])

    def test_unknown_materiality_is_not_a_failure_or_pass(self):
        self.surface().update(state="still_unresolved", material=None)
        self.assertEqual("unresolved", self.result()["disposition"])

    def test_not_assessable_cannot_be_promoted_to_coverage(self):
        self.surface().update(state="not_assessable", material=None)
        self.assertEqual("unresolved", self.result()["disposition"])

    def test_missing_judgment_stays_unresolved_even_with_all_route_receipts(self):
        self.run = replace(self.run, raw_events=({"type": "fixture_all_routes_loaded"},))
        self.judgments["judgments"] = []
        self.assertEqual("unresolved", self.result()["disposition"])

    def test_operational_failure_is_not_answer_failure(self):
        self.run = replace(self.run, state=RunState.EXECUTOR_FAILED)
        self.judgments["judgments"] = []
        self.assertEqual("operationally_invalid", self.result()["disposition"])

    def test_judgment_for_failed_run_is_rejected(self):
        self.run = replace(self.run, state=RunState.EXECUTOR_FAILED)
        with self.assertRaises(ValidationError):
            self.result()

    def test_stale_answer_binding_is_rejected(self):
        self.run = replace(self.run, final_output="Different answer")
        with self.assertRaisesRegex(ValidationError, "different answer"):
            self.result()

    def test_quote_must_exist_in_bound_source(self):
        self.surface()["evidence"][0]["quote"] = "not in this answer"
        with self.assertRaisesRegex(ValidationError, "quote not found"):
            self.result()

    def test_executor_self_report_is_not_a_judgment(self):
        self.run = replace(self.run, final_output='{"state":"resolved_by_evidence"}')
        self.judgments["judgments"] = []
        self.assertEqual("unresolved", self.result()["disposition"])

    def test_missing_or_extra_surfaces_are_rejected(self):
        original = copy.deepcopy(self.judgments)
        for operation in ("missing", "extra"):
            with self.subTest(operation=operation):
                self.judgments = copy.deepcopy(original)
                surfaces = self.judgments["judgments"][0]["surfaces"]
                if operation == "missing":
                    surfaces.pop("audience")
                else:
                    surfaces["invented"] = copy.deepcopy(surfaces["audience"])
                with self.assertRaises(ValidationError):
                    self.result()

    def test_duplicate_and_unknown_judgments_are_rejected(self):
        original = copy.deepcopy(self.judgments)
        self.judgments["judgments"].append(copy.deepcopy(self.judgments["judgments"][0]))
        with self.assertRaises(ValidationError):
            self.result()
        self.judgments = original
        self.judgments["judgments"][0]["blind_id"] = "UNKNOWN"
        with self.assertRaises(ValidationError):
            self.result()

    def test_inconsistent_state_materiality_is_rejected(self):
        for state, material in [("not_material_after_context", True),
                                ("bounded_by_limit", False), ("not_assessable", True),
                                ("still_unresolved", False), ("resolved_by_evidence", None),
                                ("still_unresolved", 1)]:
            with self.subTest(state=state, material=material):
                self.surface().update(state=state, material=material)
                with self.assertRaises(ValidationError):
                    self.result()


class CoverageCorpusTests(unittest.TestCase):
    def test_real_corpus_requires_semantic_judgment_in_legacy_report(self):
        cases = load_cases(ROOT / "evals/behavioral/cases/coverage-routing-v1.json")
        _, template, _, _, _ = fixture()
        runs = [replace(template, run_id=f"RUN-{i}-{profile}", case_identity=case.identity,
                        profile_id=profile, final_output="OK.")
                for i, case in enumerate(cases) for profile in ("baseline", "current-skill")]
        report = build_report(cases, runs, [])
        self.assertEqual(24, report["denominators"]["unresolved"])
        self.assertEqual(0, report["paired_dispositions"]["both_pass"])

    def test_surface_oracle_covers_exact_case_versions(self):
        cases = load_cases(ROOT / "evals/behavioral/cases/coverage-routing-v1.json")
        oracle = load_coverage_oracle(ROOT / "evals/behavioral/oracles/coverage-routing-v1.surface-oracle.json")
        self.assertEqual({case.identity for case in cases}, set(oracle))
        self.assertTrue(all(case.review_criteria for case in cases))
        self.assertEqual({"1.1.0"}, {case.version for case in cases})


if __name__ == "__main__":
    unittest.main()
