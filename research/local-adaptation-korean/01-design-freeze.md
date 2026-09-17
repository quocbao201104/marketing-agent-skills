# Korean Local Adaptation — Design Freeze

Status: **FROZEN FOR INDEPENDENT ADVERSARIAL REVIEW**  
Freeze date: 2026-09-17  
Repository base: `main@4536dd214ffa5b25e07b12b7bd715dc4b66fd49a`

## 1. Research question

In Korean-language marketing communication, are there addressee-facing realization decisions that an agent can still get materially wrong after the generic Marketing Practitioner controller has correctly resolved relationship, stance, audience, message, authority, and other upstream state — because the remaining choice depends on a Korean-specific sentence-ending speech-level system?

The purpose of this research is not to build a Korea market profile, a business-etiquette guide, a hierarchy engine, or a general Korean honorific grammar. It is to pressure the existing scoped local-adaptation architecture with a language whose sentence endings can index the addressee while formality/register, respect, interpersonal distance, and discourse function remain related but non-identical dimensions.

The promotion gate remains:

```text
LOCAL-SPECIFIC MECHANISM
+
MATERIAL DECISION DELTA
+
GENERIC OWNER DOES NOT ALREADY KNOW
THE TARGET-SPECIFIC MECHANISM
=
ADAPTATION CANDIDATE
```

Counterfactual test:

> Remove Korean-specific knowledge, but keep all task-specific evidence plus Chapter 07 and the already-promoted Vietnamese, Japanese, and Spanish adaptation units. Can the existing owner still make the correct Korean realization decision reliably?

If yes, the material stays generic, task-specific, or ordinary language competence. If no, it may justify one bounded Korean unit.

## 2. Existing architecture under pressure

The current architecture already provides:

```text
CURRENT JOB
→ FREEZE RESOLVED STATE
→ NAME OPEN DECISION
→ SELECT EXISTING OWNER
→ LOAD THE SMALLEST DECISION-RELEVANT KNOWLEDGE
→ PRESERVE TRUTH / AUTHORITY / CLAIM BOUNDARIES
```

Chapter 07 already owns relationship-sensitive localization realization and exposes the bounded JIT edge into:

```text
adapt-localization.relationship-realization
```

That route already contains Vietnamese, Japanese, and Spanish contributions. Korean must therefore justify a target-language-specific realization mechanism under the same owner and route. Variation by itself is not evidence for a new owner, country pack, resolver, or routing family.

## 3. Freeze verdict

One Korean-specific mechanism survives the promotion gate:

```text
KO-LANG-SPEECH-01
Korean addressee speech-level realization
→ PROMOTE CANDIDATE
```

The following do not survive as separate units or architecture:

```text
Korea country pack
→ REJECT

one global "formal ↔ casual" Korean scale
→ REJECT

customer / senior / business → fixed speech-level lookup
→ REJECT

marketing → 해요체 lookup
→ REJECT

formal → more respectful lookup
→ REJECT

full Korean honorific grammar module
→ REJECT

separate Korean subject/object-honorification unit at this stage
→ REJECT

사물존대 lookup rule
→ REJECT

압존법 hierarchy resolver
→ REJECT

artifact-type activation such as UI / social / legal / business email
→ REJECT

new route / owner / controller / shared primitive
→ REJECT
```

No evidence currently justifies a second Korean unit.

## 4. KO-LANG-SPEECH-01 — Korean addressee speech-level realization

### 4.1 Local-specific mechanism

Korean `상대 높임법` is realized through sentence-ending choices directed at the addressee. Current National Institute of Korean Language guidance lists speech levels including:

```text
해라체
하게체
하오체
하십시오체
해체
해요체
```

and explicitly treats both `해요체` and `해체` as part of addressee honorification [KOLA01].

The local-specific mechanism is not simply that Korean has polite and casual endings. The crucial constraint is:

```text
ADDRESSEE RESPECT
!=
FORMALITY / REGISTER
!=
INTERPERSONAL DISTANCE
!=
DISCOURSE FUNCTION
```

Current NIKL descriptions classify `해라체 / 하게체 / 하오체 / 하십시오체` as `격식체`, while `해체 / 해요체` are `비격식체`. `격식체` is described in terms of ceremonial/direct/assertive/objective expression, while `비격식체` is softer and more subjective [KOLA02]. Because `격식체` includes both highly respectful `하십시오체` and low-address `해라체`, and `비격식체` includes both `해요체` and `해체`, the formality distinction cannot safely be collapsed into one respectful↔casual scalar.

Therefore:

```text
FORMAL
!= MORE RESPECTFUL

NON-FORMAL
!= LESS RESPECTFUL
```

This creates a material failure for generic localization. A request such as `make this more formal` does not by itself authorize changing the relationship or increasing addressee deference.

### 4.2 Same relationship does not imply one invariant speech level

Current NIKL guidance states that one speaker may commonly alternate formal and non-formal addressee styles with the same listener depending on the concrete situation, and that such use cannot be declared wrong without context [KOLA03].

A 2022 Korean-language study of news interviews likewise analyzes `하십시오체 ↔ 해요체` style shifting in formal situations, finding frequent switching and arguing that a simple formal/non-formal textbook dichotomy is insufficient for natural relative-honorific use [KOLA04].

Therefore:

```text
ONE RELATIONSHIP
!= ONE SPEECH LEVEL FOR EVERY UTTERANCE

SPEECH-LEVEL SHIFT
!= AUTOMATIC RELATIONSHIP SHIFT

MIXED SPEECH LEVELS
!= AUTOMATIC ERROR
!= AUTOMATICALLY VALID
```

The last line is essential. The unit must preserve a supported style shift, but it must also repair unsupported drift when approved organization state, interaction state, or surrounding discourse resolves a different system.

### 4.3 Existing owner

Owner remains:

```text
Localization / Chapter 07
```

The unit consumes already-resolved relationship, stance, interaction state, speaker/publishing identity, approved voice, and applicable organization/surface evidence. It does not decide who deserves respect, what organizational hierarchy exists, or what relationship the speaker and addressee should have.

### 4.4 Decision impact

The bounded decision is:

> Given already-resolved recipient relationship, interaction state, intended stance, approved voice, communication function, and applicable organization/surface evidence, how should Korean sentence-ending addressee speech level be realized without inventing a different relationship, collapsing formality into respect, or normalizing a legitimate discourse-functional shift?

The unit may:

```text
- preserve an approved speech-level policy;
- distinguish addressee respect from formal/non-formal register;
- preserve a supported 하십시오체 ↔ 해요체 shift;
- repair unsupported speech-level drift;
- keep the still-open sentence-ending dimension separate from subject/object honorification;
- leave address-neutral / non-final surfaces alone when no addressee speech-level choice exists.
```

It may not independently determine hierarchy, familiarity, customer deference, seniority, legal authority, or a market-wide preferred style.

### 4.5 Scope

Candidate scope:

```text
language: Korean (`ko`)
market / geography: not inherently Korea-only
audience / role: audience-facing or interpersonal wording where sentence-ending addressee speech level is materially open or being changed
channel / surface: any, but only when a finite addressee-facing ending choice is actually material
category / buying context: not category-specific
effective period: core grammatical distinctions are structural; organization style and response effects are scope- and time-sensitive
```

The unit follows language realization, not nationality or market membership.

## 5. What the unit must preserve

When applicable, preserve:

```text
speaker / publishing identity
actual recipient relationship
standing / authority already resolved upstream
interaction history
intended stance
communication function of the utterance
approved organization / surface voice
verified existing speech-level choices
supported discourse-functional speech-level shifts
applicable accessibility/community constraints
```

If one speech-level dimension is already resolved, freeze it and constrain only the still-open dimension.

## 6. What the unit must not infer

Do not manufacture any of the following from Korean language, Korea market, age, job title, customer status, or broad culture alone:

```text
HIERARCHY
FAMILIARITY
INTIMACY
AUTHORITY
SENIORITY RELATIONSHIP
CUSTOMER DEFERENCE LEVEL
ONE UNIVERSAL "POLITE KOREAN" STYLE
ONE SPEECH LEVEL PER BRAND
ONE SPEECH LEVEL PER RELATIONSHIP
```

Guardrails:

```text
KOREAN
!= MAXIMUM HONORIFICATION

CUSTOMER
!= 하십시오체

MARKETING
!= 해요체

FORMAL
!= MORE RESPECTFUL

FRIENDLY
!= 해체

BUSINESS
!= 하십시오체 BY DEFINITION
```

## 7. First-party organization and surface state

Current KB customer-language guidance is useful as a bounded first-party example. KB states that its tone changes by purpose, target, and situation: `하십시오체` for service policy, terms/notices, objective data, expert/investment guidance, thanks, errors/refusals/restrictions; `해요체` for requests, recommendations, action prompts, difficult explanations, and asking customer intent. It separately uses nouns or nominal endings for titles, banners, notes, and buttons [KOLA07].

This supports only:

```text
SAME ORGANIZATION
+
SAME BROAD CUSTOMER RELATIONSHIP
!= ONE SPEECH LEVEL FOR EVERY SURFACE / FUNCTION
```

It does not support:

```text
KOREAN BANKING → COPY KB
POLICY → 하십시오체 UNIVERSALLY
CTA → 해요체 UNIVERSALLY
```

Applicable first-party organization/surface policy is resolved state within its actual scope. Broader sociolinguistic evidence is not permission to reopen it merely because other Korean styles exist.

## 8. Marketing evidence is context, not prescription

A 2015 content analysis of 1,750 Korean TV-ad sentences found formal/non-formal ending distributions associated with product involvement, sentence type, and articulation context; 57.6% of the analyzed ad sentences used non-final constructions without a formal/non-formal sentence ending [KOLA08].

A 2018 two-experiment study found, within its experimental conditions, more favorable ad attitudes for non-formal endings than formal endings, with a larger effect in radio than print [KOLA09].

These records support only that speech-level realization can vary materially by communication context and can affect audience response under bounded conditions.

They do not establish:

```text
해요체 → better marketing
해요체 → higher conversion
radio → always 해요체
high-involvement → always 하십시오체
one advertising sample → current population preference
```

Observed distribution and experimental response are not universal brand rules.

## 9. Subject/object honorification is a boundary, not a second unit

Korean distinguishes at least:

```text
주체 높임법
→ honor the grammatical subject, commonly via -시-

객체 높임법
→ honor the target/object of an action, including lexical forms such as 뵙다 / 드리다 / 여쭈다

상대 높임법
→ realize addressee treatment through sentence endings
```

Current NIKL guidance states these as distinct honorification mechanisms [KOLA05]. NIKL examples also show that lexical object honorification such as `드리다` and an addressee-directed sentence ending can coexist in the same clause [KOLA06].

Therefore:

```text
ADDRESSEE SPEECH LEVEL
!= SUBJECT HONORIFICATION
!= OBJECT / ACTION-TARGET HONORIFICATION
```

This matters because `JP-LANG-HON-01` already supplies a generic warning against collapsing addressee, actor/referent, and action target. Korean research has not yet shown a separate subject/object mechanism that requires another runtime unit beyond that existing architecture plus ordinary Korean competence.

So:

```text
KO-LANG-HON-02
→ REJECT FOR NOW
```

If a future concrete failure survives the existing owner plus current units, it can be researched separately.

## 10. 사물존대 / indirect subject honorification is not a lookup

NIKL guidance on examples such as `객실이 없으세요`, `4인실이세요`, and `객실이 남아있으세요` says that a room itself is generally not an honorification target in those constructions, while separately noting that indirect subject honorification may be analyzed where a body part, property, possession, or other closely related entity is used to honor the actual person; the scope can involve grammatical disagreement [KOLA10].

Therefore reject both simplifications:

```text
INANIMATE + -시-
→ ALWAYS ERROR
```

and

```text
CUSTOMER-RELATED NOUN + -시-
→ ALWAYS CORRECT
```

This is not part of the promotion-bearing `KO-LANG-SPEECH-01` mechanism. It is a boundary preventing the Korean research track from becoming a customer-service honorific grammar module.

## 11. 압존법 does not justify a hierarchy resolver

Current NIKL guidance states that `압존법` is not fixed in language regulations and cites `표준 언어 예절` as describing it traditionally in family and teacher-student contexts rather than as a general social/workplace rule [KOLA11].

Therefore reject:

```text
LISTENER RANK > REFERENT RANK
→ AUTOMATICALLY SUPPRESS REFERENT HONORIFICATION
```

No executable hierarchy graph or rank resolver is justified.

## 12. Negative activation

`KO-LANG-SPEECH-01` does not load merely because the task mentions:

```text
Korean
Korea
customer
business
senior audience
marketing
social media
policy
formal copy
```

Candidate activation requires:

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

Do not use when:

- the task is only market selection or Korea research;
- the artifact contains no material finite addressee-facing ending choice;
- titles, banners, buttons, labels, or nominal forms already avoid the speech-level decision naturally;
- applicable approved organization/surface wording fully resolves the speech level and no truthful or linguistic conflict requires reopening it;
- the only open issue is subject/object honorification rather than addressee speech level;
- the remaining issue is ordinary Korean grammar unrelated to addressee treatment;
- activation would be based only on nationality, market, age, job title, or customer status.

## 13. Address-neutral / non-final realization is a bounded option, not a fallback strategy

The 2015 advertising corpus provides direct evidence that many Korean ad sentences in that sample did not use a formal/non-formal final ending [KOLA08]. KB likewise uses noun/nominal endings for bounded surfaces such as titles, banners, notes, and buttons [KOLA07].

Therefore:

```text
SURFACE NATURALLY HAS NO ADDRESSEE SPEECH-LEVEL DECISION
→ NO LOAD
```

But:

```text
ADDRESS-NEUTRAL / NON-FINAL WORDING EXISTS
!= MUST USE IT
```

Do not distort direct conversational copy merely to avoid an unresolved speech-level choice.

## 14. Necessity test against Chapter 07 + existing units

### Case A — fixed relationship, legitimate style shift

```text
relationship: fixed
speaker/listener: fixed
formal interview context
utterances alternate 하십시오체 ↔ 해요체
```

Chapter 07 knows to preserve relationship state. `JP-LANG-HON-01` knows that addressee and action target are distinct. Neither currently encodes the Korean-specific fact that sentence-ending addressee style may legitimately shift between formal and non-formal forms with one listener in one broad relationship/context.

Without Korean-specific knowledge, a consistency-oriented editor may normalize the shift incorrectly.

**Candidate changes the decision.**

### Case B — user asks "make it more formal"

Generic wording transformation may treat formal as more respectful. Korean evidence shows that `격식체` is not one monotonic respect level because it includes both `하십시오체` and low-address `해라체`, while non-formal includes both `해요체` and `해체` [KOLA01][KOLA02].

**Candidate changes the decision.**

### Case C — approved brand policy already resolves the surface

```text
organization policy:
policy notices → 하십시오체
explanations → 해요체
```

Chapter 07 already knows to preserve first-party state. The Korean unit adds no new decision once the scoped policy fully resolves the relevant dimension.

**No load / negative control.**

### Case D — button / title

```text
카드 연결하기
```

No material addressee sentence-ending choice exists.

**No load / negative control.**

### Case E — subject honorification only

```text
listener ending already fixed
only -시- / subject-honorification issue remains
```

This is outside the candidate's owner-local scope.

**Do not expand the unit.**

### Necessity verdict

The surviving novelty is narrow:

```text
KOREAN SENTENCE-ENDING ADDRESSEE SPEECH LEVEL
+
FORMALITY / RESPECT NON-EQUIVALENCE
+
SUPPORTED SAME-RELATIONSHIP STYLE SHIFTING
+
BOUNDARY AGAINST SUBJECT/OBJECT HONORIFICATION
```

That is sufficient for one bounded adaptation candidate and insufficient for a Korean grammar module.

## 15. Architecture result

Current architecture is sufficient:

```text
owner                  Localization / Chapter 07
route                  adapt-localization.relationship-realization
new owner              NO
new route              NO
controller change      NO
Chapter 07 change      NO
routing-index change   NO
get-knowledge.py       NO
shared primitive       NO
hierarchy resolver     NO
speech-level score     NO
Korea country pack     NO
```

Complexity of Korean honorification does not itself establish a discovery, addressability, or composition failure.

## 16. Rejected hypotheses

### H1 — relationship determines one Korean ending style

Rejected. Same-listener formal/non-formal alternation can occur depending on situation [KOLA03][KOLA04].

### H2 — formal means more respectful

Rejected. `격식체` and `비격식체` are not a monotonic respect scale [KOLA01][KOLA02].

### H3 — customer means 하십시오체

Rejected. First-party KB evidence intentionally uses both `하십시오체` and `해요체` by communication function [KOLA07].

### H4 — marketing means 해요체

Rejected. Advertising usage varies by sentence type, involvement, and articulation context, and many sampled ad sentences use no such ending at all [KOLA08].

### H5 — experimental ad preference proves best practice

Rejected. KOLA09 is bounded experimental evidence, not a universal conversion rule.

### H6 — Korean honorific complexity requires a hierarchy resolver

Rejected. Neither `압존법` nor the subject/object/addressee distinctions justify a new runtime hierarchy graph [KOLA05][KOLA11].

### H7 — mixed speech levels are always errors

Rejected [KOLA03][KOLA04].

### H8 — mixed speech levels are always valid

Rejected. Supported alternation is evidence-dependent; approved state and discourse context can make a shift accidental drift.

## 17. Frozen adversarial cases K1–K16

### K1 — approved 하십시오체

```text
APPROVED ORGANIZATION STATE: 하십시오체
NO OTHER SPEECH-LEVEL DIMENSION OPEN
```

Expected: preserve; no reopen merely because Korean evidence exists.

### K2 — approved 해요체

Same as K1 with `해요체`.

Expected: preserve.

### K3 — same brand, different surfaces

```text
policy / restriction = 하십시오체
request / explanation = 해요체
```

Expected: preserve scoped first-party state; do not globally normalize the brand to one level.

### K4 — intentional style shift

Same speaker and listener shift `하십시오체 ↔ 해요체` with supported discourse function.

Expected: preserve; consistency alone is not repair authority.

### K5 — accidental style drift

```text
resolved surface voice = 해요체
no stance shift
no evidence for another speech level
draft randomly jumps into 해라체 / 하십시오체
```

Expected: repair drift. `Mixed != automatic error` must not become `mixed = always preserve`.

### K6 — "make it more formal"

Expected: do not automatically increase addressee respect or hierarchy. Clarify/realize the requested register without assuming a new relationship.

### K7 — "make it friendlier"

Expected: do not automatically downgrade to `해체`. Friendly stance does not itself authorize lower addressee treatment.

### K8 — title / button / nominal form

```text
카드 연결하기
```

Expected: no load; no finite addressee speech-level choice.

### K9 — honored third-party subject, listener ending fixed

Only subject honorification is materially open.

Expected: `KO-LANG-SPEECH-01` does not seize ownership.

### K10 — subject honorification + 해요체 coexist

Expected: do not classify co-occurring `-시-` and `해요체` as redundant "double politeness" merely because two honorification mechanisms appear.

### K11 — inanimate/customer-service edge

Example class includes room/object + `-시-`.

Expected: do not run a universal `사물존대` lookup. Preserve actual grammatical/honorific target analysis and ordinary Korean competence.

### K12 — 압존법 hierarchy cue

Senior listener and another senior referent are both present.

Expected: no mechanical suppression rule from rank alone.

### K13 — Korean outside Korea

Korean-language support targets users in another country and speech-level choice is open.

Expected: may load. Language realization does not require Korea-market membership.

### K14 — Korea market, English output

Expected: no Korean unit activation.

### K15 — relationship known, speech level unresolved and unavoidable

No scoped organization/community evidence resolves the ending choice.

Expected: do not invent `standard Korean = 하십시오체` or `marketing = 해요체`; preserve/expose the unresolved dependency according to Chapter 07.

### K16 — Korean noun with no relationship decision

Task mentions Korean/Korea, but no material sentence-ending addressee choice exists.

Expected: no load.

## 18. Evidence and inferential boundaries

Keep these distinctions explicit:

```text
OFFICIAL GRAMMATICAL DESCRIPTION
!= UNIVERSAL BRAND POLICY

ATTESTED STYLE SHIFTING
!= EVERY MIXED DRAFT IS VALID

FIRST-PARTY ORGANIZATION POLICY
!= POPULATION PREFERENCE

ADVERTISING CORPUS DISTRIBUTION
!= EFFECTIVENESS

EXPERIMENTAL FAVORABILITY EFFECT
!= CONVERSION RULE

LANGUAGE ETIQUETTE GUIDANCE
!= EXECUTABLE HIERARCHY RESOLVER
```

No single source proposes `KO-LANG-SPEECH-01`. The candidate is a repository-level synthesis constrained by the evidence ledger and existing architecture.

## 19. Final freeze adjudication

```text
KO-LANG-SPEECH-01
→ PROMOTE CANDIDATE FOR INDEPENDENT ADVERSARIAL REVIEW

SECOND KOREAN UNIT
→ NOT JUSTIFIED

NEW OWNER / ROUTE / CONTROLLER / RESOLVER
→ NOT JUSTIFIED

RUNTIME IMPLEMENTATION
→ NOT YET AUTHORIZED
```

The frozen candidate must now survive independent source adjudication, K1–K16, ordinary-grammar boundary attacks, composition with the existing VN/JP/ES units, and the counterfactual necessity test before any runtime promotion.