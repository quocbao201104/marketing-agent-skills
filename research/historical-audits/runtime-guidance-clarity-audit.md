# Runtime guidance clarity audit and regression contract

Status: **STATIC VERIFICATION AND TARGETED REGRESSION CONTRACT - NO LIVE BEHAVIORAL PASS**

## Scope

This audit follows [the cross-layer role reasoning audit](cross-layer-role-reasoning-audit.md). It reviews the working tree based on `189afbc821a2b14c6c315c664ae8f31b9898bf89`, including the preceding Chapter 04/12 and S03/S04 repairs. Earlier audit verdicts describe the pre-clarification text; this document records the subsequent changes.

The review checked the twelve previously identified guidance clusters against the controller, their surrounding text, the relevant operating-guide handoffs, and existing regressions. It is not an exhaustive audit of every platform or knowledge file. No subagents or model behavior trials were used. All examples below are constructed counterexamples and controls, not captured failures.

Contribution risk: **Level 2 - bounded controller/composition and editing behavior**. The initial pass clarified role steering and resolved two instruction tensions. The subsequent application-clarity pass rewrote the remaining eight clusters to make actions, conditions, and continuation explicit while preserving their existing boundaries. It adds no runtime phase, schema, route, mandatory approval, or general ban on negative instructions. Static review can establish a textual conflict or clearer disposition; it cannot establish model compliance or the causal effect of wording.

## Disposition of the twelve clusters

| Cluster | Disposition | Reason |
| --- | --- | --- |
| Controller role steering | Rewrite locally | Separate ordinary execution, trigger, basis, and disposition; distinguish evidence from editorial authority at the exception. |
| Chapter 04 role steering | Align locally | Apply the same basis distinction and preserve the scope and evidence status of a selection. |
| Chapter 03 selection | Rephrase | Separate exploration, selection within authority, and downstream use. Carry what was chosen and where it applies; preserve factual evidence status. |
| Chapter 04 whole-artifact review | Repair | The blanket lead/repetition role-check instruction is broader than the conditional check in the controller and Section 5. Ground comparison in the artifact's actual meaning. |
| Controller resolved-state rule | Rephrase | State the action for adopted choices, reviewable assertions, fixed wording, and unsupported claims in sequence; retain the necessity condition for reopening. |
| Controller planning/clarification | Rephrase | Make continuation and missing-input branches explicit. Missing material input and missing authority each remain sufficient reasons to gate dependent work when a wrong assumption would invalidate it. |
| Controller continuation/update | Rephrase | Separate retained state, changed scope, weakened evidence, and resumption into their own actions. Preserve paused work, unaffected outputs, and evidence status. |
| Content selection | Rephrase | Lead with the reader job and local sufficiency; then allocate deeper detail. Preserve material disclosure, domain capability identity, and the per-detail omission test. |
| Composition/routing | Rephrase selected entries | State the permitted action for fixed inputs, identity inputs, descriptive/causal questions, and copy capabilities. Preserve specialist ownership, factual sufficiency, and direct execution. |
| Chapter 04 claim control | Rephrase | Specify which part of a claim to qualify and which supported relations must survive; keep factual truth distinct from semantic equivalence. |
| Chapter 04 editing | Repair | The local query/route requirement covers claim strength but omits the already-authorized claim-correction exception and the distinction between missing expertise and missing authority. |
| Operating-guide message-to-copy handoff | Rephrase | Group message inputs, claim constraints, and material relationship state by function. Surface information when the communication needs it rather than serializing the handoff. |

Email history, inbox allocation, and relationship-force passages were also inspected as adjacent controls. They distinguish evidence, local jobs, permission, and standing; no additional wording repair was established there.

## Application-clarity pass

The initial `Keep` verdicts meant that no conflicting action had been established. That standard was narrower than the requested improvement in how instructions guide execution. This pass treats those eight clusters as wording candidates, not newly confirmed behavioral defects.

The inspected problems are structural: a single paragraph mixes retained state with update events; authority conditions are embedded across positive and negative clauses; an output-selection paragraph starts with prohibited delegation before defining local sufficiency; and a handoff lists constraints without grouping their use. Replacements put the current action first and keep its material condition beside it. Conditions are retained because they carry meaning, not removed merely to make the prose affirmative.

The semantic review specifically preserves:

- adopted choices versus assertions under review; exact wording and necessity-based reopening;
- delegated selection versus factual verification and external commitment;
- missing material input even when decision authority has already been delegated;
- paused/cancelled outcomes, dependent revisions, and recovery of available state;
- material disclosure and enough domain capability for the artifact to work on its own;
- direct execution for resolved tasks, specialist retrieval for open choices, and hypothesis status for provisional work;
- beneficiaries, shared/returned objects, responsibility, and other supported semantic relations during claim qualification;
- relationship or responsibility content when the communication job actually requires it, while keeping internal handoff notes out of ordinary copy.

Existing negative invariants and prohibitions remain where they express a useful boundary. The wording pass does not claim that fewer negative sentences cause better results.

## F1 - Basis and scope at the role-change decision

**Input / task:** A missing size disclosure is being repaired on a PDP. The separate email has an adopted general reintroduction job, and no recipient-specific size concern is established.

**Current representation / route:** The former controller paragraph combines a conditional role check, examples, reader state, touchpoint job, evidence, adopted decisions, repetition, and recovery. Chapter 04 Section 5 lists the same possible bases.

**Failure hypothesis:** A candidate size-led email supplies its own rationale: the agent assumes subscribers are concerned about size, relabels the email job, and treats that as support. Alternatively, acceptance of one size-explanation ad is expanded into campaign-wide authority.

**Decision consequence:** An inference becomes an established reader state, or a scoped selection becomes broader authority. These violate existing global rules; this audit does not claim the complete prior contract permitted them.

**Smallest correction:** Replace the controller paragraph with ordinary behavior, a conditional trigger, a grounded basis distinction, and bounded disposition. Align Section 5. Preserve known state, warranted inference, and authorized editorial choice as distinct bases. A draft may reveal a new question that warrants investigation.

**Counterpressure:** New customer research is not required for every editorial choice. Delegated selection remains actionable, and local foregrounding remains possible without strategic promotion.

## F2 - Conditional steering versus blanket review

**Input / task:** Review a security-response email whose established job is providing a requested report. The report leads the subject and remains proof in the product strategy.

**Current representation / route:** Controller role steering and Chapter 04 Section 5 call for a role check only when there is a material role change. Section 10 previously said to add one for audience-facing leads and repeated emphasis without that condition.

**Textual tension:** Reading Section 10 literally adds the check even when the comparison shows no material change; following the conditional controller leaves it dormant. This matters for unnecessary processing or reopening settled work.

**Smallest correction:** Keep whole-artifact review, but invoke role steering when the comparison reveals a possible material role change. Assess what the artifact communicates instead of treating a positioning label or repeated keyword as proof of fidelity.

**Counterpressure:** Review must still catch unsupported changes in meaning when the original positioning label remains in planning notes. A legitimate local subject need not restate the whole product promise.

## F3 - Editing authority versus truthful claim correction

**Input / task:** Polish supplied copy using evidence that supports an observed outcome but not the copy's causal attribution. Audience, product, and intended message otherwise remain fixed.

**Current representation / route:** The actual `copywriting.editing` slice lists claim scope/strength in the protected envelope, then requires query or routing for a changed decision unless wider authority is explicit. Controller step 2 permits narrowing or flagging unsupported claims. Sections 8/9 authorize the same bounded correction but are outside that retrieved slice.

**Textual tension:** A faithful local reading can require escalation solely because correcting an unsupported claim changes its strength. The controller allows that correction without reopening positioning. Missing local context can reverse the action.

**Smallest correction:** State the bounded claim-correction exception beside the envelope. Retain supported meaning and fixed-wording constraints. For other changes, use authority from the request and context, retrieve specialist guidance for actual dependencies, and clarify or bound only when material input or authority remains missing.

**Counterpressure:** This is not permission to restyle fixed copy, invent a replacement claim, or change the offer, audience, or CTA under the name of claim correction.

## Regression cases for subsequent use

These are manual reasoning contracts. Structural validation does not execute them against a model.

### C01 - Candidate-created reader concern

**Given:** The F1 brief and a candidate size-led subject with the rationale that subscribers must be anxious about scale.

**Expected:** Keep the anxiety unestablished, preserve the general email job, and repair the candidate locally while retaining necessary product facts. The PDP defect remains a disclosure issue.

**Fail if:** The candidate's rationale becomes established reader state or is used to authorize a broader premise without independent support.

### C02 - Authorized editorial choice and new evidence

**Given:** The user delegates selection of an educational email topic. Scale is a truthful topic supported by verified product measurements; no customer anxiety is known.

**Expected:** The agent may select a scale explanation, retain that choice's scope, and write it without another approval. It need not assert that readers are known to be anxious or that scale is the market's main purchase motive. If drafting exposes a factual question, available evidence may resolve it and justify an affected revision.

**Fail if:** The agent demands customer research for the ordinary topic choice, treats its selection as empirical proof, or rejects evidence discovered during drafting merely because it came later.

### C03 - Local acceptance and wider authority

**Given:** The user accepts a size-explanation ad while retaining general campaign positioning, then requests a general email.

**Expected:** Keep the ad accepted within its purpose and preserve the general message in the new email. The controller should suffice when no further handbook read is needed.

**Control:** If the user explicitly selects the creative concept for the campaign, apply it within that authority while keeping factual assumptions distinct from verified evidence.

**Fail if:** Local acceptance becomes campaign-wide authority, or explicit campaign selection is blocked merely because the concept began as a local execution.

### C04 - Ordinary lead versus effective role change

**Given:** Review the requested security-report email from F2.

**Expected:** Recognize the legitimate local lead; no separate role audit or upstream reconsideration is warranted.

**Control:** Review a general campaign whose note retains the original personal/everyday positioning but whose audience-facing material communicates only smallness. Compare actual meaning and apply local role steering if the proposition has changed. The same phrase in a legitimate scale explanation remains permissible.

**Fail if:** Every headline triggers an extra audit, a retained positioning label excuses changed meaning, or particular words become mandatory/prohibited.

### C05 - Correct a claim through the editing slice

**Given:** Request: polish a sentence for use in marketing. Supplied evidence: pilot teams recorded a 40% reduction in average approval time compared with their pre-pilot baseline; the comparison does not identify causality. Draft: `Relay caused pilot teams' average approval time to fall by 40%.` Audience and product facts are otherwise resolved. Load the controller plus `copywriting.editing`.

**Expected:** Preserve the observed result, pilot scope, metric, and beneficiary while removing or qualifying unsupported attribution to Relay. Complete the bounded edit without an approval or positioning detour solely because claim strength changes. Do not turn the observed percentage into a future guarantee.

**Fail if:** The agent preserves unsupported causality, invents replacement proof, unnecessarily asks to change positioning, or deletes the supported beneficiary/outcome relation merely to sound cautious.

### C06 - Fixed wording and a genuine wider decision

**Given:** The same causal sentence is an exact quotation the user requires to remain verbatim.

**Expected:** Flag the unsupported attribution without rewriting the fixed quote. Continue other supported work; do not imply the claim is validated.

**Separate control:** A clarity edit proposes replacing an adopted demo CTA with a paid-trial commitment whose terms and authority are unresolved. Resolve the material dependency through the existing uncertainty policy; the claim-correction exception does not authorize the new offer or commitment.

**Fail if:** The agent edits fixed wording silently, treats all changed decisions as ordinary claim repairs, or fabricates terms to complete the wider change.

### C07 - Retained decisions and reviewable assertions

**Given:** A fixed audience and price, a supplied positioning proposal explicitly offered for critique, and a source claim that exceeds the supplied evidence.

**Expected:** Preserve the audience and price, review the proposal as a proposal, and narrow or flag the unsupported claim. Reopen an adopted input only when contradiction, material staleness, or insufficiency makes that necessary for truthful completion.

**Control:** Exact quoted wording remains unchanged when explicitly fixed; flag the issue rather than silently correcting the quote.

**Fail if:** Supplied material becomes verified evidence, all supplied decisions are frozen against requested critique, or a local claim issue restarts unrelated strategy.

### C08 - Authority and missing input are separate

**Given:** The user delegates a choice among supported message directions and requests implementation. All material facts are available.

**Expected:** Select and implement within scope without another approval. That authority does not imply permission for an external commitment.

**Control:** The same delegation leaves a material user-owned product fact unresolved, with plausible values that would invalidate different downstream versions and no available source resolving it. Prepare the supported recommendation and smallest question, wait for that input on dependent work, and continue independent work. A missing immaterial preference does not trigger this branch.

**Fail if:** Delegation is mistaken for factual sufficiency, a missing fact is filled by assumption, silence is treated as approval, or ordinary choices require another confirmation.

### C09 - Scope change and continuation

**Given:** A task requests a PDP, ad, and email. The user cancels the ad, pauses the email, and corrects a specification used by the PDP. A retained note contains the earlier specification.

**Expected:** Reconcile the note with the correction, revise the affected PDP content before relying on it, exclude the cancelled ad, and keep the paused email available without executing it or counting it as required for current completion. Preserve unaffected choices and retrieve recoverable missing state before asking.

**Fail if:** The latest instruction erases all earlier outcomes, stale notes outrank the correction, paused work is executed, or the agent requires a new state form for a simple task.

### C10 - Sufficient introduction and selective detail

**Given:** A short introduction to an unfamiliar marketing tool must explain its supported work, invite relevant feedback, and link to documentation. Sources include capabilities, installation detail, internal research notes, and a material limitation.

**Expected:** Provide enough concrete domain capability and participation context in the introduction itself. Include the limitation if it changes this reader's decision or truthful interpretation. Put deeper installation detail in the documentation and keep unnecessary internal notes out of the copy. Keep the existing omission test and whole-artifact judgment.

**Fail if:** The introduction becomes an inventory, operating safeguards replace domain capability, a necessary limitation disappears, or all understanding is delegated to the link.

### C11 - Routing by unresolved work

**Given:** An approved identity needs mechanical resizing, or supplied copy needs a narrow rewrite with its facts, message, and representation already resolved.

**Expected:** Execute directly within those constraints. No identity exploration, full copywriting sequence, or causal investigation is created by the artifact type.

**Controls:** A new identifying-cue choice lacks material audience/deployment inputs: recover those inputs or use the uncertainty policy before selecting the cue. A real causal question enters Chapter 05. A descriptive record mismatch remains descriptive when no causal inference is needed. Payment to a creator alone does not establish paid-media delivery.

**Fail if:** The agent skips the specialist needed for an open decision, invents identity inputs, or turns a resolved production task into an upstream workflow.

### C12 - Claim relations and handoff realization

**Given:** A supplied message identifies the beneficiary, a returned/shared output, and responsibility, but one claim overstates certainty. Its handoff also contains research notes and material relationship constraints.

**Expected:** Qualify only the unsupported certainty while preserving the supported relations. Use the handoff to realize appropriate wording and interaction; surface research or relationship information when the reader's current decision or the communication job needs it. A correction whose job includes responsibility must still acknowledge it.

**Fail if:** A true process statement replaces a material beneficiary/output relation, the handoff becomes the copy outline, or instructions to keep internal state out of prose suppress a required acknowledgement or disclosure.

## Verification boundaries

Review the controller together with Chapter 04 Sections 5 and 10 and the actual `copywriting.editing` excerpt. Preserve existing S01-S05 and P01-P08, including supported promotion, local foregrounding, numeric/nonnumeric variants, and continuation scope. Check exact text edits, UTF-8/BOM/newlines, links, routing, and repository verification.

Any green repository check establishes package, retrieval, and harness integrity only. This audit establishes neither a universal advantage for affirmative wording nor a live improvement in marketing behavior. The negative constraints retained here serve explicit truth, scope, and authority boundaries.

## References

- [Controller](../skills/marketing-agent-skills/SKILL.md)
- [Positioning output](../skills/marketing-agent-skills/handbook/03-positioning-and-value.md#10-positioning-output)
- [Expression and role steering](../skills/marketing-agent-skills/handbook/04-messaging-proof-and-copy.md#5-copy-as-an-expression-layer)
- [Whole-artifact review](../skills/marketing-agent-skills/handbook/04-messaging-proof-and-copy.md#10-copy-quality-is-multidimensional)
- [Editing slice](../skills/marketing-agent-skills/handbook/04-messaging-proof-and-copy.md#17-editing-and-voice-repair)
- [State handoffs](../skills/marketing-agent-skills/references/operating-guide.md#state-handoffs)
- [Role-steering regressions](decision-local-role-steering-regressions.md)
- [Cross-layer regressions](cross-layer-promotion-regressions.md)
