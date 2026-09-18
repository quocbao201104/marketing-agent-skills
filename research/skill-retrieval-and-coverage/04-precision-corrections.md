# Skill Retrieval and Coverage - Precision Corrections

Review target: `30c70c268808f7b8e027c75675255630ddcd22bf`.

## Disposition and scope

This amendment supersedes the route-count interpretation of semantic coverage in
sections 10-12 of the original design freeze and the corresponding conclusions
in the implementation review. The original records remain historical provenance.
No live-model improvement is claimed. Activation cases, description variants,
logical routes and owner taxonomy are retained.

## Demonstrated failures

1. A completed run with only some required route groups was classified as
   `premature_closure` whether its independent answer judgment was pass, fail or
   absent. The trace cannot establish whether a question was resolved using
   context, legitimately excluded, bounded, or awaiting user input.
2. All 12 coverage cases had empty semantic review criteria and only an
   `output_present` predicate. The legacy reporter accepted an unjudged `OK.` as
   PASS. This cannot measure decision coverage.
3. FAST-001 and FAST-002 requested transformations without supplying their source
   text, making a correct input request look like a fast-path failure.

## Bounded runtime correction

A surface is now explicitly a concrete question or dependency supported by
context, evidence or requested scope, judged using the existing materiality rule.
Coverage is not a checklist of marketing domains. The stopping condition applies
expected decision or learning value and inquiry cost before requiring exhaustive
resolution, while preserving unknowns and identifying truly blocked outcomes.
The existing reopening exceptions and action authority remain unchanged.

## Evaluation correction

- Trace schema v3 uses `partial_route_coverage` for the mechanical observation.
  Historical route counts remain usable as retrieval telemetry, not as a semantic
  failure rate. Existing route-oracle schemas need no expansion.
- Coverage cases advance to v1.1.0 with semantic criteria and both missing source
  artifacts. The matching route oracle allows relevant reads instead of requiring
  all anticipated owners or a fixed read order.
- A separate evaluator surface oracle asks task-specific questions. An independent
  blind judgment records resolution, justified exclusion, bounded uncertainty,
  unresolved material uncertainty, or insufficient assessment evidence.
- The `coverage` CLI binds judgments through the sealed blind index and answer
  hash, validates source quotations and surface identities, and reports missing
  judgments as unresolved. It neither infers correctness from route counts nor
  accepts executor claims as independent review.
- A returned turn awaiting necessary input is not task completion. Only a claimed
  complete result with a still-unresolved material dependency establishes
  `premature_closure`. Route reads cannot make that dependency disappear.

See `evals/behavioral/README.md` for the judgment schema and execution command.
These are offline evaluation records, not mandatory runtime state or output.

## Verification scope

Targeted tests cover sufficient supplied evidence without reads, full reads with
an unresolved dependency, bounded completion, legitimate input requests,
unassessable judgments, stale answer bindings, missing/extra surfaces, invalid
quotes, operational failures and the legacy nonempty-answer false-pass path.
Fixture execution tests infrastructure only. Live activation and coverage effects
remain unmeasured; merge readiness does not promote an empirical improvement claim.
