# Commercial Design Research

Status: **THEORY VERIFIED — BOUNDED RUNTIME INTEGRATED**

This directory preserves the substantive research lineage behind the Marketing Practitioner capability for **commercial design, pricing architecture, and terms of exchange**.

The research addresses the structural gap between positioning/value reasoning (Chapter 03) and commerce-state/catalog representation (Chapter 09). It investigates how practitioners design commercial conditions—entitlements, payment architecture, relationship and risk terms, and commercial transitions—before they freeze into an active catalog state or enter bilateral buyer-specific sales negotiation.

## Governing Question

> Given an offering, market context, and relevant alternatives, how should a marketing practitioner design commercial exchange—packaging, charge basis, payment architecture, relationship terms, and transition paths—while preserving evidence limits, organizational constraints, and meaningful customer choice?

Key assumptions rejected during scoping:
- Commercial design is reducible to price-point optimization or profit-maximization elasticity formulas.
- Stated willingness-to-pay is directly predictive of sustainable market clearing prices.
- B2B commercial terms can replace buyer-specific sales negotiation.

## Disposition

```text
CORE THEORY FREEZE: ADJUDICATED (PR #11 / PR #12)
PRICING METRIC SUB-TRACK: COMPLETED & INTEGRATED
RUNTIME TARGET: Chapter 10 (10-commercial-design-pricing-and-terms.md)
ROUTING NAMESPACE: commercial-design.* (commercial-design.payment, commercial-design.dynamics)
EVIDENCE LEDGER: references/commercial-design-evidence.md
```

- **Runtime Target**: Handbook Chapter 10 (`10-commercial-design-pricing-and-terms.md`), evidence ledger `references/commercial-design-evidence.md`.
- **Mechanisms Added**: Package/entitlement boundaries, charge-basis selection matrix, payment architectures, risk allocation frameworks, and transition/migration governance.
- **Expansions Rejected**: General business-model innovation, microeconomic elasticity solvers, and automated dynamic yield management engines.

## File Lineage Table

### Phase 1: Core Commercial Design Architecture
| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`00-research-brief.md`](00-research-brief.md) | Research scope, core failure modes, and boundary definitions | Research Brief |
| [`01-theory-freeze-candidate.md`](01-theory-freeze-candidate.md) | Candidate theory freeze for general commercial design and exchange terms | Theory Freeze |
| [`02-evidence-ledger.md`](02-evidence-ledger.md) | Primary and secondary empirical evidence ledger supporting exchange mechanisms | Evidence Ledger |
| [`03-commercial-design-freeze-adjudication.md`](03-commercial-design-freeze-adjudication.md) | Independent review adjudication closing core commercial design theory | Adjudication |

### Phase 2: Pricing-Metric & Charge-Basis Selection Sub-Track
| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`03-pricing-metric-selection-theory-freeze.md`](03-pricing-metric-selection-theory-freeze.md) | Dedicated theory freeze on pricing metrics (seat vs usage vs outcome) | Theory Freeze |
| [`04-pricing-metric-selection-evidence-ledger.md`](04-pricing-metric-selection-evidence-ledger.md) | Empirical evidence ledger evaluating charge-basis misalignments | Evidence Ledger |
| [`05-pricing-metric-selection-post-review-repair.md`](05-pricing-metric-selection-post-review-repair.md) | Review adjudication and bounded repairs for pricing-metric selection | Post-Review Repair |

Related historical audits & regressions:
- [`../historical-audits/commercial-design-runtime-routing-smoke.md`](../historical-audits/commercial-design-runtime-routing-smoke.md)
- [`../historical-audits/pricing-metric-selection-bounded-cases.md`](../historical-audits/pricing-metric-selection-bounded-cases.md)

## Protected Invariants

```text
POSITIONING / VALUE
!=
COMMERCIAL DESIGN
!=
BUYER-SPECIFIC COMMERCIAL NEGOTIATION / COMMITMENT
!=
CURRENT COMMERCE STATE / REPRESENTATION

STATING WILLINGNESS-TO-PAY != OPTIMAL SUSTAINABLE PRICE
PRICE POINT != PRICING METRIC / CHARGE BASIS
ACCESS ENTITLEMENT != PAYMENT ARCHITECTURE
```

- Upstream positioning and target customer choices remain frozen during commercial design.
- Commercial design sets the default terms of exchange; it does not own bilateral account negotiations (owned by Chapter 16 / Founder-led Sales).
- Unresolved evidence regarding customer willingness-to-pay must be treated as unknown rather than modeled via speculative curves.
