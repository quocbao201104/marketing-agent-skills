# Local Adaptation Japan Research

Status: **THEORY VERIFIED — BOUNDED RUNTIME INTEGRATED**

This directory preserves the design freeze, empirical evidence ledger, adversarial review briefs, and implementation verifications establishing the **Japanese linguistic relationship-realization adaptation**.

The research addresses the failure where marketing agents either treat Japanese marketing as an impenetrable exotic culture requiring full brand redesign, or conversely generate awkward literal translations that violate critical social distance norms. The Japanese adaptation bounds realization strictly to addressability, honorific registers (keigo: sonkeigo, kenjougo, teineigo), and relationship realization when an open communication decision requires target-language expression.

## Governing Question

> When a marketing communication decision is targeted for the Japanese market, how should practitioner reasoning specialize relationship realization, honorific registers, and commercial distance without reopening settled positioning or defaulting to cultural caricature?

Key assumptions rejected during scoping:
- Launching an approved global brand in Japan requires an automatic redesign of visual identity or value proposition.
- Japanese business communication requires maximum politeness (teineigo/sonkeigo) in every context regardless of customer closeness or product category.

## Disposition

```text
STATUS: THEORY VERIFIED & BOUNDED RUNTIME INTEGRATED
RUNTIME TARGET: skills/marketing-agent-skills/adaptations/japan/
GOVERNING CHAPTER: Chapter 07 (07-international-marketing-and-ethics.md)
EVIDENCE SOURCE: references/local-adaptation-evidence.md
```

- **Runtime Target**: `skills/marketing-agent-skills/adaptations/japan/` and Chapter 07 routes.
- **Mechanisms Added**: Keigo honorific tier selection, speaker-recipient relationship matrices, and pragmatic commercial distance boundaries.
- **Expansions Rejected**: Autonomous Japanese cultural guidebooks, consumer psychology stereotyping, and localized market-entry consulting templates.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-design-freeze.md`](01-design-freeze.md) | Design freeze specifying Japanese relationship realization and honorific registers | Design Freeze |
| [`02-evidence-ledger.md`](02-evidence-ledger.md) | Sociolinguistic and commercial evidence ledger grounding register selection | Evidence Ledger |
| [`03-independent-review-brief.md`](03-independent-review-brief.md) | Adversarial review brief examining register boundary failures and over-politeness risks | Review Brief |
| [`04-independent-review-result.md`](04-independent-review-result.md) | Independent review certification confirming boundary invariants | Review Result |
| [`05-independent-implementation-review-result.md`](05-independent-implementation-review-result.md) | Final implementation audit certifying runtime package integration | Implementation Review |

Related historical audits & regressions:
- [`../historical-audits/local-adaptation-japan-v0.md`](../historical-audits/local-adaptation-japan-v0.md)

## Protected Invariants

```text
JAPAN ALONE != PERMISSION TO REOPEN BRAND IDENTITY
KEIGO REGISTER = SOCIAL DISTANCE & RELATIONSHIP REALIZATION (NOT GENERIC FLATTERY)
RESOLVED GLOBAL POSITIONING REMAINS FROZEN
TRANSLATION != CULTURAL REINVENTION
```

- Launching an approved global product in Japan does not reopen positioning or brand identity; Chapter 07 activates only if target-language realization is open.
- Honorific selection must match actual customer-organization relationship posture rather than defaulting to mechanical maximal deference.
