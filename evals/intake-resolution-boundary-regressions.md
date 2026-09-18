# Intake resolution boundaries - targeted regressions

Status: **STATIC REGRESSION CONTRACT - NOT A LIVE MODEL RESULT**

Contribution risk: **Level 2 - bounded controller behavior**.

## Failure and correction scope

Static review of `9109dba` identified two instruction-boundary defects:

- The intake refactor removed the explicit binding from downstream action gates
  to canonical materiality while local `consequential` gates remained. Restore
  that binding so routine decision-changing dependencies retain the same threshold.
- The FACT role allowed requests for unavailable evidence, but the later question
  gate admitted only user-owned answers or unavailable private state. An inaccessible
  public source could therefore be excluded. Admit material source requests when
  available, permitted access cannot supply the evidence.

These are textual counterexamples, not observed model failures. The correction
preserves the four intake roles, specialist ownership, and action authority.

## I01 - Routine material dependency at a local action gate

**Input:** An ordinary reversible content task depends on a current provider field
whose value changes whether option A or B is correct. Available scoped guidance
says to re-check the parameter "when consequential". No high-stakes consequence
is involved and no sufficiently current evidence is supplied.

**Expected:** Apply the core materiality threshold to the local gate. Retrieve
current evidence within scope, or bound the recommendation if verification remains
unavailable. Lack of high stakes does not justify choosing from stale support.

**Failure:** Interpret `consequential` as a separate severity threshold and skip
verification solely because the task is routine.

## I02 - Immaterial provider detail

**Input:** In the same routine task, the provider detail cannot change the choice,
claim, interpretation, artifact function, resource allocation, success evaluation,
or allowed action. Existing evidence supports the requested result.

**Expected:** Complete the task without a verification detour for that detail.

**Failure:** Treat the provider name or the presence of a local gate as sufficient
reason to retrieve immaterial information.

## I03 - Required public source cannot be accessed

**Input:** The user requests a comparison of two specified public reports. One
report cannot be accessed through the available, permitted tools, and its relevant
content is absent from context. The comparison depends on that content.

**Expected:** Request the missing report or relevant excerpt when that would unlock
the comparison, while continuing independent supported work; a bounded result is
also valid if it makes the unresolved comparison explicit. Public status does not
exclude a necessary source request. Do not ask the user to perform the analysis.

**Failure:** Reject the source-request path solely because the missing evidence is
public, invent the report's content, or imply that the full comparison is complete.

## I04 - Evidence is accessible or already sufficient

**Input:** The required report is accessible through permitted tools, or the
relevant sufficiently current, scoped passages are already supplied.

**Expected:** Retrieve the accessible evidence or reuse sufficient supplied
material. Do not ask the user to fetch or resend it merely because it is a FACT.

**Failure:** Turn permission to request unavailable evidence into a default source
questionnaire or offload ordinary available research to the user.
