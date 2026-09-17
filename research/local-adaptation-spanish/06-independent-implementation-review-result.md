# Spanish Local Adaptation — Independent Implementation Review Result

Status: **POST-FREEZE INDEPENDENT IMPLEMENTATION REVIEW RECORDED**  
Review date: 2026-09-17  
Frozen research target: `c5ac8e7cd5408600789e2da01472449ff9dd62f6`  
Independent research review: `ba041b6b96118e8f5e665fd39659934b52d55677`  
Post-review research repair: `eff18d2e3e27114768d77c0ecb9470debeced406`  
Frozen runtime implementation target: `83e5947f665ef9650d17107c45abaef1d92764dd`

This review adjudicates the runtime implementation at exactly `83e5947f665ef9650d17107c45abaef1d92764dd`.

Later commits are not retroactive evidence that a defect in that target was already fixed.

## Verdict

```text
PASS_WITH_BOUNDED_REPAIR
```

The Spanish runtime semantics, evidence boundaries, route composition, and targeted eval specification survive implementation review. One bounded lifecycle-state defect prevents an unqualified `PASS`: the frozen runtime contribution is marked `reviewed` before this independent implementation review occurred.

```text
ES-LANG-ADDR-01 SEMANTICS     → PASS
ES-IR-01 BOUNDED REPAIR       → PASS
RUNTIME EVIDENCE LEDGER       → PASS
S1–S16 STATIC ORACLE          → PASS
NEGATIVE CONTROLS             → PASS
VN / JP REGRESSION            → PASS
EXISTING ROUTE                → PASS
ARCHITECTURE                   → RETAIN
LIFECYCLE STATE AT TARGET      → BOUNDED REPAIR REQUIRED
```

---

# A. IMPLEMENTATION FIDELITY

## ES-LANG-ADDR-01 — PASS

The runtime implementation is faithful to the promotion-bearing mechanism accepted by the frozen research review:

```text
TONIC ADDRESS FORM
!= VERBAL TREATMENT PATTERN
!= COMPLETE TREATMENT SYSTEM
```

The contribution retains the discriminating Spanish-specific facts without becoming a general Spanish grammar module:

- pronominal and verbal voseo need not coincide;
- `vos` does not imply blind replacement of `te / tu / tuyo`;
- `tú +` voseante verbal morphology may be legitimate in scoped Chilean systems;
- mixed treatment is neither automatically erroneous nor automatically valid;
- plural `ustedes / vosotros` realization remains variety-sensitive;
- `Spain → vosotros`, `ustedes → formal plural`, and `Latin America → one treatment system` remain prohibited lookup rules.

The implementation consumes already-resolved relationship, stance, approved voice, surface state, and scoped variety evidence. It does not promote a Spanish country pack, formality scale, variety resolver, or new decision owner.

The runtime `LOAD WHEN`, `DO NOT USE WHEN`, `MUST PRESERVE`, `MUST NOT INFER`, and realization guardrails are materially aligned with the frozen design plus independent research review.

---

# B. ES-IR-01 — BOUNDED REPAIR FIDELITY

## PASS

The post-review research repair required the runtime implementation to narrow the referent-collision mechanism to the evidence actually carried by ESLA11:

```text
USTED / USTEDES VERBAL AGREEMENT
SHARES THIRD-PERSON MORPHOLOGY
→ MATERIAL ADDRESSEE / THIRD-PARTY AMBIGUITY
  MAY REQUIRE LOCAL CLARIFICATION
```

The runtime implementation does exactly that.

It also states explicitly:

```text
POSSESSIVE OR OTHER REFERENT AMBIGUITY
INCLUDING su / sus
→ GENERIC SOURCE-REFERENT FIDELITY / ORDINARY SPANISH COMPETENCE
→ NOT AN INDEPENDENTLY EVIDENCED ES-LANG-ADDR-01 MECHANISM
```

The runtime evidence ledger repeats the same boundary and ESLA11's `does not establish` section explicitly rejects possessive `su / sus` ambiguity as an independently evidenced Spanish mechanism.

Therefore the frozen overreach is not reintroduced during promotion.

```text
su / sus ambiguity
→ NOT PROMOTED AS SPANISH-SPECIFIC MECHANISM
```

No new ambiguity resolver, reference primitive, route, or evidence source is justified.

---

# C. S1–S16 IMPLEMENTATION ADJUDICATION

This is a static/adversarial implementation review of the runtime contract and eval oracle. It is not a behavioral model benchmark.

## S1 — stable approved tuteo — PASS

Resolved treatment is protected by `DO NOT USE WHEN` and first-party / approved-form preservation. Spanish language alone does not reopen the unit.

## S2 — Rioplatense voseo repair — PASS

The implementation explicitly preserves `te / tu / tuyo` from blind replacement while allowing treatment-sensitive verbal / imperative repair against a supported resolved voseo system.

## S3 — Chilean mixed verbal voseo — PASS

The implementation explicitly rejects `TÚ → necessarily tuteante morphology` and `MIXED FORM → automatic error`; supported `tú +` voseante morphology is preservable.

## S4 — accidental mixed system — PASS

The implementation also states `MIXED FORM != AUTOMATICALLY VALID` and authorizes repair of treatment-sensitive forms inconsistent with the resolved system. Legitimate mixed systems do not become a blanket preservation rule.

## S5 — Canary familiar plural — PASS

The runtime claim and guardrails retain the Canarian counterexample and prohibit `Spain → vosotros` and `ustedes → formal plural` inference.

## S6 — supported peninsular `vosotros` — PASS

Section-local scope plus stronger current regional / organization evidence prevents Canarian evidence from erasing a separately supported `vosotros` system. Resolved approved forms are not reopened.

## S7 — underspecified `Latin America` — PASS

The contribution explicitly forbids `Latin America → one treatment system`; when the socially meaningful choice remains unavoidable and underdetermined, the dependency remains exposed rather than becoming a pan-regional lookup.

## S8 — El Salvador speech vs advertising — PASS

The runtime evidence ledger and contribution preserve:

```text
EVERYDAY SPEECH NORM
!= AUTOMATIC MARKETING REALIZATION
```

Neither everyday voseo nor the scoped advertising distribution becomes a universal Salvadoran brand policy or conversion claim.

## S9 — organization / channel policy — PASS

Applicable first-party organization or channel state freezes the treatment dimension it actually controls; broader sociolinguistic evidence does not reopen it or become a population preference claim.

## S10 — first-party treatment choice with incompatible morphology — PASS

The implementation separates an organization's authority to resolve an address form from treatment-sensitive linguistic coherence. A fixed treatment choice may remain frozen while still-open inconsistent treatment-sensitive forms are checked under existing controller / truthfulness rules.

No policy-precedence engine is required.

## S11 — address-neutral UI — PASS

A natural neutral label such as `Crear` with no material second-person decision satisfies the runtime no-load boundary.

## S12 — direct CTA where treatment matters — PASS

Address-neutral realization is explicitly optional only where natural and meaning-preserving. The unit prohibits making direct copy awkward or impersonal merely to hide an unresolved treatment dependency.

## S13 — `ustedes` / third-person verbal collision — PASS

The implementation loads only for the treatment-sensitive verbal collision supported by ESLA11, preserves addressee / third-party fidelity when material, and prohibits importing another variety's address paradigm merely to disambiguate.

If `su / sus` is ambiguous, the runtime contract assigns that to generic source-referent fidelity / ordinary Spanish competence, not to an independently evidenced Spanish adaptation mechanism.

## S14 — intentional stance shift — PASS

The contribution preserves intended stance and supported interactional shifts; surface consistency is not allowed to erase an evidenced `tú → usted` transition.

## S15 — Spanish outside a Spanish-speaking country — PASS

Applicability follows Spanish-language realization scope rather than membership in Spain, Latin America, or another Spanish-speaking market.

## S16 — country noun with no treatment choice — PASS

Country / language nouns alone are explicitly non-authoritative for activation. No material second-person decision means no Spanish-unit detour.

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
S13  PASS
S14  PASS
S15  PASS
S16  PASS
```

---

# D. NEGATIVE CONTROLS

## PASS

The eval suite correctly distinguishes ordinary Spanish correctness from treatment-system realization.

Examples such as:

```text
Tú compraste el información.
→ noun/article gender agreement

Vos podés comprar tres producto.
→ number agreement

Usted llegó ayer y mañana volverá ayer.
→ temporal / semantic incoherence
```

remain outside `ES-LANG-ADDR-01` merely because second-person wording is nearby.

The runtime contribution reinforces the same boundary:

```text
TREATMENT-SENSITIVE REALIZATION
→ ES-LANG-ADDR-01

GENERAL SPANISH CORRECTNESS
→ ORDINARY LANGUAGE COMPETENCE / OTHER OWNER
```

No spelling, punctuation, general conjugation, lexical, gender-agreement, or broad locale module is introduced.

---

# E. VN / JP REGRESSION REVIEW

## PASS

The implementation delta from the post-review Spanish research repair to the frozen runtime target is confined to:

```text
skills/marketing-practitioner/adaptations/localization.md
skills/marketing-practitioner/references/local-adaptation-spanish-evidence.md
evals/local-adaptation-spanish-v0.md
```

The localization change appends `ES-LANG-ADDR-01` under the existing `## Relationship realization` section; it does not replace or rewrite the existing Vietnamese or Japanese contribution semantics.

Existing units remain independently scope-checked by language and open decision:

```text
VN-LANG-REL-01
JP-LANG-HON-01
JP-LANG-PERM-01
ES-LANG-ADDR-01
```

Spanish evidence does not acquire authority over Vietnamese self/address realization or Japanese honorific / permission-sensitive realization.

No static VN/JP regression survives review.

---

# F. ROUTE / ARCHITECTURE VERDICT

```text
existing route sufficient?      YES
route remains                   adapt-localization.relationship-realization
new owner required?             NO
new route required?             NO
controller change required?     NO
Chapter 07 change required?     NO
routing-index change required?  NO
get-knowledge change required?  NO
shared primitive required?      NO
scope registry required?        NO
precedence engine required?      NO
variety resolver required?       NO
```

The routing manifest continues to bind:

```text
adapt-localization.relationship-realization
→ adaptations/localization.md
→ ## Relationship realization
```

Spanish fits the same owner-aligned family as Vietnamese and Japanese because applicability remains section-local. Complexity of Spanish variation does not demonstrate a concrete discovery, addressability, scope-composition, or conflict-resolution failure that requires larger machinery.

The runtime implementation introduces no justification for reopening `SKILL.md`, Chapter 07, `routing-index.json`, `get-knowledge.py`, the controller, or shared-state primitives.

---

# G. MATERIAL FINDING

## ES-IIR-01 — LOW — frozen implementation claims `reviewed` before implementation review

**Frozen location**

`skills/marketing-practitioner/adaptations/localization.md` → `ES-LANG-ADDR-01` → `REVIEW STATE`.

Frozen runtime target value:

```text
REVIEW STATE
reviewed
```

**Problem**

The repository's extension contract treats review state as contribution-vetting state. Existing implementation-review precedent keeps a newly implemented contribution `provisional / active` at the frozen implementation candidate and promotes it to `reviewed / active` only after independent implementation review passes.

The Spanish contribution had passed independent **research** review and bounded repair, but the runtime implementation at `83e5947...` had not yet undergone this independent implementation review. Therefore `reviewed` is temporally premature at the frozen implementation target.

This does not undermine Spanish semantics, evidence, routing, or S1–S16 behavior. It is a lifecycle/provenance defect, not a theory or architecture defect.

**Smallest repair**

Do not alter Spanish semantics, evidence, evals, route, owner, Chapter 07, controller, routing index, loader, or shared primitives.

Record the lifecycle defect explicitly. After this independent implementation review exists, the contribution may prospectively remain `reviewed / active`; the review result must not be used to claim that the frozen implementation target was already implementation-reviewed before this review occurred.

A separate bounded repair / closure record is sufficient. No runtime semantic patch is required.

---

# H. RESIDUAL UNCERTAINTY

This review establishes static implementation fidelity, not behavioral execution reliability.

It does not establish that every model / host will always:

- classify the open decision correctly;
- traverse Chapter 07;
- retrieve the owner-aligned route;
- choose the correct section-local Spanish applicability;
- produce the expected Spanish output for every S1–S16 prompt.

`evals/local-adaptation-spanish-v0.md` correctly labels itself a targeted architecture / regression specification rather than a behavioral benchmark. No commit status / CI result at the frozen target independently demonstrates behavioral execution.

Those limits do not block the implementation verdict because the task here is independent static/adversarial implementation review.

---

# FINAL DISPOSITION

```text
ES-LANG-ADDR-01
→ IMPLEMENTATION SEMANTICS PASS

ES-IR-01
→ PASS / REMAINS BOUNDED

S1–S16
→ PASS

NEGATIVE CONTROLS
→ PASS

VN / JP REGRESSION
→ PASS

ARCHITECTURE
→ RETAIN

ES-IIR-01 LIFECYCLE STATE
→ BOUNDED REPAIR / CLOSURE RECORD REQUIRED

FINAL VERDICT
→ PASS_WITH_BOUNDED_REPAIR
```
