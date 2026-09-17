# Localization Adaptations

This file contains scoped local evidence that can materially change an already-open **localization realization** decision. It does not own audience, positioning, relationship, authority, platform, product, or commercial state.

Use the contribution contract in `README.md`. The logical route identifies the decision-relevant evidence family; each contribution below remains independently scope-checked.

## Relationship realization

### VN-LANG-REL-01 — Vietnamese self-reference and recipient-address realization

**SCOPE**

- language: Vietnamese (`vi`)
- market / geography: not inherently Vietnam-only; applicability follows target-language and interaction scope rather than nationality
- audience / role: audience-facing or interpersonal wording where self-reference and/or recipient address is explicit and materially unresolved
- channel / surface: any, unless an applicable channel, community, or organizational norm supplies stronger current evidence
- category / buying context: not category-specific
- effective period: structural / low-volatility linguistic evidence; preserve newer scoped evidence when it conflicts

**CLAIM**

Vietnamese person-reference is not exhausted by a neutral source-pronoun mapping. Address can be realized through personal pronouns, kinship terms, names, titles/roles, and other relational expressions [VNLA01][VNLA03]. Kinship-derived terms are also used in wider social communication, so their social use does not by itself assert literal kinship [VNLA01].

When both self-reference and recipient address are materially expressed, treat them as a **coupled relationship realization** rather than translating each source-language pronoun independently. Applied Vietnamese-language research documents that individual forms can be known while the resulting self/address combination remains pragmatically incompatible [VNLA02].

Regional evidence also shows that one national-language label does not imply one region-neutral inventory or expressive value [VNLA04].

**DECISION IMPACT**

This contribution can change only the bounded Chapter 07 decision:

> Given an already-resolved speaker/recipient relationship and interaction state, which Vietnamese self-reference / recipient-address realization preserves that state without inventing a different relation?

Use the already-resolved relationship as input. Select a coherent realization for the current artifact; do not use this contribution to decide who the speaker or recipient *is* to each other.

If one member of the self/address realization is already resolved while the other remains materially open, freeze the resolved member and use this contribution only for the still-open dimension. Coupled realization is a compatibility constraint; it is not permission to reopen both halves.

**LOAD WHEN**

Load this route only after the localization owner has an open realization decision and all are true:

```text
TARGET LANGUAGE = VIETNAMESE
+
SELF-REFERENCE OR RECIPIENT ADDRESS IS MATERIALLY OPEN
+
THE CHOICE CAN CHANGE RELATIONSHIP / STANDING /
INSTITUTIONAL ROLE / INTERPERSONAL DISTANCE CONVEYED
```

`Vietnam`, Vietnamese nationality, audience age, or a Vietnamese-market label alone is not activation authority.

**DO NOT USE WHEN**

- the task is only market selection or market research;
- the requested transformation contains no material person-reference choice;
- all material Vietnamese self-reference and recipient-address dimensions are already resolved by applicable approved forms and no truthful conflict requires reopening them;
- the only evidence is nationality, broad culture, age/status alone, or a generic demographic label;
- a regional form is being inferred merely from geography without scoped current evidence;
- the artifact's owner has already supplied a stronger current organizational, community, or first-party language rule that fully resolves the wording dimension still at issue.

A supplied form for only one dimension does not suppress this route when another dimension remains materially open. Preserve the supplied form exactly as resolved state and constrain only the open dimension to remain compatible with it.

**MUST PRESERVE**

- speaker / publishing identity;
- actual recipient relation;
- standing / authority;
- relevant interaction history;
- invited / expected / unsolicited state when material;
- autonomy / obligation and responsibility / repair state when material;
- applicable community / organizational norms;
- verified existing forms and approved voice;
- scoped regional evidence when it is actually supplied.

**MUST NOT INFER**

Do not manufacture any of the following from Vietnamese language, nationality, market, apparent age, or broad culture alone:

```text
KINSHIP
FAMILIARITY
HIERARCHY
INTIMACY
AUTHORITY
ORGANIZATIONAL ROLE
GENDERED RELATIONSHIP
AGE RELATIONSHIP
COMMUNITY STANDING
```

**REALIZATION GUARDRAILS**

```text
SOURCE "I" / "YOU"
!= TWO INDEPENDENT WORD SUBSTITUTIONS

KINSHIP-SHAPED SOCIAL ADDRESS
!= VERIFIED LITERAL KINSHIP

OLDER / YOUNGER / CUSTOMER / VIETNAMESE
!= FIXED ADDRESS LOOKUP KEY

"TÔI / BẠN"
!= UNIVERSAL SAFE DEFAULT

ONE HALF RESOLVED
!= REOPEN BOTH HALVES
```

If the relationship-indexing choice remains genuinely underdetermined, follow Chapter 07: preserve a verified existing form when applicable; otherwise prefer natural wording that avoids an unsupported relationship claim when the context permits it, and ask for missing state only when the choice is unavoidable and consequential.

**EVIDENCE**

Primary evidence records: [VNLA01][VNLA02][VNLA03][VNLA04] in `../references/local-adaptation-vietnam-evidence.md`.

Evidence type: local Vietnamese linguistic / applied-linguistic research. This evidence supports the realization mechanism and its boundaries; it does not establish a population preference, marketing lift, or deterministic address table.

**REVIEW STATE**

reviewed

**USAGE STATE**

active

### JP-LANG-HON-01 — Japanese honorific-target realization

**SCOPE**

- language: Japanese (`ja`)
- variety: common / standard Japanese unless stronger scoped regional, community, or organization evidence applies
- market / geography: not inherently Japan-only; applicability follows target-language and interaction scope rather than nationality or market
- audience / role: any audience-facing or interpersonal wording where honorific-sensitive participant orientation is materially unresolved
- channel / surface: any, unless an applicable accessibility, community, regional, or organizational rule supplies stronger current evidence for the dimension at issue
- category / buying context: not category-specific
- effective period: primarily structural / low-volatility linguistic evidence; preserve stronger newer scoped evidence where material

**CLAIM**

Japanese honorific realization is not one global `formal ↔ casual` scalar. Official Japanese guidance distinguishes honorific resources that can orient deference toward different semantic participants. In particular, `謙譲語Ⅰ` can honor the person who is the `向かう先` of an action, while `謙譲語Ⅱ` can be deferential toward the current addressee even when that addressee is not the action target [JPLA01][JPLA02].

Therefore, when material:

```text
POLITENESS TOWARD ADDRESSEE
!=
HONORIFICATION OF ACTOR / REFERENT
!=
HONORIFICATION OF ACTION TARGET
```

Official applied examples show that globally respectful intent is insufficient: a speaker can address one person respectfully while referring to an action directed toward a different person, and a humble form can become inappropriate when it honorifically orients toward the wrong action target [JPLA02][JPLA03].

`Uchi / soto` can be a real contextual factor, but official examples also defeat a mechanical `own side → always de-honorify` rule [JPLA04]. Regional honorific systems can also differ from common/standard Japanese, so this unit is not universal authority over stronger scoped regional/community evidence [JPLA11].

**DECISION IMPACT**

This contribution can change only the bounded Chapter 07 decision:

> Given already-resolved relationship, authority, interaction state, message meaning, and the semantic roles in the current utterance, which Japanese honorific realization preserves the intended relation without orienting honorification toward the wrong participant or action target?

Use already-resolved state as input. When the chosen Japanese construction depends on them, preserve the utterance-local distinction among addressee, actor/referent, action target, and speaker/publishing identity. These are local semantic roles in the current utterance, not new shared controller primitives.

If one realization dimension is already fixed by applicable approved wording or stronger scoped evidence, freeze that dimension and use this contribution only for the still-open honorific-sensitive choice.

**LOAD WHEN**

Load this route only after the localization owner has an open realization decision and all are true:

```text
TARGET LANGUAGE = JAPANESE
+
HONORIFIC-SENSITIVE PARTICIPANT ORIENTATION IS MATERIALLY OPEN
+
THE CHOICE CAN CHANGE WHO / WHAT THE JAPANESE FORM
TREATS AS THE ADDRESSEE, REFERENT, ACTOR, OR ACTION TARGET
FOR RELATIONAL / HONORIFIC PURPOSES
```

`Japan`, Japanese nationality, customer status, age, company context, or Japanese language alone is not activation authority. A mass-audience Japanese artifact with no material participant-sensitive honorific choice does not load this contribution merely because it is Japanese.

**DO NOT USE WHEN**

- the task is only market selection, country research, or bounded transformation with no material honorific-sensitive participant choice;
- all material Japanese honorific choices are already resolved by applicable approved forms and no truthful conflict requires reopening them;
- the only evidence is nationality, broad culture, age/status, customer status, organization membership, or geography alone;
- a regional form is being inferred merely from place without stronger scoped regional/community evidence;
- an applicable accessibility requirement or current organization/community rule already resolves the same wording dimension.

A supplied speech level such as `です / ます` does not suppress this contribution if honorific target orientation remains materially open. Freeze the resolved speech-level dimension and constrain only the open dimension.

**MUST PRESERVE**

- speaker / publishing identity;
- actual addressee relation;
- actor / referent and action target when materially distinguished in the current utterance;
- standing / authority;
- relevant interaction history;
- applicable organization / community context;
- autonomy / obligation and responsibility / repair state when material;
- verified existing forms and approved voice;
- applicable accessibility requirements;
- stronger scoped regional / community evidence when actually supplied.

**MUST NOT INFER**

Do not manufacture any of the following from Japanese language, nationality, market, customer status, age, apparent seniority, organization membership, or broad culture alone:

```text
WHO DESERVES HONORIFICATION
HIERARCHY
FAMILIARITY
ORGANIZATIONAL SIDE
AUTHORITY
CUSTOMER DEFERENCE LEVEL
REGIONAL HONORIFIC FORM
ONE UNIVERSAL FORMALITY LEVEL
```

**REALIZATION GUARDRAILS**

```text
"BE RESPECTFUL"
!= SUFFICIENT JAPANESE HONORIFIC TARGET

ADDRESSEE
!= ACTOR / REFERENT
!= ACTION TARGET

UCHI / SOTO
!= DETERMINISTIC LOOKUP TABLE

OWN ORGANIZATION
!= ALWAYS DE-HONORIFY

EXTERNAL PERSON
!= ALWAYS HONORIFY

CUSTOMER
!= MAXIMUM KEIGO

TARGET LANGUAGE = JA
!= STANDARD-JAPANESE UNIT HAS UNIVERSAL AUTHORITY
```

If honorific orientation remains genuinely underdetermined, preserve a verified existing form when applicable; otherwise prefer a natural realization that does not invent unsupported hierarchy or honorific target relations, and ask for missing state only when the choice is unavoidable and consequential.

**EVIDENCE**

Primary evidence records: [JPLA01][JPLA02][JPLA03][JPLA04][JPLA11] in `../references/local-adaptation-japan-evidence.md`.

Evidence type: Japanese government honorific guidance plus bounded regional evidence. These sources support the realization mechanism and its limits; they do not establish universal population preference, marketing lift, or a deterministic organization / age / customer lookup table.

**REVIEW STATE**

reviewed

**USAGE STATE**

active

### JP-LANG-PERM-01 — Japanese permission / benefit-sensitive deferential realization

**SCOPE**

- language: Japanese (`ja`)
- variety: common / standard Japanese unless stronger scoped regional, community, or organization evidence applies
- market / geography: not inherently Japan-only
- audience / role: audience-facing or interpersonal wording where an own-side action, announcement, refusal, repair, or other deferential realization remains materially open
- channel / surface: any, unless an applicable accessibility, community, regional, or organizational rule supplies stronger current evidence for the dimension at issue
- category / buying context: not category-specific
- material dimensions: permission, authority, agency, autonomy / obligation, benefit framing, responsibility / repair
- effective period: the baseline construction semantics are established, while pragmatic acceptability and extension are medium-volatility; newer scoped evidence may matter for usage judgments

**CLAIM**

The Japanese construction `〜させていただく` is not a semantically neutral transformation meaning only “make this more polite.” Official guidance describes its baseline analysis as an own-side action associated with permission from the addressee or a third party plus benefit to the speaker, with appropriateness varying by how strongly those conditions are satisfied or plausibly construed [JPLA05].

Therefore:

```text
INTRODUCING させていただく
!= SEMANTICALLY NEUTRAL POLITENESS POLISHING
```

At the same time, contemporary usage has expanded. NINJAL and recent Japanese research document cases in which the other party is weakly involved or the original permission/benefit meaning is pragmatically weakened through language change [JPLA06][JPLA07]. NHK variation evidence also shows that acceptability is context- and population-sensitive rather than one universal Japanese preference [JPLA08][JPLA09].

Therefore the reverse inference is also invalid:

```text
EXISTING させていただく
!= VERIFIED FACTUAL PERMISSION
!= VERIFIED FACTUAL BENEFIT
```

**DECISION IMPACT**

This contribution can change only the bounded Chapter 07 decision:

> Given already-resolved permission, authority, agency, autonomy/obligation, benefit, responsibility, and interaction state, does using, preserving, or replacing a Japanese deferential own-side-action form such as `〜させていただく` preserve that state rather than silently changing it?

This contribution consumes resolved state. It does not decide whether permission, legal authority, business authorization, benefit, obligation, or responsibility actually exists.

**LOAD WHEN**

Load this route only after the localization owner has an open realization decision and all are true:

```text
TARGET LANGUAGE = JAPANESE
+
AN OWN-SIDE ACTION / ANNOUNCEMENT / REFUSAL / REPAIR /
DEFERENTIAL POLITENESS CHOICE IS MATERIALLY OPEN
+
THE TARGET-LANGUAGE CHOICE CAN ALTER OR IMPLY
PERMISSION / AUTHORITY / AGENCY / AUTONOMY / OBLIGATION /
BENEFIT / RESPONSIBILITY / REPAIR FRAMING
```

This lookup may be required even when the user frames the task only as “make this more polite/natural in Japanese.” The possible semantic consequence, not the stylistic noun, is the reason to load.

`Japan`, Japanese nationality, customer status, business email, or “make it polite” alone is not activation authority.

**DO NOT USE WHEN**

- the task is only market selection, country research, or bounded transformation with no material own-side-action / deferential semantic choice;
- all material Japanese wording dimensions are already resolved by applicable approved forms and no truthful conflict requires reopening them;
- the only evidence is nationality, broad culture, age, region, or customer status;
- the contribution would be used to infer factual permission, legal authority, or benefit solely from an existing surface form;
- a current approved organization/community form fully resolves the same wording dimension and no stronger truthfulness conflict requires change.

Absence of independently verified permission does not by itself authorize replacing an approved existing `させていただく` form. Preserve the approved wording dimension while keeping factual permission state separate.

**MUST PRESERVE**

- speaker / publishing identity;
- actual addressee relation;
- resolved authority / permission state;
- agency and autonomy / obligation;
- responsibility / repair state;
- relevant interaction history;
- verified existing forms and approved voice;
- applicable organization / community norms;
- applicable accessibility requirements;
- stronger scoped regional / current usage evidence when material.

**MUST NOT INFER**

Do not manufacture any of the following from `させていただく`, Japanese language, nationality, market, age, region, or broad culture alone:

```text
FACTUAL PERMISSION
LEGAL AUTHORIZATION
CUSTOMER AUTHORIZATION
FACTUAL BENEFIT
TRANSFER OF DECISION AUTHORITY
LACK OF RESPONSIBILITY
ONE POPULATION-WIDE ACCEPTABILITY VERDICT
```

**REALIZATION GUARDRAILS**

```text
させていただく PRESENT
!= VERIFIED PERMISSION

させていただく PRESENT
!= VERIFIED BENEFIT

NO VERIFIED PERMISSION
!= AUTOMATICALLY FORBIDDEN

MORE POLITE
!= SEMANTICALLY NEUTRAL

DEFERENCE
!= TRANSFER OF DECISION AUTHORITY

APOLOGY / REPAIR
!= PERMISSION REQUEST

UNILATERAL DECISION
!= CUSTOMER AUTHORIZATION

AGE / REGION
!= FORM LOOKUP KEY
```

For Easy Japanese or another authoritative accessibility requirement, simpler realization may legitimately reduce honorific/deferential complexity while preserving respectful stance [JPLA10]. Accessibility is a scoped dependency, not a Japan-wide default.

**EVIDENCE**

Primary evidence records: [JPLA05][JPLA06][JPLA07][JPLA08][JPLA09][JPLA10] in `../references/local-adaptation-japan-evidence.md`.

Evidence type: Japanese government language guidance, NINJAL corpus/historical-pragmatics explanation, published Japanese scholarly synthesis on language change, recent NHK language-variation evidence, and government Easy Japanese guidance. This evidence supports the semantic risk and its non-transfer boundaries; it does not establish marketing lift, universal current preference, or factual permission from wording alone.

**REVIEW STATE**

reviewed

**USAGE STATE**

active

### ES-LANG-ADDR-01 — Spanish second-person address-system realization

**SCOPE**

- language: Spanish (`es`)
- variety: section-local; use pan-Hispanic claims only where the evidence supports them, and preserve stronger current regional, community, or organization evidence for the dimension at issue
- market / geography: not inherently Spain-, Latin-America-, or country-specific; applicability follows target-language realization rather than market membership
- audience / role: audience-facing or interpersonal wording where second-person treatment is explicit or materially implied and remains unresolved
- channel / surface: any; a surface may remain address-neutral when that is natural and no material relationship meaning is lost
- category / buying context: not category-specific
- effective period: core treatment-system facts are relatively structural; population preference, brand policy, and channel usage remain more scope- and time-sensitive

**CLAIM**

Spanish second-person realization is not one universal choice among `tú / vos / usted / vosotros / ustedes`. In scoped varieties, the tonic address form, verbal treatment pattern, and other treatment-sensitive forms can be coupled without being identical [ESLA01][ESLA03].

RAE/ASALE documents pronominal and verbal voseo that need not coincide, and ordinary American voseo can preserve `te`, `tu`, and `tuyo` rather than replacing an entire `tú` paradigm [ESLA01]. Chilean research provides a discriminating counterexample in which `tú +` voseante verbal morphology and `vos +` tuteante morphology are attested configurations [ESLA03].

Therefore:

```text
TONIC ADDRESS FORM
!= COMPLETE TREATMENT SYSTEM

PRONOUN
!= VERBAL TREATMENT PATTERN

MIXED PRONOUN / VERB FORM
!= AUTOMATIC ERROR
```

Plural realization also varies. Current Canarian evidence defeats `Spain → vosotros` and `ustedes → formal plural`: `ustedes` can serve familiar/peer as well as respectful plural treatment in the common Canarian pattern [ESLA05].

**DECISION IMPACT**

This contribution can change only the bounded Chapter 07 decision:

> Given already-resolved recipient relationship, intended stance, approved voice, applicable surface state, and target Spanish variety when materially known, how should second-person address be realized without inventing a different relationship, stance, or regional identity and without corrupting treatment-sensitive grammar?

Use resolved state as input. The unit may preserve a supported local treatment system, repair only the treatment-sensitive forms that are inconsistent with the resolved system, and preserve legitimate mixed pronominal/verbal configurations when scoped evidence supports them.

If applicable first-party organization or channel policy already resolves the relevant treatment dimension, freeze it. Broader sociolinguistic evidence is not permission to reopen that choice merely because other Spanish systems exist [ESLA07][ESLA08].

**LOAD WHEN**

Load this route only after the localization owner has an open realization decision and all are true:

```text
TARGET LANGUAGE = SPANISH
+
SECOND-PERSON TREATMENT REALIZATION IS MATERIALLY OPEN
+
THE CHOICE CAN CHANGE RELATIONSHIP / STANCE /
VARIETY-SENSITIVE ADDRESS OR TREATMENT-SYSTEM COHERENCE
```

A materially ambiguous `usted / ustedes` verbal form may also load this unit when second-person treatment realization has collapsed an addressee/third-party distinction because the verbal agreement shares third-person morphology [ESLA11].

`Spanish`, `Spain`, `Latin America`, a country name, customer status, age, social-media context, or a Spanish-speaking-market label alone is not activation authority.

**DO NOT USE WHEN**

- the task is only market selection, country research, or localization with no material second-person treatment choice;
- all material Spanish treatment dimensions are already resolved by applicable approved forms and no truthful or linguistic conflict requires reopening them;
- the surface naturally uses an address-neutral form and no material relationship meaning is lost;
- the remaining issue is ordinary Spanish grammar unrelated to the treatment system;
- the only evidence is country, nationality, broad region, age/status, customer status, or a generic market label;
- the contribution would be used to infer a regional form merely from geography without stronger scoped evidence;
- a current first-party organization/community/surface policy fully resolves the treatment dimension still at issue.

An address-neutral realization is optional only where it is natural for the surface. Do not make direct copy awkward or impersonal merely to hide an unresolved treatment dependency [ESLA09][ESLA10].

**MUST PRESERVE**

- speaker / publishing identity;
- actual recipient relation;
- intended stance and supported interactional shifts;
- relevant interaction history;
- singular / plural audience reference;
- verified existing treatment forms and approved voice;
- applicable organization / channel policy;
- scoped target-variety or community evidence when actually supplied;
- source addressee / third-party referent distinctions when treatment-sensitive verbal morphology makes them material.

**MUST NOT INFER**

Do not manufacture any of the following from Spanish language, country, nationality, broad region, customer status, age, or channel alone:

```text
ONE UNIVERSAL ADDRESS SYSTEM

TÚ = INFORMAL

USTED = FORMAL

VOS = REQUIRED IN A VOSEO REGION

SPAIN = VOSOTROS

LATIN AMERICA = ONE TREATMENT SYSTEM

USTEDES = FORMAL PLURAL

COUNTRY = TARGET VARIETY

CUSTOMER = USTED

SOCIAL MEDIA = TÚ

LOCAL EVERYDAY SPEECH = BRAND POLICY
```

**REALIZATION GUARDRAILS**

```text
PRONOUN
!= COMPLETE TREATMENT PARADIGM

VOS
!= REPLACE TÚ EVERYWHERE

VOS
!= REPLACE TE / TU / TUYO

TÚ
!= NECESSARILY TUTEANTE VERB MORPHOLOGY

MIXED FORM
!= AUTOMATIC ERROR

MIXED FORM
!= AUTOMATICALLY VALID

USTEDES
!= FORMAL PLURAL BY DEFINITION

SPAIN
!= VOSOTROS IN EVERY VARIETY

EVERYDAY SPEECH NORM
!= AUTOMATIC MARKETING REALIZATION

ADDRESS-NEUTRAL WORDING EXISTS
!= MUST USE IT
```

When the resolved treatment system changes or a draft drifts away from it, recheck only the treatment-sensitive forms actually present. Do not turn this contribution into a full Spanish conjugation or proofreading module [ESLA01].

For `usted / ustedes`, second-person verbal agreement shares morphology with third-person forms [ESLA11]. If that creates a material addressee-versus-third-party ambiguity in context, clarify the referent only as needed using a natural formulation supported for the target variety and voice. Do not import another variety's address paradigm solely to disambiguate.

Possessive or other referent ambiguity, including `su / sus`, remains generic source-referent fidelity / ordinary Spanish competence under the current evidence set. Do not treat it as an independently evidenced `ES-LANG-ADDR-01` mechanism or prescribe a Spanish-specific possessive repair without separate evidence.

If the treatment choice remains genuinely underdetermined, follow Chapter 07: preserve an applicable verified existing form; otherwise use natural wording that avoids unsupported relationship claims when the surface permits it, and expose or request the missing state only when the socially meaningful choice is unavoidable and consequential.

**EVIDENCE**

Primary mechanism evidence: [ESLA01][ESLA03][ESLA05][ESLA11] in `../references/local-adaptation-spanish-evidence.md`.

Boundary and composition evidence: [ESLA02][ESLA04][ESLA06][ESLA07][ESLA08][ESLA09][ESLA10] in the same ledger.

Evidence type: authoritative pan-Hispanic grammatical references, scoped Spanish-language sociolinguistic research, current regional academy guidance, bounded advertising-context research, and first-party organization/product style policies. These sources support the treatment-system mechanism and its non-transfer boundaries; they do not establish universal population preference, country lookup rules, marketing lift, or one pan-Hispanic brand voice.

**REVIEW STATE**

reviewed

**USAGE STATE**

active

### KO-LANG-SPEECH-01 — Korean addressee speech-level realization

**SCOPE**

- language: Korean (`ko`)
- market / geography: not inherently Korea-only; applicability follows target-language realization rather than nationality or market membership
- audience / role: audience-facing or interpersonal wording where a finite sentence-ending addressee speech-level choice is materially open or being changed
- channel / surface: any, but only when an addressee-facing ending choice is actually material; titles, labels, banners, buttons, and nominal/non-final forms may require no speech-level decision
- category / buying context: not category-specific
- effective period: core grammatical distinctions are relatively structural; organization policy, usage distribution, and response effects remain scope- and time-sensitive

**CLAIM**

Korean `상대 높임법` realizes addressee treatment through sentence-ending choices including `해라체`, `하게체`, `하오체`, `하십시오체`, `해체`, and `해요체` [KOLA01]. The critical runtime constraint is not simply that Korean has polite and casual endings. Formal/non-formal register and addressee respect are related but non-identical dimensions [KOLA01][KOLA02].

Therefore:

```text
ADDRESSEE RESPECT
!= FORMALITY / REGISTER
!= INTERPERSONAL DISTANCE
!= DISCOURSE FUNCTION

FORMAL
!= MORE RESPECTFUL

NON-FORMAL
!= LESS RESPECTFUL
```

Current usage evidence also supports contextual speech-level shifting with the same listener, including `하십시오체 ↔ 해요체` shifting in formal situations [KOLA03][KOLA04]. Therefore a fixed broad relationship does not require one invariant speech level across every utterance.

```text
ONE RELATIONSHIP
!= ONE SPEECH LEVEL FOR EVERY UTTERANCE

SPEECH-LEVEL SHIFT
!= AUTOMATIC RELATIONSHIP SHIFT

MIXED SPEECH LEVELS
!= AUTOMATIC ERROR
!= AUTOMATICALLY VALID
```

The last boundary is required: preserve a supported shift, but repair unsupported drift when applicable organization, interaction, stance, or surrounding discourse state resolves another system.

**DECISION IMPACT**

This contribution can change only the bounded Chapter 07 decision:

> Given already-resolved recipient relationship, interaction state, intended stance, approved voice, communication function, and applicable organization/surface evidence, how should Korean sentence-ending addressee speech level be realized without inventing a different relationship, collapsing formality into respect, or normalizing a legitimate discourse-functional shift?

Use resolved state as input. The unit may preserve an approved speech-level policy, distinguish register from addressee respect, preserve a supported same-listener style shift, repair unsupported speech-level drift, and leave naturally non-final surfaces alone when no ending decision exists.

If an applicable first-party organization or surface policy already resolves the relevant speech-level dimension, freeze it. Broader linguistic or marketing evidence is not permission to reopen that choice merely because other Korean styles exist [KOLA07].

**LOAD WHEN**

Load this route only after the localization owner has an open realization decision and all are true:

```text
TARGET LANGUAGE = KOREAN
+
ADDRESSEE SPEECH-LEVEL REALIZATION
IS MATERIALLY OPEN OR BEING CHANGED
+
THE CHOICE CAN ALTER ADDRESSEE RESPECT / REGISTER /
INTERPERSONAL DISTANCE / DISCOURSE FUNCTION
```

`Korean`, `Korea`, customer status, age, seniority, business context, marketing, social media, or a request for “polite Korean” alone is not activation authority.

**DO NOT USE WHEN**

- the task is only market selection, Korea research, or localization with no material finite addressee-ending choice;
- all material Korean speech-level dimensions are already resolved by applicable approved forms and no truthful or linguistic conflict requires reopening them;
- the surface naturally uses a title, label, button, banner, noun, nominal ending, or other non-final realization with no material addressee speech-level choice [KOLA07][KOLA08];
- the only open issue is subject or object/action-target honorification rather than sentence-ending addressee treatment;
- the remaining issue is ordinary Korean grammar unrelated to addressee speech level;
- activation would rest only on nationality, market, age, job title, customer status, organization membership, or broad culture;
- a current first-party organization/community/surface policy fully resolves the speech-level dimension still at issue.

Non-final or address-neutral realization is optional only where natural for the surface. Do not distort direct conversational copy merely to hide an unresolved speech-level dependency.

**MUST PRESERVE**

- speaker / publishing identity;
- actual recipient relationship;
- standing / authority already resolved upstream;
- relevant interaction history and interaction state;
- intended stance;
- communication function of the utterance;
- verified existing speech-level choices and approved voice;
- supported discourse-functional speech-level shifts;
- applicable organization / surface / community policy;
- applicable accessibility constraints;
- truthfulness and source participant/reference distinctions.

**MUST NOT INFER**

Do not manufacture any of the following from Korean language, Korea market, age, job title, customer status, organization membership, or broad culture alone:

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

**REALIZATION GUARDRAILS**

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

ONE RELATIONSHIP
!= ONE INVARIANT SPEECH LEVEL

SUPPORTED SPEECH-LEVEL SHIFT
!= AUTOMATIC DRIFT

MIXED SPEECH LEVELS
!= AUTOMATICALLY VALID
```

Korean subject, object/action-target, and addressee honorification remain separate dimensions [KOLA05][KOLA06]:

```text
ADDRESSEE SPEECH LEVEL
!= SUBJECT HONORIFICATION
!= OBJECT / ACTION-TARGET HONORIFICATION
```

If only `-시-`, lexical object honorification, or another subject/object-honorification issue remains open while the addressee ending is already resolved, do not use `KO-LANG-SPEECH-01` to seize that decision. The current evidence does not justify `KO-LANG-HON-02`.

Do not convert `사물존대` into `inanimate + -시- → always wrong` or `customer-related noun + -시- → always correct`; KOLA10 establishes a grammatical boundary, not a lookup table. Likewise, `압존법` does not justify a listener-rank/referent-rank suppression algorithm or hierarchy resolver [KOLA11].

Marketing evidence remains contextual only. Distribution in TV ads and bounded experimental response effects show that speech-level realization can vary materially and affect response under tested conditions [KOLA08][KOLA09]; they do not establish `해요체` as a default, conversion lift, or a universal channel rule.

If the speech-level choice remains genuinely underdetermined and unavoidable, follow Chapter 07: preserve an applicable verified existing form; otherwise keep the unresolved dependency visible rather than inventing `standard Korean = 하십시오체`, `marketing = 해요체`, or another cultural default.

**EVIDENCE**

Primary mechanism evidence: [KOLA01][KOLA02][KOLA03][KOLA04] in `../references/local-adaptation-korean-evidence.md`.

Boundary and composition evidence: [KOLA05][KOLA06][KOLA07][KOLA08][KOLA09][KOLA10][KOLA11] in the same ledger.

Evidence type: current National Institute of Korean Language guidance, published Korean applied-linguistics research, first-party organization language policy, and bounded Korean advertising research. These sources support the speech-level mechanism and its non-transfer boundaries; they do not establish a Korea-wide relationship lookup, one universal brand voice, a hierarchy graph, or marketing lift.

**REVIEW STATE**

reviewed

**USAGE STATE**

active

### PT-LANG-ADDR-01 — Portuguese second-person address-system realization

**SCOPE**

- language: Portuguese (`pt`)
- market / geography: not inherently Brazil-, Portugal-, Angola-, Mozambique-, or country-specific; applicability follows target-language realization and scoped evidence rather than market membership
- audience / role: audience-facing or interpersonal wording where second-person treatment-system realization is materially open or being changed
- channel / surface: any, but only when second-person treatment morphology or explicit/null addressee realization is material
- category / buying context: not category-specific
- effective period: core structural variation is relatively durable; sociolinguistic distribution, organization policy, and surface usage remain scope- and time-sensitive

**CLAIM**

Portuguese second-person discourse reference is not mechanically determined by one visible address form. In scoped Portuguese varieties, subject form, verbal agreement, object clitics, possessives, and related person-sensitive forms can combine in ways that do not collapse into one uniform textbook paradigm [PTLA04][PTLA05][PTLA06][PTLA07][PTLA08].

Therefore:

```text
ADDRESS FORM
!= COMPLETE PERSON PARADIGM

TU
!= AUTOMATIC OVERT 2SG AGREEMENT EVERYWHERE

VOCÊ SUBJECT
!= AUTOMATIC REPLACEMENT OF TE

VOCÊ
!= AUTOMATIC COMPLETE 3SG PARADIGM ACROSS ALL FORMS

SCOPED VOCÊ + TU-DERIVED / 2SG-SHAPED FORMS
!= AUTOMATIC CORRUPTION

ATTESTED COMPOSITION
!= BLANKET PRESERVATION OF EVERY MIX
```

Portuguese also has a distinct explicitness-sensitive treatment boundary. In scoped European Portuguese evidence, explicit `você` and third-person-singular realization with no overt subject are not pragmatically interchangeable merely because both can address the recipient with 3SG verbal morphology [PTLA02][PTLA03].

```text
EXPLICIT VOCÊ
!= NULL 3SG ADDRESS REALIZATION

SAME 3SG VERBAL MORPHOLOGY
!= SAME TREATMENT REALIZATION

ZERO OVERT PRONOUN
!= ZERO PRAGMATIC / RELATIONAL VALUE
```

A transformation such as `Deseja continuar? → Você deseja continuar?` is therefore not guaranteed to be relationship-neutral.

**DECISION IMPACT**

This contribution can change only the bounded Chapter 07 decision:

> Given an already-resolved recipient relationship, stance, interaction state, approved voice, and applicable scoped Portuguese variety/community/organization evidence, how should second-person address be realized without falsely treating one address form as a complete person paradigm, mechanically normalizing supported treatment-system composition, or changing treatment value by inserting/removing an explicit addressee form?

Use resolved state as input. The unit may preserve supported `tu / você` treatment composition, preserve supported `tu` agreement patterns, preserve supported `você + te` or analogous scoped composition, distinguish explicit `você` from null-3SG realization when material, and repair unsupported drift only against applicable resolved state.

If an explicit first-party writing rule or approved organization/surface policy resolves the relevant treatment dimension, freeze it. Current first-party surface usage can also be strong scoped evidence and may be resolved state when it is the actual approved wording/voice, but observed usage alone must not be upgraded into a documented organization policy [PTLA10][PTLA11][PTLA12].

**LOAD WHEN**

Load this route only after the localization owner has an open realization decision and all are true:

```text
TARGET LANGUAGE = PORTUGUESE
+
SECOND-PERSON TREATMENT REALIZATION
IS MATERIALLY OPEN OR BEING CHANGED
+
THE OPEN CHOICE CAN ALTER TREATMENT-SYSTEM COHERENCE
OR EXPLICIT / NULL ADDRESSEE REALIZATION
```

`Portuguese`, `Brazil`, `Portugal`, `Angola`, `Mozambique`, customer status, age, business context, formality, friendliness, public-sector context, marketing, or social media alone is not activation authority.

**DO NOT USE WHEN**

- the task is only market selection, country research, locale formatting, or localization with no material second-person treatment choice;
- all material Portuguese treatment dimensions are already resolved by applicable approved forms and no truthful or linguistic conflict requires reopening them;
- the surface naturally contains no material second-person/addressee realization;
- the remaining issue is ordinary Portuguese grammar unrelated to the treatment system;
- the only remaining issue is generic source-referent ambiguity such as `seu / sua` with the treatment system already fixed;
- activation would rest only on country, nationality, age, customer status, channel, organization membership, or broad culture;
- an applicable explicit first-party rule fully resolves the treatment dimension still at issue.

A country label does not select a target variety or treatment system. If the choice remains genuinely underdetermined, preserve an applicable verified form or approved current wording when possible; otherwise follow Chapter 07 rather than inventing a country/pronoun default.

**MUST PRESERVE**

- speaker / publishing identity;
- actual recipient relationship;
- standing / authority resolved upstream;
- relevant interaction history and interaction state;
- intended stance;
- source addressee / third-party distinctions;
- verified treatment forms already supplied;
- approved organization / surface voice;
- scoped target-variety / community evidence when actually supplied;
- applicable accessibility / plain-language constraints;
- truthfulness and source meaning;
- the distinction between documented first-party policy and observed current first-party usage.

**MUST NOT INFER**

Do not manufacture any of the following from Portuguese language, country, nationality, market, customer status, age, channel, organization membership, or broad culture alone:

```text
BRAZIL = VOCÊ
PORTUGAL = TU
ANGOLA = ONE SYSTEM
MOZAMBIQUE = ONE SYSTEM
COUNTRY = TARGET VARIETY
CUSTOMER = VOCÊ
FORMAL = SENHOR / SENHORA
FRIENDLY = TU
YOUNG = TU
GOVERNMENT = VOCÊ
TU = OVERT 2SG EVERYWHERE
VOCÊ = COMPLETE 3SG PARADIGM EVERYWHERE
ONE PRONOUN = ONE COMPLETE TREATMENT PARADIGM
CURRENT FIRST-PARTY USAGE = DOCUMENTED POLICY
OBSERVED CROSS-SURFACE DIFFERENCE = VERIFIED INTENTIONAL POLICY
```

**REALIZATION GUARDRAILS**

```text
ADDRESS FORM
!= COMPLETE PERSON PARADIGM

TU
!= AUTOMATIC OVERT 2SG AGREEMENT

VOCÊ SUBJECT
!= AUTOMATIC REPLACEMENT OF TE

VOCÊ + TE
!= AUTOMATIC ERROR

VOCÊ + 2SG-SHAPED FORM
!= AUTOMATIC ERROR

MIXED PARADIGM
!= AUTOMATIC ERROR
!= AUTOMATICALLY VALID

EXPLICIT VOCÊ
!= NULL 3SG ADDRESS REALIZATION

ZERO OVERT PRONOUN
!= ZERO RELATIONSHIP MEANING

BRAZIL / PORTUGAL / ANGOLA / MOZAMBIQUE
!= TREATMENT LOOKUP KEY

FORMAL
!= SENHOR / SENHORA LOOKUP

FIRST-PARTY USAGE
!= POPULATION NORM
!= DOCUMENTED POLICY BY DEFAULT
```

When the resolved treatment system changes or a draft drifts away from it, recheck only treatment-sensitive forms actually implicated. Do not turn this contribution into a full Portuguese conjugation, clitic, possessive, or proofreading module.

Possessive or other referent ambiguity, including `seu / sua`, remains generic source-referent fidelity / ordinary Portuguese competence under the current evidence set. Do not treat it as an independently evidenced `PT-LANG-ADDR-01` mechanism or prescribe a Portuguese-specific possessive resolver without separate evidence.

Current first-party usage must retain its evidence class. PTLA10 is documented gov.br policy within its actual service-writing scope. PTLA11 and PTLA12 are current scoped gov.pt usage evidence; they show that one organization ecosystem can exhibit different treatment realizations, but they do not independently prove a documented or intentional cross-surface policy.

If the treatment choice remains genuinely underdetermined and unavoidable, follow Chapter 07: preserve applicable verified existing wording when possible, use natural wording that avoids unsupported relationship claims where the surface permits it, and expose or request missing state only when the socially meaningful choice is unavoidable and consequential.

**EVIDENCE**

Primary mechanism evidence: [PTLA02][PTLA03][PTLA04][PTLA05][PTLA06][PTLA07][PTLA08] in `../references/local-adaptation-portuguese-evidence.md`.

Boundary and composition evidence: [PTLA01][PTLA09][PTLA10][PTLA11][PTLA12] in the same ledger.

Evidence type: published Portuguese sociolinguistic/pragmatic research across scoped varieties plus bounded first-party public-service evidence. PTLA10 is documented first-party policy within its scope; PTLA11/PTLA12 are current first-party usage, not documented cross-surface policy. These sources do not establish country-wide treatment defaults, a country/variety resolver, population preference, universal brand voice, hierarchy mapping, or marketing lift.

**REVIEW STATE**

provisional

**USAGE STATE**

active