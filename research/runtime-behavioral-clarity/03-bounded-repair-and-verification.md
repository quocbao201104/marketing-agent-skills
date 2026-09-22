# Behavioral Instruction Clarity — Bounded Repair and Verification

Date: 2026-09-18  
Frozen audit target: `e208024548905790c93adb00096e3130e64873ae`  
Audit synthesis: `896b747a27fff316b682e06ddd2eb2cadadc1ac8`  
Regression contract: `d92983571f93289972dcff86b3bcfd3a716c2f2b`  
Frozen additive corpus: `494dcb4a9705d7db7d96e23028ac34a6a4efa005`  
Bounded runtime repair: `6f3286df9f87fb7f505a7149dc0135cab6907c61`

## Status

**STATIC BOUNDED REPAIR COMPLETE — LIVE BEHAVIORAL VERIFICATION PENDING**

This document records the post-audit repair without reusing the repair as evidence that the original findings existed. Original findings remain grounded only in the frozen target and the six-lane audit.

---

## Authorized repair scope

The frozen audit authorized only two runtime repair properties:

1. make the controller's `material` threshold executable across action gates without requiring a high-stakes interpretation;
2. remove the modifier-attachment ambiguity from the just-in-time external-fact verification rule.

No architecture expansion, owner change, route change, new runtime phase, schema, or mandatory workflow was authorized.

---

# Repair R1 — canonical action-gate materiality

Frozen controller text defined `material` as a difference that can change:

- the choice;
- supported claim;
- interpretation;
- necessary artifact function;
- allowed action.

The repair keeps that definition and adds the explicit control-plane instruction:

```text
Use this definition for action gates throughout the skill;
a difference does not need to be high-stakes to be material.
```

## Static adjudication

**F01: REPAIRED at the controller level.**

The previous interpretation variance was:

```text
material = decision-changing
vs
consequential = possibly high-stakes only
```

The repaired control plane now states that action gates use the defined materiality threshold and explicitly rejects high-stakesness as a necessary condition.

Downstream wording that still contains `consequential` was not mass-edited in this repair. This is intentional:

- `SKILL.md` is always the loaded control plane;
- the defect was cross-layer threshold drift, so the smallest root-level correction is to bind action gates to the canonical threshold once;
- historical evals, route names, research prose, and descriptive uses must not be rewritten merely for lexical consistency;
- broad local churn before behavioral evidence would make attribution of any later behavioral change harder.

If a live old-vs-repaired run shows that a model still interprets a loaded local `consequential` gate as stricter than controller materiality, that observation can justify a second bounded repair that canonicalizes the affected local gates. This possibility is a behavioral follow-up, not a reason to preemptively widen the current patch.

---

# Repair R2 — split the JIT verification boolean

Frozen controller wording:

```text
Verify material external facts just in time when time-sensitive,
provider-controlled, market-specific, or explicitly requested and
insufficiently supported ...
```

Repair:

```text
Verify material external facts just in time when they are time-sensitive,
provider-controlled, or market-specific.

Also verify a material external fact that is explicitly requested when
current support is insufficient.

Prefer authoritative primary sources and retain unknowns when current
verification is unavailable.
```

## Static adjudication

**F02: REPAIRED.**

The new text no longer permits `insufficiently supported` to attach grammatically to the entire time-sensitive/provider-controlled/market-specific list.

Therefore:

```text
provider-controlled + material
→ current verification rule applies
```

regardless of whether an older bundled source is otherwise well supported.

The separate explicitly-requested branch retains the intended counterpressure:

```text
explicit request
+ current support already sufficient
→ no redundant retrieval requirement created by this repair
```

The general uncertainty policy remains available when current verification cannot be completed.

---

# Regression contract disposition

The pre-repair additive corpus is:

```text
evals/behavioral/cases/runtime-guidance-clarity-v1.json
```

It freezes ten cases across:

- cached support vs no cached support for a current provider dependency;
- decision-material vs immaterial low-stakes provider facts;
- explicit supersession vs different abstraction;
- ordinary style request vs authorized scoped exception;
- positive delivery-history comparability control;
- hidden-mechanics UNKNOWN preservation.

The pair relations remain governed by `02-targeted-regression-contract.md`.

The legacy behavioral harness accepts `sensitivity` and `invariance` labels but does not by itself enforce cross-case semantic relations. Independent member PASS labels must therefore not be reported as relation success without explicit pair adjudication or relation-aware machinery.

---

# Scope / regression review

Compare against the frozen target after the bounded repair:

## Runtime changes

```text
skills/marketing-agent-skills/SKILL.md
```

Only two controller sentences changed:

1. materiality definition received one action-gate/high-stakes clarification;
2. the JIT verification sentence was split into unambiguous currentness and explicit-request branches.

## Added audit/eval artifacts

```text
research/runtime-behavioral-clarity/01-six-lane-audit-synthesis.md
research/runtime-behavioral-clarity/02-targeted-regression-contract.md
evals/behavioral/cases/runtime-guidance-clarity-v1.json
research/runtime-behavioral-clarity/03-bounded-repair-and-verification.md
```

No handbook, adaptation, platform, routing-index, owner, evidence-ledger, or existing behavioral-case semantics were modified.

## Preserved opposite-direction controls

Static review confirms the repaired controller still permits or requires the following distinctions:

- sufficient narrow tasks proceed directly;
- immaterial facts do not trigger retrieval merely because a platform/provider noun is present;
- current provider-controlled facts that can change a decision remain JIT dependencies;
- an explicitly requested fact with sufficient current support does not gain a redundant retrieval requirement;
- unavailable current verification produces a bounded/unknown state rather than fabricated current truth;
- changed evidence affects only affected decisions/artifacts;
- owner and resolved-state boundaries are unchanged.

---

# Verification limitations

No live model run is recorded by this repair.

The following are **not** established by static repair review or fixture validation:

- frequency of the original bad parses;
- whether the frozen skill actually fails the new cases on a chosen live model;
- whether the repaired skill passes more often;
- causal effect size of the wording change;
- generalization across models, hosts, or reasoning settings.

No CI status checks were attached to the bounded repair commit at review time. This document therefore does not claim repository CI success from GitHub status evidence.

---

# Next verification step

Use the frozen case/oracle contract with matched execution conditions:

```text
ARM 0 — no skill, contextual baseline
ARM 1 — frozen skill at e208024548905790c93adb00096e3130e64873ae
ARM 2 — repaired skill containing 6f3286df9f87fb7f505a7149dc0135cab6907c61
```

Primary comparison:

```text
ARM 1 vs ARM 2
```

Keep model, reasoning effort, prompt/case versions, tool access, repetitions, and blind adjudication protocol fixed.

For paired cases, adjudicate both:

1. independent acceptability of each member;
2. required semantic sensitivity/invariance relation.

Until that execution is completed, the correct lifecycle state is:

```text
STATIC REPAIR = complete
BEHAVIORAL CONTRACT = frozen
LIVE BEHAVIORAL EFFECT = pending
```
