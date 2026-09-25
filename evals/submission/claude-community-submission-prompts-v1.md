# Claude Community Submission Prompts v1

Status: submission-ready examples; not behavioral evidence until executed.

Captured: 2026-09-19.

Purpose: provide three self-contained working prompt/use-case examples that
demonstrate core Marketing Agent Skills functionality for Anthropic directory
review.

**Test account / authentication:** None required. Marketing Agent Skills is a
skills-only plugin with no publisher-operated backend or login. All material
fixture data needed for these examples is included inline.

These examples are derived from the broader submission/evaluation set in
`evals/submission/openai-plugin-submission-cases-v1.md`. They are intentionally
limited to three representative jobs rather than duplicating the entire OpenAI
submission set.

---

## Example 1 — Customer evidence synthesis without prevalence inflation

**Core functionality:** customer research, evidence discipline, bounded
marketing implications.

```text
I'm doing customer-evidence research for a privacy-focused web analytics
product. Treat the notes below as five public user reports, not as a
representative market sample.

1. A hosted user says conversion events can happen hours or days after the first
   visit, and their supplied original referrer is not consistently reflected in
   attribution.
2. A self-hosting user says setup documentation led them to use a secret length
   that later caused migration/startup failure; they only found the actual
   requirement after substantial debugging.
3. A user says the custom date-range selector can render partly outside the
   viewport at some screen widths and in embedded dashboards.
4. A user says an embedded dashboard can fail for Firefox users running an
   ad-blocking extension.
5. A user says a tagged custom-event integration can interfere with form
   submission in a specific HTML naming edge case.

Synthesize what this evidence supports about user needs, adoption/evaluation
barriers, and trust risks. Separate observation from interpretation. Identify
useful messaging or proof questions this evidence justifies investigating.

Do not estimate prevalence, do not call these the "top five customer problems,"
and do not turn this into a product-roadmap prioritization.
```

Expected behavior:
- treat each report as bounded qualitative evidence;
- separate observation, interpretation, and research implication;
- avoid prevalence or market-wide claims;
- identify marketing/proof questions without taking product-roadmap authority.

---

## Example 2 — Diagnose performance before choosing an intervention

**Core functionality:** performance diagnosis, causal discipline, intervention
gating.

```text
Help me diagnose a marketplace performance snapshot.

Facts:
- Marketplace merchandise sales: about $2.6B, +7.5% year over year.
- Trailing-12-month active buyers: about 87M, roughly flat year over year.
- Sales per active buyer: $124, +2.8% year over year.
- Purchase frequency is still below the prior year, although the decline has
  moderated.
- Higher average order value was the largest contributor to sales growth.
- Mobile-app sales: +12.5% year over year and about 47% of total sales.
- Non-app sales: +3.4% year over year.
- Management says product and marketing work are contributing, while also
  acknowledging external factors.

The team is tempted to say "our marketing fixed buyer growth, so increase paid
search and reuse the same creative."

What does this evidence actually establish, what plausible explanations remain,
and what should be checked before changing paid-search allocation or creative?
```

Expected behavior:
- diagnose before prescribing;
- distinguish buyer count, frequency, order value, channel mix, and attribution;
- avoid treating management attribution as causal proof;
- identify unresolved decision surfaces and discriminating checks before
  recommending paid-media changes.

---

## Example 3 — Execute from approved positioning without reopening strategy

**Core functionality:** downstream marketing execution, resolved-state
preservation, claim control.

```text
The positioning is approved. Do not reopen it.

Product: a privacy-friendly web analytics product.
Audience: a small SaaS founder who finds Google Analytics too complex and is
uncomfortable with visitor surveillance.

Approved message:
"Get useful web analytics without Google Analytics complexity or tracking
individual visitors."

Allowed facts:
- easy-to-use, privacy-friendly Google Analytics alternative;
- no cookies and no tracking of individual users;
- made and hosted in the EU on European-owned infrastructure;
- open source;
- more than 21,000 paying subscribers;
- 30-day free trial, no credit card required;
- supports traffic/source reporting, campaign measurement, goals/events,
  funnels/user journeys, and SEO analysis.

Create a landing-page structure and draft the hero plus the key section copy.
Help the visitor understand the product, evaluate the privacy/utility trade-off,
and take the free-trial action.

Do not invent performance gains, legal guarantees, customer outcomes, or new
product capabilities.
```

Expected behavior:
- preserve the approved audience and positioning;
- use only supported facts and proof;
- allocate information according to reader decision needs;
- produce usable landing-page copy without reopening settled strategy.
