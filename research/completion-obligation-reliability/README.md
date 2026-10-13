# Completion Obligation Reliability Research

Status: **THEORY VERIFIED — STATIC RUNTIME INTEGRATED**

This directory preserves the research lineage, targeted regression contracts, and adjudication records establishing **completion obligation reliability and fail-closed behavioral contracts** in the Marketing Practitioner runtime.

The research investigates the failure mode where agents prematurely terminate complex tasks, satisfy only partial subsets of compound requests, or silently hallucinate missing prerequisites rather than failing closed or surfacing explicit boundary blockers.

## Governing Question

> How can runtime controller contracts enforce reliable, exhaustive satisfaction of all active requested outcomes while failing closed when inputs or evidence are insufficient?

Key assumptions rejected during scoping:
- An agent providing a plausible conversational closing has satisfied its completion obligation.
- Missing practitioner prerequisites should be silently assumed or inferred to avoid interrupting the user.

## Disposition

```text
STATUS: STATIC RUNTIME INTEGRATED
RUNTIME TARGET: skills/marketing-agent-skills/SKILL.md (Useful Completion clauses)
REGRESSION CORPUS: evals/behavioral/cases/completion-obligation-reliability-v1.json
EVALUATION PROTOCOL: Fail-closed behavioral reporter
```

- **Runtime Target**: `skills/marketing-agent-skills/SKILL.md` (`Useful completion` section) and the behavioral evaluation harness.
- **Mechanisms Added**: Strict completion obligation accounting, fail-closed prerequisite gates, and explicit boundary declarations for unresolvable unknowns.
- **Expansions Rejected**: Conversational filler generation, speculative assumption guessing, and open-ended iterative task loops.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-theory-freeze.md`](01-theory-freeze.md) | Formal theory freeze defining completion obligations, obligation types, and failure states | Theory Freeze |
| [`02-targeted-regression-contract.md`](02-targeted-regression-contract.md) | Frozen adversarial regression contract covering multi-part and gated obligations | Regression Contract |
| [`03-live-evaluation-design.md`](03-live-evaluation-design.md) | Experimental protocol for measuring completion fidelity across model families | Evaluation Design |
| [`04-static-implementation-adjudication.md`](04-static-implementation-adjudication.md) | Independent adjudication of static controller implementation repairs | Adjudication |
| [`05-independent-review-corrections.md`](05-independent-review-corrections.md) | Bounded repairs addressing independent review critique on action boundaries | Review Corrections |
| [`06-reporter-and-input-corrections.md`](06-reporter-and-input-corrections.md) | Evaluation harness reporter corrections and input normalization contracts | Reporter Corrections |

Related historical audits & regressions:
- [`../historical-audits/cross-layer-promotion-regressions.md`](../historical-audits/cross-layer-promotion-regressions.md)
- [`../historical-audits/subagent-coordination-bounded-cases.md`](../historical-audits/subagent-coordination-bounded-cases.md)

## Protected Invariants

```text
USEFUL COMPLETION != CONVERSATIONAL CLOSURE
REQUESTED OUTCOME != OPTIONAL ADVISORY
MISSING PREREQUISITE → FAIL CLOSED / DECLARE BLOCKER
UNSUPPORTED QUESTION → RETAIN AS UNKNOWN (NEVER INVENT)
SETTLED DECISION → PRESERVE (DO NOT REOPEN)
```

- All active requested outcomes must be completely satisfied before declaring a task complete.
- When an input prerequisite is absent and cannot be derived from supplied state, declare it explicitly as an open dependency rather than fabricating a default.
- Retain unsupported customer or market questions as unknown.
