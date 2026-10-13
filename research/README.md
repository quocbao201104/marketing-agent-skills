# Research

`research/` preserves the empirical evidence, theory lineage, review history, rejected hypotheses, repairs, and evaluation records used to decide whether substantive marketing knowledge or runtime mechanisms should enter Marketing Practitioner.

It is **not** an alternate runtime handbook. The installable skill under `skills/marketing-agent-skills/` contains only the operational guidance and machinery that survived the relevant research and review boundary. Research provenance remains outside the distributable package.

## Canonical methodology

The public research process is defined in:

- [`methodology/RESEARCH-METHODOLOGY.md`](methodology/RESEARCH-METHODOLOGY.md) — canonical research method;
- [`methodology/01-post-review-repair.md`](methodology/01-post-review-repair.md) — bounded repair record from the independent methodology review.

The methodology is intentionally separate from `AGENTS.md` and `CONTRIBUTING.md`:

- `AGENTS.md` governs how agents work inside the repository;
- `CONTRIBUTING.md` governs contribution scope, change risk, protected surfaces, and validation expectations;
- `research/methodology/` governs how substantive research is framed, sourced, challenged, synthesized, and promoted.

## How research becomes repository knowledge

A typical substantive path is:

```text
failure / unresolved question / bounded learning objective / credible mechanism
→ map current ownership, state, and routes
→ broad source discovery
→ gap discovery
→ deep value extraction
→ source-scope and inferential-status control
→ triangulation when materially required
→ repository comparison
→ smallest defensible synthesis
→ falsification / counterexample pressure
→ freeze and independent review when material
→ bounded repair and verification
→ runtime/path evaluation when relevant
→ bounded promotion, no change, or rejection
```

The goal is not to maximize research volume. The goal is to improve a real practitioner decision or bounded understanding with the least necessary process and the least powerful mechanism that fixes the demonstrated problem.

A valid research result may therefore be:

- a bounded knowledge correction;
- clarification of an existing owner;
- an evidence requirement;
- a state or handoff correction;
- a routing or discovery fix;
- a scoped adaptation;
- a focused evaluation oracle;
- rejection of a proposed abstraction;
- evidence retained without runtime promotion;
- or **no repository change** (`NO_CHANGE`).

## Research tracks directory

The 28 research tracks are structured across 6 logical clusters:

```text
research/
├── 1. Research Methodology & Evidence Governance (3 tracks)
│   ├── methodology/                          # Canonical research method, falsification pressure, promotion gates
│   ├── evidence-traceability/                # Master map of 233 source IDs across 19 ledgers and 73 review passes
│   └── historical-audits/                    # Archive of 39 unmutated regression suites and smoke walkthroughs
├── 2. Runtime Architecture & Execution Mechanics (6 tracks)
│   ├── runtime-behavioral-clarity/           # Instruction realization clarity (verify ≠ always retrieve again)
│   ├── runtime-design-optimization/          # Multi-step task continuity and retrieved context scoping
│   ├── completion-obligation-reliability/    # Completion accounting and fail-closed behavioral contracts
│   ├── skill-retrieval-and-coverage/         # Top-level skill activation and prompt coverage boundaries
│   ├── cross-artifact-decision-change-repair/# Multi-artifact consistency (Closed: existing primitives sufficient)
│   └── document-artifact-planning/           # Long-form artifact planning (Closed: generalized existing reference)
├── 3. Core Marketing Disciplines & Channel Architectures (8 tracks)
│   ├── brand-identity-and-visual-systems/    # Brand-identifying visual asset realization (Chapter 15)
│   ├── commercial-design/                    # Pricing metric, charge basis, and commercial terms (Chapter 10)
│   ├── copywriting-core/                     # Message hierarchy, argument structure, and copy craft (Chapter 04)
│   ├── founder-led-sales/                    # Buyer-specific sales decision runtime (Chapter 16)
│   ├── landing-page-architecture/            # Page sequence, decision graphs, and reachability (Chapter 11)
│   ├── email-communication-architecture/     # Direct communication and send-state machines (Chapter 12)
│   ├── paid-media-architecture/              # Paid media control semantics and allocation (Chapter 14)
│   └── search-discovery-architecture/        # Search retrieval, entity discovery, and AI citations (Chapter 13)
├── 4. Evaluated Candidate Dispositions & Rejection Records (4 tracks)
│   ├── search-content-intervention/          # Candidate search content edits (Closed: redundant with Ch 13 & 04)
│   ├── performance-informed-content-iteration/# Iterative performance loops (Closed: existing Ch 05/08/04 sufficient)
│   ├── website-content-audit-disposition/    # Site content audit engine (Closed: redundant with existing grammar)
│   └── customer-lifecycle-communication/     # Complex CRM journey builder (Closed: state-conditioned decisions)
├── 5. Linguistic Systems & Locale Adaptation (6 tracks)
│   ├── local-adaptation-extensions/          # Promotion framework and boundaries for localized extensions
│   ├── local-adaptation-japan/               # Japanese keigo honorific registers and relationship distance
│   ├── local-adaptation-korean/              # Korean speech levels (hapsio vs haeyo) and commercial distance
│   ├── local-adaptation-portuguese/          # pt-BR vs pt-PT pronominal address split and clitic placement
│   ├── local-adaptation-spanish/             # Regional Spanish address forms (tuteo vs voseo vs ustedeo)
│   └── local-adaptation-vietnam/             # Vietnamese kinship pronoun address systems and asymmetry
└── 6. Empirical Evaluation & Stateful Simulation (1 track)
    └── stateful-work-episode-evaluation/     # Multi-phase state-mutating work episodes and semantic judges
```

### 1. Research Methodology & Evidence Governance
Foundational specifications governing empirical standards, source traceability, and archival integrity:
- [`methodology/`](methodology/) — Canonical research method, evidence triage, falsification pressure, and bounded repair standards.
- [`evidence-traceability/`](evidence-traceability/) — Master inventory of 233 source IDs across 19 ledgers, paired content audits, and claim clarification closures.
- [`historical-audits/`](historical-audits/) — Archive of 39 targeted regression suites, integration smokes, and adversarial contracts from earlier development milestones.

### 2. Runtime Architecture & Execution Mechanics
Mechanisms controlling instruction realization, task continuity, context extraction, and obligation satisfaction in the runtime controller (`SKILL.md`):
- [`runtime-behavioral-clarity/`](runtime-behavioral-clarity/) — Instruction realization clarity, distinguishing verification from re-retrieval, and resolving action gate ambiguity.
- [`runtime-design-optimization/`](runtime-design-optimization/) — Multi-step task continuity, retrieved handbook context scoping, and work-chain navigation.
- [`completion-obligation-reliability/`](completion-obligation-reliability/) — Fulfillment gates, completion obligations, and fail-closed behavioral contracts.
- [`skill-retrieval-and-coverage/`](skill-retrieval-and-coverage/) — Top-level skill activation, namespace precision, and prompt coverage boundaries.
- [`cross-artifact-decision-change-repair/`](cross-artifact-decision-change-repair/) — Multi-artifact consistency and change propagation (adjudicated as `NO_CHANGE`; existing primitives sufficient).
- [`document-artifact-planning/`](document-artifact-planning/) — Long-form artifact planning (adjudicated as bounded generalization of `references/report-planning.md`; no new specialist).

### 3. Core Marketing Disciplines & Channel Architectures
Theoretical foundations and evidence ledgers for active handbook chapters and JIT routing namespaces:
- [`brand-identity-and-visual-systems/`](brand-identity-and-visual-systems/) — Identity stewardship, distinctive brand assets, and visual decision boundaries (Chapter 15).
- [`commercial-design/`](commercial-design/) — Pricing-metric selection, charge-basis theory, packaging, and commercial terms (Chapter 10).
- [`copywriting-core/`](copywriting-core/) — Message hierarchies, argument structure, claim-evidence coupling, and copy realization (Chapter 04).
- [`founder-led-sales/`](founder-led-sales/) — Founder-led qualification, discovery, pipeline advancement, and sales boundaries (Chapter 16).
- [`landing-page-architecture/`](landing-page-architecture/) — Landing page decision models, conversion architecture, and wireframe semantics (Chapter 11).
- [`email-communication-architecture/`](email-communication-architecture/) — Direct communication architecture, sender posture, and lifecycle triggers (Chapter 12).
- [`paid-media-architecture/`](paid-media-architecture/) — Paid acquisition reasoning, signal health, platform constraints, and campaign architecture (Chapter 14).
- [`search-discovery-architecture/`](search-discovery-architecture/) — Organic search retrieval, search intent, indexation, and discovery architecture (Chapter 13).

### 4. Evaluated Candidate Dispositions & Rejection Records
Candidate hypotheses subjected to independent adversarial review and formally closed with `NO_CHANGE` or `REDUNDANT`:
- [`search-content-intervention/`](search-content-intervention/) — Candidate for search-facing content modifications (closed: redundant with Chapter 13 & 04).
- [`performance-informed-content-iteration/`](performance-informed-content-iteration/) — Candidate for iterative content loops (closed: existing diagnosis and copy primitives sufficient).
- [`website-content-audit-disposition/`](website-content-audit-disposition/) — Candidate for comprehensive site audit engine (closed: redundant with existing controller grammar).
- [`customer-lifecycle-communication/`](customer-lifecycle-communication/) — Candidate for complex CRM/journey builder (closed: state-transition model already handles repeated decisions).

### 5. Linguistic Systems & Locale Adaptation
Linguistic research and sociolinguistic constraints governing cross-border communication and relationship realization under Chapter 07:
- [`local-adaptation-extensions/`](local-adaptation-extensions/) — Governing framework and boundary conditions for locale-specific extensions.
- [`local-adaptation-japan/`](local-adaptation-japan/) — Japanese honorific systems (keigo), relationship realization, and business communication posture.
- [`local-adaptation-korean/`](local-adaptation-korean/) — Korean speech-level realization (hapsio vs. haeyo) and commercial distance.
- [`local-adaptation-portuguese/`](local-adaptation-portuguese/) — Portuguese market differentiation (pt-BR vs. pt-PT addressability and formality).
- [`local-adaptation-spanish/`](local-adaptation-spanish/) — Spanish regional address systems (tuteo, voseo, ustedeo) and localized marketing registers.
- [`local-adaptation-vietnam/`](local-adaptation-vietnam/) — Vietnamese kinship pronoun systems and digital commerce dynamics.

### 6. Empirical Evaluation & Stateful Simulation
Methodology and test harnesses for measuring agent capability in multi-turn, state-mutating environments:
- [`stateful-work-episode-evaluation/`](stateful-work-episode-evaluation/) — Stateful work episode methodology, Episode 01 fixtures, and evidence-grounded semantic judge calibration.

## Research boundaries

Keep these distinctions explicit:

```text
research provenance ≠ runtime instructions
source quantity ≠ evidence quality
source-owned fact ≠ cross-context generalization
formal theory ≠ observed empirical evidence
professional practice ≠ empirical law
external support ≠ project synthesis
interesting mechanism ≠ justified architecture
static knowledge quality ≠ runtime path quality
research activity ≠ requirement to change the repository
```

When sufficient knowledge already exists but is not reliably reached or used, inspect activation, routing, discovery, loading, retrieval boundaries, composition, and handoffs before adding more handbook prose.

When a bounded source-owned fact is directly stated by a current authoritative source, one source may be enough. Triangulate when the conclusion requires synthesis, transfer, causal interpretation, generalization, architecture promotion, or resolution of material disagreement or uncertainty.

## Where to start

For a new substantive research track:

1. read [`methodology/RESEARCH-METHODOLOGY.md`](methodology/RESEARCH-METHODOLOGY.md);
2. use `CONTRIBUTING.md` to determine change risk and implementation boundaries;
3. inspect the current owner, route, state, and relevant existing research before proposing new architecture;
4. create only the research artifacts needed to preserve the material evidence and review lineage.

For ordinary editorial or mechanical changes, do not create a research track merely for ceremony.
