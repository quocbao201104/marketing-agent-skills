# External Review Follow-up — Verification vs Retrieval

Date: 2026-09-18

Prior merged static candidate: `f075d7073c3f881edb7c39e69a1c38b136a6e4ee`

## Review disposition

The external review agreed with the bounded `material` and JIT-verification repairs, while identifying one residual instruction-realization ambiguity:

```text
VERIFY CURRENT STATE
!=
ALWAYS RETRIEVE AGAIN
```

The prior controller specified when a material external fact requires current verification, but did not state directly that sufficiently current, scoped evidence already available in context can satisfy that verification requirement.

That omission could support an unnecessary-retrieval reading even though the surrounding runtime already prefers direct execution when supplied evidence is sufficient.

## Bounded follow-up repair

The evidence safeguard now states:

```text
Use sufficiently current, scoped evidence already available;
retrieve again only when freshness, applicability, or support remains unresolved.
```

This makes the intended execution relation explicit:

```text
verification requirement
→ inspect available evidence for currentness + scope + support
→ reuse it when sufficient
→ retrieve only if a material verification dependency remains unresolved
```

The repair does not weaken freshness requirements. Older authoritative evidence does not become current merely because it is authoritative.

The repair also does not create a mandatory retrieval step for every provider-controlled or time-sensitive fact. Retrieval is a means of resolving verification, not the definition of verification itself.

## Closure semantics

`F01 CLOSED` and `F02 CLOSED` mean the **identified static instruction-realization defects have been repaired**.

They do not mean:

- every possible reasoning path is proven behaviorally stable;
- live models have been shown never to misapply the rule;
- current wording has been proven superior on production workloads.

Execution stability remains a real-task validation question under `05-real-task-validation-brief.md`.

## Architecture impact

None.

No owner, route, precedence rule, workflow stage, domain model, or retrieval subsystem was added.
