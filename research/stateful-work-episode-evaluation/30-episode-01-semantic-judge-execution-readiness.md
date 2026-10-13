# Episode 01 semantic-judge execution readiness

Status: **REPOSITORY VERIFIED; CONCRETE JUDGE CONFIGURATION NOT FROZEN**

Recorded: 2026-09-10, Asia/Saigon.

## Scope and lineage

This record covers repository verification and execution preparation for the real blinded semantic-judge competence preflight. It does not redesign the approved corpus, establish model competence, or authorize paired work-episode execution.

The user supplied the independent closure verdict `SEMANTIC_JUDGE_FINAL_REPAIR_PASS` and approved proceeding with preparation.

```text
Approved candidate: f967c239aacfe6ae3e4fa85b56e9b64e0f9b4195
Starting HEAD: ecce48287d5295eac4371c01bcb2a9a509df868f
Execution branch: codex/episode-01-semantic-judge-preflight
```

The approved candidate is an ancestor of the execution branch. The only committed difference between the candidate and starting HEAD is the final local closure brief. `evals/work-episodes/episode-01/` and `scripts/verify.ps1` have no committed differences from the approved candidate.

The pre-existing untracked plan at `docs/superpowers/plans/2026-09-09-work-episode-evaluation.md` was preserved. It is not the governing specification for this preflight.

## Completed verification

Executed from the repository root:

```powershell
powershell -NoProfile -File .\scripts\verify.ps1
```

Observed exit code: `0`. Final result: `repository verification: PASS`.

The entrypoint ran package validation, routing validation, Pressure Discovery tests, behavioral harness tests, Episode 01 tests, the existing deterministic Episode 01 preflight, and UTF-8/generated-artifact checks. This is infrastructure/regression evidence only. Output was observed through the task's command log; no standalone full verification transcript was saved during this preparation.

The approved semantic scorer has not been run against real model responses. Any scorer use inside repository unit tests is synthetic regression checking, not the concrete execution's single scoring event.

## Source-resolved versions and fingerprints

Version constants were read programmatically from repository assignments without loading the case corpus for execution guidance:

```text
PROMPT_VERSION = e01-semantic-packet-v3
RUBRIC_VERSION = e01-semantic-rubric-v2
PREFLIGHT_VERSION = e01-semantic-preflight-v2
```

SHA-256 of current working-tree file bytes:

| File under `evals/work-episodes/episode-01/` | SHA-256 |
| --- | --- |
| `semantic_judge.py` | `9858dcfe64ff832fdd48a643bba3c4036659aa2b8e5a5d1183c530b3c8635c82` |
| `semantic_judge_protocol.py` | `ca3ff2d7a36681776efb61ad1bac53c27ab16a796528924879b04406c107ba82` |
| `semantic_judge_preflight.py` | `9a9a053407cb7223d6a6d0df634110886c549ca8bed1684bd2b2b22adf941ac7` |
| `semantic_judge_cases.py` | `f19f3b45025d510c468509d742f25a333008a108594fc8ce79debeae0d007616` |

These are readiness fingerprints, not an execution-bundle seal or corpus digest. The eventual runner must bind its own source, exact prompt bytes, manifest, configuration, and raw responses before scoring.

## Approved execution interfaces

The repository supplies `semantic_judge_preflight.py export <output_dir>` and `semantic_judge_preflight.py score <responses_dir> --provider <provider> --model <model>`. The scorer's accepted prompt/rubric versions resolve from frozen constants.

The exporter writes blinded prompt files and a manifest; it does not itself implement a provider invocation or the complete evidence sealing required by the handoff. Its output-directory creation allows existing directories, so the execution wrapper must exclusively create a new run directory and reject existing outputs before calling the unchanged exporter.

The scorer consumes one response file per packet. Raw provider responses must be retained separately; extracted model text must not be repaired, reformatted, or replaced to obtain schema acceptance. Its report must be captured with stdout, stderr, exit code, and source hash after the complete execution evidence has been sealed.

## Configuration dependency

No exact provider/model was specified in the handoff or selected in this preparation. The current process reports no `OPENAI_API_KEY`, no `ANTHROPIC_API_KEY`, and no `OPENAI_BASE_URL` environment override. Only presence booleans were inspected; credential files and secret values were not read. This does not establish whether another authorized connection exists elsewhere.

The user has been asked for the intended provider/model and access method, without supplying secrets in chat. No alternative model or credential route has been selected implicitly.

The required invocation boundary is one tool-free, prompt-only request per packet, without repository context, prior packet responses, or retrieval. Ordinary repository-aware agent sessions do not meet that requirement. A valid isolated provider connection must be established before describing configuration as frozen.

Once the model and access method are known, bind available model-version information, reasoning/sampling controls, output limits, timeout, retry and concurrency policy, timestamp, candidate SHA, and runner source SHA in a machine-readable freeze. The proposed mechanical policy is serial execution, no semantic retries, and no automatic transport retries; it becomes binding only in the actual execution freeze. Missing or unavailable model/configuration must stop before packet calls, with no silent fallback.

## Current execution state

```text
execution_configuration_frozen = false
packets_exported_for_concrete_run = 0
judge_packet_calls = 0
real_response_scoring_invocations = 0
semantic_competence_preflight_pass = not established
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

The next dependent step is selecting and verifying the concrete judge connection. The subsequent execution wrapper must export/seal all 20 prompts, preserve every invocation's raw evidence, seal the complete response set, and invoke the approved scorer exactly once. Independent review remains required even if that concrete run passes.
