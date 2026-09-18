# Completion Obligation Reliability — Theory Freeze

Date: 2026-09-18  
Frozen runtime target: `main@0d6afac77a11662567ea57c64a22963bc92abec6`  
Candidate branch: `candidate/completion-obligation-stability`

## Status

**THEORY FROZEN — BOUNDED RUNTIME REPAIR APPLIED — LIVE EFFECT PENDING**

This track studies whether Marketing Practitioner reliably reaches the right stopping state for a sufficiently specified task. It does not introduce a new output schema, owner, route, runtime job, or evaluation framework.

## Core distinctions

```text
OUTPUT != COMPLETION != QUALITY != EFFECT
```

- **Output** is the artifact, answer, recommendation, or other visible result.
- **Completion** is whether the active task obligations are satisfied.
- **Quality** is how well a valid result performs on contextual dimensions such as clarity, voice, originality, or information density.
- **Effect** is the downstream real-world outcome and requires its own evidence.

Completion is task-local and job-relative:

```text
TASK-LOCAL COMPLETION
=
active requested outcome
+ applicable job-completion function
+ explicit delivery constraints
+ preserved resolved state
+ applicable evidence / authority bounds
```

The seven existing jobs remain authoritative. No global Definition of Done replaces them.

## Terminal obligation stability

The smallest useful model is:

```text
RETENTION
keep obligations that remain active

SATISFACTION
verify the active obligations before return

CLOSURE
do not manufacture new obligations merely because validation began
```

Or:

```text
retain -> verify -> close
```

This captures the two symmetric errors:

```text
drop a real obligation
-> false completion

add a spurious obligation
-> false incompletion / unnecessary work
```

## Verify is not reconsider

Terminal validation checks already-applicable obligations against current task state. It is not a generic instruction to reconsider the strategy, search for optional improvements, reopen settled choices, or expand scope.

```text
VERIFY
= test postconditions against current resolved state

RECONSIDER
= reopen a settled decision or invent additional work
```

Reconsideration remains justified only under the controller's existing contradiction, material staleness, insufficiency, scope-change, or evidence-change rules.

## Bounded completion

Uncertainty does not imply incompletion. A bounded conclusion can be complete when that is the useful result of the active job, especially for `RESEARCH / UNDERSTAND`, `DIAGNOSE`, and some `DECIDE` tasks.

A material unresolved dependency blocks only the outcomes that actually depend on it. Independent requested outcomes remain completable.

## Runtime disposition

The existing architecture already represents the required semantics through:

- active outcome retention;
- seven useful-completion functions;
- resolved-state preservation;
- materiality and uncertainty rules;
- evidence and authority boundaries;
- scope-change and continuation rules;
- final validation;
- qualitative completion review.

Therefore this track does **not** authorize an Output Contract engine, mandatory completion object, universal checklist, new state ontology, or user-facing status machine.

The bounded candidate repair only makes terminal verification and closure explicit in the existing controller and aligns the completion review rubric with that interpretation.

## Evaluation disposition

Reuse existing infrastructure:

```text
Pressure Discovery
-> semantic predicates, pressure/control relations, attribution

Behavioral Harness
-> isolated execution, repetitions, sealed evidence, blind review

Targeted regression contract
-> frozen behavior before live comparison
```

The first corpus is diagnostic and repository-seeded. It is not ecological recurrence evidence and must not be reported as population performance.

## Governing research question

> Can the agent validate a stable set of task-local completion obligations at the return boundary without dropping active outcomes, violating settled state, overclaiming evidence, falsely blocking bounded completion, or reopening work that was already settled?

Live execution may refine the wording or reveal a narrower repair. Absence of live evidence does not change the static design conclusion recorded here; it limits claims about behavioral effect.
