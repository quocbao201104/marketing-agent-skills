# Portuguese Local Adaptation — Post-Review Bounded Repair

Status: **BOUNDED REVIEW REPAIR APPLIED — RUNTIME PROMOTION NOT YET PERFORMED**  
Date: 2026-09-17  
Frozen candidate reviewed: `3269d2f4139123fa2a387a8e64611a193bee8c02`  
Independent review result commit: `ac70453b5d3c7770f5c099f7b63ed34e1a16a70c`  
Independent verdict: `PASS_WITH_BOUNDED_REPAIR`  
Promotion verdict: `PROMOTE`

This record closes exactly one material finding from `04-independent-review-result.md`:

```text
PT-IR-01
current first-party gov.pt usage was promoted into wording implying
documented / deliberate cross-surface treatment policy
```

It does not reopen the Portuguese local-adaptation theory, add new evidence, change either promotion-bearing mechanism, or promote `PT-LANG-ADDR-01` into runtime knowledge.

The frozen files remain frozen at the reviewed commit. This repair is an explicit post-review delta over that target rather than a retroactive rewrite of the reviewed artifact.

---

## PT-IR-01 — bounded evidence-authority repair

### Finding

The frozen design correctly records that:

- PTLA10 is an explicit gov.br service-writing rule instructing writers to use `você` for the citizen;
- PTLA11 is current gov.pt public-service copy that repeatedly realizes direct reader address through 3SG/null-subject forms;
- PTLA12 is current gov.pt `On@18` copy that uses a `tu` system.

The defect occurs when §9 and P16 move from the PTLA11/PTLA12 observations to language implying a documented or intentional cross-surface policy:

```text
CURRENT FIRST-PARTY USAGE
→ "deliberately" uses a realization
→ FIRST-PARTY / SURFACE POLICY
→ organization "intentionally" uses different treatment realizations
```

The frozen evidence does not independently establish that gov.pt has a documented policy assigning those differing treatment systems by audience or surface.

### Repair

For every subsequent design, implementation, evaluation, or review step, apply the following authority distinction:

```text
PTLA10 GOV.BR GUIDE
→ DOCUMENTED FIRST-PARTY POLICY WITHIN ITS ACTUAL SCOPE

PTLA11 GOV.PT GENERAL SERVICE SURFACE
→ CURRENT FIRST-PARTY USAGE
→ CURRENT SCOPED FIRST-PARTY REALIZATION

PTLA12 GOV.PT ON@18 SURFACE
→ CURRENT FIRST-PARTY USAGE
→ CURRENT SCOPED FIRST-PARTY REALIZATION
```

Do not infer:

```text
CURRENT FIRST-PARTY USAGE
= DOCUMENTED FIRST-PARTY POLICY

OBSERVED CROSS-SURFACE DIFFERENCE
= VERIFIED INTENTIONAL POLICY ASSIGNMENT
```

The valid narrower inference is:

```text
ONE ORGANIZATION ECOSYSTEM
CAN EXHIBIT DIFFERENT SCOPED TREATMENT REALIZATIONS
```

This is evidence against mechanically normalizing every surface to one organization-wide Portuguese treatment form. It is not evidence that the organization has formally documented why those differences exist.

---

## Repaired §9 interpretation — first-party state boundary

For runtime derivation, replace the overbroad frozen §9 interpretation with:

```text
EXPLICIT FIRST-PARTY WRITING RULE / APPROVED POLICY
→ RESOLVED STATE WITHIN ITS ACTUAL SCOPE

CURRENT FIRST-PARTY SURFACE USAGE
→ STRONG SCOPED EVIDENCE FOR THAT SURFACE
→ MAY BE RESOLVED STATE WHEN IT IS THE ACTUAL APPROVED WORDING / VOICE
→ DOES NOT BY ITSELF ESTABLISH A DOCUMENTED ORGANIZATION POLICY

FIRST-PARTY USAGE OR POLICY
!= POPULATION PREFERENCE
!= COUNTRY-WIDE DEFAULT
```

Therefore:

- PTLA10 may be cited as first-party **policy** evidence within the gov.br service-writing scope;
- PTLA11/PTLA12 may be cited as current first-party **usage / realization** evidence within their actual surfaces;
- PTLA11/PTLA12 must not be described as proof that gov.pt intentionally assigned different treatment systems by surface or audience unless separate policy evidence is later supplied.

---

## P16 repaired interpretation

Frozen P16 used this setup:

```text
one organization intentionally uses different treatment realizations
across products / surfaces / audiences
```

Post-repair, split the case by evidence class.

### P16-A — actual policy supplied

If the task supplies approved organization rules that intentionally differ by product, surface, or audience:

```text
PRESERVE EACH POLICY IN ITS ACTUAL SCOPE
DO NOT NORMALIZE TO ONE ORGANIZATION-WIDE PORTUGUESE PRONOUN
```

This is a generic first-party-state rule and does not depend on PTLA11/PTLA12 proving such a policy exists at gov.pt.

### P16-B — only current first-party usage observed

If the only evidence is current first-party artifacts such as PTLA11/PTLA12:

```text
PRESERVE THE OBSERVED SCOPED REALIZATION WHEN IT IS APPLICABLE
TREAT IT AS STRONG CURRENT FIRST-PARTY USAGE EVIDENCE
DO NOT INFER A DOCUMENTED CROSS-SURFACE POLICY
DO NOT NORMALIZE ONE SURFACE FROM ANOTHER WITHOUT STRONGER EVIDENCE
```

Thus P16 remains a valid composition test after narrowing its authority claim.

---

## Evidence-ledger interpretation after repair

No evidence record is rejected or replaced.

```text
PTLA01–PTLA12
→ ALL REMAIN PASS
```

For the evidence-to-claim map and all future runtime summaries, interpret the first-party rows as:

```text
DOCUMENTED FIRST-PARTY POLICY CAN RESOLVE TREATMENT
→ PTLA10

CURRENT FIRST-PARTY USAGE CAN PROVIDE STRONG SCOPED REALIZATION EVIDENCE
→ PTLA11, PTLA12

ONE ORGANIZATION ECOSYSTEM CAN EXHIBIT DIFFERENT SCOPED REALIZATIONS
→ PTLA11, PTLA12

PTLA11 + PTLA12
!= DOCUMENTED CROSS-SURFACE POLICY
```

The frozen evidence ledger itself already labels PTLA11 and PTLA12 as current first-party public-service copy / guide and its source records remain usable. This repair narrows the project-level synthesis authority carried forward from those records.

---

## What remains unchanged

The repair does **not** change:

- promotion verdict `PROMOTE` for `PT-LANG-ADDR-01`;
- Mechanism A: `ADDRESS FORM != COMPLETE PERSON PARADIGM`;
- scoped `tu` with non-overt / 3SG-shaped agreement handling;
- scoped `você + te` handling;
- scoped Cabinda `você +` tu-derived / 2SG-shaped forms;
- the reverse guardrail `MIXED PARADIGM != AUTOMATICALLY VALID`;
- Mechanism B: `EXPLICIT VOCÊ != NULL 3SG ADDRESS REALIZATION`;
- country / nationality / market negative activation;
- `seu/sua` remaining generic referent fidelity under current evidence;
- the existing Localization / Chapter 07 owner;
- `adapt-localization.relationship-realization`;
- `SKILL.md`;
- Chapter 07;
- `routing-index.json`;
- `get-knowledge.py`;
- any shared-state primitive;
- any country/variety resolver;
- any paradigm scorer.

---

## Why no new source was added

The independent review found an authority-label defect, not a missing Portuguese mechanism.

The smallest repair is therefore to narrow the synthesis:

```text
CURRENT FIRST-PARTY USAGE
!= DOCUMENTED FIRST-PARTY POLICY
```

rather than adding bibliography merely to preserve stronger wording.

The two promotion-bearing mechanisms already survive independently of the overbroad policy characterization.

---

## Post-repair promotion state

```text
PT-IR-01
→ CLOSED BY AUTHORITY NARROWING

PT-LANG-ADDR-01
→ REVIEW-SUPPORTED FOR FUTURE RUNTIME PROMOTION

PROMOTION VERDICT
→ PROMOTE

SPLIT UNIT
→ NO

NEW OWNER / ROUTE / RESOLVER
→ NO

NEW EVIDENCE SOURCE
→ NO

adaptations/localization.md
→ UNCHANGED
```

The next runtime implementation, if performed, must be derived from:

```text
frozen target 3269d2f4139123fa2a387a8e64611a193bee8c02
+
04-independent-review-result.md
+
this repair record
```

Do not restore `deliberately`, `intentionally`, `surface policy`, or equivalent wording for PTLA11/PTLA12 unless separate evidence independently documents that policy or intent.
