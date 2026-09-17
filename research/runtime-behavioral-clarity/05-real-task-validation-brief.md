# Behavioral Instruction Clarity — Real-Task Validation Brief

Date: 2026-09-18  
Frozen audit target: `e208024548905790c93adb00096e3130e64873ae`  
Controller repair: `6f3286df9f87fb7f505a7149dc0135cab6907c61`

## Status

**DEFERRED EMPIRICAL PHASE — DO NOT EXECUTE AS PART OF THE CURRENT THEORY PASS**

This brief exists so later real-task analysis begins with a fixed methodology rather than being redesigned after outcomes are observed.

The objective is not to prove that a wording repair "wins" a benchmark. The objective is to learn whether instruction realization materially changes behavior in actual Marketing Practitioner work, and to localize any observed failure before changing runtime architecture.

---

# 1. Why real tasks are the preferred next evidence

Synthetic cases are useful for freezing semantic distinctions, but they frequently announce the exact feature under test.

Real tasks contain the conditions that make instruction clarity difficult:

- incomplete but sufficient context;
- irrelevant adjacent information;
- multiple valid subproblems;
- already-resolved upstream decisions;
- naturally occurring source conflict;
- platform/provider state that may or may not matter;
- ambiguous authority;
- pressure to finish a useful artifact rather than recite a policy.

The strongest evidence for this workstream is therefore behavior observed while solving authentic tasks, not performance on prompts constructed from the finding itself.

---

# 2. Evidence unit: the work episode

Do not treat individual turns or outputs as isolated benchmark questions when the actual job spans state transitions.

Use a **work episode** as the primary unit:

```text
USER JOB
→ available context / artifacts
→ existing resolved state
→ open decision
→ agent actions / retrieval
→ resulting decision or artifact
→ user correction / acceptance / downstream consequence where observable
```

An episode may be one turn when the task is truly self-contained.

---

# 3. What to collect

For each episode retain only what is needed to reconstruct the decision.

## A. Task package

- exact or minimally redacted user request;
- relevant supplied artifacts;
- current date/time when provider state is material;
- available tools / connectors;
- output constraint.

## B. Resolved-state ledger

Record only materially relevant state:

- fixed audience / positioning / offer / policy;
- supported facts;
- assumptions or hypotheses;
- open decisions;
- authority boundaries.

## C. External-state dependencies

For each potentially changing external fact:

- whether it is time-sensitive;
- provider-controlled;
- market/surface scoped;
- supplied/cached/current;
- whether its present truth can change the actual decision.

## D. Behavior trace

Record observable behavior, not inferred hidden reasoning:

- what knowledge was loaded;
- what current facts were retrieved or not retrieved;
- what was preserved/reopened;
- what action was taken;
- what uncertainty was retained;
- what owner or dependency the agent returned to.

## E. Result

- final artifact / recommendation;
- user correction if any;
- material downstream use or failure if observable.

Do not require private chain-of-thought to evaluate these episodes.

---

# 4. Sampling principle

Do not search only for tasks that obviously exercise F01/F02.

Prefer naturally occurring tasks from normal use, then tag them after the fact when one of these distinctions actually became relevant.

Useful sources:

- real copy/adaptation/platform tasks;
- actual current-provider questions;
- tasks with approved upstream state;
- tasks where the user supplies older documentation;
- tasks that stay fully on the fast path;
- tasks where no current external fact matters.

This preserves negative controls and prevents the corpus from becoming a collection of only known-hard prompts.

---

# 5. Primary observational questions

## Q1 — Does materiality govern retrieval rather than perceived seriousness?

Look for episodes where a low-stakes fact changes the current decision.

Correct pattern:

```text
low stakes
+ decision-changing current fact
→ treat as material
```

Potential failure:

```text
low stakes
→ skip currentness check
→ materially wrong branch
```

---

## Q2 — Does cached support suppress current verification incorrectly?

Look for:

```text
older authoritative evidence exists
+ current provider-controlled state matters
```

Correct pattern:

```text
historical support retained
+ current state checked or explicitly bounded
```

Potential failure:

```text
"already supported"
→ cached source treated as current
```

---

## Q3 — Does currentness create over-retrieval?

The repair must not produce:

```text
provider noun
→ always search
```

Look for tasks where provider trivia cannot change the requested result.

Correct behavior is to stay on the direct path.

---

## Q4 — Does a local dependency reopen unrelated state?

A current provider fact may change one representation choice without reopening positioning, audience, offer, or unrelated artifacts.

Watch for scope expansion after retrieval.

---

## Q5 — Do local `consequential` gates still behave as stricter than controller `material`?

This is the key follow-up for the intentionally minimal R1 repair.

If actual tasks repeatedly show:

```text
controller says material
but loaded local module behaves as high-stakes-only
```

then a second bounded repair to the implicated local action gates becomes evidence-backed.

Do not preemptively rewrite every occurrence without this observation.

---

# 6. Failure localization ladder

When an episode looks wrong, do not immediately attribute it to instruction wording.

Test in this order:

```text
F0  task/specification defect
F1  missing or conflicting authority
F2  missing external/tool access
F3  activation failure
F4  routing / knowledge-load failure
F5  local knowledge omission
F6  instruction interpretation / composition defect
F7  evidence/inference error
F8  owner / scope leak
F9  execution variance
F10 evaluator disagreement / invalid oracle
F11 broader architecture candidate
F12 unresolved attribution
```

The labels need not become runtime taxonomy. They are an investigation aid.

A wording repair is justified only when the episode supports F6 more strongly than competing explanations.

A shared-architecture change requires stronger recurrence and owner-level evidence than a local wording repair.

---

# 7. Counterfactual comparison when practical

Do not require every real task to be rerun.

When an episode is important enough and replay is legitimate, compare:

```text
same task package
same tools / accessible sources
same model family and comparable effort
old frozen skill
vs
candidate skill
```

Use the old frozen version as a diagnostic counterfactual, not as a mandatory benchmark arm for normal work.

A replay is most informative when the original failure can be reproduced without leaking the proposed fix into the task prompt.

---

# 8. What counts as useful evidence

## Stronger evidence

- naturally occurring task;
- relevant distinction was not explicitly announced by the prompt;
- observable action differs in a decision-relevant way;
- owner/scope and available evidence can be reconstructed;
- competing explanations are limited;
- similar failure recurs across independent episodes.

## Weaker evidence

- synthetic prompt written from the defect description;
- evaluator rewards terminology rather than behavior;
- only final wording differs but decision is unchanged;
- task itself is underspecified;
- current-state access differs between runs;
- result depends on random stylistic variation;
- same source episode is duplicated many times.

---

# 9. Do not use aggregate win rate as the main conclusion

For this research question, a scalar score hides the important information.

Prefer a finding ledger such as:

| Episode | Open decision | Material distinction | Observed action | Expected bounded behavior | Failure class | Confidence |
| --- | --- | --- | --- | --- | --- | --- |

Then summarize by failure family and recurrence roots.

A small number of high-confidence real failures can justify a bounded wording repair more strongly than a large synthetic score.

---

# 10. Preserve negative and no-change evidence

Record episodes where:

- the controller already worked correctly;
- provider state was correctly judged immaterial;
- local `consequential` wording caused no divergence;
- no retrieval was necessary;
- the model bounded an unknown correctly;
- old and repaired versions behave identically.

This prevents research from turning every difficult task into evidence for more instructions.

---

# 11. Promotion gates after real-task analysis

## Gate A — no further change

Use when:

- no recurring behavior problem is observed;
- failures localize to task ambiguity, missing evidence, or execution variance;
- repaired controller is sufficient in realistic use.

Disposition:

```text
KEEP CURRENT REPAIR
NO FURTHER RUNTIME CHANGE
```

## Gate B — local wording repair

Use when:

- a repeated behavior defect localizes to one executable local gate;
- parent semantics are correct;
- bounded wording change can remove the variance.

Disposition:

```text
REPAIR AFFECTED LOCAL GATE ONLY
ADD REGRESSION FROM REAL EPISODE
```

## Gate C — shared control-plane repair

Use when independent domains fail because the same parent policy remains ambiguous or contradictory.

Requires stronger recurrence than Gate B.

## Gate D — architecture research

Only reopen architecture when observed failures cannot be repaired through:

- existing owner boundaries;
- state preservation;
- trigger/action clarification;
- precedence clarification;
- local knowledge correction.

Architecture is the last hypothesis, not the first response to model error.

---

# 12. Relationship to the frozen synthetic corpus

`evals/behavioral/cases/runtime-guidance-clarity-v1.json` remains useful as:

- semantic documentation;
- a future local regression probe;
- an oracle sanity check;
- a contamination canary if later revisions accidentally reverse the intended distinction.

It must not be treated as:

- representative production sampling;
- an ecological benchmark;
- evidence that R1/R2 improve actual work;
- evidence of failure prevalence.

No need to run it before collecting real-task evidence unless it becomes useful for a specific implementation regression.

---

# 13. Recommended workflow when the repository is pulled locally

```text
1. use the repaired branch on normal work
2. preserve notable work episodes as they naturally occur
3. flag surprising decisions, unnecessary retrieval, or scope reopening
4. reconstruct the episode before inspecting the proposed fix
5. classify competing failure causes
6. replay old vs repaired only for informative cases
7. promote recurring real failures into local regressions
8. repair the smallest demonstrated decision branch
```

The workflow should remain lightweight enough that observation does not distort normal use.

---

# 14. Empirical claim boundary

Until the real-task phase is performed, the strongest justified statement is:

> Static adversarial review identified two behaviorally meaningful instruction-realization defects and a bounded controller repair that removes their textual ambiguity. Whether those repairs materially improve behavior in realistic Marketing Practitioner tasks remains an empirical question intentionally deferred to real use.

That is the closure boundary for the current research pass.
