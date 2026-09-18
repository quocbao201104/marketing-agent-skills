# OpenAI Plugin Submission Cases v1

Status: research-grounded candidate set; not yet live-run.

Captured: 2026-09-19.

Purpose: provide five positive and three negative submission cases for the public
Marketing Practitioner plugin without inventing arbitrary business metrics. The
prompts freeze public facts into self-contained fixtures so a reviewer can run
them without browsing. Provenance remains outside the prompt so current web
changes do not silently change the test.

## Test protocol

Default submission-routing run:

1. start a clean conversation with Marketing Practitioner installed and available;
2. do not explicitly invoke `/marketing-practitioner` or otherwise force-select the skill;
3. send only the case prompt;
4. record whether Marketing Practitioner was selected;
5. judge the task behavior separately from activation.

These activation labels are **internal auto-routing expectations**, not OpenAI's
public definition of positive and negative submission cases.

- Positive submission cases still need the expected skill/workflow behavior,
  expected result shape, and any fixture or test-account requirements.
- Negative submission cases need the expected refusal, clarification, or safe
  fallback plus the reason Marketing Practitioner should not complete the
  requested action.

For the internal routing regression, positive cases expect selection and negative
cases expect non-selection in the clean auto-routing run above.

If a reviewer instead runs a case with the plugin already explicitly selected,
activation is no longer a valid pass/fail signal. In that regime, judge ownership
behavior instead: an in-scope task should be handled by the skill, while an
out-of-scope task should be bounded or handed off without applying Marketing
Practitioner as the task-solving framework.

## Case design rules

- Use public, inspectable facts or public user reports.
- Paraphrase source material; do not copy long passages.
- Freeze material facts in the prompt and record the capture date.
- Do not treat vendor marketing claims as independently verified outcomes.
- Keep each case self-contained.
- Map each positive case to the smallest runtime owner(s) that should matter.
- Submission cases are not behavioral evidence until they are executed against
  the final package.
- Do not modify the frozen behavioral pilot merely to satisfy store submission.
  Promote a case into the behavioral harness later only if it earns a stable
  evaluation role.

---

## Positive 1 — Public customer evidence without prevalence inflation

**ID:** SUB-POS-001  
**Job:** RESEARCH / UNDERSTAND  
**Primary owner:** Chapter 01 — customer research and evidence  
**Secondary dependency:** Chapter 04 only if communication implications are used  
**Internal auto-routing expectation:** YES  
**Activation shape:** explicit evidence synthesis with product-adoption symptoms
**Fixture / test account:** No account or authentication required. All material fixture data is included inline in the submission prompt.  

### Public provenance

Public Plausible Analytics GitHub issue reports:

- https://github.com/plausible/analytics/issues/5564
- https://github.com/plausible/analytics/issues/5612
- https://github.com/plausible/analytics/issues/4967
- https://github.com/plausible/analytics/issues/2550
- https://github.com/plausible/analytics/issues/2851

Captured observations used in the fixture:

- one Plausible Cloud user reported difficulty preserving an original referrer
  for conversion events that can occur hours or days after the first visit;
- one self-hosting user reported misleading setup documentation around the
  required SECRET_KEY_BASE length and substantial debugging before finding the
  cause;
- one user reported a custom date-range selector becoming unusable at some
  intermediate viewport sizes and in embedded dashboards;
- one user reported an iframe integration failing for Firefox users with
  uBlock;
- one user reported that tagged custom-event handling could interfere with form
  submission in a specific HTML naming edge case.

These are individual issue reports, not a representative customer sample.

### Submission prompt

```text
I'm doing customer-evidence research for Plausible Analytics. Treat the notes
below as five public user reports, not as a representative market sample.

1. A Plausible Cloud user says conversion events can happen hours or days after
   the first visit, and their supplied original referrer is not consistently
   reflected in attribution.
2. A self-hosting user says setup documentation led them to use a
   SECRET_KEY_BASE length that later caused migration/startup failure; they only
   found the actual requirement after substantial debugging.
3. A user says the custom date-range selector can render partly outside the
   viewport at some screen widths and in embedded dashboards.
4. A user says an embedded dashboard can fail for Firefox users running uBlock.
5. A user says a tagged custom-event integration can interfere with form
   submission when a form control uses a particular submit name/id pattern.

Synthesize what this evidence supports about user needs, adoption/evaluation
barriers, and trust risks. Separate observation from interpretation. Identify
useful messaging or proof questions this evidence justifies investigating.

Do not estimate prevalence, do not call these the "top five customer problems,"
and do not turn this into a product-roadmap prioritization.
```

### Expected behavior

- Under the default auto-routing run, selects Marketing Practitioner.
- Preserves each report as a bounded observation.
- Groups plausible mechanisms without implying independent prevalence.
- Distinguishes hosted, self-hosted, embedded, attribution, and implementation
  contexts where they matter.
- Produces messaging/proof research questions rather than silently converting
  issue reports into a market-wide positioning claim.
- Does not recommend roadmap priority as if marketing evidence grants product
  authority.

### Expected result shape

1. Evidence-backed themes.
2. Observation vs interpretation table.
3. Messaging/proof questions worth testing.
4. Explicit evidence limits and missing evidence.

### Why this belongs in the repo

This is a realistic replacement for synthetic interview counts. It directly
tests the repo's qualitative-recurrence vs population-prevalence boundary and
the product-roadmap handoff.

---

## Positive 2 — Real pricing architecture, no invented willingness-to-pay

**ID:** SUB-POS-002  
**Job:** DECIDE  
**Primary routes:** `commercial-design.configuration`,
`commercial-design.payment`, `commercial-design.modifiers-representation`,
`commercial-design.decision`  
**Internal auto-routing expectation:** YES  
**Activation shape:** published offer structure with an unresolved commercial
communication/design question
**Fixture / test account:** No account or authentication required. All material fixture data is included inline in the submission prompt.  

### Public provenance

Buffer pricing and small-business pages:

- https://buffer.com/pricing
- https://buffer.com/made-for/small-business

Captured facts used in the fixture:

- Free supports up to three channels, 10 scheduled posts per channel, and one
  user account.
- Essentials is listed at $5/month for one channel when billed yearly, with
  unlimited scheduled posts and one user account.
- Team is listed at $10/month for one channel when billed yearly, with unlimited
  team members plus access levels and content approval workflows.
- Buffer says annual billing saves two months.
- Buffer says channels above 10 receive volume discounts, reducing average cost
  per channel as the number of channels grows.
- Buffer positions its small-business offer around planning, publishing,
  analytics, and community management without social media taking over the
  operator's day.

### Submission prompt

```text
Audit this published Buffer pricing structure as a commercial-design and
pricing-page communication problem.

Facts:
- Free: up to 3 channels, 10 scheduled posts per channel, 1 user.
- Essentials: $5/month for 1 channel when billed yearly; unlimited scheduled
  posts; 1 user; advanced analytics.
- Team: $10/month for 1 channel when billed yearly; unlimited team members;
  advanced analytics; access levels; content approval workflows.
- Annual billing saves two months.
- Above 10 channels, Buffer applies volume discounts so average cost per
  channel falls as channel count grows.
- Buffer's small-business positioning emphasizes simple planning, publishing,
  analytics, and community management without social media taking over the day.

Explain the package/payment logic a buyer is being asked to understand,
identify the most material clarity or transition questions, and recommend a
small set of hypotheses to test.

Do not invent willingness-to-pay, profitability, unit economics, or customer
preference data. Do not choose a new price just because the current numbers are
available.
```

### Expected behavior

- Under the default auto-routing run, selects Marketing Practitioner and enters commercial design rather than generic copywriting.
- Separates package entitlement, pricing metric, annual discount, and volume
  modifier.
- Does not infer that per-channel pricing is good/bad from first principles.
- Identifies unresolved evidence needed before a price/package redesign.
- Can recommend representation or testing changes that are supported without
  pretending to certify finance.

### Expected result shape

1. Current commercial logic.
2. Material buyer-clarity / transition questions.
3. Evidence gaps.
4. Testable hypotheses or bounded representation changes.

---

## Positive 3 — Real marketplace performance diagnosis before intervention

**ID:** SUB-POS-003  
**Job:** DIAGNOSE  
**Primary owner:** Chapter 05 — diagnosis / causality / experimentation  
**Conditional routes:** `etsy.diagnosis`, `paid-media.observation`  
**Internal auto-routing expectation:** YES  
**Activation shape:** apparently good aggregate growth with mixed underlying
drivers and an intervention temptation
**Fixture / test account:** No account or authentication required. All material fixture data is included inline in the submission prompt.  

### Public provenance

Etsy Q2 2026 shareholder letter and 10-Q:

- https://investors.etsy.com/sec-filings/all-sec-filings/content/0001370637-26-000079/q226shareholderletter.htm
- https://investors.etsy.com/sec-filings/all-sec-filings/content/0001370637-26-000080/etsy-20260630.htm

Captured Etsy marketplace facts used in the fixture:

- Q2 2026 Etsy marketplace GMS was about $2.6B, up 7.5% year over year.
- trailing-twelve-month active buyers were about 87M and roughly flat year over
  year;
- GMS per active buyer was $124, up 2.8% year over year;
- purchase frequency remained below the prior year, though its decline
  moderated;
- higher average order value was the largest contributor to GMS growth;
- mobile-app GMS grew 12.5% year over year and represented about 47% of total
  GMS;
- non-app GMS grew 3.4% year over year;
- Etsy attributed improvement in part to product and marketing work, while also
  noting external factors.

### Submission prompt

```text
Help me diagnose Etsy marketplace performance from this Q2 2026 public snapshot.

Facts:
- Marketplace GMS: about $2.6B, +7.5% year over year.
- Trailing-12-month active buyers: about 87M, roughly flat year over year.
- GMS per active buyer: $124, +2.8% year over year.
- Purchase frequency is still below the prior year, although the decline has
  moderated.
- Higher average order value was the largest contributor to GMS growth.
- Mobile-app GMS: +12.5% year over year and about 47% of total GMS.
- Non-app GMS: +3.4% year over year.
- Management says product and marketing work are contributing, while also
  acknowledging external factors.

The team is tempted to say "our marketing fixed buyer growth, so increase paid
search and reuse the same creative."

What does this evidence actually establish, what plausible explanations remain,
and what should be checked before changing paid-search allocation or creative?
```

### Expected behavior

- Under the default auto-routing run, selects Marketing Practitioner.
- Diagnoses before prescribing.
- Separates GMS growth, buyer count, frequency, AOV, app mix, and management
  attribution.
- Does not treat management attribution as causal proof.
- Recognizes that stronger app growth does not by itself establish why it grew.
- Reaches paid-media semantics only after identifying the unresolved causal and
  allocation questions.
- Recommends discriminating checks rather than a reflexive creative rewrite or
  budget increase.

### Expected result shape

1. What is established.
2. What remains explanatory / causal uncertainty.
3. Decision surfaces that could change the intervention.
4. Next checks, ordered by decision value.

---

## Positive 4 — Real enterprise buyer requirements vs public vendor evidence

**ID:** SUB-POS-004  
**Job:** DECIDE / founder-led sales  
**Primary routes:** `founder-sales.pursuit`, `founder-sales.selection`,
`founder-sales.proof`, `founder-sales.decision`  
**Conditional dependency:** `commercial-design` only for the buyer's requested
pricing structure  
**Internal auto-routing expectation:** YES  
**Activation shape:** buyer opportunity with a mix of confirmed fit, unknowns,
and likely gaps
**Fixture / test account:** No account or authentication required. All material fixture data is included inline in the submission prompt.  

### Public provenance

University at Buffalo RFI #25AXB0165 and Buffer public product/pricing pages:

- Secondary public RFI mirror:
  https://govtribe.com/file/government-file/1392364-event-dot-pdf
  - No official public primary URL is currently located.
  - Fixture facts are frozen inline, so test execution does not depend on mirror availability.
- Buffer pricing:
  https://buffer.com/pricing
- Buffer small-business product page:
  https://buffer.com/made-for/small-business

Captured buyer requirements from the public RFI include content planning and
publishing, community management, analytics/reporting, social listening, paid
advertising management, automation, access controls, security/compliance,
implementation/training/support, and representative pricing information.

Captured Buffer evidence includes planning/publishing, AI assistance, analytics,
a community inbox, API access, support, and Team-plan access levels/content
approval workflows. The captured Buffer pages do not establish support for
every RFI requirement, including social listening and paid-advertising
management.

### Submission prompt

```text
Qualify this enterprise social-media opportunity using only the buyer
requirements and vendor evidence below.

Buyer: University at Buffalo public RFI #25AXB0165.
The buyer asked vendors about:
- content planning/scheduling/publishing;
- engagement and community management;
- analytics and reporting;
- social listening/monitoring;
- paid-advertising management;
- automation;
- user access controls and collaboration;
- security/compliance;
- implementation, training, and support;
- pricing/licensing structure.

Vendor evidence available from Buffer's current public pages:
- planning and publishing across social channels;
- AI Assistant;
- analytics;
- community inbox;
- API access;
- customer support;
- Team plan includes unlimited team members, access levels, and content
  approval workflows;
- public pricing is primarily channel-based.

The supplied evidence does NOT establish whether Buffer satisfies every buyer
requirement, including social listening, paid-ad management, and all enterprise
security/compliance requirements.

Should this opportunity be advanced, bounded, or deprioritized based on the
evidence we have? Build a fit / unknown / gap map, identify the smallest proof
and discovery questions needed next, and propose the next justified sales step.

Do not invent product capabilities or treat unknowns as either a fit or a
disqualifier.
```

### Expected behavior

- Under the default auto-routing run, selects Marketing Practitioner and enters founder-sales rather than producing generic RFP copy.
- Distinguishes confirmed fit, material unknowns, and evidenced gaps.
- Avoids hallucinating Buffer features.
- Treats an RFI as an information-gathering buying state, not a won/lost deal.
- Makes pursuit/resource guidance conditional on what the unresolved buyer
  requirements could change.
- Hands pricing structure to commercial design only if needed rather than
  letting pricing dominate opportunity qualification.

### Expected result shape

1. Fit / unknown / gap matrix.
2. Material buyer-decision risks.
3. Discovery/proof questions.
4. Recommended pursuit state and next justified step.

---

## Positive 5 — Real product facts, resolved positioning, bounded landing page

**ID:** SUB-POS-005  
**Job:** WRITE  
**Primary routes:** Chapter 04, `landing-page.core`,
`landing-page.sequence`, `landing-page.proof-risk`,
`landing-page.action-form`  
**Internal auto-routing expectation:** YES  
**Activation shape:** approved strategy and product facts; execution should not
reopen positioning
**Fixture / test account:** No account or authentication required. All material fixture data is included inline in the submission prompt.  

### Public provenance

Plausible Analytics official homepage and about page:

- https://plausible.io/
- https://plausible.io/about

Captured facts used in the fixture:

- Plausible describes itself as an easy-to-use, privacy-friendly Google
  Analytics alternative.
- It says it uses no cookies and does not track individual users.
- It is made and hosted in the EU on European-owned infrastructure.
- It is open source.
- It reports more than 21,000 paying subscribers.
- It offers a 30-day free trial with no credit card required.
- Product capabilities on the public page include traffic/source reporting,
  campaign measurement, goals/events, funnels/user journeys, and SEO-related
  analysis.

### Submission prompt

```text
The positioning is approved. Do not reopen it.

Product: Plausible Analytics.
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

### Expected behavior

- Under the default auto-routing run, selects Marketing Practitioner.
- Preserves the approved positioning and audience.
- Uses supplied proof/facts without upgrading them into guarantees.
- Allocates information according to reader decision needs.
- Does not reopen pricing, segmentation, or positioning without a material
  contradiction.
- Produces usable page copy rather than an internal strategy lecture.

### Expected result shape

1. Page sequence / section purposes.
2. Hero copy.
3. Key section copy and proof placement.
4. CTA / risk-reduction copy.

---

# Negative cases

## Negative 1 — Real product issue, but the requested work is technical

**ID:** SUB-NEG-001  
**Boundary:** unrelated technical work / product-roadmap implementation  
**Internal auto-routing expectation:** NO  
**Source:** https://github.com/plausible/analytics/issues/5612

### Submission prompt

```text
Plausible's self-hosted setup can fail when SECRET_KEY_BASE is shorter than the
runtime actually requires. I want you to patch the Elixir/Phoenix configuration
code, add validation, and write the regression test for this bug.
```

### Internal auto-routing expectation

Marketing Practitioner should not be selected in the clean auto-routing run.

### Expected submission behavior

Use a safe fallback or handoff to the appropriate coding capability. If the
plugin was already explicitly selected before the prompt, do not use Marketing
Practitioner as the task-solving framework; bound or hand off the technical
implementation instead.

### Why Marketing Practitioner should not complete this task

The requested action is software implementation/debugging, which is outside the
skill's ownership. Marketing Practitioner may only become relevant later if the
user separately asks how to communicate the change or learn from customer
evidence.

---

## Negative 2 — Real procurement context, but the requested judgment is legal

**ID:** SUB-NEG-002  
**Boundary:** legal/compliance authority  
**Internal auto-routing expectation:** NO  
**Source:** University at Buffalo RFI #25AXB0165 public procurement materials

### Submission prompt

```text
The University at Buffalo RFI says vendors can mark information confidential or
proprietary, but the submission is still subject to New York State public-records
rules. Give me a definitive legal determination of whether our pricing can be
withheld from disclosure, cite the controlling New York law, and draft the legal
language we should rely on.
```

### Internal auto-routing expectation

Marketing Practitioner should not be selected as the task owner in the clean
auto-routing run.

### Expected submission behavior

Refuse to provide a definitive legal determination as Marketing Practitioner, or
hand off to an appropriate legal capability if one is available. If the plugin
was already explicitly selected, identify the legal dependency and preserve any
separate commercial/sales work that does not require the legal answer.

### Why Marketing Practitioner should not complete this task

The requested judgment depends on legal authority and interpretation. Marketing
guidance must not substitute for legal analysis merely because the scenario
arises inside procurement or sales work.

---

## Negative 3 — Real pricing context, but the requested work is accounting

**ID:** SUB-NEG-003  
**Boundary:** finance/accounting  
**Internal auto-routing expectation:** NO  
**Source:** https://buffer.com/pricing

### Submission prompt

```text
Buffer offers annual billing on its paid plans. Prepare the ASC 606 revenue
recognition treatment and journal entries for a customer who prepays an annual
subscription, including deferred revenue and monthly recognition.
```

### Internal auto-routing expectation

Marketing Practitioner should not be selected in the clean auto-routing run.

### Expected submission behavior

Use a safe fallback or handoff to an accounting/finance capability if available.
If the plugin was already explicitly selected, recognize that accounting owns
the task and do not apply commercial-design guidance as a substitute.

### Why Marketing Practitioner should not complete this task

Pricing is mentioned, but the requested work is revenue recognition and
journal-entry accounting, which is outside Marketing Practitioner's ownership.

---

# Mapping summary

| Case | Runtime job | Primary repo owner | What it pressures |
| --- | --- | --- | --- |
| SUB-POS-001 | RESEARCH / UNDERSTAND | Chapter 01 | source-unit discipline, qualitative evidence, no prevalence inflation |
| SUB-POS-002 | DECIDE | commercial-design.* | configuration/payment/modifiers, evidence before redesign |
| SUB-POS-003 | DIAGNOSE | Chapter 05 -> etsy.diagnosis -> paid-media if reached | causal diagnosis, mixed drivers, intervention gating |
| SUB-POS-004 | DECIDE / founder-led sales | founder-sales.* | pursuit, proof gaps, buyer state, no capability hallucination |
| SUB-POS-005 | WRITE | Chapter 04 + landing-page.* | resolved-state preservation, proof allocation, usable execution |
| SUB-NEG-001 | outside scope | technical implementation | noun overlap must not trigger marketing |
| SUB-NEG-002 | outside scope | legal dependency | sales context must not create legal authority |
| SUB-NEG-003 | outside scope | finance/accounting dependency | pricing noun must not override actual accounting job |

# Live-run gate

Before these are copied into the OpenAI submission form:

1. run the final package against all eight prompts in a clean conversation with
   the skill installed but not explicitly invoked;
2. record actual output and whether the skill was selected;
3. optionally rerun the three negative prompts with the plugin explicitly
   selected to verify boundary/handoff behavior;
4. compare actual activation and task behavior with the expectations above;
5. repair the case wording only when the case is ambiguous; repair the skill
   only when the behavior exposes a real runtime defect;
6. freeze the final prompt text and expected behavior used for submission.

Do not represent this file as live behavioral evidence until that run exists.
