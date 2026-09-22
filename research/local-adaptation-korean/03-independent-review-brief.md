# Korean Local Adaptation — Independent Adversarial Review Brief

Status: **FROZEN REVIEW CONTRACT**  
Review target: `fcebad983691851d75017487e4f650aff8a5512e`  
Target artifacts:

```text
research/local-adaptation-korean/01-design-freeze.md
research/local-adaptation-korean/02-evidence-ledger.md
```

This review brief is committed after the frozen target. It defines how the target is judged; it is not retroactive evidence that the frozen candidate already satisfies the contract.

## 1. Reviewer role

Act as an **INDEPENDENT ADVERSARIAL LOCAL-ADAPTATION REVIEWER** for the Korean candidate in Marketing Practitioner.

Do not defend the candidate.

Do not modify the repository.

Do not implement the unit.

Do not broaden the task into a Korea market profile, Korean culture guide, business-etiquette guide, or full Korean honorific grammar.

Do not recommend a new country pack, hierarchy graph, formality score, speech-level resolver, route family, or controller primitive merely because Korean honorification is complex.

Your job is to determine whether the frozen evidence justifies `KO-LANG-SPEECH-01` and whether it composes safely with the already-released Chapter 07 + VN/JP/ES local-adaptation architecture.

## 2. Primary questions

Answer all of the following:

1. Does `KO-LANG-SPEECH-01` represent a real Korean-specific realization mechanism that generic Chapter 07 plus the existing VN/JP/ES contributions do not already fully encode?
2. Is the novelty specifically sentence-ending addressee speech-level realization rather than the broad fact that Korean has honorifics?
3. Does the candidate correctly distinguish formality/register from addressee respect without inventing a new global speech-level score?
4. Does same-listener style shifting create a material decision delta rather than merely documenting stylistic variation?
5. Can the unit distinguish legitimate `하십시오체 ↔ 해요체` shifting from accidental register drift?
6. Does the candidate avoid seizing subject/object honorification decisions that belong outside its narrow scope?
7. Can the existing route `adapt-localization.relationship-realization` express the mechanism without a Korea-specific resolver or new owner?
8. Are any evidence-ledger claims broader than the cited Korean sources actually support?
9. Should the proposed unit be promoted, narrowed, split, or rejected?

## 3. Files to read

Start with the frozen target only:

```text
research/local-adaptation-korean/01-design-freeze.md
research/local-adaptation-korean/02-evidence-ledger.md
```

Then read only current runtime surfaces materially required to test composition:

```text
skills/marketing-agent-skills/SKILL.md
skills/marketing-agent-skills/handbook/07-international-marketing-and-ethics.md
skills/marketing-agent-skills/adaptations/README.md
skills/marketing-agent-skills/adaptations/localization.md
skills/marketing-agent-skills/routing-index.json
skills/marketing-agent-skills/scripts/get-knowledge.py
```

Inspect existing VN/JP/ES contributions specifically to test novelty and regression boundaries.

Read other chapters only if a concrete adversarial case requires their owner/state semantics.

Do not use later commits after `fcebad983691851d75017487e4f650aff8a5512e` as evidence that a frozen defect was already solved.

## 4. Promotion standard

The Korean unit is valid only if the reviewer can sustain:

```text
LOCAL-SPECIFIC MECHANISM
+
MATERIAL DECISION DELTA
+
GENERIC OWNER DOES NOT ALREADY KNOW
THE TARGET-SPECIFIC MECHANISM
=
VALID ADAPTATION
```

Reject the unit if Chapter 07 plus supplied task evidence and existing VN/JP/ES knowledge can already make the correct Korean decision reliably without Korean-specific sentence-ending knowledge.

Do not count `models sometimes make Korean politeness mistakes` as promotion evidence by itself.

## 5. Evidence adjudication

Adjudicate every source record `KOLA01`–`KOLA11` as:

```text
PASS
PARTIAL
FAIL
```

For each `PARTIAL` or `FAIL`, identify the exact unsupported, stale, scope-mismatched, or over-broad claim.

Special scrutiny:

- `KOLA01`–`KOLA04` carry the primary addressee-speech-level and style-shifting burden.
- `KOLA05`–`KOLA06` establish the boundary between addressee speech level and subject/object honorification; they must not silently create a second Korean unit.
- `KOLA07` is first-party organization policy only; it must not become a Korean population norm.
- `KOLA08` is advertising-distribution evidence; it must not become best practice or causal effectiveness.
- `KOLA09` is bounded experimental response evidence; it must not become conversion or universal-channel guidance.
- `KOLA10` is a boundary against simplistic `사물존대` lookup rules, not a promoted mechanism.
- `KOLA11` must defeat, not justify, an executable hierarchy resolver.

## 6. Required attacks on KO-LANG-SPEECH-01

Evaluate K1–K16.

### K1 — approved 하십시오체

```text
TARGET: Korean
APPROVED ORGANIZATION/SURFACE STATE: 하십시오체
NO OTHER SPEECH-LEVEL DIMENSION OPEN
```

Required behavior: do not reopen the resolved ending system merely because the Korean unit exists.

### K2 — approved 해요체

Same construction as K1 with `해요체`.

Required behavior: preserve.

### K3 — same brand, different surfaces

```text
policy / restrictions = 하십시오체
requests / explanations = 해요체
```

Required behavior: preserve scoped first-party state; do not normalize the entire organization to one speech level.

### K4 — intentional style shift

Same speaker and same listener shift `하십시오체 ↔ 해요체` with supported interaction/discourse function.

Required behavior: preserve the shift. Surface consistency alone is not repair authority.

### K5 — accidental style drift

Construct Korean copy where:

```text
resolved voice = 해요체
no stance / audience / interaction shift
no first-party or discourse evidence supports a change
```

and the draft randomly jumps into `해라체` and/or `하십시오체`.

Required behavior: repair the drift. `Mixed != automatic error` must not become `mixed = always preserve`.

### K6 — user asks "make it more formal"

Required behavior: do not automatically increase addressee deference, hierarchy, or interpersonal distance. Test whether the unit can preserve the resolved relationship while handling register/formality.

### K7 — user asks "make it friendlier"

Required behavior: do not automatically downgrade to `해체`. Friendly stance is not proof of a low-address relationship.

### K8 — title / banner / button / nominal form

Example:

```text
카드 연결하기
```

Required behavior: no Korean speech-level detour when no finite addressee sentence-ending decision exists.

### K9 — honored third-party subject, listener ending already fixed

Only `-시-` / subject honorification is materially open.

Required behavior: `KO-LANG-SPEECH-01` must not seize the decision merely because honorification exists in the sentence.

### K10 — subject honorification and 해요체 coexist

Construct a clause where subject honorification and addressee speech level are both grammatical and intentional.

Required behavior: do not treat the co-occurrence as redundant `double politeness`; keep the two target dimensions distinct.

### K11 — inanimate/customer-service honorification edge

Use examples in the class of `객실이 없으세요` or a genuinely indirect-honorification context.

Required behavior: do not convert `KOLA10` into a binary `inanimate + -시-` lookup. Keep ordinary grammatical analysis and the candidate's narrow scope.

### K12 — 압존법 hierarchy cue

Context includes a senior listener and another senior referent.

Required behavior: no automatic honorification suppression based on rank ordering. No hierarchy graph.

### K13 — Korean outside Korea

Korean-language support is written for users in the United States, Vietnam, or another non-Korea market. Speech-level realization is materially open.

Required behavior: language realization may activate the unit; Korea-market membership is not required.

### K14 — Korea market, English output

Required behavior: no Korean speech-level activation merely because the campaign is in Korea.

### K15 — relationship known, speech level unresolved and unavoidable

No scoped organization/community/surface evidence resolves the ending choice.

Required behavior: do not invent:

```text
standard Korean → 하십시오체
marketing → 해요체
customer → 하십시오체
```

Preserve or expose the unresolved dependency according to Chapter 07.

### K16 — Korean noun with no relationship decision

Task mentions Korean/Korea, but no finite sentence-ending addressee choice exists.

Required behavior: no load.

## 7. Novelty attack against JP-LANG-HON-01

The reviewer must explicitly test whether Japanese knowledge makes the Korean unit redundant.

`JP-LANG-HON-01` already distinguishes:

```text
ADDRESSEE
!= ACTOR / REFERENT
!= ACTION TARGET
```

That is not enough by assertion alone. Test the counterfactual:

```text
REMOVE ALL KOREAN-SPECIFIC KNOWLEDGE
KEEP:
- Chapter 07
- JP-LANG-HON-01
- JP-LANG-PERM-01
- VN-LANG-REL-01
- ES-LANG-ADDR-01
- task-specific relationship / voice evidence
```

Can the system still reliably know that:

1. `격식체` is not one higher respect setting than `비격식체`?
2. a same-listener `하십시오체 ↔ 해요체` shift may be legitimate rather than drift?
3. `make it more formal` does not itself authorize a relationship/honorification change?
4. a finite addressee ending can be already resolved while subject/object honorification remains separately open?

If yes, reject the Korean unit. If no, the novelty survives.

## 8. Formality-scale attack

Try to force the candidate into a scalar such as:

```text
해라체 < 해체 < 하게체 < 해요체 < 하오체 < 하십시오체
```

or any similar single ordering.

Required behavior: reject the scalar. The candidate should encode bounded distinctions and evidence-driven realization, not a universal numerical or ordinal politeness score.

## 9. First-party-state attack

Use a current organization rule that fixes a speech level for a specific surface.

Required behavior:

```text
APPLICABLE FIRST-PARTY POLICY
→ RESOLVED STATE WITHIN ITS ACTUAL SCOPE
```

Broader Korean evidence must not reopen it merely because another speech style is also grammatical or common elsewhere.

Then test a deliberately bad organization rule that conflicts with ordinary grammatical realization. Organization authority may choose tone/style; it does not make ungrammatical morphology valid. The existing controller should surface the conflict rather than require a new Korean precedence engine.

## 10. Marketing-evidence attack

Attack both forbidden upgrades:

```text
KOLA08 distribution
→ use the most frequent style
```

and

```text
KOLA09 favorability result
→ use 해요체 for higher conversion
```

Both must fail.

The valid use of these sources is bounded:

```text
speech-level choice can vary materially by context
and may affect measured audience response
```

not:

```text
therefore one universal style wins
```

## 11. Non-final / address-neutral attack

Use KOLA07 and KOLA08 to test surfaces with no finite ending.

Required behavior:

```text
NO MATERIAL ADDRESSEE ENDING DECISION
→ NO LOAD
```

But do not let this become:

```text
IF SPEECH LEVEL IS HARD
→ REWRITE EVERYTHING AS NOUNS / -기
```

If direct interpersonal wording is central to the communication job, the system must not hide an unresolved speech-level dependency behind awkward nominalization.

## 12. Ordinary-grammar boundary

Identify at least three Korean errors that are **not** `KO-LANG-SPEECH-01` failures even if they occur in customer-facing Korean.

Examples may include:

- spacing/orthography unrelated to speech level;
- particle/case errors unrelated to addressee treatment;
- tense/aspect or lexical-selection errors unrelated to speech level;
- subject/object honorification issues where the addressee ending is already resolved.

Fail the candidate if it expands into a general Korean proofreading or honorific module.

## 13. Composition with existing units

The reviewer must verify that the Korean candidate does not distort existing behavior:

```text
VN-LANG-REL-01
JP-LANG-HON-01
JP-LANG-PERM-01
ES-LANG-ADDR-01
```

Required architecture:

```text
CURRENT JOB
→ Chapter 07 localization owner
→ bounded discovery
→ adapt-localization.relationship-realization
→ section-local unit scope check
→ apply only the materially open language-specific constraint
```

Language name, country name, or route/file location must not activate every local unit.

## 14. Architecture attack

Do not sustain new machinery unless the reviewer can demonstrate all three:

```text
1. concrete discovery / addressability / composition failure
2. existing local contribution contract cannot repair it
3. material runtime consequence follows
```

Korean complexity alone is insufficient.

Explicitly adjudicate:

```text
existing route sufficient?      YES / NO
new owner required?             YES / NO
new route required?             YES / NO
shared primitive required?      YES / NO
hierarchy resolver required?    YES / NO
speech-level score required?    YES / NO
controller change required?     YES / NO
Chapter 07 change required?     YES / NO
routing-index change required?  YES / NO
get-knowledge change required?  YES / NO
```

## 15. Required final verdict

Choose exactly one:

```text
PASS
PASS_WITH_BOUNDED_REPAIR
FAIL
```

Then report:

### A. Promotion verdict

```text
KO-LANG-SPEECH-01
→ PROMOTE / NARROW / SPLIT / REJECT
```

Do not split merely because Korean has subject/object/addressee honorification. A split requires independently promotion-bearing mechanisms.

### B. Source adjudication

`KOLA01`–`KOLA11`, each `PASS / PARTIAL / FAIL`.

### C. Material findings

For every finding record:

```text
ID
SEVERITY
FROZEN LOCATION
UNSUPPORTED / INCORRECT CLAIM
WHY MATERIAL
SMALLEST REPAIR
```

### D. Architecture verdict

State whether existing owner/route remain sufficient and whether any new machinery is actually justified.

### E. K1–K16 results

Adjudicate every frozen adversarial case.

### F. Residual uncertainty

Record what remains unknown without converting unknowns into defaults or new research obligations.

## 16. Reviewer prohibition

The reviewer must not implement or repair the repository while performing the independent review.

If a bounded defect exists:

```text
REVIEW RESULT FIRST
→ COMMIT RESULT
→ AUTHOR REPAIR LATER AS A SEPARATE DELTA
```

Do not rewrite the frozen target and then claim the original target passed.

The review exists to falsify the candidate, not to make it pass.