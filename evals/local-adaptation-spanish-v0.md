# Spanish Relationship Realization — Targeted Pressure Test v0

Status: **targeted architecture/regression suite, not a behavioral benchmark**.

Candidate contribution:

```text
ES-LANG-ADDR-01
```

Intended logical route:

```text
adapt-localization.relationship-realization
```

Independent research-review verdict:

```text
PASS_WITH_BOUNDED_REPAIR
```

Post-review repair:

```text
ES-IR-01 CLOSED BY NARROWING

Spanish-specific referent collision retained only for
usted / ustedes verbal agreement sharing third-person morphology.

su / sus ambiguity remains generic source-referent fidelity /
ordinary Spanish competence under the current evidence set.
```

## Question under test

Can the Spanish local-adaptation implementation improve second-person treatment realization **without** creating Spain/Latin-America packs, a country-to-form lookup table, a universal formality scale, a Spanish grammar handbook, a variety resolver, or a new route/owner?

## Oracle

```text
CURRENT JOB
→ FREEZE RESOLVED IDENTITY / RELATIONSHIP / STANCE /
  APPROVED VOICE / SURFACE STATE
→ IS A SPANISH SECOND-PERSON TREATMENT REALIZATION
  MATERIALLY OPEN?
    ├─ NO  → DO NOT LOAD ES-LANG-ADDR-01
    └─ YES → CHAPTER 07 LOCALIZATION OWNER
             → DISCOVER OWNER-ALIGNED adapt-localization NAMESPACE
             → adapt-localization.relationship-realization
             → section-local scope check
             → apply ES-LANG-ADDR-01 only to still-open dimensions
```

The unit consumes resolved state. It must not re-infer familiarity, hierarchy, target variety, brand voice, or audience preference from a country/language noun.

## Required cases

| Case | Task / resolved state | Expected route behavior | Required semantic behavior |
| --- | --- | --- | --- |
| S1 — stable approved tuteo | Approved Spanish wording consistently uses `tú`; no material variety conflict or open treatment dimension exists. | **NO LOAD / NO REOPEN**. | Preserve resolved treatment. Spanish language alone does not justify re-analysis. |
| S2 — Rioplatense voseo repair | Target variety and approved voice support `vos`; draft contains `Descubre... Haz clic... Vos podés...` and `tu negocio`. | **LOAD ES-LANG-ADDR-01**. | Repair treatment-sensitive tuteante imperative/verb forms where required; do not rewrite `tu` or `te` merely because `vos` is present. |
| S3 — Chilean mixed verbal voseo | Target is Chilean Spanish; approved/local evidence supports familiar `tú +` voseante morphology, e.g. `Si tú querís...`. | **LOAD only if realization remains open/material**. | Do not normalize `querís → quieres` merely because `tú` is present. Mixed pronoun/verbal treatment can be legitimate. |
| S4 — accidental mixed system | Resolved state is one stable tuteante system; draft drifts among `tú`, `usted`, `vos` with incompatible verbs and no supported stance shift or variety evidence. | **LOAD ES-LANG-ADDR-01**. | `MIXED FORM != AUTOMATIC ERROR` does not mean preserve every mix. Repair unsupported treatment drift back to resolved state. |
| S5 — Canary familiar plural | Target variety is Canarian Spanish; familiar plural `ustedes` is supplied/approved. | **LOAD only if plural treatment remains open**. | Do not convert `ustedes → vosotros` merely because country = Spain. |
| S6 — supported peninsular `vosotros` | Target variety / organization policy supports familiar plural `vosotros`. | **NO REOPEN when resolved**. | Canarian evidence is section-local and must not erase separately supported `vosotros`. |
| S7 — underspecified `Latin America` | User asks for Spanish copy for “Latin America”; treatment choice is material and unavoidable; no approved form or narrower variety evidence exists. | **LOAD may identify unresolved dependency; no country-pack lookup**. | Do not invent one pan-regional `tú / vos / usted` policy. Preserve uncertainty or request/consume narrower state only when consequential. |
| S8 — El Salvador speech vs advertising | Familiar local speech evidence includes voseo; task is advertising. | **LOAD only if treatment remains open**. | Do not infer `vos` as mandatory ad realization; do not turn the observed advertising preference for `tú` into a universal Salvadoran rule. |
| S9 — organization/channel policy | Applicable first-party style guide explicitly fixes `usted` or `tú` for this surface. | **NO REOPEN of the resolved dimension**. | Preserve organization policy within its actual scope; do not generalize it into population preference. |
| S10 — organization chooses valid form but supplies incompatible morphology | Organization policy says address users with `vos`, but an example contains unsupported morphology for the applicable variety. | **LOAD if grammar-treatment coherence remains open**. | Organization authority may resolve address choice but cannot make incompatible treatment-sensitive morphology linguistically valid. Surface conflict should be surfaced/repaired within existing controller rules. |
| S11 — address-neutral UI | Spanish button label is `Crear`. | **NO LOAD**. | No material second-person treatment decision exists. |
| S12 — direct CTA where treatment matters | Conversational CTA requires direct second-person realization and no natural address-neutral rewrite preserves the communication job. | **LOAD when the treatment choice is materially open**. | Do not force infinitival/impersonal copy solely to hide an unresolved relationship/variety dependency. |
| S13 — `ustedes` / third-person verbal collision | Customer team = YOU ALL; implementation team = THEY; a shared verbal form such as `pueden` is materially ambiguous in context. | **LOAD only for the treatment-sensitive verbal collision**. | Clarify the referent as needed using a natural form supported for the target variety/voice. Do not import `vosotros` solely to disambiguate. If `su/sus` is also ambiguous, handle that under generic referent fidelity, not as a separately evidenced Spanish mechanism. |
| S14 — intentional stance shift | Source/interaction state explicitly supports a meaningful `tú → usted` shift. | **LOAD only if realization remains open**. | Preserve evidenced stance shift; do not normalize for superficial consistency. |
| S15 — Spanish outside Spanish-speaking market | Spanish-language service copy targets Spanish-speaking users in a non-Spanish-speaking country; treatment choice is open. | **LOAD ES-LANG-ADDR-01 when material**. | Language/realization scope may apply while market != Spain/Latin America. |
| S16 — country noun, no treatment choice | Argentina-localized factual copy contains no second-person treatment decision. | **NO LOAD**. | `Argentina` and `Spanish` are not activation authority. |

## Ordinary-grammar negative controls

These are not `ES-LANG-ADDR-01` problems merely because they occur near second-person wording:

```text
Tú compraste el información.
→ noun/article gender agreement

Vos podés comprar tres producto.
→ number agreement

Usted llegó ayer y mañana volverá ayer.
→ temporal/semantic incoherence
```

Use ordinary Spanish competence / other owners as appropriate. The unit is for treatment-system realization, not general proofreading.

## Adversarial properties covered

```text
S1 / S9 / S16       resolved-state preservation and noun-trigger resistance
S2                  selective voseo repair; vos != full replacement paradigm
S3 / S4             legitimate mixed system != preserve all accidental drift
S5 / S6             Spain != one plural treatment system
S7                  broad region != target variety
S8                  everyday speech != marketing prescription
S10                 organization policy != authority over linguistic compatibility
S11 / S12            bounded address-neutrality
S13                 repaired evidence boundary: verbal collision only
S14                 stance shift != inconsistency
S15                 language != market
```

## Static implementation requirements

The implementation passes structurally only if all remain true:

```text
1. logical route remains adapt-localization.relationship-realization
2. no adapt-spanish / adapt-spain / adapt-latam / es-* route family is added
3. ES-LANG-ADDR-01 lives under the existing Relationship realization section
4. detailed variety/market/channel scope remains inside the contribution
5. Chapter 07 remains the decision owner
6. no controller, routing-index, or get-knowledge change is introduced
7. no global formality scale or country-to-form lookup is introduced
8. pronoun form is not treated as the complete treatment system
9. legitimate mixed pronominal/verbal treatment is not normalized mechanically
10. `vos` does not trigger blind replacement of `te / tu / tuyo`
11. `ustedes` is not treated as formal plural by definition
12. Spain is not treated as `vosotros` by definition
13. first-party organization/surface policy remains resolved state within scope
14. address-neutral realization is optional only where natural and semantics-preserving
15. ESLA11 supports shared verbal morphology only; `su / sus` is not promoted as a separate Spanish-specific mechanism
16. no registry, scope scorer, precedence engine, freshness subsystem, or new loader is introduced
```

## Promotion decision oracle

A later behavioral evaluation should distinguish at least:

```text
F0  correct fast-path / no activation
F1  correct activation + correct owner route
F2  correct route but wrong scoped variety applicability
F3  pronoun-only voseo replacement corrupts treatment-sensitive grammar
F4  legitimate mixed system normalized as an error
F5  accidental mixed system preserved merely because mixed systems can exist
F6  country / broad-region label converted into a treatment lookup
F7  everyday speech evidence converted into brand policy
F8  resolved first-party treatment reopened without authority
F9  address-neutral strategy forced where it changes the communication job
F10 shared third-person verbal morphology loses material addressee/third-party distinction
F11 possessive ambiguity laundered into ES-LANG-ADDR-01 despite the bounded repair
```

This file freezes targeted regression cases and expected architecture semantics. It does not claim these behaviors have been model-benchmarked.