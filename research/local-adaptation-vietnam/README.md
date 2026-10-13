# Local Adaptation Vietnam Research

Status: **THEORY VERIFIED — BOUNDED RUNTIME INTEGRATED**

This directory preserves the post-repair review results and implementation audits establishing the **Vietnamese linguistic relationship-realization adaptation**.

The research addresses the failure where marketing agents translate English or global marketing copy into Vietnamese using either unnatural, robotic pronouns (*bạn* / *chúng tôi*) or inappropriately presumptuous familial kinship pronouns (*anh* / *chị* / *em* / *mình*) that violate social distance and commercial credibility. The Vietnamese adaptation formalizes kinship-based and professional address selection as a bounded relationship realization decision.

## Governing Question

> When marketing communication is targeted for the Vietnamese market, how should practitioner reasoning specialize kinship pronoun selection (*anh*, *chị*, *em*, *bạn*, *mình*, *quý khách*), self/address asymmetry, and commercial posture without defaulting to mechanical literalism or inappropriate familiarity?

Key assumptions rejected during scoping:
- Vietnamese digital marketing should universally use *bạn* as a direct equivalent for English "you".
- Localizing for Vietnam requires altering the underlying product positioning or economic terms.

## Disposition

```text
STATUS: THEORY VERIFIED & BOUNDED RUNTIME INTEGRATED
RUNTIME TARGET: skills/marketing-agent-skills/adaptations/vietnam/
GOVERNING CHAPTER: Chapter 07 (07-international-marketing-and-ethics.md)
EVIDENCE SOURCE: references/local-adaptation-evidence.md
```

- **Runtime Target**: `skills/marketing-agent-skills/adaptations/vietnam/` and Chapter 07 routes.
- **Mechanisms Added**: Kinship pronoun relationship-realization matrix, speaker-recipient asymmetry rules, and professional vs. commercial distance calibration.
- **Expansions Rejected**: Autonomous Vietnamese cultural manuals, lifestyle trend taxonomies, and ungrounded consumer behavior stereotypes.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-post-repair-review-result.md`](01-post-repair-review-result.md) | Post-repair independent review certifying Vietnamese relationship-realization logic and runtime integration | Review Result |

Related historical audits & regressions:
- [`../historical-audits/local-adaptation-vn-language-v0.md`](../historical-audits/local-adaptation-vn-language-v0.md)

## Protected Invariants

```text
VIETNAM CONTEXT ALONE != PERMISSION TO REOPEN GLOBAL STRATEGY
KINSHIP PRONOUNS = SOCIAL DISTANCE & COMMERCIAL REALIZATION (NOT CASUAL SLANG)
BẠN != UNIVERSAL DIRECT TRANSLATION OF "YOU"
QUÝ KHÁCH VS ANH/CHỊ/EM → DETERMINED BY BRAND-CUSTOMER DISTANCE
SHARED THEORY REMAINS SHARED
```

- Target language realization activates only when Vietnamese text expression is open; it does not authorize reopening settled value propositions or pricing architecture.
- Address form selection must reflect actual brand posture: high-touch/hospitality (*quý khách*), peer-level consumer (*bạn*), or community-intimate (*anh/chị/em*).
