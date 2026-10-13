# Skill Retrieval and Coverage Research

Status: **THEORY VERIFIED — STATIC RUNTIME INTEGRATED**

This directory preserves the research lineage, activation study protocols, and precision corrections governing **top-level skill activation, prompt coverage, and namespace retrieval boundaries**.

The track resolves the tension between under-activation (failing to load the practitioner skill on legitimate, nuanced marketing decision tasks) and over-activation / routing leakage (triggering specialist routing on superficial keyword mentions or treating platform names as automatic reasons to load platform modules).

## Governing Question

> How can the skill controller and routing manifest maximize activation fidelity on genuine marketing decision tasks while maintaining strict precision against keyword traps and superficial topic matches?

Key assumptions rejected during scoping:
- Mentioning a platform name (e.g., "Facebook", "Amazon") is sufficient reason to load that platform's specialist module.
- The marketing skill should activate as a universal conversational assistant for any business query.

## Disposition

```text
STATUS: INTEGRATED INTO RUNTIME CONTROLLER & ROUTING INDEX
RUNTIME TARGET: skills/marketing-agent-skills/SKILL.md & routing-index.json
EVALUATION CORPUS: evals/behavioral/cases/coverage-routing-v1.json
REGRESSION SUITE: evals/behavioral/cases/skill-activation-v1.json
```

- **Runtime Target**: `skills/marketing-agent-skills/SKILL.md` (activation triggers, job boundaries) and `routing-index.json`.
- **Mechanisms Added**: Decision-dependency routing criteria, negative boundary triggers, and precise prompt-coverage calibration.
- **Expansions Rejected**: Generic keyword-matching heuristics, unbounded semantic search embeddings, and automatic platform takeovers.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-design-freeze.md`](01-design-freeze.md) | Original design freeze for skill activation conditions and route coverage boundaries | Design Freeze |
| [`02-activation-study-protocol.md`](02-activation-study-protocol.md) | Empirical protocol for testing model activation across ambiguous and adversarial prompts | Study Protocol |
| [`03-implementation-review.md`](03-implementation-review.md) | Audit evaluating runtime routing accuracy, false positive rates, and prompt leakage | Implementation Review |
| [`04-precision-corrections.md`](04-precision-corrections.md) | Bounded precision repairs eliminating keyword over-routing and reinforcing negative boundaries | Precision Corrections |

Related historical audits & regressions:
- [`../historical-audits/knowledge-routing-v0.1-smoke.md`](../historical-audits/knowledge-routing-v0.1-smoke.md)
- [`../historical-audits/intake-resolution-boundary-regressions.md`](../historical-audits/intake-resolution-boundary-regressions.md)

## Protected Invariants

```text
PLATFORM NAME != REASON TO LOAD THAT PLATFORM
TOPIC KEYWORD != DECISION DEPENDENCY
ARTIFACT NOUN != ACTIVATION AUTHORITY
RESOLVED STATE DIRECTLY SUFFICIENT → DO NOT ROUTE
OPEN DECISION SURFACE REQUIRES SPECIALIST → ROUTE BY DECISION NEED
```

- Route by decision dependency, never by platform name, topic keyword, or artifact noun.
- If supplied state is sufficient to make the decision, execute directly without external routing.
- The skill activates only for marketing decision surfaces; general programming, administrative, or unrelated business queries must not trigger marketing specialist paths.
