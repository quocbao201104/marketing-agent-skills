from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from evals.behavioral.materialize_activation_variants import (
    MaterializationError,
    materialize,
)


def skill_text(description: str) -> str:
    return (
        "---\n"
        "name: marketing-agent-skills\n"
        f"description: {json.dumps(description)}\n"
        "---\n"
        "\n"
        "# Marketing Practitioner\n"
        "\n"
        "Body stays fixed.\n"
    )


class ActivationVariantMaterializerTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.skill = self.root / "skills" / "marketing-agent-skills"
        self.skill.mkdir(parents=True)
        (self.skill / "SKILL.md").write_text(
            skill_text("current description"),
            encoding="utf-8",
            newline="\n",
        )
        (self.skill / "references").mkdir()
        (self.skill / "references" / "note.md").write_text(
            "unchanged resource\n",
            encoding="utf-8",
            newline="\n",
        )
        self.manifest = self.root / "manifest.json"

    def write_manifest(self, d0: str = "current description") -> None:
        self.manifest.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "experiment_id": "fixture",
                    "base_skill": "skills/marketing-agent-skills",
                    "base_commit": "a" * 40,
                    "constraint": "description only",
                    "variants": {
                        "D0": {
                            "label": "current",
                            "description": d0,
                        },
                        "D1": {
                            "label": "candidate",
                            "description": "candidate description",
                        },
                    },
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )

    def test_materializes_description_only_variants(self) -> None:
        self.write_manifest()
        output = self.root / "generated"

        receipt = materialize(
            manifest_path=self.manifest,
            repo_root=self.root,
            output_root=output,
        )

        self.assertEqual(2, len(receipt["variants"]))
        d0 = output / "D0" / "marketing-agent-skills"
        d1 = output / "D1" / "marketing-agent-skills"
        self.assertIn(
            'description: "current description"',
            (d0 / "SKILL.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            'description: "candidate description"',
            (d1 / "SKILL.md").read_text(encoding="utf-8"),
        )
        self.assertEqual(
            (d0 / "references" / "note.md").read_bytes(),
            (d1 / "references" / "note.md").read_bytes(),
        )
        self.assertIn(
            "Body stays fixed.",
            (d1 / "SKILL.md").read_text(encoding="utf-8"),
        )

    def test_d0_can_preserve_a_frozen_baseline_description(self) -> None:
        self.write_manifest(d0="frozen baseline description")

        materialize(
            manifest_path=self.manifest,
            repo_root=self.root,
            output_root=self.root / "generated",
            selected=("D0",),
        )

        text = (
            self.root
            / "generated"
            / "D0"
            / "marketing-agent-skills"
            / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn(
            'description: "frozen baseline description"',
            text,
        )
        self.assertIn("Body stays fixed.", text)

    def test_refuses_to_overwrite_existing_variant(self) -> None:
        self.write_manifest()
        output = self.root / "generated"
        materialize(
            manifest_path=self.manifest,
            repo_root=self.root,
            output_root=output,
            selected=("D1",),
        )

        with self.assertRaises(MaterializationError):
            materialize(
                manifest_path=self.manifest,
                repo_root=self.root,
                output_root=output,
                selected=("D1",),
            )


if __name__ == "__main__":
    unittest.main()
