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
    / "profiles"
    / "activation-variants-v1.json"
)
SKILL = ROOT / "skills" / "marketing-practitioner" / "SKILL.md"


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

    def test_d0_matches_current_skill_description(self) -> None:
        variants = json.loads(VARIANTS.read_text(encoding="utf-8"))["variants"]
        skill_text = SKILL.read_text(encoding="utf-8")
        current_line = next(
            line for line in skill_text.splitlines() if line.startswith("description:")
        )
        current = json.loads(current_line.split(":", 1)[1].strip())
        self.assertEqual(current, variants["D0"]["description"])

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
