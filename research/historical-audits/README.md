# Historical Audits Research

Status: **HISTORICAL ARCHIVE — UNMUTATED EVALUATION CONTRACTS**

This directory preserves 39 historical regression contracts, targeted integration smoke suites, adversarial walkthroughs, and post-review repair verifications executed across earlier development milestones of Marketing Agent Skills.

These files serve as **immutable regression oracles and provenance witnesses**. They capture the exact falsification pressure, edge cases, and boundary validations that forced each runtime chapter, JIT route namespace, and controller safeguard into its current bounded form.

## Governing Question

> What historical edge cases, adversarial tests, and integration smoke walkthroughs validated the runtime capabilities during development, and how do they map to current handbook chapters and specialist routes?

Key assumptions rejected during scoping:
- Development smoke tests and audit walkthroughs should be deleted after merging PRs.
- Historical evaluation contracts can be mutated to match subsequent stylistic preferences without re-running verification.

## Disposition

```text
STATUS: HISTORICAL REGRESSION ARCHIVE
TOTAL ARTIFACTS: 39 Unmutated Evaluation Contracts & Smoke Suites
ROLE: Long-term provenance witnesses & regression oracles
RUNTIME STATUS: Immutable historical records (Do not modify contents)
```

## Master Cross-Reference Mapping Matrix

The table below maps all 39 historical audit artifacts to their governing research tracks, artifact types, and target runtime chapters:

| Historical Audit Artifact | Governing Track / Subsystem | Artifact Type | Target Runtime / Chapter / Route | Milestone Status & Invariant |
| :--- | :--- | :--- | :--- | :--- |
| [`brand-identity-and-visual-systems-adversarial-cases.md`](brand-identity-and-visual-systems-adversarial-cases.md) | `brand-identity-and-visual-systems` | Candidate Eval Contract | Chapter 15 / `brand-identity.*` | Tests identity stewardship vs. general graphic design. |
| [`brand-identity-and-visual-systems-runtime-smoke.md`](brand-identity-and-visual-systems-runtime-smoke.md) | `brand-identity-and-visual-systems` | Targeted Walkthrough | Chapter 15 / `brand-identity.*` | Author semantic walkthrough checking route activation. |
| [`brand-identity-input-sufficiency-regressions.md`](brand-identity-input-sufficiency-regressions.md) | `brand-identity-and-visual-systems` | Regression Contract | Chapter 15 / `brand-identity.*` | Input sufficiency ≠ live image generation execution. |
| [`commerce-agentic-frontier-audit.md`](commerce-agentic-frontier-audit.md) | `evidence-traceability` (Commerce) | Adversarial Audit | Chapter 09 / `references/commerce/` | Agentic commerce boundaries vs. platform catalog state. |
| [`commerce-agentic-frontier-runtime-smoke.md`](commerce-agentic-frontier-runtime-smoke.md) | `evidence-traceability` (Commerce) | Integration Smoke | Chapter 09 / `references/commerce/` | Platform state mutations vs. agent commercial reasoning. |
| [`commerce-ai-native-product-discovery-targeted-pass.md`](commerce-ai-native-product-discovery-targeted-pass.md) | `evidence-traceability` (Commerce) | Practitioner Pass | Chapter 09 / Conversational discovery | Conversational product discovery; intent matching vs. ranking. |
| [`commerce-environment-adversarial-audit.md`](commerce-environment-adversarial-audit.md) | `evidence-traceability` (Commerce) | Adversarial Audit | Chapter 09 (Commerce Environments) | Core commerce architecture adversarial audit. |
| [`commerce-etsy-query-matching-source-conflict-correction.md`](commerce-etsy-query-matching-source-conflict-correction.md) | `evidence-traceability` (Commerce) | Post-Review Correction | Chapter 09 / `etsy-evidence.md` | Etsy query-matching correction resolving source conflict. |
| [`commerce-runtime-routing-smoke.md`](commerce-runtime-routing-smoke.md) | `evidence-traceability` (Commerce) | Routing Smoke | Chapter 09 / Commerce routing | Validates commerce runtime routing and platform isolation. |
| [`commercial-design-runtime-routing-smoke.md`](commercial-design-runtime-routing-smoke.md) | `commercial-design` | Integration Smoke | Chapter 10 / `commercial-design.*` | Post-PR #12 routing smoke; checks over/under-routing boundaries. |
| [`conditional-core-refactor-audit.md`](conditional-core-refactor-audit.md) | `runtime-design-optimization` | Static Architecture Audit | `SKILL.md` / Core Controller | Base v1.9.2 refactor audit; static design and migration mapping. |
| [`content-environment-losslessness-audit.md`](content-environment-losslessness-audit.md) | `copywriting-core` | Losslessness Audit | Chapter 04 / Content Core | Verifies compact-core content refactor loses no expressive power. |
| [`cross-layer-promotion-regressions.md`](cross-layer-promotion-regressions.md) | `completion-obligation-reliability` | Regression Contract | Controller / Chapter handoffs | Cross-layer promotion regressions; prevents premature promotion. |
| [`cross-layer-role-reasoning-audit.md`](cross-layer-role-reasoning-audit.md) | `runtime-behavioral-clarity` | Static Reasoning Audit | Controller role steering | Multi-role reasoning audit; ensures role boundaries remain distinct. |
| [`decision-local-role-steering-regressions.md`](decision-local-role-steering-regressions.md) | `runtime-behavioral-clarity` | Regression Contract | Controller role steering | Decision-local role steering regressions. |
| [`document-artifact-planning-repair.md`](document-artifact-planning-repair.md) | `document-artifact-planning` | Regression Cases | Reference: `report-planning.md` | Validates bounded repair of artifact planning guidance. |
| [`email-communication-architecture-adversarial-cases.md`](email-communication-architecture-adversarial-cases.md) | `email-communication-architecture` | Adversarial Contract | Chapter 12 / `email-communication.*` | Email decision architecture adversarial test cases. |
| [`email-communication-architecture-runtime-smoke.md`](email-communication-architecture-runtime-smoke.md) | `email-communication-architecture` | Runtime Smoke | Chapter 12 / `email-communication.*` | Post-freeze runtime walkthrough for email communication. |
| [`founder-led-sales-release-190-regressions.md`](founder-led-sales-release-190-regressions.md) | `founder-led-sales` | Regression Suite | Chapter 16 / `founder-sales.*` | Release 1.9.0 bounded repair regressions for founder-led sales. |
| [`intake-resolution-boundary-regressions.md`](intake-resolution-boundary-regressions.md) | `runtime-behavioral-clarity` | Regression Contract | Controller / Intake Gate | Intake boundary regressions; resolved state must not reopen. |
| [`knowledge-routing-v0.1-smoke.md`](knowledge-routing-v0.1-smoke.md) | `skill-retrieval-and-coverage` | Architecture Smoke | `scripts/get-knowledge.py` | Early knowledge routing index v0.1 smoke test suite. |
| [`landing-page-architecture-adversarial-cases.md`](landing-page-architecture-adversarial-cases.md) | `landing-page-architecture` | Adversarial Contract | Chapter 11 / `landing-page.*` | Landing-page conversion and structure adversarial test cases. |
| [`local-adaptation-japan-v0.md`](local-adaptation-japan-v0.md) | `local-adaptation-japan` | Pressure Test Suite v0 | Reference: `local-adaptation.md` | Japanese relationship realization and honorific registers. |
| [`local-adaptation-korean-v0.md`](local-adaptation-korean-v0.md) | `local-adaptation-korean` | Pressure Test Suite v0 | Reference: `local-adaptation.md` | Korean speech-level realization and pragmatic distance. |
| [`local-adaptation-portuguese-v0.md`](local-adaptation-portuguese-v0.md) | `local-adaptation-portuguese` | Pressure Test Suite v0 | Reference: `local-adaptation.md` | Portuguese localization; pt-BR vs. pt-PT addressability. |
| [`local-adaptation-spanish-v0.md`](local-adaptation-spanish-v0.md) | `local-adaptation-spanish` | Pressure Test Suite v0 | Reference: `local-adaptation.md` | Spanish regional address forms (tuteo, voseo, ustedeo). |
| [`local-adaptation-vn-language-v0.md`](local-adaptation-vn-language-v0.md) | `local-adaptation-vietnam` | Pressure Test Suite v0 | Reference: `local-adaptation.md` | Vietnamese relationship realization and kinship pronoun logic. |
| [`paid-media-architecture-adversarial-cases.md`](paid-media-architecture-adversarial-cases.md) | `paid-media-architecture` | Candidate Eval Contract | Chapter 14 / `paid-media.*` | Paid media decision reasoning adversarial test cases. |
| [`paid-media-architecture-review-regression.md`](paid-media-architecture-review-regression.md) | `paid-media-architecture` | Review Regression | Chapter 14 / `paid-media.*` | Post-independent-review local correction regression suite. |
| [`paid-media-architecture-runtime-smoke.md`](paid-media-architecture-runtime-smoke.md) | `paid-media-architecture` | Runtime Walkthrough | Chapter 14 / `paid-media.*` | Targeted runtime walkthrough for paid media architecture. |
| [`prebenchmark-runtime-smoke.md`](prebenchmark-runtime-smoke.md) | `stateful-work-episode-evaluation` | Execution Pack | Runtime Platform / Controller | Pre-benchmark platform runtime smoke pack. |
| [`pricing-metric-selection-bounded-cases.md`](pricing-metric-selection-bounded-cases.md) | `commercial-design` | Implementation Eval | Chapter 10 / `commercial-design.payment` | Bounded Chapter 10 pricing-metric / charge-basis eval cases. |
| [`runtime-adversarial-walkthrough.md`](runtime-adversarial-walkthrough.md) | `runtime-behavioral-clarity` | Static Runtime Audit | Controller / Operating Guide | Platform runtime adversarial walkthrough. |
| [`runtime-controller-refinement-audit.md`](runtime-controller-refinement-audit.md) | `runtime-behavioral-clarity` | Architecture Audit | Controller / JIT routes | Runtime controller refinement and activation audit. |
| [`runtime-guidance-clarity-audit.md`](runtime-guidance-clarity-audit.md) | `runtime-behavioral-clarity` | Regression Contract | Controller / JIT verification | Guidance clarity audit and regression contract. |
| [`search-content-intervention-adversarial-cases.md`](search-content-intervention-adversarial-cases.md) | `search-content-intervention` | Candidate Eval Suite | Chapter 13 / Content modifications | Post-review repair eval suite for rejected search intervention. |
| [`search-discovery-architecture-adversarial-cases.md`](search-discovery-architecture-adversarial-cases.md) | `search-discovery-architecture` | Candidate Eval Contract | Chapter 13 / `search-discovery.*` | Search and discovery architecture adversarial test cases. |
| [`search-discovery-architecture-runtime-smoke.md`](search-discovery-architecture-runtime-smoke.md) | `search-discovery-architecture` | Runtime Walkthrough | Chapter 13 / `search-discovery.*` | Candidate self-runtime walkthrough for search & discovery. |
| [`subagent-coordination-bounded-cases.md`](subagent-coordination-bounded-cases.md) | `completion-obligation-reliability` | Static Design Cases | `references/work-coordination.md` | Conditional subagent delegation cases and invariant bounds. |

## Protected Invariants

```text
HISTORICAL ARTIFACT = IMMUTABLE PROVENANCE WITNESS
DO NOT RE-RUN TO RETROFIT NEW STYLES
EVALUATION CONTRACTS REMAIN SEALED
ALL AUDITS GROUND RUNTIME CLAIMS TO CONCRETE VERIFICATION
```
