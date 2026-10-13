# Local Adaptation Spanish Research

Status: **THEORY VERIFIED — BOUNDED RUNTIME INTEGRATED**

This directory preserves the design freeze, empirical evidence ledger, adversarial review briefs, post-review repairs, and implementation audits establishing the **Spanish linguistic relationship-realization adaptation**.

The research addresses the failure where marketing agents apply a synthetic "neutral Spanish" (Español neutro) that sounds foreign and unnatural across local markets, or misapply address forms across Latin America and Spain. The Spanish adaptation formalizes the tripartite address system—*tuteo* (standard informal in Spain and parts of Latin America), *voseo* (standard across the Rioplatense region and parts of Central America), and *ustedeo* (both formal commercial address and dialectal default in Colombia/Costa Rica)—as a bounded relationship realization decision.

## Governing Question

> When marketing communication is targeted for Spanish-speaking markets, how should practitioner reasoning specialize regional address forms (*tuteo*, *voseo*, *ustedeo*), grammatical verb conjugation, and commercial formality without flattening regional diversity into artificial "neutral" Spanish or cultural stereotypes?

Key assumptions rejected during scoping:
- A single "universal Latin American Spanish" can serve all regional digital marketing campaigns effectively.
- *Usted* indicates cold bureaucratic distance in all Spanish-speaking regions.

## Disposition

```text
STATUS: THEORY VERIFIED & BOUNDED RUNTIME INTEGRATED
RUNTIME TARGET: skills/marketing-agent-skills/adaptations/spanish/
GOVERNING CHAPTER: Chapter 07 (07-international-marketing-and-ethics.md)
EVIDENCE SOURCE: references/local-adaptation-evidence.md
```

- **Runtime Target**: `skills/marketing-agent-skills/adaptations/spanish/` and Chapter 07 routes.
- **Mechanisms Added**: Regional address selection matrix (*tuteo* vs. *voseo* vs. *ustedeo*), morphological verb agreement rules, and B2B/B2C commercial formality calibration.
- **Expansions Rejected**: Autonomous regional country profiles, colloquial slang dictionaries, and broad Hispanic marketing generalities.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-design-freeze.md`](01-design-freeze.md) | Design freeze specifying regional Spanish address systems (*tuteo*, *voseo*, *ustedeo*) and conjugation | Design Freeze |
| [`02-evidence-ledger.md`](02-evidence-ledger.md) | Sociolinguistic evidence ledger documenting commercial address norms across Spain and the Americas | Evidence Ledger |
| [`03-independent-review-brief.md`](03-independent-review-brief.md) | Adversarial review brief examining address form clashes in regional ad copy | Review Brief |
| [`04-independent-review-result.md`](04-independent-review-result.md) | Independent review certification confirming grammatical address boundaries | Review Result |
| [`05-post-review-repair.md`](05-post-review-repair.md) | Bounded repairs addressing voseo pronominal-verbal agreement in direct CTAs | Post-Review Repair |
| [`06-independent-implementation-review-result.md`](06-independent-implementation-review-result.md) | Implementation audit verifying runtime adaptation package conformity | Implementation Review |
| [`07-independent-implementation-review-repair.md`](07-independent-implementation-review-repair.md) | Final repair record resolving addressability edge cases in cross-regional campaigns | Review Repair |

Related historical audits & regressions:
- [`../historical-audits/local-adaptation-spanish-v0.md`](../historical-audits/local-adaptation-spanish-v0.md)

## Protected Invariants

```text
TUTEO != VOSEO != USTEDEO
"NEUTRAL SPANISH" != UNIVERSAL FIT
REGIONAL ADDRESS FORM → DETERMINED BY TARGET REGION × COMMERCIAL DISTANCE
LOCAL EVIDENCE SPECIALIZES OPEN REALIZATION (DOES NOT REOPEN UPSTREAM DECISIONS)
```

- In Rioplatense marketing (Argentina, Uruguay), *voseo* is standard informal commercial address; forcing *tuteo* creates immediate foreign friction.
- Local linguistic specialization bounds realization strictly to address and morphology; it does not authorize reopening settled value propositions.
