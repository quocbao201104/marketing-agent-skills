"""Prompt-only local-router execution; frozen semantic files are never edited."""
from __future__ import annotations

import argparse
import ast
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
CANDIDATE = "f967c239aacfe6ae3e4fa85b56e9b64e0f9b4195"
MODELS = ("openrouter/deepseek-v4-pro", "openrouter/deepseek-v4-flash")
TIMEOUT = 180
MAX_TOKENS = 16384


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")


def write_bytes(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)


def write_json(path, value):
    write_bytes(path, canonical(value) + b"\n")


def read_json(path):
    return json.loads(path.read_bytes())


def request_body(model, prompt):
    return {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "temperature": 0,
        "max_tokens": MAX_TOKENS,
        "reasoning": {"enabled": True, "exclude": True},
        "tools": [],
        "tool_choice": "none",
        "plugins": [],
        "provider": ({"allow_fallbacks": True, "require_parameters": True}
                     if model.startswith("deepseek/") else {"allow_fallbacks": False}),
    }


def model_matches(requested, observed):
    leaf = requested.removeprefix("openrouter/")
    return observed in {requested, leaf, "deepseek/" + leaf}


def extract_response(raw):
    metadata = {"content_parse_error": None}
    try:
        provider = json.loads(raw)
        metadata.update({k: provider.get(k) for k in
                         ("id", "model", "provider", "system_fingerprint", "usage")})
        choices = provider["choices"]
        if len(choices) != 1:
            raise ValueError("expected exactly one choice")
        choice = choices[0]
        metadata["finish_reason"] = choice.get("finish_reason")
        message = choice["message"]
        metadata["tool_calls_present"] = bool(message.get("tool_calls"))
        content = message.get("content")
        if not isinstance(content, str):
            raise ValueError("content is not a string")
        return content, metadata
    except (ValueError, KeyError, TypeError, IndexError) as exc:
        metadata["content_parse_error"] = type(exc).__name__
        return "", metadata


def seal_directory(root, name):
    files = {p.relative_to(root).as_posix(): digest(p.read_bytes())
             for p in sorted(root.rglob("*")) if p.is_file()}
    seal = {"sealed_at": now(), "files": files,
            "bundle_sha256": digest(canonical(files))}
    write_json(root / name, seal)
    return seal


def verify_seal(root, name):
    seal = read_json(root / name)
    if digest(canonical(seal["files"])) != seal["bundle_sha256"]:
        raise ValueError("seal manifest mismatch")
    for name, expected in seal["files"].items():
        if digest((root / name).read_bytes()) != expected:
            raise ValueError("sealed evidence changed: " + name)


def claim_scoring(root):
    verify_seal(root, "evidence-seal.json")
    if read_json(root / "collection.json")["attempt_count"] != 20:
        raise ValueError("all 20 attempts must be collected before scoring")
    write_json(root / "scoring-started.json", {"started_at": now(), "invocation": 1})


def validate_prompt(prompt):
    if re.search(r"E01-SJ-\d{2}", prompt):
        raise ValueError("case identity leaked")
    forbidden = {"case_id", "expected_applicability", "expected_outcome",
                 "gold_label", "gold_labels", "pressure_control", "skill_condition",
                 "sibling_id"}

    def visit(value):
        if isinstance(value, dict):
            if forbidden.intersection(value):
                raise ValueError("judge-facing metadata leak")
            for item in value.values():
                visit(item)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(json.loads(prompt))
    for label in ('"no-skill"', '"skill-present"', '"pressure"', '"control"'):
        if label in prompt:
            raise ValueError("condition label leaked")


def git(*args):
    result = subprocess.run(["git", *args], cwd=REPO, capture_output=True, check=True)
    return result.stdout.decode("utf-8").strip()


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise urllib.error.HTTPError(req.full_url, code, "redirect refused", headers, fp)


def http_call(url, key, body=None):
    headers = {"Authorization": "Bearer " + key, "Content-Type": "application/json"}
    req = urllib.request.Request(url, data=body, headers=headers)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    start, tick = now(), time.monotonic()
    raw, status, error, exposed_headers = b"", None, None, {}
    try:
        with opener.open(req, timeout=TIMEOUT) as response:
            raw, status = response.read(), response.status
            exposed_headers = {k: response.headers.get(k) for k in
                               ("content-type", "x-request-id", "request-id", "date")}
    except urllib.error.HTTPError as exc:
        raw, status, error = exc.read(), exc.code, "HTTPError"
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        error = type(exc).__name__
    return raw, {"started_at": start, "finished_at": now(),
                 "latency_seconds": time.monotonic() - tick,
                 "http_status": status, "transport_error": error,
                 "response_headers": exposed_headers, "transport_retries": 0}


def versions():
    wanted = {"PROMPT_VERSION", "RUBRIC_VERSION", "PREFLIGHT_VERSION"}
    found = {}
    for name in ("semantic_judge.py", "semantic_judge_preflight.py"):
        for node in ast.parse((ROOT / name).read_text(encoding="utf-8-sig")).body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in wanted:
                        found[target.id] = ast.literal_eval(node.value)
    if set(found) != wanted:
        raise ValueError("frozen versions missing")
    return found


def prepare(root, model, base_url, listing, verification_hash):
    root.mkdir(parents=True, exist_ok=False)
    source_files = {p.name: p.read_bytes() for p in ROOT.glob("*.py")}
    for name, data in source_files.items():
        write_bytes(root / "sources" / name, data)
    available = [m for m in listing["data"] if m.get("id") == model]
    if len(available) != 1:
        raise ValueError("requested model unavailable or ambiguous")
    freeze = {
        "provider": "openrouter" if base_url.startswith("https://openrouter.ai/") else "local-router/openrouter", "base_url": base_url,
        "model": model, "available_model_metadata": available[0],
        "model_snapshot": "not exposed by model catalog; bind each raw response identity",
        "response_model_aliases": [model, model.removeprefix("openrouter/"),
                                   "deepseek/" + model.removeprefix("openrouter/")],
        "versions": versions(), "request_settings": request_body(model, "") ,
        "prompt_replacement": "messages[0].content = exact exported UTF-8 prompt",
        "reasoning_policy": "enabled; exclude reasoning text; effort omitted, provider default",
        "other_sampling_settings": "omitted; provider defaults, not claimed deterministic",
        "tool_access": "disabled", "retrieval_access": "disabled",
        "repository_access": "disabled", "history": "none; one user message only",
        "semantic_retries": 0, "transport_retries": 0, "timeout_seconds": TIMEOUT,
        "concurrency": {"per_model": 1, "across_models": 2},
        "timestamp": now(), "candidate_commit": CANDIDATE,
        "execution_head": git("rev-parse", "HEAD"),
        "branch": git("branch", "--show-current"),
        "git_status_before": git("status", "--short"),
        "runner_sha256": digest(Path(__file__).read_bytes()),
        "source_sha256": {k: digest(v) for k, v in source_files.items()},
        "verification_log_sha256": verification_hash,
        "isolation_boundary": "HTTP body generated here; no tools dispatched or external context supplied",
        "router_internal_transformations": "upstream service internals not observable; raw model/provider metadata retained",
        "parsing": "extract choices[0].message.content exactly; no JSON repair or reasoning fallback",
        "failure_policy": "retain every error; finish 20 attempts; score after full seal; no retries",
        "semantic_judge_adapter_validated": False, "live_trials_permitted": False,
    }
    write_json(root / "execution-freeze.json", freeze)
    exported = subprocess.run([sys.executable, "-B", str(root / "sources" /
                              "semantic_judge_preflight.py"), "export", str(root / "export")],
                              capture_output=True)
    write_bytes(root / "export-stdout.txt", exported.stdout)
    write_bytes(root / "export-stderr.txt", exported.stderr)
    if exported.returncode:
        raise RuntimeError("approved exporter failed")
    manifest = read_json(root / "export" / "manifest.json")
    ids = manifest["packet_ids"]
    if manifest["packet_count"] != 20 or len(ids) != 20 or len(set(ids)) != 20:
        raise ValueError("not exactly 20 unique packets")
    hashes = {}
    for packet in ids:
        if not re.fullmatch(r"[A-Za-z0-9_-]+", packet):
            raise ValueError("unsafe packet filename")
        data = (root / "export" / "prompts" / (packet + ".json")).read_bytes()
        validate_prompt(data.decode("utf-8"))
        hashes[packet] = digest(data)
    write_json(root / "prompt-set.json", {"prompt_sha256": hashes,
               "prompt_set_sha256": digest(canonical(hashes)), "packet_count": 20,
               "corpus_digest": manifest["corpus_digest"], "validated_at": now()})
    seal_directory(root, "pre-execution-seal.json")


def collect(root, key):
    verify_seal(root, "pre-execution-seal.json")
    freeze = read_json(root / "execution-freeze.json")
    manifest = read_json(root / "export" / "manifest.json")
    records = []
    for index, packet in enumerate(manifest["packet_ids"], 1):
        prompt_bytes = (root / "export" / "prompts" / (packet + ".json")).read_bytes()
        payload = canonical(request_body(freeze["model"], prompt_bytes.decode("utf-8")))
        attempt = root / "attempts" / packet
        write_bytes(attempt / "request.json", payload)
        write_json(attempt / "started.json", {"packet_id": packet, "started_at": now()})
        raw, metadata = http_call(freeze["base_url"] + "/chat/completions", key, payload)
        write_bytes(attempt / "raw-response.bin", raw)
        content, parsed = extract_response(raw)
        metadata.update(parsed)
        metadata.update({"packet_id": packet, "request_sha256": digest(payload),
                         "prompt_sha256": digest(prompt_bytes), "raw_response_sha256": digest(raw),
                         "response_text_sha256": digest(content.encode("utf-8")),
                         "model_identity_matches": model_matches(freeze["model"], parsed.get("model"))})
        write_bytes(root / "responses" / (packet + ".json"), content.encode("utf-8"))
        write_json(attempt / "metadata.json", metadata)
        # Syntax-only parsing is retained but never used to retry or score early.
        try:
            parsed_content = json.loads(content)
        except (ValueError, TypeError):
            parsed_content = None
        write_json(attempt / "parsed-content.json", {"parsed": parsed_content})
        records.append(metadata)
        print(f"{freeze['model']}: collected {index}/20; HTTP {metadata['http_status']}", flush=True)
    verify_seal(root, "pre-execution-seal.json")
    write_json(root / "collection.json", {"attempt_count": len(records), "records": records,
               "completed_at": now(), "transport_retries": 0,
               "git_status_after_collection": git("status", "--short")})
    seal_directory(root, "evidence-seal.json")


def score(root):
    claim_scoring(root)
    freeze = read_json(root / "execution-freeze.json")
    command = [sys.executable, "-B", str(root / "sources" / "semantic_judge_preflight.py"),
               "score", str(root / "responses"), "--provider", freeze["provider"],
               "--model", freeze["model"]]
    result = subprocess.run(command, capture_output=True)
    write_bytes(root / "scorer-stdout.txt", result.stdout)
    write_bytes(root / "scorer-stderr.txt", result.stderr)
    write_json(root / "scorer-execution.json", {"exit_code": result.returncode,
               "command": command, "finished_at": now(),
               "scorer_source_sha256": freeze["source_sha256"]["semantic_judge_preflight.py"]})
    report = json.loads(result.stdout)
    write_json(root / "scorer-report.json", report)
    records = read_json(root / "collection.json")["records"]
    identity_ok = all(r["model_identity_matches"] for r in records)
    execution_ok = all(r["http_status"] == 200 and not r["transport_error"]
                       and not r.get("tool_calls_present") for r in records)
    summary = {
        "candidate": CANDIDATE, "execution_branch": freeze["branch"],
        "execution_head": freeze["execution_head"], "provider": freeze["provider"],
        "model": freeze["model"], "judge_id": report["judge_id"],
        "versions": freeze["versions"], "corpus_digest": report["corpus_digest"],
        "packets_executed": len(records), "transport_retries": 0,
        "structurally_accepted": sum(c["structurally_accepted"] for c in report["case_scores"]),
        "semantic_cases_passed": sum(c["passed"] for c in report["case_scores"]),
        "scorer_gate": report["gate"], "model_identity_verified": identity_ok,
        "execution_valid": execution_ok and identity_ok,
        "overall_preflight_gate": report["gate"] if execution_ok and identity_ok else "INVALID",
        "raw_evidence_bundle_digest": read_json(root / "evidence-seal.json")["bundle_sha256"],
        "scorer_report_digest": digest((root / "scorer-report.json").read_bytes()),
        "semantic_competence_preflight_pass": bool(report["semantic_competence_preflight_pass"]
                                                   and execution_ok and identity_ok),
        "semantic_judge_adapter_validated": False, "live_trials_permitted": False,
        "total_latency_seconds": sum(r["latency_seconds"] for r in records),
        "reported_total_tokens": sum((r.get("usage") or {}).get("total_tokens", 0) for r in records),
        "usage_available_count": sum(isinstance(r.get("usage"), dict) for r in records),
    }
    verify_seal(root, "evidence-seal.json")
    write_json(root / "execution-summary.json", summary)
    seal_directory(root, "final-seal.json")
    print(json.dumps(summary, sort_keys=True), flush=True)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True, type=Path)
    parser.add_argument("--base-url", default="http://localhost:20128/v1")
    parser.add_argument("--verification-log", required=True, type=Path)
    args = parser.parse_args()
    if args.base_url not in {"http://localhost:20128/v1", "https://openrouter.ai/api/v1"}:
        raise ValueError("endpoint is not explicitly authorized")
    models = (tuple("deepseek/" + m.removeprefix("openrouter/") for m in MODELS)
              if args.base_url.startswith("https://openrouter.ai/") else MODELS)
    key = os.environ.get("EPISODE_JUDGE_KEY")
    if not key:
        raise ValueError("EPISODE_JUDGE_KEY is required")
    git("merge-base", "--is-ancestor", CANDIDATE, "HEAD")
    frozen_paths = [str(p.relative_to(REPO)).replace("\\", "/")
                    for p in ROOT.glob("*.py") if p.name != Path(__file__).name]
    if git("diff", CANDIDATE, "--", *frozen_paths):
        raise ValueError("approved semantic sources changed")
    base = args.results.resolve()
    base.mkdir(parents=True, exist_ok=False)
    verification = args.verification_log.read_bytes()
    if b"repository verification: PASS" not in verification:
        raise ValueError("successful repository verification log required")
    write_bytes(base / "repository-verification.txt", verification)
    raw, status = http_call(args.base_url + "/models", key)
    if status["http_status"] != 200:
        raise ValueError("model catalog unavailable; no packet executed")
    listing = json.loads(raw)
    if not set(models).issubset({m["id"] for m in listing["data"]}):
        raise ValueError("requested model missing; no packet executed")
    # Persist only requested model descriptors; no credential-bearing request headers.
    write_json(base / "model-catalog.json", {"data": [m for m in listing["data"]
                                                      if m["id"] in models]})
    roots = [base / model.split("/")[-1] for model in models]
    for root, model in zip(roots, models):
        prepare(root, model, args.base_url, listing, digest(verification))
    sets = [read_json(root / "prompt-set.json")["prompt_set_sha256"] for root in roots]
    if len(set(sets)) != 1:
        raise ValueError("models did not receive identical prompt sets")
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(collect, root, key) for root in roots]
        for future in futures:
            future.result()
    # No model remains active when either scorer first accesses expected outcomes.
    summaries = [score(root) for root in roots]
    write_json(base / "comparison.json", summaries)
    seal_directory(base, "batch-seal.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
