# Completion Obligation Reliability — Live Evaluation Design

Date: 2026-09-18  
Frozen baseline: `main@0d6afac77a11662567ea57c64a22963bc92abec6`  
Behavioral corpus: `evals/behavioral/cases/completion-obligation-reliability-v1.json`

## Status

**LIVE EXECUTION DEFERRED — DESIGN FROZEN**

The user intends to run live evaluation after the implementation work is complete. This document fixes the comparison and interpretation rules in advance so later tuning does not silently redefine success.

## Arms

Primary comparison:

```text
ARM 1 — frozen baseline skill at 0d6afac77a11662567ea57c64a22963bc92abec6
ARM 2 — bounded completion-obligation repair
```

Optional contextual arm:

```text
ARM 0 — no-skill baseline
```

ARM 0 is not the causal comparison for the controller wording change.

## Execution controls

Hold fixed across compared arms:

- model and model snapshot where observable;
- reasoning effort;
- case version;
- tool and permission regime;
- host/runtime configuration as far as the harness can seal it;
- fresh-context policy;
- workspace isolation;
- output constraints;
- blind adjudication procedure.

Each attempt uses a fresh context. Do not expose oracle text, relation labels, failure classes, or prior candidate answers to the executor.

Counterbalance or pre-lock run order when temporal/order effects are plausible.

## Repetition policy

Start with two repetitions per case/arm.

Trigger up to three additional repetitions only when:

- a material hard failure is observed;
- the first two repetitions disagree materially;
- an intervention result would otherwise be confounded by execution variance.

The maximum of five repetitions is for discovery characterization, not a population failure-rate estimate.

## Judgment pipeline

```text
candidate output
  -> deterministic predicates first
  -> blind semantic predicate review
  -> independent member disposition
  -> explicit pair relation adjudication
  -> attribution only after behavior is locked
```

Allowed member dispositions remain:

- pass;
- fail;
- unresolved.

Operational failure is not answer failure.

For semantic review, prefer material atomic obligations over holistic impressions. Do not use prose polish to compensate for a hard completion violation.

## Pair relations

Use corpus version `1.2.0` with the legacy behavioral reporter for independent member dispositions and baseline-versus-skill comparisons. Its `expected_relation = skill_not_worse` labels describe only that supported reporting contract. Adjudicate the six sensitivity relations separately with the existing Pressure Discovery relation protocol; the legacy report does not score or prove those relations.

Both members must be independently acceptable before a pair can pass its relation.

The six frozen families test:

1. additive outcome retention;
2. downstream consistency with resolved decision state;
3. bounded completion calibration;
4. blockage locality;
5. scope/state transition;
6. delivery-constraint sensitivity.

## First diagnostic intervention

If the baseline shows a stable material completion failure, test the smallest terminal intervention first:

```text
Before returning, verify every active requested outcome against the
conditions that materially determine whether it is complete. Do not
reopen settled choices or create new work merely to improve the result.
```

This is a terminal postcondition cue, not a request to reconsider the reasoning.

## Diagnostic escalation

Only if the smaller terminal cue is insufficient, use an answer-free state capsule such as:

```text
Active outcomes:
- <outcome A>
- <outcome B>

Preserve:
- <resolved invariant>

Bound:
- <applicable evidence/authority limit>
```

The capsule may restate already-visible task state. It must not contain the answer.

If a generic attention reminder repairs equally well, do not attribute the effect to completion-obligation representation.

## Interpretation

Use existing Pressure Discovery attribution rules.

Important dispositions:

- stable behavioral failure with no discriminating mechanism -> F12;
- mixed exact runs -> F2 controls the stability claim;
- answer-free state-only repair with adequate owners may support an F6-like composition candidate;
- a bounded out-of-scope dependency is not a completion failure when the skill correctly stops at that boundary.

## Regression checks

A completion repair must not cause:

- strategy or pricing to reopen without an existing reopening condition;
- new clarification questions for sufficient narrow tasks;
- optional variants, polish, or extra research to become completion requirements;
- cancelled outcomes to be revived;
- bounded conclusions to be mislabeled incomplete;
- fast-path tasks to gain visible process narration or checklist ceremony.

Track naturally induced:

- output length;
- questions/turns;
- tool calls;
- tokens where observable;
- latency where observable;
- unfinished required work;
- unnecessary reopening.

These are burden diagnostics, not a single aggregate score.

## Promotion rule

Live results may justify wording refinement or a narrower local repair. A shared runtime abstraction still requires the existing F11 architecture-reopening gate.

The default interpretation remains:

```text
smallest demonstrated repair
> larger unproven mechanism
```

No live result should be used to retroactively change the frozen oracle for the same evaluation version. Material oracle changes require a new version and rejudgment.
