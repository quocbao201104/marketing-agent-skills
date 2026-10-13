# Founder-Led Sales Research

Status: **THEORY VERIFIED — BOUNDED RUNTIME INTEGRATED**

This directory preserves the research lineage, runtime contracts, bounded evaluation records, and post-repair verifications establishing the **buyer-specific commercial decision runtime** in Handbook Chapter 16 (`16-founder-led-sales-decision-runtime.md`).

The research addresses the failure where marketing agents conflate market-wide commercial design (Chapter 10) with bilateral account-specific sales interactions. Chapter 16 establishes a rigorous decision runtime across 8 sequential account stages (FS1–FS8: Pursuit Allocation, Account Selection, Multi-Stakeholder Access, Discovery & Diagnosis, Solution Proof, Decision Enablement, Commercial Commitment, and Evidence-Backed Progression).

## Governing Question

> Given a specific Account × Buying Situation, how should a founder or practitioner allocate pursuit resources, diagnose organizational problems, prove solutions, and enable buyer decision consensus without mistaking seller activity or positive conversational sentiment for genuine commercial commitment?

Key assumptions rejected during scoping:
- Sales is merely copywriting delivered through direct messages or conversational email.
- Positive buyer sentiment or enthusiasm is equivalent to organizational consensus and purchase commitment.
- More seller follow-ups automatically accelerate deal progression.

## Disposition

```text
STATUS: THEORY VERIFIED & BOUNDED RUNTIME INTEGRATED
RUNTIME TARGET: Handbook Chapter 16 (16-founder-led-sales-decision-runtime.md)
ROUTING NAMESPACE: founder-sales.* (8 addressable stages FS1–FS8)
EVIDENCE LEDGER: references/founder-led-sales-evidence.md
REGRESSION CORPUS: evals/behavioral/cases/founder-led-sales-runtime-v1.json
```

- **Runtime Target**: Handbook Chapter 16 and the `founder-sales.*` routing namespace.
- **Mechanisms Added**: Resource-allocation gating (FS1), stakeholder map access (FS3), proof boundary enforcement (FS5), decision enablement matrices (FS6), and progress audit invariants (FS8).
- **Expansions Rejected**: Automated high-volume spam cadence generators, aggressive psychological manipulation tricks, and enterprise CRM software mechanics.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-cross-fs-synthesis.md`](01-cross-fs-synthesis.md) | Theoretical foundation distinguishing buyer-specific sales decisions from market positioning | Research Synthesis |
| [`02-runtime-contract.md`](02-runtime-contract.md) | Formal runtime specification defining states, gates, and handoffs across FS1–FS8 stages | Runtime Contract |
| [`03-runtime-evaluation-brief.md`](03-runtime-evaluation-brief.md) | Adversarial evaluation methodology for testing agent sales decision stability | Evaluation Brief |
| [`04-implementation-self-review.md`](04-implementation-self-review.md) | Author audit checking route bindings, boundary enforcement, and chapter structure | Self-Review |
| [`05-independent-implementation-review-brief.md`](05-independent-implementation-review-brief.md) | Independent review brief examining failure modes and edge cases in B2B qualification | Review Brief |
| [`06-local-repair-record.md`](06-local-repair-record.md) | Bounded repairs addressing independent review findings on customer proof boundaries | Repair Record |
| [`07-post-repair-verification-brief.md`](07-post-repair-verification-brief.md) | Verification specification for certifying repaired Chapter 16 behavior | Verification Brief |
| [`08-bounded-runtime-path-evaluation.md`](08-bounded-runtime-path-evaluation.md) | Empirical execution report evaluating model performance on sales decision gates | Evaluation Report |
| [`09-runtime-evaluation-preflight-record.md`](09-runtime-evaluation-preflight-record.md) | Deterministic preflight validation of behavioral test cases and profile bindings | Preflight Record |
| [`10-post-repair-verification-result.md`](10-post-repair-verification-result.md) | Final independent closure certificate verifying complete runtime integration | Verification Result |

Related historical audits & regressions:
- [`../historical-audits/founder-led-sales-release-190-regressions.md`](../historical-audits/founder-led-sales-release-190-regressions.md)

## Protected Invariants

```text
MARKET / ICP / POSITIONING / DEFAULT COMMERCIAL SYSTEM
→ Upstream owners (Chapters 01, 02, 03, 10)

SPECIFIC Account × Buying Situation + UNRESOLVED SALES DECISION
→ Chapter 16 (founder-sales.*)

RESOLVED SALES DECISION + WORDING / EXPRESSION OPEN
→ Chapter 04 (copywriting.*)

COMMERCIAL DESIGN != BUYER-SPECIFIC COMMERCIAL NEGOTIATION / COMMITMENT
POSITIVE SENTIMENT != CONSENSUS / PURCHASE COMMITMENT
SELLER ACTIVITY != BUYER PROGRESSION
WAITING ON BUYER MILESTONE != INVENTED SELLER NOISE
```

- Commercial design (Chapter 10) establishes the default economic model; Chapter 16 governs bilateral negotiations and exceptions for specific accounts.
- If the customer's legal or evaluation team owns the next dated step and requires nothing from the seller, waiting is correct; do not invent unnecessary seller activity.
- Positive conversational sentiment must never be recorded as purchase commitment without formal consensus and commercial sign-off.
