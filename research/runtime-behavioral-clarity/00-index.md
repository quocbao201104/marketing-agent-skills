# Runtime Behavioral Instruction Clarity — Research Index

Date: 2026-09-18  
Branch: `audit/behavioral-instruction-clarity`  
Frozen audit target: `e208024548905790c93adb00096e3130e64873ae`

## Current disposition

```text
THEORY / STATIC RESEARCH
COMPLETE

CONFIRMED RUNTIME FINDINGS
F01 CLOSED
F02 CLOSED

EVALUATION-CONTRACT FINDING
EVAL-F01 CLOSED BY FAIL-CLOSED REPORTER BOUNDARY

SYNTHETIC LIVE EVAL
INTENTIONALLY DEFERRED

REAL-TASK VALIDATION
DEFERRED UNTIL NORMAL WORK EPISODES ARE AVAILABLE
```

The synthetic behavioral corpus is retained as a semantic/regression contract only. It is not treated as production validation. The legacy behavioral reporter supports `skill_not_worse`; cross-case sensitivity/invariance semantics belong to the Pressure Discovery relation protocol.

## Read order

1. [`01-six-lane-audit-synthesis.md`](01-six-lane-audit-synthesis.md) — frozen six-lane audit and finding ledger.
2. [`02-targeted-regression-contract.md`](02-targeted-regression-contract.md) — frozen semantic/oracle contract written before runtime repair.
3. [`03-bounded-repair-and-verification.md`](03-bounded-repair-and-verification.md) — exact bounded controller repair and initial static post-repair verification.
4. [`04-theoretical-closure.md`](04-theoretical-closure.md) — generalized theory of behaviorally executable agent instructions and defect taxonomy.
5. [`05-real-task-validation-brief.md`](05-real-task-validation-brief.md) — deferred methodology for later analysis on authentic work episodes.
6. [`06-final-static-adjudication.md`](06-final-static-adjudication.md) — final closure of F01, F02, and EVAL-F01 for the static candidate.

Additive diagnostic corpus:

- [`../../evals/behavioral/cases/runtime-guidance-clarity-v1.json`](../../evals/behavioral/cases/runtime-guidance-clarity-v1.json)

## Provenance

- Frozen pre-repair target: `e208024548905790c93adb00096e3130e64873ae`
- Audit synthesis commit: `896b747a27fff316b682e06ddd2eb2cadadc1ac8`
- Regression contract commit: `d92983571f93289972dcff86b3bcfd3a716c2f2b`
- Additive synthetic corpus freeze: `494dcb4a9705d7db7d96e23028ac34a6a4efa005`
- Bounded controller repair: `6f3286df9f87fb7f505a7149dc0135cab6907c61`
- Static repair record: `0c7eb5397c52de97516cbfa5265ea6832cfa37a9`
- Theory closure: `77dd0d7a93d17c153cdc36b9c4c5ca6503739c17`
- Real-task validation brief: `5a2ddbb9fa390bb6da5b5e55e377a163c0f41db7`
- Legacy reporter fail-closed relation boundary: `b2ced4740e4ac9e6d515b2c412ad31a83e171a04`
- Reporter regression tests: `23ea63f896e6595af0a18d32c0ebafbfda172230`
- Clarity corpus normalization: `4d6338dcf4365247ad1b5395f2fd3ed2a7bcff88`
- Final static adjudication: `da21e605f56e0311d5f6040aad09c7481d0f8cbb`

## Current justified claim

Static adversarial review identified and the bounded repair closes two behaviorally meaningful instruction-realization defects:

1. drift between the defined `material` threshold and undefined `consequential` action gates;
2. modifier-attachment ambiguity in the controller JIT-verification condition.

The evaluation-side audit also found that the legacy reporter accepted relation labels it did not operationalize. The reporter now fails closed on those unsupported relation semantics and directs them to the Pressure Discovery protocol instead of silently implying support.

No architecture, ownership, routing, domain knowledge, or precedence engine was added.

No claim is made here that the repair improves live behavior, failure frequency, or marketing outcomes. Those questions are reserved for later real-task observation.
