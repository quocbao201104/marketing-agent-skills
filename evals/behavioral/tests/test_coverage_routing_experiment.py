from __future__ import annotations

import unittest
from pathlib import Path

from evals.behavioral.behavioral_eval.trace import load_oracle
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
SKILL = ROOT / "skills" / "marketing-practitioner" / "SKILL.md"


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

    def test_multi_owner_cases_require_multiple_groups(self) -> None:
        cases = {case.identity: case for case in load_cases(CASES)}
        oracle = load_oracle(ORACLE)
        multi = [
            identity
            for identity, case in cases.items()
            if case.family == "coverage-multi-owner"
        ]
        self.assertEqual(3, len(multi))
        for identity in multi:
            self.assertGreaterEqual(len(oracle[identity].must_load), 3)

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

    def test_dependency_cases_have_ordered_handoffs(self) -> None:
        cases = {case.identity: case for case in load_cases(CASES)}
        oracle = load_oracle(ORACLE)
        dependencies = [
            identity
            for identity, case in cases.items()
            if case.family == "coverage-strategic-dependency"
        ]
        for identity in dependencies:
            self.assertGreaterEqual(len(oracle[identity].handoff), 2)

    def test_founder_sales_dependency_case_preserves_settled_icp(self) -> None:
        oracle = load_oracle(ORACLE)["BEH-COV-DEP-003@1.0.0"]
        self.assertNotIn(
            ("handbook/02-segmentation-icp-and-jtbd.md",),
            oracle.must_load,
        )
        self.assertIn(
            "handbook/02-segmentation-icp-and-jtbd.md",
            oracle.must_not_load,
        )
        self.assertEqual(
            ("founder-sales.selection", "founder-sales.pursuit"),
            oracle.handoff,
        )

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
            "Do not stop after resolving one plausible path while another material unresolved surface remains.",
            text,
        )
        self.assertIn(
            "Apply the stopping rule only after the material open decision surfaces",
            text,
        )


if __name__ == "__main__":
    unittest.main()
