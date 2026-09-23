# SaaS Opportunity Cookbook
Last updated: 2026-09-23 | Entries: 9/10

> R7 note: **FlowTrace removed** — Sanctum Runtime now sells approve/block/pause from $12–$59/mo across OpenAI-compatible and Claude/MCP tool calls. The August “remove next run if a pause SKU ships” condition is met. No new idea cleared the bar. **StatusCard** (Slack scavenger hunt) lost to briefhq chat on HubSpot+Stripe. **GPSR file generators** (EUProof, Eldris) and **Shopify GPSR widgets** already exist. **SMB offboarding** is CloudM, Zenphi, and Substly. **Battery DPP** (18 Feb 2027) is Provenant and Sensoneo dpp.gs. DentPay holds #1: Samera’s live list is still Dentally + Xero; Dentivize connects US PMS but sells KPI dashboards, not production-% pay.

---

## #1 — DentPay  ·  78/100  ·  DECLINED
First added: 2026-07-16 | Last updated: 2026-09-23 | Score delta this week: −2

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — CSV-first rule engine)
- Value Clarity:       18/20  (unchanged — OM ritual self-evident)
- Market Timing:       15/20  (−2 — Dentivize now lists live connectors for Open Dental, Dentrix, and Eaglesoft at $149/mo and shows payroll as a KPI. It is still an analytics dashboard, not a pay-rule engine. Samera’s integrations page lists Dentally and Xero as live; SoE, Sage, QuickBooks, R4, and Exact are “coming soon,” not OD/Dentrix. HRPayPick 2026 still says no payroll platform has native production import for all three US PMS.)
- B2B Monetisation:    16/20  (unchanged)
- Pull Factor:         13/20  (unchanged — study clubs)

**Strengths:**
- HRPayPick 2026 still says Gusto, OnPay, and peers have no native production-pay import from Dentrix or Eaglesoft. Open Dental users build their own CSV bridges. That is the product.
- Dentivize’s own pricing page sells “performance & financial dental KPIs” and overhead/payroll metrics, not per-provider lab-fee and write-off rules with a Gusto approval pack.
- Sticky once pay rules are configured — a wrong paycheck is employer liability.

**Risks:**
- Dentivize already has the PMS pipes. Adding pay-rule math is a product decision, not a data-access project.
- Samera’s “request an integration” form is how a US PMS would show up. Recheck the live list monthly.
- Practices may not trust paycheck math from a solo tool without a CPA partner.

**Verdict:** Hold #1. The US export-to-paycheck job is still open. The threat is Dentivize adding rules, not Samera shipping Dentrix.

### The Pitch
**Problem:** US dental practices paying associates and hygienists on production still spend hours each pay period exporting Open Dental or Dentrix reports, pasting into Excel, applying lab fees, write-offs, and card-fee rules, then hoping the spreadsheet matches the contract. Open Dental's Provider Payroll report is raw material, not a pay engine. Samera automated this for UK Dentally and Xero. Gusto deposits pay but does not reconcile OD production rules. HRPayPick 2026 confirms no payroll platform has native plug-and-play integration with all three major US PMS systems.

**Solution:** DentPay imports OD/Dentrix production exports, applies per-provider pay rules once, flags anomalies before payout, and exports an approval pack to Gusto/ADP. Office managers review exceptions; they do not rebuild formulas.

**Target customer:** Office manager / owner at 1–3 location US dental practice on Open Dental or Dentrix with associates or hygienists on production splits.

**Why now:** Production-% pay is still the norm. Samera proved the pay-calculation job in the UK on Dentally+Xero and has not shipped Open Dental or Dentrix. Dentivize proved US practices will connect those PMS systems, but it sells dashboards.

**Why they buy without being sold to:** An office manager who spent Sunday fixing a hygienist underpay uploads last month's OD export, sees the same total with three flagged lab mismatches, and refuses to go back to Excel.

**Revenue model:** $149 / $249 / $399 per practice. 30-day trial. CPA referral 15%.

**Unfair advantage:** US OD/Dentrix rule templates and an anomaly library. Study-club distribution. A dashboard company and a UK accountant product are not optimising for a $149 US paycheck file.

### Solo Build Plan
1. Weeks 1–3: OD Provider Payroll CSV ingest; rule builder; pay summary PDF.
2. Weeks 4–5: Anomaly flags; vs last period; Gusto CSV export.
3. Weeks 6–7: Dentrix path; multi-provider approval.
4. Weeks 8–9: Stripe; sample-file onboarding.
5. Weeks 10–12: Pilot 8 practices via dental groups / OD user groups.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-09-23
**Strongest part:** Two live sites still miss the job. Samera’s integration list has no US PMS. Dentivize’s $149 plan is KPI dashboards. HRPayPick still documents the CSV gap.
**Open question:** Will Dentivize add per-provider pay rules on the connectors it already has, before DentPay has eight reference practices?

---

## #2 — AdvisorAlert  ·  74/100  ·  UNCHANGED
First added: 2026-07-31 | Last updated: 2026-09-23 | Score delta this week: —

> Catch compliance gaps before the SEC exam does — continuous monitoring built for independent RIAs, not mega-firms.

### Score Breakdown
- Solo Buildability:   12/20  (unchanged — email sampling in a regulated context; a 5-check MVP is still the scope)
- Value Clarity:       17/20  (unchanged — a deficiency letter is a 10-second pitch)
- Market Timing:       16/20  (unchanged — Hadrius still publishes no price. RightAIChoice and Luthor, 2026, both say custom quote only. No starter tier under $5K is on the site.)
- B2B Monetisation:    17/20  (unchanged — $299–799/month vs a $5K–$20K consultant)
- Pull Factor:         12/20  (unchanged — custodian and study-group referrals, not public viral)

**Strengths:**
- Hadrius’s raise validated RIA compliance automation. Pricing is still sales-led.
- The 1–5 person RIA is not the buyer Hadrius’s “hundreds of employees / $2T AUM” story is written for.
- RIAs already pay consultants. A monitoring subscription is an easy comparison.

**Risks:**
- Must be sold as monitoring, not advice, or it trips adviser-registration issues.
- Hadrius can still ship a micro-RIA starter from the same funding.
- False positives on ordinary client email destroy trust.

**Verdict:** Keep the micro-RIA beachhead. The under-$5K public tier still does not exist.

### The Pitch
**Problem:** Independent registered investment advisors with $50M–$500M AUM typically have 1–5 employees, no dedicated CCO, and rely on an annual compliance consultant for $5,000–$20,000/year. Meanwhile the SEC expects continuous monitoring: reviewing client communications for solicitation violations, sampling marketing content, confirming trades match investment policy statements, maintaining a current compliance calendar. Hadrius validated the category and still sells by quote to larger firms. The 1–5 person shop has no purpose-built tool under $5K/year.

**Solution:** AdvisorAlert connects to your Gmail or Outlook, samples 50 client communications per month, and flags language that could constitute testimonials, solicitations, or performance guarantees. It also maintains your compliance calendar (Form ADV due dates, custody rule filings, code of ethics deadlines) and lets you submit marketing content for a plain-English compliance check. The weekly digest is your CCO's to-do list — not a 200-page manual.

**Target customer:** Principal / de-facto CCO at a 1–5 person RIA, $50M–$500M AUM, serving retail or HNW clients on Schwab, Fidelity, or Pershing. Not a broker-dealer, not a family office. Buyer: the principal who is also the CCO. Users: principal + any administrative staff who handle client communication.

**Why now:** AI communication volume is widening the review gap faster than headcount. Hadrius proved the category and, as of this run, still has no public starter price. Small RIAs keep paying consultants for a calendar and an email sample.

**Why they buy without being sold to:** An RIA principal who received an SEC deficiency letter for "inadequate email review" starts a free AdvisorAlert trial, connects their inbox, and sees their first flagged communication within 5 minutes.

**Revenue model:** $299/month (email sampling for 1 inbox, compliance calendar, 12 framework checks). $499/month (3 inboxes + marketing content review PDF upload). $799/month (unlimited + trade surveillance from Schwab/Fidelity custodian data feeds). Annual −2 months. Free compliance calendar (no email connection required) as lead generation entry point.

**Unfair advantage:** Micro-RIA compliance calendar templates built for the 1–5 person shop. Distribution through Schwab Advisor Services and Fidelity Institutional communities, not an enterprise sales team.

### Solo Build Plan
1. Weeks 1–2: Free compliance calendar (ADV, custody, code of ethics deadlines) — ship as a stand-alone lead magnet with no email connection.
2. Weeks 3–4: Gmail/Outlook OAuth; email ingestion; AI flag for testimonials, performance guarantees, solicitation language with explainability.
3. Weeks 5–6: Compliance calendar integration with email alerts; marketing content review (PDF/LinkedIn post upload).
4. Weeks 7–8: Stripe; free-calendar to paid-monitoring funnel; legal review of ToS ("monitoring tool, not compliance advice").
5. Weeks 9–12: Pilot 5 micro-RIAs through Schwab advisor network referrals and IAA or NAPFA regional events.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** Hadrius validated the category and still hides the price. That is the gap.
**Open question:** Hadrius starter tier under $5K/year?

---

## #3 — RuleFlow  ·  73/100  ·  UNCHANGED
First added: 2026-08-16 | Last updated: 2026-09-23 | Score delta this week: —

> New federal rules become a checklist and an evidence folder — not another unread PDF in Slack.

### Score Breakdown
- Solo Buildability:   13/20  (unchanged — obligation feed plus Jira/Asana plus an evidence ZIP; legal review is the hard part)
- Value Clarity:       16/20  (unchanged — “this rule changed, here is the owner and the date”)
- Market Timing:       16/20  (unchanged — frtracker.app is still a research evidence map, not a task system. CUBE, Ascent, Resolver, and Bloomberg Regology still sell libraries and enterprise workflow.)
- B2B Monetisation:    17/20  (unchanged)
- Pull Factor:         11/20  (unchanged)

**Strengths:**
- FRTracker extracts sourced obligations. It does not assign an owner, a due date, or an evidence slot.
- Enterprise regulatory-change tools still start as library products for Tier-1 firms.
- Traceable quotes back to the Federal Register are what a small exam team can defend.

**Risks:**
- FRTracker, or a funded RegTech, adds “send to Jira.”
- A wrong obligation map is a liability. The product is monitoring, not advice.
- The count of 20–200 person fintech lenders is smaller than the pitch sounds.

**Verdict:** Hold. The workflow layer on a public obligation feed is still unshipped.

### The Pitch
**Problem:** A four-person compliance team at a community bank or fintech lender tracks Federal Register changes in a shared spreadsheet and a Slack channel of PDFs. CUBE and Ascent sell this to Tier-1 banks. FRTracker extracts obligations from primary text and shows evidence hashes — and it is still a research tool. When a final rule drops, nobody owns the checklist, and the exam asks for evidence that does not exist.

**Solution:** RuleFlow turns each relevant obligation into a task with an owner, a due date, and an evidence slot. It watches the agencies you care about, diffs proposed vs final, and opens Asana/Jira items mapped to the source passage. At exam time you export a folder: rule, obligation, who did what, attached proof.

**Target customer:** CCO / compliance analyst at a 20–200 person US fintech lender, community bank, or payments firm. Buyer: CCO or General Counsel. Users: the 2–6 people who currently paste Federal Register links into Slack.

**Why now:** The open primitive exists and has not grown a workflow. Enterprise RegTech still sells breadth. A four-person team needs one agency family and an evidence folder.

**Why they buy without being sold to:** After a consent order or a nasty Federal Register notice, the CCO pastes last month’s spreadsheet into RuleFlow, sees three missed effective dates, and refuses to go back to Slack PDFs.

**Revenue model:** $399/mo (1 agency family + 10 users). $599/mo (3 families + Jira/Asana sync). $799/mo (unlimited + evidence vault + SSO). Annual −2 months. 14-day trial on a saved agency watchlist.

**Unfair advantage:** Obligation, task, and evidence for one vertical (US fintech lending / community banks), with citations back to primary text.

### Solo Build Plan
1. Weeks 1–3: Ingest daily Federal Register deltas or the FRTracker-style obligation feed; agency watchlist; obligation cards with source quotes.
2. Weeks 4–5: Task export to Asana/Jira; owner and due date; proposed-vs-final diff.
3. Weeks 6–7: Evidence upload per obligation; exam-pack ZIP/PDF.
4. Weeks 8–9: Stripe; fintech-lending template.
5. Weeks 10–12: Pilot 5 CCOs via community-bank ops groups and fintech compliance Slack.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** The research tool is public. The unpaid job is still owner, date, and proof.
**Open question:** Will FRTracker itself add “send to Jira” and eat the wedge?

---

## #4 — ChurnDetect  ·  71/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-09-23 | Score delta this week: −2

> Find the customers about to leave — 90 days before they tell you — from the support tickets they are already sending.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged)
- Value Clarity:       17/20  (unchanged — retrospective demo still self-closing)
- Market Timing:       12/20  (−1 — Zendesk QA Spotlight now flags tickets where a customer explicitly says they will cancel or switch. It is still per conversation, not an account score 90 days out.)
- B2B Monetisation:    15/20  (unchanged)
- Pull Factor:         12/20  (−1 — Spotlight, Pecan, Gainsight, and ChurnZero all use the word churn)

**Strengths:**
- Spotlight catches the sentence “cancel my subscription.” It does not rank accounts by the prior 90 days of unresolved threads.
- The retrospective on a churned account is still a demo that does not need a pitch.
- Gainsight and ChurnZero remain far above a 10–150 person SaaS budget.

**Risks:**
- Zendesk can roll Spotlight flags up to the organisation object. That is the kill.
- Support text is customer PII. Consent and retention have to be explicit.
- Planhat and similar mid-market CS tools can move down.

**Verdict:** Hold the account-level retrospective. Do not claim “Zendesk cannot see churn” — it can see the explicit sentence.

### The Pitch
**Problem:** B2B SaaS companies discover customer churn risk almost exclusively at renewal time, when the decision is already made. The warning signals — repeated unresolved issues, competitor mentions, escalating response times — are buried in the support inbox. Zendesk can now highlight a ticket where someone says they will cancel. It does not tell a CSM which $50K account has been quietly deteriorating for 90 days. The first official indication is still often a “not renewing” email.

**Solution:** ChurnDetect connects to Zendesk or Intercom, reads the past 6 months of tickets, and rolls threads up to the account: unresolved patterns, feature gaps, and competitive mentions. The weekly list is accounts, with the threads that triggered the flag, not a queue of angry sentences.

**Target customer:** Customer success manager / VP CS at a 10–150 person B2B SaaS company with 100+ customers, on Zendesk or Intercom, without Gainsight or ChurnZero. Buyer: VP CS or CRO. Company runs roughly $1M–$15M ARR.

**Why now:** Ticket-level churn language is now a Zendesk QA feature. Account-level pattern detection across a quarter of tickets is still a separate product, and the model cost is under a tenth of a cent per ticket.

**Why they buy without being sold to:** A CS manager who lost a $30K account runs the retrospective on that account’s last tickets, sees the pattern 90 days before the cancel sentence, and buys. The demo is their own history.

**Revenue model:** $199/month (up to 500 accounts + Zendesk). $349/month (unlimited accounts + Intercom/Zendesk + Slack alerts). $599/month (API + custom risk taxonomy). 14-day free trial. Annual −2 months.

**Unfair advantage:** The historical retrospective. Vertical risk taxonomies for B2B SaaS that a generic “cancel” keyword does not have.

### Solo Build Plan
1. Weeks 1–3: Zendesk connector; 6-month ticket ingest; thread classification.
2. Weeks 4–5: Account rollup; weekly Slack digest with evidence links.
3. Weeks 6–7: Intercom; custom risk terms.
4. Weeks 8–9: Stripe; retrospective demo on five historical accounts; consent flow.
5. Weeks 10–12: Pilot 8 SaaS companies through CS-leader communities.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-23
**Strongest part:** Spotlight answered the keyword. It did not answer “which account, 90 days ago.”
**Open question:** Will Zendesk attach Spotlight churn flags to the organisation and call it account health?

---

## #5 — BreakWatch  ·  67/100  ·  UNCHANGED
First added: 2026-08-16 | Last updated: 2026-09-23 | Score delta this week: —

> Know which of your vendors shipped a breaking API change before production does.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — changelog crawlers, OpenAPI diff, Slack)
- Value Clarity:       14/20  (unchanged)
- Market Timing:       11/20  (unchanged — no confirmed cheap “watch these vendor APIs you do not own” SKU found this run. Producer doc tools remain the crowded shelf.)
- B2B Monetisation:    14/20  (unchanged)
- Pull Factor:         13/20  (unchanged)

**Strengths:**
- Teams that consume HubSpot, Stripe, QuickBooks, and Shopify still find out in production.
- AI agents made a stale field mapping a bad write, not only a stale dashboard.
- Onboarding is “paste the APIs that paged you.”

**Risks:**
- Optic, Speakeasy, or Bump.sh can ship a consumer watchlist. That is still the kill condition.
- Changelog formats are messy. False alarms kill the Slack channel.
- Unified API vendors can fold monitoring into the connector fee.

**Verdict:** Last seat on the consumer-side watch. Remove next run if a named vendor-watch SKU is live under $400/month.

### The Pitch
**Problem:** A 15-person SaaS maintaining HubSpot, Stripe, QuickBooks, and Shopify integrations finds out about breaking changes when customers file tickets. Producer-side documentation tools help the company that publishes the API. They do not watch the APIs you consume. Specway’s 2026 integration report put undocumented breaking changes at the centre of that failure.

**Solution:** BreakWatch watches the vendor APIs you depend on — changelogs, OpenAPI diffs, status pages — and opens a Slack item when a field disappears or an auth flow changes. You subscribe to endpoints, not to a new integration platform.

**Target customer:** Eng lead at a 5–30 person SaaS with 5–15 outbound integrations. Buyer: CTO. Users: the engineers on integration on-call.

**Why now:** Agent workflows write back into customer systems. A renamed field is no longer a display bug.

**Why they buy without being sold to:** After a silent HubSpot field rename corrupts a week of deals, the eng lead adds HubSpot to BreakWatch and requires a Slack ping before the next change hits production.

**Revenue model:** $149/mo (10 watched APIs). $249/mo (30 APIs + OpenAPI diff). $399/mo (contract-test hooks). Annual −2 months. 14-day trial.

**Unfair advantage:** A watchlist of the APIs small SaaS actually breaks on, maintained as consumer-side alerts.

### Solo Build Plan
1. Weeks 1–3: Watchers for Stripe, HubSpot, Shopify, QuickBooks; Slack alerts.
2. Weeks 4–5: Diff UI; mute controls.
3. Weeks 6–7: GitHub Action that comments when a watched spec moved.
4. Weeks 8–9: Stripe billing; incident-paste onboarding.
5. Weeks 10–12: Pilot 6 SaaS teams via r/SaaS and integration Slack groups.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-08-16
**Strongest part:** The buyer consumes APIs. The incumbents document APIs they publish.
**Open question:** Does Optic or Speakeasy already sell “watch vendor APIs you don’t own”?

---

## #6 — MarkPack  ·  64/100  ·  DECLINED
First added: 2026-08-03 | Last updated: 2026-09-23 | Score delta this week: −9

> One evidence folder for Article 50 marks and disclosures — for the product Encypher and Capture do not already sign.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — disclosure snippets, one marking path, ZIP evidence)
- Value Clarity:       14/20  (−2 — Encypher’s free tier already returns a marked text plus a downloadable evidence record)
- Market Timing:       12/20  (−5 — Article 50 applies since 2 Aug 2026. Commission transparency guidelines are published. Encypher and Capture both ship C2PA-class marking and an audit export. The 2 Dec 2026 grace for systems already on the market is about ten weeks out.)
- B2B Monetisation:    13/20  (−1 — free tiers and $0 entry make $199/mo a comparison, not a default)
- Pull Factor:         11/20  (−1 — eng buyers will try the free marker first)

**Strengths:**
- The obligation is in force, and the Commission has published guidelines on how to show it.
- A multi-product SaaS still needs one folder: which features are in scope, who owns disclosure, what the CI check failed.
- Encypher is a marking API. Capture is a signing API plus a chain layer. Neither is a product inventory.

**Risks:**
- Buyers will not pay $199/mo to wrap a free evidence record they can download today.
- Adobe and model providers can mark outputs at the source.
- Demand can fall off after 2 December if enforcement stays quiet.

**Verdict:** Keep only as the inventory-and-CI layer. Do not rebuild a marking API. One more run, then remove if no design-partner will pay beside Encypher’s free tier.

### The Pitch
**Problem:** Article 50 transparency duties have applied since 2 August 2026. Chatbots must disclose that a person is talking to AI. Generative systems need machine-readable marks, with a grace to 2 December 2026 for systems placed on the market before 2 August. Encypher will mark a piece of text and hand back an evidence record. Capture will sign a file and export an audit view. A 40-person SaaS with a chatbot, an email writer, and an image tool still cannot answer “which of our features are in scope, which marks survived, and where is the folder for counsel?”

**Solution:** MarkPack does not replace the marker. It is the register: each AI feature, the disclosure surface, the marking vendor, the last CI result, and a ZIP that maps those rows to Article 50 paragraphs. A GitHub Action fails the build when a feature is in scope and the mark step is missing.

**Target customer:** Eng lead and counsel at a 15–150 person company shipping more than one EU-facing AI feature. Buyer: CTO or GC. Users: the engineer who wires Encypher or Capture, and the lawyer who has to show the folder.

**Why now:** The guidelines are published, so “we will wait for the code of practice” is a weaker excuse. The December grace is the remaining date that still creates a sprint. After that, the sale is an audit, not a deadline.

**Why they buy without being sold to:** Counsel asks for one evidence pack covering three features. Eng has three vendor dashboards and a Notion page. MarkPack’s ZIP is the reply.

**Revenue model:** $199/mo (up to 5 AI features, evidence ZIP, one CI repo). $349/mo (SSO, retention, multiple repos). Annual −2 months. 14-day trial that imports a CSV of features and emits a sample pack. No charge for the marking API — the customer brings Encypher, Capture, or their own.

**Unfair advantage:** The register and the CI gate, updated when Commission guidance changes. Marking vendors want to sign bytes. They do not want to own your feature inventory.

### Solo Build Plan
1. Weeks 1–2: Feature register; obligation rows; sample ZIP from a CSV. No watermark code.
2. Weeks 3–4: GitHub Action that checks a manifest the customer’s marker already writes.
3. Weeks 5–6: Disclosure snippet library for chat widgets; screenshot slot in the pack.
4. Weeks 7–8: Stripe; import from a one-page questionnaire.
5. Weeks 9–10: Five design partners who already pay a marking vendor. If none will pay for the folder, stop.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-09-23
**Strongest part:** The rewrite stops competing with Encypher’s free evidence file and sells the multi-feature register those tools do not have.
**Open question:** Will anyone pay for the folder once the free marker already downloads a per-content record?

---

## #7 — BriefDesk  ·  64/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-09-23 | Score delta this week: −8

> A Friday leadership note from the tools Brief does not already brief — or leave the category.

### Score Breakdown
- Solo Buildability:   17/20  (unchanged — three OAuth apps and a weekly prompt)
- Value Clarity:       14/20  (−3 — “a weekly brief from HubSpot, Stripe, and Linear” is now Brief’s own docs)
- Market Timing:       8/20  (−4 — briefhq.ai documents HubSpot OAuth, a Stripe restricted key, Linear, and scheduled Weekly Brief agents. The product graph also drafts stakeholder updates from Linear, GitHub, and Slack.)
- B2B Monetisation:    14/20  (−1 — the buyer can trial the incumbent)
- Pull Factor:         11/20  (−1)

**Strengths:**
- The Friday copy-paste ritual is still real for firms that are not on Brief’s connector list.
- QuickBooks or Xero plus a professional-services project tool is a narrower stack than “HubSpot + Stripe + Linear.”
- Synthesis cost is still cents per brief.

**Risks:**
- Brief already answers “what’s our MRR?” and ships a weekly agent. The August open question is closed.
- HubSpot Breeze and Data Parrot cover the CRM-only version.
- A rename does not create a new job if the job is “weekly narrative from live tools.”

**Verdict:** Last seat. Remove next run unless a paid pilot is on a stack Brief’s docs do not list (QuickBooks + a PS project tool, not HubSpot+Stripe+Linear).

### The Pitch
**Problem:** The generic “Monday brief from CRM, projects, and billing” is no longer empty. Brief connects HubSpot and Stripe, runs scheduled weekly agents, and drafts status updates from Linear, GitHub, and Slack. Agencies and professional-services firms that run QuickBooks or Xero and a delivery tool Brief does not treat as the system of record still build the Friday note by hand. That remaining ritual is the only BriefDesk that is still a product.

**Solution:** BriefDesk connects one accounting ledger (QuickBooks or Xero) and one delivery system (a PS project tool), and sends one Friday note: what was billed, what slipped, what needs a partner decision. It does not try to be a product-decision graph for a software company already on Linear.

**Target customer:** Operations lead at a 10–80 person agency or professional-services firm on QuickBooks or Xero, not a venture-backed SaaS team on HubSpot and Linear. Buyer: founder or COO. User: the person who currently pastes into a doc on Friday.

**Why now:** The horizontal weekly brief shipped in 2026. The leftover buyer is the services firm whose billing system is the ledger, not Stripe.

**Why they buy without being sold to:** They connect QuickBooks, receive Friday’s note with the three slipped projects and the invoices that do not match time, and stop building the doc. If their stack is HubSpot plus Stripe plus Linear, they should buy Brief instead.

**Revenue model:** $149/month (one ledger + one project tool, one brief a week). $249/month (client-level briefs for an agency). Annual −2 months. 14-day trial. No HubSpot-first plan — that plan is how this product loses.

**Unfair advantage:** Templates for billable-work firms: utilisation, write-offs, and slipped retainers. Not a second product graph.

### Solo Build Plan
1. Weeks 1–3: QuickBooks or Xero plus one project tool. Refuse HubSpot as the first connector.
2. Weeks 4–5: Friday narrative with week-over-week numbers and a human edit step.
3. Weeks 6–7: Slack delivery; stale-data warning.
4. Weeks 8–9: Stripe; trial that generates two briefs from live data.
5. Week 10: Five agency pilots. If they say Brief or a spreadsheet is enough, remove the entry.

### Critic's Assessment
**Rating:** 5/10 | **Last critique:** 2026-09-23
**Strongest part:** The rewrite admits Brief won the SaaS stack and keeps only the services-ledger brief.
**Open question:** Is QuickBooks plus a project tool enough of a gap once Brief adds those connectors?

---

## #8 — TokenBill  ·  63/100  ·  DECLINED
First added: 2026-08-16 | Last updated: 2026-09-23 | Score delta this week: −9

> Leave invoice-level AI forecasts to StackSpend and Finout — or find a buyer they do not serve.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — read-only billing connections are buildable)
- Value Clarity:       13/20  (−3 — “pace to forecast across OpenAI, Anthropic, and Cursor” is StackSpend’s homepage)
- Market Timing:       8/20  (−5 — StackSpend ships daily Slack, anomaly alerts, and pace-to-forecast for those vendors. Finout puts OpenAI, Anthropic, Bedrock, Vertex, and Cursor on the same bill as cloud, with no SDK. CloudZero ingests Anthropic admin usage.)
- B2B Monetisation:    14/20  (−1)
- Pull Factor:         12/20  (unchanged)

**Strengths:**
- Finance still hates opening four consoles. That pain is why three products launched.
- A 15-person company may bounce off Finout’s FinOps positioning.
- Card-statement ingest, with no admin API key, is a thinner setup than CloudZero’s Anthropic connection.

**Risks:**
- StackSpend already is the no-SDK, multi-vendor, Slack-forecast product from August’s pitch.
- Ramp or Brex categorising “AI vendors” would finish the casual buyer.
- Rebuilding parsers against a live competitor is a solo tax with no moat.

**Verdict:** Last seat, and a weak one. Remove next run unless the offer is explicitly “PDF forward only, for companies that will not create an admin key” and a pilot prefers it to StackSpend.

### The Pitch
**Problem:** The August pitch — one forecast for OpenAI, Claude, and Cursor before the invoice, delivered to finance, with no SDK in the app — is now a shipping product. StackSpend monitors those providers, sends a daily Slack or email signal, and shows pace-to-forecast. Finout allocates the same vendors beside cloud spend. TokenBill cannot win by repeating that sentence.

**Solution:** The only remaining setup is forwarding PDFs and billing emails, for a bookkeeper who will not create an OpenAI admin key or an Anthropic analytics key. TokenBill parses those documents, labels estimates versus billed amounts, and alerts when a vendor is running hot. If the buyer can paste an API key, they should use StackSpend.

**Target customer:** Fractional CFO or bookkeeper serving 20–80 person companies that pay 3+ AI vendors on a card and will not administer provider consoles. Buyer: the fractional CFO. Not the startup that already has a platform admin.

**Why now:** The funded and productised forecast tools assume an API key. A bookkeeper’s inbox is still PDFs. That is a smaller market than August’s pitch claimed.

**Why they buy without being sold to:** They forward a quarter of invoices, see a run-rate that matches the card, and set an alert. If they are willing to connect a read-only key, the trial should tell them to leave.

**Revenue model:** $99/mo (email forward, 5 vendors). Do not price at $249 beside StackSpend’s key-based product. Annual −2 months. Kill the SKU if five bookkeepers will not pay.

**Unfair advantage:** None against a key-based tool. The only edge is refusal to ask for an admin key, which is also the reason the data is worse.

### Solo Build Plan
1. Week 1: Use StackSpend and Finout on a personal account. Write down what the PDF-only user still cannot do.
2. Weeks 2–4: If that gap is real, ship email-forward parse for three invoice formats only.
3. Weeks 5–6: Run-rate and a Slack alert. Label every figure billed vs estimated.
4. Week 7: Five bookkeeper conversations. No Stripe until one prepays.
5. If nobody prepays, delete the product. Do not add team allocation.

### Critic's Assessment
**Rating:** 4/10 | **Last critique:** 2026-09-23
**Strongest part:** The critique names the incumbent instead of repeating “not Langfuse.”
**Open question:** Is there a bookkeeper who will not create a read-only key and will still pay $99/month?

---

## #9 — AuthTrack  ·  61/100  ·  DECLINED
First added: 2026-08-16 | Last updated: 2026-09-23 | Score delta this week: −9

> A prior-auth clock for practices whose own advisors are telling them to use a spreadsheet.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — CSV log, clocks, HIPAA)
- Value Clarity:       12/20  (−4 — Staffingly, Clunic, and AMS tell practices the rule binds payers, and that a spreadsheet is the 2026 control)
- Market Timing:       11/20  (−3 — 7-day and 72-hour clocks have been live since 1 Jan 2026. FHIR prior-auth APIs are still 1 Jan 2027. The 2026 advice in public checklists is “do not buy a module.”)
- B2B Monetisation:    13/20  (−1 — one avoided write-off still pays, but the buyer is being coached not to purchase)
- Pull Factor:         11/20  (−1)

**Strengths:**
- A biller who misses a clock loses the appeal window even if the legal duty sits on the payer.
- Linear Health still aims at specialty groups on Athena, not a two-provider fax log.
- v1 does not need an EHR writeback.

**Risks:**
- The open question from August is being answered in public: “use a spreadsheet, do not overpay.”
- Clearinghouses can add a clock before 2027.
- HIPAA scope is real for a product this small.

**Verdict:** Last seat. Remove next run without a biller who will pay after reading a “you do not need software” checklist.

### The Pitch
**Problem:** Since 1 January 2026, impacted payers must decide standard prior auths in 7 calendar days and urgent ones in 72 hours, and denials need a specific reason. The duty is on the payer. Practice checklists published in 2026 say the provider control is a spreadsheet: date received, clock, denial text. AuthTrack only exists if that spreadsheet is where clocks actually get missed, and if a biller will pay to stop missing them. It is not a compliance product the practice is required to buy.

**Solution:** AuthTrack is that spreadsheet with a clock that turns red and a denial-reason field that will not save blank. CSV import, email reminders, an appeal PDF. No FHIR client. No claim that the practice is “CMS-0057 compliant” because they subscribed.

**Target customer:** Billing coordinator at a 2–10 provider practice still on fax and Excel, not on Athena with an automation vendor. Buyer: office manager. User: the biller.

**Why now:** The clocks are already in force, so the pain is operational, not anticipatory. The 2027 API date is a reason not to buy a portal robot. It is not a reason to buy a timer unless the timer is cheaper than a missed appeal.

**Why they buy without being sold to:** They import the sheet, see two clocks already past, and keep the board. If they shrug and go back to Excel, the product is wrong.

**Revenue model:** $99/mo for one location. The old $149–$299 range fights the “do not buy software” advice. 14-day trial with a sample CSV. Annual −2 months.

**Unfair advantage:** A required denial-reason field and a clock, priced like a utility. Enterprise PA platforms will not bother.

### Solo Build Plan
1. Weeks 1–2: CSV log, 7-day and 72-hour clocks, denial reason required.
2. Weeks 3–4: Email reminder and a one-page appeal PDF.
3. Week 5: Show it to six billers. Ask them to pay $99. HIPAA BAA only if two say yes.
4. Do not build SMS, multi-site, or EHR writeback before a prepay.
5. If the answer is “our sheet is fine,” remove the entry.

### Critic's Assessment
**Rating:** 5/10 | **Last critique:** 2026-09-23
**Strongest part:** The pitch now matches the public checklists: payers owe the decision; the practice owes a log. The product is only the log.
**Open question:** Will a biller pay $99 after a consultant told them Excel is the control?

---

## Removed this run
| Entry | Last score | Reason |
|-------|------------|--------|
| FlowTrace | 62 → 48 | **Sanctum Runtime** sells observe vs govern. Personal is $12/mo and Operator is $59/mo to approve, block, or hold tool calls, including OpenAI-compatible traffic and Claude/MCP. SanctumShield at $99/mo remains a policy PDF, which August already priced in. The runtime pause was the remaining wedge. It is a live price page. Below the keep line. |
