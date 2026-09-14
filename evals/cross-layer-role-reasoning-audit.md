# Cross-layer role reasoning audit

Status: **STATIC REASONING AUDIT - NO LIVE BEHAVIORAL RESULT**

## Scope and evidence boundary

Reviewed base: `189afbc821a2b14c6c315c664ae8f31b9898bf89`, plus the current uncommitted Chapter 04/12 clarifications and S03/S04 extensions. These working-tree changes are part of the reviewed material, not a separately frozen release.

This audit constructs three counterexamples and legitimate controls. The candidate outputs and rationales below are synthetic illustrations, not observed model transcripts. No subagents or live model trials were used for this audit. It does not establish failure frequency, internal generation order, or causal benefit from any proposed clarification.

The cases distinguish missing knowledge from misapplication of existing guidance. A plausible failure that already contradicts the controller is not evidence that a new architecture is necessary.

## R01 - A candidate does not establish its own exception

**Input / task:** An initial pendant is positioned as a quiet, personal detail for everyday wear. Its verified letter height is approximately 7.4 mm. The PDP needs a size disclosure because its photographs can make scale unclear. The separate requested email is a general reintroduction for subscribers; no size-specific recipient question is recorded. Its general job is retained.

**Current representation / route:** Controller decision-local role steering, source fidelity, and uncertainty handling; Chapter 04 expression and persuasion guidance; `email.send-decision` and `email.allocation` only if those decisions remain open.

**Synthetic failure:** The agent proposes a size-led email campaign premise, then reasons that subscribers must be worried about size and calls the email a size-reassurance touchpoint. It uses this inferred job to authorize the premise.

**Why it changes the decision:** A representation defect on the PDP supports disclosure there. It does not establish the email recipients' concern or authorize replacing the retained general email job. The justification depends on the candidate it is supposed to assess.

**Expected disposition:** Keep the disclosure repair. Do not treat the inferred concern as established audience state. Complete the general email within its retained job, with size included only at the role warranted by that job. A plausible concern can remain a hypothesis; it does not need to be erased or converted into a required research task.

**Legitimate controls:**

- A recipient explicitly asks how tall the letter is. A size-led response performs the established local job without changing campaign positioning.
- The user delegates selection of an educational email topic. The agent may choose a scale explanation as a bounded editorial decision without asserting that subscribers are known to fear size mismatch or that size is the product's primary value.
- A draft reveals a previously unnoticed factual dependency. The agent may investigate it and revise the affected decision when evidence warrants; discovering a question during drafting is not itself circular reasoning.

**Existing protection:** The controller forbids silently assumed facts and separates hypotheses from decisions. Chapter 04 persuasion rejects inferred psychological state without evidence, and its angle guidance forbids manufacturing the demand required to validate a creative route.

**Smallest candidate clarification:** At an existing role check, distinguish an established fact, a warranted inference, and an authorized editorial choice. A candidate's preferred wording does not itself establish reader state. This would clarify application of existing rules, not require all editorial decisions to have new customer research.

**Audit verdict:** Plausible exception misapplication; no newly demonstrated permission in the complete current contract. Add a targeted counterexample before treating a wording change as necessary.

## R02 - Selection preserves the scope of what was selected

**Input / task:** The user accepts a size-focused ad for explaining scale and says to retain the general quiet, personal, everyday positioning. The next task is a general follow-up email. Product facts and customer evidence have not changed.

**Current representation / route:** Controller steps 2 and 7 and multi-step state; Chapter 03 positioning output; Chapter 04 role steering. Existing S04 covers accumulated local foregrounding.

**Synthetic failure:** The agent records a size-led campaign direction as adopted because the ad was accepted. It then uses the supposed adopted decision to justify a size-led email premise.

**Why it changes the decision:** Authorization for one execution has been broadened into authorization for an upstream strategy. No new evidence or decision supports that expansion. The ad's acceptance is real; the expanded scope is not.

**Expected disposition:** Retain the accepted ad and its scale-explanation purpose. Use the original general positioning for the new email. Do not ask for approval again merely to preserve already resolved scope.

**Legitimate controls:**

- The user explicitly selects a size-led creative concept for the campaign. The agent may apply that concept within the delegated scope while preserving supported claims; selection does not prove that size is the market's primary purchase motive.
- The user asks the agent to select a campaign direction and implement it. A reasoned selection within that authority does not require another approval checkpoint.

**Existing protection:** Chapter 03 says selection must occur within task authority and does not verify factual assumptions. The controller preserves settled choices within current scope, and Chapter 04 states that a prior local lead is not evidence for strategic promotion.

**Smallest candidate clarification:** In a retained selection, preserve what was selected and where it applies whenever losing that scope could change the next decision. This can use the existing state mechanism; no approval log, role ledger, or new handoff schema is required.

**Audit verdict:** A concrete variant of scope loss, already prohibited by the current contract. Extend the S04 acceptance/continuation scenario rather than introduce a universal approval stage.

## R03 - A related attribute does not preserve the whole proposition

**Input / task:** The adopted campaign meaning is a quiet, personal initial for everyday wear. Size supports the quiet scale. Review a campaign whose headline is `Small on purpose.`, whose imagery consists of scale comparisons, and whose body explains only smallness. Its planning note still names the original positioning. No new positioning evidence or wider selection is supplied.

**Current representation / route:** Controller final priority/role validation; Chapter 04 whole-artifact hierarchy review; S03 wording variant.

**Synthetic failure:** The review accepts the campaign because smallness is compatible with quietness and the planning note still contains the original positioning.

**Why it changes the decision:** Compatibility with one part of the proposition is treated as preservation of the entire proposition. The retained label does not establish what the audience-facing artifact communicates. Smallness has displaced the personal/everyday value as the organizing premise.

**Expected disposition:** Inspect the combined headline, body, examples, imagery, and action against the adopted meaning and the current job. Repair the affected expression if it communicates a materially narrower or different reason to care. This is an interpretation of the artifact, not a measurement of actual audience response.

**Legitimate controls:**

- The same headline accompanies expression that clearly supports a personal everyday initial, with scale serving that meaning. The phrase alone does not establish failure.
- A dedicated scale-explanation execution omits other value dimensions because its bounded job does not need them. It need not repeat the whole positioning statement.
- A creative concept realizes the meaning through images or implication rather than repeating the words `personal` and `everyday`. Missing keywords do not prove semantic loss.

**Existing protection:** Chapter 04 explicitly requires assessment of effective hierarchy across the whole artifact, including placement, repetition, examples, and procedural detail. S03 already includes the nonnumeric wording variant.

**Smallest candidate clarification:** In the review fixture, include the candidate's superficially plausible rationale and ask whether the artifact supports that rationale. Keep judgment at the level of meaning and job, not required keywords or a prescribed balance of value dimensions.

**Audit verdict:** Recognition/review risk, not a new missing semantic rule. Strengthen the existing counterexample; do not add another general prohibition.

## Cross-case conclusions

The cases share a pattern: a downstream artifact or choice is used to strengthen the basis, scope, or role of its own inputs. They differ in what changes: inferred reader state in R01, selection scope in R02, and effective proposition in R03. One example may exhibit several changes; the categories are not mutually exclusive causal findings.

A useful review can inspect the supplied brief, source evidence, selected option and its scope, retained summary, and actual artifact. It need not demand hidden reasoning or infer cognitive order from a final answer. A justification consistent with an output is not automatically independent support for that output.

No mandatory pre-expression stage, new primitive, or universal state form is justified by this static audit. R01/R02 may benefit from local clarification if review reveals ambiguity at the point of use; R03 already has direct wording. Bounded editorial choice, provisional exploration, legitimate local emphasis, and delegated selection must remain possible.

If runtime guidance is later changed, inspect it together with the always-loaded controller and the actual retrieved slice. A clarification placed only in Chapter 04 does not reach a narrow fast-path task that legitimately reads no handbook. That is a delivery limit, not an automatic reason to duplicate all guidance in the controller.

## Repository references

- [Controller](../skills/marketing-practitioner/SKILL.md): decision-local role steering; missing information and uncertainty; multi-step state; source fidelity; final validation.
- [Positioning](../skills/marketing-practitioner/handbook/03-positioning-and-value.md): Section 10, positioning output and selection authority.
- [Messaging](../skills/marketing-practitioner/handbook/04-messaging-proof-and-copy.md): Sections 5, 10, 12, and 13, including local role steering and whole-artifact review.
- [Email](../skills/marketing-practitioner/handbook/12-email-communication-architecture.md): Sections 2, 5, and 6, including local information jobs and continuity.
- [Role-steering regression contract](decision-local-role-steering-regressions.md): S01-S05, including S03 wording and S04 continuation variants.
- [Cross-layer regression contract](cross-layer-promotion-regressions.md): P01, P04, P07, and P08.
