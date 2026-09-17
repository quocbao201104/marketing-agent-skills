# Spanish Local Adaptation — Post-Review Bounded Repair

Status: **BOUNDED REVIEW REPAIR APPLIED — RUNTIME PROMOTION NOT YET PERFORMED**  
Date: 2026-09-17  
Frozen candidate reviewed: `c5ac8e7cd5408600789e2da01472449ff9dd62f6`  
Independent review result commit: `ba041b6b96118e8f5e665fd39659934b52d55677`  
Independent verdict: `PASS_WITH_BOUNDED_REPAIR`

This record closes exactly one material finding from `04-independent-review-result.md`:

```text
ES-IR-01
possessive ambiguity asserted beyond the frozen evidence record
```

It does not reopen the Spanish local-adaptation theory, add new evidence, or promote `ES-LANG-ADDR-01` into runtime knowledge.

The frozen files remain frozen at the reviewed commit. This repair is an explicit post-review delta over that target rather than a retroactive rewrite of the reviewed artifact.

---

## ES-IR-01 — bounded evidence-scope repair

### Finding

Frozen §8 stated:

```text
`usted / ustedes` use third-person verbal morphology,
and possessives such as `su / sus` can be referentially ambiguous in context.
```

The frozen evidence ledger supports the first clause through ESLA11. It does not independently establish the second clause as a Spanish adaptation claim, and the ledger itself identifies treatment-sensitive possessive/reference ambiguity as deferred evidence if a specific repair is to be promoted.

### Repair

For every subsequent design, implementation, or evaluation step, replace the unsupported §8 scope with the narrower rule below:

```text
USTED / USTEDES VERBAL AGREEMENT
SHARES THIRD-PERSON MORPHOLOGY
+
CONTEXT CONTAINS BOTH ADDRESSEE AND THIRD-PARTY REFERENTS
+
THE SHARED VERBAL FORM CREATES MATERIAL AMBIGUITY
→ CLARIFY THE REFERENT ONLY AS NEEDED
→ USE A NATURAL FORMULATION SUPPORTED FOR THE TARGET VARIETY / VOICE

AMBIGUITY
!= PERMISSION TO IMPORT ANOTHER VARIETY'S ADDRESS PARADIGM
```

And add this explicit boundary:

```text
POSSESSIVE OR OTHER REFERENT AMBIGUITY
INCLUDING `su / sus`
→ PRESERVE SOURCE REFERENT FIDELITY THROUGH ORDINARY SPANISH COMPETENCE
  AND THE GENERIC CHAPTER 07 CONTRACT
→ DO NOT TREAT IT AS AN INDEPENDENTLY EVIDENCED
  ES-LANG-ADDR-01 MECHANISM FROM THE CURRENT LEDGER
→ DO NOT PRESCRIBE A SPANISH-SPECIFIC POSSESSIVE REPAIR
  UNLESS SEPARATELY EVIDENCED
```

### S13 repaired interpretation

S13 remains a valid composition test:

```text
customer team       = YOU ALL
implementation team = THEY
draft                = pueden / sus
```

Post-repair adjudication is:

```text
`pueden`
→ ESLA11 can support the Spanish-specific shared-verbal-morphology collision

`sus`
→ generic source-referent fidelity / ordinary Spanish competence only
  under the current evidence set

both
→ must preserve the intended referent if ambiguity is material

neither
→ authorizes importing `vosotros / vuestro` solely to disambiguate
```

This preserves the adversarial case without laundering an unsupported possessive claim into the local adaptation.

---

## Why no new source was added

The methodology favors the least powerful mechanism that fixes the demonstrated failure.

The promotion-bearing Spanish mechanism already survives without a possessive-specific rule. Therefore the smallest repair is to narrow the unsupported claim, not to expand the bibliography merely to preserve broader wording.

A later concrete task may justify new possessive/reference evidence. Until then:

```text
MISSING EVIDENCE
!= REQUIREMENT TO FILL THE BIBLIOGRAPHY

SUPPORTED CORE MECHANISM
!= PERMISSION TO KEEP ADJACENT UNSUPPORTED DETAIL
```

---

## What remains unchanged

The repair does **not** change:

- the promotion verdict for `ES-LANG-ADDR-01`;
- the `tú / vos / usted` non-linear treatment boundary;
- selective `vos + te / tu / tuyo` preservation;
- pronominal-only or verbal-only voseo;
- Chilean mixed-system handling;
- scoped plural `ustedes / vosotros` handling;
- first-party-state boundaries;
- address-neutrality boundaries;
- ordinary-grammar boundary;
- the existing Localization / Chapter 07 owner;
- `adapt-localization.relationship-realization`;
- `SKILL.md`;
- Chapter 07;
- `routing-index.json`;
- `get-knowledge.py`;
- any shared-state primitive.

---

## Post-repair promotion state

```text
ES-IR-01
→ CLOSED BY NARROWING

ES-LANG-ADDR-01
→ REVIEW-SUPPORTED FOR FUTURE RUNTIME PROMOTION

SPLIT UNIT
→ NO

NEW OWNER / ROUTE / RESOLVER
→ NO

NEW EVIDENCE SOURCE
→ NO

adaptations/localization.md
→ UNCHANGED
```

The next step, if requested, is a bounded runtime implementation derived from:

```text
frozen target c5ac8e7cd5408600789e2da01472449ff9dd62f6
+
04-independent-review-result.md
+
this repair record
```

Do not restore the broader possessive-ambiguity claim during runtime promotion unless new scoped evidence independently supports it.
