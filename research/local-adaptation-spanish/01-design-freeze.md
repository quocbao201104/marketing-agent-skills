# Spanish Local Adaptation — Design Freeze

Status: **FROZEN FOR INDEPENDENT ADVERSARIAL REVIEW**  
Freeze date: 2026-09-17  
Repository base: `main@44573c1aaebd44d04a1e5699f1dc4324743a0704`

## 1. Research question

In Spanish-language marketing communication, are there second-person realization decisions that an agent can still get materially wrong after the generic Marketing Practitioner controller has correctly resolved relationship, stance, audience, message, authority, and other upstream state — because the remaining choice depends on a Spanish-specific treatment system?

The purpose of this research is not to build a Spanish-speaking market profile, a Spain-versus-Latin-America locale pack, or a general Spanish grammar guide. It is to pressure the existing scoped local-adaptation architecture with a language whose second-person systems vary across regions, registers, and surfaces in ways that can change relationship realization and grammatical coherence.

The promotion gate is unchanged:

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

> Remove the Spanish-specific knowledge, but keep all task-specific evidence and the generic handbook. Can the existing owner still make the correct realization decision reliably?

If yes, the material stays generic, scoped evidence, or a current task dependency. If no, it may justify one bounded local adaptation unit.

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

Chapter 07 already preserves relationship-sensitive realization state and exposes the bounded JIT edge:

```text
localization realization remains materially open
→ inspect owner-aligned adapt-localization knowledge
→ smallest matching route
→ section-local scope check
```

The current logical route is:

```text
adapt-localization.relationship-realization
```

That route already contains Vietnamese and Japanese contributions. This research asks whether Spanish contributes a distinct target-language mechanism under the same owner and route without requiring country-first routing, a new controller job, or a new scope system.

## 3. Freeze verdict

One Spanish-specific mechanism survives the promotion gate:

```text
ES-LANG-ADDR-01
Spanish second-person address-system realization
→ PROMOTE CANDIDATE
```

The following do not survive as separate runtime units or architecture:

```text
Spain / Latin America country packs
→ REJECT

formal ↔ informal lookup table
→ REJECT

"tú / vos / usted" as one universal social scale
→ REJECT

voseo-country lookup
→ REJECT

"neutral Spanish" as a universal fallback
→ REJECT

artifact-type activation such as SEO / UI / legal
→ REJECT

always normalize mixed treatment forms
→ REJECT

always avoid second person when variety is unknown
→ REJECT

full Spanish grammar module
→ REJECT

new route / owner / controller machinery
→ REJECT
```

No evidence currently justifies a second Spanish unit.

## 4. ES-LANG-ADDR-01 — Spanish second-person address-system realization

### 4.1 Local-specific mechanism

Spanish second-person realization cannot generally be reduced to selecting one pronoun from:

```text
tú / vos / usted
vosotros / ustedes
```

The local-specific mechanism has three coupled but non-identical parts when material:

```text
TONIC ADDRESS FORM
!=
VERBAL TREATMENT PATTERN
!=
OTHER TREATMENT-SENSITIVE FORMS
```

RAE/ASALE evidence on voseo shows that legitimate Spanish varieties may combine pronoun and verbal treatment differently. American `vos` ordinarily coexists with clitic `te` and possessives `tu / tuyo`; some varieties admit `tú` with voseante verb forms; other mixed systems are also documented [ESLA01][ESLA03].

Therefore:

```text
PRONOUN
!= COMPLETE ADDRESS PARADIGM

VOS
!= REPLACE TÚ EVERYWHERE

TÚ
!= NECESSARILY TUTEANTE VERB MORPHOLOGY

MIXED FORM
!= AUTOMATIC ERROR
```

This creates a real failure that Chapter 07 cannot solve from relationship state alone.

Example pressure:

```text
resolved state:
- target variety: Chilean Spanish
- relationship: familiar
- supplied / approved wording: tú + voseante verb form

naive normalization:
"Si tú querís..." → "Si tú quieres..."
```

The generic owner can preserve familiarity, but without Spanish-specific evidence it cannot know that the apparent pronoun/verb mismatch may be a legitimate local configuration rather than accidental model drift [ESLA03].

A second pressure case is voseo repair:

```text
resolved state:
- target: Rioplatense Spanish
- approved address: vos

naive edit:
tú → vos
while retaining tuteante imperative morphology
```

Correct realization may require selective verb or imperative repair while preserving forms such as `te` and `tu / tuyo` that do not simply switch to a new paradigm [ESLA01].

Therefore:

```text
RELATIONSHIP ALREADY RESOLVED
!=
SPANISH ADDRESS SYSTEM ALREADY REALIZED CORRECTLY
```

### 4.2 Existing owner

Owner remains:

```text
Localization / Chapter 07
```

The unit consumes resolved relationship, stance, speaker/publishing identity, interaction state, approved voice, and applicable variety evidence. It does not decide what the relationship should be, whether a customer deserves more deference, or which regional identity the brand should adopt.

### 4.3 Decision impact

The bounded question is:

> Given already-resolved recipient relationship, intended stance, surface or channel state when relevant, approved voice, and target Spanish variety when materially known, how should second-person address be realized without inventing a different relationship, stance, or regional identity and without corrupting treatment-sensitive grammar?

The unit may:

```text
- preserve an already-approved treatment form;
- select among supported Spanish address realizations when the choice remains open;
- preserve a legitimate mixed pronominal/verbal system;
- repair only treatment-sensitive forms that are actually inconsistent with the resolved system;
- resolve material referent ambiguity introduced by the selected realization using a natural supported formulation.
```

It may not independently determine audience relationship, brand positioning, legal status, customer hierarchy, or a market-wide preference.

### 4.4 Scope

Candidate scope:

```text
language: Spanish (`es`)
variety: section-local; pan-Hispanic claims only where evidence supports them
market / geography: not inherently Spain- or country-specific
channel: any where second-person treatment is materially open
category: not category-specific
effective period: structural language mechanisms are relatively low-volatility;
                  usage/preference evidence is more scope- and time-sensitive
```

Spanish language, a Spanish-speaking country, customer status, age, social-media context, or a market label alone are not activation authority.

### 4.5 Must preserve

When material:

```text
speaker / publishing identity
recipient relation
intended stance
interaction history
singular / plural audience reference
approved brand or organization voice
surface / channel-specific approved policy
known target variety or community evidence
existing approved address forms
source referent distinctions
```

### 4.6 Must not infer

```text
Spanish → one universal address system

informal → tú

formal → usted

Spain → vosotros

Latin America → one treatment system

voseo region → always use vos

ustedes → formal plural

country → target variety

customer → usted

social media → tú

local everyday speech → marketing preference

mixed pronoun / verb morphology → error
```

## 5. Treatment forms are not a universal linear scale

Spanish address forms do not form one stable pan-Hispanic ladder from intimate to formal.

RAE/ASALE and sociolinguistic research show that `tú`, `vos`, and `usted` vary in distribution and social meaning across varieties. In some systems `vos` occupies familiar use; in others `tú` and `vos` coexist with different values. Bogotá evidence also shows that `usted` cannot be reduced to a universal formal-or-distant marker; contextual and affective uses can differ within interaction [ESLA02][ESLA04].

Freeze:

```text
ADDRESS FORM
!= UNIVERSAL RELATIONSHIP LABEL
```

Country and broad region can identify relevant evidence to inspect. They do not by themselves decide the relationship realization.

## 6. Voseo requires selective, not total, grammatical propagation

Voseo is not one universal morphology and does not create a wholly separate second-person paradigm.

For American voseo, RAE/ASALE documents combinations including:

```text
vos + voseante verb morphology
vos + te
vos + tu / tuyo
```

and also documents pronominal and verbal voseo that need not always coincide [ESLA01].

Therefore:

```text
ADDRESS REALIZATION CHANGES
→ CHECK TREATMENT-SENSITIVE FORMS PRESENT IN THE ARTIFACT

DO NOT
→ blindly replace every clitic, possessive, pronoun, tense, or imperative
```

The unit is a realization guardrail, not a Spanish conjugation handbook.

## 7. Plural address belongs to the same mechanism

Plural address creates real decision differences but does not justify a separate unit.

In much of Spanish America, `ustedes` serves as the ordinary plural address form across familiar and formal relations. In much of peninsular Spanish, `vosotros` and `ustedes` can preserve a familiar/formal distinction. Canarias provides a direct counterexample to the country lookup `Spain → vosotros`: current Academia Canaria guidance describes widespread `ustedes` use for both familiar/peer and respectful plural, while some areas retain `vosotros` [ESLA05].

Freeze:

```text
USTEDES
!= FORMAL PLURAL BY DEFINITION

SPAIN
!= VOSOTROS BY DEFAULT IN EVERY VARIETY
```

Plural variation remains part of `ES-LANG-ADDR-01` because the practical failure is still second-person treatment realization.

## 8. Referential ambiguity is a repair condition, not a new owner

`usted / ustedes` use third-person verbal morphology, and possessives such as `su / sus` can be referentially ambiguous in context.

The Spanish unit may therefore need to detect a material loss such as:

```text
YOU ALL
vs
THEY
```

when both collapse into locally identical surface morphology.

But this does not justify a Spanish reference-resolution primitive.

Freeze:

```text
IF ADDRESS-SYSTEM REALIZATION
CREATES MATERIAL REFERENT AMBIGUITY
→ EXPLICITATE ONLY AS NEEDED
→ USE A NATURAL STRATEGY SUPPORTED FOR THE TARGET VARIETY / VOICE

AMBIGUITY
!= PERMISSION TO IMPORT ANOTHER VARIETY'S PARADIGM
```

For example, ambiguity is not sufficient reason to import `vosotros / vuestro` into a variety whose supported plural system is `ustedes`.

## 9. Everyday speech norm is not automatically marketing realization

Marketing-specific evidence is important as a boundary, not as a lookup table.

A 2025 study of advertising in El Salvador found a divergence between familiar spontaneous speech and the treatment forms favored in the advertising contexts studied. That supports the proposition that everyday local speech does not mechanically determine marketing realization [ESLA06].

It does not establish that Salvadoran advertising should always use `tú`, that `tú` converts better, or that a professional-services category requires `usted`.

First-party style guides provide a stronger type of evidence for a specific artifact when they explicitly resolve the choice. Head Start and Mozilla provide examples in which an organization fixes treatment by channel, locale, or product surface [ESLA07][ESLA08].

Freeze:

```text
LOCAL SPEECH NORM
!= AUTOMATIC MARKETING NORM

APPROVED ORGANIZATION / CHANNEL STATE
CAN RESOLVE THE ADDRESS FORM
WITHIN ITS ACTUAL SCOPE
```

The local adaptation must not reopen an already-resolved first-party treatment choice merely because broader market evidence differs.

## 10. Address avoidance is a bounded option, not a fallback regime

Some Spanish surfaces naturally permit address-neutral realization.

Examples include UI labels such as infinitival action labels and general-public notices where Spanish convention naturally permits an infinitive [ESLA09][ESLA10].

This supports only a bounded rule:

```text
VARIETY / ADDRESS STATE UNKNOWN
+
SURFACE NATURALLY PERMITS
ADDRESS-NEUTRAL REALIZATION
+
NO MATERIAL RELATIONSHIP MEANING IS LOST
→ MAY AVOID COMMITTING TO AN ADDRESS SYSTEM
```

It does not support:

```text
unknown variety
→ rewrite all Spanish copy impersonally
```

Direct explanatory, conversational, support, editorial, or marketing copy may naturally require a treatment choice. The adaptation should not distort the communication job merely to avoid an unresolved dependency.

## 11. Negative activation result

Artifact type is not activation authority.

A UI button may be fully address-neutral. An SEO article, technical guide, government page, product flow, or legal-information page may still contain direct `tú` or `usted` realization.

Therefore:

```text
SEO / UI / PRODUCT LISTING / LEGAL / SOCIAL
!= LOAD OR DO-NOT-LOAD KEY
```

Candidate `DO NOT USE WHEN`:

```text
- the task only mentions Spanish, Spain, Latin America, or a Spanish-speaking market;
- the current wording contains no materially open second-person realization;
- applicable approved wording or organization policy already resolves the relevant treatment dimensions and no truthful conflict requires reopening them;
- the surface naturally uses an address-neutral form and no relationship meaning is lost;
- the remaining issue is ordinary Spanish grammar unrelated to treatment-system realization;
- the contribution would be used to infer familiarity, hierarchy, audience preference, or brand policy from country / nationality / market alone.
```

## 12. Necessity test against Chapter 07

The Spanish candidate survived the counterfactual necessity test.

Chapter 07 already knows:

```text
- freeze resolved relationship state;
- do not infer relationship from nationality or broad culture;
- preserve existing verified forms when applicable;
- avoid unsupported relationship claims when language/context permits;
- perform bounded adaptation lookup only when realization remains materially open.
```

But Chapter 07 does not itself know:

```text
- legitimate tú + voseante configurations exist;
- vos does not imply replacement of te / tu / tuyo;
- voseo morphology differs materially across varieties;
- ustedes may be familiar plural;
- Spain does not imply vosotros in every variety;
- apparent mixed treatment can be legitimate local structure rather than model drift.
```

Therefore the candidate contributes target-language knowledge that can change the realization decision without creating a new decision owner.

## 13. Route and controller impact

No new route is justified.

The existing route remains:

```text
adapt-localization.relationship-realization
→ adaptations/localization.md
→ Relationship realization
```

A future implementation should attempt the smallest change:

```text
append ES-LANG-ADDR-01 under the existing relationship-realization section
+
add a scoped Spanish runtime evidence ledger if current repository convention requires it
+
add targeted Spanish adversarial evals
```

Do not modify `SKILL.md`, `routing-index.json`, the controller, or Chapter 07 unless independent review demonstrates a concrete discovery or representation failure that cannot be repaired locally.

## 14. Rejected hypotheses

### Rejected: Spanish can use a country lookup table

Counterexamples inside Spain, Colombia, Chile, and broader voseo systems make country too coarse for reliable treatment realization [ESLA01][ESLA03][ESLA04][ESLA05].

### Rejected: `tú / vos / usted` map to one formal-informal scale

Their values and distributions differ by variety and interaction [ESLA01][ESLA04].

### Rejected: `vos` means replace the full `tú` paradigm

American voseo commonly preserves `te` and `tu / tuyo`; verbal and pronominal voseo need not coincide [ESLA01].

### Rejected: mixed treatment is automatically inconsistent

Chilean evidence documents legitimate mixed pronominal/verbal systems [ESLA03].

### Rejected: `ustedes` means formal plural

Much of the Spanish-speaking world uses `ustedes` irrespective of the familiar/formal plural distinction; Canarias is a direct Spain-side counterexample [ESLA05].

### Rejected: marketing should mirror everyday local speech

Advertising evidence from El Salvador demonstrates that the two can diverge [ESLA06].

### Rejected: one address form should be enforced across an organization

First-party style guides show that organizations may deliberately resolve treatment differently by channel or surface [ESLA07][ESLA08].

### Rejected: unknown variety means use "neutral Spanish"

No evidence in this track establishes one relationship-neutral pan-Hispanic treatment system. Address-neutral wording is only a local option where the surface naturally permits it.

### Rejected: artifact class can decide whether the unit loads

Treatment-sensitive and treatment-neutral realizations occur across multiple artifact classes. Activation must remain decision-first.

## 15. Frozen adversarial cases

A future implementation and review should preserve at least the following cases.

### ES1 — Chilean mixed treatment

```text
TARGET: Chilean Spanish
RELATIONSHIP: familiar
SUPPLIED / APPROVED COPY:
"Si tú querís mejorar tu cuenta..."

FAILURE:
normalize `querís` → `quieres` merely because `tú` is present.

EXPECTED:
recognize that a mixed tú + voseante configuration can be legitimate;
require stronger scoped evidence before normalization.
```

### ES2 — Rioplatense voseo repair

```text
TARGET: Rioplatense Spanish
APPROVED ADDRESS: vos
DRAFT:
"Descubre cómo mejorar tu negocio. Haz clic. Vos podés empezar hoy."

FAILURE:
replace only the subject pronoun or rewrite unaffected `tu` as if voseo required a wholly separate possessive paradigm.

EXPECTED:
repair treatment-sensitive imperative/verb forms when needed;
preserve unaffected `tu` / `te` forms when supported by the applicable system.
```

### ES3 — Canary familiar plural

```text
TARGET: Canary Spanish
AUDIENCE: familiar plural
CURRENT FORM: ustedes

FAILURE:
convert `ustedes` → `vosotros` because country = Spain.

EXPECTED:
preserve or resolve according to scoped Canarian / organizational evidence.
```

### ES4 — approved organization policy

```text
TARGET LANGUAGE: Spanish
BROAD MARKET EVIDENCE: mixed
ORGANIZATION STYLE GUIDE: explicitly uses usted on this surface

FAILURE:
reopen the choice because local speech research shows widespread tú or vos.

EXPECTED:
preserve first-party policy for the dimensions and surface it actually resolves.
```

### ES5 — everyday speech vs advertising

```text
MARKET: El Salvador
TASK: advertising copy
OBSERVATION: familiar everyday speech may be voseante

FAILURE:
infer `vos` as mandatory marketing realization from local conversational norm.

EXPECTED:
treat conversational usage as relevant context, not brand policy;
use scoped marketing / first-party evidence to resolve the artifact.
```

### ES6 — address-neutral UI

```text
TARGET LANGUAGE: Spanish
SURFACE: button label
LABEL: "Crear"

FAILURE:
load the Spanish address unit merely because the language is Spanish.

EXPECTED:
no adaptation detour when no material second-person realization exists.
```

### ES7 — referent ambiguity

```text
AUDIENCE: customer team addressed as ustedes
CONTEXT ALSO CONTAINS: third-party implementation team
DRAFT CONTAINS: pueden / sus

FAILURE:
allow material YOU-ALL / THEY ambiguity that changes the message;
or import vosotros/vuestro solely to disambiguate.

EXPECTED:
clarify the referent with a natural formulation supported by the target variety / voice.
```

### ES8 — intentional stance shift

```text
DIALOGUE / CAMPAIGN COPY:
contains a supported tú → usted shift for a material stance change

FAILURE:
normalize all treatment forms for superficial consistency.

EXPECTED:
preserve an evidenced interactional shift; do not treat consistency as the owner.
```

## 16. Evidence / inference boundaries

The companion evidence ledger must preserve:

```text
LINGUISTIC DISTRIBUTION
!= AUDIENCE PREFERENCE

AUDIENCE PREFERENCE
!= MARKETING EFFECT

ATTESTED LOCAL USE
!= REQUIRED BRAND USE

COUNTRY
!= TARGET VARIETY

PRONOUN
!= COMPLETE TREATMENT SYSTEM

MIXED FORM
!= ERROR

OFFICIAL LANGUAGE GUIDANCE
!= UNIVERSAL BRAND POLICY

FIRST-PARTY BRAND POLICY
!= POPULATION-WIDE LANGUAGE RULE
```

The runtime candidate is a project synthesis over multiple evidence classes. No single source establishes the complete `ES-LANG-ADDR-01` contract.

## 17. Current freeze adjudication

```text
Spanish-specific treatment-system gap                    SURVIVES
Need for one bounded address-system unit                 SURVIVES
Need for Spain / LatAm locale packs                      REJECTED
Need for country → form lookup                           REJECTED
Need for universal formal/informal scale                 REJECTED
Need to normalize all mixed forms                        REJECTED
Need for full grammar handbook                           REJECTED
Need for artifact-type activation                        REJECTED
Need for "neutral Spanish" fallback                     REJECTED
Need for second Spanish runtime mechanism                NOT ESTABLISHED
Need for new owner / route / controller machinery        REJECTED
Need for independent adversarial review before promotion SURVIVES
```

The next artifact records the source-level evidence, scope, and `does not establish` boundaries used by this freeze.