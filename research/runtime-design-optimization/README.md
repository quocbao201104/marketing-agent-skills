# Runtime Design Optimization Research

Status: **THEORY VERIFIED — STATIC RUNTIME INTEGRATED**

This directory preserves the research lineage, structural reviews, and multi-step task continuity designs optimizing the runtime controller (`SKILL.md`) and retrieved handbook context scoping.

The track focuses on improving agent reasoning across complex work chains: ensuring that upstream decisions remain settled, preventing context explosion through minimal addressable retrieval, and maintaining coherent task continuity across multi-step marketing operations.

## Governing Question

> How can the runtime controller optimize agent multi-step task continuity and scope retrieved handbook context to the smallest decision-changing section without introducing speculative abstractions or losing execution rigor?

Key assumptions rejected during scoping:
- Better agent performance requires providing the full handbook upfront in context.
- Multi-step tasks require a complex state-machine orchestrator rather than clean decision-dependency handoffs.

## Disposition

```text
STATUS: INTEGRATED INTO RUNTIME CONTROLLER
RUNTIME TARGET: skills/marketing-agent-skills/SKILL.md & routing mechanics
MECHANISMS ADDED: Work-chain navigation, smallest addressable section retrieval, and settled-state retention
```

- **Runtime Target**: `skills/marketing-agent-skills/SKILL.md` (task lifecycle, decision preservation, and routing clauses).
- **Mechanisms Added**: Multi-step task continuity principles, precise section-level context retrieval, and explicit work-chain handoffs.
- **Expansions Rejected**: Monolithic prompt expansions, heavy stateful graph frameworks, and automated task-looping daemons.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-design-review.md`](01-design-review.md) | Initial architectural audit evaluating context bloat and multi-step degradation | Design Review |
| [`02-core-organization-and-quality-design.md`](02-core-organization-and-quality-design.md) | Core organization specifications and qualitative execution benchmarks | Architecture Design |
| [`03-multi-step-task-continuity.md`](03-multi-step-task-continuity.md) | Protocols for preserving settled choices across multi-turn work episodes | Continuity Design |
| [`04-retrieved-handbook-context.md`](04-retrieved-handbook-context.md) | Context-scoping mechanisms and minimum-sufficient section boundary specifications | Scoping Design |
| [`05-index-discovery-and-work-chains.md`](05-index-discovery-and-work-chains.md) | Index discovery mechanics, routing lookup, and sequential work-chain linking | Work Chains |

## Protected Invariants

```text
PRESERVE SETTLED STATE != REOPEN CHOICES FOR STYLE
TASK CONTINUITY != FULL CONTEXT DUMP
SMALLEST USEFUL SECTION != WHOLE CHAPTER
OBSERVATION ≠ INTERPRETATION ≠ HYPOTHESIS ≠ DECISION
```

- Completed and accepted upstream choices must not be reopened merely to improve them.
- Retrieve only when specialist knowledge can materially change an open decision surface.
- Unresolved dependencies must be resolved through explicit practitioner handoffs rather than speculative inference.
