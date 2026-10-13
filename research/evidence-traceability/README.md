# Evidence Traceability Research

Status: **RESEARCH COMPLETE — FOUNDATIONAL METHODOLOGY / REPOSITORY GOVERNANCE**

This directory preserves the master evidence traceability mapping, adversarial content reviews, and clarification closures linking empirical marketing claims to source provenance across all 19 reference ledgers and 16 handbook chapters.

It documents the exhaustive audit validating that every substantive claim in the runtime handbook derives from verified empirical literature, established legal/regulatory statutes, or authoritative platform developer specifications, while ensuring that evidence boundaries and negative inferences are faithfully represented.

## Governing Question

> How is every factual, causal, and architectural claim in the practitioner runtime mapped to verifiable empirical provenance without conflating source citation with runtime authorization?

Key assumptions rejected during scoping:
- Citing an authoritative paper justifies unconstrained runtime application beyond the study's explicit domain boundary.
- Platform vendor marketing claims constitute reliable empirical evidence for algorithmic behavior.

## Disposition

```text
STATUS: FOUNDATIONAL EVIDENCE LEDGER AUDIT
INVENTORY: 233 Source IDs across 19 Evidence Ledgers
TOTAL AUDIT PASSES: 73 Sequential Review and Clarification Closures
RUNTIME TARGET: skills/marketing-agent-skills/references/* and get-knowledge.py --source
```

- **Runtime Target**: 19 reference evidence ledgers under `skills/marketing-agent-skills/references/` and the source retrieval index in `scripts/get-knowledge.py`.
- **Mechanisms Added**: Exact source-to-claim mapping, explicit evidence boundaries (`Supported vs Not Supported`), and JIT source retrieval CLI (`--source <source-id>`).
- **Expansions Rejected**: Secondary marketing blog citations, vendor promotional whitepapers without methodology, and unreplicable anecdotal claims.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`source-inventory.json`](source-inventory.json) | Machine-readable master index of 233 source IDs, metadata, and ledger bindings | Master Inventory |
| [`01-evidence-traceability-map.md`](01-evidence-traceability-map.md) | Architectural roadmap of evidence coverage across handbook chapters 01–16 | Master Map |
| [`02`–`34` Series] | Paired content review and clarification closures for Chapters 01–15 | Chapter Audits |
| [`35-audit-synthesis-and-research-priorities.md`](35-audit-synthesis-and-research-priorities.md) | Mid-point audit synthesis establishing empirical gaps and priority repairs | Audit Synthesis |
| [`36`–`43` Series] | Observational causal inference and Google Commerce / conversational audits | Channel Audits |
| [`44-audit-coverage-and-next-priorities.md`](44-audit-coverage-and-next-priorities.md) | Second-stage audit coverage evaluation across tasks and platforms | Audit Synthesis |
| [`45`–`50` Series] | Task guide standardization, localization sources, and pricing-metric evidence reviews | Specialized Audits |
| [`51-conditional-subagent-coordination-design.md`](51-conditional-subagent-coordination-design.md) | Architecture review of conditional subagent delegation invariants | Architectural Pass |
| [`52`–`73` Series] | Platform-specific empirical audits (Amazon, TikTok Shop, Shopee, LinkedIn, Community) | Platform Audits |

## Protected Invariants

```text
SOURCE PROVENANCE != RUNTIME RULE
A SOURCE ESTABLISHES EVIDENCE, NOT AN AUTOMATIC RUNTIME MANDATE
CORRELATION != CAUSATION
ATTRIBUTION != INCREMENTALITY
QUALITATIVE RECURRENCE != POPULATION PREVALENCE
STATING WILLINGNESS-TO-PAY != OPTIMAL SUSTAINABLE PRICE
```

- A source ID verifies provenance for an empirical claim; it does not grant permission to bypass runtime decision gates.
- Every evidence entry must document both what the cited source demonstrates and what it fails to demonstrate.
- Evidence scope (geography, sample population, platform version, and time period) must remain strictly bound.
