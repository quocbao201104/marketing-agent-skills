# Korean Local Adaptation — Independent Implementation Review Result

Status: **POST-IMPLEMENTATION INDEPENDENT REVIEW RECORDED**  
Review date: 2026-09-17  
Frozen research target: `fcebad983691851d75017487e4f650aff8a5512e`  
Independent research review: `07c1fc481207c856980072be664034db464e43cf`  
Frozen runtime implementation target: `b52dad48d7d2436f27161badfcd42377aff5d5cf`

## Verdict

```text
PASS
```

The frozen runtime implementation faithfully promotes the research-approved `KO-LANG-SPEECH-01` contribution without broadening the mechanism, evidence scope, activation authority, or architecture.

```text
KO-LANG-SPEECH-01
→ IMPLEMENTATION PASS

RUNTIME EVIDENCE KOLA01–KOLA11
→ PASS

K1–K16 EVAL COVERAGE
→ PASS

VN / JP / ES REGRESSION
→ PASS

ARCHITECTURE
→ PASS

LIFECYCLE / PROVENANCE
→ PASS

BOUNDED REPAIR
→ NONE
```

This review adjudicates the frozen implementation at `b52dad48d7d2436f27161badfcd42377aff5d5cf`. No commit after that target is used as evidence that a defect was repaired. The review commit records this result only and does not modify runtime implementation files.

---

# A. Implementation faithfulness to frozen research

The runtime contribution remains the same mechanism approved by the independent research review:

```text
KO-LANG-SPEECH-01
Korean addressee speech-level realization
```

The implementation does not broaden the candidate into a Korea market profile, a general Korean honorific module, a hierarchy system, or a style/politeness score.

The promotion-bearing novelty remains exactly the narrow Korean-specific realization knowledge approved by research review:

```text
FORMAL / NON-FORMAL REGISTER
!= ONE MONOTONIC ADDRESSEE-RESPECT SCALE
```

and:

```text
ONE RELATIONSHIP
!= ONE INVARIANT SPEECH LEVEL

SUPPORTED 하십시오체 ↔ 해요체 SHIFT
!= AUTOMATIC DRIFT

MIXED SPEECH LEVELS
!= AUTOMATIC ERROR
!= AUTOMATICALLY VALID
```

The runtime unit carries those distinctions directly into its `CLAIM`, `DECISION IMPACT`, `LOAD WHEN`, `DO NOT USE WHEN`, `MUST PRESERVE`, `MUST NOT INFER`, and `REALIZATION GUARDRAILS` sections.

The implementation remains an input-consuming realization constraint. It does not decide hierarchy, familiarity, intimacy, authority, seniority relationship, customer deference, brand-wide speech level, or market preference.

**Faithfulness verdict: PASS.**

---

# B. Runtime evidence-ledger adjudication — KOLA01–KOLA11

This section checks whether `skills/marketing-agent-skills/references/local-adaptation-korean-evidence.md` preserves the scope accepted by frozen research and independent research review. It does not reopen the completed research review or use later commits as repaired evidence.

## KOLA01 — PASS

Runtime support remains limited to Korean addressee speech-level realization through sentence-final endings and the six recorded speech levels.

The runtime ledger still explicitly rejects:

- a universal brand preference;
- customer-to-ending lookup;
- equal commercial currency of all six styles;
- a global commercial ranking.

No scope expansion appears.

## KOLA02 — PASS

Runtime evidence preserves the approved distinction:

```text
격식체 / 비격식체
!= ONE HIGHER-RESPECT / LOWER-RESPECT AXIS
```

It does not convert formal style into a professional default, nor non-formal style into a persuasion rule.

## KOLA03 — PASS

Runtime evidence keeps the same-listener contextual-shifting claim narrow: mixed formal/non-formal usage can be legitimate depending on situation and cannot be declared wrong without context.

It explicitly rejects the invalid reverse inference that every mixed draft is natural, intentional, or valid.

## KOLA04 — PASS

Runtime evidence preserves the bounded `하십시오체 ↔ 해요체` style-shifting result in formal news-interview situations.

It does not promote the study into:

- a universal switching frequency;
- a rule that every formal interaction should mix styles;
- marketing-effect evidence;
- organization voice policy.

## KOLA05 — PASS

Runtime evidence keeps subject, object/action-target, and addressee honorification as distinct grammatical dimensions.

It explicitly states that this does not justify:

- one runtime unit per honorification mechanism;
- a hierarchy graph;
- a rank resolver;
- population or marketing preference.

This remains a scope/composition boundary, not a second promoted Korean mechanism.

## KOLA06 — PASS

Runtime evidence preserves the coexistence boundary: object honorification and addressee speech level can occur in the same clause without being the same decision.

No universal `드리다` rule, hierarchy inference, or separate object-honorification runtime owner is introduced.

## KOLA07 — PASS

KB remains explicitly first-party organization/customer-language policy only.

The runtime ledger supports only that one organization may use different speech styles by purpose, target, situation, or surface/function.

It explicitly rejects:

```text
KB POLICY
→ KOREAN POPULATION PREFERENCE
```

and rejects banking-wide or universal mappings such as:

```text
policy → 하십시오체
CTA → 해요체
```

No population-rule upgrade occurs.

## KOLA08 — PASS

The TV-ad study remains distribution/context evidence only.

The runtime ledger preserves the sampled 1,750-sentence scope and the 57.6% non-final result while rejecting:

- current universal Korean-advertising norms;
- causal effectiveness;
- high-involvement-to-formal prescription;
- cross-channel transfer.

No frequency-to-best-practice promotion occurs.

## KOLA09 — PASS

The advertising experiment remains bounded response evidence.

The runtime ledger keeps the distinction:

```text
MORE FAVORABLE AD ATTITUDE IN TESTED CONDITIONS
!= CONVERSION
!= REVENUE
!= PURCHASE CAUSALITY
!= UNIVERSAL CHANNEL RULE
!= 2026 POPULATION DEFAULT
```

No universal marketing prescription appears.

## KOLA10 — PASS

`사물존대` remains a boundary against simplistic correction logic.

The runtime ledger explicitly rejects both binaries:

```text
inanimate + -시-
→ always wrong
```

and:

```text
customer-related noun + -시-
→ always correct
```

It also states that KOLA10 does not establish promotion of this mechanism inside `KO-LANG-SPEECH-01`.

## KOLA11 — PASS

`압존법` remains anti-resolver evidence.

The runtime ledger rejects:

- listener-rank/referent-rank algorithms;
- hierarchy graphs;
- general workplace/social suppression rules;
- marketing-effect claims.

It defeats rather than creates a hierarchy resolver.

### Runtime evidence summary

```text
KOLA01  PASS
KOLA02  PASS
KOLA03  PASS
KOLA04  PASS
KOLA05  PASS
KOLA06  PASS
KOLA07  PASS
KOLA08  PASS
KOLA09  PASS
KOLA10  PASS
KOLA11  PASS
```

The runtime ledger is slightly more compact than the research ledger in places, but it does not broaden the accepted claim set.

---

# C. K1–K16 implementation-eval adjudication

`evals/local-adaptation-korean-v0.md` is correctly labeled a targeted architecture/regression suite rather than a behavioral benchmark. Its job is to freeze the required semantic and routing boundaries around the implementation.

## K1 — approved `하십시오체` — PASS

The eval requires no reopen when an applicable organization/surface policy already fixes `하십시오체` and no other addressee-ending dimension is open.

This matches runtime `DO NOT USE WHEN` and resolved-state preservation.

## K2 — approved `해요체` — PASS

The eval requires preservation of the approved dimension and no Korean-specific reopening.

## K3 — same brand, different surfaces — PASS

The eval prevents global normalization of one organization to one speech level and keeps first-party state scoped by surface/function.

## K4 — intentional same-listener shift — PASS

The eval explicitly preserves supported `하십시오체 ↔ 해요체` shifting and rejects consistency-only normalization.

The route loads only when realization is actually open/material; merely observing a settled approved shift is not independent activation authority.

## K5 — accidental speech-level drift — PASS

The eval explicitly attacks the opposite failure mode: evidence that mixed usage can exist must not become permission to preserve arbitrary drift.

Resolved `해요체` plus unsupported jumps into `해라체` / `하십시오체` must be repaired toward resolved state.

## K6 — “make it more formal” — PASS

The eval correctly distinguishes a **request to change register** from the bare presence of a `formal` label.

When the ending realization is materially being changed, the unit may load, but it must not convert `formal` into higher respect, hierarchy, or interpersonal distance.

## K7 — “make it friendlier” — PASS

Friendly stance does not authorize automatic downgrade to `해체`.

## K8 — title / button / nominal form — PASS

The eval correctly requires no load for surfaces such as `카드 연결하기` when no finite addressee-ending choice exists.

## K9 — honored third-party subject, ending fixed — PASS

Only subject honorification remains open; the Korean speech-level unit must not seize ownership.

## K10 — subject honorification + `해요체` coexist — PASS

The eval explicitly prevents the false `double politeness` collapse and keeps the two grammatical dimensions distinct.

## K11 — `사물존대` edge — PASS

The eval keeps the issue outside the promoted mechanism unless an addressee-ending decision is separately open, and rejects an inanimate/customer lookup rule.

## K12 — `압존법` hierarchy cue — PASS

The eval explicitly forbids mechanical suppression from rank order and forbids a hierarchy resolver.

## K13 — Korean outside Korea — PASS

Activation follows Korean target-language realization, not Korea-market membership.

## K14 — Korea market, English output — PASS

Geography alone does not activate Korean sentence-ending knowledge.

## K15 — relationship known, speech level unresolved — PASS

The eval requires preservation of uncertainty and rejects:

```text
standard Korean → 하십시오체
marketing → 해요체
customer → 하십시오체
```

## K16 — Korean noun / market mention only — PASS

Korean/Korea nouns without a material finite addressee-ending decision do not activate the unit.

### K1–K16 summary

```text
K1   PASS
K2   PASS
K3   PASS
K4   PASS
K5   PASS
K6   PASS
K7   PASS
K8   PASS
K9   PASS
K10  PASS
K11  PASS
K12  PASS
K13  PASS
K14  PASS
K15  PASS
K16  PASS
```

The eval additionally includes non-speech-level negative controls for particle/case grammar, counting/noun-expression issues, and temporal/semantic incoherence, which correctly prevents the unit from expanding into a general Korean proofreading module.

---

# D. Novelty and scope-boundary review

## Promotion-bearing novelty — PASS

Runtime novelty remains limited to Korean addressee speech-level realization.

The implementation directly preserves the two discriminating research deltas:

```text
격식체
!= AUTOMATICALLY HIGHER ADDRESSEE RESPECT
```

and:

```text
ONE BROAD RELATIONSHIP
!= ONE INVARIANT SPEECH LEVEL
```

with the further necessary distinction:

```text
SUPPORTED 하십시오체 ↔ 해요체 SHIFT
!= AUTOMATIC DRIFT

MIXED SPEECH LEVELS
!= AUTOMATICALLY VALID
```

No broader claim is needed to justify the runtime unit.

## Subject/object honorification — PASS

The implementation treats:

```text
ADDRESSEE SPEECH LEVEL
!= SUBJECT HONORIFICATION
!= OBJECT / ACTION-TARGET HONORIFICATION
```

as a scope/composition boundary.

It explicitly says that when only `-시-`, lexical object honorification, or another subject/object issue remains open, `KO-LANG-SPEECH-01` must not seize the decision.

It also explicitly states:

```text
KO-LANG-HON-02
→ NOT JUSTIFIED
```

No second Korean unit is silently promoted.

## `사물존대` — PASS

No binary lookup or customer-service correction table appears in runtime.

## `압존법` — PASS

No rank graph, listener/referent comparison algorithm, or suppression resolver appears.

## First-party KB policy — PASS

KB stays organization/surface state within its own scope and does not become Korean population truth.

## Advertising evidence — PASS

KOLA08/KOLA09 remain context/response evidence only and do not become a style winner, conversion rule, or channel prescription.

---

# E. Negative activation review

Runtime activation remains decision-first:

```text
TARGET LANGUAGE = KOREAN
+
ADDRESSEE SPEECH-LEVEL REALIZATION
IS MATERIALLY OPEN OR BEING CHANGED
+
THE CHOICE CAN ALTER
ADDRESSEE RESPECT / REGISTER /
INTERPERSONAL DISTANCE / DISCOURSE FUNCTION
```

The implementation explicitly rejects noun/status activation from Korean, Korea, customer status, age, seniority, business context, marketing, social media, organization membership, and broad culture.

A bare `formal` descriptor likewise does not satisfy `LOAD WHEN` by itself. K6 is different: an explicit request to **change Korean formality/register** can make the sentence-ending realization materially open, at which point the unit may load while preserving the existing relationship and respect state.

Therefore:

```text
FORMAL LABEL ALONE
!= ACTIVATION

MATERIALLY CHANGING KOREAN ENDING REGISTER
→ MAY ACTIVATE
```

This preserves the frozen K6 / negative-activation distinction.

**Negative activation verdict: PASS.**

---

# F. VN / JP / ES semantic regression review

From the independent research-review commit to the frozen implementation target, the implementation delta is confined to:

```text
evals/local-adaptation-korean-v0.md
skills/marketing-agent-skills/adaptations/localization.md
skills/marketing-agent-skills/references/local-adaptation-korean-evidence.md
```

Within `adaptations/localization.md`, the Korean unit is appended under the existing `## Relationship realization` section. Existing VN/JP/ES contribution semantics are not rewritten by the Korean implementation.

The units remain compositionally distinct:

```text
VN-LANG-REL-01
→ Vietnamese coupled self-reference / recipient-address realization

JP-LANG-HON-01
→ Japanese honorific-target participant orientation

JP-LANG-PERM-01
→ Japanese permission / benefit-sensitive deferential realization

ES-LANG-ADDR-01
→ Spanish second-person treatment-system realization

KO-LANG-SPEECH-01
→ Korean sentence-ending addressee speech-level realization
```

The Korean contribution does not redefine another unit's scope, activation, evidence, or owner.

**Regression verdict: PASS.**

---

# G. Architecture review

The frozen implementation does not introduce architecture machinery beyond the existing local-adaptation contract.

```text
route
→ adapt-localization.relationship-realization

new owner
→ NO

new route
→ NO

controller change
→ NO

Chapter 07 change
→ NO

routing-index.json change
→ NO

get-knowledge.py change
→ NO

shared primitive
→ NO

hierarchy resolver
→ NO

speech-level score
→ NO

Korea country pack
→ NO

Korean-specific loader
→ NO
```

The existing architecture remains sufficient:

```text
CURRENT JOB
→ Chapter 07 localization owner
→ bounded JIT lookup
→ adapt-localization.relationship-realization
→ section-local contribution scope check
→ apply only the materially open target-language constraint
```

No concrete discovery, addressability, applicability, or composition failure justifies additional machinery.

**Architecture verdict: PASS.**

---

# H. Lifecycle / provenance adjudication

Frozen runtime state:

```text
REVIEW STATE = provisional
USAGE STATE = active
```

This is correct provenance **before** independent implementation review.

The adaptation contribution contract defines the two fields independently:

```text
REVIEW STATE
provisional | reviewed

USAGE STATE
active | contested | deprecated
```

and states that review state records contribution vetting while usage state records current repository disposition.

Therefore:

```text
provisional
→ correctly records that independent implementation review
  had not yet happened at frozen target
```

while:

```text
active
→ records that the runtime contribution is installed/currently usable
  as repository disposition
```

`active` does not imply `reviewed`, and `provisional` does not require the unit to be `contested` or `deprecated`.

The frozen implementation therefore avoids the lifecycle defect in which an implementation claims `reviewed` before independent implementation review has actually occurred.

After this review result exists, a later lifecycle-only commit may change `REVIEW STATE` to `reviewed` if the repository workflow chooses to record the completed vetting in runtime metadata. Such a change would be a separate post-review delta, not evidence used to adjudicate the frozen target and not a repair required for this PASS verdict.

**Lifecycle verdict: PASS.**

---

# I. Material findings

No material implementation finding survives review.

```text
FINDINGS
→ NONE

SMALLEST BOUNDED REPAIR
→ NONE REQUIRED
```

No runtime repair is authorized or needed in this review commit.

---

# J. Residual uncertainty

The implementation correctly leaves the following outside runtime defaults:

- exhaustive natural discourse conditions for all Korean speech-level shifts;
- population prevalence of particular levels across industries, demographics, or channels;
- current brand/audience preference absent scoped first-party evidence;
- complete subject/object/indirect-honorification theory;
- disputed `사물존대` edge analyses;
- exhaustive modern `압존법` etiquette conditions;
- causal conversion/revenue effects of speech-level choices;
- LLM-specific error rates.

These unknowns do not justify widening `KO-LANG-SPEECH-01`, creating a second Korean unit, or adding architecture machinery.

---

# Final disposition

```text
TOP-LEVEL VERDICT
→ PASS

KO-LANG-SPEECH-01 IMPLEMENTATION
→ PASS

RUNTIME KOLA01–KOLA11 SCOPE
→ PASS

K1–K16 EVAL
→ PASS

NOVELTY REMAINS KOREAN ADDRESSEE SPEECH-LEVEL REALIZATION
→ YES

KO-LANG-HON-02
→ NOT PROMOTED

사물존대 BINARY LOOKUP
→ NO

압존법 HIERARCHY RESOLVER
→ NO

KB POPULATION RULE
→ NO

ADVERTISING UNIVERSAL PRESCRIPTION
→ NO

VN / JP / ES SEMANTIC REGRESSION
→ NONE FOUND

EXISTING ROUTE
→ PRESERVED

NEW OWNER / ROUTE / CONTROLLER / CHAPTER 07 / ROUTING INDEX / LOADER
→ NONE

SHARED PRIMITIVE / HIERARCHY RESOLVER / SPEECH-LEVEL SCORE
→ NONE

LIFECYCLE AT FROZEN TARGET
→ CORRECT: provisional + active

BOUNDED REPAIR
→ NONE

RUNTIME MODIFIED BY REVIEW COMMIT
→ NO
```
