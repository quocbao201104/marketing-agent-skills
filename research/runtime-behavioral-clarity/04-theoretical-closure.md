# Behavioral Instruction Clarity — Theoretical Closure

Date: 2026-09-18  
Frozen audit target: `e208024548905790c93adb00096e3130e64873ae`  
Branch: `audit/behavioral-instruction-clarity`

## Status

**THEORETICAL / STATIC RESEARCH COMPLETE FOR THIS PASS**

Live synthetic execution is intentionally deferred. The frozen synthetic corpus remains a specification and regression artifact, not evidence of production behavior. Real-task validation is reserved for later use on actual work episodes.

This document closes the theory layer of the behavioral-instruction-clarity audit. It generalizes the six-lane findings into a reusable model for writing and reviewing agent instructions without adding a new runtime architecture to Marketing Practitioner.

---

# 1. Research question

The practical question is not whether an instruction is semantically sensible or stylistically polished.

It is:

> Can a competent agent convert the instruction into the intended decision behavior without multiple reasonable readings producing materially different actions?

This creates a distinction between two defect classes.

```text
TEXT DEFECT
= the sentence is hard to parse or understand

BEHAVIORAL INSTRUCTION DEFECT
= the sentence may be understandable,
  but it does not determine the intended decision behavior tightly enough
```

A sentence can be grammatically clear and semantically true while still being behaviorally defective.

The audit therefore treats instruction quality as a property of **decision compilation**, not prose elegance.

---

# 2. Core thesis

## Decision-changing text must be behaviorally executable

Any text capable of changing an agent decision should expose enough of the following structure for the intended behavior to be recoverable:

```text
TRIGGER
→ DECISION OWNER
→ RELEVANT STATE
→ ACTION
→ BOUNDARY / INVARIANT
→ PRECEDENCE WHEN CONFLICTED
→ OUTPUT / DECISION DELTA
→ STOP / RETURN CONDITION
```

Not every instruction needs every field written explicitly. The requirement is semantic, not templatic.

A local sentence may omit an element when the composed runtime supplies it unambiguously. Conversely, repeating all fields does not guarantee quality if their relation remains ambiguous.

The relevant question is always:

> Could two reasonable executions of the composed instruction set produce materially different decisions?

If yes, and the difference is caused by instruction realization rather than genuine task uncertainty, the instruction is defective.

---

# 3. The instruction compiler model

The audit can be understood as testing a conceptual compiler from natural-language instruction to agent policy.

```text
NATURAL-LANGUAGE GUIDANCE
        ↓
1. identify open decision
        ↓
2. resolve trigger condition
        ↓
3. identify owner / authority
        ↓
4. read relevant state and evidence
        ↓
5. select permitted action
        ↓
6. preserve invariants and unaffected state
        ↓
7. resolve conflicts or retain uncertainty
        ↓
8. produce bounded decision/artifact
        ↓
9. stop or return to parent owner
```

A wording defect matters when it changes compilation at one of these steps.

The two confirmed findings in this audit are compiler defects of this form:

```text
F01
same intended threshold
→ two lexical realizations (`material`, `consequential`)
→ plausible threshold drift
→ different trigger behavior

F02
same intended boolean policy
→ ambiguous modifier attachment
→ different logical parse
→ different verification behavior
```

Neither defect required new domain knowledge or new architecture.

---

# 4. Behavioral instruction defect taxonomy

This taxonomy is intentionally narrower than a general writing-quality rubric. A defect belongs here only when it can alter execution materially.

## D1 — Trigger ambiguity

The agent cannot determine when a rule activates.

Examples:

```text
"when appropriate"
"when consequential"
"when needed"
```

These are not automatically defects. They become defects when no composed definition makes the threshold recoverable and different readings change action.

F01 is a trigger-ambiguity example.

---

## D2 — Boolean / modifier attachment ambiguity

A condition can be parsed into different logical expressions.

Example shape:

```text
A or B or C and D
```

Possible parses:

```text
A OR B OR (C AND D)
```

versus:

```text
(A OR B OR C) AND D
```

When the branches produce different actions, prose punctuation is not enough; decompose the policy.

F02 is this defect class.

---

## D3 — Implicit action

The trigger is identifiable but the agent is only told what to notice, consider, remember, or avoid, without an executable disposition.

Example:

```text
"Be mindful that provider state may change."
```

Possible actions include retrieve, warn, proceed, ask, defer, or do nothing.

A behavior-changing rule should expose which one applies.

---

## D4 — Missing boundary / invariant

The action is correct locally but its allowed scope is unclear.

Failure shape:

```text
correct local diagnosis
→ unauthorized upstream reopening
```

Examples attacked in this audit:

- local founder-sales stop → global pursuit stop;
- local linguistic evidence → relationship/authority redesign;
- platform delivery confound → rewrite strategy or creative globally.

These passed because the repository already preserves owners and local/global state boundaries.

---

## D5 — Ownership leakage

A specialist or local rule begins deciding a question owned by another layer.

Typical form:

```text
LOCAL FACT
→ promoted into GLOBAL DECISION
```

The correct repair is usually an ownership boundary or return path, not more domain detail.

---

## D6 — Precedence collapse

One easy-to-recognize attribute becomes an unjustified universal winner.

Examples:

```text
newer > older
more specific > broader
official > user
reviewed > provisional
private > upstream
local > global
```

The repository correctly avoids these universal shortcuts. Precedence instead composes actual scope, owner, authority, evidence, and material freshness.

---

## D7 — Epistemic inversion

The instruction permits an unsupported inverse conclusion.

```text
evidence does not support X
→ therefore not-X
```

or:

```text
state is not comparable
→ therefore creative is good
```

Good runtime guidance preserves the remaining hypothesis space rather than replacing one unsupported conclusion with its opposite.

---

## D8 — State-reopening leak

A changed local fact causes unrelated settled decisions to be reopened.

Correct behavior is:

```text
changed evidence
→ update affected decision/artifact
→ preserve unaffected state
```

not:

```text
changed evidence
→ restart strategy
```

---

## D9 — Unknown collapse

The instruction encourages completing a recommendation by filling undisclosed system state or unsupported hierarchy.

Example:

```text
feature is processed
→ feature must be most important ranking factor
```

A usable agent policy must preserve `UNKNOWN` as an executable result when evidence does not license a stronger claim.

---

## D10 — Example-as-rule leakage

An example supplies an incidental property that the agent promotes into the rule itself.

This is especially risky when the example is easier to imitate than the abstract decision condition.

Good examples identify which property is normative and which is incidental.

---

## D11 — Negative-only guard

A prohibition blocks one bad action without specifying the remaining legitimate path.

Example:

```text
"Do not rewrite the creative yet."
```

without:

```text
"First localize delivery/exposure state; then retain creative as one competing hypothesis."
```

Negative instructions are not inherently bad. They are insufficient when removing the prohibited action leaves the agent without a decision path.

---

## D12 — Sufficiency threshold without decision reference

Terms such as `enough`, `sufficient`, or `adequate` can become hidden fixed thresholds.

They are safer when tied to the decision:

```text
sufficient to distinguish the remaining actions
sufficient for truthful completion
sufficient for a mode-specific comparison
```

The audit retained `enough delivery history` as pressure rather than a confirmed defect because surrounding guidance operationalizes what comparability requires.

---

# 5. A rule-quality model

Instruction quality is not proportional to detail count.

A useful conceptual objective is:

```text
BEHAVIORAL RULE QUALITY
≈
DECISION SIGNAL
───────────────
INTERPRETIVE NOISE + CONTEXT COST
```

Where **decision signal** is information that changes:

- trigger;
- action;
- owner;
- allowed scope;
- evidence interpretation;
- precedence;
- stop condition.

And **interpretive noise** includes:

- redundant rationale;
- near-synonyms with different implied thresholds;
- mixed commands and explanations in one clause;
- examples whose normative property is unstated;
- warnings without a next action;
- duplicated rules with subtly different wording.

This aligns with the repository's existing minimum-sufficient-task principle:

```text
MINIMUM SUFFICIENT TASK SPECIFICATION
=
THE JOB
+
ONLY THE QUALIFIERS THAT CAN MATERIALLY CHANGE THE RESULT
```

The same principle applies internally to skill instructions:

```text
MINIMUM SUFFICIENT BEHAVIORAL INSTRUCTION
=
THE DECISION PATH
+
ONLY THE CONDITIONS / BOUNDARIES THAT CAN MATERIALLY CHANGE EXECUTION
```

This is not a shortest-text objective. Removing a necessary boundary can make shorter prose worse.

---

# 6. Canonical vocabulary as behavioral infrastructure

A term should become canonical when all three conditions hold:

1. it gates behavior repeatedly;
2. the distinction matters materially;
3. inconsistent synonyms can imply different thresholds.

`material` qualifies because the controller already defines it operationally.

A canonical term should not be introduced merely for conceptual neatness. Every additional controlled term creates context cost and another mapping burden.

Therefore:

```text
CANONICALIZE
when lexical variance changes execution

DO NOT CANONICALIZE
merely because multiple ordinary words describe the same idea
```

This explains why the bounded repair binds action gates to `material` at the controller rather than globally rewriting every occurrence of `consequential` in descriptive prose.

---

# 7. Decompose logic, not prose

When an instruction encodes boolean logic, precedence, or exception structure, natural language should expose the logic rather than rely on punctuation.

Bad executable shape:

```text
Do X when A, B, C, or D and E.
```

Better:

```text
Do X when A, B, or C.
Also do X when D and E.
```

This principle is narrow:

> Split clauses when the split removes a behaviorally material parse ambiguity.

It is not a rule that all complex sentences are bad.

---

# 8. Separate control plane from explanation plane

A skill often needs both:

- **control-plane text** — directly changes what the agent does;
- **explanation/evidence text** — helps understand why the rule exists or where it comes from.

Problems arise when these planes are mixed so tightly that rationale looks like another condition or an example looks like authority.

Useful structure:

```text
ACTION / POLICY
because / evidence / rationale
boundary / exception
```

The control plane should remain recoverable without requiring the agent to infer executable logic from the rationale.

This supports the skill-creation principle that `SKILL.md` should function as a compact control plane while detailed background stays in references.

---

# 9. Composed executability matters more than sentence-local completeness

A local sentence should not be judged in isolation when the parent controller clearly supplies missing semantics.

The audit repeatedly rejected false-positive defects where the full composition already made behavior deterministic enough.

Examples:

- platform activation is constrained by the controller's open-decision/minimum-read rules;
- local founder-sales stop results return to FS1 for global pursuit consequences;
- adaptation contributions inherit a shared owner and preservation contract;
- performance diagnosis inherits the platform state/exposure/comparability model.

Therefore static review should test:

```text
LOCAL SENTENCE
+
PARENT CONTROL PLANE
+
OWNER CONTRACT
+
APPLICABLE SPECIALIST RULES
```

not merely local wording.

This prevents needless duplication and control-plane bloat.

---

# 10. Boundary design: what changes and what must survive

A strong behavior-changing instruction makes its preservation semantics recoverable.

For a local repair:

```text
MAY CHANGE
= the implicated open decision / unsupported element

MUST PRESERVE
= unrelated settled state, supported meaning, authority, scope, and evidence status
```

The most important cross-repo pattern found by this audit is the prevention of **scope promotion**:

```text
LOCAL RESULT
!=
GLOBAL OWNER DECISION
```

This pattern appears in:

- Founder-led Sales;
- localization/adaptation;
- platform diagnosis;
- claims/editing;
- changed-state continuation.

The architecture is coherent because these domains already implement this invariant independently.

---

# 11. Precedence is multidimensional, not a total order

The audit found no need for a global precedence table.

The more faithful model is:

```text
1. identify the decision owner
2. check actual applicability / scope
3. determine binding authority
4. evaluate evidentiary support / provenance
5. apply freshness where current state can materially change the decision
6. if no justified winner remains, preserve conflict or uncertainty
```

A source can be newer but out of scope.
A source can be closer-scoped but non-authoritative.
A policy can govern style but not make a false statement true.
A user can authorize an editorial choice without proving a market fact.

This is why a universal scalar source score would lose important semantics.

---

# 12. Good instruction design preserves legitimate no-action states

Executable guidance must allow:

- proceed;
- retrieve;
- clarify;
- bound;
- preserve uncertainty;
- retain current state;
- stop local work;
- return to another owner;
- do nothing.

A rule set that always forces positive intervention encourages over-editing and false certainty.

The repository's uncertainty and owner-return semantics are therefore not fallback weaknesses; they are part of correct behavior.

---

# 13. Static audit standard

A static finding should be promoted only when all of the following hold:

1. the text can change a decision;
2. at least two readings are plausible in the composed runtime;
3. the readings produce materially different behavior;
4. the difference is not genuine task uncertainty;
5. existing owner/boundary/precedence guidance does not already disambiguate it;
6. a bounded repair exists that does not require speculative architecture.

This avoids lexical linting.

Words such as:

```text
should
consider
appropriate
material
consequential
enough
```

are not defects by themselves.

The unit of adjudication is the **behavioral branch**, not the vocabulary item.

---

# 14. Repair standard

The smallest valid repair changes the executable policy representation while preserving the intended decision architecture.

Preferred repair order:

```text
1. clarify canonical threshold
2. decompose ambiguous condition
3. state missing action
4. state missing invariant / owner return
5. state conflict disposition
6. only then consider architecture
```

Do not add a new owner, route, schema, or mandatory phase merely because wording is hard to execute.

For this audit, the confirmed defects stopped at steps 1–2.

---

# 15. Why synthetic cases are retained but not treated as proof

The additive corpus created during this work serves three limited purposes:

1. freeze the semantic distinction being repaired;
2. prevent later reviewers from changing the oracle after seeing outputs;
3. provide compact regression probes when implementation work resumes.

It does **not** establish:

- ecological validity;
- failure frequency;
- production reliability;
- causal improvement from the repair;
- superiority over another prompt or skill version.

Synthetic diagnostic cases are especially vulnerable to demand characteristics: the prompt can make the intended distinction easier to detect than it is in real work.

Therefore a synthetic green result would be weaker evidence than repeated correct behavior on naturally occurring tasks where the distinction is implicit rather than announced.

---

# 16. Relationship to Pressure Discovery

The existing Pressure Discovery methodology already separates:

```text
DIAGNOSTIC INJECTION
from
ECOLOGICAL PRESSURE
```

and treats repository-derived cases as unsuitable seeds for ecological performance claims.

This theoretical closure adopts that separation.

The current 10-case corpus is a **diagnostic/regression artifact** derived from the audit and must remain in that role.

Real-task validation should begin from operational episodes, not from these test prompts.

---

# 17. Relationship to task specification

The user-facing Task Specification Guide and this internal instruction-clarity model are structurally parallel.

For user tasks:

```text
JOB
+
MATERIAL QUALIFIERS
+
FIXED STATE / BOUNDARIES
```

For agent runtime guidance:

```text
OPEN DECISION
+
MATERIAL TRIGGER
+
ACTION
+
OWNER / BOUNDARY
+
CONFLICT / UNCERTAINTY DISPOSITION
```

Both reject maximal context as a default and both optimize for enough information to avoid materially wrong branching.

This provides a coherent repo-level principle:

> Add information when it changes the decision policy; do not add information merely because it is related to the topic.

---

# 18. Research conclusions

## C1 — Semantic correctness is necessary but insufficient

An instruction may express a true principle yet fail as an executable policy.

## C2 — The highest-value clarity work occurs at branch points

Clarifying rationale is lower leverage than clarifying where an agent chooses between actions.

## C3 — Canonical thresholds matter more than canonical vocabulary generally

Terminology should be standardized only where lexical variance changes the action boundary.

## C4 — Boolean decomposition is a legitimate runtime repair

When grammar permits two materially different logical parses, separate clauses are safer than explanatory prose around the same sentence.

## C5 — Local correctness requires scope preservation

A correct local result is still wrong if it changes a decision the local rule does not own.

## C6 — Precedence should preserve multiple dimensions

Authority, scope, evidence, freshness, and ownership are not safely reducible to one total ordering.

## C7 — `UNKNOWN`, conflict, no-change, and owner-return are valid executable outcomes

A competent system does not need to force every branch into an affirmative recommendation or modification.

## C8 — Static audit can justify bounded wording repair but not behavioral-performance claims

Observed behavior on real tasks remains a separate empirical question.

## C9 — Synthetic regression cases are specification locks, not ecological validation

Their value is in preserving intended distinctions and preventing oracle drift.

## C10 — Real tasks are the appropriate next evidence source

The most informative future analysis is not a larger synthetic benchmark. It is a collection of actual work episodes where the instruction distinction becomes naturally relevant and where resulting behavior can be inspected in context.

---

# 19. Closure disposition

This research pass is complete when separated into three layers:

```text
THEORY / STATIC AUDIT
COMPLETE

BOUNDED RUNTIME REPAIR
COMPLETE AT CONTROLLER LEVEL

REAL-TASK BEHAVIORAL VALIDATION
DEFERRED BY DESIGN
```

No further runtime expansion is justified by the current theoretical evidence.

Future edits should be driven by either:

- a new static contradiction/interpretation defect with a bounded proof; or
- a real-task failure episode that can be localized to instruction realization rather than missing knowledge, missing authority, execution variance, or evaluator preference.
