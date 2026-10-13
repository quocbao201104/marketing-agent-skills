# Search and Discovery Architecture Research

Status: **THEORY VERIFIED — BOUNDED RUNTIME INTEGRATED**

This directory preserves the research lineage, theory freeze, mechanical verifications, and adversarial reviews establishing **search retrieval, entity discovery, and AI citation semantics** in Handbook Chapter 13 (`13-search-and-discovery-architecture.md`).

The research addresses the failure where marketing agents treat organic search as a collection of mechanical SEO keyword-stuffing tricks or confuse AI engine answers with guaranteed traffic. Chapter 13 establishes rigorous models for four distinct discovery layers: information need framing, entity availability and crawlability, retrieval selection, and system commitment (citations, snippets, direct answers).

## Governing Question

> How should a practitioner reason about entity discovery, information availability, organic retrieval selection, and AI engine answer grounding without collapsing into keyword manipulation or confusing citations with verified business authority?

Key assumptions rejected during scoping:
- Search optimization is primarily about repeating keyword phrases in headers and meta tags.
- Being cited or referenced by an LLM search engine guarantees referral traffic or brand endorsement.
- Search discovery architecture owns commerce catalog and product ranking (owned by Chapter 09).

## Disposition

```text
STATUS: THEORY VERIFIED & RUNTIME INTEGRATED
RUNTIME TARGET: Handbook Chapter 13 (13-search-and-discovery-architecture.md)
ROUTING NAMESPACE: discovery.* (5 addressable routes)
EVIDENCE LEDGER: references/search-discovery-evidence.md
```

- **Runtime Target**: Handbook Chapter 13 and the `discovery.*` routing namespace.
- **Mechanisms Added**: Need classification, entity availability models, retrieval selection criteria, AI engine commitment boundaries, and citation observation semantics.
- **Expansions Rejected**: Automated keyword density optimizers, black-hat ranking algorithms, and speculative search engine reverse-engineering claims.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-theory-freeze.md`](01-theory-freeze.md) | Comprehensive theory freeze defining availability, retrieval, and AI engine commitment | Theory Freeze |
| [`02-implementation-self-review.md`](02-implementation-self-review.md) | Author audit checking route bindings, evidence ledger linkages, and negative boundaries | Self-Review |
| [`03-mechanical-verification.md`](03-mechanical-verification.md) | Deterministic verification of route resolution and formatting standards | Mechanical Verification |
| [`04-targeted-evaluation-adjudication.md`](04-targeted-evaluation-adjudication.md) | Targeted adjudication evaluating runtime behavior on adversarial search queries | Adjudication |
| [`05-independent-runtime-review-brief.md`](05-independent-runtime-review-brief.md) | Independent review brief examining edge cases in synthetic answers and indexing | Review Brief |
| [`06-review-launch-note.md`](06-review-launch-note.md) | Review launch instructions and evaluation criteria | Review Launch |
| [`07-review-prompt.md`](07-review-prompt.md) | Reviewer prompt specifying adversarial inspection guidelines | Review Prompt |
| [`08-pr-scope-note.md`](08-pr-scope-note.md) | PR scope boundary statement safeguarding chapter non-inflation | Scope Note |
| [`09-release-preparation.md`](09-release-preparation.md) | Release packaging checklist and runtime verification sign-off | Release Preparation |

Related historical audits & regressions:
- [`../historical-audits/search-discovery-architecture-adversarial-cases.md`](../historical-audits/search-discovery-architecture-adversarial-cases.md)
- [`../historical-audits/search-discovery-architecture-runtime-smoke.md`](../historical-audits/search-discovery-architecture-runtime-smoke.md)

## Protected Invariants

```text
AVAILABILITY / SELECTION / COMMITMENT != KEYWORD MANIPULATION
AI CITATION != INDUSTRY AUTHORITY
DISCOVERY AVAILABILITY → Chapter 13
CONTENT / MESSAGE CRAFT → Chapter 04
COMMERCE LISTINGS / CATALOG DISCOVERY → Chapter 09

INDEXED IN SEARCH != SELECTED FOR DIRECT ANSWER
OBSERVED CITATION != CAUSAL REFERRAL TRAFFIC
```

- An indexed page rarely appearing in AI answers requires Chapter 13 for availability/commitment diagnosis; rewrite content only if the failure localizes to message/copy craft.
- Being cited 500 times by an engine does not validate an unearned industry authority claim; Chapter 04 governs substantive claim verification.
- Non-commerce entity discovery is strictly decoupled from commerce marketplace rankings (Chapter 09).
