from __future__ import annotations

import importlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


class ExecutionEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(importlib.util.find_spec("semantic_judge_execution"),
                             "execution evidence runner is not implemented")
        self.runner = importlib.import_module("semantic_judge_execution")
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_request_contains_only_one_unmodified_prompt_and_no_tools(self):
        prompt = '{"packet":"Unicode: Việt Nam"}'
        body = self.runner.request_body("openrouter/deepseek-v4-pro", prompt)
        self.assertEqual(body["messages"], [{"role": "user", "content": prompt}])
        self.assertEqual(body["tools"], [])
        self.assertEqual(body["tool_choice"], "none")
        self.assertFalse(body["provider"]["allow_fallbacks"])
        self.assertNotIn("models", body)
        self.assertNotIn("response_format", body)

    def test_evidence_write_never_overwrites(self):
        path = self.root / "response.json"
        self.runner.write_bytes(path, b"original")
        with self.assertRaises(FileExistsError):
            self.runner.write_bytes(path, b"replacement")
        self.assertEqual(path.read_bytes(), b"original")

    def test_direct_request_allows_same_model_provider_failover(self):
        body = self.runner.request_body("deepseek/deepseek-v4-pro", "exact prompt")
        self.assertTrue(body["provider"]["allow_fallbacks"])
        self.assertTrue(body["provider"]["require_parameters"])
        self.assertEqual(body["model"], "deepseek/deepseek-v4-pro")
        self.assertNotIn("models", body)
        self.assertTrue(self.runner.model_matches(body["model"], body["model"]))

    def test_extract_preserves_malformed_model_json_exactly(self):
        text = '```json\n{"broken":\n```'
        raw = json.dumps({"choices": [{"message": {"content": text},
                                       "finish_reason": "stop"}]}).encode()
        content, metadata = self.runner.extract_response(raw)
        self.assertEqual(content, text)
        self.assertIsNone(metadata["content_parse_error"])

    def test_extract_does_not_use_reasoning_as_answer(self):
        raw = b'{"choices":[{"message":{"content":null,"reasoning":"secret rationale"}}]}'
        content, metadata = self.runner.extract_response(raw)
        self.assertEqual(content, "")
        self.assertIsNotNone(metadata["content_parse_error"])

    def test_model_identity_accepts_only_locked_aliases(self):
        model = "openrouter/deepseek-v4-pro"
        self.assertTrue(self.runner.model_matches(model, "deepseek/deepseek-v4-pro"))
        self.assertFalse(self.runner.model_matches(model, "deepseek/deepseek-v4-flash"))
        self.assertFalse(self.runner.model_matches(model, None))

    def test_seal_detects_raw_response_changes(self):
        self.runner.write_bytes(self.root / "raw.bin", b"original")
        self.runner.seal_directory(self.root, "evidence-seal.json")
        self.runner.verify_seal(self.root, "evidence-seal.json")
        (self.root / "raw.bin").write_bytes(b"changed")
        with self.assertRaises(ValueError):
            self.runner.verify_seal(self.root, "evidence-seal.json")

    def test_scoring_rejects_unsealed_evidence(self):
        with self.assertRaises(FileNotFoundError):
            self.runner.claim_scoring(self.root)
        self.assertFalse((self.root / "scoring-started.json").exists())

    def test_scoring_can_be_claimed_only_once(self):
        self.runner.write_json(self.root / "collection.json", {"attempt_count": 20})
        self.runner.seal_directory(self.root, "evidence-seal.json")
        self.runner.claim_scoring(self.root)
        with self.assertRaises(FileExistsError):
            self.runner.claim_scoring(self.root)

    def test_short_collection_cannot_be_scored(self):
        self.runner.write_json(self.root / "collection.json", {"attempt_count": 19})
        self.runner.seal_directory(self.root, "evidence-seal.json")
        with self.assertRaises(ValueError):
            self.runner.claim_scoring(self.root)

    def test_prompt_validation_rejects_case_identity_leak(self):
        with self.assertRaises(ValueError):
            self.runner.validate_prompt('{"case_id":"E01-SJ-01"}')


if __name__ == "__main__":
    unittest.main()
