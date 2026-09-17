# Spanish Local Adaptation — Independent Adversarial Review Result

Status: **POST-FREEZE INDEPENDENT REVIEW RECORDED**  
Review date: 2026-09-17  
Frozen candidate reviewed: `c5ac8e7cd5408600789e2da01472449ff9dd62f6`  
Review contract: `03-independent-review-brief.md`

## Verdict

```text
PASS_WITH_BOUNDED_REPAIR
```

The frozen candidate sustains one Spanish-specific local-adaptation mechanism and the existing thin local-adaptation architecture.

```text
ES-LANG-ADDR-01
→ PROMOTE AFTER ONE BOUNDED EVIDENCE-SCOPE REPAIR

EXISTING OWNER
→ PASS

EXISTING ROUTE
→ PASS

NEW SHARED PRIMITIVE
→ REJECT

NEW ROUTE / COUNTRY PACK / VARIETY RESOLVER
→ REJECT
```

This review adjudicates the frozen target only. It does not treat `03-independent-review-brief.md` or any later commit as evidence that a frozen defect was already solved, and it does not retroactively modify the reviewed candidate.

---

# A. PROMOTION VERDICT

## ES-LANG-ADDR-01 — PROMOTE AFTER BOUNDED REPAIR

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

The material Spanish-specific mechanism is not merely the existence of `tú / vos / usted / vosotros / ustedes`. It is the fact that, in scoped Spanish varieties, these dimensions can be coupled without being identical:

```text
TONIC ADDRESS FORM
!= VERBAL TREATMENT PATTERN
!= OTHER TREATMENT-SENSITIVE FORMS
```

The strongest promotion-bearing deltas are:

- American voseo does not imply replacing `te / tu / tuyo` with a wholly separate paradigm;
- pronominal and verbal voseo can occur independently;
- Chilean Spanish can legitimately realize `tú +` voseante verbal morphology;
- voseo morphology is not uniform across varieties;
- familiar plural `ustedes` exists, including inside Spain, so `Spain → vosotros` and `ustedes → formal plural` are invalid lookup rules.

Generic Chapter 07 can preserve relationship state, approved wording, evidence scope, and uncertainty, but it does not itself encode those Spanish-specific realization facts. Removing the Spanish-specific knowledge therefore changes the reliability of the realization decision in the discriminating cases.

The candidate does **not** need to be split. Singular/pronominal voseo, verbal treatment, plural treatment, and selective repair remain one bounded second-person realization family under the same owner. First-party policy and address-neutral surfaces are composition / negative-activation boundaries, not separate Spanish mechanisms.

The one repair required before promotion is an evidence-scope correction in the frozen referent-ambiguity discussion. It does not alter the core mechanism.

---

# B. SOURCE ADJUDICATION

## ESLA01 — PASS

RAE / ASALE `voseo` carries the primary linguistic burden for the candidate. It supports:

- pronominal, verbal, and combined voseo;
- ordinary American `vos + te + tu / tuyo` realization;
- independent pronominal-only and verbal-only patterns;
- regionally variable verbal paradigms;
- Rioplatense imperative forms that demonstrate why pronoun-only substitution is insufficient.

The frozen `does not support` boundaries correctly prevent conversion, brand-preference, country-lookup, and universal prestige claims.

## ESLA02 — PASS

RAE / ASALE `vos` supports `vos` as an established second-person singular treatment form and supports the narrower claim that treatment values are not one pan-Hispanic scalar. The frozen ledger correctly avoids converting Argentina / Paraguay examples into a universal brand rule.

## ESLA03 — PASS

The Chilean research supports the discriminating mechanism needed here: documented `tú +` voseante verbal morphology and `vos +` tuteante verbal morphology occur in descriptions of the Chilean treatment system. The frozen ledger properly limits this to attested configurations and does not infer that every Chilean speaker or brand should use them.

## ESLA04 — PASS

The Bogotá study supports rejection of a universal `tú = close/informal`, `usted = distant/formal` mapping in the studied population and supports context-sensitive social / affective treatment meanings. The frozen scope correctly avoids a Colombia-wide prevalence or marketing prescription.

## ESLA05 — PASS

Academia Canaria guidance directly supports the Spain-side counterexample needed by the architecture: widespread Canarian `ustedes` for both familiar / peer and respectful plural use, with `vosotros` retained in some areas. It supports `Spain != vosotros by default` and `ustedes != formal plural by definition`; it does not authorize geography-only selection for a brand.

## ESLA06 — PASS

The 2025 Salvadoran advertising study supports a bounded marketing-context claim: the studied advertising treatment distribution can diverge from familiar spontaneous-speech usage. The ledger explicitly rejects both impermissible upgrades:

```text
observed advertising distribution
!= universal Salvadoran brand rule
!= conversion effect
```

## ESLA07 — PASS

Head Start is valid first-party organization / channel evidence for the artifact dimensions it controls. It supports the composition rule that an organization may resolve Spanish treatment differently by surface. It does not support a US-Spanish population preference.

## ESLA08 — PASS

Mozilla `es-CL` / `es-ES` style guidance is valid first-party localization-policy evidence for the bounded purpose claimed: one organization can resolve treatment differently by locale / surface. Any future runtime use must still pass freshness and actual-scope checks; the frozen ledger does not claim Mozilla policy is a current population truth or a cross-organization rule.

## ESLA09 — PASS

The Microsoft Spanish UI guidance supports the existence of natural address-neutral action labels such as infinitival button labels. The frozen ledger correctly limits this to a surface-local option and does not promote an infinitive CTA rule for general marketing copy.

## ESLA10 — PASS

FundéuRAE supports infinitive forms with imperative value in bounded constructions such as instructions for the public in general. The frozen ledger correctly rejects a universal neutral-Spanish fallback.

## ESLA11 — PASS

RAE grammatical material supports the claim actually stated in the ledger: `usted / ustedes` are second-person discourse forms whose verbal agreement uses morphology shared with third-person singular / plural forms, so verbal morphology alone can fail to distinguish addressee from third-party reference in an underdetermined context.

ESLA11 does **not** independently support a possessive-ambiguity claim about `su / sus`. The ledger itself correctly says that stronger evidence may be needed for treatment-sensitive possessive/reference ambiguity if a specific repair is promoted. The defect is therefore in the frozen design's use of ESLA11 beyond its recorded support, not in ESLA11 as adjudicated.

### Source verdict summary

```text
ESLA01  PASS
ESLA02  PASS
ESLA03  PASS
ESLA04  PASS
ESLA05  PASS
ESLA06  PASS
ESLA07  PASS
ESLA08  PASS
ESLA09  PASS
ESLA10  PASS
ESLA11  PASS
```

No source record needs to be rejected or reclassified. One frozen design claim needs to be narrowed back to the support the ledger actually records.

---

# C. MATERIAL FINDINGS

## ES-IR-01 — MEDIUM — possessive ambiguity is asserted beyond the frozen evidence record

**Frozen location**

`research/local-adaptation-spanish/01-design-freeze.md`, §8 `Referential ambiguity is a repair condition, not a new owner`.

The frozen text states:

```text
`usted / ustedes` use third-person verbal morphology,
and possessives such as `su / sus` can be referentially ambiguous in context.
```

It then lets the Spanish unit detect a `YOU ALL vs THEY` loss when those forms collapse, while the source map points the referent-collision basis to ESLA11.

**Problem**

ESLA11 directly supports the shared **verbal agreement morphology** of `usted / ustedes` with third-person forms. It does not, as recorded, establish the separate possessive `su / sus` ambiguity claim. The evidence ledger explicitly lists stronger possessive/reference evidence as missing or deferred if a specific repair is to be prescribed.

The factual proposition may be linguistically true, but independent review cannot promote it merely from reviewer knowledge. Under the repository's source-fidelity method, the frozen claim is broader than its recorded evidence.

This is material because S13 explicitly pressures `pueden / sus`, and the candidate must not let a generic referent-fidelity requirement silently become an unsupported Spanish-specific possessive mechanism.

**Smallest repair**

Narrow §8 to the supported verbal-morphology collision:

```text
usted / ustedes verbal agreement
shares third-person morphology
→ material addressee / third-party ambiguity may require local clarification
```

Then explicitly state that other referent ambiguity, including `su / sus`, remains ordinary source-referent fidelity / Spanish competence unless separately evidenced; do not prescribe a Spanish-specific possessive repair from the current ledger.

Do **not** add a new owner, new ambiguity resolver, new route, or new source merely to preserve the broader wording. Narrowing the unsupported claim is the least powerful repair.

No other material finding survives review.

---

# D. ARCHITECTURE VERDICT

```text
existing route sufficient?      YES
new owner required?             NO
new route required?             NO
shared primitive required?      NO
controller change required?     NO
routing-index change required?  NO
get-knowledge change required?  NO
Chapter 07 change required?     NO
```

The existing route is materially discoverable and addressable:

```text
adapt-localization.relationship-realization
→ adaptations/localization.md
→ ## Relationship realization
```

Chapter 07 already exposes the bounded JIT edge for materially open target-language relationship realization and already prevents noun-triggered activation. The adaptation contract already expresses section-local language / variety / channel / organization scope, resolved-state preservation, evidence conflict, and uncertainty without a country-first resolver or precedence engine.

Spanish variety complexity does not establish a discovery, addressability, or composition failure. A single route may validly contain separately scoped Vietnamese, Japanese, and future Spanish contributions because the route is owner / decision aligned rather than country aligned.

First-party policy conflicts also do not require a precedence primitive. Current architecture already compares actual scope, provenance, evidence quality, authoritative organization state, and the decision dimension at issue; unresolved conflicts may remain unresolved.

---

# E. FROZEN ADVERSARIAL CASE RESULTS

## S1 — generic tuteo, no local pressure — PASS

A stable approved `tú` system with no material variety conflict is resolved state. The candidate's `DO NOT USE WHEN` prevents reopening it merely because Spanish knowledge exists.

## S2 — Rioplatense voseo repair — PASS

Given approved `vos`, the candidate can repair treatment-sensitive forms such as tuteante imperatives while preserving unaffected `tu / te` where the applicable Rioplatense system supports them. Pronoun-only replacement is explicitly rejected.

For the supplied draft, the relevant pressure is selective repair of forms such as `Descubre` / `Haz` toward the supported voseante imperative system while not rewriting `tu negocio` merely because `vos` is present.

## S3 — Chilean mixed verbal voseo — PASS

`Si tú querís...` cannot be normalized to `Si tú quieres...` merely from the presence of `tú`. ESLA03 supplies enough scoped evidence to require stronger task / organization / variety evidence before treating the mix as drift.

## S4 — mixed form is actually accidental — PASS

Adversarial construction:

```text
RESOLVED STATE:
- one stable tuteante system
- no stance shift
- no variety evidence supporting mixed treatment

DRAFT:
"Tú puedes empezar hoy. Usted haz clic y vos puede continuar."
```

`MIXED FORM != AUTOMATIC ERROR` does not mean `MIXED FORM = ALWAYS PRESERVE`. With resolved state and no evidence supporting the shifts, the candidate permits repair of treatment-sensitive forms that are inconsistent with the resolved system.

## S5 — Canary familiar plural — PASS

Canary familiar-plural `ustedes` must not be converted to `vosotros` merely because the geography is Spain. ESLA05 directly defeats that lookup.

## S6 — central / northern Spain familiar plural with approved `vosotros` — PASS

The Canarian counterexample is section-local evidence, not authority to erase a separately supported central / northern peninsular `vosotros` system. Approved `vosotros` remains resolved within its scope.

## S7 — Latin America as an underspecified label — PASS

`Latin America` plus a materially open treatment choice is insufficient to invent a pan-regional `tú / vos / usted` policy. Preserve uncertainty or obtain the missing scoped state when unavoidable. Address-neutral realization is allowed only when the surface naturally permits it without losing material relationship meaning.

## S8 — El Salvador everyday speech vs advertising — PASS

Both prohibited inferences are rejected:

```text
familiar everyday voseo
→ ads must use vos                 INVALID

study favors tú in sampled ads
→ all Salvadoran ads should use tú INVALID
```

ESLA06 is useful because it proves the two evidence classes cannot be mechanically collapsed, not because it supplies a country prescription.

## S9 — organization / channel policy — PASS

An applicable Head Start- or Mozilla-style first-party rule resolves the controlled wording dimension for the applicable artifact / surface. Broader sociolinguistic evidence must not reopen it merely because other forms exist locally. The same first-party policy must not be generalized into a population preference.

## S10 — first-party state conflicts with language-system possibility — PASS

Adversarial construction:

```text
TARGET: Rioplatense Spanish
ORGANIZATION POLICY:
- address users with vos
- fixed example requires "vos puede continuar"
```

An organization may choose a treatment policy; it cannot make an incompatible morphology valid by authority alone. The candidate separates approved treatment choice from treatment-sensitive grammatical realization. If wording itself is explicitly fixed, the generic controller's fixed-wording / truthfulness boundary requires surfacing the conflict rather than silently inventing a repair policy. No new resolver is needed.

## S11 — address-neutral UI — PASS

`Crear` as a button label contains no material open second-person realization. Spanish language alone must not trigger the adaptation route.

## S12 — direct CTA where treatment is unavoidable — PASS

Adversarial construction:

```text
"Cuéntanos qué necesitas y te mostramos el siguiente paso."
```

If the communication job requires direct conversational address and the treatment system is materially unresolved, rewriting everything into infinitives / impersonal constructions merely to avoid the dependency can change the interaction job. The candidate correctly retains the unresolved dependency rather than universalizing neutral wording.

## S13 — `ustedes` / third-person referent collision — PASS WITH BOUNDED EVIDENCE REPAIR

Adversarial context:

```text
customer team       = YOU ALL
implementation team = THEY
surface forms        = pueden / sus
```

Behavioral requirement survives: preserve source referent distinctions, clarify locally when ambiguity is material, and do not import `vosotros / vuestro` solely to disambiguate.

The verbal collision (`pueden`) is supported by ESLA11. The frozen Spanish-specific support for possessive `sus` is not established by ESLA11 and must be narrowed as ES-IR-01 specifies. `sus` can still be handled under generic referent fidelity / ordinary Spanish competence; it simply cannot be promoted from this ledger as an independently evidenced Spanish adaptation mechanism.

## S14 — intentional stance shift — PASS

Adversarial construction:

```text
speaker begins with established familiar tú
interaction changes to a supported distancing / formal stance
source or interaction state explicitly supports usted
```

The shift is evidence, not inconsistency. The candidate preserves supported interactional change instead of normalizing for surface consistency.

## S15 — Spanish outside a Spanish-speaking country — PASS

Spanish-language communication in a non-Spanish-speaking market can require the unit when second-person realization is materially open. Activation follows the language / realization decision, not a Spanish-speaking-country pack.

## S16 — country name with no second-person decision — PASS

A task localizing facts for Argentina with no second-person treatment choice does not load `ES-LANG-ADDR-01`. `Argentina` and `Spanish` are not activation authority.

### S1–S16 summary

```text
S1   PASS
S2   PASS
S3   PASS
S4   PASS
S5   PASS
S6   PASS
S7   PASS
S8   PASS
S9   PASS
S10  PASS
S11  PASS
S12  PASS
S13  PASS WITH BOUNDED EVIDENCE REPAIR
S14  PASS
S15  PASS
S16  PASS
```

---

# Boundary attack — treatment system vs ordinary grammar

The candidate survives the ordinary-grammar boundary. These errors are **not** `ES-LANG-ADDR-01` problems merely because they occur in Spanish or near second-person wording:

1. `Tú compraste el información.` — noun/article gender agreement (`la información`) is ordinary grammar, not treatment-system realization.
2. `Vos podés empezar, mañana.` — an unjustified punctuation/comma error is ordinary writing correctness, not voseo realization.
3. `Usted no sabe porqué ocurrió.` where interrogative / explanatory syntax requires another `por qué / porque` form — orthographic / syntactic selection is ordinary Spanish correctness, not second-person treatment.
4. A poor lexical choice or false friend in `Tú puedes ...` remains lexical localization unless the replacement changes the treatment system itself.

Scope remains:

```text
TREATMENT-SENSITIVE REALIZATION
→ ES-LANG-ADDR-01

GENERAL SPANISH CORRECTNESS
→ ordinary language competence / existing owner
```

---

# Variety-scope attack

The candidate survives country-to-variety pressure:

```text
Spain
→ does not erase Canarias

Canarias
→ does not erase supported central / northern vosotros

Chile
→ mixed systems are possible, not mandatory

Argentina / Río de la Plata
→ scoped voseo evidence can constrain realization,
  but Argentina as a country noun is not sufficient by itself

Colombia
→ Bogotá city-level evidence cannot become a Colombia-wide rule

Central America / El Salvador
→ advertising evidence cannot become a regional treatment default
```

The correct failure mode for underspecified variety is explicit uncertainty or bounded state retrieval, not a country-derived pseudo-dialect resolver.

---

# First-party-state attack

Both failure directions are controlled:

```text
A. adaptation overrides approved state too eagerly
→ REJECTED

B. first-party policy becomes population truth
→ REJECTED
```

The valid relation is:

```text
FIRST-PARTY POLICY
= authoritative for controlled artifact dimensions within scope

FIRST-PARTY POLICY
!= population prevalence
!= grammatical license for otherwise unsupported morphology
```

---

# Address-neutrality attack

Both failure directions are controlled:

```text
neutral button / notice
→ do not demand unnecessary relationship state

direct relationship-bearing marketing/support copy
→ do not distort the job merely to avoid choosing a treatment system
```

Address-neutrality is therefore a bounded no-op / realization option, not a Spanish fallback regime.

---

# Counterfactual necessity adjudication

Remove `ES-LANG-ADDR-01` while retaining Chapter 07, task evidence, organization policy, and ordinary Spanish generation:

| Candidate material | Correct answer reliably remains without Spanish unit? | Promotion consequence |
|---|---|---|
| `vos + te / tu / tuyo` preservation | No | promotion-bearing |
| verbal-only voseo | No | promotion-bearing |
| Chilean `tú +` voseante morphology | No | promotion-bearing |
| Canary familiar-plural `ustedes` | No | promotion-bearing |
| current first-party treatment policy | Yes, generically | composition boundary only |
| address-neutral UI such as `Crear` | Yes, generically | negative-activation boundary only |

This is the decisive reason the candidate is valid but bounded: the Spanish-specific morphological / treatment-system knowledge changes decisions; generic authority preservation and neutral-surface handling do not independently justify the unit.

---

# F. RESIDUAL UNCERTAINTY

The following remain unknown without blocking promotion after ES-IR-01 is repaired:

- prevalence of particular treatment configurations within heterogeneous Spanish-speaking populations;
- current brand / audience preference for `tú`, `vos`, `usted`, `vosotros`, or `ustedes` outside an actually supplied first-party or scoped evidence context;
- causal marketing or conversion effects of treatment choices;
- exhaustive Andalusian plural-treatment variation;
- exhaustive current discourse conditions for intentional within-interaction treatment switching;
- treatment-sensitive possessive ambiguity as a separately evidenced Spanish adaptation mechanism;
- LLM-specific error rates for these treatment systems.

Those unknowns are not permission to generalize. They become new research dependencies only when a concrete task requires them.

---

# Final disposition

```text
TOP-LEVEL VERDICT
→ PASS_WITH_BOUNDED_REPAIR

ES-LANG-ADDR-01
→ PROMOTE AFTER ES-IR-01

SPLIT UNIT
→ NO

NEW OWNER
→ NO

NEW ROUTE
→ NO

NEW SHARED PRIMITIVE / RESOLVER
→ NO

PROMOTE TO adaptations/localization.md NOW
→ NO — review closes first; bounded repair is a separate subsequent step
```
