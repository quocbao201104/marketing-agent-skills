# Document and Artifact Planning Research

Status: **THEORY VERIFIED — BOUNDED RUNTIME INTEGRATED**

This directory preserves the research disposition and independent adversarial review evaluating whether Marketing Practitioner requires a dedicated Document Communication Architecture capability for white papers, workbooks, reusable reference guides, and educational marketing artifacts.

Independent review rejected the creation of a new specialist chapter or `document.*` namespace. Instead, it authorized a bounded generalization of the existing report-planning reference (`references/report-planning.md`) to encompass artifact retrieval modes (skimming, lookup, work-through) and reader-facing continuity without expanding the core runtime surface.

## Governing Question

> Does planning long-form, reusable marketing documents and interactive workbooks require a dedicated document-communication specialist, or can the existing report-planning and presentation guidance be generalized?

Key assumptions rejected during scoping:
- The existence of distinct document genres (whitepapers, e-books, workbooks) justifies an independent handbook chapter and routing namespace.
- Delivering output in PDF format or with visual layouts represents a marketing architecture boundary.

## Disposition

```text
STATUS: BOUNDED REPAIR AUTHORIZED — NO NEW SPECIALIST
DEDICATED SPECIALIST / NAMESPACE: NOT JUSTIFIED (REJECTED)
RUNTIME TARGET: skills/marketing-agent-skills/references/report-planning.md (generalized)
MECHANISMS ADDED: Conditional reader work-through chain, artifact use/retrieval contracts
EXPANSIONS REJECTED: document.* namespace, PDF/layout engines, document taxonomy
```

- **Runtime Target**: `skills/marketing-agent-skills/references/report-planning.md` and controller report/artifact triggers.
- **Mechanisms Added**: Generalization from report-centric guidance to multi-modal artifact planning (lookup, comparison, work-through) and workbook action continuity.
- **Expansions Rejected**: Dedicated Document chapter, document taxonomy, PDF layout generator, and graphic design rules.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`00-post-review-disposition.md`](00-post-review-disposition.md) | Frozen adversarial adjudication rejecting specialist chapter and authorizing bounded reference repair | Post-Review Disposition |

Related historical audits & regressions:
- [`../historical-audits/document-artifact-planning-repair.md`](../historical-audits/document-artifact-planning-repair.md)

## Protected Invariants

```text
ARTIFACT NOUN != ACTIVATION AUTHORITY
PDF DELIVERY != CAPABILITY BOUNDARY
WORKBOOK != PROSE + BLANK BOXES
DOCUMENT PLANNING != GENERIC GRAPHIC DESIGN
BRAND IDENTITY != DOCUMENT APPLICATION ARCHITECTURE
```

- An artifact noun (e.g., "whitepaper", "guide") does not authorize activating a new specialist; route according to underlying message, proof, and audience dependencies.
- Chapter 04 owns message, claims, and copy; the generalized report-planning reference owns document information architecture and reader use contracts; Chapter 15 owns persistent brand assets; ordinary tooling owns visual layout and rendering.
