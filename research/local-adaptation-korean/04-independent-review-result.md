# Korean Local Adaptation — Independent Adversarial Review Result

Status: **POST-FREEZE INDEPENDENT REVIEW RECORDED**  
Review date: 2026-09-17  
Frozen candidate reviewed: `fcebad983691851d75017487e4f650aff8a5512e`  
Review contract: `03-independent-review-brief.md`

## Verdict

```text
PASS
```

The frozen candidate sustains one Korean-specific local-adaptation mechanism and the existing thin local-adaptation architecture.

```text
KO-LANG-SPEECH-01
→ PROMOTE

EXISTING OWNER
→ PASS

EXISTING ROUTE
→ PASS

SECOND KOREAN UNIT
→ REJECT

NEW SHARED PRIMITIVE / RESOLVER
→ REJECT

NEW OWNER / ROUTE / CONTROLLER CHANGE
→ REJECT
```

This review adjudicates the frozen target only. `03-independent-review-brief.md` was committed after the frozen target and is used only as the review contract; it is not treated as retroactive evidence that the frozen candidate already satisfied the contract. No commit after `fcebad983691851d75017487e4f650aff8a5512e` is used as evidence that a frozen defect was repaired.

---

# A. PROMOTION VERDICT

## KO-LANG-SPEECH-01 — PROMOTE

The promotion gate survives:

```text
LOCAL-SPECIFIC MECHANISM
+
MATERIAL DECISION DELTA
+
GENERIC OWNER DOES NOT ALREADY KNOW
THE TARGET-SPECIFIC MECHANISM
=
VALID ADAPTATION
```

The promotion-bearing novelty is specifically Korean sentence-ending addressee speech-level realization, not the broad observation that Korean has honorifics.

The decisive Korean-specific facts are:

```text
FORMAL / NON-FORMAL REGISTER
!= ONE MONOTONIC ADDRESSEE-RESPECT SCALE
```

and:

```text
ONE SPEAKER + ONE LISTENER + ONE BROAD RELATIONSHIP
CAN STILL SUPPORT CONTEXTUAL SPEECH-LEVEL SHIFTING

SUPPORTED 하십시오체 ↔ 해요체 SHIFT
!= AUTOMATIC DRIFT
```

Generic Chapter 07 already preserves resolved relationship, authority, organization state, and uncertainty. `VN-LANG-REL-01`, `JP-LANG-HON-01`, `JP-LANG-PERM-01`, and `ES-LANG-ADDR-01` already supply other language-specific realization constraints. None of them encodes the Korean-specific formal/non-formal classification or the Korean same-listener `하십시오체 ↔ 해요체` style-shifting fact.

Removing Korean-specific knowledge therefore changes the reliability of the decision in the discriminating cases: a consistency-oriented editor can incorrectly normalize a legitimate shift, and a generic `make it more formal` transformation can incorrectly treat formality as an instruction to increase addressee deference or relationship distance.

The subject/object/addressee distinction is important but is **not independently promotion-bearing novelty**. `JP-LANG-HON-01` already supplies a generic architectural warning against collapsing addressee, actor/referent, and action target, while KOLA05–KOLA06 establish the Korean grammatical boundary needed to stop `KO-LANG-SPEECH-01` from seizing subject/object honorification. The frozen design already states this and rejects `KO-LANG-HON-02`; no repair or split is required.

---

# B. SOURCE ADJUDICATION

Independent source re-check did not identify a promotion-bearing claim broader than the frozen ledger records.

## KOLA01 — PASS

The NIKL advisory supports the recorded core fact that Korean `상대 높임법` is realized through sentence-final ending choice and includes `해라체`, `하게체`, `하오체`, `하십시오체`, `해체`, and `해요체`.

The freeze does not misuse this taxonomy as a brand-preference scale or as evidence that all six styles are equally current in every commercial context.

## KOLA02 — PASS

The NIKL advisory classifies `해라체 / 하게체 / 하오체 / 하십시오체` as `격식체` and `해체 / 해요체` as `비격식체`, while describing the two classes in stylistic terms rather than as one high-to-low respect ordering.

Because the formal class includes both high-address `하십시오체` and low-address `해라체`, while the non-formal class includes both `해요체` and `해체`, the frozen inference is valid:

```text
FORMAL
!= AUTOMATICALLY MORE RESPECTFUL
```

The source does not support a professional-marketing preference, and the ledger does not claim one.

## KOLA03 — PASS

The NIKL usage advisory directly supports the narrow same-listener point: formal and non-formal addressee styles may commonly be used with the same listener depending on the concrete situation, and mixed use cannot be declared wrong without context.

The ledger correctly stops short of saying every mixed draft is natural, intentional, or valid.

## KOLA04 — PASS

The 2022 news-interview study supports the `하십시오체 ↔ 해요체` style-shifting burden in formal situations. Its abstract reports analysis of five university-published Korean textbooks and seven news-interview episodes with foreign interviewees, frequent style shifting in the interviews, and the inadequacy of a simple formal/non-formal textbook dichotomy for natural relative-honorific use.

The freeze uses this as evidence that supported shifting exists and matters to natural realization. It does not turn the study into a universal frequency target, marketing rule, or organization policy.

## KOLA05 — PASS

The NIKL grammatical advisory supports the distinction among:

```text
주체 높임법
객체 높임법
상대 높임법
```

including `-시-` for subject honorification, lexical object-honorific forms such as `뵙다 / 드리다 / 여쭈다`, and sentence-ending addressee realization.

The ledger correctly uses this as a boundary, not as evidence for three runtime owners or a Korean hierarchy engine.

## KOLA06 — PASS

The NIKL example `이 책을 아주머니께 가져다 드려라` supports coexistence of lexical object honorification (`드리다`) and a separately selected addressee-directed `해라체` ending.

The frozen inference that object/action-target honorification and addressee speech level can coexist without being the same decision is supported. No separate object-honorification runtime unit follows from the source.

## KOLA07 — PASS

The live first-party KB customer-language guidance supports the bounded organization example recorded in the ledger: KB varies `하십시오체`, `해요체`, and noun/nominal endings by purpose, target, situation, and surface/function.

This supports:

```text
SAME ORGANIZATION
+
SAME BROAD CUSTOMER RELATIONSHIP
!= ONE SPEECH LEVEL FOR EVERY SURFACE / FUNCTION
```

It does **not** establish a Korean population preference, banking-industry rule, or universal mapping such as `policy → 하십시오체` or `CTA → 해요체`, and the freeze explicitly rejects those upgrades.

## KOLA08 — PASS

The 2015 KCI-indexed content analysis supports the recorded sample facts: 1,750 TV-ad sentences were analyzed; formal/non-formal ending frequency differed by product involvement, sentence type, and articulation context; and 57.6% of the analyzed sentences were non-final constructions without a formal/non-formal sentence ending.

The freeze correctly uses this as distribution/context evidence and as support for the possibility of surfaces with no material speech-level decision. It does not convert frequency into effectiveness or a current universal norm.

## KOLA09 — PASS

The 2018 KCI-indexed two-experiment study supports the bounded response claim: in the tested conditions, non-formal endings produced more favorable attitudes toward the ad than formal endings, with a larger reported effect for radio than print.

The freeze correctly refuses all stronger upgrades:

```text
FAVORABLE AD ATTITUDE
!= CONVERSION
!= REVENUE
!= UNIVERSAL CHANNEL RULE
!= 2026 POPULATION DEFAULT
```

## KOLA10 — PASS

The NIKL advisory supports both sides of the frozen boundary. Examples with `객실` itself as subject are treated as inappropriate targets for honorification, while customer-subject contexts can support `-시-`; the response also notes that indirect subject honorification can involve closely related body parts, properties/possessions, or similar relations and that grammatical analysis may differ.

The ledger therefore correctly rejects both binary lookup rules:

```text
INANIMATE + -시-
→ ALWAYS ERROR
```

and:

```text
CUSTOMER-RELATED NOUN + -시-
→ ALWAYS CORRECT
```

This remains an ordinary-grammar / scope boundary, not a promotion-bearing mechanism.

## KOLA11 — PASS

The NIKL advisory states that `압존법` is not fixed by Korean language regulations and cites traditional use mainly in family and teacher-student contexts rather than a general social/workplace rule.

The frozen use is correct: the source defeats an executable rank-order suppression rule; it does not justify one.

### Source verdict summary

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

---

# C. MATERIAL FINDINGS

No material finding survives review.

```text
FINDINGS
→ NONE

BOUNDED REPAIR REQUIRED
→ NO
```

Reviewer clarification, not a defect: the subject/object/addressee boundary should be understood as a scope/composition guardrail, not as independent Korean novelty. The frozen design already says `JP-LANG-HON-01` supplies the generic warning, rejects a second Korean honorification unit, and keeps the promoted decision at sentence-ending addressee realization. No frozen change is required to preserve that reading.

---

# D. ARCHITECTURE VERDICT

```text
existing route sufficient?      YES
new owner required?             NO
new route required?             NO
shared primitive required?      NO
hierarchy resolver required?    NO
speech-level score required?    NO
controller change required?     NO
Chapter 07 change required?     NO
routing-index change required?  NO
get-knowledge change required?  NO
```

The current architecture is already sufficient:

```text
CURRENT JOB
→ FREEZE RESOLVED STATE
→ Chapter 07 localization owner
→ bounded JIT adaptation lookup
→ adapt-localization.relationship-realization
→ section-local unit scope check
→ apply only the still-open Korean-specific constraint
```

`routing-index.json` already maps:

```text
adapt-localization.relationship-realization
→ adaptations/localization.md
→ ## Relationship realization
```

`get-knowledge.py` already resolves namespace/section routes generically and extracts the indexed heading section. It does not need Korean-specific code.

The adaptation contribution contract already permits multiple independently scoped language units under one owner/decision-aligned route and explicitly rejects country-first packs, scope registries, specificity scores, and precedence machinery absent a demonstrated discovery/addressability/composition failure.

No such failure appears here. Korean honorific complexity is not evidence for new runtime machinery.

---

# E. K1–K16 ADVERSARIAL RESULTS

## K1 — approved 하십시오체 — PASS

Applicable approved organization/surface state already resolves the ending system. The candidate explicitly preserves resolved state and does not reopen it merely because Korean-specific knowledge exists.

## K2 — approved 해요체 — PASS

Same result as K1. The candidate preserves the approved `해요체` dimension.

## K3 — same brand, different surfaces — PASS

A first-party rule such as:

```text
policy / restriction = 하십시오체
request / explanation = 해요체
```

remains scoped resolved state. The candidate does not normalize the organization to one global speech level.

## K4 — intentional style shift — PASS

When the same speaker/listener `하십시오체 ↔ 해요체` shift is supported by interaction/discourse function, the candidate preserves it. Surface consistency alone is not repair authority.

## K5 — accidental style drift — PASS

Adversarial construction:

```text
RESOLVED SURFACE VOICE = 해요체
NO STANCE / AUDIENCE / INTERACTION SHIFT
NO FIRST-PARTY OR DISCOURSE SUPPORT FOR CHANGE

DRAFT:
"지금 확인해 보세요. 자세한 내용은 아래에서 확인하라. 문제가 있으면 문의하십시오."
```

The frozen candidate permits repair back to the resolved system. `MIXED != AUTOMATIC ERROR` does not become `MIXED = ALWAYS PRESERVE`.

## K6 — “make it more formal” — PASS

The candidate rejects a scalar transformation in which `formal` automatically means more addressee deference, higher hierarchy, or greater interpersonal distance.

It preserves the resolved relationship and treats register/formality as the requested dimension. If the requested change is still underdetermined after preserving that state, Chapter 07's uncertainty rule applies rather than inventing a new relationship.

## K7 — “make it friendlier” — PASS

`friendly` is not activation authority for `해체`. The candidate preserves addressee treatment unless evidence supports a relationship-level change.

## K8 — title / banner / button / nominal form — PASS

`카드 연결하기` contains no material finite addressee sentence-ending choice. No Korean speech-level detour is justified.

## K9 — honored third-party subject, listener ending fixed — PASS

If only `-시-` / subject honorification remains open, `KO-LANG-SPEECH-01` does not seize the decision. The candidate's scope is sentence-ending addressee realization.

## K10 — subject honorification and 해요체 coexist — PASS

Example class:

```text
선생님이 곧 오세요.
```

Subject honorification and addressee-directed `해요체` can coexist. The candidate and KOLA05–KOLA06 prevent a false `double politeness` collapse.

## K11 — inanimate/customer-service honorification edge — PASS

The candidate does not convert KOLA10 into `inanimate + -시-` correction code. It keeps the grammatical/honorific-target analysis outside the promoted sentence-ending mechanism.

## K12 — 압존법 hierarchy cue — PASS

A senior listener plus another senior referent does not trigger automatic suppression by relative rank. No hierarchy graph or rank resolver is introduced.

## K13 — Korean outside Korea — PASS

Korean-language support in the United States, Vietnam, or another non-Korea market may load the unit when sentence-ending addressee realization is materially open. Activation follows target language and decision state, not Korea-market membership.

## K14 — Korea market, English output — PASS

Korea geography/market context alone does not activate a Korean sentence-ending unit when the output language is English.

## K15 — relationship known, speech level unresolved and unavoidable — PASS

The candidate does not invent any of the following:

```text
standard Korean → 하십시오체
marketing → 해요체
customer → 하십시오체
```

When scoped evidence does not resolve an unavoidable speech-level choice, the unresolved dependency remains visible under Chapter 07 rather than being converted into a cultural default.

## K16 — Korean noun with no relationship decision — PASS

A Korean/Korea mention without a material finite addressee ending choice does not load the unit.

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

---

# Formality-scale attack

The candidate rejects a universal scalar such as:

```text
해라체 < 해체 < 하게체 < 해요체 < 하오체 < 하십시오체
```

No ordinal speech-level score is needed or justified. The evidence supports category distinctions and context-sensitive realization, not one commercial politeness axis.

---

# First-party-state attack

Both directions survive review:

```text
APPLICABLE ORGANIZATION / SURFACE POLICY
→ RESOLVED STATE WITHIN ITS SCOPE
```

but:

```text
FIRST-PARTY POLICY
!= KOREAN POPULATION RULE
```

A deliberately bad organization rule also does not create a new precedence engine. Organization authority may choose tone/style, but it does not make ordinary Korean morphology grammatical by declaration. Existing controller truthfulness/fixed-wording behavior can surface the conflict without Korean-specific precedence machinery.

---

# Marketing-evidence attack

Both forbidden upgrades fail:

```text
KOLA08 DISTRIBUTION
→ USE THE MOST FREQUENT STYLE
```

is invalid, and:

```text
KOLA09 FAVORABILITY EFFECT
→ USE 해요체 FOR HIGHER CONVERSION
```

is invalid.

The supported inference remains bounded:

```text
speech-level realization varies materially by context
and can affect measured audience response under tested conditions
```

No universal marketing prescription follows.

---

# Non-final / address-neutral attack

The candidate correctly preserves both sides:

```text
NO MATERIAL FINITE ADDRESSEE ENDING DECISION
→ NO LOAD
```

and:

```text
ADDRESS-NEUTRAL / NOMINAL REALIZATION EXISTS
!= USE IT TO HIDE EVERY HARD SPEECH-LEVEL DECISION
```

A button/title may naturally avoid the decision. Direct interpersonal copy must not be awkwardly nominalized merely to avoid an unresolved relationship-sensitive choice.

---

# Ordinary-grammar boundary

The candidate survives the general-Korean-proofreading attack. These errors are **not** `KO-LANG-SPEECH-01` failures merely because they occur in customer-facing Korean:

1. `고객님 께서 확인해 주세요.` — spacing/orthographic correctness (`고객님께서`) is ordinary Korean writing, not sentence-ending speech-level selection.
2. `이 서비스를 고객이 필요합니다.` — case/argument-structure repair is ordinary grammar, not addressee treatment.
3. A wrong tense/aspect or lexical choice inside a sentence whose ending system is already resolved remains ordinary Korean competence.
4. A pure `-시-` subject-honorification error with an already-fixed addressee ending remains outside `KO-LANG-SPEECH-01`.

Scope remains:

```text
FINITE ADDRESSEE SPEECH-LEVEL REALIZATION
→ KO-LANG-SPEECH-01

GENERAL KOREAN CORRECTNESS
OR SUBJECT/OBJECT HONORIFICATION ONLY
→ ordinary language competence / existing owner boundary
```

---

# Composition with existing VN / JP / ES units

The candidate composes safely with:

```text
VN-LANG-REL-01
JP-LANG-HON-01
JP-LANG-PERM-01
ES-LANG-ADDR-01
```

The common architecture remains decision-first and section-local:

```text
CURRENT JOB
→ Chapter 07 localization owner
→ bounded discovery
→ adapt-localization.relationship-realization
→ inspect each contribution's own language/scope conditions
→ apply only the materially open target-language constraint
```

No language name, country name, or shared file location activates all units.

The units remain non-redundant:

- Vietnamese: coupled self-reference / recipient-address realization.
- Japanese honorific-target unit: participant/action-target orientation.
- Japanese permission/benefit unit: semantic consequences of deferential own-side-action forms.
- Spanish: second-person treatment-system realization and variety-sensitive coupling.
- Korean: sentence-ending addressee speech-level realization where formality and respect are non-identical and supported same-listener shifting may be legitimate.

---

# Counterfactual necessity adjudication

Remove `KO-LANG-SPEECH-01` while retaining Chapter 07, VN/JP/ES units, task-specific relationship/voice evidence, and ordinary Korean generation:

| Candidate material | Correct answer reliably remains without Korean unit? | Promotion consequence |
|---|---|---|
| `격식체` is not one higher respect setting than `비격식체` | No | promotion-bearing |
| supported same-listener `하십시오체 ↔ 해요체` shift may be legitimate | No | promotion-bearing |
| `make it more formal` must not itself authorize a relationship/honorification change | No, not reliably without the Korean classification above | promotion-bearing |
| subject/object/addressee are distinct dimensions | Partly: generic participant-target boundary already exists, but Korean grammar still needs ordinary language knowledge | scope/composition guardrail, not independent promotion basis |
| applicable first-party speech-level policy is resolved state | Yes, generically | composition boundary only |
| title/button with no finite ending should not load | Yes, generically once the Korean unit's activation scope is known | negative-activation boundary only |
| `사물존대` is not a binary lookup | Not safely as a Korean-specific grammatical claim | boundary evidence only; not a new unit |
| `압존법` is not a workplace rank algorithm | Not safely as a Korean-specific etiquette claim | anti-resolver boundary only; not a new unit |

This is the decisive novelty result: the promotion case is carried by Korean sentence-ending addressee speech-level knowledge, not by country, hierarchy, generic politeness, or advertising preference.

---

# F. RESIDUAL UNCERTAINTY

The following remain unknown without blocking promotion:

- exhaustive discourse conditions governing every natural `하십시오체 ↔ 해요체` shift;
- prevalence of all six speech levels across contemporary commercial channels and populations;
- current brand/audience preference for particular speech levels outside supplied first-party or scoped evidence;
- regional/dialect honorific systems not covered by the frozen candidate;
- a complete theory of subject, object, and indirect honorification;
- disputed edge analyses inside indirect subject honorification;
- exhaustive modern etiquette conditions for `압존법`-like usage;
- causal conversion/revenue effects of speech-level choices;
- LLM-specific Korean speech-level error rates.

These unknowns do not authorize defaults, a second Korean unit, a hierarchy resolver, a country pack, or broader research obligations. They become dependencies only when a concrete task requires them.

---

# Final disposition

```text
TOP-LEVEL VERDICT
→ PASS

KO-LANG-SPEECH-01
→ PROMOTE

SPLIT UNIT
→ NO

BOUNDED REPAIR
→ NONE

NEW OWNER
→ NO

NEW ROUTE
→ NO

NEW SHARED PRIMITIVE / HIERARCHY RESOLVER / SPEECH-LEVEL SCORE
→ NO

CONTROLLER CHANGE
→ NO

CHAPTER 07 CHANGE
→ NO

ROUTING-INDEX CHANGE
→ NO

GET-KNOWLEDGE CHANGE
→ NO

PROMOTE TO adaptations/localization.md NOW
→ NO — review result is recorded first; runtime implementation/promotion remains a separate subsequent delta
```
