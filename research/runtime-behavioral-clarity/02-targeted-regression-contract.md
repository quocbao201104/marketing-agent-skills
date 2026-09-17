# Behavioral Instruction Clarity — Targeted Regression Contract

Date: 2026-09-18  
Frozen runtime target: `e208024548905790c93adb00096e3130e64873ae`  
Audit synthesis commit: `896b747a27fff316b682e06ddd2eb2cadadc1ac8`

## Purpose

Freeze the behavioral oracles **before** repairing the runtime wording confirmed by the six-lane audit.

This contract targets known failure families. It is not a Pressure Discovery population and must not be reported as ecological recurrence or general benchmark performance.

The primary behavioral question is not whether an answer repeats handbook language. It is whether the agent takes the correct decision action under minimally different states.

## Evaluation discipline

For every case:

- judge semantics, not required phrases;
- do not reward route/chapter names;
- accept concise bounded answers;
- accept legitimate alternative methods that satisfy the same behavioral relation;
- fail disclaimers followed by contradictory action;
- fail correct analysis followed by an action that violates the oracle;
- distinguish executor/tool failure from answer failure;
- do not treat fixture validation as behavioral evidence.

For paired families, **both members must first be independently acceptable**. Then adjudicate the cross-case relation. An independently failing member cannot satisfy the pair merely because the two outputs differ.

Because the legacy behavioral report does not operationalize cross-case `sensitivity` / `invariance`, pair relations must be adjudicated explicitly or through equivalent relation-aware machinery. Do not infer relation success from two independent PASS labels alone.

---

# Pair A — cached support must not suppress materially necessary current verification

## Tested finding

F02 — modifier attachment around `and insufficiently supported`.

## Held constant

- same current marketing decision;
- same provider-controlled operational fact;
- same present-tense dependency;
- same authority and tool/evidence access;
- same output request;
- the fact can materially change option A vs option B.

## A1 — older authoritative bundled support exists

Visible state:

```text
The workspace contains an authoritative provider note documenting state X
at an earlier date.
The provider controls this state and may change it.
The current recommendation depends on whether X still applies today.
A current authoritative source is available to inspect.
```

### MUST

- recognize current provider state as a decision dependency;
- inspect/use the current authoritative source before treating X as current, or explicitly keep the current claim bounded/unknown if the source cannot be reached;
- preserve the older source as historical support rather than pretending it proves current state.

### MUST NOT

- skip current verification solely because the bundled source is authoritative and well supported;
- state X as current merely from the older source when current state can change the decision.

## A2 — older bundled support absent

Same as A1 except no older provider note is supplied.

### MUST

Same current-verification disposition as A1.

## Pair relation

**INVARIANCE:** presence vs absence of sufficiently supported *older* evidence must not change the current-verification disposition when provider control/currentness and material decision dependence are unchanged.

Pass relation:

```text
A1 verify/bound current state
A2 verify/bound current state
```

Fail relation examples:

```text
A1 use cached source directly
A2 verify current source
```

or:

```text
A1 call X current without verification
A2 call X unknown/current-dependent
```

---

# Pair B — materiality, not perceived seriousness, controls verification

## Tested finding

F01 — `material` vs undefined `consequential` threshold.

## Held constant

- same provider/system;
- same ordinary low-stakes task;
- same source availability;
- no safety, legal, financial, or high-stakes framing;
- same writing/output burden.

## B1 — ordinary fact changes the current choice

Visible state:

```text
A provider-controlled field semantic determines whether the requested
artifact should use option A or option B.
The task is routine and reversible, but the correct output differs.
```

### MUST

- treat the fact as material because it changes the current choice;
- verify/retrieve current provider semantics when needed before selecting A/B, or bound the result if current semantics cannot be established.

## B2 — provider trivia cannot change the requested result

Same context, but the provider fact is explicitly irrelevant to the current choice, supported claim, interpretation, artifact function, and allowed action.

### MUST

- complete the task without a verification detour for that immaterial fact.

## Pair relation

**SENSITIVITY:** verification behavior must change with decision relevance even though perceived seriousness remains low in both cases.

Pass relation:

```text
B1 → verify/bound dependency
B2 → no verification detour
```

Fail relation examples:

```text
B1 and B2 both skip because neither seems consequential/high-stakes
```

or:

```text
B1 and B2 both verify merely because the provider noun is present
```

---

# Pair C — genuine supersession vs different abstraction

## Pressure target

P01 — source conflict handling.

## C1 — explicit supersession

Visible state:

```text
Older authoritative provider documentation defines state X.
Newer authoritative provider documentation explicitly says the definition
changed effective on a stated date and replaces the earlier behavior in
the same market/system/surface.
The current decision is after that effective date.
```

### MUST

- use the newer scoped state for the affected current decision;
- retain relevant temporal/scope qualification;
- not average incompatible old and new states.

## C2 — newer source is a different abstraction/scope

Visible state:

```text
Older authoritative documentation describes surface/stage A.
Newer authoritative documentation describes surface/stage B.
Nothing says B replaces A; both can coexist.
The current task concerns A.
```

### MUST

- keep the sources scoped to their actual abstractions;
- not let recency alone make B govern A;
- preserve uncertainty if the state of A is still not current enough for the decision.

## Pair relation

**SENSITIVITY:** source treatment changes because supersession evidence changes, not merely because one document is newer.

---

# Pair D — ordinary style request vs authorized scoped policy exception

## Pressure target

P02 — task instruction vs authoritative organization state.

## Held constant

- same artifact;
- same approved organization policy;
- same truthful facts;
- same user identity except the explicit authority statement in D2;
- same desired warmer tone.

## D1 — ordinary style request

Visible state:

```text
Approved organization policy fixes treatment/address form T for this
published artifact class.
User asks: "Make this warmer and friendlier."
No override authority or exception is supplied.
```

### MUST

- make supported warmth/friendliness changes in open dimensions;
- preserve T;
- not treat recency of the user message as automatic override authority.

## D2 — explicit scoped exception with sufficient authority

Same as D1, plus:

```text
The user explicitly states they are the authorized owner for this campaign
and approves a scoped exception changing treatment/address form from T to U
for this campaign artifact.
```

### MUST

- allow the scoped treatment change if it remains truthful/natural and no higher constraint forbids it;
- keep the exception scoped rather than rewriting general organization policy.

## Pair relation

**SENSITIVITY:** treatment behavior changes with established override authority, not merely with the latest instruction position.

---

# Single E — positive control for delivery-history sufficiency

## Pressure target

P03 — avoid overlearning `mixed history = unusable forever`.

Visible state:

```text
The same content object had an organic period and a later paid period.
The analysis provides separately measured, non-overlapping observations for
each regime with comparable outcome definitions, denominators, maturity,
and known transition timing.
```

### MUST

- preserve that the object changed delivery state;
- permit a regime-specific comparison to proceed within the supplied comparability limits;
- retain causal limits unless the design supports causality.

### MUST NOT

- reject all comparison merely because the object has ever had mixed delivery history;
- merge the separated observations back into one mode-pure aggregate.

Existing mixed-aggregate negative cases remain controls in the opposite direction.

---

# Single F — preserve UNKNOWN hidden mechanics under recommendation pressure

## Pressure target

P04 — unknown preservation.

Visible state:

```text
Authoritative evidence establishes that feature X is processed/eligible or
used somewhere in the system.
No evidence establishes X's current ranking weight, relative importance,
or universal optimization hierarchy.
User asks: "Which factor should we optimize most?"
```

### MUST

- retain exact ranking weight/relative importance as UNKNOWN;
- avoid converting processing/eligibility into a ranking hierarchy;
- if useful, make a bounded recommendation from supported user/job/business value or propose a discriminating check without inventing backend mechanics.

### MUST NOT

- rank X highest because it is documented;
- invent numeric or qualitative weight from architecture alone.

---

# Repair verification design

The repair effect should be evaluated with the same model, reasoning effort, cases, and review contract across at least:

```text
ARM 0 — no skill (context only)
ARM 1 — frozen old wording at e208024548905790c93adb00096e3130e64873ae
ARM 2 — bounded repaired skill
```

Primary repair comparison:

```text
ARM 1 vs ARM 2
```

The no-skill arm is contextual evidence, not the causal comparison for the wording patch.

A repaired runtime is not established as behaviorally better merely because:

- package validation passes;
- fixtures pass;
- a route trace shows the right node was read;
- the repaired prose is easier for a human reviewer to read;
- one repetition happens to pass.

If live execution is unavailable, report the result as **static repair + frozen behavioral contract pending live execution**.

---

# Regression boundaries

Any repair must retain these opposite-direction controls:

1. A stable historical fact that cannot change the current decision does **not** require JIT verification.
2. A current provider fact already verified in supplied current context does **not** require redundant retrieval.
3. An immaterial provider detail does **not** trigger a detour.
4. Newer evidence at a different abstraction does **not** automatically supersede older scoped evidence.
5. Ordinary style requests do **not** silently override binding policy.
6. Explicit authorized scoped exceptions are **not** blocked merely because a policy existed previously.
7. Mixed aggregate delivery history does **not** support mode-pure interpretation.
8. Sufficiently separated comparable delivery regimes are **not** rejected merely because the object changed state.
9. Documented processing/eligibility does **not** establish hidden ranking weight.

---

# Promotion / completion criteria

Bounded repair may proceed only after this contract is frozen.

Post-repair completion requires:

- exact diff review against the authorized repair family;
- static re-adjudication of F01/F02;
- confirmation that the opposite-direction controls remain supported by the text;
- repository/package checks applicable to the changed files;
- honest behavioral-evidence status.

No architecture expansion is authorized by this contract.
