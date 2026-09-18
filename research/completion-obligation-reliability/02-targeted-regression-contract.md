# Completion Obligation Reliability — Targeted Regression Contract

Date: 2026-09-18  
Frozen runtime target: `main@0d6afac77a11662567ea57c64a22963bc92abec6`  
Theory freeze: `research/completion-obligation-reliability/01-theory-freeze.md`

## Purpose

Freeze the behavioral oracles before live execution of the bounded completion repair.

This corpus targets known completion-obligation failure modes. It is diagnostic and repository-seeded, not ecological recurrence evidence and not a general benchmark.

For every pair:

1. judge each member independently;
2. then judge the required semantic relation;
3. do not infer relation success from two independent PASS labels.

The legacy behavioral reporter intentionally does not operationalize cross-case `sensitivity` or `invariance`; use the existing Pressure Discovery relation protocol for pair adjudication.

## Evaluation discipline

- Judge semantic task fulfillment, not preferred phrasing.
- Use deterministic checks first where available.
- Treat explicit delivery constraints, fixed state, evidence limits, and authority limits as hard only when material to completion.
- Do not compensate a material hard violation with polish or extra analysis.
- Accept concise and noncanonical valid answers.
- Reject fluent answers that omit a requested material outcome.
- Accept bounded conclusions when the job asks what the current evidence supports.
- Reject generic caution that leaves independently completable work undone.
- Do not let final validation create new obligations from optional improvements.
- Separate executor/tool failure from answer failure.
- Fixture validation is not behavioral evidence.

---

## Pair COR01 — active outcome retention

### COR01-A — one requested artifact

Task: rewrite an approved launch email while preserving the supplied offer, claims, and CTA.

**MUST**
- return the revised email;
- preserve the fixed offer, claims, and CTA;
- avoid reopening settled strategy.

### COR01-B — additive second artifact

Same task, plus one subject line.

**MUST**
- return both subject line and revised email;
- preserve the same fixed offer, claims, and CTA;
- not drop or materially rewrite the email merely because the subject line was added.

### Relation

**SENSITIVITY / ADD:** adding the subject-line outcome adds that artifact while preserving the unaffected email obligations.

---

## Pair COR02 — downstream consistency with resolved decision state

### COR02-A — approved direction A

An upstream positioning decision is explicitly fixed to Direction A. Write a landing hero and launch email from that direction.

### COR02-B — approved direction B

Identical task except the authoritative positioning decision is fixed to Direction B.

**MUST**
- produce both requested artifacts;
- represent the supplied adopted direction in both;
- preserve unaffected product facts and price;
- not reopen the positioning choice.

### Relation

**SENSITIVITY / CHANGE_TO + PRESERVE:** downstream representation changes with the authoritative positioning state; unaffected facts remain stable.

---

## Pair COR03 — bounded completion calibration

### COR03-A — evidence supports only a bounded conclusion

An observational before/after result includes a material traffic-mix change and no valid causal design. The user asks what the evidence establishes and whether the copy change caused the lift.

**MUST**
- give a useful bounded conclusion;
- distinguish observation from causality;
- not treat the evidence limit as a reason to refuse the requested account;
- optionally identify a discriminating next check if useful.

### COR03-B — scoped causal conclusion is supported

Same decision question, but a valid randomized comparison with stable outcome definitions and no material design defect is supplied.

**MUST**
- permit the stronger scoped conclusion supported by that design;
- retain the actual scope and uncertainty;
- not remain generically noncommittal merely because causal caution exists.

### Relation

**SENSITIVITY / LOOSEN:** conclusion strength changes with evidence license.

---

## Pair COR04 — blockage locality

### COR04-A — one blocked, one independent

The user requests:
1. a destination-specific adaptation whose required private destination policy is missing;
2. a synthesis of supplied customer interviews that does not depend on that policy.

**MUST**
- identify the material dependency for the blocked adaptation;
- complete the interview synthesis;
- not block all work;
- not invent the missing private policy.

### COR04-B — both outcomes genuinely depend on the missing state

Same surface form, but the second requested result now explicitly requires the same unavailable private policy to determine its interpretation.

**MUST**
- not claim either dependent outcome fully complete;
- still provide any useful bounded supported work;
- identify the shared material dependency precisely.

### Relation

**SENSITIVITY:** completion status changes only for outcomes whose real dependency changes.

---

## Pair COR05 — scope and state transition

### COR05-A — current campaign state

Active artifacts are landing page, email, and ad. Approved price is $29. The user asks for a consistency repair across the active set.

**MUST**
- preserve $29;
- account for all three active artifacts;
- preserve unaffected positioning and claims.

### COR05-B — authoritative change and cancellation

Same campaign, but price is authoritatively changed to $39 and the ad is cancelled. Landing page and email remain active.

**MUST**
- update the affected active artifacts to $39;
- exclude the cancelled ad from current completion requirements;
- preserve unaffected positioning and claims;
- not retain stale $29 state.

### Relation

**SENSITIVITY / CHANGE_TO + DROP + PRESERVE:** exactly affected obligations change.

---

## Pair COR06 — delivery constraint as completion condition

### COR06-A — strict title limit

Write exactly one marketplace title, maximum 60 characters, preserving supplied verified compatibility and price facts.

**MUST**
- return exactly one usable title;
- obey the 60-character limit;
- preserve verified compatibility and price;
- not invent product claims.

### COR06-B — relaxed title limit

Same task, but the maximum is 90 characters.

**MUST**
- still return exactly one title;
- obey the new limit;
- preserve the same semantic facts.

### Relation

**SENSITIVITY / LOOSEN + PRESERVE:** representation may expand under the relaxed delivery constraint while fixed meaning remains stable.

---

## Opposite-direction regressions

Any runtime repair must preserve these controls:

1. A sufficient single-output task remains direct and concise.
2. Final validation does not reopen approved positioning, price, or other settled state without an existing reopening condition.
3. A bounded evidence limit can satisfy completion when the requested job is a bounded account.
4. Missing state blocks only dependent outcomes.
5. Cancelled or replaced outcomes are not revived during validation.
6. Optional polish, variants, or further research do not become new completion requirements.
7. Explicit delivery constraints remain real completion conditions.
8. A valid artifact is not rejected merely because it uses noncanonical wording or structure.

## Live comparison

Primary comparison:

```text
ARM 1 — frozen runtime at main@0d6afac77a11662567ea57c64a22963bc92abec6
ARM 2 — bounded completion-obligation repair
```

Optional no-skill execution is contextual only.

Use the same model, reasoning effort, tool regime, prompt/case versions, workspace isolation, and blind adjudication process. Start with two repetitions per condition. Trigger additional repetitions only for material failures or mixed results, up to five per condition for discovery characterization.

A single passing rerun does not establish repair effect. Relation adjudication remains separate from individual member PASS/FAIL.

## Disposition categories

- **COR-N0 — no observed defect**
- **COR-N1 — behavioral defect, variable / F2 controls**
- **COR-N2 — behavioral defect, mechanism unresolved / F12**
- **COR-N3 — local repair**
- **COR-N4 — terminal cue candidate**
- **COR-N5 — composition/state candidate**
- **COR-N6 — architecture research candidate subject to existing F11 gate**

No result in this contract automatically authorizes a new shared runtime abstraction.
