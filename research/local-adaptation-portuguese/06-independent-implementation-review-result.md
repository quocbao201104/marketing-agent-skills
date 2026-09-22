# Independent implementation review result — PT-LANG-ADDR-01

## Review target and provenance lock

Unit under review:

`PT-LANG-ADDR-01 — Portuguese second-person address-system realization`

Provenance used for this review:

```text
Frozen research target:
3269d2f4139123fa2a387a8e64611a193bee8c02

Independent research review:
ac70453b5d3c7770f5c099f7b63ed34e1a16a70c

Post-review bounded repair:
2f3c431a33cd6d80be7f589aa83ff8ff35f67641

Frozen runtime implementation target:
699bf9fa54eaa894dfd1ec6a293201fb8d6fc205
```

The branch head at the start of implementation review was exactly the frozen runtime implementation target. No commit after `699bf9fa54eaa894dfd1ec6a293201fb8d6fc205` was used as evidence that an implementation defect had been repaired.

The frozen runtime target adds the Portuguese contribution by appending to `skills/marketing-agent-skills/adaptations/localization.md`; its parent-to-target diff does not modify the controller, Chapter 07, `routing-index.json`, `get-knowledge`, or an existing local-adaptation unit.

This review does not repair runtime and does not close lifecycle state.

---

## Contract under review

The implementation must remain faithful to the frozen research design as repaired by `PT-IR-01`.

Promotion-bearing novelty:

```text
A. ADDRESS FORM
   != COMPLETE PERSON PARADIGM

B. EXPLICIT VOCÊ
   != NULL 3SG ADDRESS REALIZATION
```

Authority repair:

```text
PTLA10
= documented first-party policy

PTLA11 / PTLA12
= current scoped first-party usage

CURRENT FIRST-PARTY USAGE
!= DOCUMENTED FIRST-PARTY POLICY
```

The implementation is reviewed adversarially against those boundaries, not against an assumption that promotion was correct.

---

## 1. Promotion-bearing novelty attack

| Novelty | Adjudication | Implementation review |
|---|---|---|
| A. `ADDRESS FORM != COMPLETE PERSON PARADIGM` | PASS | Runtime explicitly blocks `tu -> automatic overt 2SG`, `você -> complete 3SG paradigm`, and `você -> automatic replacement of te`. It permits supported scoped composition without treating every mixed paradigm as valid. Unsupported drift remains repairable against applicable resolved state. |
| B. `EXPLICIT VOCÊ != NULL 3SG ADDRESS REALIZATION` | PASS | Runtime explicitly distinguishes overt `você` from null-3SG realization, rejects pragmatic equivalence from shared 3SG morphology, and blocks both automatic insertion of `você` and automatic deletion of an already-resolved explicit `você`. |

The runtime therefore implements two Portuguese-specific realization constraints rather than merely repeating generic Chapter 07 or the Spanish address-system logic.

---

## 2. Adversarial runtime behavior checks

| Check | Adjudication | Reason |
|---|---|---|
| `tu` is not encoded as always requiring overt 2SG agreement | PASS | Runtime states `TU != AUTOMATIC OVERT 2SG AGREEMENT EVERYWHERE` and repeats the guardrail without converting it into a reverse default. |
| `você` is not encoded as a full 3SG paradigm across verb/clitic/possessive forms | PASS | Runtime states `VOCÊ != AUTOMATIC COMPLETE 3SG PARADIGM ACROSS ALL FORMS` and limits repair to implicated treatment-sensitive forms rather than a full grammar module. |
| `você + te` is not auto-normalized merely because it is mixed | PASS | Runtime explicitly states `VOCÊ + TE != AUTOMATIC ERROR` and allows supported scoped composition. |
| Scoped `você +` tu-derived / 2SG-shaped forms are not auto-rejected | PASS | Runtime explicitly states scoped `você +` tu-derived / 2SG-shaped forms are not automatic corruption/error. |
| Mixed paradigms are not blanket-preserved | PASS | Runtime states `ATTESTED COMPOSITION != BLANKET PRESERVATION OF EVERY MIX` and `MIXED PARADIGM != AUTOMATICALLY VALID`. |
| Supported local composition is preserved when scoped evidence / approved state resolves it | PASS | Decision impact and preservation rules allow supported `tu / você` composition, agreement patterns, `você + te`, and analogous scoped composition as resolved state. |
| Unsupported paradigm drift remains repairable | PASS | Runtime allows repair against applicable policy, brief, approved wording, or other resolved scoped state; it does not equate mixed form with either automatic error or automatic validity. |
| Explicit `você` and null 3SG are not treated as pragmatically equivalent | PASS | The implementation encodes this as an explicit mechanism boundary and warns that inserting `você` is not guaranteed to be relationship-neutral. |
| Null subject is not treated as a missing-subject error requiring automatic `você` insertion | PASS | Guardrails preserve eligible resolved null realization and reject automatic insertion. |
| Explicit `você` is not automatically deleted when scoped/first-party state resolves it | PASS | Runtime preserves verified treatment forms / approved voice and rejects deletion based on false explicit/null equivalence. |
| `Brazil -> você`, `Portugal -> tu`, `Angola -> X`, `Mozambique -> X` is not a lookup | PASS | Country is explicitly denied as a target-variety or treatment lookup key; named-country mappings are prohibited. |
| `formal -> senhor/senhora` is not deterministic | PASS | Runtime explicitly prohibits `FORMAL = SENHOR / SENHORA` lookup. |
| Portuguese/Korea/Brazil/customer/formal/social-media/business nouns alone do not activate | PASS | Activation requires Portuguese output plus a material second-person treatment realization decision plus a surface that exposes that decision; noun/context traps alone are denied authority. |
| Portuguese outside Lusophone geography can load when realization is materially open | PASS | Scope is not inherently country-specific; applicability follows target-language realization and scoped state/evidence. |
| Lusophone market plus non-Portuguese output does not load | PASS | `TARGET LANGUAGE = PORTUGUESE` is a mandatory activation condition. |
| Address-neutral / nominal / UI surface with no second-person decision does not load | PASS | `DO NOT USE WHEN` excludes surfaces with no material second-person/addressee realization. |
| `seu/sua` ambiguity is not promoted into a Portuguese-specific resolver | PASS | Runtime explicitly leaves `seu/sua` under generic source-referent fidelity / ordinary Portuguese competence absent separate evidence. |
| Ordinary Portuguese grammar is not seized | PASS | Runtime excludes ordinary grammar unrelated to the treatment system and refuses to become a full conjugation, clitic, possessive, or proofreading module. |

No tested runtime behavior collapses the unit into a pronoun recommender, country resolver, full person-paradigm normalizer, or generic Portuguese grammar owner.

---

## 3. `PT-IR-01` bounded-repair preservation

### PTLA10

**PASS.** The runtime classifies PTLA10 as documented gov.br policy within its actual service-writing scope. It may resolve/freeze treatment only within that applicable scope. It is not promoted into a Brazilian population preference or `Brazil -> você` default.

### PTLA11 / PTLA12

**PASS.** The runtime classifies PTLA11 and PTLA12 as current scoped gov.pt usage evidence. It permits current first-party usage to be strong scoped evidence, and permits it to function as resolved state when the supplied wording/voice is actually approved/current for the surface.

The runtime does **not** relabel PTLA11/PTLA12 as:

- documented gov.pt policy;
- deliberate cross-surface policy;
- intentional audience-treatment policy.

It expressly states that observed cross-surface difference does not independently prove a documented or intentional cross-surface policy.

### First-party semantics

**PASS.** The implementation preserves the repaired authority model:

```text
APPLICABLE DOCUMENTED POLICY
-> may resolve/freeze treatment within scope

CURRENT FIRST-PARTY USAGE
-> may be strong scoped evidence / approved state if actually supplied
-> does not automatically prove organization-wide policy

FIRST-PARTY USAGE
!= population preference
!= country-wide default
```

No authority upgrade from current usage to organization-wide policy is present at the frozen runtime target.

---

## 4. Runtime evidence ledger adjudication — PTLA01–PTLA12

| Evidence ID | Adjudication | Boundary retained by implementation |
|---|---|---|
| PTLA01 | PASS | Comparative Portuguese variation is used against country/pronoun simplification, not to create `Portugal -> tu` or `Brazil -> você`. |
| PTLA02 | PASS | Explicit `você` versus null-3SG pragmatic distinction is used as a realization boundary; it is not converted into a ban on explicit `você` or a universal null default. |
| PTLA03 | PASS | Corroborates explicit/null treatment realization without creating a prestige hierarchy, deterministic `tu/você/senhor` scale, or country lookup. |
| PTLA04 | PASS | Supports variable `tu` agreement and blocks `tu -> overt 2SG` normalization; scoped evidence is not expanded into a Brazil-wide rule. |
| PTLA05 | PASS | Supports multiple Brazilian second-person subsystems and the inadequacy of a country label; no region-to-pronoun runtime lookup is introduced. |
| PTLA06 | PASS | Supports retention of `te` with `você` and blocks full-paradigm normalization; it is not turned into a universal `você -> te` rule. |
| PTLA07 | PASS | Supports contemporary scoped mixed 2SG object realization; runtime does not universalize the tested Brazilian scope or transfer it to other Portuguese varieties. |
| PTLA08 | PASS | Falsifies universal `você -> complete 3SG paradigm`; the Cabinda evidence is not promoted to Angola generally or transferred cross-variety. |
| PTLA09 | PASS | Supports pragmatic plurality of `você` in scoped Angolan data; it is used against a global formality/hierarchy lookup rather than to create one. |
| PTLA10 | PASS | Retained as documented first-party gov.br service-writing policy in its actual scope only. |
| PTLA11 | PASS | Retained as current scoped gov.pt usage showing null/3SG-style direct-reader realization; explicitly not documented policy evidence. |
| PTLA12 | PASS | Retained as current scoped gov.pt usage showing a `tu` system on the On@18 surface; explicitly not documented policy or proof of intentional audience assignment. |

**Ledger result:** `PTLA01–PTLA12 = PASS`.

The runtime keeps the evidence-to-decision boundary intact: linguistic evidence establishes possible mechanisms and falsifies unsafe normalizations; scoped first-party evidence can preserve applicable supplied state; none of it becomes population preference, marketing lift, a country pack, a hierarchy resolver, or a complete paradigm scorer.

---

## 5. Eval / adversarial set P1–P16

Each case in `evals/local-adaptation-portuguese-v0.md` was adjudicated against the frozen runtime implementation.

| Case | Adjudication | Implementation result |
|---|---|---|
| P1 | PASS | Positive activation requires Portuguese plus a material second-person realization decision; unit stays bounded to Chapter 07 realization. |
| P2 | PASS | Country/language/customer/context nouns alone do not activate the unit. |
| P3 | PASS | Negative noun/context traps do not manufacture treatment state. |
| P4 | PASS | Weak or insufficient evidence cannot force pronoun/paradigm normalization. |
| P5 | PASS | Supplied current/approved first-party wording may act as scoped realization state without being promoted beyond its evidence class. |
| P6 | PASS | Applicable documented first-party policy can resolve/freeze treatment within its actual scope and outranks generic fallback speculation. |
| P7 | PASS | Explicit `você` and null-3SG realization remain separate; no automatic insertion/deletion by morphology equivalence. |
| P8 | PASS | Runtime lifecycle remains `REVIEW STATE = provisional`, `USAGE STATE = active`; the two states are not conflated. |
| P9 | PASS | Country labels do not become treatment defaults or variety selectors. |
| P10 | PASS | Formality/relationship descriptors do not become deterministic `senhor/senhora`, `tu`, or `você` mappings. |
| P11 | PASS | Portuguese outside Lusophone geography can load when a material Portuguese treatment-realization dependency exists. |
| P12 | PASS | Lusophone geography with non-Portuguese target output does not activate the Portuguese unit. |
| P13 | PASS | Address-neutral / nominal / UI realization with no material second-person decision does not load. |
| P14 | PASS | `seu/sua` ambiguity remains generic source-referent fidelity; no Portuguese-specific possessive resolver is created. |
| P15 | PASS | Ordinary Portuguese grammar remains outside this unit. |
| P16 | PASS | Repaired semantics are encoded: documented policy may resolve within scope; current scoped usage may preserve supplied/approved local state but is not relabeled as policy or intentional cross-surface audience assignment. |

### P16 repaired-semantics check

The eval no longer requires the pre-repair inference that PTLA11/PTLA12 demonstrate an intentional documented cross-surface policy. Its runtime-compatible meaning is:

```text
ONE ORGANIZATION ECOSYSTEM
CAN EXHIBIT DIFFERENT SCOPED TREATMENT REALIZATIONS

!=

THE FROZEN SOURCES PROVE
A DOCUMENTED INTENTIONAL CROSS-SURFACE POLICY
```

The policy-supplied case and usage-only case are separated. The old overclaim is not encoded as the expected result.

**P1–P16 result:** all `PASS`.

---

## 6. Architecture adjudication

Existing architecture is sufficient. The frozen implementation reuses the Localization / Chapter 07 owner and the already-defined semantic route `adapt-localization.relationship-realization`. At the frozen target, `routing-index.json` already maps that route to `adaptations/localization.md` / `## Relationship realization`.

```text
owner:
Localization / Chapter 07

route:
adapt-localization.relationship-realization
```

| Architecture check | Adjudication |
|---|---|
| existing owner sufficient? | YES |
| existing route sufficient? | YES |
| new owner introduced? | NO |
| new route introduced? | NO |
| shared primitive introduced? | NO |
| country/variety resolver? | NO |
| paradigm scorer? | NO |
| hierarchy/formality resolver? | NO |
| controller changed? | NO |
| Chapter 07 changed? | NO |
| routing-index changed? | NO |
| get-knowledge changed? | NO |

The parent-to-frozen-target diff contains only the Portuguese append to `skills/marketing-agent-skills/adaptations/localization.md`. More importantly, the appended semantics themselves do not simulate a hidden resolver: country, variety, hierarchy, formality, full paradigm, and ordinary-grammar inference are all explicitly denied as decision authority.

**Architecture result:** PASS.

---

## 7. Regression adjudication

Regression was checked semantically, not only by changed-file count.

| Existing unit | Adjudication | Why Portuguese does not change its meaning/routing/scope |
|---|---|---|
| VN-LANG-REL-01 | PASS | Existing Vietnamese block remains unchanged and Vietnamese-gated. Portuguese adds no shared resolver/controller that can reinterpret Vietnamese relationship realization. |
| JP-LANG-HON-01 | PASS | Existing Japanese honorific semantics and activation remain unchanged and Japanese-gated; Portuguese composition rules do not alter Japanese honorific ownership. |
| JP-LANG-PERM-01 | PASS | Existing Japanese permission-related semantics remain unchanged; no Portuguese route or primitive seizes or rewrites that dependency. |
| ES-LANG-ADDR-01 | PASS | Spanish remains independently Spanish-gated. Portuguese reuses the owner/route but does not import Portuguese evidence into Spanish or redefine the Spanish address-system contract. |
| KO-LANG-SPEECH-01 | PASS | Korean remains Korean-gated with its own speech-level boundaries. Portuguese introduces no hierarchy resolver, shared speech-level primitive, or controller change. |

The Portuguese unit is additionally gated by a material Portuguese second-person treatment-realization decision. Reusing the existing owner/route is composition under the existing architecture, not a semantic mutation of prior local units.

**Regression result:** PASS.

---

## 8. Lifecycle adjudication

Frozen runtime state:

```text
REVIEW STATE = provisional
USAGE STATE  = active
```

### REVIEW STATE = provisional

**PASS.** This is provenance-correct at the frozen runtime target. The research candidate had already received independent research review and bounded repair, but the runtime implementation itself had not yet received this independent implementation review at `699bf9fa54eaa894dfd1ec6a293201fb8d6fc205`.

An earlier independent **research** review is not the same event as an independent **implementation** review. Therefore `provisional` does not falsely claim implementation-review completion.

### USAGE STATE = active

**PASS.** `active` is a separate usage disposition and does not imply that `REVIEW STATE` is already `reviewed`. The frozen runtime therefore keeps lifecycle provenance and runtime usage status distinct.

This review commit must not change:

```text
REVIEW STATE
provisional -> reviewed
```

Any lifecycle closure after a passing implementation review belongs in a separate post-review commit.

**Lifecycle result:** PASS.

---

## 9. Findings

None.

No material defect was found that requires a bounded runtime repair. In particular, no finding was found for:

- promotion novelty collapse;
- `tu`/agreement over-normalization;
- `você` full-paradigm inference;
- mixed-composition blanket normalization or blanket preservation;
- explicit/null equivalence;
- country/variety lookup;
- hierarchy/formality lookup;
- PTLA11/PTLA12 authority inflation;
- P16 pre-repair wording leakage;
- architecture expansion;
- regression into existing local-adaptation units;
- lifecycle provenance confusion.

---

## 10. Review commit boundary

This independent implementation review records adjudication only.

It does **not**:

- modify runtime implementation;
- modify the Portuguese evidence ledger;
- modify P1–P16;
- repair any finding;
- change owner/route/controller architecture;
- change `REVIEW STATE` from `provisional` to `reviewed`;
- perform lifecycle closure.

---

# FINAL VERDICT: PASS
