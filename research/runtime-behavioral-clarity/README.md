# Runtime Behavioral Instruction Clarity Research

Status: **THEORY VERIFIED — STATIC RUNTIME INTEGRATED**

This directory preserves the research lineage, adversarial audit synthesis, regression contracts, and bounded repairs resolving instruction-realization ambiguity and action-gate drift in the Marketing Practitioner runtime controller (`SKILL.md`).

Static adversarial review identified and resolved two behaviorally consequential instruction-realization defects: drift between the defined `material` threshold and undefined `consequential` action gates, and modifier-attachment ambiguity in the JIT-verification condition. External review follow-up further clarified the boundary between verification requirements and unnecessary external retrieval.

## Governing Question

> How can runtime controller instructions eliminate ambiguity between verification obligations and redundant external retrieval while maintaining strict action-gate precision?

Key assumptions rejected during scoping:
- Verification requires mandatory external retrieval for every provider-controlled or time-sensitive fact.
- Unresolved execution stability can be proven through synthetic benchmark corpora alone.

## Disposition

```text
THEORY / STATIC RESEARCH: COMPLETE
CONFIRMED RUNTIME FINDINGS: F01 CLOSED, F02 CLOSED
EVALUATION-CONTRACT FINDING: EVAL-F01 CLOSED (FAIL-CLOSED REPORTER BOUNDARY)
EXTERNAL REVIEW FOLLOW-UP: CLOSED (VERIFY != ALWAYS RETRIEVE AGAIN)
REAL-TASK VALIDATION: DEFERRED TO AUTHENTIC WORK EPISODES
```

- **Runtime Target**: `skills/marketing-agent-skills/SKILL.md` (evidence safeguard and JIT verification clauses)
- **Mechanisms Added**: Bounded reuse of sufficiently current, scoped local evidence; explicit fail-closed relation semantics in behavioral evaluation harness.
- **Expansions Rejected**: No new controller job, durable primitive, routing table, or external retrieval subsystem.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-six-lane-audit-synthesis.md`](01-six-lane-audit-synthesis.md) | Frozen six-lane audit and finding ledger across instruction realization | Audit Synthesis |
| [`02-targeted-regression-contract.md`](02-targeted-regression-contract.md) | Frozen semantic oracle contract drafted prior to runtime repair | Contract Freeze |
| [`03-bounded-repair-and-verification.md`](03-bounded-repair-and-verification.md) | Exact bounded controller repair and initial static post-repair verification | Bounded Repair |
| [`04-theoretical-closure.md`](04-theoretical-closure.md) | Generalized theory of behaviorally executable agent instructions and defect taxonomy | Theory Closure |
| [`05-real-task-validation-brief.md`](05-real-task-validation-brief.md) | Methodology specification for deferred validation on authentic work episodes | Validation Brief |
| [`06-final-static-adjudication.md`](06-final-static-adjudication.md) | Final closure of F01, F02, and EVAL-F01 for static candidate baseline | Adjudication |
| [`07-external-review-follow-up.md`](07-external-review-follow-up.md) | Resolution of verification vs. retrieval ambiguity post-external review | Follow-up Repair |

Additive diagnostic corpus:
- [`../../evals/behavioral/cases/runtime-guidance-clarity-v1.json`](../../evals/behavioral/cases/runtime-guidance-clarity-v1.json)

## Protected Invariants

```text
VERIFY CURRENT STATE != ALWAYS RETRIEVE AGAIN
SUFFICIENT LOCAL EVIDENCE → REUSE DIRECTLY
UNRESOLVED FRESHNESS / APPLICABILITY / SUPPORT → RETRIEVE AGAIN
MATERIAL THRESHOLD != UNDEFINED CONSEQUENTIAL GATE
OBSERVATION ≠ INTERPRETATION ≠ HYPOTHESIS ≠ DECISION
```

- Sufficiently current, scoped evidence already available in context satisfies verification without redundant external retrieval.
- Retrieval is a mechanism for resolving verification dependencies, not the definition of verification itself.
- Older authoritative evidence does not become current merely because it is authoritative.
