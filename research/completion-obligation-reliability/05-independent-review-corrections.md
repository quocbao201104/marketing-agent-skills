# Completion Obligation Reliability — Independent Review Corrections

Date: 2026-09-18  
Baseline: `main@0d6afac77a11662567ea57c64a22963bc92abec6`  
Candidate branch: `candidate/completion-obligation-stability`  
Corrected regression contract commit: `13dd5aaa023d51df2bf9bcd0c352a45dc7f236e2`  
Corrected corpus commit: `ec41e6f705268392552437bd1ad8d3c2dd83e293`

## Status

**INDEPENDENT REVIEW FINDINGS REPAIRED — RUNTIME PATCH UNCHANGED**

An independent review accepted the bounded runtime repair and architecture, but found five defects in the first frozen regression corpus. These findings were treated as evaluator/scenario defects, not evidence against the runtime change.

The original static adjudication remains a record of the pre-review state. This document records the subsequent corrections rather than rewriting that history.

## R1 — COR01 source artifact was missing

### Review finding

The first version asked the executor to rewrite an approved launch email but did not supply the source email. This made a correct request for missing input indistinguishable from outcome-retention failure.

### Repair

Both members now include the same approved source email. The only pair mutation is the additional subject-line outcome in B.

Expected relation:

```text
A: rewrite supplied email
B: rewrite same supplied email + add subject
```

The pair now tests additive outcome retention without hidden input.

## R2 — COR03-B causal license was underdetermined

### Review finding

The first version said a randomized treatment mean was higher and that uncertainty was reported, but did not state whether the uncertainty supported a positive effect.

### Repair

B now supplies:

```text
estimated treatment effect = +0.9 percentage points
95% CI = +0.3 to +1.5 percentage points
```

The interval excludes zero, so the stronger scoped positive causal conclusion is licensed by the visible scenario rather than by evaluator inference.

## R3 — COR04-B made optional bounded work mandatory

### Review finding

When both requested final outputs depend on unavailable private policy, the first oracle required additional bounded observations from the interview notes. That introduced an extra completion requirement not requested by the user.

### Repair

The hard semantics now require only:

- do not invent the private policy;
- do not claim either policy-dependent result complete;
- identify the shared material dependency precisely.

Bounded observations are explicitly **MAY**, not **MUST**.

This aligns the oracle with the runtime principle that validation must not manufacture new obligations.

## R4 — COR05 lacked the world state needed for repair

### Review finding

The first version asked for repaired current landing/email/ad artifacts while withholding the artifacts, approved positioning, and approved claims.

### Repair

Both members now supply:

- approved positioning;
- approved non-price claim;
- current landing copy;
- current email copy;
- current ad copy.

The B mutation changes only:

```text
price: $29/month -> $39/month
ad: active -> cancelled
```

The pair can now legitimately test:

```text
CHANGE_TO price
DROP cancelled ad
PRESERVE unaffected meaning
```

without hidden world state.

## R5 — COR06 did not force sensitivity

### Review finding

Changing the maximum from 60 to 90 characters did not necessarily require different correct outputs; a short title could validly pass both cases.

### Repair

Both members now receive the same approved 70-character title:

> Patchboard — Visual Debugger for Local Python AI Workflows — $29/month

and the instruction:

> Keep the approved title unchanged unless the marketplace limit requires a change.

Therefore:

```text
A: max 60 -> must shorten
B: max 90 -> must preserve approved title unchanged
```

The pair now tests a real sensitivity relation and simultaneously tests that terminal validation does not trigger optional rewriting.

## Corpus re-freeze

All 12 members were re-frozen as case version `1.1.0` against the corrected regression contract commit.

The full corpus remains diagnostic and repository-seeded. These repairs improve oracle validity; they do not turn the corpus into ecological recurrence evidence.

## Runtime disposition after review

No independent-review finding required changing:

- `skills/marketing-practitioner/SKILL.md`;
- `skills/marketing-practitioner/frameworks/quality-rubrics.md`;
- routing;
- work-coordination ownership;
- seven job definitions;
- task-specification fields;
- behavioral reporter architecture;
- Pressure Discovery architecture.

The independent review therefore strengthens the bounded disposition:

```text
RUNTIME PATCH             KEEP
ARCHITECTURE EXPANSION    NOT REQUIRED
EVAL DEFECTS              REPAIRED
LIVE EFFECT               PENDING
```

## Remaining boundary

Live execution remains necessary for behavioral effect claims. It is not needed to re-litigate the static evaluator defects corrected here.

If live evidence later requires changing a case oracle materially, create a new case version rather than silently modifying `1.1.0`.
