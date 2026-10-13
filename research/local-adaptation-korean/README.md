# Local Adaptation Korean Research

Status: **THEORY VERIFIED — BOUNDED RUNTIME INTEGRATED**

This directory preserves the design freeze, empirical evidence ledger, adversarial review briefs, and implementation reviews establishing the **Korean linguistic relationship-realization adaptation**.

The research addresses the failure where marketing agents either generate stiff, overly ceremonial Korean prose (excessive hasoseo-che / hapsio-che) or conversely adopt inappropriately intimate styles (banmal) in commercial contexts. The Korean adaptation bounds linguistic realization strictly to the two-dimensional matrix of formality and politeness across Korea's grammatical speech levels (hapsio-che, haeyo-che, etc.).

## Governing Question

> When a marketing communication decision is targeted for the Korean market, how should practitioner reasoning specialize speech-level selection, grammatical politeness, and commercial relationship distance without reopening settled positioning or defaulting to cultural caricature?

Key assumptions rejected during scoping:
- Korean marketing communications must universally employ formal hapsio-che across all digital and B2C channels.
- Localizing for South Korea requires creating a separate consumer psychology profile.

## Disposition

```text
STATUS: THEORY VERIFIED & BOUNDED RUNTIME INTEGRATED
RUNTIME TARGET: skills/marketing-agent-skills/adaptations/korean/
GOVERNING CHAPTER: Chapter 07 (07-international-marketing-and-ethics.md)
EVIDENCE SOURCE: references/local-adaptation-evidence.md
```

- **Runtime Target**: `skills/marketing-agent-skills/adaptations/korean/` and Chapter 07 routes.
- **Mechanisms Added**: Formality × Politeness speech-level matrix (hapsio-che vs. haeyo-che), commercial stance calibration, and brand-customer distance rules.
- **Expansions Rejected**: Autonomous Korean culture packs, trend taxonomies, and ungrounded consumer behavior assertions.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-design-freeze.md`](01-design-freeze.md) | Design freeze specifying Korean speech levels, pragmatic distance, and address forms | Design Freeze |
| [`02-evidence-ledger.md`](02-evidence-ledger.md) | Sociolinguistic evidence ledger grounding commercial speech-level distribution | Evidence Ledger |
| [`03-independent-review-brief.md`](03-independent-review-brief.md) | Adversarial review brief examining speech-level boundary violations in digital channels | Review Brief |
| [`04-independent-review-result.md`](04-independent-review-result.md) | Independent review certification confirming grammatical and pragmatic boundaries | Review Result |
| [`05-independent-implementation-review-result.md`](05-independent-implementation-review-result.md) | Implementation audit verifying runtime adaptation package conformity | Implementation Review |

Related historical audits & regressions:
- [`../historical-audits/local-adaptation-korean-v0.md`](../historical-audits/local-adaptation-korean-v0.md)

## Protected Invariants

```text
KOREAN MARKET != REOPENING STRATEGIC POSITIONING
SPEECH LEVEL = FORMALITY × POLITENESS (NOT GENERIC DEFERENCE)
HAPSIO-CHE VS HAEYO-CHE → GOVERNED BY BRAND-CUSTOMER DISTANCE
LOCAL EVIDENCE SPECIALIZES OPEN DECISION (NOT A NEW OWNER)
```

- Korea market entry does not reopen settled positioning, customer problem definitions, or commercial terms.
- Speech level realization must be determined by the interaction of channel context and brand-customer distance, not crude demographic assumptions.
