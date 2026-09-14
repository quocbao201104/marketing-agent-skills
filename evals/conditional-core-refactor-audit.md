# Conditional Core Refactor Audit

Status: static design, migration map, and paired review contracts. No live model or subagent runs. Base: v1.9.2, commit `c16fcfd3bea5043a541c319040753709204eea11`.

## Problem and bounded correction

INPUT / TASK: rewrite a supplied caption with settled meaning, facts, voice, and interaction; no delegation or interrupted work.

CURRENT REPRESENTATION: loading the 5,449-word controller also delivers detailed subagent coordination, identity/sales/platform boundary examples, and task-specific final-review dimensions.

FAILURE IN ORGANIZATION: conditional detail occupies the common instruction body even when its condition is false. The agent must distinguish these branches while executing a sufficient narrow request. This is observable instruction exposure, not demonstrated causal evidence of model confusion or the earlier escalation.

DECISION CONSEQUENCE: shortening the common body could reduce unrelated guidance, but hiding an activation condition could also cause the relevant guard to be missed before a decision. Preserve the direct-path safeguards and the conditions for reading specialist detail.

SMALLEST CORRECTION: retain one controller, its jobs, index, specialist ownership, and common safeguards. Consolidate repeated explanations; relocate coordination detail into one conditional reference and specialist/review detail into existing references. Add no independent skill, mandatory support pass, or new routing subsystem. Treat the controller and retrieval-boundary change as Level 2; the approved design authorizes this bounded physical reorganization.

## Migration map

Original locations below refer to the base revision. Destinations are relative to the installed skill root. Each condition must be recognizable from the controller before the dependent decision.

| Original section | Common-body responsibility | Detailed destination and reading condition |
| --- | --- | --- |
| Purpose; Runtime controller | Identify all active outcomes; execute sufficient tasks; resolve actual dependencies and return | No additional prerequisite |
| Decision-local role steering; strategy invariant; role-composition bullets | One common role boundary and local repair rule, including cross-surface accumulation | Existing Chapter 04 examples only when the role/expression decision needs specialist guidance |
| Planning and decision checkpoints; uncertainty | Materiality, available authority, smallest necessary question, bounded result, independent continuation | `references/work-coordination.md#planning-and-scope-changes` when dependencies or scope are difficult to manage |
| Keeping multi-step work coherent | Retain outcomes/status, decisions/roles/scopes, evidence, return point; repair affected work; reconcile resumption | `references/work-coordination.md#continuation-and-recovery` when recovery or retained-state management remains unclear |
| Coordinating subagents when useful | Availability, permission, and useful decomposition before delegation | `references/work-coordination.md#coordinating-subagents-when-useful`, before making assignments when delegation is chosen |
| Useful completion by job | Retain seven useful-result criteria in the final section | No mandatory rubric read |
| Retrieving the relevant knowledge | Index ownership, bounded selectors, denied helper fallback, delivered-content integrity | No new retrieval prerequisite |
| Source/scope/counterevidence/uncertainty invariants | Supported specificity and first-person claims, evidence scope, non-independence, causal limits, unknowns | Existing evidence guidance when a methodological question remains |
| Knowledge table and composition boundaries | Direct namespaces; enough activation and owner distinctions to choose before acting | `references/operating-guide.md` relevant specialist heading only when boundary, subroute, or handoff state remains unclear |
| Audience-facing content-selection gate | Local sufficiency, capability identity, material qualifications, inclusion versus strategic role, natural language and supported relationships | `references/operating-guide.md#content-selection-and-realization` when selection or realization remains unclear; specialist Chapter 04/page/email ownership continues |
| Optional instruments | Explicit conditions for cards, rubrics, provenance, and artifact planning | Existing references by relevant section only |
| Final validation | Truth, scope, completion, actual communicated meaning, and proportionate correction | Relevant `frameworks/quality-rubrics.md` sections for deeper review; platform evidence details under diagnosis review |

## Paired static review contracts

Review the proposed core with only the indicated excerpt, then with its surrounding reference. Record structural/reasoning findings separately from executable verification.

### P01 - Sufficient narrow writing / missing interaction

A supplied caption rewrite with fixed message, voice, facts, and next action completes from the core without a support read. An unfamiliar-product introduction with facts but an unresolved invitation retains enough concrete capability and uses the relevant interaction guidance. Missing interaction is not repaired by dumping internal labels or safety mechanics into the copy.

### P02 - Local foregrounding / strategic promotion

A size specification may lead a scale clarification while retaining its supporting role. A general campaign email cannot infer a size-led promise from earlier accepted ad/PDP placements or from its own candidate hook. Supported promotion within authority remains available; repair is local when support is absent.

### P03 - Delegated choice / missing fact or authority

A delegated editorial choice proceeds within scope. Delegation does not establish empirical assumptions or authorize an external commitment outside scope. Missing material input gets a bounded recommendation/question before dependent work; independent outcomes continue and silence is not approval.

### P04 - Straightforward continuation / difficult recovery

Available state suffices for direct continuation. An incomplete summary triggers bounded recovery, retaining the adopted value, local role, scope, and source basis; unrecoverable material state remains bounded or is clarified. No universal record template or automatic coordination read is required.

### P05 - Scope change / cancellation or pause

Changed evidence repairs dependent artifacts before reuse while preserving unaffected claims. A cancelled deliverable leaves active work; a paused one is retained for later but is not counted as current incomplete execution. Other requested outcomes survive a narrowed subtask.

### P06 - New identity / approved production

Before selecting a new identifying cue, establish audience, intended recognition, and deployment inputs and use relevant identity guidance. A project name/function is not a complete brief. Approved export or resizing remains direct; provisional sketches stay candidates and selected assets are checked in required uses.

### P07 - Account commitment / settled wording

Unresolved account-specific pursuit or commitment enters founder-sales; default commercial-system design remains separate. Settled buyer terms needing expression return to copy. Price, POC, security, and other nouns alone do not select an owner.

### P08 - Causal question / descriptive discrepancy

A causal question routes to Chapter 05 before tactical changes and preserves measurement comparability. A descriptive field mismatch remains descriptive. Paying a creator does not alone establish paid-media delivery.

### P09 - Platform fact / broader environment question

A platform-specific field question can enter that platform namespace directly. A Facebook Group introduction with unresolved participation uses its Group/community guidance; missing external rules do not prevent packaged reads or establish local rules. Verify material destination rules before final representation where available.

### P10 - Ordinary writing / consequential relationship

Natural target-language copy preserves supported voice without a broad localization read. A materially unresolved relationship, authority, obligation, identity, or responsibility implication enters Chapter 07 or stronger scoped local evidence. Compression preserves supported beneficiary/object/responsibility relations; qualifications narrow claim strength.

### P11 - Local work / permitted delegation

Simple or nondelegable work stays local. When useful delegation is chosen and permitted, read only the coordination heading before assignments; preserve action limits, edit ownership, evidence assessment, integration, and recovery from failure. Continuation alone does not load subagent guidance.

### P12 - Sufficient structure / unresolved artifact architecture

A supplied sufficient report structure executes directly. An open document-use/representation decision reads the existing report guidance; an HTML section is relevant only to open implementation/delivery choices. Format and task size do not create approval gates.

### P13 - Normal completion / deeper review

All seven jobs retain useful completion criteria. Normal completion needs no formal rubric. A requested structured review uses relevant dimensions, keeps exploratory and final status distinct, and does not mistake static rubric judgments for measured efficacy.

### P14 - Available helper / denied or incomplete read

Known logical routes use the existing index and helper when allowed. A denied helper falls back to bounded index-directed reading. Missing material content in a truncated response is recovered before use; irrelevant truncation does not cause wholesale rereads. A resolved dependency returns to the pending job.

## Verification record

### Static review findings

The core and each new conditional heading were inspected independently, with the surrounding reference used to check applicability. The actual helper outputs for `copywriting.editing`, `email.continuity`, and `brand-identity.exploration` were also read with the revised core. Indexed knowledge and selectors themselves were unchanged.

| Contracts | Static result and relevant boundary |
| --- | --- |
| P01, P13 | Sufficient work remains direct; the core retains local understanding, domain capability, all seven useful-result criteria, and proportionate validation. The content-selection support condition is specifically uncertainty in applying inclusion/local sufficiency, not every open writing choice. |
| P02 | The four decision-local steering paragraphs remain verbatim. Core handoff scope and whole-artifact validation retain the distinction between local prominence and broader strategy; the email continuity excerpt agrees. |
| P03 | The core retains materiality, delegated selection versus empirical support, smallest necessary input, independent continuation, and external-action authority. The editing excerpt allows supported claim repair while preserving fixed wording and wider decision boundaries. |
| P04, P05 | The core alone retains role/scope, return point, changed-evidence repair, cancellation/pause distinctions, and reconciliation. The recovery heading adds record detail without including subagent instructions. |
| P06 | The core establishes identity inputs and specialist reading before cue choice; the exploration excerpt keeps alternatives provisional and rejects compulsory exploration or unsupported geometry claims. Approved production remains direct. |
| P07, P08 | Account-specific versus default-system ownership and causal versus descriptive questions remain visible before routing. The operating guide now has a bounded founder-sales heading. A compact metric-condition rule was retained in the core so optional rubric loading does not become the only protection before a metric-based decision. |
| P09, P10 | Direct platform entry, the Group participation trigger, material destination rules, and consequential language/relationship routing remain in the core. Supported relationships and natural-language constraints still apply on the direct path. |
| P11 | Delegation must be chosen, available, permitted, and justified before the coordination read and assignments. The moved assignment, evidence-assessment, integration, and failure-handling paragraphs remain intact. No actual agent was invoked. |
| P12 | Open artifact structure/use still activates the existing report reference; a sufficient structure does not. HTML guidance remains conditional on an implementation/delivery question. |
| P14 | Index ownership, selector boundaries, delivered-content integrity, denied-helper fallback, and return to the pending job remain in the core. Helpers resolved the three inspected routes; policy denial and truncation controls were assessed by reasoning, not live host experiments. |

Two review corrections were made before handoff: retained a minimal exposure/measurement/comparability requirement in the core, and aligned the operating-guide introduction with its new content-selection entry condition so it does not contradict the controller or become a mandatory hop for all writing.

### Initial refactor verification

The first repository verification run reached the UTF-8 check and failed because shortening the prose removed the two Unicode sentinel characters required by `scripts/verify.ps1`. The stored text was valid UTF-8. Restored meaningful inequality and dependency-arrow notation in the core; left the verifier unchanged. Subsequent full verification passed. Final verification and integrity results are recorded below after the last edits.

The common body remains one skill with six main sections. Its word count changes from 5,449 to 2,788 (48.8% lower, counted by whitespace, including unchanged metadata). This is a textual exposure measure, not a tokenizer measurement or quality result. No live model/subagent runs, efficacy claims, version bump, commit, or release publication are part of this refactor.


Final results:

- Full `scripts/verify.ps1`: PASS, including package validators, routing mechanics, 289 logical routes / 262 evidence sources, corpus validation, harness unit tests, Episode 01 preflight, and UTF-8/generated-artifact hygiene.
- `git diff --check`: PASS.
- All six task files retain UTF-8 without BOM, CRLF, and no trailing whitespace. Checked 27 local links and existing incoming core anchors; all resolve.
- The six-section core retains the decision-local steering paragraphs verbatim. The standalone recovery slice excludes delegation instructions; moved subagent coordination paragraphs remain intact.
- Compared SHA-256 hashes against the pre-edit inventory: 527 unrelated existing files, including the five pre-existing untracked work-episode files, are unchanged. Routing metadata, helpers, indexed handbook sections, and release metadata are unchanged.

These results establish structural validity and the documented static reasoning coverage. They do not establish how often a host/model follows the revised reading conditions or whether marketing outcomes improve.

## v2.0.0 wording and release follow-up

The initial verification above records the pre-release refactor. The subsequent authorized release updates skill/plugin metadata, current installation links, README, and changelog to v2.0.0 and publishes the complete package.

Before release, tightened three instruction groups:

- Knowledge reading begins from a concrete unresolved question and the knowledge needed to answer it; sufficient supplied inputs proceed directly. P01/P14 retain the direct path and bounded retrieval; exploration may still start with a bounded inspection without a predetermined commercial decision.
- Coordination entry conditions identify unresolved dependency order, affected scope, retained state, or return-point recovery. P04/P05 retain direct continuation with sufficient state and conditional support only for the remaining management question. The reference headings use the same conditions as the core.
- Communication review compares the whole artifact's headline, body, examples, imagery, emphasis, and action with the adopted message and touchpoint job. P02/P13 distinguish a materially changed premise from legitimate local foregrounding; exploratory artifacts are judged against their candidate assumptions rather than required to have an adopted final strategy.

Final core length: 2,841 whitespace-delimited words including metadata, versus 5,449 at v1.9.2 (47.9% reduction). These counts describe the document, not model token use or behavior. Final release verification is recorded below after execution.

Release preparation verification: full `scripts/verify.ps1` PASS (138 pressure-discovery, 90 behavioral-harness, and 33 work-episode unit tests; 261 total), with route/source validation, corpus checks, and hygiene checks. All 12 release/refactor files pass encoding/line-ending integrity; 75 local links and incoming core anchors resolve. SHA-256 comparison preserves 521 unrelated pre-existing files, including all five pre-existing untracked files. A 69-file portable ZIP was built and validated; its core and new coordination reference match the source bytes. Staged diff validation passes. No live model or subagent evaluation was performed.
