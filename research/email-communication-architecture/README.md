# Email Communication Architecture Research

Status: **THEORY VERIFIED — BOUNDED RUNTIME INTEGRATED**

This directory preserves the research freeze, adversarial review briefs, and targeted evaluation adjudications establishing **direct email communication architecture and send-state machines** in Handbook Chapter 12 (`12-email-communication-architecture.md`).

The research addresses the failure where marketing agents treat email merely as a high-volume broadcast blast or copy delivery mechanism. Chapter 12 governs the critical communication decisions: whether to send, wait, suppress, or branch; state-machine sequence logic; cross-surface promise continuity (inbox subject → email body → landing page); and email measurement observation semantics.

## Governing Question

> Once message, claims, and proof are sufficiently resolved, how should a practitioner decide whether and when to communicate via email, manage sequence wait/exit state, maintain cross-surface promise continuity, and interpret inbox signals without defaulting to broadcast volume or speculative personalization?

Key assumptions rejected during scoping:
- More email sends and higher volume always yield higher incremental conversion.
- Email open rates constitute reliable evidence of customer engagement and attention.
- Sequence automation should run on fixed chronological clocks regardless of user state.

## Disposition

```text
STATUS: THEORY VERIFIED & RUNTIME INTEGRATED
RUNTIME TARGET: Handbook Chapter 12 (12-email-communication-architecture.md)
ROUTING NAMESPACE: email.* (4 addressable routes)
EVIDENCE LEDGER: references/email-communication-evidence.md
```

- **Runtime Target**: Handbook Chapter 12 and the `email.*` routing namespace.
- **Mechanisms Added**: Send-state decision matrices (send, wait, suppress, branch), stateful sequence exit logic, cross-surface continuity invariants, and signal observation filters.
- **Expansions Rejected**: Spam generation templates, mechanical deliverability bypass tricks, and ungrounded hyper-personalization engines.

## File Lineage Table

| File | Purpose | Stage |
| :--- | :--- | :--- |
| [`01-theory-freeze.md`](01-theory-freeze.md) | Formal theory freeze establishing email send decisions, sequence state machines, and promise continuity | Theory Freeze |
| [`02-targeted-evaluation-adjudication.md`](02-targeted-evaluation-adjudication.md) | Targeted adjudication evaluating runtime behavior against adversarial test cases | Adjudication |
| [`03-independent-runtime-review-brief.md`](03-independent-runtime-review-brief.md) | Independent review brief examining edge cases in sender posture and suppression boundaries | Review Brief |

Related historical audits & regressions:
- [`../historical-audits/email-communication-architecture-adversarial-cases.md`](../historical-audits/email-communication-architecture-adversarial-cases.md)
- [`../historical-audits/email-communication-architecture-runtime-smoke.md`](../historical-audits/email-communication-architecture-runtime-smoke.md)

## Protected Invariants

```text
SEND DECISION != BROADCAST VOLUME
OPEN RATE != ATTENTION / INCREMENTALITY
SUBJECT PROMISE == BODY PROMISE == LANDING PAGE PROMISE
SUPPRESSION / WAITING CAN BE CORRECT WITHOUT INVENTED SEND ACTIVITY
EMAIL OBSERVATION SEMANTICS != DIRECT PURCHASE ATTRIBUTION
```

- If customer state indicates an open service issue or unread critical alert, suppress promotional sequences; waiting is an active, valid decision.
- The subject line promise, email body proposition, and destination landing-page payoff must maintain exact semantic alignment (`email.continuity`).
- Do not treat email proxy metrics (opens, clicks) as direct evidence of revenue incrementality.
