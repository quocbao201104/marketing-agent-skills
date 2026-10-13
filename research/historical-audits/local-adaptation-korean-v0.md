# Korean Addressee Speech-Level Realization — Targeted Pressure Test v0

Status: **targeted architecture/regression suite, not a behavioral benchmark**.

Candidate contribution:

```text
KO-LANG-SPEECH-01
```

Intended logical route:

```text
adapt-localization.relationship-realization
```

Independent research-review verdict:

```text
PASS
```

Promotion verdict:

```text
KO-LANG-SPEECH-01
→ PROMOTE
```

## Question under test

Can the Korean local-adaptation implementation improve sentence-ending addressee speech-level realization **without** creating a Korea country pack, a Korean honorific mega-unit, a hierarchy resolver, a speech-level score, a new route/owner, or a general Korean grammar module?

## Oracle

```text
CURRENT JOB
→ FREEZE RESOLVED IDENTITY / RELATIONSHIP / STANCE /
  INTERACTION STATE / APPROVED VOICE / SURFACE STATE
→ IS A KOREAN ADDRESSEE SPEECH-LEVEL REALIZATION
  MATERIALLY OPEN OR BEING CHANGED?
    ├─ NO  → DO NOT LOAD KO-LANG-SPEECH-01
    └─ YES → CHAPTER 07 LOCALIZATION OWNER
             → DISCOVER OWNER-ALIGNED adapt-localization NAMESPACE
             → adapt-localization.relationship-realization
             → section-local scope check
             → apply KO-LANG-SPEECH-01 only to the open ending dimension
```

The unit consumes resolved state. It must not re-infer hierarchy, intimacy, seniority, customer deference, brand voice, or market preference from Korean/Korea/customer/business labels.

## Required cases

| Case | Task / resolved state | Expected route behavior | Required semantic behavior |
| --- | --- | --- | --- |
| K1 — approved `하십시오체` | Applicable organization/surface policy already fixes `하십시오체`; no other addressee-ending dimension is open. | **NO REOPEN**. | Preserve resolved speech level. Korean language alone is not authority to reconsider it. |
| K2 — approved `해요체` | Applicable policy already fixes `해요체`. | **NO REOPEN**. | Preserve the approved dimension. |
| K3 — same brand, different surfaces | One scoped first-party policy uses `하십시오체` for policy/restriction and `해요체` for request/explanation. | **NO GLOBAL NORMALIZATION**. | Preserve the applicable surface/function policy; do not infer one brand-wide speech level. |
| K4 — intentional same-listener shift | Same speaker/listener and broad relationship; discourse/context supports `하십시오체 ↔ 해요체` shifting. | **LOAD only if realization remains open/material**. | Do not normalize the supported shift merely for consistency. |
| K5 — accidental speech-level drift | Resolved surface voice is `해요체`; draft drifts to `해라체` and `하십시오체` without stance, interaction, or policy support. | **LOAD KO-LANG-SPEECH-01**. | `MIXED != AUTOMATIC ERROR` does not mean preserve unsupported drift; repair toward resolved state. |
| K6 — “make it more formal” | Relationship/addressee treatment is already resolved; user asks for more formal Korean. | **LOAD when ending realization is being changed**. | Do not equate `formal` with more respect, higher hierarchy, or greater interpersonal distance. Preserve relationship while changing only the requested register dimension if support exists. |
| K7 — “make it friendlier” | Relationship is resolved and respectful; user requests friendlier wording. | **LOAD only if ending realization is materially changed**. | `friendly` does not authorize automatic downgrade to `해체`. |
| K8 — title/button/nominal form | Surface is a title, banner, button, or nominal form such as `카드 연결하기`; no finite addressee ending is present. | **NO LOAD**. | No material speech-level decision exists. |
| K9 — honored third-party subject, ending fixed | Only `-시-` / subject honorification remains open; addressee ending is already fixed. | **NO KO-SPEECH OWNERSHIP**. | Keep subject honorification outside this unit; do not seize the decision because the text is Korean. |
| K10 — subject honorification + `해요체` coexist | Example class such as `선생님이 곧 오세요.` | **NO COLLAPSE**. | Subject honorification and addressee-directed `해요체` may coexist; do not call this redundant or “double politeness” by default. |
| K11 — `사물존대` edge | Customer-service wording contains `-시-` with an inanimate/customer-related noun. | **OUTSIDE PROMOTED MECHANISM unless addressee ending is separately open**. | Inspect ordinary Korean grammar/actual subject; do not apply `inanimate + -시-` lookup rules. |
| K12 — `압존법` hierarchy cue | Senior listener and another senior referent are present. | **NO HIERARCHY RESOLVER**. | Do not mechanically suppress referent honorification from relative rank. |
| K13 — Korean outside Korea | Korean-language support copy is for users in the US, Vietnam, or another non-Korea market; addressee ending is open. | **LOAD KO-LANG-SPEECH-01 when material**. | Applicability follows target-language realization, not Korea-market membership. |
| K14 — Korea market, English output | Market is Korea but output is English. | **NO LOAD**. | Geography does not activate Korean sentence-ending knowledge. |
| K15 — relationship known, speech level unresolved | Relationship is known, but an unavoidable Korean finite addressee ending remains materially unresolved and no scoped policy resolves it. | **LOAD may expose unresolved dependency**. | Do not invent `standard Korean = 하십시오체`, `marketing = 해요체`, or `customer = 하십시오체`. Preserve uncertainty under Chapter 07. |
| K16 — Korean noun / market mention only | Task mentions Korea/Korean or contains Korean nouns but no material finite addressee ending choice. | **NO LOAD**. | Korean/Korea is not activation authority. |

## Non-speech-level negative controls

These are not `KO-LANG-SPEECH-01` problems merely because they occur in Korean copy:

```text
고객님이 상품을 구매했어요 → 상품를 구매했어요
→ particle / ordinary grammar issue

세 개 상품을 확인해요
→ counting / noun-expression issue if correction is needed

어제 내일 다시 방문해요
→ temporal / semantic incoherence
```

Use ordinary Korean competence or the appropriate owner. The promoted unit is only for sentence-ending addressee speech-level realization.

## Adversarial properties covered

```text
K1 / K2 / K3      resolved first-party state preservation
K4 / K5           legitimate shift != preserve unsupported drift
K6                 formality != addressee respect
K7                 friendliness != automatic 해체
K8 / K16           noun/surface trigger resistance
K9 / K10 / K11    addressee speech level != subject/object honorification
K12                압존법 != executable hierarchy graph
K13 / K14          target language != market geography
K15                unresolved state != cultural default
```

## Static implementation requirements

The implementation passes structurally only if all remain true:

```text
1. logical route remains adapt-localization.relationship-realization
2. no adapt-korean / adapt-korea / ko-* route family is added
3. KO-LANG-SPEECH-01 lives under the existing Relationship realization section
4. Chapter 07 remains the decision owner
5. no controller, routing-index, or get-knowledge change is introduced
6. no Korea country pack is introduced
7. no global speech-level score or formal↔casual scalar is introduced
8. formal/non-formal register is not treated as identical to addressee respect
9. one relationship is not treated as requiring one invariant speech level
10. supported 하십시오체 ↔ 해요체 shifting is not normalized mechanically
11. mixed speech levels are not treated as automatically valid
12. customer/business/marketing labels do not map directly to a speech level
13. first-party organization/surface policy remains resolved state within scope
14. subject/object honorification remains a boundary, not a second Korean runtime unit
15. 사물존대 is not converted into an inanimate/customer lookup
16. 압존법 is not converted into a hierarchy resolver
17. non-final/address-neutral realization is optional only where natural and semantics-preserving
18. advertising distribution/effect evidence is not upgraded into a universal prescription
19. no registry, precedence engine, freshness subsystem, or Korean-specific loader is introduced
```

## Promotion decision oracle

A later behavioral evaluation should distinguish at least:

```text
F0  correct fast-path / no activation
F1  correct activation + correct owner route
F2  formal request incorrectly converted into higher deference / hierarchy
F3  supported same-listener style shift normalized as inconsistency
F4  unsupported speech-level drift preserved because mixed use can exist
F5  customer / business / marketing noun converted into ending lookup
F6  resolved first-party speech-level policy reopened without authority
F7  subject/object honorification incorrectly absorbed by KO-LANG-SPEECH-01
F8  사물존대 converted into binary correction code
F9  압존법 converted into rank-order suppression logic
F10 Korea geography activates Korean speech-level handling for non-Korean output
F11 non-final/title/button surface forced into an unnecessary speech-level decision
F12 advertising distribution/effect evidence upgraded into a default style recommendation
```

This file freezes targeted regression cases and expected architecture semantics. It does not claim these behaviors have been model-benchmarked.
