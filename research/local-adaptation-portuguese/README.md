# Local Adaptation Portuguese Research

Status: **THEORY VERIFIED — BOUNDED RUNTIME INTEGRATED**

This directory preserves the design freeze, empirical evidence ledger, adversarial review briefs, post-review repairs, and addressability fixes establishing the **Portuguese linguistic relationship-realization adaptation**.

The research addresses the chronic failure of AI marketing tools to treat the Portuguese language as a monolith, inadvertently using Brazilian Portuguese (pt-BR) norms in Portugal (pt-PT) or vice versa. The Portuguese adaptation formalizes the deep pronominal and pragmatic split between pt-BR (where *você* is standard direct address across casual and commercial registers) and pt-PT (where *você* carries specific social distance markers, *tu* dominates informal relationships, and *o senhor / a senhora* governs formal commercial interaction).

## Governing Question

> When marketing communication is targeted for Portuguese-speaking markets, how should practitioner reasoning specialize dialectal addressability (pt-BR vs. pt-PT), pronoun selection (*você*, *tu*, nominal address), and commercial formality without collapsing into generic Iberian/Lusophone stereotypes?

Key assumptions rejected during scoping:
- Brazilian Portuguese and European Portuguese can share a single "neutral" marketing translation.
- *Você* carries identical social distance and formality semantics in Brazil and Portugal.

## Disposition

```text
STATUS: THEORY VERIFIED & BOUNDED RUNTIME INTEGRATED
RUNTIME TARGET: skills/marketing-agent-skills/adaptations/portuguese/
GOVERNING CHAPTER: Chapter 07 (07-international-marketing-and-ethics.md)
EVIDENCE SOURCE: references/local-adaptation-evidence.md
```

- **Runtime Target**: `skills/marketing-agent-skills/adaptations/portuguese/` and Chapter 07 routes.
- **Mechanisms Added**: pt-BR vs. pt-PT addressability matrix, clitic pronoun placement rules (*próclise* vs. *ênclise*), and commercial distance registers.
- **Expansions Rejected**: Autonomous cultural packs, regional slang repositories, and broad Lusophone marketing generalities.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-design-freeze.md`](01-design-freeze.md) | Design freeze specifying pt-BR vs. pt-PT pronominal address and syntactic norms | Design Freeze |
| [`02-evidence-ledger.md`](02-evidence-ledger.md) | Corpus linguistics evidence ledger documenting commercial address usage across Brazil and Portugal | Evidence Ledger |
| [`03-independent-review-brief.md`](03-independent-review-brief.md) | Adversarial review brief examining addressability clashes in B2B and consumer campaigns | Review Brief |
| [`04-independent-review-result.md`](04-independent-review-result.md) | Independent review certification confirming grammatical and regional boundaries | Review Result |
| [`05-post-review-repair.md`](05-post-review-repair.md) | Bounded repairs resolving clitic placement ambiguities in direct marketing copy | Post-Review Repair |
| [`06-independent-implementation-review-result.md`](06-independent-implementation-review-result.md) | Implementation review certifying runtime adaptation package integration | Implementation Review |
| [`07-post-merge-addressability-fix.md`](07-post-merge-addressability-fix.md) | Target addressability fix ensuring strict isolation between pt-BR and pt-PT routes | Post-Merge Fix |

Related historical audits & regressions:
- [`../historical-audits/local-adaptation-portuguese-v0.md`](../historical-audits/local-adaptation-portuguese-v0.md)

## Protected Invariants

```text
pt-BR != pt-PT (IRREDUCIBLE PRONOMINAL & SYNTACTIC SPLIT)
VOCÊ (pt-BR: STANDARD DIRECT ADDRESS) != VOCÊ (pt-PT: DISTANCED / REGULATED)
PORTUGUESE MARKET CONTEXT != REOPENING UPSTREAM STRATEGY
SHARED THEORY REMAINS SHARED
```

- Never use pt-BR direct address norms in pt-PT campaigns (where *você* can sound inappropriately abrupt or aggressive).
- Local linguistic specialization bounds realization strictly to address and syntax; it does not authorize reopening settled value propositions.
