# Behavioral evaluation harness

This harness compares an isolated no-skill baseline with an exact workspace copy of `marketing-practitioner`. It separates executor and isolation failures from answer quality, seals raw run records, and produces condition-blind review packets. It intentionally does not calculate a single quality score.

## Validate the frozen contracts

```powershell
python -B -m evals.behavioral.behavioral_eval.cli validate --cases evals\behavioral\cases\pilot-v1.json --profiles evals\behavioral\profiles
```

The pilot has 12 cases and two repetitions per arm. The committed profiles pin the model and reasoning effort. Change them deliberately and treat the result as a different executor condition.

## Validate targeted regression corpora

Additive regression corpora are versioned separately from the frozen 12-case pilot. They reuse the same case contract and harness, but they do not change the pilot population or its historical interpretation.

For the external-refinement regressions:

```powershell
python -B -m evals.behavioral.behavioral_eval.cli validate --cases evals\behavioral\cases\external-refinement-regressions-v1.json --profiles evals\behavioral\profiles
```

When running or reporting a targeted corpus, pass its `--cases` path explicitly. The harness currently adjudicates each case independently; opposite-direction controls that share a family are separate cases, not a new cross-case sensitivity-scoring mechanism.

A fixture preflight can exercise the additive corpus without producing behavioral evidence:

```powershell
python -B -m evals.behavioral.behavioral_eval.cli run --cases evals\behavioral\cases\external-refinement-regressions-v1.json --adapter fixture --repeat-limit 1 --results evals\behavioral\results\external-refinement-fixture
```

## Exercise infrastructure with fixtures

```powershell
python -B -m evals.behavioral.behavioral_eval.cli run --adapter fixture --results evals\behavioral\results\fixture-smoke
```

Fixture answers test orchestration, isolation, sealing, and report plumbing only. They are not behavioral evidence.

For a bounded preflight, add one or more `--case-id BEH-...` selectors and `--repeat-limit 1`. These selectors do not modify the frozen case or profile contracts; the effective subset is recorded in the manifest.

## Run the live paired pilot

```powershell
python -B -m evals.behavioral.behavioral_eval.cli run --adapter codex-cli --profile-id baseline --profile-id current-skill --results evals\behavioral\results\pilot-v1
```

Every case/profile/repetition runs in a fresh temporary Git workspace. The baseline workspace contains no `marketing-practitioner` skill. The skill arm copies the repository skill to `.agents/skills/marketing-practitioner` and binds its tree hash before execution. Existing result directories are never overwritten.

Each sealed manifest declares the execution regime as `host-realistic/workspace-isolated`, not hermetic. It records the historical Codex CLI flags and read-only sandbox, categorical inherited host scope, and observed executor versions when available. `--ignore-user-config` suppresses `config.toml`; it does not assert rules isolation. Visibility of user/admin/system/plugin skill metadata and rules remains explicitly `unverified` because the harness does not use `--ignore-rules` or redirect host home/Codex directories.

Review `blind-packets.json` without opening the manifest or run records. Save judgments as:

```json
{
  "judgments": [
    {"blind_id": "5a19...", "disposition": "pass"}
  ]
}
```

Allowed answer dispositions are `pass`, `fail`, and `unresolved`. Then build the paired report:

`blind-index.json` is the sealed mapping used by the report command. Keep it away from reviewers until their judgments are frozen.

```powershell
python -B -m evals.behavioral.behavioral_eval.cli report --results evals\behavioral\results\pilot-v1 --judgments judgments.json --output paired-report.json
```

Generated result bundles are ignored by Git. Preserve only redacted aggregate evidence that has been deliberately audited for release.

## Reconstruct skill-graph walks

Sealed `raw_events` can be replayed against a sidecar route oracle. The oracle is not part of the case schema and is never copied into blind packets. The trace answers which skill nodes were read; it is not an answer-quality score.

```powershell
python -B -m evals.behavioral.behavioral_eval.cli trace --results evals\behavioral\results\pilot-v1 --oracle evals\behavioral\oracles\pilot-v1.route-oracle.json --output evals\behavioral\results\pilot-v1-walk-trace.json --markdown evals\behavioral\reports\pilot-v1-walk-trace.md
```

Use local sealed results when they exist. Do not treat this reconstruction as a reason to edit handbook nodes unless the walk shows the required node was loaded and behavior was still wrong.

## Decision coverage review

Coverage case v1.1.0 separates three observations:

- `trace` reports file/route reads. Schema v3 calls a partial required walk
  `partial_route_coverage`; it never establishes `premature_closure`.
- `report` evaluates each answer against its semantic criteria. With no judgment,
  nonempty coverage answers remain `unresolved`.
- `coverage` reports task-local surface resolution from independent reviewer
  judgments. It does not read route traces or trust executor self-reports.

The coverage route oracle permits relevant reads without requiring every domain
or a fixed read order. The separate `coverage-routing-v1.surface-oracle.json`
contains concrete task questions. These are evaluator questions, not a runtime
form or mandatory output sections. Each can be resolved from supplied evidence,
excluded with a supported materiality judgment, or bounded appropriately.

Review `blind-packets.json` together with the matching surface questions. Keep
profile/arm identities hidden. A reviewer must assess what the answer actually
establishes, whether remaining uncertainty can change the useful result, and
whether the answer claims completion, reports partial work, or awaits necessary
input. A finished model turn does not itself claim task completion.

Save a separate coverage judgment file, with one entry per reviewed blind ID:

```json
{
  "schema_version": 1,
  "judgments": [{
    "blind_id": "<ID from blind-packets.json>",
    "answer_sha256": "<SHA-256 of candidate_answer encoded as UTF-8>",
    "closure": "complete",
    "surfaces": {
      "<surface ID from oracle>": {
        "state": "resolved_by_evidence",
        "material": true,
        "basis": "Explain the supported conclusion and its effect on the requested result.",
        "evidence": [{"source": "answer", "quote": "<exact supporting passage>"}]
      }
    }
  }]
}
```

Include every surface for that case exactly once. Evidence anchors may quote
`prompt` or `answer`. For an omission, cite the relevant prompt obligation and
explain the missing treatment in `basis`; do not invent an answer quotation.
Hashes, exact surface sets, and quotes are checked mechanically. These checks
bind the judgment to the candidate but do not establish semantic entailment:
that remains the independent reviewer's responsibility. If a tool result changes
the decision, its material evidence must be present in the review packet before
it can justify the judgment; otherwise retain `not_assessable`.

Surface states:

- `resolved_by_evidence`: the question is answered with sufficient support.
- `not_material_after_context`: context establishes that it cannot materially
  change the requested result; `material` must be false.
- `bounded_by_limit`: an evidence, authority, or justified inquiry-cost limit is
  explicit and the answer respects it; `material` must be true. Merely saying
  "unknown" while prescribing an unsupported fix is not a valid bound.
- `still_unresolved`: a relevant uncertainty remains unaddressed; `material` is
  true when its impact is established, or null when that impact is unassessable.
- `not_assessable`: the packet cannot support a decision; `material` is null.

`closure` is `complete`, `partial`, `awaiting_input`, or `not_assessable`.
`premature_closure` requires a completed run, independently judged claimed task
completion, and at least one still-unresolved material surface. Partial work or
a necessary question remains `open_dependency`; an honest bounded conclusion may
satisfy coverage. Missing judgments or unassessable conditions remain unresolved.
Coverage satisfaction is not an overall answer-quality or causal-effect claim.

```powershell
python -B -m evals.behavioral.behavioral_eval.cli coverage --cases evals/behavioral/cases/coverage-routing-v1.json --results <sealed-results-directory> --judgments <coverage-judgments.json> --output <new-coverage-report.json>
```

Omit `--judgments` to inspect the unjudged denominator; no completed run passes
by default. Existing reports are never overwritten. Use case versions from the
same sealed experiment. All reviewer judgments and generated reports stay outside
tracked source. A new material surface absent from the frozen oracle requires a
versioned oracle correction, not retroactive success or failure under the old one.
