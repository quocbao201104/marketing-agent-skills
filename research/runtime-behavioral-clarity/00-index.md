# Runtime Behavioral Instruction Clarity — Research Index

Date: 2026-09-18  
Branch: `audit/behavioral-instruction-clarity`  
Frozen audit target: `e208024548905790c93adb00096e3130e64873ae`

## Current disposition

```text
THEORY / STATIC RESEARCH
COMPLETE FOR THIS PASS

BOUNDED CONTROLLER REPAIR
COMPLETE

SYNTHETIC LIVE EVAL
INTENTIONALLY DEFERRED

REAL-TASK VALIDATION
DEFERRED UNTIL NORMAL WORK EPISODES ARE AVAILABLE
```

The synthetic behavioral corpus is retained as a semantic/regression contract only. It is not treated as production validation.

## Read order

1. [`01-six-lane-audit-synthesis.md`](01-six-lane-audit-synthesis.md) — frozen six-lane audit and finding ledger.
2. [`02-targeted-regression-contract.md`](02-targeted-regression-contract.md) — frozen semantic/oracle contract written before runtime repair.
3. [`03-bounded-repair-and-verification.md`](03-bounded-repair-and-verification.md) — exact bounded repair and static post-repair verification.
4. [`04-theoretical-closure.md`](04-theoretical-closure.md) — generalized theory of behaviorally executable agent instructions and defect taxonomy.
5. [`05-real-task-validation-brief.md`](05-real-task-validation-brief.md) — deferred methodology for later analysis on authentic work episodes.

Additive diagnostic corpus:

- [`../../evals/behavioral/cases/runtime-guidance-clarity-v1.json`](../../evals/behavioral/cases/runtime-guidance-clarity-v1.json)

## Provenance

- Frozen pre-repair target: `e208024548905790c93adb00096e3130e64873ae`
- Audit synthesis commit: `896b747a27fff316b682e06ddd2eb2cadadc1ac8`
- Regression contract commit: `d92983571f93289972dcff86b3bcfd3a716c2f2b`
- Additive synthetic corpus commit: `494dcb4a9705d7db7d96e23028ac34a6a4efa005`
- Bounded controller repair commit: `6f3286df9f87fb7f505a7149dc0135cab6907c61`
- Static repair record commit: `0c7eb5397c52de97516cbfa5265ea6832cfa37a9`
- Theory closure commit: `77dd0d7a93d17c153cdc36b9c4c5ca6503739c17`
- Real-task validation brief commit: `5a2ddbb9fa390bb6da5b5e55e377a163c0f41db7`

## Current justified claim

Static adversarial review identified two behaviorally meaningful instruction-realization defects:

1. drift between the defined `material` threshold and undefined `consequential` action gates;
2. modifier-attachment ambiguity in the controller JIT-verification condition.

A bounded controller repair removes the identified textual ambiguity without changing architecture, ownership, routing, or domain knowledge.

No claim is made here that the repair improves live behavior, failure frequency, or marketing outcomes. Those questions are reserved for later real-task observation.
