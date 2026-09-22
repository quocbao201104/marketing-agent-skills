# Completion Obligation Reliability — Static Implementation Adjudication

Date: 2026-09-18  
Baseline: `main@0d6afac77a11662567ea57c64a22963bc92abec6`  
Candidate branch: `candidate/completion-obligation-stability`

## Verdict

**PASS BOUNDED STATIC REPAIR — LIVE BEHAVIORAL EFFECT PENDING**

The implementation matches the frozen theory and stays within the authorized bounded scope.

## Runtime changes

### `skills/marketing-agent-skills/SKILL.md`

Two existing controller surfaces were sharpened:

1. **Current-task execution / Step 5**
   - terminal verification now names only material completion determinants;
   - active requested results remain the unit of completion;
   - fixed state, delivery constraints, and evidence/authority bounds remain applicable;
   - validation repairs material failures locally;
   - validation does not reopen settled choices or create new work merely for improvement;
   - a bounded conclusion may be complete when that is the requested useful result.

2. **Completion / Useful completion by job**
   - the seven job criteria are clarified as terminal functions for active outcomes;
   - they remain functions, not workflow steps, mandatory headings, cards, or option counts;
   - they do not reopen resolved work.

No job, route, owner, state schema, output schema, mandatory checklist, or user-facing status machine was added.

### `skills/marketing-agent-skills/frameworks/quality-rubrics.md`

One proportional-review guard was added:

> validate the active job rather than manufacture new completion requirements from optional improvements.

This keeps review aligned with terminal closure without turning the rubric into a runtime completion engine.

## Preserved behavior

Static comparison against the baseline confirms the repair does not intentionally alter:

- the four missing-information roles;
- the canonical materiality threshold;
- current source-request boundaries;
- resolved-state reopening conditions;
- specialist ownership or routing;
- action-authority boundaries;
- continuation and recovery semantics;
- subagent ownership/integration rules;
- the seven completion jobs;
- fast-path permission for sufficient narrow tasks.

The latest input-governance repair on `main@0d6afac...` was incorporated before this adjudication.

## Research and evaluation artifacts

Added:

- `research/completion-obligation-reliability/01-theory-freeze.md`
- `research/completion-obligation-reliability/02-targeted-regression-contract.md`
- `research/completion-obligation-reliability/03-live-evaluation-design.md`
- `evals/behavioral/cases/completion-obligation-reliability-v1.json`

The behavioral corpus contains 12 visible members across six pressure/control families:

1. outcome retention;
2. downstream consistency;
3. bounded completion calibration;
4. blockage locality;
5. scope/state transition;
6. delivery constraint.

The corpus is diagnostic and repository-seeded. It is not ecological recurrence evidence.

## Mechanical/static checks completed in this session

- Candidate branch rebased cleanly onto latest `main` content and is not behind the baseline.
- Behavioral case JSON parsed successfully.
- Case count: 12.
- Case IDs are unique.
- Hard predicate types are limited to existing supported harness predicates: `output_present` and `max_characters`.
- Cross-case members use `expected_relation = sensitivity`, which the current case model accepts.
- The existing behavioral reporter intentionally rejects cross-case sensitivity scoring; the frozen contract therefore requires the existing Pressure Discovery relation protocol instead of adding new reporter machinery.

A full local repository verification run was not executed in this session because the current execution environment could not resolve GitHub for a fresh clone. No CI or live-model success is claimed from the static checks above.

## Live boundary

The following remain pending and must not be inferred from the static repair:

- whether the baseline exhibits the targeted failures on a chosen live model;
- whether the candidate changes their frequency or stability;
- behavioral effect size;
- token/latency/tool burden differences;
- generalization across models or hosts;
- ecological recurrence.

The live design is frozen in `03-live-evaluation-design.md` so later execution can refine the implementation without retroactively redefining the original success criteria.

## Final static disposition

```text
ARCHITECTURE EXPANSION        NOT REQUIRED
BOUNDED CONTROLLER REPAIR     SUPPORTED
QUALITY-RUBRIC ALIGNMENT      SUPPORTED
NEW EVALUATOR INFRASTRUCTURE  NOT REQUIRED
LIVE EFFECT                   PENDING
```
