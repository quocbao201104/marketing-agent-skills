# Completion Obligation Reliability - Reporter and Input Corrections

Review target: `2627afed10236aa87fa8ff43a4476e3a1967d5e4`

## Scope

This follow-up corrects two evaluation defects. Runtime instructions and the six
pair-level sensitivity relations remain unchanged. Earlier adjudications record
their historical corpus versions; this document and the amended regression
contract govern version `1.2.0`.

## Reporter compatibility

All 12 prior members declared `expected_relation = sensitivity`. The case loader
accepted that label, but `build_report` rejected the entire corpus before scoring
any member. Merely moving pair adjudication to Pressure Discovery did not make
the independent legacy report usable.

Version `1.2.0` uses `skill_not_worse` for the legacy reporting boundary. Retain
cross-case sensitivity in the regression contract and adjudicate it separately
through Pressure Discovery. Two member PASS labels do not prove a pair relation.

## COR04 source sufficiency

Both COR04 prompts now contain the same approved source announcement. The private
portal disclosure policy remains unavailable. A still requires completion of the
independent interview synthesis; B still requires recognition that both final
outputs depend on the policy. Optional bounded observations remain optional.

This removes a second, unintended adaptation blocker without changing the
intended difference between the two members.

## Version and provenance

All 12 case identities advance from `1.1.0` to `1.2.0` because the reporting
contract changed; the COR04 prompts also change. Preserve historical results
under their original identities. The corpus provenance will reference the commit
that freezes this amended contract before the revised corpus is committed.

## Verification boundaries

Validate corpus loading, verify the shared COR04 source and intended dependency
difference, and exercise fixture execution followed by legacy reporting. Run the
repository checks before delivery. Fixture results establish infrastructure
compatibility only; semantic acceptability, pair relations, and live behavioral
effect remain unvalidated by those checks.
