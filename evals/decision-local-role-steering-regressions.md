# Decision-local role steering — targeted regressions

Status: **REGRESSION CONTRACT — NOT A CLAIM OF UNIVERSAL RUNTIME PASS**

## Purpose

Test the recovery behavior added for cross-layer role drift without turning it into a mandatory workflow stage.

The mechanism should remain dormant during ordinary execution and activate only when a candidate decision would materially change what retained state functions as in the audience-facing artifact.

The target behavior is:

```text
NORMAL EXECUTION
→ candidate expression / representation
→ no material role delta: continue
→ possible material role delta: check support
   → justified: preserve or update role, then continue
   → unsupported: return to last supported role and repair the smallest affected choice
```

A visible or prominent supporting item is not automatically a role change. A role check is warranted only when the candidate would materially alter the item's effective strategic function, including by turning repeated local emphasis into a cross-surface organizing premise.

## S01 — Ordinary supporting detail stays on the fast path

**Input:** Positioning and message are resolved around reducing manual handoffs. A product page includes a verified implementation detail and a customer quote as supporting proof. Neither is proposed as the headline, dominant proposition, or organizing concept.

**Expected:** Use the supporting material normally. Do not introduce a separate role audit, reopen positioning, create an explicit role ledger, or add an approval step merely because proof and detail are present.

**Failure:** Convert ordinary drafting into a mandatory role-classification workflow when no material role delta is proposed.

## S02 — Local foregrounding is not strategic promotion

**Input:** A workflow SaaS is positioned around reducing manual handoffs. An enterprise security email exists specifically to provide SOC 2 material requested by procurement. SOC 2 remains proof / approval-path evidence in the broader product strategy.

**Expected:** The subject, opening, or first view may foreground SOC 2 because verification is the current touchpoint job. Preserve its broader proof role; do not reopen product positioning merely because the local communication leads with it.

**Failure:** Either suppress the useful SOC 2 lead because proof is "not primary value," or silently rewrite the product's strategic value around SOC 2.

## S03 — Unsupported promotion re-anchors locally

**Input:** Resolved primary value is a quiet, personal, everyday initial. Verified letter size is approximately 7.4mm and is retained as a specification / identity clarification / possible reason-to-believe for the quiet scale. A candidate campaign lead is `It's 7.4mm. That's the point.` No additional evidence establishes the measurement itself as the primary customer value or campaign premise.

**Expected:** Detect the material role delta before committing the lead. Return to the last supported primary value/message, retain 7.4mm as supporting specification/proof, and repair only the affected lead or downstream expression. Do not restart research, reopen unrelated positioning, or ask the user to reconfirm settled strategy.

**Failure:** Commit the measurement as the dominant proposition because it is concrete, memorable, or easy to verify; or recover by restarting the whole workflow instead of making a bounded repair.

**Wording variant:** Replace the numeric campaign lead with `Small on purpose.` Keep the same resolved value and evidence. Inspect the whole candidate artifact: removing the number does not repair the failure if smallness still displaces the personal, everyday value as the campaign premise. Conversely, the phrase may serve a bounded scale-focused execution or express the resolved quiet character without changing the strategic role. Judge the effective role in context, not the presence of the number or phrase; neither wording is automatically a pass or failure.

## S04 — Repetition triggers only when it changes the effective role

**Input:** Campaign value remains resolved around a quiet, personal, everyday initial. One paid-social execution legitimately uses the verified 7.4mm specification as its lead to make scale concrete. The PDP separately gives 7.4mm strong first-view prominence in a structured size fact because omission could cause a size mismatch; its value headline remains unchanged. The next task is a general follow-up email whose job is to re-present the product, not to answer a size-specific question. A candidate subject is `7.4mm. That's the point.` No new customer, demand, or positioning evidence has been introduced since the earlier local executions.

**Expected:** Infer from the retained campaign value, the two already-accepted local uses, the email's different job, and the proposed subject whether this additional foregrounding would materially change 7.4mm from a supporting specification into a cross-surface organizing premise. In this fixture it should trigger the role check: the email has no independent size-resolution job and no new evidence supports campaign-level promotion. Preserve the earlier legitimate ad and PDP uses, reject the unsupported promotion in the new subject, and repair only the new decision or the smallest affected set of expressions.

**Failure:** Trigger after the first legitimate foregrounding; treat each surface as independent forever and miss the accumulated role change; infer promotion merely from a repetition count; or treat prior repetition itself as evidence that promotion is justified.

**Continuation variant:** After the accepted ad and PDP work, request a concise working summary for later continuation. Resume from that summary instead of the full earlier transcript, then give the general follow-up email task and candidate subject above. Preserve both the produced summary and the subsequent email for review.

**Expected:** The summary retains the adopted campaign value, the specification's supporting role, and why each earlier touchpoint foregrounded it. It does not recast those local executions as an adopted size-led campaign direction. The resumed email preserves that distinction and repairs the unsupported subject locally. No fixed summary template or separate role ledger is required.

**Failure:** The summary drops the decision-changing scope or records a size-led campaign direction as adopted; or the resumed email treats prior local emphasis as authority for strategic promotion. A suitable final email does not excuse a misleading summary, and a faithful summary does not excuse unsupported promotion on resumption.

## S05 — Genuine promotion is allowed and retained

**Input:** A compatibility limitation begins as a supporting product constraint. New customer and decision evidence establishes exact compatibility as the decisive purchase criterion for the current segment, and the task explicitly requires a compatibility-led message.

**Expected:** Recognize that the higher role is now supported, update the retained role/state, and allow compatibility to organize the message. Do not keep forcing the old hierarchy merely because the item originated as a specification or constraint.

**Failure:** Treat role preservation as role immutability and block an evidence-supported promotion.

## Adjudication

A passing implementation should demonstrate all three properties:

1. **Low interference:** no extra audit on the normal fast path when no material role delta is proposed.
2. **Timely steering:** intervene at the role-changing decision point, before unsupported promotion becomes a committed downstream premise.
3. **Bounded recovery:** when promotion is unsupported, restore the last supported role and repair the smallest affected downstream scope rather than restarting unrelated upstream work.

Do not count a final artifact as evidence that the steering path was used unless the evaluation can distinguish the relevant candidate state, trigger condition, and resulting bounded disposition.
