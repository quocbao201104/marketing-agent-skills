# Behavioral Instruction Clarity — Six-Lane Audit Synthesis

Date: 2026-09-18  
Frozen audit target: `e208024548905790c93adb00096e3130e64873ae`  
Branch: `audit/behavioral-instruction-clarity`

## Status

**PASS_WITH_BOUNDED_REPAIR**

This document freezes the six-lane audit before any runtime repair. Findings below are adjudicated against the frozen target only. Later commits must not be used as evidence that a defect did or did not exist at the frozen target.

The audit asks whether decision-changing instructions are behaviorally executable: whether a competent agent can recover the trigger, action, boundary, precedence, and intended decision delta without two reasonable readings producing materially different behavior.

The audit does **not** claim observed live-model failure frequency, improved model behavior, or causal effect from any future wording repair.

---

## Audit architecture

1. **Decision-point audit** — identify text that can change decisions and its authority.
2. **Trigger → Action audit** — identify when each rule fires and what the agent must do.
3. **Boundary / invariant audit** — identify what may change and what must remain fixed.
4. **Precedence / conflict audit** — determine how owner, scope, authority, evidence, and freshness compose when rules collide.
5. **Interpretation-variance audit** — attack wording that admits two reasonable but behaviorally different readings.
6. **Behavioral-eval audit** — determine whether current evaluation infrastructure and cases can distinguish the target behavior.

Lifecycle used for this work:

```text
freeze
→ audit all lanes
→ finding ledger
→ deduplicate root causes
→ freeze regression/oracle contract
→ bounded repair
→ static re-review
→ behavioral verification
```

No runtime files were edited during lanes 1–6.

---

# Final finding ledger

## F01 — canonical `material` threshold drifts to undefined `consequential` gates

**Class:** behavioral interpretation / trigger clarity  
**Severity:** P1 bounded wording defect  
**Scope:** action-authoritative gates whose intended condition is whether a fact or distinction can change the current decision

The controller defines **material** operationally: a difference is material when it can change a choice, supported claim, interpretation, necessary artifact function, or allowed action.

Several downstream action gates instead use **consequential** without a corresponding behavioral definition.

Two readings are both linguistically reasonable:

```text
A. consequential = decision-changing = material
B. consequential = high-stakes / serious / especially important
```

Those readings can produce opposite actions for an ordinary, low-stakes fact that still changes the current choice.

Example failure shape:

```text
provider-controlled fact
+ ordinary operational decision
+ fact changes option A vs option B
+ no safety/legal/high-stakes consequence

Reader A → verify/retrieve because the fact is material
Reader B → skip because it is not "consequential enough"
```

**Required repair property:** use the canonical `material` threshold, or the explicit phrase `when it can materially change the current decision`, at behavior-authoritative gates. Do not globally replace every descriptive use of `consequential` in the repository.

---

## F02 — JIT verification condition has modifier-attachment ambiguity

**Class:** behavioral interpretation / executable boolean realization  
**Severity:** P1 controller-level wording defect  
**Scope:** `skills/marketing-practitioner/SKILL.md` evidence-and-claim safeguard

Frozen wording:

```text
Verify material external facts just in time when time-sensitive,
provider-controlled, market-specific, or explicitly requested and
insufficiently supported ...
```

Two parses are grammatically plausible:

```text
A.
TIME-SENSITIVE
OR PROVIDER-CONTROLLED
OR MARKET-SPECIFIC
OR (EXPLICITLY REQUESTED AND INSUFFICIENTLY SUPPORTED)
→ VERIFY JIT
```

versus:

```text
B.
(
  TIME-SENSITIVE
  OR PROVIDER-CONTROLLED
  OR MARKET-SPECIFIC
  OR EXPLICITLY REQUESTED
)
AND INSUFFICIENTLY SUPPORTED
→ VERIFY JIT
```

The difference is behaviorally material when a provider-controlled or time-sensitive fact already has bundled or cached support but current state can change the decision.

```text
provider-controlled fact
+ older authoritative bundled source
+ current decision depends on the present provider state

Parse A → verify current state
Parse B → "already supported" → skip verification
```

Surrounding owner guidance, especially provider-dependent operating guidance, indicates that current provider-controlled dependencies should be retrieved just in time when they can change the decision. The controller sentence should expose that logic directly rather than relying on downstream disambiguation.

**Required repair property:** split the boolean into unambiguous clauses. Preserve the separate rule that an explicitly requested fact need not be redundantly retrieved when current support is already sufficient.

---

# Cross-lane findings that were **not** promoted to runtime defects

The following were attacked and found sufficiently executable in full composition.

## Activation and routing

- A platform or artifact noun does not create a job.
- Platform-specific knowledge is loaded only for a concrete unresolved decision that the knowledge can materially change.
- Sufficient narrow transformations remain on the direct path.

**Disposition:** PASS.

## Founder-led Sales local stops and global pursuit

Local conclusions such as access exhaustion, proof completion, no current decision path, or walking a current package remain local. Global pursuit allocation remains owned by FS1 and depends on forward value, learning/options, burden, and opportunity cost.

**Disposition:** PASS STRONG.

## Adaptation ownership and resolved state

Local adaptation refines an already-open owner decision. Local relevance does not authorize reopening resolved identity, relationship, authority, policy, or unrelated dimensions. Section-local evidence does not become a new decision owner.

**Disposition:** PASS STRONG.

## Platform diagnosis before tactical repair

Weak metrics or state changes do not immediately authorize creative/copy repair. Runtime paths preserve competing explanations and require state/localization checks before tactical intervention.

The inverse is also preserved:

```text
evidence does not support X
!=
evidence supports not-X
```

**Disposition:** PASS.

## Mixed delivery history

A change in organic/paid/collaboration state can invalidate a mode-pure interpretation without invalidating the object, all history, or every possible comparison.

**Disposition:** PASS.

## Precedence architecture

The repository intentionally avoids a universal winner table such as:

```text
newer > older
more specific > broader
private > upstream
reviewed > provisional
local > global
```

Conflict resolution composes:

```text
DECISION OWNER
→ ACTUAL SCOPE / APPLICABILITY
→ BINDING AUTHORITY
→ EVIDENCE / PROVENANCE
→ FRESHNESS WHEN MATERIAL
→ preserve unresolved conflict when no winner is justified
```

**Disposition:** PASS.

No new precedence engine, owner, schema, route family, or mandatory workflow is justified by this audit.

---

# Behavioral pressure cases retained for evaluation

These are not static defects. They remain candidates because model behavior may still fail under pressure even though the current text is coherent enough for static adjudication.

## P01 — genuine supersession vs abstraction mismatch

- New authoritative evidence that explicitly supersedes an old state may govern the affected scope.
- A newer source that answers a different surface, stage, purpose, or abstraction must not win merely because it is newer.

## P02 — user/task instruction vs authoritative organization policy

- Ordinary style requests may change open dimensions without silently overriding a binding scoped policy.
- A legitimate explicit scoped exception with sufficient authority may change the governed dimension.
- Missing override authority should remain a bounded dependency rather than being guessed.

## P03 — sufficiency of delivery history

- Mixed aggregate history must not be treated as mode-pure merely because the object is identical.
- Sufficiently separated and comparable regime-specific observations should not be rejected merely because an object has ever changed delivery state.

## P04 — preserve UNKNOWN under recommendation pressure

Evidence that a feature is processed, eligible, retrieved, or used somewhere in a system does not establish an undisclosed ranking weight or optimization hierarchy.

---

# Evaluation-layer finding

## EVAL-F01 — legacy behavioral `expected_relation` is not operationalized as a cross-case semantic relation

**Class:** bounded evaluation-contract gap  
**Severity:** P2 evaluation follow-up  
**Not a runtime skill defect**

The behavioral case model accepts:

```text
skill_not_worse
sensitivity
invariance
```

but the legacy report pairs independently judged pass/fail arms and does not enforce a semantic cross-case sensitivity/invariance relation. Repository documentation already notes that opposite-direction controls are independent cases rather than a cross-case sensitivity scoring mechanism.

Pressure Discovery defines stronger pair semantics and is the better methodological reference for relational checks.

This gap does not block the bounded runtime repair. It does constrain what may be claimed from legacy behavioral reports.

---

# Behavioral evidence status

At the frozen target:

```text
F01, F02 = statically confirmed wording defects
```

but:

```text
not established:
- live failure frequency
- whether a specific model currently takes the bad parse
- whether a repair improves behavior
- causal effect size of wording changes
```

Release 2.0 static clarity work and infrastructure checks do not constitute live model behavioral evidence.

---

# Repair gate

Only the following runtime repair family is currently authorized by this audit:

1. Canonicalize behavior-authoritative decision-change thresholds to `material` / `materially change the current decision`.
2. Split the controller JIT-verification boolean into unambiguous clauses while preserving current uncertainty and authority boundaries.

Repair must preserve:

- direct execution for sufficient narrow tasks;
- existing owner boundaries;
- resolved-state preservation;
- claim/evidence discipline;
- provider/system/surface scope;
- UNKNOWN/conflict preservation;
- current source preference only where freshness is materially decision-relevant;
- no blanket verification requirement for immaterial external facts.

No architecture expansion is authorized.

---

# Required next artifact

Before runtime edits, freeze a targeted regression/oracle contract covering:

- F01 materiality threshold;
- F02 cached-support/currentness attachment;
- supersession vs abstraction control;
- ordinary style request vs authorized scoped override;
- mixed delivery negative and positive controls;
- preservation of unknown hidden mechanics.

That contract is `02-targeted-regression-contract.md` in this directory.
