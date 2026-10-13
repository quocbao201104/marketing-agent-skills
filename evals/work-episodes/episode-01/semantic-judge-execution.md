# Real semantic-judge execution through the local router

The additive `semantic_judge_execution.py` runner executes the user-selected
`openrouter/deepseek-v4-pro` and `openrouter/deepseek-v4-flash` models as separate
20-packet preflights. It leaves the approved exporter, corpus, protocol, adapter,
and scorer unchanged.

## Invocation and isolation boundary

Supply the router credential through the process environment variable
`EPISODE_JUDGE_KEY`. Do not write the value to repository files, command logs,
request-body records, or published reports. The supported endpoint for this
concrete execution is `http://localhost:20128/v1`.

Every HTTP request contains exactly one user message: the unchanged rendered
packet prompt. No system/developer message, previous response, repository path,
tool definition, gold label, or agent context is appended. Tool use is disabled;
the runner never dispatches tool calls. Redirects and environment HTTP proxies
are disabled in the HTTP client.

The request fixes temperature at zero, maximum tokens at 16,384, reasoning
enabled with reasoning text excluded, no tool choice, no plugins, and provider
fallback disabled. The model catalog and raw response identities are retained.
Other sampling settings are omitted and therefore remain provider defaults.
These settings follow the [OpenRouter request schema](https://openrouter.ai/docs/api_reference/overview).

This establishes the client request boundary. It does not independently expose
or certify transformations inside the local router or its upstream provider.
Do not describe an undisclosed model snapshot or internal router behavior as
verified. Each run's summary distinguishes returned model identity from its
requested identifier, accepting only the aliases listed before execution.

## Frozen execution policy

- One serial worker per model; at most two model requests active across the batch.
- A 180-second HTTP operation timeout, no semantic retries, and no automatic
  transport retries.
- Twenty requests scheduled for each model, including transport failures.
  Errors remain failed attempts; another packet is not a replacement attempt.
- Each model receives an identical sealed prompt set in the exporter's order.
- Request bodies, raw HTTP response bodies, extracted content, syntax-only
  parsing, timestamps, exposed identity/usage, and errors are retained separately.
- Malformed content is never repaired. Missing content produces an empty scorer
  input, with the original raw response and extraction error retained.
- Both collections finish and are sealed before either semantic scorer runs.
- An exclusive scoring marker permits only one scorer invocation per run.
- Model identity or transport failures make the overall execution `INVALID`,
  even when a scorer report is available. Scorer errors are not evidence that a
  model answered the affected packets incorrectly.
- `semantic_judge_adapter_validated` and `live_trials_permitted` remain false.

## Reproduction

First run the repository verification entrypoint and save its output. The
runner requires that successful verification log. From the repository root,
with the environment variable already supplied:

```powershell
python -B evals/work-episodes/episode-01/semantic_judge_execution.py --results evals/behavioral/results/semantic-judge-deepseek-NEW-RUN --verification-log evals/behavioral/results/judge-preparation-20260910/verification.txt
```

Choose a new, unused result directory for every execution. The command refuses
existing output directories. It does not resume or overwrite an earlier batch.
The runner freezes its source bytes and all Episode 01 Python sources into each
run; exporter and scorer subprocesses use those copies. Source hashes, Git HEAD,
branch, untracked changes, and the approved candidate are recorded explicitly.

Each model directory contains `execution-freeze.json`, exported prompts and
manifest, `prompt-set.json`, `pre-execution-seal.json`, per-packet attempt records,
`collection.json`, and `evidence-seal.json`. After the single scoring call it also
contains scorer stdout/stderr, exit metadata, `scorer-report.json`,
`execution-summary.json`, and `final-seal.json`. The parent batch contains
`comparison.json` and `batch-seal.json`.

Seals are content-addressed manifests verified before and after scoring. They
detect changes to the recorded bytes; they are not an independent timestamping
service or a guarantee against a party replacing an entire bundle.

Keep raw bundles under ignored results. A tracked report must omit credentials,
upstream account identifiers, and private host details. A passing concrete run
requires independent review before any judge-validation or live-trial gate can
change. A failed or invalid run must be preserved without immediate tuning or
replacement of individual answers.
