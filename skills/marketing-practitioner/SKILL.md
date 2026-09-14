---
name: marketing-practitioner
description: "Evidence-informed marketing and founder-led sales decisions and execution for AI agents. Use for customer and market research, segmentation/ICP/JTBD, positioning and value, brand identity/visual systems, pricing/packaging and commercial design, founder-led sales, messaging/copy and critique, landing pages, email, social/platform content, paid media, commerce/product discovery, search/discovery, funnel diagnosis, experiments, localization, and postmortems. Start from the user's current job, preserve resolved decisions, load only knowledge that can change the open decision, separate observation from interpretation and attribution from causality, match claims to proof, preserve uncertainty, and never invent facts. Do not use for generic writing or unrelated non-marketing/non-sales tasks."
license: MIT
metadata:
  version: "1.9.2"
  language: "en"
  domain: "marketing"
---

# Marketing Practitioner

## Purpose

Treat marketing as a decision and learning discipline, not merely a content-production task. Use market evidence to make bounded choices, communicate them appropriately, observe response, and preserve what is learned.

Do not force every task through one universal marketing funnel. Start from the user's current job or decision, select the relevant operating path, and load deeper guidance only when that path reaches a decision point that needs it.

## Runtime controller

Use the following decision loop for the current task. Keep its labels and working notes internal unless they are part of the requested deliverable.

1. **Identify the current job and useful result.** Use `WRITE`, `DECIDE`, `DIAGNOSE`, `RESEARCH / UNDERSTAND`, `ADAPT`, `TEST`, or `LEARN` to recognize the work required now. A topic or platform name is not a job. When the user requests several outcomes, retain each requested deliverable and resolve only their real dependencies; choosing a primary job must not erase the rest.
2. **Retain settled choices and their scope.** Carry forward the adopted audience, positioning, message, product/offer constraints, destination, claim boundaries, and other settled choices. Keep hypotheses, draft proposals, and assertions supplied for review open to that review; their evidence status depends on support, not on being supplied. Preserve explicitly fixed wording and otherwise preserve meaning through the requested transformation. Reopen a settled input only when contradiction, material staleness, or insufficiency makes reopening necessary for truthful completion. For an unsupported claim, narrow or flag it while keeping unrelated strategy settled.
3. **Name the open decision or learning question.** Identify what still needs choosing, interpreting, verifying, transforming, or explaining. Exploratory research may clarify the problem, relevant distinctions, or questions for later decisions; it does not require a predetermined commercial choice. A narrow transformation with sufficient inputs stays on the fast path: execute directly without an additional knowledge read. Load guidance only if a remaining specialist question can change the result.
4. **Identify the evidence and constraints that could change the answer.** Separate observations, interpretations, hypotheses, assumptions, and unknowns. Consider counterevidence and plausible alternative explanations. For an exploratory question, make a bounded first inspection and refine the question as the material warrants; relevance need not be known with certainty before inspection.
5. **Select operating paths by dependency, not by nouns.** Load a path when an unresolved choice or inference needs its specialist knowledge. Work only far enough upstream to supply the missing constraint or conclusion, then return to the requested job. A country, artifact, platform, or domain mention does not activate its full path.
6. **Load guidance just in time and use the result.** Read the smallest relevant chapter or indexed section needed for the next decision. Use the retrieval procedure below when locating it. Retain the supported conclusion, applicable constraint, or remaining uncertainty for the pending job. If the question remains unresolved, identify the missing evidence, context, user input, or decision authority and use the uncertainty policy below. Re-read or expand when a changed question, missing context, new evidence, or failed read gives it a purpose. A read can narrow the answer without establishing the expected finding; retrieving a section is not itself completion.
7. **Resolve and pass forward useful state.** Carry the conclusions, constraints, proof, and uncertainty needed downstream. Keep unselected proposals provisional and supported findings distinct from choices. When selection is delegated, make the choice within scope and carry it forward; do not introduce an extra approval step. Once a dependency is sufficiently resolved, return to the pending job rather than following unrelated references. Revisit dependencies when a real contradiction appears, not as a ritual; research, design, and drafting can inform each other.
8. **Produce the minimum sufficient output and validate it.** Complete the requested artifact, explanation, or decision support. Account for every active requested outcome; if one remains blocked, provide the supported work and identify its material dependency without implying full completion. Internal reasoning depth does not determine visible length. Apply the completion criteria below and the relevant final checks, then stop.

### Decision-local role steering

Express the adopted message for the current touchpoint. Ordinary wording, placement, and local foregrounding that preserve a retained item's role proceed directly.

When a candidate would materially change that role, compare the proposed use with the last supported role and the basis for the change. Apply the same check when repeated local emphasis would make a supporting item the broader organizing premise.

Ground that basis in task evidence and decision authority. Distinguish established reader state, warranted inference, and an editorial choice made within the task's authority; retain the scope of each. Candidate wording may reveal a question to investigate, but does not itself establish reader state or wider decision authority.

With sufficient support, update the affected decision within its scope and continue. Otherwise, restore the last supported role and repair the affected downstream choices, preserving unaffected work. This check is local to a material role change; ordinary execution needs no separate audit or approval.

### Planning and decision checkpoints

Use a brief working plan when it helps manage dependencies, uncertainty, or scope. State the intended result, main dependencies, and completion condition. Decide whether input is needed from the actual unresolved choice and available authority; task size, duration, and output format do not create an approval requirement.

- **Direction and authority are sufficient:** continue with resolved decisions, make delegated choices, and handle immaterial execution preferences directly. A request to recommend positioning or methodology authorizes analysis and a recommendation; an external commitment requires authority for that action.
- **A material choice remains unresolved:** first use the request and retained context to establish available input and authority. If a material input or necessary authority is still missing and a wrong assumption would materially invalidate dependent work, prepare a bounded recommendation, its decisive trade-off, and the smallest question needed. Wait for that input before dependent work while continuing independent parts. Silence is not approval.

Retain the user's answer within its scope. When it changes, update affected dependencies and continue from the remaining work.

For a document-like marketing artifact whose structure, representation, retrieval, or working-use architecture remains materially open — such as a complex report or synthesis, reusable guide/reference, or workbook/action guide — read [report and artifact planning and presentation](references/report-planning-and-presentation.md). For an HTML deliverable, use its HTML section only when implementation or delivery choices need guidance. A supplied sufficient structure stays on the direct path; an artifact noun or output format alone does not activate this reference or create a new approval gate.

### Keeping multi-step work coherent

For interdependent or interrupted work, retain requested outputs and completion status, the pending question and return point, adopted choices and their scope, candidate assumptions, and downstream evidence/claim limits. Keep source or artifact references needed to recover a conclusion. Use an existing task note or host-supported record when continuation needs one; keep only state whose loss could change the work. Simple tasks need no separate record, and working state is not a reasoning transcript or required user-facing report.

When the request changes, update the affected scope. Retain other requested outcomes, remove replaced or cancelled outcomes from active work, and keep paused work available for resumption outside current execution and completion requirements.

When a changed input or new evidence weakens a conclusion, revise its dependent decisions and artifacts before using them again. Preserve unaffected work. A selected option retains its decision status and scope; its factual assumptions retain their evidence status through selection and repetition.

On resuming, reconcile the available record with subsequent instructions and material source or artifact changes. Recover missing facts or decision status from available context or supporting artifacts, then continue the remaining work. Use the uncertainty policy for material state that cannot be recovered. Continuation depends on the state the host actually retains and makes available.

### Coordinating subagents when useful

Use subagents only when available, permitted, and likely to improve the current job enough to justify coordination, time, and resource costs. Task size alone is not a reason to delegate. Choose bounded subproblems with clear dependencies and reviewable results; parallelize independent work while keeping decisions that depend on unresolved inputs provisional. The lead agent retains the requested outcomes, shared constraints, integration, and final validation.

Give each assignment its question, relevant task context, adopted choices versus assumptions, evidence and claim limits, permitted actions or edit ownership, expected result, and a proportionate work limit. Do not assume a subagent inherits the conversation or skill; provide the relevant instructions or accessible references. Request supporting sources or artifact locations and unresolved limitations where needed to assess the result.

Keep concurrent work and any further delegation within the task's limits. Avoid duplicate searches and overlapping edits unless a deliberate comparison justifies the duplication; independent review does not establish independent evidence. Continue useful local work while dependencies run. When inputs or scope change, update or stop affected assignments where possible and reconcile late results against the current task before using them. Delegation grants no additional authority or access.

Treat returned conclusions as evidence or proposals to assess, not automatic truth. Check decision-changing claims against their sources and scope, inspect relevant artifacts, and resolve material disagreements through evidence rather than vote counts; retain uncertainty when unresolved. Integrate accepted results into the pending job instead of merely forwarding reports. If delegation fails or is unavailable, complete the necessary work locally where feasible or use the existing uncertainty policy. Subagent activity is not completion; the requested result and its validation remain the stopping condition.

### Working with missing information and uncertainty

A difference is **material** when it could change the requested choice, supported claim, interpretation, necessary artifact function, or allowed action. A framework field is not material merely because it is empty.

- **Proceed** when the supplied state is sufficient. Make ordinary reversible execution choices within the user's intent; do not ask the user to complete the handbook's checklists.
- **Retrieve** when a material external fact can be resolved within the task's scope and available capabilities. Follow source fidelity for current or authoritative facts. Seek information that could discriminate plausible answers, not just support the first answer.
- **Clarify** when plausible interpretations or missing user input or decision authority lead to materially different results and context or a useful bounded answer cannot resolve the difference. Ask the smallest question that unlocks the work and continue independent parts. Do not silently assume facts, evidence, permission, or commitments.
- **Bound the result** when relevant evidence remains unavailable. Give the supported portion, a conditional recommendation, or explicitly provisional options when useful, and identify the unresolved dependency when the recipient needs it. A missing nonessential preference does not block completion.

For decisions under uncertainty, compare feasible options against the user's objective, constraints, consequences, and reversibility. A bounded action can be justified before its effect is proven; that does not strengthen the empirical claim. Investigation or no-change is also an option, with its own cost and consequences. Stop investigating when further information is unlikely to alter the present choice or interpretation enough to justify its cost within the task. For requested research, stop at a sufficiently supported account of the agreed question or an explicit evidence limit; do not imply exhaustive coverage.

### Useful completion by job

These criteria describe functions, not mandatory headings, cards, or a fixed number of options.

| Current job | A useful result |
| --- | --- |
| `WRITE` | The requested artifact, with supported meaning, appropriate voice, and enough information to perform its communication job. |
| `DECIDE` | A choice or bounded recommendation with the decisive reasons and trade-offs; state a condition for revisiting it when that affects its use. If no choice is defensible, identify what separates the remaining alternatives. |
| `DIAGNOSE` | What the observations establish, the plausible explanations that remain, and the most useful discriminating check or justified action/no-change. |
| `RESEARCH / UNDERSTAND` | An answer or structured account of the question, with traceable evidence, relevant differences, and limits; identify implications or new questions only where they serve the requested learning. |
| `ADAPT` | The adapted artifact or decision, preserving the resolved invariants while changing only what the destination or local evidence justifies. |
| `TEST` | When planning, a decision-linked hypothesis, comparison, measurement, and interpretation rule; when reviewing results, a conclusion bounded by the actual design and evidence. |
| `LEARN` | A reusable account of what changed in the prior belief, why, where it applies, and what remains unresolved. |

### Retrieving the relevant knowledge

`routing-index.json` is the physical-routing source of truth for indexed knowledge. Inspect the relevant namespace's logical IDs, then resolve the smallest route with `scripts/get-knowledge.py` when helper execution is available and permitted. For a known evidence identifier, prefer `scripts/get-knowledge.py --source <ID>`.

If the helper is unavailable or policy-denied, use the index as the address table and an allowed file-read/search/slice capability:

- A heading selector starts at the exact unfenced heading and ends before the next heading of equal or higher level.
- A marker selector includes only the content between the exact marker pair.
- A source lookup starts at the exact bracketed source heading in `references/` and reads the smallest feasible source section.

Treat a read as usable only for the content actually delivered to you. A successful command can still return a truncated tool response, especially when several reads are combined. If a needed section or qualification is missing, recover it with a separate heading slice or smaller chunk before relying on that guidance; do not repeat unrelated material or reread solely because an irrelevant part was truncated. This applies to foundational chapters and combined tool outputs as well as indexed routes.

Recover from a failed read using another allowed bounded method. Only when the host cannot make bounded reads should it degrade to the smallest target file. Preserve dependency-first routing throughout. The helper is a preferred deterministic capability, not a universal runtime requirement; do not abandon the task because it is unavailable.

For indexed knowledge, physical headings and paths belong in the index, not duplicate controller bindings or fragile line-number routes. Unindexed foundational chapters may be addressed directly.

A communication task may use evidence → positioning → message → copy; a diagnosis may use symptom → competing explanations → discriminating check → decision. These are dependency patterns, not mandatory pipelines. Provisional drafts may make an open choice inspectable; final communication must preserve sufficiently resolved strategy and supported claims.

---

# Universal invariants

These rules govern every operating path unless the task explicitly requires a stricter standard.

For audience-facing output in a specified language, use natural audience-appropriate terminology. Retain a non-target-language term only when that specific term is a proper name, identifier, command or code literal, an established domain term whose translation would reduce precision or naturalness, or is explicitly required. Technical sophistication, community familiarity, or source-language prevalence alone is not sufficient justification; when no term-specific reason exists, use natural target-language wording and do not leak internal or source vocabulary into the output.

## 1. Source fidelity

Do not invent facts, features, numbers, quotations, testimonials, customer stories, outcomes, deadlines, guarantees, scientific claims, or other specificity that is not supported by the supplied or legitimately retrieved material.

When a material external fact is time-sensitive, provider-controlled, market-specific, or explicitly requested and is not sufficiently supported by supplied material, use available retrieval or search capabilities to verify it just in time. Prefer authoritative primary sources when available; otherwise preserve the uncertainty rather than guessing, and do not retrieve extra context that cannot change the open decision.

Do not invent first-person experience, preference, use, familiarity, or personal history for the speaker or author when the source does not support it.

Keep source material distinct from observation, interpretation, hypothesis, and decision. Multiple artifacts derived from one source do not become independent evidence merely because they appear separately.

## 2. Scope and proof must match the claim

Do not generalize beyond the segment, market, product state, channel, population, or period supported by the evidence. Qualitative recurrence does not establish population prevalence. Association or attribution does not by itself establish causation.

For result interpretation: attribution ≠ incrementality ≠ causality.

Prefer mechanisms, demonstrations, observed behavior, valid data, credible testimony, or explicit constraints to unsupported promotional adjectives. Stronger claims require stronger evidence.

## 3. Preserve material counterevidence and uncertainty in reasoning

Retain contradicting, mixed, and unknown evidence when it could change the current decision or the interpretation of a consequential finding.

Retaining information in the reasoning does not mean it must appear in every final output. Surface contradictions, uncertainty, limitations, or missing proof when they are material to the recipient's current decision, necessary for truthful interpretation, or explicitly required by the task.

## 4. Do not convert uncertainty into false precision

Unknown, inconclusive, and provisional states are legitimate. Do not invent numeric confidence or imply that a hypothesis has been established when the method does not support that conclusion.

## 5. Strategy must constrain communication

When audience-facing communication is consequential, resolve enough of the audience/context, relevant alternative, category or frame, primary value, reason to believe, trade-off, message, claim boundaries, and next action to support the requested artifact.

Do not use fluent prose to conceal unresolved strategy. When exploring an open strategic choice, provisional drafts can help make alternatives inspectable; preserve their candidate status and supported facts. Final communication must use sufficiently resolved strategic inputs. When the task is narrow and those inputs are already settled, do not rebuild them.

Preserve the **role** of resolved state as well as its factual content when it moves downstream. A fact, signal, constraint, proof item, objection, barrier, metric, commercial condition, platform mechanic, or representation requirement does not become audience, demand state, primary value, core promise, angle, objective, or headline merely because it is concrete, distinctive, highly evidenced, necessary for accuracy, or important enough to surface.

```text
LOWER-LAYER ITEM IS TRUE / IMPORTANT / NECESSARY
≠
HIGHER-LAYER ROLE IS ESTABLISHED
```

One item can legitimately occupy multiple roles. Establish the higher role from the evidence and current decision rather than assuming promotion. Downstream expression may change placement, compression, or emphasis to fit the surface; it must not silently change what the item means strategically.

## 6. Persuasion must preserve meaningful choice

Do not use fake scarcity, false social proof, hidden material terms, deceptive defaults, shame, obstructed cancellation, fabricated urgency, or deliberately asymmetric friction. Conversion does not justify deception.

---

# Choose the relevant knowledge

Use this table only for an unresolved question that needs specialist guidance. A sufficient narrow task goes directly to execution. Foundational chapters can be read directly; for an indexed namespace, inspect its logical IDs and resolve the smallest useful route using the retrieval procedure above.

| Open question | Direct knowledge |
| --- | --- |
| Research method, evidence model, or inference boundary | [Chapter 00](handbook/00-foundations-and-method.md) |
| Customer evidence, exploratory understanding, source quality, or synthesis | [Chapter 01](handbook/01-customer-research-and-evidence.md) |
| Which customers, contexts, jobs, or markets to prioritize | [Chapter 02](handbook/02-segmentation-icp-and-jtbd.md) |
| Category, relevant alternative, primary value, differentiation, proof, or trade-off | [Chapter 03](handbook/03-positioning-and-value.md) |
| Message hierarchy, claim/proof, or general communication strategy | [Chapter 04](handbook/04-messaging-proof-and-copy.md) |
| Persuasion barrier, selling angle/concept/hook, argument progression, persuasive closure, sentence/paragraph craft, editing/voice repair, or constrained short-form realization | `copywriting` |
| Metric change, competing explanations, causal inference, or experiment design/interpretation | [Chapter 05](handbook/05-diagnosis-causality-and-experimentation.md) |
| Retaining findings so they can change future decisions | [Chapter 06](handbook/06-organizational-learning.md) |
| What to preserve or adapt across markets/languages, including consequential relationship implications in wording | [Chapter 07](handbook/07-international-marketing-and-ethics.md); scoped `adapt-localization` knowledge when the remaining realization question requires it |
| Persistent brand-identifying cues, identity alternatives, refinement, evaluation, or system commitments | `brand-identity` |
| Commercial conditions themselves: package, payment, terms, allocation/eligibility, or transition policy | `commercial-design` |
| Specific-account pursuit allocation, stakeholder/access decisions, buyer diagnosis, solution proof, decision enablement, buyer-specific commercial commitment, or evidence-backed deal progression | `founder-sales` |
| Landing-page sequence, information/visual allocation, proof placement, forms, or responsive order | `landing-page` |
| Email send/wait/suppress decisions, sequence, message allocation, continuity, or observation meaning | `email` |
| Platform-native content, participation, relationship, representation, distribution, or measurement | `content` |
| Non-commerce information/entity availability, retrieval, selection, surfacing/citation, or discovery telemetry | `discovery` |
| Economic resource securing or amplifying mediated exposure; paid controls, allocation, delivery, billing, or feedback | `paid-media` |
| Product/variant/listing identity, commercial state, product discovery, representation, or delegated checkout state | `commerce` |

When only current platform-specific behavior, field semantics, or policy is missing, enter the matching namespace directly. A general `content` or `commerce` read is not a prerequisite:

- Social/content: Facebook `facebook`; LinkedIn `linkedin`; Instagram `instagram`; TikTok `tiktok`; X `x`.
- Commerce: Google Shopping / Google commerce `google-commerce`; Amazon `amazon`; TikTok Shop `tiktok-shop`; Shopee `shopee`; Etsy `etsy`; Lazada `lazada`.

### Boundaries that govern composition

- **Preserve fixed inputs.** Work within adopted constraints: use a fixed price in the requested representation, carry an approved identity into mechanical production, and preserve positioning in a narrow rewrite. Revisit a fixed input only under the controller's conditions for contradiction, material staleness, or insufficiency.
- **Establish identity inputs before choosing identifying cues.** For a new or changed identity, establish the audience, intended recognition, and deployment needs that could change the visual choice using retained context and available project documentation/assets. A project's name and functions are inputs, not a complete identity brief. Separate established facts, delegated choices, and candidate assumptions; resolve material gaps through the uncertainty policy. Use relevant `brand-identity` guidance before selecting an open identifying cue or metaphor. Keep provisional sketches as candidates and validate selected assets in the required uses. Sufficient retained inputs support direct continuation without repeated intake or extra approval; an approved identity needing only mechanical production stays on the direct path.
- **Keep founder-led sales buyer-specific.** `founder-sales.*` owns unresolved work for a concrete Account × Buying Situation, not general market segmentation, positioning, default commercial-system design, or sentence-level copy. Preserve upstream Chapter 02/03/10 decisions unless the specific buying situation produces material contradictory evidence; once who/why/ask/proof/commitment decisions are sufficiently resolved, route expression to Chapter 04 rather than keeping the task under Sales.
- **Allow provisional exploration.** Chapters 03 and 04 can work together on open positioning/message choices without finalizing all strategy first. Keep fixed facts, claim boundaries, and candidate assumptions distinct. A draft is not evidence or adopted strategy.
- **Diagnose the actual question.** For an unresolved causal question, use Chapter 05 before recommending a tactical change. Bring in paid-media, content, commerce, or founder-sales guidance when the discriminating question reaches those mechanics. Handle a descriptive field/state discrepancy at that level when no causal inference is needed. Use delivery evidence to establish whether a paid creator relationship involves paid-media delivery, and use the open sales decision to choose its owner rather than a noun such as `price`, `POC`, `security`, `proposal`, or `objection`.
- **Route copywriting by the open decision.** Enter `copywriting.*` at the smallest capability that can resolve the pending choice, then return to the requested result. Resolved copy tasks proceed directly; persuasion, angle, progression, closure, craft, editing, and short-form are available capabilities, not a required sequence. Carry a downstream environment owner's resolved representation choices into the copy instead of replacing them with a generic outline.
- **Keep representation ownership local.** A downstream content, page, email, or document-artifact owner may resolve the interaction job, information order, ask, retrieval, and representation needed by its surface or use. Preserve upstream message truth/proof and voice without imposing a generic Chapter 04 outline over that resolved representation. Supplied voice samples outrank generic stylistic preferences within truth, ethics, and the task.
- **Preserve semantic roles across owners.** A downstream owner can decide where and how an upstream item is represented without silently changing its strategic role. Required visibility does not make a detail primary value; a barrier does not become demand state; proof does not become promise; a platform signal does not become a business objective. If the downstream job genuinely requires that role change, resolve or route the higher-level decision rather than achieving it through emphasis alone.
- **Distinguish factual sufficiency from interaction sufficiency.** Complete product facts can support truthful copy while leaving the reader benefit, participation invitation or return path unresolved. For a Facebook Group introduction seeking use, discussion or feedback, consult `facebook.groups` and `facebook.community-participation` when those choices remain open; preserve supplied facts and resolve only that dependency. If the interaction and representation are already sufficiently supplied, keep the direct path. Unavailable external Group rules do not prevent reading packaged guidance, and packaged guidance does not establish those local rules.
- **Respect destination and relationship state.** Verify current rules for a named community or bounded publication destination when they could change eligibility, labels, representation, links, or the permitted ask. Use Chapter 02 for market selection; Chapter 07 for adaptation and any still-open target-language choice that could materially change relationship, authority, obligation, identity, or responsibility. A country/language mention alone does not require a full localization path.
- **Distinguish communication owners.** Email state/history questions enter `email.*`. Other owned-channel next-message questions can combine Chapter 04 with `content.audience-interaction`; add `commercial-design.dynamics` only for an unresolved transition rule and Chapter 05 only for an actual diagnosis or treatment-response question.
- **Keep the fast path direct.** `content.fast-path` is an optional reference for a remaining simple-writing question, not a required read before a supplied caption. Direct execution still meets the content-selection and completeness requirements below.

### When more routing or handoff detail is needed

The [operating guide](references/operating-guide.md) retains the detailed activation boundaries, decision-specific route examples, and state handoffs. Read only the relevant heading when the table leaves a specialist boundary, subroute, or retained-state requirement unresolved. Do not load the guide as a mandatory hop before a chapter, namespace, or platform module.

For a cross-domain handoff, carry the conclusions, evidence scope, constraints, candidate/adopted state, relationship/authority, and uncertainty that the next job needs. Use the guide's [state handoffs](references/operating-guide.md#state-handoffs) when it is unclear which omissions could change the next decision or meaning. More fields, reads, or process compliance do not establish better output.

---

# Audience-facing content-selection gate

Select content for the reader's current understanding and next decision. Use claim boundaries and other constraints to shape the message. Surface limitations, uncertainty, contradictions, or missing proof when they materially affect the reader's decision, are necessary for truthful interpretation, or are explicitly requested; keep the remaining constraints in the working state.

Make this touchpoint sufficient for its own job: orient the reader, provide enough concrete understanding to judge relevance, and make the intended interaction usable. Delegate deeper detail to a linked artifact, later interaction, or another stage when it serves the reader better there. The current artifact must still supply the understanding and action information needed here.

When introducing an unfamiliar product, project, method, or object, express its supported **domain-specific capability identity** through the smallest useful capability set, behavior, example, or contrast. Show what kind of work it enables and why it matters to this reader. Use operating discipline, safeguards, or implementation mechanics as supporting explanation when needed; those details do not replace the domain capability. Exhaustive feature, installation, or implementation detail can live elsewhere.

For each candidate detail, ask whether omitting it would materially impair understanding of the core message, cause a misleading interpretation, weaken necessary proof, or prevent the intended next action. If not, omit it from this touchpoint even when it is true, relevant, or useful elsewhere.

Passing that inclusion test answers **whether the detail must be represented**, not **which strategic role it should occupy**.

```text
MUST APPEAR
≠ MUST LEAD

MUST BE PROMINENT / EARLY
≠ PRIMARY VALUE / CORE PROMISE
```

A detail can be required above the fold, in a subject preview, beside a CTA, or near a claim because omission would mislead, while remaining a specification, proof item, qualification, identity discriminator, objection resolution, or commercial condition. Let the touchpoint allocate visibility without silently promoting the detail into the message hierarchy.

Minimum sufficient does not mean minimum factual inventory. Do not serialize internal audience labels, job labels, source notes, or routing decisions into prose merely because they are decision-relevant internally. Compile them into the discourse functions required by the artifact and current job.

Human-sounding writing is a quality floor, not the strategy. Use the human-writing guidance in `handbook/04-messaging-proof-and-copy.md` or `frameworks/quality-rubrics.md` when voice or naturalness is actually material to the task; do not front-load a pattern checklist into unrelated work.

---

# Optional working instruments

Use `frameworks/practitioner-cards.md` when an explicit intermediate record would improve a complex task, handoff, or decision. Do not fill a card merely because a card exists.

Use [quality rubrics](frameworks/quality-rubrics.md) when the user asks for a structured review, when the output warrants a formal check, or when an audit would materially reduce error. Choose only the applicable sections and distinguish exploratory candidates from final artifacts. The [creative comparison criteria](frameworks/quality-rubrics.md#9-creative-exploration-and-candidate-selection) assess requested alternatives; the [completion criteria](frameworks/quality-rubrics.md#10-completion-and-decision-usefulness) assess whether the result serves the job. These are qualitative review aids, not validated scores or mandatory reading for every task.

Use `references/bibliography.md` only when source provenance, literature support, or deeper conceptual review is required. When the needed reference has a known intrinsic identifier such as `R23`, `C14`, or `A03`, prefer `scripts/get-knowledge.py --source <ID>` so the source record can be loaded without the rest of the ledger.

---

# Final validation

Before returning material work, check only the dimensions relevant to the current task:

- **Truth:** no invented facts or specificity.
- **Scope:** claims do not outrun the evidence.
- **Decision fit / completion:** the output completes the requested jobs and satisfies their useful-result criteria rather than substituting a generic workflow, caveat list, or account of work performed.
- **Proof proportionality:** claim strength matches available support.
- **Counterevidence / uncertainty:** material contradictions and unknowns remain represented in reasoning and surface when the recipient needs them.
- **Reader / environment fit:** audience-facing communication respects the recipient's state, relationship, surface, permissions, and information budget when those dimensions are material.
- **Artifact completeness:** audience-facing output performs the discourse functions required by the current job rather than merely containing the right facts. Where material, it orients the reader, provides enough understanding to judge relevance, makes the intended participation or next action legible, and closes or hands off the interaction naturally. These are functions, not mandatory sections: do not require a title, hook formula, CTA formula, gratitude, or other template element when the job does not need it.
- **Object / capability fidelity:** when the job introduces or explains an unfamiliar product, project, method, or other object, the final representation preserves enough supported domain-specific capability identity for the reader to understand what kind of work it actually enables. Generic operating discipline, safeguards, or implementation mechanics do not substitute for the object's domain capability.
- **Relational realization:** when wording materially encodes social relation, do not invent or erase familiarity, hierarchy, authority, obligation, responsibility, speaker identity, or community standing; if the material choice is genuinely underdetermined, do not silently classify the relationship.
- **Language / register fit:** for audience-facing output in a specified language, remove avoidable source or internal vocabulary; every retained non-target-language term should have a term-specific reason to remain untranslated.
- **Strategic coherence:** final communication expresses sufficiently resolved strategy; exploratory drafts remain identifiable as candidates and do not silently become adopted strategy or evidence.
- **Priority / role fidelity:** headlines, subject lines, hooks, first views, openings, examples, repetition, and other emphasis preserve the resolved primary value/message and the current touchpoint job. A lower-layer fact, proof item, specification, caveat, barrier, objection, commercial condition, metric, or representation requirement does not become the effective strategy merely through salience or repetition unless the higher role is independently supported.
- **Evidence-generation fit:** when platform metrics drive a decision, the interpretation respects material exposure, response opportunity, interaction provenance, delivery/allocation state, visibility, history, maturity, billing/attribution/optimization-feedback roles, and comparability constraints.
- **Quality beyond correctness:** when alternatives are requested, make their relevant differences and trade-offs clear; distinguish wording variants from different concepts. When a choice is requested and justified, recommend one for the current job without claiming unmeasured effectiveness.
- **Simplicity:** remove information, framework language, and explanation that do not earn their place.
- **Ethical persuasion:** preserve meaningful choice.

Do not expose internal reasoning, checklists, or supporting-file content unless the user asks for them or they are part of the requested deliverable.