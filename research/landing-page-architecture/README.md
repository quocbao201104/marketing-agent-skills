# Landing Page Architecture Research

Status: **THEORY VERIFIED — BOUNDED RUNTIME INTEGRATED**

This directory preserves the research brief, theory freeze, empirical evidence ledger, and adjudication records establishing **landing-page conversion architecture and decision graphs** in Handbook Chapter 11 (`11-landing-page-architecture.md`).

The research addresses the failure where marketing agents jump directly from copy writing to front-end layout or treat landing pages as a rigid, linear document. Chapter 11 governs the information architecture, sequence, reader decision paths (ready buyers, skeptical newcomers, security evaluators), cross-page delegation, and action/form boundaries once underlying positioning and commercial terms are settled.

## Governing Question

> Once message, proof, and commercial terms are sufficiently resolved, how should a marketing practitioner structure the page sequence, decision graph, scan vs. deep reading paths, and proof placement without collapsing into generic UI layout or reopening settled upstream decisions?

Key assumptions rejected during scoping:
- Landing page design is an aesthetic exercise best left to generic web design templates.
- Every visitor reads the landing page in a single, top-to-bottom linear path.
- The primary landing page must contain all possible company information and technical specifications.

## Disposition

```text
STATUS: THEORY VERIFIED & RUNTIME INTEGRATED
RUNTIME TARGET: Handbook Chapter 11 (11-landing-page-architecture.md)
ROUTING NAMESPACE: landing-page.* (7 addressable routes)
EVIDENCE LEDGER: references/landing-page-evidence.md
```

- **Runtime Target**: Handbook Chapter 11 and the `landing-page.*` routing namespace.
- **Mechanisms Added**: Decision-graph navigation, scan vs. deep path separation, information reachability thresholds, cross-page delegation boundaries, and responsive priority ordering.
- **Expansions Rejected**: HTML/CSS code generators, drag-and-drop page builders, and micro-aesthetic styling frameworks.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`00-research-brief.md`](00-research-brief.md) | Research brief defining the gap between copy writing and front-end implementation | Research Brief |
| [`01-theory-freeze.md`](01-theory-freeze.md) | Theory freeze specifying decision-graph architecture, information reachability, and section functions | Theory Freeze |
| [`02-evidence-ledger.md`](02-evidence-ledger.md) | Primary empirical evidence ledger evaluating eye-tracking, cognitive load, and page conversion | Evidence Ledger |
| [`03-freeze-adjudication.md`](03-freeze-adjudication.md) | Independent review adjudication certifying Chapter 11 runtime integration | Adjudication |

Related historical audits & regressions:
- [`../historical-audits/landing-page-architecture-adversarial-cases.md`](../historical-audits/landing-page-architecture-adversarial-cases.md)

## Protected Invariants

```text
MESSAGE / PROOF / COMMERCIAL RESOLVED + PAGE ALLOCATION OPEN
→ Chapter 11 (landing-page.*)

PERSISTENT BRAND IDENTITY CUE → Chapter 15
PAGE ALLOCATION & COMPOSITION → Chapter 11
FRONTEND CODING / CMS RENDERING → Downstream tooling

ONE RIGID LINEAR PATH != MULTI-AUDIENCE DECISION GRAPH
PAGE ALLOCATION != GENERIC UI / GRAPHIC DESIGN
ALL INFO ON ONE PAGE != CROSS-PAGE DELEGATION
```

- The landing page owner organizes page sequence and decision enablement; it does not reopen approved positioning, pricing, or message proof.
- Visual identity provides master brand constraints (Chapter 15), but Chapter 11 owns hero composition and section allocation.
- Detailed technical, compliance, or secondary materials should be delegated to canonical cross-pages rather than cluttering core conversion paths.
