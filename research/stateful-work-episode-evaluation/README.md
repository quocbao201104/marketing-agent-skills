# Stateful Work Episode Evaluation Research

Status: **EVALUATION HARNESS / EMPIRICAL ORACLE**

This directory preserves the comprehensive research lineage, methodology specifications, fixture designs, adversarial reviews, and judge provenance repairs establishing the **Stateful Work Episode Evaluation harness** (`evals/work-episodes/`).

The research addresses the fundamental inadequacy of conventional synthetic LLM benchmarks (single-turn Q&A, multiple-choice tests, surface-level text similarity) for assessing marketing agent reliability. It establishes an authentic, multi-phase, state-mutating work-episode methodology—instantiated in Episode 01—with deterministic preflight gates, stateful artifacts, and evidence-grounded semantic judges.

## Governing Question

> How can agent performance on authentic, multi-turn marketing operations be rigorously evaluated across mutating state and complex deliverables without relying on synthetic benchmarks or uncalibrated, ungrounded LLM judges?

Key assumptions rejected during scoping:
- Single-turn synthetic questions provide reliable signal on multi-step marketing competence.
- An ungrounded LLM judge with generic scoring rubrics (1–5) can reliably evaluate strategic marketing decisions.
- Evaluation fixtures can be run without strict deterministic preflight and artifact integrity checks.

## Disposition

```text
STATUS: EVALUATION HARNESS / EMPIRICAL ORACLE COMPLETE
RUNTIME TARGET: evals/work-episodes/episode-01/ (preflight.py, fixtures, test suite)
TEST SUITE: evals/work-episodes/episode-01/tests/
METHODOLOGY: Deterministic preflight + evidence-grounded semantic judge
```

- **Runtime Target**: `evals/work-episodes/episode-01/` and repository verification gate (`verify.ps1`).
- **Mechanisms Added**: Multi-phase state-mutating work episodes, sealed evaluation fixtures, deterministic preflight validation, and calibrated semantic judges.
- **Expansions Rejected**: Synthetic leaderboard rankings, non-reproducible crowd-sourced evaluations, and single-turn benchmark dumps.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-research-brief.md`](01-research-brief.md) | Research brief establishing the need for stateful, multi-phase agent evaluation | Research Brief |
| [`02-evidence-synthesis.md`](02-evidence-synthesis.md) | Synthesis of literature on multi-turn agent evaluation, tool use, and state drift | Evidence Synthesis |
| [`03-stateful-work-episode-methodology.md`](03-stateful-work-episode-methodology.md) | Core specification of the stateful work episode methodology and lifecycle | Core Methodology |
| [`04-post-review-repair.md`](04-post-review-repair.md) | Bounded repairs addressing peer review feedback on state isolation and reproducibility | Post-Review Repair |
| [`05-post-repair-verification-brief.md`](05-post-repair-verification-brief.md) | Verification specification certifying core methodology repair | Verification Brief |
| [`05a-post-repair-verification-result.md`](05a-post-repair-verification-result.md) | Independent verification results confirming methodology stability | Verification Result |
| [`06-episode-01-design.md`](06-episode-01-design.md) | Detailed design specification for Episode 01 (B2B SaaS Positioning & Go-To-Market) | Episode Design |
| [`07-episode-01-evaluator-fixtures.md`](07-episode-01-evaluator-fixtures.md) | Design and checksums for immutable evaluator input fixtures and artifacts | Fixtures Design |
| [`08-independent-episode-01-review-brief.md`](08-independent-episode-01-review-brief.md) | Independent review brief examining Episode 01 realism and scoring rubrics | Review Brief |
| [`09-episode-01-independent-review-result.md`](09-episode-01-independent-review-result.md) | Peer review results assessing Episode 01 evaluation rigor | Review Result |
| [`10`–`15` Series] | Implementation repairs, closure verification briefs, and results for Episode 01 harness | Implementation Pass |
| [`16`–`18` Series] | Semantic applicability repairs and closure verification for evaluation criteria | Applicability Pass |
| [`19`–`20` Series] | Semantic judge provenance repairs ensuring scores cite ground-truth oracle evidence | Judge Provenance |
| [`30-episode-01-semantic-judge-execution-readiness.md`](30-episode-01-semantic-judge-execution-readiness.md) | Final readiness audit certifying Episode 01 semantic judge execution capabilities | Readiness Audit |

Related historical audits & regressions:
- [`../historical-audits/prebenchmark-runtime-smoke.md`](../historical-audits/prebenchmark-runtime-smoke.md)

## Protected Invariants

```text
STATEFUL WORK EPISODE != SYNTHETIC QA BENCHMARK
SEMANTIC JUDGE PROVENANCE = GROUNDED IN EXPLICIT ORACLE EVIDENCE
DETERMINISTIC PREFLIGHT MUST PASS BEFORE LIVE MODEL EVALUATION
FIXTURE RUNS != EMPIRICAL BEHAVIORAL EVIDENCE (THEY VERIFY HARNESS PLUMBING ONLY)
SEALED ARTIFACT INTEGRITY CANNOT BE MUTATED BY RUNTIME
```

- Episode fixtures verify orchestration and plumbing; they must not be cited as live behavioral proof.
- Semantic judge judgments must cite specific, documented oracle evidence; unanchored subjective grading is rejected.
- All evaluation runs require deterministic preflight verification (`evals/work-episodes/episode-01/preflight.py`).
