# Spanish Local Adaptation — Independent Adversarial Review Brief

Status: **FROZEN REVIEW CONTRACT**  
Review target: `c5ac8e7cd5408600789e2da01472449ff9dd62f6`  
Target artifacts:

```text
research/local-adaptation-spanish/01-design-freeze.md
research/local-adaptation-spanish/02-evidence-ledger.md
```

This review brief is committed after the frozen target. It defines how the target is judged; it is not retroactive evidence that the candidate already satisfies the contract.

## 1. Reviewer role

Act as an **INDEPENDENT ADVERSARIAL LOCAL-ADAPTATION REVIEWER** for the Spanish candidate in Marketing Practitioner.

Do not defend the candidate.

Do not modify the repository.

Do not implement the unit.

Do not broaden the task into a general Spanish grammar, Hispanic-culture, Spain-versus-Latin-America, or localization survey.

Do not recommend a new primitive, country pack, route family, variety resolver, or precedence engine merely because Spanish treatment systems vary.

Your job is to determine whether the frozen evidence justifies `ES-LANG-ADDR-01` and whether it fits the already-released thin local-adaptation architecture without material distortion.

## 2. Primary questions

Answer all of the following:

1. Does `ES-LANG-ADDR-01` represent a real Spanish-specific realization mechanism that generic Chapter 07 does not already fully encode?
2. Does the candidate materially improve decisions rather than merely restating that Spanish has `tú / vos / usted / vosotros / ustedes`?
3. Are pronominal treatment, verbal treatment, and selective grammatical repair separated correctly without becoming a grammar handbook?
4. Can the unit safely live under the existing route `adapt-localization.relationship-realization`?
5. Can the existing contribution contract express variety scope, first-party overrides, mixed systems, and evidence conflict without a new resolver or country-first route?
6. Does Spanish pressure reveal a shared-state or discovery defect that cannot be repaired locally?
7. Are any claims in the evidence ledger broader than the cited sources actually support?
8. Should the proposed unit be promoted, narrowed, split, or rejected?

## 3. Files to read

Start with the frozen target only:

```text
research/local-adaptation-spanish/01-design-freeze.md
research/local-adaptation-spanish/02-evidence-ledger.md
```

Then read only current runtime surfaces materially required to test composition:

```text
skills/marketing-practitioner/SKILL.md
skills/marketing-practitioner/handbook/07-international-marketing-and-ethics.md
skills/marketing-practitioner/adaptations/README.md
skills/marketing-practitioner/adaptations/localization.md
skills/marketing-practitioner/routing-index.json
skills/marketing-practitioner/scripts/get-knowledge.py
```

Read other handbook chapters only when a concrete adversarial case requires their owner/state semantics.

Do not use later commits after the frozen target as evidence that a defect was already solved.

## 4. Promotion standard

The Spanish unit is valid only if the reviewer can sustain:

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

Reject the unit if Chapter 07 plus supplied task evidence can already make the correct decision reliably without Spanish-specific knowledge.

Do not count `models sometimes make Spanish mistakes` as sufficient promotion evidence by itself.

## 5. Evidence adjudication

Adjudicate every source record `ESLA01`–`ESLA11` as:

```text
PASS
PARTIAL
FAIL
```

For each `PARTIAL` or `FAIL`, state exactly which claim is unsupported, stale, scope-mismatched, or over-broad.

Special scrutiny:

- `ESLA01`–`ESLA05` should carry the primary linguistic-mechanism burden.
- `ESLA06` is marketing-context evidence; it must not become a country-wide prescription or conversion claim.
- `ESLA07`–`ESLA08` are first-party organization/style policies; they support organization-state precedence only within their actual scope.
- `ESLA09`–`ESLA10` support bounded address-neutral realization, not a universal `neutral Spanish` strategy.
- `ESLA11` supports the grammatical basis of referent collision; it does not by itself justify a new ambiguity resolver.

## 6. Required attacks on ES-LANG-ADDR-01

Evaluate S1–S16.

### S1 — generic tuteo, no local pressure

```text
TARGET: Spanish
APPROVED COPY: stable tú-system
NO MATERIAL VARIETY CONFLICT
```

Required behavior: do not reopen a resolved treatment system merely because the unit exists.

### S2 — Rioplatense voseo repair

```text
TARGET: Rioplatense Spanish
APPROVED ADDRESS: vos
DRAFT:
"Descubre cómo mejorar tu negocio. Haz clic. Vos podés empezar hoy."
```

Attack whether the candidate can repair treatment-sensitive imperative forms without rewriting unaffected `tu / te` forms as if `vos` created a wholly separate paradigm.

### S3 — Chilean mixed verbal voseo

```text
TARGET: Chilean Spanish
SUPPLIED / APPROVED:
"Si tú querís..."
```

Required behavior: do not normalize `querís → quieres` merely because `tú` is present. Demand stronger scoped evidence before treating the mixed system as error.

### S4 — mixed form is actually accidental

Construct a text where `tú`, `usted`, and conflicting verb forms are produced by model drift and no source/variety/stance evidence supports the shift.

Required behavior: the candidate must be capable of repair; `mixed form != automatic error` must not become `mixed form = always preserve`.

### S5 — Canary familiar plural

```text
TARGET: Canary Spanish
AUDIENCE: familiar plural
CURRENT FORM: ustedes
```

Fail the candidate if it converts to `vosotros` merely because country = Spain.

### S6 — central/northern Spain familiar plural with approved `vosotros`

Required behavior: do not use the Canarian counterexample to erase a separately supported `vosotros` system.

### S7 — Latin America as an underspecified label

```text
TARGET MARKET: "Latin America"
NO MORE SPECIFIC VARIETY EVIDENCE
ADDRESS CHOICE IS MATERIAL
```

Required behavior: do not invent one pan-Latin-American `tú / vos / usted` policy.

### S8 — El Salvador everyday speech vs advertising

Use the empirical advertising evidence.

Required behavior: reject both overreaches:

```text
local everyday voseo → ads must use vos
study favors tú → all Salvadoran ads should use tú
```

### S9 — organization/channel policy

Use Head Start or Mozilla-style first-party state where the current surface explicitly resolves `tú` or `usted`.

Required behavior: preserve the applicable first-party policy rather than reopening it from broader sociolinguistic evidence.

### S10 — first-party state conflicts with language-system possibility

Construct an organization rule that requests a form incompatible with the applicable known grammatical system.

Required behavior: distinguish `organization may choose treatment` from `organization policy makes ungrammatical morphology valid`. Preserve authority boundaries and surface the conflict rather than silently inventing a repair policy.

### S11 — address-neutral UI

```text
SURFACE: button label
LABEL: "Crear"
```

Required behavior: no Spanish adaptation detour when no material second-person choice exists.

### S12 — direct CTA where treatment is unavoidable

Construct conversational copy where replacing the direct address with infinitives or impersonal phrasing would materially damage the communication job.

Required behavior: do not hide an unresolved treatment dependency behind awkward `neutral` wording.

### S13 — `ustedes` / third-person referent collision

Context contains both:

```text
customer team = YOU ALL
implementation partner = THEY
```

Draft uses forms such as `pueden / sus`.

Required behavior: preserve referent fidelity if ambiguity is material, but do not import `vosotros / vuestro` solely to disambiguate.

### S14 — intentional stance shift

Construct dialogue or campaign copy where a `tú → usted` shift is explicitly supported by interactional state or source evidence.

Required behavior: do not normalize for superficial consistency.

### S15 — Spanish outside a Spanish-speaking country

Test Spanish-language communication in a non-Spanish-speaking market.

Required behavior:

```text
language relevance
!= country-pack activation
```

### S16 — country name with no second-person decision

```text
TASK: localize facts for Argentina
COPY: no second-person treatment choice
```

Required behavior: `Argentina` and `Spanish` alone do not activate the unit.

## 7. Boundary attack: treatment system vs ordinary grammar

The reviewer must identify at least three Spanish errors that are ordinary grammar or style issues but **not** `ES-LANG-ADDR-01` problems.

Fail the candidate if it absorbs general conjugation, spelling, punctuation, gender agreement, lexical choice, or all Spanish locale variation merely because those errors occur near second-person wording.

Required boundary:

```text
TREATMENT-SENSITIVE REALIZATION
→ candidate scope

GENERAL SPANISH CORRECTNESS
→ existing language competence / other owner
```

## 8. Variety-scope attack

Pressure whether the candidate silently turns:

```text
country
→ dialect
→ treatment system
```

Test at least:

```text
Spain / Canarias
Chile
Argentina / Río de la Plata
Colombia with city-level variation
Central America / El Salvador
```

The reviewer should prefer rejection or explicit uncertainty over unsupported specificity.

No registry or specificity scorer should be recommended unless a concrete failure shows the current section-local scope contract cannot represent the conflict.

## 9. First-party-state attack

The candidate claims current first-party organization/channel state can resolve treatment within scope.

Pressure both failure directions:

```text
A. adaptation overrides approved state too eagerly

B. first-party policy is treated as population-wide truth
```

Required distinction:

```text
FIRST-PARTY POLICY
= authoritative for controlled artifact dimensions

FIRST-PARTY POLICY
!= sociolinguistic prevalence claim
```

## 10. Address-neutrality attack

The candidate allows avoidance of a treatment choice when a surface naturally permits it.

Pressure both failures:

```text
A. underuse:
   agent asks for unnecessary relationship facts for a neutral button / notice

B. overuse:
   agent rewrites direct marketing/support copy into unnatural impersonal language
   merely to avoid resolving treatment
```

The candidate succeeds only if avoidance is surface-local and meaning-preserving.

## 11. Counterfactual necessity test

For each surviving rule, ask:

> If `ES-LANG-ADDR-01` were removed, but Chapter 07, task evidence, organization policy, and ordinary Spanish generation remained, would the correct realization still be reliably available?

At minimum test:

```text
- vos + te / tu / tuyo preservation;
- verbal-only voseo;
- Chilean tú + voseante morphology;
- Canary familiar-plural ustedes;
- current first-party treatment policy;
- address-neutral UI.
```

Reject candidate material that does not change the answer under this counterfactual.

## 12. Architecture attack

The frozen candidate proposes no change to:

```text
SKILL.md
routing-index.json
controller
Chapter 07
shared state primitives
```

Attempt to prove that one of those changes is necessary.

Only sustain an architecture finding if you can show:

```text
CONCRETE DISCOVERY / ADDRESSABILITY / COMPOSITION FAILURE
+
LOCAL CONTRIBUTION CANNOT REPAIR IT
+
MATERIAL RUNTIME CONSEQUENCE
```

Complexity of Spanish variation alone is not sufficient.

## 13. Required final verdict

Return exactly one top-level verdict:

```text
PASS
PASS_WITH_BOUNDED_REPAIR
FAIL
```

Then report:

```text
A. PROMOTION VERDICT
   - ES-LANG-ADDR-01: PROMOTE / NARROW / SPLIT / REJECT

B. SOURCE ADJUDICATION
   - ESLA01–ESLA11: PASS / PARTIAL / FAIL

C. MATERIAL FINDINGS
   - severity
   - exact frozen-file location
   - unsupported or unsafe claim
   - smallest repair

D. ARCHITECTURE VERDICT
   - existing route sufficient? yes/no
   - new owner required? yes/no
   - new route required? yes/no
   - shared primitive required? yes/no

E. FROZEN ADVERSARIAL CASE RESULTS
   - S1–S16

F. RESIDUAL UNCERTAINTY
   - what remains unknown without blocking the verdict
```

Do not implement the repair. The review result must remain independent from the subsequent author repair step.