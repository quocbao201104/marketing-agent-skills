# Skill Retrieval and Coverage — Design Freeze

Current coverage semantics are amended by [Precision Corrections](04-precision-corrections.md); the original route-count design below is retained as historical provenance.

Status: **FROZEN FOR BOUNDED IMPLEMENTATION EXPERIMENT — LIVE BEHAVIOR NOT YET ESTABLISHED**  
Freeze date: 2026-09-18  
Repository base: `main@c12a7e2760636bed76551e897c0419273296a684`  
Candidate branch: `research/skill-retrieval-coverage-freeze`

This freeze consolidates the activation, retrieval, coverage, composition, and evaluation research performed against the current Marketing Practitioner runtime. It authorizes only the smallest experiments needed to test the two demonstrated architecture pressures below.

It does **not** establish that the current live model fails either pressure at an unacceptable rate, and it does **not** authorize a routing-index redesign, handbook ontology, capability graph engine, additional top-level skill, or broad controller rewrite.

---

## 1. Frozen research question

Two runtime failures are under test:

### RQ-A — top-level skill discovery / activation

When a user presents a marketing or founder-led-sales problem without naming the relevant marketing framework, artifact, or capability, does the host reliably recognize that `marketing-agent-skills` should be activated?

The failure of interest is:

```text
RELEVANT SKILL EXISTS
+
USER EXPRESSES A LATENT JOB / BUSINESS SYMPTOM
+
ROUTING METADATA DOES NOT MAKE THE OWNED JOB LEGIBLE ENOUGH
=
ACTIVATION MISS
```

The opposite failure is also material:

```text
MARKETING-ADJACENT NOUN APPEARS
+
NO MARKETING / SALES DECISION OR SEMANTIC EXECUTION IS ACTUALLY OPEN
+
SKILL ACTIVATES ANYWAY
=
FALSE ACTIVATION
```

### RQ-B — internal multi-route coverage

After `marketing-agent-skills` has activated, can the controller distinguish a bounded open question from a broad unresolved problem whose materially decision-changing owners have not yet been localized?

The failure of interest is:

```text
BROAD / UNCERTAIN JOB
+
ONE OR MORE PLAUSIBLE ROUTES ARE FOUND
+
OTHER MATERIAL OPEN DECISION SURFACES REMAIN UNLOCALIZED OR UNRESOLVED
+
AGENT STOPS
=
PREMATURE CLOSURE
```

The opposite failure is over-routing:

```text
BOUNDED JOB
+
SETTLED STATE IS ALREADY SUFFICIENT
+
COVERAGE MECHANISM OPENS UNRELATED OWNERS
=
OVER-READ / WRONG EDGE
```

---

## 2. External research basis

The following external findings survive into this freeze as architecture-relevant evidence, not as direct runtime claims about this repository.

### Progressive disclosure makes metadata a real routing surface

OpenAI skill documentation states that ChatGPT and Codex begin with skill `name` and `description`, then load the full `SKILL.md` after deciding to use the skill. Codex also budgets the initial skill list, shortening descriptions first and potentially omitting skills from large initial lists.

Relevant sources:

- OpenAI, **Build skills**: <https://developers.openai.com/docs/build-skills>
- OpenAI, **Use skills to speed up OSS maintenance**: <https://developers.openai.com/blog/skills-agents-sdk>
- OpenAI API, **Skills**: <https://developers.openai.com/api/docs/guides/tools-skills>

Frozen implication:

```text
description
!= decorative summary

description
= pre-activation routing contract
```

### Skill retrieval remains a distinct systems problem

**SkillRet: A Large-Scale Benchmark for Skill Retrieval in LLM Agents** evaluates realistic skill retrieval at scale and reports that generic retrieval remains far from solved, especially when skill-relevant signals are sparse inside long or noisy requests.

Source:

- <https://arxiv.org/abs/2605.05726>

Frozen implication:

```text
user wording
!= reliable capability name

latent job / symptom recognition
is part of retrieval quality
```

### Metadata-only selection can miss decisive body-level distinctions

**SkillRouter: Retrieve-and-Rerank Skill Selection for LLM Agents at Scale** reports large degradation when retrieval loses skill-body evidence and highlights heavy functional overlap among skills.

Source:

- <https://arxiv.org/abs/2603.22455>

This repository contains one large top-level skill rather than ~80K peer skills, so the paper does **not** justify a body-level external router here.

The narrow retained implication is:

```text
routing metadata must carry the most discriminating
pre-activation information available within its budget
```

### Multi-skill routing depends on decomposition and composition

**Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose** finds task decomposition to be a major bottleneck and improves it by feeding available skill information back into decomposition.

Source:

- <https://arxiv.org/abs/2606.18051>

**Generative Skill Composition for LLM Agents** formalizes skill composition as a joint decision over which skills, how many, and in what order.

Source:

- <https://arxiv.org/abs/2606.32025>

Frozen implication:

```text
"find one relevant route"
!=
"localize the complete-enough material decision space"
```

The repository already has owner, dependency, handoff, and JIT-routing machinery, so the implementation consequence is intentionally smaller than the generic research architecture.

---

## 3. Repository facts established by audit

The current repository is not a flat set of independent top-level skills.

The relevant runtime shape is:

```text
marketing-agent-skills
        ↓
SKILL.md controller
        ↓
foundational handbook owners
+
logical specialist routes
+
platform / adaptation modules
```

The current runtime already contains the following useful machinery:

```text
job-first routing
resolved-state preservation
open-decision ownership
dependency-aware routing
smallest relevant read
stable-section JIT
conditional expansion
handoffs
route tracing
behavioral route oracles
fast-path protection
```

The current controller also already states principles equivalent to:

```text
follow dependencies rather than nouns

evidence → positioning → message → copy
is conditional, not a mandatory pipeline

expand only when the unresolved dependency
crosses a relevant boundary
```

Therefore the frozen architecture verdict is:

> The repository does **not** need a new routing system. It needs a bounded activation-surface experiment and a bounded broad-problem coverage-control experiment.

---

## 4. Demonstrated design pressure A — metadata budget allocation

Current description at the freeze base is approximately 95 words and contains four conceptual parts:

```text
identity / high-level scope
capability inventory
post-activation runtime behavior
broad exclusion
```

A substantial portion of the description explains behavior that is already available only after activation, including preserving resolved decisions, loading only decision-changing knowledge, separating observation from interpretation, matching claims to proof, and preserving uncertainty.

Those rules are valuable, but the full `SKILL.md` body already owns them.

The pre-activation description has weaker representation of:

```text
latent user jobs
business symptoms
problem states
adjacent-but-non-owned tasks
noun traps
```

This is an established **design pressure**, not yet a demonstrated live regression.

### Frozen hypothesis H-A

Reallocating description budget from post-activation process prose toward job ownership, symptom classes, and sharper exclusion boundaries will improve activation on paraphrased / symptom-led / noisy marketing tasks without causing systematic false activation on adjacent or mechanical tasks.

---

## 5. Demonstrated design pressure B — broad-problem scope localization

The current controller is strong once an open question is already localized:

```text
OPEN QUESTION
→ OWNER
→ SMALLEST MATERIAL KNOWLEDGE
→ RESOLVE
→ RETURN
```

The pressure appears earlier:

```text
BROAD PROBLEM
→ ? COMPLETE-ENOUGH MATERIAL QUESTION SET
→ OWNER(S)
```

Current instructions strongly optimize for the smallest relevant read and stopping when further information is unlikely to change the current choice enough to justify cost.

That is correct for bounded work.

For broad diagnostic or strategic jobs, however, a first plausible explanation can appear sufficient before every materially decision-changing surface has been localized.

The gap is not lack of knowledge, route IDs, or owner semantics.

It is:

```text
BROAD-PROBLEM SCOPE LOCALIZATION
+
COVERAGE-AWARE STOPPING
```

### Frozen hypothesis H-B

A small controller refinement that distinguishes bounded open questions from broad unresolved jobs, localizes only material decision surfaces, and forbids stopping while a localized material surface remains unresolved will reduce partial required-set walks without increasing over-read on narrow tasks.

---

## 6. Frozen runtime model

The implementation experiment must preserve the following shape:

```text
USER JOB
   ↓
RESOLVED STATE
   ↓
LOCALIZE OPEN SCOPE
   │
   ├─ bounded
   │    ↓
   │  current narrow path
   │
   └─ broad / materially unresolved
        ↓
      small set of material decision surfaces
        ↓
      resolved / open / bounded-out
        ↓
SELECT OWNERS BY DEPENDENCY
   ↓
SMALLEST JUSTIFIED ROUTES
   ↓
RESOLVE / PASS FORWARD MINIMAL STATE
   ↓
COVERAGE-AWARE STOP
   ↓
MINIMUM SUFFICIENT OUTPUT
```

Frozen principle:

> **Cover decisions broadly enough; read knowledge narrowly.**

This explicitly rejects:

```text
load all potentially related knowledge
```

and also rejects:

```text
find one plausible route
→ call the problem covered
```

---

## 7. Protected surfaces

The first implementation experiment must **not** modify:

```text
skills/marketing-agent-skills/routing-index.json
skills/marketing-agent-skills/scripts/get-knowledge.py
skills/marketing-agent-skills/handbook/*
skills/marketing-agent-skills/platforms/*
skills/marketing-agent-skills/adaptations/*
evals/behavioral/behavioral_eval/runner.py
existing owner boundaries
existing logical route IDs
release/version metadata
```

Reason:

- `routing-index.json` is an address table and should not become an ontology or workflow engine.
- handbook knowledge has not been demonstrated as the bottleneck.
- the helper already resolves logical IDs.
- `runner.py` deliberately treats an unverified activation in the skill arm as operationally invalid; that invariant protects existing behavioral comparisons.
- no evidence currently justifies a second top-level marketing skill or a capability-graph runtime.

---

## 8. Lane A — top-level activation evaluation

Activation evaluation is a separate lane from internal route evaluation.

### 8.1 Why a separate lane is required

The current behavioral runner contains this intentional invariant:

```text
workspace-copy skill arm
+
activation not verified
→ ACTIVATION_UNVERIFIED
```

That is correct for the existing positive-skill behavioral suite.

It prevents a missing skill activation from being silently interpreted as a successful skill-arm answer.

Negative activation cases therefore must not be forced through normal skill-arm answer adjudication in iteration 1.

### 8.2 Observable activation evidence

Use existing host telemetry:

```text
explicit skill activation event
OR
successful read of marketing-agent-skills/SKILL.md
→ activation observed
```

Absence should initially be reported as:

```text
activation not observed
```

not automatically as a guaranteed non-activation unless the sealed execution contract proves telemetry completeness.

### 8.3 Activation case families

Pilot target: 24 cases, four per family.

```text
A1 DIRECT
explicit marketing / sales job

A2 PARAPHRASE
same owned job without framework vocabulary

A3 SYMPTOM
business symptom implies marketing / sales job

A4 NOISY / CONNECTED
material signal embedded in longer context

A5 ADJACENT NEGATIVE
product, legal, finance, CRM/ops, technical owner

A6 NOUN-TRAP NEGATIVE
marketing noun present but job is mechanical / unrelated
```

Representative metamorphic pairs:

```text
Count characters in this meta description.
→ activation forbidden

Shorten this approved meta description to 150 characters
without changing its marketing meaning.
→ activation required
```

```text
How should an AI agent choose among Skills?
→ activation forbidden

We sell an AI-agent debugging product.
Customers do not understand why it is different from hosted alternatives.
→ activation required
```

```text
Put these eight accounts into HubSpot and create a stage-change automation.
→ activation forbidden

The founder can personally pursue only eight accounts.
Which deserve founder attention and why?
→ activation required
```

### 8.4 Activation oracle

Use a sidecar oracle rather than changing `CaseContract`.

Candidate:

```text
evals/behavioral/oracles/
  skill-activation-v1.activation-oracle.json
```

Minimal semantics:

```json
{
  "case@version": {
    "activation": "required"
  }
}
```

or:

```json
{
  "case@version": {
    "activation": "forbidden"
  }
}
```

### 8.5 Activation failure taxonomy

```text
activation_required + activation_observed
→ activation_ok

activation_required + activation_not_observed
→ no_activation / activation_unverified

activation_forbidden + activation_observed
→ false_activation

activation_forbidden + activation_not_observed
→ no_false_activation_observed
```

Do not overload `no_activation` as a universal quality judgment. Its meaning depends on the case expectation.

---

## 9. Activation description ablation

Freeze four variants.

### D0 — current

Unmodified current description.

### D1 — routing-budget cleanup

Preserve the current capability breadth but remove most post-activation process prose from the description.

Question under test:

> Does freeing routing budget alone improve discovery?

### D2 — job-centered

Represent the owned work in practitioner-job terms rather than primarily repository-taxonomy terms.

Candidate job classes:

```text
understand
choose
diagnose
design
communicate
test
adapt
learn
```

Question under test:

> Does job ownership improve paraphrase routing without symptom examples?

### D3 — job + symptom + boundary

Add compact latent-problem classes and sharper adjacent exclusions.

Candidate symptom classes:

```text
unclear differentiation
uncertain target choice
weak or changing conversion
conflicting performance signals
unclear value / commercial fit
stalled buyer progress
```

Candidate boundary classes:

```text
generic writing
mechanical content operations
product-roadmap work
legal work
finance/accounting work
CRM operations
unrelated technical work
```

D3 is a hypothesis candidate, not the predetermined winner.

### 9.1 Experimental controls

Hold constant:

```text
SKILL.md body
routing index
knowledge files
model
reasoning effort
case corpus
repetitions
workspace regime
```

Only the description may differ.

Keep variants within a comparable routing budget rather than allowing length alone to become the treatment.

---

## 10. Lane B — internal coverage evaluation

Use the existing behavioral route oracle.

No route-oracle schema v2 is justified for the first experiment.

Current `must_load` already supports multiple requirement groups:

```json
"must_load": [
  ["diagnosis", "handbook/05-diagnosis-causality-and-experimentation.md"],
  ["paid-media.observation", "paid-media"],
  ["segmentation", "handbook/02-segmentation-icp-and-jtbd.md"],
  ["positioning", "handbook/03-positioning-and-value.md"]
]
```

Interpretation:

```text
group 1
AND group 2
AND group 3
AND group 4
```

Alternatives inside one group are acceptable representatives of the same requirement.

This is sufficient to test full required-set coverage.

---

## 11. Coverage trace refinement

Current trace classification maps missing required groups to `skip_jit`.

Add observable counts:

```text
required_group_count
satisfied_group_count
missing_groups
```

Add one new primary failure:

```text
premature_closure
```

Candidate semantics:

```text
required_group_count >= 2
AND
0 < satisfied_group_count < required_group_count
AND
run completed
→ premature_closure
```

Existing `skip_jit` may remain as a secondary label for backward compatibility.

Distinguish:

```text
0 satisfied + required missing
→ skip_jit

partial required set satisfied
→ premature_closure

all required groups satisfied
→ coverage complete
```

No private chain-of-thought, hidden reasoning ledger, or self-reported "I considered X" is required.

---

## 12. Coverage case families

Pilot target: 12 cases, three per family.

### C1 — genuine multi-owner diagnosis

A broad observation has multiple materially plausible owners.

Pass requires the route walk to cover the required set rather than stop after one plausible explanation.

### C2 — narrow sibling / materiality control

A minimally changed sibling removes one or more material dependencies.

Pass requires the controller **not** to open those owners merely because the prompt contains the same nouns.

### C3 — strategic dependency

Several owners form a real conditional dependency, for example:

```text
customer evidence
→ segment choice
→ positioning consequence
```

Pass requires the necessary handoff without converting it into a universal pipeline.

### C4 — fast-path regression guard

Bounded transformations and resolved-state tasks.

Pass requires the coverage mechanism to remain effectively invisible.

---

## 13. Coverage controller ablation

Only two variants are authorized.

### C0 — current controller

Unmodified current runtime controller.

### C1 — bounded coverage refinement

The candidate may add only the following semantics:

```text
For a bounded unresolved question,
keep the current narrow path.

When the useful result is broad and the material causes,
decision owners, or dependencies are not yet localized,
first identify the small set of unresolved decision surfaces
that could materially change the result.

Treat a surface as open only when current evidence or task scope
leaves it materially unresolved. Do not activate a surface merely
because its topic is mentioned.

Route each open surface to its owner and smallest useful knowledge.

Do not stop after resolving one plausible path while another
material unresolved surface remains.
```

Final wording may be compressed during implementation as long as these semantics survive.

No fixed marketing checklist is allowed.

---

## 14. Experimental order

Do not change metadata and controller behavior simultaneously.

### Study 1 — activation

```text
D0
D1
D2
D3
↓
development cases
↓
select candidate D*
↓
freeze
↓
holdout + challenge cases
```

### Study 2 — coverage

With `D*` fixed:

```text
D* + C0
vs
D* + C1
↓
multi-owner
narrow sibling
strategic dependency
fast-path guard
↓
select C*
```

### Study 3 — end-to-end regression

```text
ORIGINAL
D0 + C0

vs

CANDIDATE
D* + C*
```

Run relevant existing behavioral suites plus the new activation and coverage cases.

Do not infer the effect of one layer from a simultaneous multi-layer patch.

---

## 15. Activation metrics and gates

Report separately:

```text
direct activation-observed rate
paraphrase activation-observed rate
symptom activation-observed rate
noisy activation-observed rate
adjacent false-activation-observed rate
noun-trap false-activation-observed rate
repeat instability
```

Do not collapse these into one scalar during development.

### Non-compensatory promotion gates

A candidate description may advance only if:

```text
DIRECT
no material regression

LATENT
improvement is repeated across paraphrase / symptom / noisy families,
not one memorized wording

NEGATIVE
no systematic new false activation

STABILITY
gain survives repeats
```

Higher latent recall does not compensate for broad adjacent false activation.

---

## 16. Coverage metrics and gates

Report:

```text
full required-set coverage
premature_closure
skip_jit
wrong_edge
over_read
missing_handoff
loaded_but_ignore
unique namespaces loaded
whole-file loads
extra namespaces
```

### Non-compensatory promotion gates

C1 may advance only if:

```text
MULTI-OWNER
full coverage improves
AND premature closure decreases

NARROW / FAST PATH
over_read and wrong_edge do not materially increase

ANSWER QUALITY
behavioral output does not regress

EFFICIENCY
coverage improvement is not achieved by indiscriminate loading
```

A candidate that loads every plausible owner is a failure even if full-set recall rises.

---

## 17. Failure taxonomy additions

Keep the existing trace vocabulary and add only:

```text
false_activation
premature_closure
```

Target symmetry:

```text
                 TOO LITTLE        CORRECT          TOO MUCH

TOP LEVEL        no activation     activation       false activation

INTERNAL         premature         sufficient       over_read /
                 closure           coverage         wrong_edge
```

This table is the frozen mental model for the track.

---

## 18. Candidate change surface

If implementation begins after this freeze, the first candidate should be limited to:

```text
skills/marketing-agent-skills/SKILL.md
  - description variant
  - bounded scope-localization / coverage-stop refinement

evals/behavioral/behavioral_eval/trace.py
  - satisfied-group accounting
  - premature_closure classification
  - activation-lane report/classification support if needed

evals/behavioral/tests/test_trace.py
  - none / partial / full required-set tests
  - false-activation classification tests if activation support lives here

evals/behavioral/cases/
  - skill-activation-v1.json
  - coverage-routing-v1.json

evals/behavioral/oracles/
  - skill-activation-v1.activation-oracle.json
  - coverage-routing-v1.route-oracle.json
```

A small dedicated activation evaluator is allowed if that preserves the runner invariant more cleanly than extending `trace.py`.

---

## 19. Explicit non-goals

This track does not authorize:

```text
new top-level marketing skills
skill family split
capability ontology runtime
capability graph engine
graph metadata in routing-index.json
mandatory load-all behavior
universal marketing checklist
fixed top-k route count
new handbook chapters
new platform modules
new owner taxonomy
new state bus
private chain-of-thought logging
self-reported "considered capabilities" as correctness evidence
runner weakening for negative activation cases
version bump before behavior is established
```

Generic research architectures may contain these components. This repository has not demonstrated a need for them.

---

## 20. Rollback / rejection rules

Reject or roll back the candidate when any of the following occurs:

### Metadata candidate rejection

```text
latent activation improves only on development wording
false activation rises materially on adjacent tasks
noun-trap activation rises
direct activation regresses
holdout gain disappears
```

### Coverage candidate rejection

```text
premature_closure falls only because unrelated routes are loaded
fast-path over-read rises
resolved state is reopened more often
wrong owner / forbidden path rises
answer quality regresses
controller wording creates a fixed checklist in practice
```

### Architecture-reopen gate

Reopen the protected architecture only after a concrete live failure shows that:

```text
the correct owner / route cannot be represented
OR
the current oracle cannot express the valid route set
OR
bounded scope localization cannot be implemented
without a new shared runtime primitive
```

Do not reopen architecture from theory alone.

---

## 21. Evidence interpretation rules

A correct final answer does not prove correct activation or routing.

A correct route walk does not prove a good answer.

A missing activation receipt does not automatically prove non-activation unless the execution contract guarantees complete capture.

A route mentioned in the prompt does not establish that it is material.

A route not loaded does not establish irrelevance.

A new rule should not be retained because it is elegant; it must survive the bounded regression gates above.

---

## 22. Implementation sequence

After independent review of this freeze:

```text
1. Add activation corpus + sidecar oracle + evaluator/report
2. Add D0-D3 description variants without changing controller body
3. Run activation development experiment
4. Freeze D*
5. Run activation holdout / challenge
6. Add coverage corpus using existing route-oracle schema
7. Add satisfied-group accounting + premature_closure classifier
8. Add C1 controller candidate
9. Run D*+C0 vs D*+C1
10. Run original vs combined candidate regression
11. Promote only if all non-compensatory gates pass
12. Otherwise keep current runtime and preserve the research result
```

No live experiment result is claimed by this document.

---

## 23. Final frozen verdict

### What is established

```text
- skill metadata is a real pre-activation routing surface;
- current description spends meaningful routing budget on post-activation behavior;
- current behavioral telemetry can observe positive activation;
- current runner intentionally assumes skill-arm activation is required;
- current route oracle can already express multi-group required coverage;
- current trace can observe missing required routes;
- current controller already has strong JIT, dependency, state-preservation,
  and fast-path machinery;
- routing-index.json does not need to become a workflow / ontology layer;
- broad-problem scope localization is less explicit than bounded-question routing;
- a partial required-set walk is currently collapsed into the broader skip_jit class.
```

### What remains a live hypothesis

```text
H-A:
job / symptom / boundary-oriented metadata improves useful auto-activation
without unacceptable false activation.

H-B:
bounded broad-scope localization + coverage-aware stopping reduces
partial required-set walks without causing over-routing.
```

### Smallest authorized response

```text
MEASURE ACTIVATION
→ TUNE DESCRIPTION ONLY IF EVIDENCE SUPPORTS IT
→ MEASURE PARTIAL COVERAGE
→ ADD ONE BOUNDED CONTROLLER RULE ONLY IF IT HELPS
→ PRESERVE EVERYTHING ELSE
```

This research track is frozen at that boundary.
