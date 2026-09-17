# Behavioral Instruction Clarity — Final Static Adjudication

Date: 2026-09-18  
Frozen audit target: `e208024548905790c93adb00096e3130e64873ae`  
Branch: `audit/behavioral-instruction-clarity`

## Final disposition

**PASS — CONFIRMED STATIC FINDINGS CLOSED**

This disposition is limited to the textual/runtime-contract defects established by the six-lane audit. It does not claim improved live-model behavior, lower production failure frequency, or better marketing outcomes. Those remain real-task questions.

---

## F01 — `material` vs `consequential` action-gate drift

**Final status: CLOSED**

The frozen target defined `material` operationally but several downstream action gates used `consequential` without a separate executable definition. The audit established a plausible high-stakes reading that could narrow activation incorrectly.

The bounded controller repair added two constraints to the canonical materiality definition:

```text
Use this definition for action gates throughout the skill;
a difference does not need to be high-stakes to be material.
```

A post-repair runtime scan then classified remaining `consequential` occurrences.

### Action-gate occurrences

Examples include:

- current platform-fact verification;
- current operational-claim re-checks;
- whether missing localization relationship state warrants a question;
- whether platform-specific field semantics justify leaving a fast path;
- whether a current scoped implementation parameter must be re-checked.

None of the inspected local gates defines a competing threshold or grants local authority to override the controller. They therefore inherit the control-plane materiality rule.

### Non-action occurrences intentionally unchanged

The scan also found uses such as:

- stable logical route identifiers such as `content.consequential-strategy`;
- descriptive phrases such as a consequential relation, state, distinction, or dependency;
- historical research/eval prose and changelog text.

These are not threshold definitions. Renaming them would add churn without removing a behavioral ambiguity.

### Adjudication

The root defect was cross-layer threshold drift, not the lexical presence of the word `consequential`. The smallest sufficient repair is therefore a single canonical action-gate definition at the always-loaded control plane, not a repository-wide synonym rewrite.

No remaining inspected runtime rule establishes `consequential` as a stricter high-stakes threshold.

---

## F02 — JIT verification modifier attachment

**Final status: CLOSED**

Frozen wording admitted two materially different parses of `and insufficiently supported`.

The repaired controller now separates the policies:

```text
Verify material external facts just in time when they are
 time-sensitive, provider-controlled, or market-specific.

Also verify a material external fact that is explicitly requested
when current support is insufficient.
```

This makes the intended boolean relation explicit:

```text
material AND (time-sensitive OR provider-controlled OR market-specific)
→ current verification

material AND explicitly requested AND insufficiently supported
→ verification
```

Cached support therefore cannot suppress current verification merely because a provider-controlled or time-sensitive fact is already documented historically.

The uncertainty boundary remains intact: if current verification is unavailable, retain the unknown rather than inventing current state.

---

## EVAL-F01 — legacy `expected_relation` overstates reporter capability

**Final status: CLOSED BY FAIL-CLOSED CONTRACT**

The legacy behavioral case model accepts relation labels including `sensitivity` and `invariance`, but its reporter adjudicates independent baseline-vs-skill answer dispositions. It does not implement cross-case semantic relation scoring.

The repair does not build a second relation engine. Instead, the legacy reporter now explicitly supports only:

```text
expected_relation = skill_not_worse
```

If a caller supplies `sensitivity` or `invariance`, both direct pairing and report construction fail closed with an instruction to use the Pressure Discovery relation protocol.

Targeted unit contracts cover both entry points.

The additive clarity corpus was correspondingly normalized to `skill_not_worse`. Its cross-case sensitivity/invariance semantics remain in the frozen regression/oracle contract, where they are methodological relations rather than claims about legacy reporter capability.

This preserves separation of concerns:

```text
legacy behavioral reporter
→ independent case quality / baseline-vs-skill comparison

Pressure Discovery relation protocol
→ semantic sensitivity / invariance relations
```

---

# Pressure cases retained without repair

The following remain **pressure cases, not confirmed defects**:

- P01 — genuine supersession vs abstraction mismatch;
- P02 — ordinary user instruction vs authorized policy exception;
- P03 — sufficiency of delivery-history comparability;
- P04 — preserving UNKNOWN under recommendation pressure.

Static composition already provides coherent behavior for each. They are retained for later observation on real tasks and must not be converted into new runtime machinery merely because they are difficult.

---

# Architecture disposition

No audit finding justified adding or changing:

- decision owners;
- route families;
- runtime phases;
- specialist activation architecture;
- adaptation ownership;
- platform ontology;
- precedence scoring;
- mandatory approval/checklist workflows.

The final candidate changes instruction realization and one evaluation fail-closed boundary only.

---

# Verification performed in this pass

Performed:

- six-lane static/adversarial instruction audit against the frozen target;
- pre-repair finding and regression-contract freeze;
- exact post-repair diff review;
- whole-runtime classification of relevant `consequential` uses into action-gate vs descriptive/identifier uses;
- Python syntax compilation of the modified reporter/test code;
- additive case-contract normalization to the reporter's actual supported relation;
- repository-side provenance records for every stage.

Not performed and not claimed:

- synthetic live-model comparison;
- real-task production validation;
- failure-frequency estimation;
- causal attribution of future behavioral improvements to these text changes.

---

# Final static candidate

The branch is ready to merge when repository diff/merge checks show it remains a clean descendant of the frozen `main` target.

After merge, real-task validation should use ordinary work episodes rather than treating the synthetic corpus as a production benchmark. See `05-real-task-validation-brief.md`.
