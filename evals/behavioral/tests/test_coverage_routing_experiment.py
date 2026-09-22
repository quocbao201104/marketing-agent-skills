from __future__ import annotations

import unittest
from pathlib import Path

from evals.behavioral.behavioral_eval.trace import load_oracle
from evals.behavioral.behavioral_eval.coverage import load_coverage_oracle
from evals.behavioral.behavioral_eval.validation import load_cases


ROOT = Path(__file__).resolve().parents[3]
CASES = ROOT / "evals" / "behavioral" / "cases" / "coverage-routing-v1.json"
ORACLE = (
    ROOT
    / "evals"
    / "behavioral"
    / "oracles"
    / "coverage-routing-v1.route-oracle.json"
)
SKILL = ROOT / "skills" / "marketing-agent-skills" / "SKILL.md"


class CoverageRoutingExperimentContractTests(unittest.TestCase):
    def test_case_families_are_balanced(self) -> None:
        cases = load_cases(CASES)
        self.assertEqual(12, len(cases))
        families: dict[str, int] = {}
        for case in cases:
            families[case.family] = families.get(case.family, 0) + 1
        self.assertEqual(
            {
                "coverage-multi-owner": 3,
                "coverage-narrow-sibling": 3,
                "coverage-strategic-dependency": 3,
                "coverage-fast-path": 3,
            },
            families,
        )

    def test_route_oracle_exactly_covers_cases(self) -> None:
        cases = load_cases(CASES)
        oracle = load_oracle(ORACLE)
        self.assertEqual({case.identity for case in cases}, set(oracle))

    def test_multi_owner_cases_have_semantic_questions_not_required_reads(self) -> None:
        cases = load_cases(CASES)
        routes = load_oracle(ORACLE)
        surfaces = load_coverage_oracle(
            ROOT / "evals/behavioral/oracles/coverage-routing-v1.surface-oracle.json"
        )
        for case in cases:
            self.assertFalse(routes[case.identity].must_load)
            self.assertTrue(case.review_criteria)
            if case.family == "coverage-multi-owner":
                self.assertGreaterEqual(len(surfaces[case.identity]), 3)

    def test_narrow_cases_keep_explicit_forbidden_upstream_owners(self) -> None:
        cases = {case.identity: case for case in load_cases(CASES)}
        oracle = load_oracle(ORACLE)
        narrow = [
            identity
            for identity, case in cases.items()
            if case.family == "coverage-narrow-sibling"
        ]
        for identity in narrow:
            self.assertTrue(oracle[identity].must_not_load)

    def test_dependency_cases_do_not_require_route_read_order(self) -> None:
        cases = load_cases(CASES)
        oracle = load_oracle(ORACLE)
        for case in cases:
            if case.family == "coverage-strategic-dependency":
                self.assertFalse(oracle[case.identity].handoff)
                self.assertTrue(oracle[case.identity].may_load)

    def test_founder_sales_dependency_case_preserves_settled_icp(self) -> None:
        oracle = load_oracle(ORACLE)["BEH-COV-DEP-003@1.1.0"]
        self.assertNotIn(
            ("handbook/02-segmentation-icp-and-jtbd.md",),
            oracle.must_load,
        )
        self.assertIn(
            "handbook/02-segmentation-icp-and-jtbd.md",
            oracle.must_not_load,
        )
        self.assertFalse(oracle.handoff)
        self.assertIn("founder-sales.selection", oracle.may_load)
        self.assertIn("founder-sales.pursuit", oracle.may_load)

    def test_fast_path_family_contains_a_true_no_read_case(self) -> None:
        cases = {case.identity: case for case in load_cases(CASES)}
        oracle = load_oracle(ORACLE)
        fast = [
            oracle[identity]
            for identity, case in cases.items()
            if case.family == "coverage-fast-path"
        ]
        self.assertTrue(
            any(item.walk == "fast_path" and not item.must_load for item in fast)
        )

    def test_runtime_candidate_contains_bounded_coverage_control(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn(
            "Localize the open scope, then resolve it.",
            text,
        )
        self.assertIn(
            "do not activate a surface merely because its topic is mentioned",
            text,
        )
        self.assertIn(
            "Before closing, account for other material open questions",
            text,
        )
        self.assertIn(
            "For each material open question, assess whether further information could change",
            text,
        )


if __name__ == "__main__":
    unittest.main()
