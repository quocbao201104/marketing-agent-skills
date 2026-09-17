# Portuguese Local Adaptation — Design Freeze

Status: **FROZEN FOR INDEPENDENT ADVERSARIAL REVIEW**  
Freeze date: 2026-09-17  
Repository base: `main@da81db89fcb06b8f6b489b8b42f6c700782e68c1`

## 1. Research question

In Portuguese-language marketing communication, are there second-person/addressee realization decisions that remain materially risky after the generic Marketing Practitioner controller has correctly resolved relationship, stance, audience, message, authority, and other upstream state — because the remaining surface choice depends on Portuguese-specific treatment-system composition or explicit-vs-null realization?

The global framework remains the default for every locale. This research does not assume Portuguese requires an adaptation merely because Portuguese varies by country or community.

Promotion gate:

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

Counterfactual:

> Remove Portuguese-specific knowledge while preserving Chapter 07 plus the currently promoted Vietnamese, Japanese, Spanish, and Korean adaptation units. Can the existing runtime still realize Portuguese addressee-sensitive wording reliably without importing unsupported country, pronoun, or paradigm assumptions?

## 2. Existing architecture under pressure

Current owner remains Chapter 07 localization / relationship-indexing realization.

Current logical route remains:

```text
adapt-localization.relationship-realization
```

The current architecture already requires:

```text
CURRENT JOB
→ FREEZE RESOLVED STATE
→ NAME OPEN REALIZATION DECISION
→ USE EXISTING OWNER
→ LOAD ONLY SMALLEST DECISION-RELEVANT LOCAL KNOWLEDGE
```

Portuguese must therefore justify a target-language realization constraint, not a Portugal/Brazil/Africa country pack, variety resolver, pronoun recommender, social hierarchy engine, or full grammar module.

## 3. Freeze verdict

One candidate survives the current promotion gate:

```text
PT-LANG-ADDR-01
Portuguese second-person address-system realization
→ PROMOTE CANDIDATE FOR INDEPENDENT REVIEW
```

Rejected at freeze:

```text
Brazil country pack                         NO
Portugal country pack                       NO
Lusophone-country inheritance tree          NO
Brazil → você lookup                        NO
Portugal → tu lookup                        NO
formal → senhor(a) lookup                   NO
one universal tu/você scale                 NO
full Portuguese pronoun grammar module      NO
seu/sua ambiguity resolver                  NO
variety classifier / resolver               NO
paradigm score                              NO
new route                                   NO
new owner                                   NO
controller change                           NO
Chapter 07 change                           NO
routing-index change                        NO
get-knowledge change                        NO
```

## 4. Candidate mechanism

### 4.1 Mechanism A — address form does not determine one complete grammatical-person paradigm

Portuguese second-person discourse reference can be distributed across subject forms, verbal agreement, clitics, possessives, and prepositional forms in ways that are not mechanically recoverable from the visible subject pronoun alone.

Brazilian Portuguese research documents variation including:

```text
tu + overt 2SG agreement

tu + non-overt / 3SG-shaped agreement

você-subject + te object clitic

te vs você as 2SG direct-object realizations
```

[PTLA04][PTLA05][PTLA06][PTLA07]

Cabinda Portuguese provides a stronger falsification of any pan-Portuguese paradigm lookup: `você` can combine with forms historically associated with the `tu` paradigm, including object clitics, possessives, and to a lesser degree 2SG verbal endings [PTLA08].

Therefore:

```text
ADDRESS FORM
!= COMPLETE PERSON PARADIGM

TU
!= AUTOMATIC 2SG MORPHOLOGY EVERYWHERE

VOCÊ
!= AUTOMATIC 3SG PARADIGM ACROSS ALL FORMS

VOCÊ + TE
!= AUTOMATIC ERROR

VOCÊ + 2SG-SHAPED FORM
!= AUTOMATIC ERROR

MIXED PARADIGM
!= AUTOMATICALLY VALID
```

The last line is essential: attested composition defeats mechanical normalization, but it does not license arbitrary mixture. Applicable variety/community/organization evidence and already-resolved wording state still constrain the artifact.

### 4.2 Mechanism B — explicit vs null addressee realization can itself carry treatment meaning

European Portuguese evidence shows that explicit `você` and third-person-singular realization with no explicit subject are not pragmatically interchangeable merely because both can refer to the addressee while using 3SG verbal morphology.

Corpus and experimental work describes current European Portuguese `você` as socially/pragmatically polyvalent and increasingly marginal in some uses, while null-subject + 3SG has developed as an unmarked or productive treatment strategy in relevant contexts [PTLA02][PTLA03].

Therefore:

```text
EXPLICIT VOCÊ
!= NULL 3SG ADDRESS REALIZATION

SAME 3SG VERBAL MORPHOLOGY
!= SAME TREATMENT REALIZATION

ZERO OVERT PRONOUN
!= ZERO RELATIONSHIP MEANING
```

A transformation such as:

```text
Deseja continuar?
→ Você deseja continuar?
```

is not semantically guaranteed to be relationship-neutral in Portuguese.

### 4.3 Existing owner

The candidate consumes already-resolved:

```text
speaker / publishing identity
recipient relation
standing / authority
interaction history
intended stance
approved voice
target variety/community evidence when actually known
organization / surface policy
source participant/reference distinctions
```

It does not decide who should be addressed as familiar, formal, deferential, senior, customer, peer, or subordinate.

## 5. Bounded decision impact

Candidate decision:

> Given an already-resolved recipient relationship, stance, interaction state, approved voice, and scoped Portuguese variety/community/organization evidence, how should second-person address be realized without falsely treating a subject form as a complete paradigm, mechanically normalizing supported treatment-system composition, or changing treatment value by inserting/removing an explicit addressee form?

The unit may:

```text
- preserve scoped tu/você treatment composition;
- repair only unsupported treatment-system drift;
- preserve supported tu + noncanonical agreement where scoped evidence resolves it;
- preserve supported você + te or analogous composition;
- distinguish explicit você from null-3SG realization where that distinction is material;
- preserve a first-party organization/surface treatment policy;
- leave address-neutral or non-second-person surfaces alone.
```

It may not select a Portuguese variety or relationship from country, nationality, age, customer status, or broad culture alone.

## 6. Scope

Candidate scope:

```text
language: Portuguese (`pt`)
market/geography: not inherently Brazil-, Portugal-, Angola-, Mozambique-, or country-specific
audience/role: interpersonal or audience-facing copy where second-person treatment-system realization is materially open
surface: any, but only when second-person treatment morphology or explicit/null address is material
category: not category-specific
effective period: structural variation is relatively durable; organization policy and sociolinguistic distribution remain scope/time sensitive
```

The unit follows language realization plus scoped evidence. A country label is not a variety decision.

## 7. Must preserve

When applicable, preserve:

```text
speaker / publishing identity
actual recipient relationship
standing / authority
interaction history
intended stance
source addressee vs third-party distinctions
approved organization / surface voice
verified treatment forms already supplied
scoped target-variety/community evidence
accessibility/plain-language constraints
truthfulness and source meaning
```

If one treatment dimension is already resolved, freeze it and constrain only the still-open dimension.

## 8. Must not infer

Do not manufacture:

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
TU = 2SG EVERYWHERE
VOCÊ = 3SG EVERYWHERE
ONE PRONOUN = ONE COMPLETE TREATMENT PARADIGM
```

## 9. First-party state boundary

Brazilian federal service-writing guidance explicitly instructs writers, within the gov.br service-writing scope, to use `você` for the citizen and `nós` for the agency [PTLA10]. This is strong first-party policy evidence for that surface, not a Brazilian population rule.

Current gov.pt service guidance frequently realizes the addressee through 3SG forms without an explicit `você` (`Se tiver dúvidas`, `pode`, `use`) [PTLA11], while the gov.pt `On@18` youth guide deliberately uses a `tu` system (`te`, `vais`, `podes`, `precisares`) [PTLA12].

Thus:

```text
FIRST-PARTY / SURFACE POLICY
→ RESOLVED STATE WITHIN ITS SCOPE

FIRST-PARTY USAGE
!= POPULATION PREFERENCE
!= COUNTRY-WIDE DEFAULT
```

## 10. `seu/sua` boundary

Portuguese possessives can create addressee-versus-third-party ambiguity in some treatment systems. That fact is real, but current research has not shown that a Portuguese-specific possessive resolver is required beyond generic source-referent fidelity and ordinary Portuguese competence.

Therefore:

```text
SEU/SUA AMBIGUITY
→ GENERIC REFERENT-FIDELITY BOUNDARY FOR NOW

PT POSSESSIVE RESOLVER
→ REJECT
```

Do not repeat the Spanish mistake of promoting a nearby ambiguity without a demonstrated local-specific decision delta.

## 11. Negative activation

Do not load `PT-LANG-ADDR-01` merely because the task mentions:

```text
Portuguese
Brazil
Portugal
Angola
Mozambique
customer
business
formal
friendly
social media
public-sector copy
marketing
```

Candidate activation requires:

```text
TARGET LANGUAGE = PORTUGUESE
+
SECOND-PERSON TREATMENT REALIZATION IS MATERIALLY OPEN OR BEING CHANGED
+
THE OPEN CHOICE CAN ALTER TREATMENT-SYSTEM COHERENCE
OR EXPLICIT/NULL ADDRESSEE REALIZATION
```

Do not load when:

- no material second-person/addressee choice exists;
- applicable approved wording fully resolves all relevant treatment dimensions;
- only ordinary Portuguese grammar is open;
- only generic referent ambiguity is open;
- the task is market research, country research, or locale formatting;
- activation would depend only on country/nationality/customer/age/channel nouns.

## 12. P1–P16 adversarial set

### P1 — approved gov.br-style `você`

Applicable organization rule fixes `você` for this surface.

Expected: **NO REOPEN** of the address choice. Portuguese variation elsewhere is not authority to replace it.

### P2 — approved PT `tu` system

Applicable copy already uses `tu/te` plus supported 2SG forms consistently.

Expected: **NO REOPEN** merely because Portuguese also has `você` or null-3SG strategies.

### P3 — scoped Brazilian `tu + non-overt agreement`

Local/community evidence supports wording such as `tu fala / tu vai`.

Expected: **PRESERVE** when the relevant variety/community and voice are actually resolved. Do not normalize mechanically to `tu falas / tu vais`.

### P4 — unsupported `tu` drift

Approved artifact uses canonical `tu` agreement for its scoped variety; one draft line accidentally switches to a different agreement pattern with no evidence.

Expected: attested variation does not immunize drift. **REPAIR TO RESOLVED SYSTEM**.

### P5 — `você` subject + `te` object

Scoped Brazilian evidence/approved voice supports `você ... te`.

Expected: **DO NOT NORMALIZE** solely because subject and clitic derive from different historical paradigms.

### P6 — arbitrary paradigm mix

Draft mixes `tu`, `você`, `te`, `lhe`, incompatible verbal forms, and possessives without scoped support or stance shift.

Expected: `MIXED != AUTOMATIC ERROR` does not mean preserve everything. **REPAIR UNSUPPORTED DRIFT** using resolved state.

### P7 — Cabinda `você + tu-derived forms`

Scoped Cabinda evidence supports the local composition.

Expected: **DO NOT FORCE PAN-PORTUGUESE VOCÊ→3SG-PARADIGM NORMALIZATION**.

### P8 — explicit `você` insertion in PT-PT

Input: `Deseja continuar?` with relationship and style already appropriate.

Transformation proposes `Você deseja continuar?` merely for explicitness.

Expected: **REJECT AUTOMATIC INSERTION**. Explicitness can change treatment value.

### P9 — explicit `você` removal

A scoped organization/community intentionally uses explicit `você`.

Expected: null-3SG evidence elsewhere does not authorize deleting it. **PRESERVE RESOLVED FORM**.

### P10 — null 3SG with no missing-subject repair

PT-PT copy uses natural `Se tiver dúvidas, pode...`.

Expected: **DO NOT ADD VOCÊ** merely because an editor prefers explicit English-like subjects.

### P11 — country-only request

"Translate this for Brazil" / "for Portugal" with no narrower treatment evidence and a material unavoidable address choice.

Expected: candidate may surface the unresolved dependency, but **NO COUNTRY→PRONOUN LOOKUP**.

### P12 — Portuguese outside Lusophone geography

Portuguese-language support copy targets Portuguese speakers in the US, France, Japan, etc.; treatment realization remains open.

Expected: **MAY LOAD**. Language realization is not geography membership.

### P13 — Lusophone market, non-Portuguese output

Task targets Brazil/Portugal but final copy is English or Spanish.

Expected: **NO LOAD**.

### P14 — `seu/sua` referent collision only

Treatment choice is already fixed; only possessive referent remains ambiguous.

Expected: **DO NOT USE PT-LANG-ADDR-01 AS A POSSESSIVE RESOLVER**. Handle via generic referent fidelity.

### P15 — address-neutral / nominal UI

Button or heading contains no material second-person treatment realization.

Expected: **NO LOAD**. Portuguese language alone is not activation authority.

### P16 — first-party surface policies differ within one organization

One organization intentionally uses different treatment realizations across products/surfaces/audiences.

Expected: **PRESERVE EACH POLICY IN ITS ACTUAL SCOPE**. Do not normalize to one brand-wide Portuguese pronoun.

## 13. Counterfactual necessity test

### Case A — `tu` does not determine agreement mechanically

Without Portuguese-specific evidence, a generic editor can interpret `tu fala` as ordinary subject-verb error and normalize it even where scoped local evidence supports the form [PTLA04][PTLA05].

**Candidate changes the decision.**

### Case B — `você` does not determine the rest of the paradigm mechanically

Brazilian evidence supports `você` subject with `te` as 2SG object; Cabinda evidence goes further and documents broader composition with tu-derived forms [PTLA06][PTLA07][PTLA08].

**Candidate changes the decision.**

### Case C — explicitness itself can change treatment value

European Portuguese evidence distinguishes explicit `você` from null-subject + 3SG treatment strategies [PTLA02][PTLA03]. A generic clarity transformation that inserts an explicit subject can therefore alter the relationship conveyed.

**Candidate changes the decision.**

### Case D — possessive ambiguity only

Generic referent fidelity remains sufficient under current evidence.

**Candidate does not own this decision.**

## 14. Novelty relative to existing units

`ES-LANG-ADDR-01` already teaches that pronoun form need not equal a complete Spanish treatment system and that mixed forms are not automatically errors. That architectural lesson is relevant as a hypothesis, but the Spanish unit is scope-bound and cannot serve as evidence for Portuguese.

Portuguese independently demonstrates:

```text
TU / VOCÊ COMPOSITION WITH PORTUGUESE-SPECIFIC
VERBAL / CLITIC REALIZATIONS
```

and, most distinctly:

```text
EXPLICIT VOCÊ
!= NULL-3SG TREATMENT REALIZATION
```

The second mechanism is not currently encoded by the Spanish unit.

`KO-LANG-SPEECH-01` concerns Korean sentence-ending addressee speech level and does not resolve Portuguese person/paradigm composition or null-subject treatment.

## 15. Architecture verdict

Current evidence supports:

```text
existing owner                        YES
existing route                        YES
new owner                             NO
new route                             NO
shared primitive                      NO
country/variety resolver              NO
hierarchy resolver                    NO
paradigm score                        NO
controller change                     NO
Chapter 07 change                     NO
routing-index change                  NO
get-knowledge change                  NO
```

## 16. Freeze decision

```text
PT-LANG-ADDR-01
→ PROMOTE CANDIDATE FOR INDEPENDENT REVIEW
```

Promotion-bearing novelty is limited to:

1. Portuguese-specific composition of second-person discourse reference across subject form, agreement, clitic and related treatment-sensitive morphology; and
2. scoped Portuguese evidence that explicit addressee realization versus null 3SG realization can itself change treatment value.

The candidate is **not** a country lookup, a full pronoun grammar, a Portuguese politeness scale, or a possessive ambiguity resolver.
