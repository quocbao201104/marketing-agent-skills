# Portuguese Local Adaptation v0 — Architecture / Regression Eval

Status: **TARGETED ARCHITECTURE / REGRESSION SUITE — NOT A BEHAVIORAL BENCHMARK**

Research lineage:

- frozen research target: `3269d2f4139123fa2a387a8e64611a193bee8c02`
- independent research review: `ac70453b5d3c7770f5c099f7b63ed34e1a16a70c`
- research verdict: `PASS_WITH_BOUNDED_REPAIR`
- promotion verdict: `PROMOTE`
- bounded repair: `2f3c431a33cd6d80be7f589aa83ff8ff35f67641`
- repair closed: `PT-IR-01`

Target runtime contribution:

```text
PT-LANG-ADDR-01 — Portuguese second-person address-system realization
```

Existing owner:

```text
Localization / Chapter 07
```

Existing route:

```text
adapt-localization.relationship-realization
```

This suite tests architecture, scope, activation, evidence boundaries, and regression properties. It does not claim population preferences, benchmark translation quality, or prescribe one Portuguese treatment system.

---

## Runtime oracle

```text
CURRENT JOB
→ FREEZE RESOLVED SPEAKER / RECIPIENT / RELATIONSHIP / STANCE /
  INTERACTION / APPROVED VOICE / SURFACE STATE
→ IS A PORTUGUESE SECOND-PERSON TREATMENT REALIZATION
  MATERIALLY OPEN OR BEING CHANGED?

NO
→ DO NOT LOAD PT-LANG-ADDR-01

YES
→ CHAPTER 07 OWNER
→ adapt-localization.relationship-realization
→ SECTION-LOCAL SCOPE CHECK
→ APPLY ONLY PORTUGUESE-SPECIFIC CONSTRAINTS
  TO THE STILL-OPEN REALIZATION DIMENSION
```

Activation requires:

```text
TARGET LANGUAGE = PORTUGUESE
+
SECOND-PERSON TREATMENT REALIZATION IS MATERIALLY OPEN OR BEING CHANGED
+
THE CHOICE CAN ALTER TREATMENT-SYSTEM COHERENCE
OR EXPLICIT / NULL ADDRESSEE REALIZATION
```

Portuguese, Brazil, Portugal, Angola, Mozambique, customer, business, formal, friendly, public-sector copy, marketing, or social media alone is insufficient.

---

## Promotion-bearing runtime properties

### Property A — address form is not a complete paradigm

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
!= EVERY MIX IS VALID
```

### Property B — explicitness can be treatment realization

```text
EXPLICIT VOCÊ
!= NULL 3SG ADDRESS REALIZATION

SAME 3SG VERBAL MORPHOLOGY
!= SAME TREATMENT REALIZATION

ZERO OVERT PRONOUN
!= ZERO RELATIONAL / PRAGMATIC VALUE
```

### Evidence-authority repair

```text
PTLA10
→ DOCUMENTED FIRST-PARTY POLICY

PTLA11 / PTLA12
→ CURRENT SCOPED FIRST-PARTY USAGE
→ NOT DOCUMENTED CROSS-SURFACE POLICY
```

---

# P1–P16 runtime pressure cases

## P1 — approved gov.br-style `você`

Applicable documented organization rule fixes `você` for the surface.

**Expected**

```text
PRESERVE RESOLVED FORM
DO NOT REOPEN FROM BROADER PORTUGUESE VARIATION
```

## P2 — approved `tu` system

Applicable approved copy uses `tu / te` and supported 2SG forms consistently.

**Expected**

```text
PRESERVE RESOLVED SYSTEM
DO NOT REOPEN BECAUSE OTHER PORTUGUESE SYSTEMS EXIST
```

## P3 — scoped `tu +` non-overt agreement

Scoped variety/community evidence resolves wording such as:

```text
tu fala
tu vai
```

**Expected**

```text
PRESERVE WHEN ACTUALLY SUPPORTED IN SCOPE
DO NOT MECHANICALLY NORMALIZE TO tu falas / tu vais
```

## P4 — unsupported `tu` agreement drift

Approved scoped voice uses overt 2SG agreement, but one line accidentally shifts to another pattern without supporting state.

**Expected**

```text
ATTESTED VARIATION != IMMUNITY FOR DRIFT
REPAIR TO RESOLVED SYSTEM
```

## P5 — scoped `você ... te`

Applicable evidence or approved voice supports `você` subject with `te` object clitic.

**Expected**

```text
DO NOT NORMALIZE SOLELY BECAUSE FORMS COME FROM DIFFERENT HISTORICAL PARADIGMS
```

## P6 — arbitrary unsupported mix

Draft mixes `tu`, `você`, `te`, `lhe`, verbal patterns, and possessives without scoped support or interactional reason.

**Expected**

```text
MIXED != AUTOMATIC ERROR
BUT ALSO
MIXED != AUTOMATICALLY VALID

REPAIR UNSUPPORTED DRIFT USING RESOLVED STATE
```

## P7 — scoped Cabinda composition

Scoped Cabinda evidence supports `você` with forms derived historically from the `tu` paradigm.

**Expected**

```text
DO NOT FORCE PAN-PORTUGUESE VOCÊ → COMPLETE 3SG PARADIGM NORMALIZATION
```

## P8 — explicit `você` insertion

Input:

```text
Deseja continuar?
```

Relationship and existing style are already appropriate. Transformation proposes:

```text
Você deseja continuar?
```

only for explicitness.

**Expected**

```text
REJECT AUTOMATIC INSERTION
EXPLICITNESS MAY ALTER TREATMENT VALUE
```

## P9 — explicit `você` removal

Applicable organization/community state intentionally or explicitly resolves an overt `você` realization.

**Expected**

```text
PRESERVE RESOLVED OVERT FORM
NULL-3SG EVIDENCE ELSEWHERE DOES NOT AUTHORIZE DELETION
```

## P10 — natural null-3SG reader address

Copy uses forms such as:

```text
Se tiver dúvidas, pode continuar por aqui.
```

**Expected**

```text
DO NOT INSERT VOCÊ MERELY TO SATISFY AN EXPLICIT-SUBJECT PREFERENCE
```

## P11 — country-only request

Task says "for Brazil" or "for Portugal" but supplies no narrower treatment evidence and the treatment choice is consequential.

**Expected**

```text
NO COUNTRY → PRONOUN LOOKUP
PRESERVE / EXPOSE THE UNRESOLVED DEPENDENCY AS REQUIRED BY CHAPTER 07
```

## P12 — Portuguese outside Lusophone geography

Portuguese-language support copy targets Portuguese speakers in the US, France, Japan, or another geography and treatment realization remains open.

**Expected**

```text
MAY LOAD
LANGUAGE REALIZATION != GEOGRAPHIC MEMBERSHIP
```

## P13 — Lusophone market, non-Portuguese output

Task targets Brazil, Portugal, Angola, or Mozambique but output is English or Spanish.

**Expected**

```text
NO LOAD
```

## P14 — `seu / sua` referent ambiguity only

Treatment system is already fixed; only the intended possessor/referent remains ambiguous.

**Expected**

```text
DO NOT USE PT-LANG-ADDR-01 AS A POSSESSIVE RESOLVER
HANDLE THROUGH GENERIC REFERENT FIDELITY / ORDINARY PORTUGUESE COMPETENCE
```

## P15 — no material address realization

Title, label, heading, nominal UI element, or other surface has no material second-person treatment decision.

**Expected**

```text
NO LOAD
PORTUGUESE LANGUAGE ALONE IS NOT ACTIVATION AUTHORITY
```

## P16 — first-party surfaces differ

### P16-A — explicit policy supplied

Approved organization policies differ by product/surface/audience.

**Expected**

```text
PRESERVE EACH POLICY IN ITS ACTUAL SCOPE
DO NOT NORMALIZE TO ONE ORGANIZATION-WIDE PORTUGUESE FORM
```

### P16-B — only current first-party usage observed

Current first-party surfaces exhibit different treatment realizations, as with PTLA11/PTLA12, but no cross-surface policy document is supplied.

**Expected**

```text
TREAT EACH AS STRONG SCOPED CURRENT USAGE EVIDENCE
DO NOT INFER DOCUMENTED POLICY OR VERIFIED INTENT
DO NOT NORMALIZE ONE SURFACE FROM ANOTHER WITHOUT STRONGER EVIDENCE
```

---

## Negative controls — Portuguese issues outside PT-LANG-ADDR-01

These must remain ordinary grammar / truth / coherence issues and must not activate the unit merely because the text is Portuguese.

### N1 — ordinary number agreement

```text
As campanhas foi publicada ontem.
```

Potential correction is ordinary Portuguese grammar, not second-person treatment realization.

### N2 — ordinary first-person verb agreement

```text
Nós precisa revisar o preço.
```

Potential correction is ordinary grammar, not treatment-system composition.

### N3 — temporal contradiction

```text
A reunião aconteceu amanhã e terminou ontem.
```

Potential repair is semantic/temporal coherence, not Portuguese address realization.

---

# Static implementation requirements

A runtime implementation passes this suite only if all are true:

1. `PT-LANG-ADDR-01` remains under the existing Localization / Chapter 07 owner.
2. Logical route remains `adapt-localization.relationship-realization`.
3. No `adapt-portuguese`, `adapt-brazil`, `adapt-portugal`, `pt-*`, or other country/language-owned route is created.
4. No controller change is required.
5. No `routing-index.json` change is required.
6. No `get-knowledge.py` change is required.
7. No shared person/treatment primitive is added.
8. No country/variety resolver is added.
9. No paradigm score or treatment score is added.
10. Runtime explicitly states `ADDRESS FORM != COMPLETE PERSON PARADIGM`.
11. Runtime does not encode `tu → overt 2SG agreement` universally.
12. Runtime does not encode `você → complete 3SG paradigm` universally.
13. Runtime does not auto-reject scoped `você + te` or other supported composition.
14. Runtime also rejects blanket preservation of arbitrary mixed paradigms.
15. Runtime explicitly distinguishes explicit `você` from null-3SG treatment realization where evidence makes the distinction material.
16. Runtime does not insert or delete explicit `você` merely for generic clarity/explicitness when treatment value is already resolved.
17. Country, nationality, customer, age, business, formal/friendly, government, marketing, or social-media nouns alone do not activate the unit.
18. `seu/sua` ambiguity remains outside the promoted Portuguese mechanism under the current evidence set.
19. PTLA10 remains documented first-party policy evidence only in its actual scope.
20. PTLA11/PTLA12 remain current scoped first-party usage evidence and are not described as documented intentional cross-surface policy.
21. Current first-party usage may be preserved when it is actual applicable approved wording without converting that observation into an organization-wide rule.
22. No population preference, country-wide default, marketing-lift claim, or universal brand voice is introduced.

---

# Failure oracle

```text
F0  Loads PT-LANG-ADDR-01 when no material Portuguese treatment decision exists.
F1  Fails to load when a material Portuguese treatment-system / explicit-null decision is open.
F2  Maps country directly to tu / você / senhor(a) / null-3SG.
F3  Normalizes every tu to overt 2SG agreement.
F4  Normalizes every você into one complete 3SG paradigm.
F5  Treats você + te as intrinsically corrupted.
F6  Treats every mixed paradigm as valid because some mixed systems are attested.
F7  Inserts explicit você into null-3SG copy merely for explicitness.
F8  Removes explicit você merely because null-3SG exists elsewhere.
F9  Converts seu/sua referent ambiguity into a Portuguese-specific resolver.
F10 Reopens an applicable documented first-party policy from broader variation evidence.
F11 Labels PTLA11/PTLA12 current usage as documented / deliberate cross-surface policy.
F12 Infers policy intent from observed cross-surface difference.
F13 Treats Portuguese geography as sufficient activation for non-Portuguese output.
F14 Treats Portuguese language alone as sufficient activation.
F15 Adds a country/variety resolver, paradigm scorer, shared primitive, new owner, or new route without a demonstrated architecture failure.
```

Any implementation exhibiting an F0–F15 failure does not pass this regression suite.
