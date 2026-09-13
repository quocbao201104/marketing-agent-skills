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

## S04 — Repetition triggers only when it changes the effective role

**Input:** A size-focused paid-social execution legitimately foregrounds a verified specification for one audience/touchpoint. A later PDP clarification also makes the specification prominent for error prevention. A proposed email subject would make the same specification the repeated organizing idea across the campaign, while the resolved campaign value remains elsewhere.

**Expected:** Do not reject either earlier local use merely because the detail leads. At the later decision point, check whether another prominent use would make the supporting detail function as a cross-surface campaign premise. If no evidence supports that promotion, preserve the earlier local executions and repair only the new decision or the smallest affected set of expressions.

**Failure:** Trigger after the first legitimate foregrounding; never trigger despite accumulated emphasis becoming the effective campaign premise; or treat prior repetition itself as evidence that promotion is justified.

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
