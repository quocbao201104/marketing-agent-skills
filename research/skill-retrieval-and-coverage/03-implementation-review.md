# Skill Retrieval and Coverage — Implementation Review

Status: **SELF-REVIEW COMPLETE — NO OPEN BLOCKING FINDINGS — LIVE BEHAVIOR NOT YET ESTABLISHED**  
Review date: 2026-09-18  
Design freeze: `research/skill-retrieval-and-coverage/01-design-freeze.md`  
Implementation reviewed through: `0a45a4e3e944ec331c2df725ccd6ccc2086e3e33`  
Draft PR: #60

This review evaluates the bounded candidate implementation produced from the design freeze. It is a code/design review of the implementation and its evaluation scaffolding. It is not a substitute for live activation or coverage experiments.

## 1. Reviewed change surface

Runtime:

```text
skills/marketing-practitioner/SKILL.md
```

Evaluation/runtime instrumentation:

```text
evals/behavioral/behavioral_eval/activation.py
evals/behavioral/behavioral_eval/activation_cli.py
evals/behavioral/behavioral_eval/trace.py
evals/behavioral/materialize_activation_variants.py
```

Evaluation corpora/oracles:

```text
evals/behavioral/cases/skill-activation-v1.json
evals/behavioral/oracles/skill-activation-v1.activation-oracle.json
evals/behavioral/cases/coverage-routing-v1.json
evals/behavioral/oracles/coverage-routing-v1.route-oracle.json
evals/behavioral/variants/skill-activation-descriptions-v1.json
evals/behavioral/experiments/skill-activation-v1/*
```

Regression tests:

```text
evals/behavioral/tests/test_activation.py
evals/behavioral/tests/test_activation_variants.py
evals/behavioral/tests/test_skill_activation_experiment.py
evals/behavioral/tests/test_coverage_routing_experiment.py
evals/behavioral/tests/test_trace.py
```

Protected runtime surfaces remain unchanged:

```text
routing-index.json
get-knowledge.py
handbook knowledge
platform knowledge
adaptation knowledge
behavioral runner semantics
logical route IDs
owner taxonomy
```

## 2. Runtime implementation reviewed

### Activation surface

The top-level description now emphasizes:

```text
owned practitioner jobs
+
latent symptom classes
+
adjacent-task boundaries
```

rather than spending substantial metadata budget on post-activation process instructions already present in the body.

The candidate remains within the intended ~100-word routing budget.

### Coverage control

Current-task Step 3 now distinguishes:

```text
bounded unresolved question
vs
broad problem whose material surfaces are not yet localized
```

The reviewed wording preserves JIT behavior:

```text
for each open surface:
use retained/supplied state directly when sufficient
otherwise:
route to the owner
and load only the smallest knowledge that can change the result
```

It explicitly prevents topic mention from becoming activation authority.

### Stopping rule

The stopping rule now applies only after material open surfaces have been localized and each has been:

```text
resolved
OR
bounded by evidence / authority
OR
shown not to affect the useful result
```

This avoids both premature closure and an impossible requirement to resolve every uncertainty exhaustively.

## 3. Findings discovered during review

### IR-01 — stacked trace labels were undercounted

Severity: **correctness**

Observed issue:

`evals/behavioral/behavioral_eval/trace.py` incremented `case_label_counts` only for the final label from a stacked classification.

This pre-existing behavior became materially wrong once a partial walk could carry:

```text
premature_closure
+
skip_jit
```

Impact:

dashboard/case-level trace counts would omit one or more real failure labels.

Fix:

```text
increment case_label_counts inside the label loop
```

Regression coverage added:

```text
test_trace_report_counts_all_stacked_labels_for_case
```

The trace report schema was bumped from v1 to v2 because the report now includes new coverage-count fields and a new primary classification.

Disposition: **FIXED**

---

### IR-02 — founder-sales dependency oracle reopened settled ICP

Severity: **semantic / evaluation validity**

Observed issue:

`BEH-COV-DEP-003` explicitly says general ICP guidance already exists, but the initial oracle required loading Chapter 02 segmentation.

That contradicted the repository principle:

```text
preserve settled state
+
account-specific pursuit
!=
general target-market reopening
```

Fix:

required coverage is now:

```text
founder-sales.selection
→
founder-sales.pursuit
```

and Chapter 02 segmentation is explicitly forbidden for that case.

Regression coverage added:

```text
test_founder_sales_dependency_case_preserves_settled_icp
```

Disposition: **FIXED**

---

### IR-03 — first coverage wording could be read as load-every-open-surface

Severity: **runtime efficiency / over-routing risk**

Observed issue:

the first candidate said:

```text
Route each open surface to its owner and smallest useful knowledge.
```

Read literally, that could cause a read even when retained or supplied state already resolves the surface.

That would weaken the repository's existing JIT architecture.

Fix:

the runtime now says, in effect:

```text
For each open surface:
use retained or supplied state directly when sufficient;
otherwise route to the owner and smallest useful knowledge
that can change the result.
```

Disposition: **FIXED**

---

### IR-04 — initial stopping wording was too absolute

Severity: **runtime completeness / bounded-uncertainty risk**

Observed issue:

the first candidate required no unresolved material surface to remain before stopping.

That could conflict with legitimate bounded outcomes where evidence or authority limits remain explicit.

Fix:

the reviewed rule allows a surface to be:

```text
resolved
bounded by evidence / authority
or shown not to affect the useful result
```

before the marginal-gain stopping rule applies.

Disposition: **FIXED**

---

### IR-05 — frozen D0 baseline initially depended on current production description

Severity: **experiment reproducibility**

Observed issue:

the activation variant materializer originally required:

```text
D0 description == currently checked-out production description
```

Once the candidate runtime adopted D3, that invariant would destroy the frozen baseline or make the experiment impossible to rematerialize.

Fix:

D0 remains the frozen pre-change description from the manifest.

All D0-D3 materialized arms still share the same checked-out instruction body and bundled resources; only the description differs between arms.

Regression coverage added.

Disposition: **FIXED**

---

### IR-06 — obsolete materializer helper remained after D0 repair

Severity: **maintenance**

After removing the old D0/current-description assertion, `_extract_description` became unused.

It was removed rather than retained as dead experiment code.

Disposition: **FIXED**

## 4. Mechanical verification

GitHub Actions workflow:

```text
Verify
run #816
run id 35341428157
```

On implementation commit `0a45a4e3e944ec331c2df725ccd6ccc2086e3e33`, the repository verification step completed successfully before this review artifact was written.

The verification entrypoint covers:

```text
repository skill validation
knowledge routing mechanics
route/source validation
existing behavioral corpus validation
behavioral harness unit tests
Pressure Discovery tests
work-episode tests
UTF-8 hygiene
generated-artifact hygiene
```

No live model-behavior claim is inferred from this mechanical pass.

## 5. Review of architecture boundaries

The implementation did not introduce:

```text
a second top-level marketing skill
a capability ontology runtime
a relation graph engine
graph metadata in routing-index.json
a universal marketing checklist
fixed top-k retrieval
load-all behavior
new handbook knowledge
new owner taxonomy
private chain-of-thought logging
weakened runner activation semantics
```

The bounded architecture remains:

```text
top-level description
→ activation

current job
→ settled state
→ localize open scope
→ reuse sufficient state
→ JIT owner/read only where unresolved
→ coverage-aware stop
→ output
```

## 6. Remaining non-blocking uncertainties

### Live activation effect is unknown

The D3 description is now implemented as the candidate, but no live D0-vs-D3 host activation experiment has been run.

Therefore this review does not claim:

```text
higher activation recall
lower false activation
or net routing improvement
```

### Live coverage effect is unknown

The C1 coverage rule is implemented and the oracle/classifier can measure partial required-set walks, but no live C0-vs-C1 run has been executed.

Therefore this review does not claim:

```text
lower premature closure rate
unchanged over-read rate
or improved final answer quality
```

### Activation-negative telemetry remains evidence-limited

The activation lane intentionally reports:

```text
activation observed
vs
activation not observed
```

and does not convert missing telemetry into an unsupported universal statement that the host definitely did not consider the skill.

## 7. Packaging limitation in this review environment

The connected GitHub tool can inspect and modify repository files but does not expose repository archive/tree download, while the code-execution container has no outbound GitHub network access.

Therefore a complete local `skill.zip` could not be reconstructed in this session without manually transferring the full skill tree.

This does not affect repository CI validation, which runs against the full checked-out skill. It does mean this review does not claim that a separate distributable ZIP was produced locally.

## 8. Review verdict

Current verdict:

```text
IMPLEMENTATION CONSISTENT WITH DESIGN FREEZE
MECHANICAL VERIFICATION PASS
NO OPEN BLOCKING CODE/DESIGN FINDINGS FROM SELF-REVIEW
LIVE BEHAVIOR UNPROVEN
KEEP PR DRAFT UNTIL MERGE INTENT IS EXPLICIT
```

The candidate is materially better specified than the pre-review implementation because the review removed three ways the coverage mechanism could undermine the repository's existing state-preservation/JIT principles:

```text
stacked-label telemetry loss
settled-ICP reopening
load-every-open-surface interpretation
```

No further architecture expansion is justified by the static review.
