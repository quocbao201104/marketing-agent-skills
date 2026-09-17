# Portuguese Local Adaptation — Independent Adversarial Review Brief

Status: **POST-FREEZE REVIEW CONTRACT**  
Frozen review target: `3269d2f4139123fa2a387a8e64611a193bee8c02`

This brief is committed after the frozen target and is only the review contract. It must not be treated as retroactive evidence that the frozen candidate already satisfied the contract.

## 1. Review objective

Independently adversarially review the frozen Portuguese local-adaptation candidate without defending it.

The reviewer must decide whether the frozen evidence and design justify:

```text
PT-LANG-ADDR-01
Portuguese second-person address-system realization
```

under the existing Chapter 07 owner and existing logical route:

```text
adapt-localization.relationship-realization
```

## 2. Non-negotiable review rules

- Review the frozen target exactly.
- Do not use later commits as proof that a frozen defect was fixed.
- Do not repair the candidate during adjudication.
- Distinguish source evidence from repository synthesis.
- Treat Spanish/Japanese/Korean analogies only as architecture comparisons, not Portuguese evidence.
- Prefer rejection/narrowing if ordinary Portuguese competence or generic Chapter 07 already resolves the claimed mechanism.
- Reject scope creep into country profiles, cultural etiquette, full Portuguese grammar, or marketing prescriptions.

## 3. Evidence adjudication

Re-check all frozen evidence records:

```text
PTLA01–PTLA12
```

For each record adjudicate:

```text
source exists / identifiable?
claim accurately represented?
sample/population/context preserved?
inference broader than evidence?
current first-party state distinguished from population norm?
promotion-bearing or boundary-only?
```

## 4. Promotion-bearing novelty attack

The frozen candidate claims two tightly related Portuguese mechanisms:

### A. Treatment-system composition

```text
ADDRESS FORM
!= COMPLETE PERSON PARADIGM

TU
!= AUTOMATIC 2SG MORPHOLOGY EVERYWHERE

VOCÊ
!= AUTOMATIC 3SG PARADIGM ACROSS ALL FORMS
```

Attack whether this is actually Portuguese-specific runtime knowledge or merely ordinary grammar.

Specifically test whether the evidence really supports the material editor failure:

```text
SUPPORTED tu + non-overt agreement
→ wrongly normalized as agreement error

SUPPORTED você + te / analogous composition
→ wrongly normalized to a single textbook paradigm
```

Do not count mere variation as novelty.

### B. Explicit-vs-null treatment realization

```text
EXPLICIT VOCÊ
!= NULL 3SG ADDRESS REALIZATION

ZERO OVERT PRONOUN
!= ZERO RELATIONSHIP MEANING
```

Attack whether the evidence supports this distinction strongly enough to change a Chapter 07 realization decision.

A candidate only survives if a generic clarity/editing operation could materially alter treatment by inserting or removing explicit address despite preserving propositional content.

## 5. Novelty comparison against existing runtime

Compare against:

- Chapter 07 relationship-indexing realization;
- `VN-LANG-REL-01`;
- `JP-LANG-HON-01`;
- `JP-LANG-PERM-01`;
- `ES-LANG-ADDR-01`;
- `KO-LANG-SPEECH-01`.

In particular attack overlap with `ES-LANG-ADDR-01`:

```text
PRONOUN != COMPLETE TREATMENT SYSTEM
MIXED FORM != AUTOMATIC ERROR
```

The Portuguese candidate must show Portuguese-specific evidence and a concrete decision delta. Similarity to Spanish is not sufficient.

Also test whether explicit-vs-null address is genuinely additional novelty rather than generic pro-drop grammar.

## 6. P1–P16 required adversarial cases

Adjudicate every frozen case.

### P1 — approved gov.br-style `você`

Expected: no reopening of an applicable first-party address policy.

### P2 — approved PT `tu` system

Expected: preserve resolved `tu` treatment; no reopening from broad Portuguese variation.

### P3 — scoped Brazilian `tu + non-overt agreement`

Expected: preserve only when scoped evidence/approved voice supports it; no mechanical textbook normalization.

### P4 — unsupported `tu` drift

Expected: repair accidental drift despite existence of legitimate variable agreement elsewhere.

### P5 — `você` subject + `te` object

Expected: do not normalize mechanically when scoped evidence supports the composition.

### P6 — arbitrary paradigm mix

Expected: attested mixture is not blanket permission to preserve unsupported combinations.

### P7 — Cabinda `você + tu-derived forms`

Expected: no pan-Portuguese `você→3SG-everything` normalization; evidence must remain Cabinda-scoped.

### P8 — explicit `você` insertion in PT-PT

Expected: insertion is not automatically relationship-neutral.

### P9 — explicit `você` removal

Expected: null-subject evidence elsewhere does not override a scoped approved explicit form.

### P10 — null 3SG with no missing-subject repair

Expected: do not add an overt pronoun merely for source-language-style explicitness.

### P11 — country-only request

Expected: no `Brazil→você` / `Portugal→tu` lookup.

### P12 — Portuguese outside Lusophone geography

Expected: language-realization scope may apply when the decision is open.

### P13 — Lusophone market, non-Portuguese output

Expected: no Portuguese adaptation load.

### P14 — `seu/sua` referent collision only

Expected: keep under generic referent fidelity unless independent evidence proves a Portuguese-specific runtime mechanism.

### P15 — address-neutral / nominal UI

Expected: no load if no material second-person treatment choice exists.

### P16 — first-party surface policies differ within one organization

Expected: preserve each scoped policy; no global brand/country normalization.

## 7. Forbidden upgrades to attack

Reject any implementation implication equivalent to:

```text
BRAZIL → VOCÊ
PORTUGAL → TU
ANGOLA → VOCÊ
MOZAMBIQUE → TU/VOCÊ FIXED RULE

CUSTOMER → VOCÊ
YOUNG → TU
FORMAL → SENHOR(A)
FRIENDLY → TU

TU → 2SG EVERYTHING
VOCÊ → 3SG EVERYTHING

VOCÊ + TE → ERROR
VOCÊ + 2SG-SHAPED FORM → ERROR

NULL SUBJECT → NEUTRAL EVERYWHERE
EXPLICIT VOCÊ → WRONG IN PORTUGAL

FIRST-PARTY STYLE → POPULATION NORM
```

## 8. Ordinary-grammar negative controls

The candidate must not become general Portuguese proofreading.

Examples outside candidate ownership unless treatment realization itself is material:

```text
article/noun gender error
ordinary number agreement error
spelling/accentuation error
tense/aspect error unrelated to treatment
lexical mistranslation
generic third-party referent ambiguity
```

`seu/sua` ambiguity alone is not currently promotion-bearing.

## 9. Architecture attack

Adjudicate whether any new machinery is truly required.

Expected frozen architecture claim:

```text
existing owner sufficient?           YES
existing route sufficient?           YES
new owner required?                  NO
new route required?                  NO
shared primitive required?           NO
country/variety resolver required?   NO
hierarchy resolver required?         NO
paradigm score required?             NO
controller change required?          NO
Chapter 07 change required?          NO
routing-index change required?       NO
get-knowledge change required?       NO
```

A reviewer should fail or narrow the design if it only works by introducing hidden country/variety classification or precedence machinery.

## 10. Counterfactual removal test

Remove all Portuguese-specific evidence while retaining:

```text
Chapter 07
+
VN / JP / ES / KO runtime contributions
+
task-specific approved state
```

Then test whether a competent generic editor can still reliably avoid:

```text
1. normalizing scoped `tu + non-overt agreement` as an error;
2. normalizing scoped `você + te` or comparable composition to one textbook paradigm;
3. inserting explicit `você` into a null-3SG PT-PT realization as a supposedly neutral clarity improvement;
4. deleting an approved explicit form because null-3SG exists elsewhere.
```

If generic knowledge reliably handles all four without Portuguese-specific evidence, reject the unit.

## 11. Review output

Write the independent result to:

`research/local-adaptation-portuguese/04-independent-review-result.md`

The result must contain:

- evidence adjudication for PTLA01–PTLA12;
- P1–P16 results;
- novelty/counterfactual adjudication;
- explicit Spanish-overlap analysis;
- architecture verdict;
- material findings if any;
- smallest bounded repair if required.

Top-level verdict must be exactly one of:

```text
PASS
PASS_WITH_BOUNDED_REPAIR
FAIL
```

Candidate disposition must be exactly one of:

```text
PROMOTE
NARROW
SPLIT
REJECT
```

If a finding exists, record it before any repair. Do not modify runtime during this review.
