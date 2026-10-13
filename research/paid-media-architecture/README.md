# Paid Media Architecture Research

Status: **THEORY VERIFIED — BOUNDED RUNTIME INTEGRATED**

This directory preserves the extensive research lineage, theory freeze, adversarial reviews, and release preparation establishing **paid media control semantics and allocation reasoning** in Handbook Chapter 14 (`14-paid-media-architecture.md`).

The research addresses the chronic failure of marketing agents to treat paid advertising as a spending accelerator or to trust ad network reporting uncritically. Chapter 14 establishes rigorous principles for economic control, delivery mechanics, auction dynamics, budget allocation across liquidity pools, conversion signal integrity, and causal attribution verification.

## Governing Question

> How should a practitioner reason about paid media resource allocation, platform delivery controls, auction feedback, and signal health without conflating ad-network platform attribution with true incremental economic return?

Key assumptions rejected during scoping:
- Platform-reported ROAS or CPA is directly indicative of incremental profit.
- Higher ad spend and broad targeting are universal remedies for conversion bottlenecks.
- Ad platform algorithmic bidding eliminates the need for human constraint and signal auditing.

## Disposition

```text
STATUS: THEORY VERIFIED & RUNTIME INTEGRATED
RUNTIME TARGET: Handbook Chapter 14 (14-paid-media-architecture.md)
ROUTING NAMESPACE: paid-media.* (4 addressable routes)
EVIDENCE LEDGER: references/paid-media-evidence.md
```

- **Runtime Target**: Handbook Chapter 14 and the `paid-media.*` routing namespace.
- **Mechanisms Added**: Paid control semantics (bidding, caps, constraints), liquidity allocation frameworks, conversion signal quality rubrics, and incremental feedback loops.
- **Expansions Rejected**: Automated ad spend scaling scripts, real-time programmatic bidding engines, and speculative audience generation algorithms.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-theory-freeze.md`](01-theory-freeze.md) | Comprehensive theoretical freeze defining paid control semantics, delivery mechanics, and measurement | Theory Freeze |
| [`02-implementation-design.md`](02-implementation-design.md) | Architectural specification mapping paid media theory to Handbook Chapter 14 and routing routes | Implementation Design |
| [`03-implementation-self-review.md`](03-implementation-self-review.md) | Author audit checking routing precision, evidence ledger linkages, and boundary constraints | Self-Review |
| [`04-mechanical-verification.md`](04-mechanical-verification.md) | Deterministic test verifying route resolution, source IDs, and formatting integrity | Mechanical Verification |
| [`05-targeted-evaluation-adjudication.md`](05-targeted-evaluation-adjudication.md) | Targeted evaluation adjudication across complex multi-channel paid scenarios | Adjudication |
| [`06-independent-runtime-review-brief.md`](06-independent-runtime-review-brief.md) | Adversarial peer review brief examining edge cases in budget allocation and attribution | Review Brief |
| [`07-independent-review-launch.md`](07-independent-review-launch.md) | Formal review launch memo and reviewer instructions | Review Launch |
| [`08-independent-review-correction.md`](08-independent-review-correction.md) | Bounded post-review corrections refining signal health and audience saturation rules | Review Correction |
| [`09-correction-verification-launch.md`](09-correction-verification-launch.md) | Verification launch certifying corrected paid media guidance | Verification Launch |
| [`10-release-preparation.md`](10-release-preparation.md) | Release packaging checklist and integration sign-off | Release Preparation |

Related historical audits & regressions:
- [`../historical-audits/paid-media-architecture-adversarial-cases.md`](../historical-audits/paid-media-architecture-adversarial-cases.md)
- [`../historical-audits/paid-media-architecture-review-regression.md`](../historical-audits/paid-media-architecture-review-regression.md)
- [`../historical-audits/paid-media-architecture-runtime-smoke.md`](../historical-audits/paid-media-architecture-runtime-smoke.md)

## Protected Invariants

```text
PAID CONTROL / ALLOCATION != AUTOMATIC SPEND INCREASE
PLATFORM ATTRIBUTION != INCREMENTALITY
CORRELATION != CAUSATION
SPONSORSHIP / COMMERCIAL DEAL != AUTOMATIC PAID MEDIA ROUTE
ALGORITHMIC OPTIMIZATION != UNCONSTRAINED AUTONOMY
```

- Paying a creator or influencer for content does not automatically trigger Chapter 14 unless paid-media delivery and auction controls are actively involved.
- Platform-reported conversions frequently capture baseline demand; decisions must account for attribution bias and incrementality tests.
- When advertising performance declines, diagnose causal factors (creative fatigue, landing page degradation, signal breakage) before adjusting budget allocation.
