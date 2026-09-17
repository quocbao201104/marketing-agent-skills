# Portuguese Local Adaptation — Independent Adversarial Review Result

Status: **POST-FREEZE INDEPENDENT REVIEW RECORDED**  
Review date: 2026-09-17  
Frozen candidate reviewed: `3269d2f4139123fa2a387a8e64611a193bee8c02`  
Review contract: `03-independent-review-brief.md`

## Verdict

```text
PASS_WITH_BOUNDED_REPAIR
```

## Candidate disposition

```text
PROMOTE
```

`PT-LANG-ADDR-01` survives the promotion gate, but one evidence-authority wording defect must be repaired before runtime promotion. The defect does not invalidate either Portuguese-specific mechanism and does not require a split, new route, new owner, resolver, scorer, controller change, or Chapter 07 change.

```text
PT-LANG-ADDR-01
→ PROMOTE AFTER ONE BOUNDED EVIDENCE-AUTHORITY REPAIR

MECHANISM A — ADDRESS FORM != COMPLETE PERSON PARADIGM
→ SURVIVES

MECHANISM B — EXPLICIT VOCÊ != NULL 3SG ADDRESS REALIZATION
→ SURVIVES

FIRST-PARTY CURRENT USAGE
→ MAY BE STRONG SCOPED EVIDENCE
→ MUST NOT BE UPGRADED TO DOCUMENTED POLICY WITHOUT POLICY EVIDENCE
```

This review adjudicates the frozen target only. `03-independent-review-brief.md` was committed in the immediate child commit `fbe4b5099cfcab43b008fe41493cfa7c1fd678f9`; it is used only as the post-freeze review contract and not as evidence that the frozen candidate already satisfied the contract. No later repair or runtime implementation is used as evidence.

---

# A. Promotion-gate adjudication

The gate remains:

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

The Portuguese candidate passes this gate for two related but independently material reasons.

## A1. Treatment-system composition survives the Spanish-overlap attack

The high-level architectural lesson is not unique to Portuguese:

```text
VISIBLE ADDRESS FORM
!= COMPLETE TREATMENT SYSTEM
```

`ES-LANG-ADDR-01` already encodes the analogous Spanish lesson that tonic address form, verbal treatment, clitics/possessives, and other treatment-sensitive forms need not form one mechanically recoverable textbook paradigm. That analogy is therefore **not** Portuguese evidence and cannot by itself justify promotion.

What survives is the Portuguese-specific content needed to prevent concrete Portuguese editing failures:

```text
TU
!= AUTOMATIC OVERT 2SG AGREEMENT IN EVERY SCOPED PORTUGUESE VARIETY

VOCÊ SUBJECT
!= AUTOMATIC REPLACEMENT OF TE

VOCÊ
!= AUTOMATIC COMPLETE 3SG PARADIGM ACROSS ALL FORMS

SCOPED VOCÊ + TU-DERIVED / 2SG-SHAPED FORMS
!= AUTOMATIC CORRUPTION
```

PTLA04 and PTLA05 establish scoped Brazilian `tu` systems with and without overt agreement. PTLA06 and PTLA07 establish Brazilian `você`-subject / `te` coexistence and direct-object competition. PTLA08 supplies the strongest falsification of a pan-Portuguese paradigm lookup: the studied Cabinda system combines `você` with object clitics, possessives, and to a smaller extent verbal endings historically associated with the `tu` paradigm.

A generic editor that knows only Chapter 07 plus the existence of the Spanish unit has no legitimate basis to transfer Spanish facts into Portuguese. Without Portuguese-specific knowledge, it cannot reliably distinguish a supported `tu fala`, supported `você ... te`, or scoped Cabinda composition from accidental agreement/paradigm drift. The Portuguese evidence therefore changes a real realization decision rather than merely repeating that languages vary.

This mechanism is still bounded. It does **not** license arbitrary mixing. The candidate correctly preserves the reverse guardrail:

```text
ATTESTED COMPOSITION
!= BLANKET PRESERVATION OF EVERY MIX
```

## A2. Explicit `você` vs null-3SG is additional Portuguese novelty

This mechanism survives more strongly and is not merely generic pro-drop grammar.

PTLA02 explicitly analyzes null subject + 3SG as an unmarked politeness strategy in current European Portuguese while documenting the declining/polyvalent status of explicit `você`. PTLA03 independently treats explicit `você` in relation to third-person realization without an overt subject and reports pragmatic potential for the null-third-person strategy.

Therefore a transformation such as:

```text
Deseja continuar?
→ Você deseja continuar?
```

cannot be treated as a guaranteed relationship-neutral clarity edit merely because propositional content and 3SG verbal morphology remain compatible.

The promotion-bearing rule is narrowly:

```text
SAME 3SG VERBAL MORPHOLOGY
!= SAME TREATMENT REALIZATION

ZERO OVERT PRONOUN
!= ZERO PRAGMATIC / RELATIONAL VALUE
```

Chapter 07 already owns relationship-sensitive realization, but it does not encode this Portuguese-specific explicit-vs-null consequence. Spanish does not supply it either. This is a genuine Portuguese decision delta.

## A3. What is not Portuguese novelty

The following remain generic architecture / evidence boundaries and must not be counted as the reason for promotion:

```text
preserve resolved organization wording
first-party evidence outranks broad priors only within supported scope
country noun != variety decision
formal != senhor/senhora lookup
mixed != automatically valid
unsupported drift may be repaired
Portuguese language alone != load
address-neutral artifact != load
seu/sua referent ambiguity alone != Portuguese-specific resolver
```

The unit survives because of the Portuguese-specific realization facts in A1 and A2, not because these generic safeguards are restated.

---

# B. Source-by-source evidence adjudication

## PTLA01 — PASS

**Source exists / identifiable:** yes. Published comparative study in *Diadorim* (2018), DOI `10.35520/diadorim.2018.v20n0a23276`.

**Claim representation:** accurate at the frozen scope. The source directly compares European and Brazilian Portuguese treatment systems, describes a more complex European system, and reports that Brazilian `tu` and `você` are not in simple complementary distribution across the country.

**Scope preserved:** yes. The ledger rejects `Portugal → tu`, `Brazil → você`, one country-wide system, and marketing-effect claims.

**Promotion role:** boundary/supporting evidence for rejecting country-level simplification; not sufficient by itself for the runtime mechanism.

## PTLA02 — PASS

**Source exists / identifiable:** yes. Lara & Guilherme (2018), *Studies in Hispanic and Lusophone Linguistics*, DOI `10.1515/SHLL-2018-0012`.

**Claim representation:** accurate. The paper reports polyvalent current European Portuguese `você`, declining/marginalized explicit use across the examined historical corpora, and explicitly concludes that null subject + 3SG has emerged as an unmarked politeness strategy in current European Portuguese.

**Scope preserved:** yes. The ledger does not convert this into a ban on explicit `você`, a Portugal-wide organization rule, or a universal Portuguese null-subject default.

**Promotion role:** primary evidence for Mechanism B.

## PTLA03 — PASS

**Source exists / identifiable:** yes. Roque & Pinto (2023), *Redis*, DOI `10.21747/21833958/red13a8`.

**Claim representation:** accurate and properly qualified. The article describes Portuguese treatment as complex/rapidly varying, focuses on problematic uses of `você`, relates them to third-person realization without an explicit subject, and labels its empirical component as a small exploratory study.

**Scope preserved:** yes. The frozen ledger does not turn the exploratory data into a universal hierarchy or country lookup.

**Promotion role:** corroborating evidence for Mechanism B; PTLA02 carries the stronger promotion burden.

## PTLA04 — PASS

**Source exists / identifiable:** yes. Souza & Chaves (2015), *Working Papers em Linguística*, DOI `10.5007/1984-8420.2015v16n1p170`.

**Claim representation:** accurate. The study explicitly examines variation such as `tu/Ø falas ~ tu/Ø fala` and past-tense variants in Florianópolis. Its evaluation sample is 22 Economics students at UFSC and the frozen ledger does not hide that the result is locally scoped.

**Scope preserved:** yes. It does not justify `tu +` non-overt agreement everywhere, every brand voice, or a Brazil-wide rule.

**Promotion role:** primary evidence that visible `tu` does not mechanically determine overt 2SG verbal agreement in every scoped Portuguese variety/community.

## PTLA05 — PASS

**Source exists / identifiable:** yes. Scherre, Andrade & Catão (2021), *Revista de Letras*, DOI `10.36517/2525-3468.rdl.v1i40.2021.71460`.

**Claim representation:** accurate. The synthesis distinguishes multiple Brazilian second-person subsystems, including `você/cê/ocê`, `tu` without agreement, and `tu` with agreement, using regional research rather than a single national system.

**Scope preserved:** yes. The ledger explicitly rejects region-to-pronoun marketing lookup, static population preference, and one channel-wide subsystem.

**Promotion role:** supports Mechanism A and the no-country-resolver boundary.

## PTLA06 — PASS

**Source exists / identifiable:** yes. Lopes & Cavalcante (2011), *Lingüística* 25, 30–65.

**Claim representation:** accurate. The study uses personal letters from Rio de Janeiro from the late nineteenth century through the first half of the twentieth century and specifically examines expansion of `você` in subject position together with retention of clitic `te`.

**Scope preserved:** yes. The ledger explicitly rejects a universal `você → te` rule, current national frequency claims, and brand preference.

**Promotion role:** primary historical evidence that `você` subject does not mechanically force replacement of `te`.

## PTLA07 — PASS

**Source exists / identifiable:** yes. Schwenter et al. (2018), *Revista Linguíʃtica* 14(2), DOI `10.31513/linguistica.2018.v14n2a17608`.

**Claim representation:** accurate. The experiment directly compares Brazilian Portuguese 2SG direct-object `te` and tonic `você`, finds conditioning by dialectal subject-pronoun preference and discourse contrast, and explicitly discusses mixed-source pronominal combinations as ordinary for many Brazilian speakers.

**Scope preserved:** yes. The ledger does not claim universal `te` preference or export to European/African Portuguese.

**Promotion role:** primary contemporary support for Mechanism A in Brazilian Portuguese.

## PTLA08 — PASS

**Source exists / identifiable:** yes. Gutiérrez Maté (2024), *LaborHistórico* 10(2), DOI `10.24206/lh.v10i2.64315`.

**Claim representation:** accurate and carefully worded. The source describes the studied Cabinda Portuguese system as combining independent/oblique `você` with at least some forms derived from the `tu` paradigm—object clitics, possessives, and to a much smaller extent verb endings—and notes that calling the paradigm “hybrid” is primarily diachronic characterization.

**Scope preserved:** yes. The frozen ledger does not export Cabinda usage to Angola generally or to Brazil/Portugal/Mozambique.

**Promotion role:** strongest falsification of `você → complete 3SG paradigm` as a pan-Portuguese normalization rule.

## PTLA09 — PASS

**Source exists / identifiable:** yes. Pires (2022), *Linguística: Revista de Estudos Linguísticos da Universidade do Porto* 17, 95–116.

**Claim representation:** accurate. The study reports an online questionnaire with 115 participants and identifies multiple pragmatic/discourse values for `você` in the studied Angolan data.

**Scope preserved:** yes. The frozen ledger does not generalize the sample into an Angola-wide scale, a brand rule, or hierarchy resolver.

**Promotion role:** boundary evidence against reducing `você` to one global formality value.

## PTLA10 — PASS

**Source exists / identifiable:** yes. gov.br service-editing guidance.

**Claim representation:** exact and strong within scope. The guide explicitly instructs writers to use `você` for the citizen and `nós` for the agency.

**Scope preserved:** yes. The ledger correctly limits authority to the guide/service-writing context and rejects a Brazilian population or private-sector default.

**Promotion role:** first-party policy boundary/composition evidence; not the Portuguese-specific novelty itself.

## PTLA11 — PASS

**Source exists / identifiable:** yes. gov.pt `Serviços públicos em Portugal`, updated 2026-05-12.

**Claim representation:** accurate as **current first-party usage**. The live surface repeatedly uses reader-directed 3SG/null-subject forms such as `Se tiver dúvidas`, `pode`, `use`, and `escolha` without inserting explicit `você`.

**Scope preserved in the ledger:** yes. The record labels this as current first-party public-service copy and rejects a Portugal-wide rule, causal effect, or population preference.

**Promotion role:** current first-party corroboration that null-3SG reader address is operationally real. It is **not**, by itself, documentary proof of a formal organization-wide treatment policy; that distinction creates PT-IR-01 below.

## PTLA12 — PASS

**Source exists / identifiable:** yes. gov.pt `On@18`, updated 2025-10-09.

**Claim representation:** accurate as **current first-party usage**. The guide uses a clear `tu` system including `te`, `vais`, `podes`, and `precisares`.

**Scope preserved in the ledger:** yes. It rejects `young audience → tu` universally and does not claim all gov.pt surfaces use `tu`.

**Promotion role:** demonstrates scoped first-party coexistence of a `tu` realization with general gov.pt surfaces that use 3SG/null-style address. It does not independently prove that the contrast is governed by a documented intentional cross-surface policy.

### Evidence summary

```text
PTLA01  PASS
PTLA02  PASS
PTLA03  PASS
PTLA04  PASS
PTLA05  PASS
PTLA06  PASS
PTLA07  PASS
PTLA08  PASS
PTLA09  PASS
PTLA10  PASS
PTLA11  PASS
PTLA12  PASS
```

No evidence record needs to be rejected. One frozen design synthesis overstates the authority class of PTLA11/PTLA12; the evidence records themselves are adequately scoped.

---

# C. Material finding

## PT-IR-01

```text
ID: PT-IR-01
SEVERITY: MEDIUM
FROZEN LOCATION:
- 01-design-freeze.md §9 First-party state boundary
- 01-design-freeze.md §12 P16
```

### UNSUPPORTED / OVERBROAD CLAIM

The frozen design moves from evidence of live first-party gov.pt usage to language implying documented policy or deliberate/intentional cross-surface treatment design:

```text
PTLA11 / PTLA12 observed first-party usage
→ "deliberately" uses a realization
→ FIRST-PARTY / SURFACE POLICY
→ P16: organization "intentionally" uses different treatment realizations
```

PTLA10 is explicit policy evidence because the gov.br guide actually instructs writers what forms to use. PTLA11 and PTLA12 are different: they show current first-party copy on two scoped gov.pt surfaces, but the frozen evidence does not independently document a gov.pt policy stating that those differing systems were intentionally assigned by surface/audience.

### WHY MATERIAL

The distinction affects authority and composition.

```text
CURRENT FIRST-PARTY USAGE
!= DOCUMENTED FIRST-PARTY POLICY
```

A current first-party artifact can be strong scoped evidence and, when it is the actual approved wording for the task, can be resolved state. But inferring a formal surface policy from observed usage can incorrectly suppress uncertainty or override other current organization evidence. That would violate the repository's source-fidelity rule even though the underlying wording examples are real.

The defect does **not** undermine:

- the existence of null-3SG reader address on gov.pt;
- the existence of a `tu` system on `On@18`;
- the generic rule that actually supplied organization/surface policy must be preserved;
- either Portuguese-specific promotion-bearing mechanism.

### SMALLEST BOUNDED REPAIR

In a separate post-review repair artifact/commit:

1. Reserve `policy`, `deliberately`, and `intentionally` for an explicit organization rule or task-supplied approved policy.
2. Describe PTLA11/PTLA12 as `current first-party usage` / `current scoped first-party realization`.
3. Keep the valid inference:

```text
ONE ORGANIZATION ECOSYSTEM
CAN EXHIBIT DIFFERENT SCOPED TREATMENT REALIZATIONS
```

without claiming the frozen sources prove a documented cross-surface policy.
4. In P16, preserve each realization when it is actually supplied/approved or otherwise authoritative in its scope; do not infer a global brand policy from page-level observation.
5. Do not add evidence, a precedence engine, organization resolver, or architecture machinery merely to retain the stronger wording.

Reviewer does **not** implement this repair in the review commit.

No other material finding survives review.

---

# D. Counterfactual removal test

Remove all Portuguese-specific knowledge and keep:

```text
Chapter 07
VN-LANG-REL-01
JP-LANG-HON-01
JP-LANG-PERM-01
ES-LANG-ADDR-01
KO-LANG-SPEECH-01
all resolved task / organization / interaction state
```

Then ask whether runtime can still **reliably** handle the required Portuguese cases.

## 1. Scoped `tu +` non-overt agreement — NO

Chapter 07 can preserve supplied approved wording and can avoid broad country assumptions, but it does not know that scoped Portuguese `tu` systems may legitimately use non-overt agreement. Spanish knowledge cannot be transferred by analogy. Without PTLA04/PTLA05-type knowledge, `tu fala / tu vai` remains vulnerable to ordinary agreement normalization.

**Portuguese-specific mechanism that survives:** `tu` does not mechanically select overt 2SG agreement across all scoped Portuguese varieties/communities.

## 2. Scoped `você + te` — NO

Generic controller logic can preserve an explicitly fixed phrase, but it cannot infer from first principles that `você` subject with `te` object is an established Portuguese composition rather than corruption. Spanish `vos + te` is irrelevant as evidence.

**Portuguese-specific mechanism that survives:** `você` subject does not determine a complete textbook paradigm and can coexist with `te` in scoped Brazilian usage.

## 3. Scoped `você + 2SG` combinations — NO

The Cabinda pattern is not recoverable from generic Chapter 07 or Spanish logic. Without Portuguese-specific evidence, a paradigm normalizer can incorrectly force `você` toward a full 3SG-shaped system.

**Portuguese-specific mechanism that survives:** Cabinda-scoped `você` can combine with forms derived from the `tu` paradigm, including clitics/possessives and more limited verbal endings.

## 4. Explicit `você` vs null-3SG treatment realization — NO

A competent grammar engine may know Portuguese permits null subjects, but that is insufficient. The runtime needs the Portuguese pragmatic fact that explicit `você` and null-subject 3SG can carry different treatment values in European Portuguese. Otherwise a clarity edit can insert/delete the pronoun while assuming relationship neutrality.

**Portuguese-specific mechanism that survives:** explicitness itself can be treatment-bearing.

## 5. Accidental mixed-paradigm drift — PARTLY, but not reliably without Portuguese evidence

Chapter 07 already knows how to preserve resolved state and repair unsupported drift; Spanish reinforces the generic lesson that `mixed != automatically wrong` and `mixed != automatically valid`. What is missing is the Portuguese-specific discriminator for which combinations are actually attested/supportable.

Thus the generic architecture can perform the **repair logic**, but not reliably classify Portuguese composition without scoped Portuguese evidence.

**Portuguese-specific mechanism that survives:** evidence-bound distinction between legitimate Portuguese composition and accidental drift.

## 6. First-party surface-specific treatment policy — YES, generically

Chapter 07 already preserves actual current organization/surface policy within scope and prevents broad priors from reopening resolved state. This does not require Portuguese-specific knowledge.

Therefore first-party policy handling is a **composition boundary**, not promotion-bearing novelty.

### Counterfactual verdict

```text
CAN RUNTIME RELIABLY HANDLE ALL REQUIRED PORTUGUESE CASES
AFTER REMOVING ALL PORTUGUESE-SPECIFIC KNOWLEDGE?

NO
```

Exactly two Portuguese-specific mechanism families remain necessary:

```text
1. PORTUGUESE SECOND-PERSON COMPOSITION
   - scoped tu/agreement variation
   - scoped você + te
   - scoped você + tu-derived / 2SG-shaped forms

2. PORTUGUESE EXPLICIT-vs-NULL TREATMENT REALIZATION
   - explicit você != null-subject 3SG pragmatically
```

They may remain in one bounded unit because they constrain the same Chapter 07 second-person realization decision and do not require different owners or routes.

---

# E. Spanish-overlap analysis

The strongest rejection hypothesis was:

```text
PT-LANG-ADDR-01
= ES-LANG-ADDR-01 translated into Portuguese examples
```

That hypothesis fails, but only after separating architecture from evidence.

## What Spanish already teaches

`ES-LANG-ADDR-01` already demonstrates the architecture-level proposition:

```text
PRONOUN / TONIC ADDRESS FORM
!= COMPLETE TREATMENT SYSTEM

MIXED FORM
!= AUTOMATIC ERROR
```

Portuguese cannot claim those abstractions themselves as new architecture.

## What Spanish does not supply

Spanish runtime knowledge does not establish any of the following Portuguese facts:

```text
Florianópolis / Brazilian tu agreement variation
Brazilian você-subject + te retention/competition
Cabinda você + tu-derived forms
European Portuguese explicit você vs null-3SG treatment distinction
```

Using Spanish as evidence for Portuguese would itself violate scope discipline.

## Runtime conclusion

The Portuguese unit is legitimate as a **language-scoped contribution under the same route**, not as a new primitive. Reuse the architecture; do not reuse Spanish evidence.

```text
SHARED ARCHITECTURAL SHAPE
!= DUPLICATE LOCAL KNOWLEDGE
```

A local contribution can be novel at the target-language decision level even when another language previously established the same architectural pattern, provided the new target has independent evidence and the facts materially change its realization decisions. Portuguese satisfies that narrower standard.

---

# F. P1–P16 adversarial adjudication

## P1 — approved gov.br-style `você` — PASS

An actually applicable gov.br service-writing rule explicitly fixes `você`. Portuguese variation elsewhere is not authority to reopen it. PTLA10 is genuine policy evidence within its scope.

## P2 — approved PT `tu` system — PASS

If the current artifact already has an applicable approved `tu/te` + supported 2SG realization, broad Portuguese variation does not reopen the treatment choice. Preserve the resolved dimension.

## P3 — scoped Brazilian `tu +` non-overt agreement — PASS

PTLA04/PTLA05 are sufficient to defeat mechanical textbook normalization when the relevant variety/community and voice are actually resolved. The same evidence does not authorize exporting the form elsewhere.

## P4 — unsupported `tu` drift — PASS

Attested variation is not immunity from inconsistency. If the scoped artifact has a resolved agreement system and one line drifts with no support, Chapter 07 + the candidate can repair back to the resolved system.

## P5 — `você` subject + `te` object — PASS

PTLA06/PTLA07 support the specific claim that `você ... te` is not intrinsically an error in Brazilian Portuguese. Do not normalize solely because the forms have different historical sources.

## P6 — arbitrary paradigm mix — PASS

The candidate explicitly rejects blanket preservation. A draft that mixes `tu`, `você`, `te`, `lhe`, verbal forms, and possessives without scoped evidence or supported stance shift remains repairable as unsupported drift.

## P7 — Cabinda `você +` tu-derived forms — PASS

PTLA08 directly defeats a pan-Portuguese `você → complete 3SG paradigm` normalization. The authority stays Cabinda-scoped; it does not create an Angola lookup.

## P8 — explicit `você` insertion in PT-PT — PASS

PTLA02/PTLA03 make automatic insertion unsafe. `Deseja continuar? → Você deseja continuar?` can change treatment realization even when propositional content remains constant.

## P9 — explicit `você` removal — PASS

Evidence that null-3SG is important in European Portuguese does not authorize deleting an explicitly approved `você` in another scoped organization/community/artifact. Preserve resolved wording unless a stronger conflict requires reopening it.

## P10 — null 3SG with no missing-subject repair — PASS

Natural Portuguese `Se tiver dúvidas, pode...` is not missing a subject merely because English-like explicitness is preferred by an editor. Do not add `você` as a relationship-neutral clarity repair.

## P11 — country-only request — PASS

`for Brazil` or `for Portugal` does not select a pronoun or agreement system. The candidate may expose an unresolved treatment dependency when unavoidable, but it cannot convert geography into a variety/treatment lookup.

## P12 — Portuguese outside Lusophone geography — PASS

The candidate follows target-language realization, not membership in a Lusophone-country set. Portuguese-language support copy in the US, France, Japan, or elsewhere may load when a material second-person realization decision remains open.

## P13 — Lusophone market, non-Portuguese output — PASS

Brazil/Portugal/Angola/Mozambique geography with English or Spanish final output does not activate `PT-LANG-ADDR-01`.

## P14 — `seu/sua` referent collision only — PASS

The frozen design correctly rejects a Portuguese-specific possessive resolver under current evidence. If treatment is fixed and only referent ambiguity remains, handle it through generic referent fidelity / ordinary Portuguese competence.

## P15 — address-neutral / nominal UI — PASS

A Portuguese heading/button with no material second-person treatment realization does not load the unit. Language alone is not activation authority.

## P16 — first-party surface policies differ within one organization — PASS WITH BOUNDED REPAIR

The behavioral boundary is correct:

```text
ONE ORGANIZATION
!= ONE AUTOMATIC PORTUGUESE TREATMENT SYSTEM FOR EVERY SURFACE
```

PTLA11 and PTLA12 demonstrate different current first-party treatment realizations within the gov.pt ecosystem. However, the frozen wording overstates the evidence when it calls those differences deliberate/intentional policy without a documented policy source.

After PT-IR-01, the case remains valid as:

- preserve actual supplied/approved surface policy when one exists;
- preserve current first-party wording within the scope it actually evidences;
- do not infer one brand-wide/country-wide system from either page;
- do not infer a documented policy solely from observed usage.

### P1–P16 summary

```text
P1   PASS
P2   PASS
P3   PASS
P4   PASS
P5   PASS
P6   PASS
P7   PASS
P8   PASS
P9   PASS
P10  PASS
P11  PASS
P12  PASS
P13  PASS
P14  PASS
P15  PASS
P16  PASS_WITH_BOUNDED_REPAIR
```

---

# G. Forbidden-upgrade attack

All required prohibited upgrades are rejected by the frozen candidate and remain rejected after review:

```text
BRAZIL → VOCÊ                       REJECT
PORTUGAL → TU                       REJECT
ANGOLA → ONE SYSTEM                 REJECT
MOZAMBIQUE → FIXED SYSTEM           REJECT

CUSTOMER → VOCÊ                     REJECT
YOUNG → TU                          REJECT
FORMAL → SENHOR/SENHORA             REJECT
FRIENDLY → TU                       REJECT

TU → OVERT 2SG EVERYTHING           REJECT
VOCÊ → COMPLETE 3SG EVERYTHING      REJECT
VOCÊ + TE → ERROR                   REJECT
VOCÊ + 2SG-SHAPED FORM → ERROR      REJECT

NULL SUBJECT → NEUTRAL EVERYWHERE   REJECT
EXPLICIT VOCÊ → WRONG IN PORTUGAL   REJECT

FIRST-PARTY USAGE → POPULATION NORM REJECT
FIRST-PARTY USAGE → POLICY          REJECT UNLESS POLICY IS ACTUALLY EVIDENCED
```

Country/market nouns alone remain insufficient activation authority.

---

# H. Ordinary-grammar negative controls

`PT-LANG-ADDR-01` does not become general Portuguese proofreading.

Outside scope unless the error materially changes treatment realization:

```text
article/noun gender
ordinary number agreement
spelling / accentuation
unrelated tense/aspect
lexical mistranslation
generic third-party referent ambiguity
seu/sua ambiguity by itself
```

A person/agreement form enters the unit only when it is part of the material second-person treatment realization being preserved or changed. This keeps Mechanism A from becoming a full paradigm checker.

---

# I. Architecture verdict

```text
existing owner sufficient?          YES
existing route sufficient?          YES
new owner required?                 NO
new route required?                 NO
shared primitive required?          NO
country/variety resolver?           NO
hierarchy resolver?                 NO
paradigm scorer?                    NO
controller change required?         NO
Chapter 07 change required?         NO
routing-index change required?      NO
get-knowledge change required?      NO
```

The existing architecture is sufficient because Chapter 07 already owns materially relationship-indexing target-language realization and already exposes the bounded JIT lookup edge:

```text
adapt-localization.relationship-realization
→ adaptations/localization.md
→ section-local contribution scope check
```

Portuguese variety complexity does not demonstrate a discovery or addressability failure. The runtime does not need to classify Brazil, Portugal, Angola, Mozambique, Cabinda, or diaspora geography before applying the unit. When scoped variety/community/organization evidence is already known, the unit consumes it; when it is not known, the unit does not invent it.

The existing contribution model also handles composition correctly:

```text
ONE ROUTE
→ MULTIPLE LANGUAGE-SCOPED CONTRIBUTIONS
→ EACH CONTRIBUTION SELF-SCOPES
```

No shared `address paradigm` primitive is required merely because Spanish and Portuguese expose analogous treatment-system composition. A shared primitive would add machinery without solving a demonstrated owner, discovery, addressability, or composition failure.

Likewise, no paradigm scorer is justified. The candidate requires evidence-bound preservation/repair, not numerical selection among Portuguese systems.

---

# J. `seu/sua` adjudication

The frozen candidate is correct to reject `seu/sua` ambiguity as independent Portuguese adaptation novelty under the current ledger.

The factual ambiguity can matter in Portuguese, but the current promotion question is not whether ambiguity exists; it is whether a Portuguese-specific runtime mechanism is needed beyond:

```text
SOURCE REFERENT FIDELITY
+
ORDINARY PORTUGUESE REALIZATION
+
ALREADY-RESOLVED TREATMENT STATE
```

The frozen evidence does not demonstrate that extra mechanism. Therefore:

```text
SEU/SUA AMBIGUITY
→ GENERIC REFERENT-FIDELITY BOUNDARY

PT-SPECIFIC POSSESSIVE RESOLVER
→ REJECT
```

This avoids repeating the Spanish possessive-evidence overreach previously caught by independent review.

---

# K. Final adjudication

The candidate is not merely a country pack, a variety catalog, a pronoun recommender, a formality scale, or a Portuguese copy of Spanish runtime logic.

The surviving Portuguese-specific decision deltas are narrow and concrete:

```text
A. ADDRESS FORM DOES NOT FIX THE COMPLETE PORTUGUESE PERSON/TREATMENT PARADIGM
   - scoped tu does not always require overt 2SG agreement
   - scoped você can coexist with te
   - scoped você can coexist with tu-derived / 2SG-shaped forms
   - attested composition does not license arbitrary mixture

B. EXPLICIT VOCÊ IS NOT PRAGMATICALLY EQUIVALENT TO NULL-SUBJECT 3SG
   - subject insertion/removal can alter treatment realization
   - same verbal morphology does not guarantee same relationship meaning
```

The counterfactual fails without Portuguese-specific knowledge, so rejection is not justified. Splitting is unnecessary because both mechanisms constrain the same already-open second-person realization decision under the same Chapter 07 owner.

One bounded evidence-authority repair is required before runtime promotion: current first-party gov.pt usage must not be mislabeled as documented deliberate surface policy unless such policy evidence is actually supplied.

## Final verdict

```text
PASS_WITH_BOUNDED_REPAIR
```

## Promotion verdict

```text
PROMOTE
```

Reviewer records PT-IR-01 here and does not implement the repair in this review commit.
