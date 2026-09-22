from __future__ import annotations

import json
import unittest
from pathlib import Path

from evals.behavioral.behavioral_eval.activation import load_activation_oracle
from evals.behavioral.behavioral_eval.validation import load_cases, load_profiles


ROOT = Path(__file__).resolve().parents[3]
CASES = ROOT / "evals" / "behavioral" / "cases" / "skill-activation-v1.json"
ORACLE = (
    ROOT
    / "evals"
    / "behavioral"
    / "oracles"
    / "skill-activation-v1.activation-oracle.json"
)
VARIANTS = (
    ROOT
    / "evals"
    / "behavioral"
    / "variants"
    / "skill-activation-descriptions-v1.json"
)
PROFILES = (
    ROOT
    / "evals"
    / "behavioral"
    / "experiments"
    / "skill-activation-v1"
    / "profiles.json"
)
SKILL = ROOT / "skills" / "marketing-agent-skills" / "SKILL.md"
SPLITS = (
    ROOT
    / "evals"
    / "behavioral"
    / "experiments"
    / "skill-activation-v1"
    / "splits.json"
)


class SkillActivationExperimentContractTests(unittest.TestCase):
    def test_case_families_are_balanced(self) -> None:
        cases = load_cases(CASES)
        self.assertEqual(24, len(cases))
        families: dict[str, int] = {}
        for case in cases:
            families[case.family] = families.get(case.family, 0) + 1
        self.assertEqual(
            {
                "activation-direct": 4,
                "activation-paraphrase": 4,
                "activation-symptom": 4,
                "activation-noisy": 4,
                "activation-adjacent-negative": 4,
                "activation-noun-trap-negative": 4,
            },
            families,
        )

    def test_oracle_exactly_covers_cases(self) -> None:
        cases = load_cases(CASES)
        oracle = load_activation_oracle(ORACLE)
        self.assertEqual({case.identity for case in cases}, set(oracle))
        required = sum(item.activation == "required" for item in oracle.values())
        forbidden = sum(item.activation == "forbidden" for item in oracle.values())
        self.assertEqual(16, required)
        self.assertEqual(8, forbidden)

    def test_four_description_profiles_are_frozen(self) -> None:
        profiles = load_profiles(PROFILES, live=True)
        self.assertEqual(
            {
                "activation-d0",
                "activation-d1",
                "activation-d2",
                "activation-d3",
            },
            {profile.profile_id for profile in profiles},
        )
        self.assertEqual({"gpt-5.6-terra"}, {profile.model for profile in profiles})
        self.assertEqual({"medium"}, {profile.reasoning_effort for profile in profiles})
        self.assertEqual({2}, {profile.repetitions for profile in profiles})

    def test_runtime_candidate_matches_d3_while_d0_remains_frozen(self) -> None:
        variants = json.loads(VARIANTS.read_text(encoding="utf-8"))["variants"]
        skill_text = SKILL.read_text(encoding="utf-8")
        current_line = next(
            line for line in skill_text.splitlines() if line.startswith("description:")
        )
        current = json.loads(current_line.split(":", 1)[1].strip())
        self.assertEqual(current, variants["D3"]["description"])
        self.assertNotEqual(current, variants["D0"]["description"])


    def test_splits_are_disjoint_and_cover_all_cases(self) -> None:
        cases = load_cases(CASES)
        document = json.loads(SPLITS.read_text(encoding="utf-8"))
        splits = document["splits"]
        self.assertEqual(14, len(splits["development"]))
        self.assertEqual(6, len(splits["holdout"]))
        self.assertEqual(4, len(splits["challenge"]))
        flattened = [case_id for values in splits.values() for case_id in values]
        self.assertEqual(len(flattened), len(set(flattened)))
        self.assertEqual({case.case_id for case in cases}, set(flattened))

    def test_description_variants_stay_in_comparable_word_budget(self) -> None:
        variants = json.loads(VARIANTS.read_text(encoding="utf-8"))["variants"]
        counts = {
            variant_id: len(spec["description"].split())
            for variant_id, spec in variants.items()
        }
        for variant_id, count in counts.items():
            self.assertGreaterEqual(count, 75, variant_id)
            self.assertLessEqual(count, 110, variant_id)


if __name__ == "__main__":
    unittest.main()
