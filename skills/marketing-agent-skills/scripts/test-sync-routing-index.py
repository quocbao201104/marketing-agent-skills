#!/usr/bin/env python3
"""Deterministic unit test suite for sync-routing-index.py."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

# Load sync-routing-index module dynamically
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
SYNC_SCRIPT = ROOT / "scripts" / "sync-routing-index.py"
GET_SCRIPT = ROOT / "scripts" / "get-knowledge.py"

spec_sync = importlib.util.spec_from_file_location("sync_routing_index", SYNC_SCRIPT)
if spec_sync is None or spec_sync.loader is None:
    raise RuntimeError(f"cannot load {SYNC_SCRIPT}")
sync_mod = importlib.util.module_from_spec(spec_sync)
import sys
sys.modules["sync_routing_index"] = sync_mod
spec_sync.loader.exec_module(sync_mod)

spec_get = importlib.util.spec_from_file_location("get_knowledge", GET_SCRIPT)
if spec_get is None or spec_get.loader is None:
    raise RuntimeError(f"cannot load {GET_SCRIPT}")
get_mod = importlib.util.module_from_spec(spec_get)
sys.modules["get_knowledge"] = get_mod
spec_get.loader.exec_module(get_mod)


class TestSyncRoutingIndex(unittest.TestCase):
    def test_clean_baseline(self) -> None:
        """Verify that the repository's current manifest reports zero drift."""
        manifest, audits = sync_mod.run_audit(
            manifest_path=ROOT / "routing-index.json",
            skill_root=ROOT,
        )
        self.assertEqual(289, len(audits))
        drift_or_error = [
            a for a in audits if a.status != sync_mod.DriftStatus.CLEAN
        ]
        self.assertEqual([], drift_or_error)

    def test_renamed_heading_detection_and_repair(self) -> None:
        """Verify drift detection and safe sync when a heading is renamed."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_root = Path(tmp_dir)

            # Create mock markdown file
            md_path = tmp_root / "test-chapter.md"
            md_path.write_text(
                "# Title\n\n## 1. Original concept\nContent here.\n\n## 2. Unrelated section\nMore content.\n",
                encoding="utf-8",
            )

            # Create mock manifest
            manifest_data = {
                "version": 2,
                "format": "grouped-semantic-routing",
                "notes": "Test manifest",
                "namespaces": {
                    "test-ns": {
                        "path": "test-chapter.md",
                        "sections": {
                            "concept": "## 1. Original concept",
                            "other": "## 2. Unrelated section",
                        },
                    }
                },
            }
            manifest_file = tmp_root / "routing-index.json"
            manifest_file.write_text(
                sync_mod.format_manifest(manifest_data), encoding="utf-8"
            )

            # Baseline check: clean
            _, audits = sync_mod.run_audit(
                manifest_path=manifest_file, skill_root=tmp_root
            )
            self.assertTrue(all(a.status == sync_mod.DriftStatus.CLEAN for a in audits))

            # Simulate author renaming heading: "## 1. Original concept" -> "## 1. Original concept and framing"
            md_path.write_text(
                "# Title\n\n## 1. Original concept and framing\nContent here.\n\n## 2. Unrelated section\nMore content.\n",
                encoding="utf-8",
            )

            # Check audit: must detect RENAMED_HEADING
            _, audits_drift = sync_mod.run_audit(
                manifest_path=manifest_file, skill_root=tmp_root
            )
            concept_audit = next(a for a in audits_drift if a.section == "concept")
            self.assertEqual(sync_mod.DriftStatus.RENAMED_HEADING, concept_audit.status)
            self.assertEqual("## 1. Original concept and framing", concept_audit.proposed_selector)
            self.assertGreater(concept_audit.confidence, 0.70)

            # Dry-run check: sync_mod.main with --dry-run
            ret_dry = sync_mod.main([
                "--dry-run",
                "--manifest",
                str(manifest_file),
            ])
            self.assertEqual(0, ret_dry)

            # File should not have changed after dry-run
            loaded_after_dry = json.loads(manifest_file.read_text(encoding="utf-8"))
            self.assertEqual("## 1. Original concept", loaded_after_dry["namespaces"]["test-ns"]["sections"]["concept"])

            # Run actual sync
            ret_sync = sync_mod.main([
                "--sync",
                "--manifest",
                str(manifest_file),
            ])
            self.assertEqual(0, ret_sync)

            # Verify manifest updated
            loaded_after_sync = json.loads(manifest_file.read_text(encoding="utf-8"))
            self.assertEqual(
                "## 1. Original concept and framing",
                loaded_after_sync["namespaces"]["test-ns"]["sections"]["concept"],
            )

            # Subsequent check is now clean
            ret_clean = sync_mod.main([
                "--check",
                "--manifest",
                str(manifest_file),
            ])
            self.assertEqual(0, ret_clean)

    def test_renumbered_heading_matching(self) -> None:
        """Verify detection when a heading's section number changes."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_root = Path(tmp_dir)
            md_path = tmp_root / "test-chapter.md"
            md_path.write_text(
                "# Title\n\n## 5. Pricing and terms\nContent.\n",
                encoding="utf-8",
            )

            manifest_data = {
                "version": 2,
                "format": "grouped-semantic-routing",
                "notes": "Test",
                "namespaces": {
                    "test-ns": {
                        "path": "test-chapter.md",
                        "sections": {
                            "pricing": "## 4. Pricing and terms",
                        },
                    }
                },
            }
            manifest_file = tmp_root / "routing-index.json"
            manifest_file.write_text(sync_mod.format_manifest(manifest_data), encoding="utf-8")

            _, audits = sync_mod.run_audit(manifest_path=manifest_file, skill_root=tmp_root)
            self.assertEqual(1, len(audits))
            self.assertEqual(sync_mod.DriftStatus.RENUMBERED, audits[0].status)
            self.assertEqual("## 5. Pricing and terms", audits[0].proposed_selector)

    def test_explicit_marker_anchor(self) -> None:
        """Verify that an explicit route marker anchors even if heading text changed completely."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_root = Path(tmp_dir)
            md_path = tmp_root / "test-chapter.md"
            md_path.write_text(
                "# Title\n\n<!-- route:id test-ns.core -->\n## Completely radically transformed heading\nContent.\n",
                encoding="utf-8",
            )

            manifest_data = {
                "version": 2,
                "format": "grouped-semantic-routing",
                "notes": "Test",
                "namespaces": {
                    "test-ns": {
                        "path": "test-chapter.md",
                        "sections": {
                            "core": "## Old classic heading",
                        },
                    }
                },
            }
            manifest_file = tmp_root / "routing-index.json"
            manifest_file.write_text(sync_mod.format_manifest(manifest_data), encoding="utf-8")

            _, audits = sync_mod.run_audit(manifest_path=manifest_file, skill_root=tmp_root)
            self.assertEqual(1, len(audits))
            self.assertEqual(sync_mod.DriftStatus.MARKER_MATCH, audits[0].status)
            self.assertEqual("## Completely radically transformed heading", audits[0].proposed_selector)
            self.assertEqual(1.0, audits[0].confidence)

    def test_ambiguity_rejection(self) -> None:
        """Verify that ambiguous competing candidates are rejected without corrupting index."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_root = Path(tmp_dir)
            md_path = tmp_root / "test-chapter.md"
            # Two headings with similar title and same level
            md_path.write_text(
                "# Title\n\n## Analytics and reporting overview\nContent.\n\n## Analytics and reporting metrics\nContent.\n",
                encoding="utf-8",
            )

            manifest_data = {
                "version": 2,
                "format": "grouped-semantic-routing",
                "notes": "Test",
                "namespaces": {
                    "test-ns": {
                        "path": "test-chapter.md",
                        "sections": {
                            "reporting": "## Analytics and reporting",
                        },
                    }
                },
            }
            manifest_file = tmp_root / "routing-index.json"
            manifest_file.write_text(sync_mod.format_manifest(manifest_data), encoding="utf-8")

            _, audits = sync_mod.run_audit(manifest_path=manifest_file, skill_root=tmp_root)
            self.assertEqual(1, len(audits))
            self.assertEqual(sync_mod.DriftStatus.AMBIGUOUS, audits[0].status)

    def test_canonical_formatting_roundtrip(self) -> None:
        """Verify that format_manifest reproduces routing-index.json cleanly."""
        manifest_path = ROOT / "routing-index.json"
        original_text = manifest_path.read_text(encoding="utf-8").replace("\r\n", "\n")
        manifest_data = sync_mod.load_manifest(manifest_path)
        formatted_text = sync_mod.format_manifest(manifest_data).replace("\r\n", "\n")
        self.assertEqual(original_text.strip(), formatted_text.strip())


if __name__ == "__main__":
    unittest.main()
