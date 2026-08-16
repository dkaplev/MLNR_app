# SaaS Opportunity Cookbook
Last updated: 2026-08-16 | Entries: 10/10

> R6 note: Four last-seat/failed-canary exits. **WholesaleDesk removed** — Orderwerks/Zoey/WizCommerce already ship QuickBooks-native B2B portals. **QuoteDock removed** — FasterQuotes/Vesel/Navix own email-forward RFQ. **DataReady removed** — Datris hosted + HubSpot Data Agent. **PromptFence removed** — RAIC/PromptWall/SanctumShield. **RuleFlow** enters on YC’s AI-native compliance RFS + FRTracker-as-primitive. **TokenBill** is finance-facing token shock (not Langfuse). **AuthTrack** is CMS-0057-F clocks for fax-era practices. **BreakWatch** is consumer-side API break alerts. DentPay holds #1 (Samera still Dentally/SoE).

---

## #1 — DentPay  ·  80/100  ·  UNCHANGED
First added: 2026-07-16 | Last updated: 2026-08-16 | Score delta this week: —

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — CSV-first rule engine)
- Value Clarity:       18/20  (unchanged — OM ritual self-evident; dentpay.tech + numbers walkthrough)
- Market Timing:       17/20  (unchanged — Aug 16 canary: Samera FAQ still Dentally + SoE only; custom integrations “tell us what you use,” not a live OD/Dentrix SKU; Xero live, QBO in development; Dentivize still analytics dashboards; OD Provider Payroll still a report)
- B2B Monetisation:    16/20  (unchanged)
- Pull Factor:         13/20  (unchanged — study clubs; US outreach guide for discovery calls)

**Strengths:**
- HRPayPick 2026 confirms: no payroll platform has native plug-and-play integration with OD, Dentrix, and Eaglesoft simultaneously. The production-% reconciliation gap is documented and unresolved.
- Dentivize.com = analytics competitor (dashboard overlay showing take-home %), not a pay calculation engine. DentPay's "CSV-to-paycheck export with anomaly flags" is still unclaimed.
- Sticky once pay rules configured — wrong paycheck = employer liability; switching cost is existential.

**Risks:**
- Dental Intelligence or Dentrix itself could deepen native pay math in a platform update.
- Dentivize with expanded payroll reconciliation features would be a direct threat.
- Relationship-heavy sales; CPA/advisor trust needed for paycheck-math credibility.

**Verdict:** Hold #1. US OD CSV-first beachhead still open; watch Samera custom-integration requests.

### The Pitch
**Problem:** US dental practices paying associates and hygienists on production still spend hours each pay period exporting Open Dental or Dentrix reports, pasting into Excel, applying lab fees, write-offs, and card-fee rules, then hoping the spreadsheet matches the contract. Open Dental's Provider Payroll report is raw material, not a pay engine. Samera automated this for UK Dentally+Xero; Gusto deposits pay but does not reconcile OD production rules. HRPayPick 2026 confirms no payroll platform has native plug-and-play integration with all three major US PMS systems.

**Solution:** DentPay imports OD/Dentrix production exports, applies per-provider pay rules once, flags anomalies before payout, and exports an approval pack to Gusto/ADP. Office managers review exceptions; they do not rebuild formulas.

**Target customer:** Office manager / owner at 1–3 location US dental practice on Open Dental or Dentrix with associates or hygienists on production splits.

**Why now:** Production % pay still the norm; UK tools (Samera/Dentivize) proved analytics willingness-to-pay; US PMS vendors have not productised the reconciliation layer.

**Why they buy without being sold to:** An OM who spent Sunday fixing a hygienist underpay uploads last month's OD export, sees the same total with three flagged lab mismatches, and refuses to go back to Excel.

**Revenue model:** $149 / $249 / $399 per practice. 30-day trial. CPA referral 15%.

**Unfair advantage:** US OD/Dentrix rule templates + anomaly library; study-club distribution; PE roll-ups won't chase at $149.

### Solo Build Plan
1. Weeks 1–3: OD Provider Payroll CSV ingest; rule builder; pay summary PDF.
2. Weeks 4–5: Anomaly flags; vs last period; Gusto CSV export.
3. Weeks 6–7: Dentrix path; multi-provider approval.
4. Weeks 8–9: Stripe; sample-file onboarding.
5. Weeks 10–12: Pilot 8 practices via dental groups / OD user groups.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-08-16
**Strongest part:** Samera’s own FAQ still lists Dentally/SoE — the US export→Excel path is intact.
**Open question:** Will practices trust a solo tool with paycheck math without a CPA partnership from day one?

---

---

## #2 — AdvisorAlert  ·  74/100  ·  UNCHANGED
First added: 2026-07-31 | Last updated: 2026-08-16 | Score delta this week: —

> Catch compliance gaps before the SEC exam does — continuous monitoring built for independent RIAs, not mega-firms.

### Score Breakdown
- Solo Buildability:   12/20  (email scanning in a regulated context; SEC API access; false-positive management; harder than a typical SaaS build but a determined solo founder with legal knowledge can ship a 5-check MVP)
- Value Clarity:       17/20  (SEC deficiency letter = immediate pain trigger; CCO who received one understands the product in 10 seconds)
- Market Timing:       16/20  (unchanged — Hadrius still custom-quote only; no public starter tier under $5K)
- B2B Monetisation:    17/20  ($299–799/month vs $5K–20K/year compliance consultant; RIAs are trained to pay for compliance; exceptional value ratio)
- Pull Factor:         12/20  (RIA compliance community is tight; word-of-mouth travels through custodian networks and compliance study groups; not publicly viral)

**Strengths:**
- Hadrius $27M raise (July 2026, CRV + YC) validates the RIA compliance automation category unambiguously.
- Micro-RIA beachhead ($50M–$500M AUM, 1–5 employees) is explicitly underserved — Hadrius starts at ~$12K/year and targets 500+ employee firms.
- RIAs already pay $5K–$20K/year for compliance consultants; $3,600/year for automated monitoring is an easy value comparison.

**Risks:**
- Regulated space creates legal positioning risk — the product must be sold as a "monitoring tool," not "compliance advice," to avoid investment adviser registration requirements.
- Hadrius could announce a micro-RIA "starter tier" using some of their $27M, directly competing on price.
- False positives in email flagging (flagging a normal client email as a compliance violation) erode trust in a regulated, high-stakes environment.

**Verdict:** Keep micro-RIA beachhead. Open question from R5 still unanswered.

### The Pitch
**Problem:** Independent registered investment advisors with $50M–$500M AUM typically have 1–5 employees, no dedicated CCO, and rely on an annual compliance consultant for $5,000–$20,000/year. Meanwhile the SEC expects continuous monitoring: reviewing client communications for solicitation violations, sampling marketing content, confirming trades match investment policy statements, maintaining a current compliance calendar. Hadrius's $27M raise in July 2026 validated the category — but Hadrius targets firms with hundreds of employees and starts at ~$12K/year. The 1–5 person RIA shop generates 85% of deficiencies on SEC exams and has no purpose-built affordable tool.

**Solution:** AdvisorAlert connects to your Gmail or Outlook, samples 50 client communications per month, and flags language that could constitute testimonials, solicitations, or performance guarantees. It also maintains your compliance calendar (Form ADV due dates, custody rule filings, code of ethics deadlines) and lets you submit marketing content for a plain-English compliance check. The weekly digest is your CCO's to-do list — not a 200-page manual.

**Target customer:** Principal / de-facto CCO at a 1–5 person RIA, $50M–$500M AUM, serving retail or HNW clients on Schwab, Fidelity, or Pershing. Not a broker-dealer, not a family office. Buyer: the principal who is also the CCO. Users: principal + any administrative staff who handle client communication.

**Why now:** AI communication volume is widening the compliance review gap faster than RIA headcount grows. Hadrius's $27M July 2026 raise — the largest compliance-tech seed in recent memory — confirms VC conviction in the category. The SEC's 2026 risk alert cited inadequate communication surveillance as the top deficiency in small RIAs. No affordable tool exists for micro-RIA shops below $5K/year.

**Why they buy without being sold to:** An RIA principal who received an SEC deficiency letter for "inadequate email review" last year starts a free AdvisorAlert trial, connects their inbox, and sees their first flagged communication — a client email that said "you always get me great returns" — within 5 minutes. No pitch required.

**Revenue model:** $299/month (email sampling for 1 inbox, compliance calendar, 12 framework checks). $499/month (3 inboxes + marketing content review PDF upload). $799/month (unlimited + trade surveillance from Schwab/Fidelity custodian data feeds). Annual −2 months. Free compliance calendar (no email connection required) as lead generation entry point.

**Unfair advantage:** Micro-RIA compliance calendar templates (Form ADV filing dates, custody rule requirements, code of ethics cycles) built specifically for the 1–5 person shop that Hadrius ignores. Distribution through Schwab Advisor Services and Fidelity Institutional partner programs where 90%+ of micro-RIAs can be reached without outbound sales.

### Solo Build Plan
1. Weeks 1–2: Free compliance calendar (ADV, custody, code of ethics deadlines) — ship as a stand-alone lead magnet with no email connection.
2. Weeks 3–4: Gmail/Outlook OAuth; email ingestion; AI flag for testimonials, performance guarantees, solicitation language with explainability ("flagged because: 'always' + 'returns' in same sentence").
3. Weeks 5–6: Compliance calendar integration with email alerts; marketing content review (PDF/LinkedIn post upload; plain-English flag report).
4. Weeks 7–8: Stripe; free-calendar → paid-monitoring conversion funnel; legal review of ToS positioning ("monitoring tool, not compliance advice").
5. Weeks 9–12: Pilot 5 micro-RIAs through Schwab advisor network referrals and IAA or NAPFA regional events.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** Hadrius $27M July 2026 is the clearest single category-validation signal in this cookbook. The micro-RIA segment gap is explicitly documented.
**Open question:** Hadrius starter tier under $5K/year?

---

---

## #3 — MarkPack  ·  73/100  ·  IMPROVED
First added: 2026-08-03 | Last updated: 2026-08-16 | Score delta this week: +2

> Ship Article 50 evidence — chatbot disclosure, C2PA marks, and an audit folder — before the inspector asks.

### Score Breakdown
- Solo Buildability:   14/20  (C2PA middleware + disclosure snippets + evidence ZIP; not a full GRC suite)
- Value Clarity:       16/20  (+1 — AI Office complaint form is live; “show me proof” is no longer hypothetical)
- Market Timing:       17/20  (+1 — Art. 50 enforcement started 2 Aug; Dec 2 marking grace ~3.5 months left; OpenCorpo/PixelOffice are checklists/forges, not evidence+CI packs)
- B2B Monetisation:    14/20  ($199–499/mo for genAI product teams shipping EU-facing content)
- Pull Factor:         12/20  (compliance buyers; eng Twitter/GitHub for SDK)

**Strengths:**
- Post-deadline enforcement window differs from pre-deadline checklist panic (ArticleShield’s failure mode).
- Dec 2 grace creates a concrete ~4-month build/ship window for marking on systems already in market.
- Obligation→artifact mapping + CI fail-on-missing-marks is a solo-shaped wedge vs consulting slideware.

**Risks:**
- Platform-native C2PA (Adobe, model providers) could commoditize marking.
- AnnexOps/ActProof-class tools may expand into evidence packs.
- Demand may cliff after Dec 2 grace if enforcement is weak.

**Verdict:** Stay on engineering evidence pack + CI — not another PDF checklist. Grace window is the sprint.

### The Pitch
**Problem:** From 2 August 2026, EU AI Act Article 50 transparency duties apply. Chatbots must disclose AI interaction; generative systems need machine-readable marking (C2PA-class) — with a grace period to 2 December 2026 for systems already on the market before 2 August (EC FAQ / Omnibus). Mid-market product teams have Notion checklists, not an evidence folder an auditor can open: disclosure screenshots, marking pipeline config, role owners, and change logs.

**Solution:** MarkPack is the technical compliance kit: drop-in disclosure components, C2PA/content-credential marking in the generation path, and a one-click evidence pack (ZIP/PDF) mapping each Art. 50 obligation to proof. Built for eng + legal together — not consultants selling slideware.

**Target customer:** Eng lead + counsel at 15–150 person companies shipping EU-facing chatbots or generative content (SaaS, media, agencies). Buyer: CTO/GC. Users: eng implementing marks + compliance owning the evidence folder.

**Why now:** Obligations are live as of 2 August 2026; high-risk Annex III was deferred in parts of the Omnibus, but Art. 50 was not. The Dec 2 marking grace is a forcing function for teams who shipped before August without watermarks.

**Why they buy without being sold to:** Counsel asks “show me Art. 50 proof” and eng has nothing reproducible — MarkPack’s evidence pack becomes the answer in one afternoon.

**Revenue model:** $199/mo (1 product). $349/mo (5 products + CI check). $499/mo (SSO + custom retention). Annual −2 months. 14-day trial with a sample evidence pack generated from a demo app.

**Unfair advantage:** Obligation→artifact mapping that updates as Commission guidance evolves; GitHub Action that fails PRs missing marks; focused on mid-market eng teams, not Big Four audit packages.

### Solo Build Plan
1. Weeks 1–3: Disclosure component library; evidence schema; sample pack generator.
2. Weeks 4–5: C2PA/content credentials hook for image/video pipeline (one stack first).
3. Weeks 6–7: CI Action; Slack “evidence incomplete” alert.
4. Weeks 8–9: Stripe; EU-facing SaaS onboarding.
5. Weeks 10–12: Pilot 6 teams via AI Act Slack/Discord + YC EU companies.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** Enforcement and the public complaint channel make evidence a real ask, not a pre-deadline panic.
**Open question:** Will buyers pay after Dec 2, or only during the remaining grace sprint?

---

## #4 — RuleFlow  ·  73/100  ·  NEW
First added: 2026-08-16 | Last updated: 2026-08-16 | Score delta this week: —

> New federal rules become a checklist and an evidence folder — not another unread PDF in Slack.

### Score Breakdown
- Solo Buildability:   13/20  (FRTracker-class obligation feed + Asana/Jira tasks + evidence ZIP; legal-correctness review is the hard part)
- Value Clarity:       16/20  (“this rule changed — here is what you must do by when” is a 15-second pitch for a CCO)
- Market Timing:       16/20  (YC Fall 2026 RFS asked for AI-native compliance infrastructure on 23 Jul; FRTracker is a free research primitive with no mid-market workflow layer; CUBE/AscentAI remain Tier-1)
- B2B Monetisation:    17/20  (community banks and fintech lenders already pay six figures in fines and consultants; $399–799/mo is cheap next to that)
- Pull Factor:         11/20  (compliance communities share tools quietly; not LinkedIn-viral)

**Strengths:**
- FRTracker already extracts must/shall/may-not obligations deterministically — the missing product is “new rule → owner → due date → evidence,” not another AI summariser.
- YC’s July 2026 request validates the category; incumbents sell libraries, not a 4-person compliance team’s inbox.
- Traceable, non-black-box extraction is a selling point for auditors.

**Risks:**
- FRTracker (or a well-funded RegTech) adds the workflow layer and collapses the wedge.
- Wrong obligation mapping creates legal liability; product must be “monitoring,” not advice.
- Mid-market fintech buyer count is smaller than it looks.

**Verdict:** Enter as the workflow layer on top of public obligation feeds. One vertical first: US fintech lenders / community banks.

### The Pitch
**Problem:** A four-person compliance team at a community bank or fintech lender tracks Federal Register changes in a shared spreadsheet and a Slack channel of PDFs. CUBE and AscentAI sell this to Tier-1 banks. FRTracker (free) now extracts individual must/shall obligations from 989K+ documents — but it is a research tool, not a system of record. When a final rule drops, nobody owns the checklist, and the exam asks for evidence that does not exist.

**Solution:** RuleFlow turns each relevant obligation into a task with an owner, a due date, and an evidence slot. It watches the agencies you care about, diffs proposed vs final, and opens Asana/Jira items mapped to the source passage. At exam time you export a folder: rule, obligation, who did what, attached proof.

**Target customer:** CCO / compliance analyst at a 20–200 person US fintech lender, community bank, or payments firm. Not a broker-dealer mega-firm. Buyer: CCO or General Counsel. Users: the 2–6 people who currently paste Federal Register links into Slack.

**Why now:** YC’s Fall 2026 RFS (23 Jul) asked for AI-native compliance infrastructure that maps activities to rules, filings, and evidence. The open primitive (FRTracker) exists; the mid-market workflow layer does not. Enterprise RegTech still starts at six figures.

**Why they buy without being sold to:** After a consent order or a nasty FR notice, the CCO pastes last month’s “rules we think apply” spreadsheet into RuleFlow, sees three missed effective dates, and refuses to go back to Slack-PDFs.

**Revenue model:** $399/mo (1 agency family + 10 users). $599/mo (3 families + Jira/Asana sync). $799/mo (unlimited + evidence vault + SSO). Annual −2 months. 14-day trial on a saved agency watchlist.

**Unfair advantage:** Obligation→task→evidence mapping for one vertical (US depository / fintech lending) with citations back to primary text — not a 200-jurisdiction library.

### Solo Build Plan
1. Weeks 1–3: Ingest FRTracker API or daily FR deltas; agency watchlist; obligation cards with source quotes.
2. Weeks 4–5: Task export to Asana/Jira; owner + due date; proposed-vs-final diff view.
3. Weeks 6–7: Evidence upload per obligation; exam-pack ZIP/PDF.
4. Weeks 8–9: Stripe; fintech-lending template (lending, BSA/AML notices, CFPB).
5. Weeks 10–12: Pilot 5 CCOs via ABA/community-bank ops groups and fintech compliance Slack.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** The primitive is free and public; the unpaid job is workflow + evidence, which is exactly what a 4-person team will pay for.
**Open question:** Will FRTracker itself add “send to Jira” and eat the wedge?

---

## #5 — ChurnDetect  ·  73/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-08-16 | Score delta this week: −2

> Find the customers about to leave — 90 days before they tell you — from the support tickets they are already sending.

### Score Breakdown
- Solo Buildability:   15/20  (Zendesk/Intercom API + AI ticket classification + Slack alerts = 3 months feasible for a focused MVP)
- Value Clarity:       17/20  ("retrospective demo on your last churned account" is self-closing; no pitch required after that demo)
- Market Timing:       13/20  (−1 — Zendesk Intelligent Triage rolled to Professional plans 1 Jul 2026; still topic/sentiment per ticket, not account-level churn)
- B2B Monetisation:    15/20  ($199–599/month; CS budget exists; protecting $30K ARR easily justifies $349/month)
- Pull Factor:         13/20  (−1 — CS AI category noise; retrospective demo still the wedge)

**Strengths:**
- Retrospective demo ("see the 8 tickets before your last churned account") is a self-closing sales mechanism that requires no pitch.
- 60% of B2B software buyers regretted their purchase in 18 months (Helply 2026); churn risk is surfaced in tickets months before renewal.
- Gap between enterprise (Gainsight $30K+, ChurnZero $20K+) and nothing for 10–150 seat SaaS is clear and large.

**Risks:**
- Zendesk's native "Intelligent Triage" already classifies intent and sentiment; if it expands to churn prediction, the differentiation narrows.
- PII/SOC2 considerations for storing and scanning customer support data require explicit consent flows.
- Planhat ($1K+/month, mid-market) could push further downmarket.

**Verdict:** Hold retrospective-demo wedge. Open question from R5 answered: triage is not account health — yet.

### The Pitch
**Problem:** B2B SaaS companies discover customer churn risk almost exclusively at renewal time, when the decision is already made. 60% of B2B buyers regretted their purchase in the past 18 months. The warning signals — frustration in tickets, repeated unresolved issues, competitor mentions, escalating response times — are buried in the support inbox. CS teams classify tickets by "resolved / open," not by "churn risk." A $50K ARR customer silently decides to cancel three months before renewal; the first official indication is a "not renewing" email.

**Solution:** ChurnDetect connects to your Zendesk or Intercom, reads the past 6 months of support tickets using AI, and classifies each conversation by churn risk language, unresolved issue patterns, feature gaps, and competitive mentions. It generates a weekly list of "accounts at risk" with the specific threads that triggered the flag. CS teams get a prioritised outreach list before accounts are lost — not after.

**Target customer:** Customer success manager / VP CS at 10–150 person B2B SaaS company with 100+ customers. Buyer: VP CS or CRO. Users: CS team + account managers. Uses Zendesk or Intercom. Does not have Gainsight or ChurnZero. Company runs $1M–15M ARR where individual account loss is felt immediately.

**Why now:** LLMs in 2026 classify "this is taking way too long to resolve" as churn risk where keyword filters miss it. The cost of this classification is now under $0.001 per ticket. Enterprise CS platforms are priced at $20–30K/year, leaving 10–150 person SaaS with no dedicated churn-detection layer.

**Why they buy without being sold to:** A CS manager who lost a $30K account to silent churn runs the free ChurnDetect retrospective on that account's last 8 tickets, sees the risk flags she missed 90 days ago, and purchases immediately. The demo is a historical audit — not a hypothetical.

**Revenue model:** $199/month (up to 500 accounts + Zendesk). $349/month (unlimited accounts + Intercom/Zendesk + Slack alerts). $599/month (unlimited + API + custom risk taxonomy + competitor-mention tracking). 14-day free trial. Annual −2 months.

**Unfair advantage:** Historical retrospective demo that turns the free trial into a self-closing pitch. Vertical risk taxonomies (SaaS-specific, agency-specific, subscription product) that generic sentiment tools do not have.

### Solo Build Plan
1. Weeks 1–3: Zendesk API connector; 6-month historical ticket ingestion; AI risk classification per thread (churn language, sentiment, competitor mentions).
2. Weeks 4–5: Account-level aggregation; weekly digest email + Slack; risk score per account with evidence thread links.
3. Weeks 6–7: Intercom connector; custom risk terms; "at risk" list with flagged quotes.
4. Weeks 8–9: Stripe; retrospective demo generator (5 historical accounts, auto-classified); explicit data consent flow.
5. Weeks 10–12: Pilot 8 SaaS companies through CS leader Slack communities and Product Hunt launch.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** The retrospective demo on a recently churned account is a self-closing conversion mechanism unlike anything in the cookbook.
**Open question:** Will Zendesk turn topic+sentiment into an account-health SKU in H2 2026?

---

---

## #6 — TokenBill  ·  72/100  ·  NEW
First added: 2026-08-16 | Last updated: 2026-08-16 | Score delta this week: —

> One invoice-level forecast for OpenAI, Claude, and Cursor — before token shock hits the P&L.

### Score Breakdown
- Solo Buildability:   16/20  (email/PDF invoice ingest + vendor price tables + cap alerts; no SDK in the customer’s app)
- Value Clarity:       16/20  (Techaisle 2026 “token shock” is a CFO sentence; “what will AI cost next month?” is obvious)
- Market Timing:       13/20  (pain is #1 SMB IT challenge in 2026; Helicone/Langfuse/vendor consoles exist but are engineer-facing and per-provider)
- B2B Monetisation:    15/20  ($149–399/mo vs surprise $8K OpenAI bills; finance will pay for forecastability)
- Pull Factor:         12/20  (CFO Slack/communities share war stories; quieter than eng Twitter)

**Strengths:**
- Techaisle 2026 names unpredictable AI consumption as the budget-constraint evolution of cloud-cost panic.
- Wedge is finance, not observability: invoices and card statements, not traces.
- Helicone ($79, proxy) and Langfuse ($29, SDK) do not serve a non-engineer ops/finance buyer.

**Risks:**
- OpenAI / Anthropic / Cursor admin consoles get “CFO forecast” tabs.
- Ramp, Brex, or Mercury add AI-vendor spend categories.
- Invoice formats are messy; accuracy below ~90% kills trust.

**Verdict:** Enter as the invoice-level AI spend forecast for 20–100 person companies. Do not build another Langfuse.

### The Pitch
**Problem:** SMBs in 2026 run OpenAI, Anthropic, Cursor, and a handful of other AI tools on usage pricing. Techaisle’s 2026 SMB IT survey put budget unpredictability — “token shock” — at the top of the challenge list, ahead of classic cloud optimisation. The engineer can open Helicone. The ops lead and the bookkeeper get PDF invoices they cannot forecast, cannot allocate to teams, and cannot cap.

**Solution:** TokenBill ingests invoices and billing emails from the AI tools you already pay, maps them to a single forecast, and alerts Slack when a vendor is running hot vs last month. No SDK. No proxy in the product. Caps are “tell finance,” not “return 402 to the model.”

**Target customer:** Ops lead / controller / founder at a 20–100 person B2B company spending $1K–$20K/month across 3+ AI vendors. Buyer: founder or finance. User: the person who currently forwards OpenAI invoices into a sheet.

**Why now:** Usage-based AI billing went from experiment to line item in 2026. Observability tools solved this for engineers. Finance still has PDFs.

**Why they buy without being sold to:** After one $4,000 Cursor+OpenAI month that nobody budgeted, the controller forwards last quarter’s invoices into TokenBill, sees the run-rate, and sets a Slack alert the same afternoon.

**Revenue model:** $149/mo (3 vendors, email forward). $249/mo (10 vendors + team allocation). $399/mo (SSO + CSV to QBO). Annual −2 months. 14-day trial.

**Unfair advantage:** Vendor invoice parsers + finance-shaped alerts. Distribution via bookkeeper / fractional-CFO communities, not AI engineer Twitter.

### Solo Build Plan
1. Weeks 1–3: Email-forward ingest for OpenAI, Anthropic, Cursor PDFs; vendor normaliser; monthly total view.
2. Weeks 4–5: Run-rate forecast; vs last month; Slack threshold alerts.
3. Weeks 6–7: Team/cost-centre tags; CSV export.
4. Weeks 8–9: Stripe; sample-invoice onboarding.
5. Weeks 10–12: Pilot 8 companies via fractional-CFO Slack and indie-hacker ops channels.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** Buyer is finance, which Helicone/Langfuse ignore; the pain is named in a 2026 analyst list.
**Open question:** Will Ramp/Brex or the model vendors ship a good-enough spend forecast first?

---

## #7 — BriefDesk  ·  72/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-08-16 | Score delta this week: −4

> Your Monday morning leadership brief writes itself — pulled from your real CRM, PM, and billing data, not from memory.

### Score Breakdown
- Solo Buildability:   17/20  (3 OAuth integrations + AI synthesis < $0.02/brief; clearly shippable solo in 3 months)
- Value Clarity:       17/20  (CSW Solutions July 2026 documents exact pain: "4-5 hours every Friday"; self-evident ROI)
- Market Timing:       12/20  (−2 — briefhq.ai now ships HubSpot+Stripe+Linear plus scheduled Weekly Brief agents; Data Parrot sends HubSpot weekly sales briefs; HubSpot Breeze Studio builds weekly CRM recaps)
- B2B Monetisation:    15/20  ($149–399/month; professional services teams have clear budget for time-back tools)
- Pull Factor:         12/20  (−1 — “weekly brief” is now a crowded phrase; rename is no longer optional)

**Strengths:**
- CSW Solutions (July 2026) documents the exact ritual: CRM tab → PM tab → billing tab → paste into Notion doc on Friday afternoon. Product builds itself around a lived pain.
- Multi-stack angle (HubSpot+ClickUp+QBO) is what HubSpot Breeze, Monday AI, and Notion AI individually cannot do — each only sees one platform's data.
- AI synthesis cost is < $0.02 per brief; margin structure is exceptional.

**Risks:**
- HubSpot could ship a "weekly AI narrative summary" that ingests its 1,400+ connected integrations natively — watch Q3/Q4 2026 announcements.
- 3 OAuth integrations (HubSpot, ClickUp, QuickBooks) = 3 weeks of auth and rate-limit work before any AI prompt engineering.
- "Narrative brief" vs dashboard is a positioning risk — some ops leads have accepted dashboards and don't feel the brief pain.

**Verdict:** Keep only if positioned as HubSpot+ClickUp+QBO ops brief — and rename before launch. One more run.

### The Pitch
**Problem:** Professional services firms, agencies, and B2B SaaS companies spend 4–5 hours every Friday manually pulling CRM deal updates, project status from their PM tool, and revenue figures from QuickBooks into a leadership brief. One person — usually the ops manager, EA, or founder — reads from three browser tabs and types into a Notion document. The brief costs $200–500 in staff time to produce, arrives late, and is stale by Monday morning. CSW Solutions documented this workflow in July 2026: "someone would export from system A, copy into the report, go to system B, copy into the report — then hope the math is right."

**Solution:** BriefDesk connects to your HubSpot (or Pipedrive), ClickUp (or Asana/Linear), and QuickBooks (or Xero/Stripe) via API and runs automatically every Friday at 4pm. It pulls key metrics — pipeline movement, project status by owner, revenue vs. target — and synthesises them into a readable narrative brief: what closed this week, what is at risk, what needs leadership attention. The brief arrives in Slack or email before 5pm. Reviewers annotate before it goes to leadership; the AI does the research, the human adds context.

**Target customer:** Operations lead / EA / founder at a 10–100 person professional services firm, agency, or B2B SaaS company using HubSpot or Pipedrive + ClickUp or Asana + QuickBooks or Xero. Buyer: founder/COO. User: ops lead or EA who currently builds the brief manually.

**Why now:** AI synthesis costs less than $0.02 per brief. HubSpot, ClickUp, and QuickBooks all publish REST APIs that support weekly automated pulls without screen-scraping. BigIdeasDB 2026 validates manual reporting as the #1 business pain at 33.3% validation rate across 148K+ complaints. CSW Solutions documented in July 2026 that SMBs are actively paying in staff hours for exactly this workflow.

**Why they buy without being sold to:** An ops manager who spent Friday afternoon copy-pasting into a leadership report gets a BriefDesk free trial, connects their HubSpot stack, and receives the same brief automatically at 5pm. They do not buy BriefDesk — they just stop cancelling it after the trial.

**Revenue model:** $149/month (1 stack: 1 CRM + 1 PM + 1 billing source; 1 brief/week). $249/month (2 stacks; for agencies managing internal + client reporting). $399/month (custom templates + Slack delivery + API access). Annual discount: 2 months free. 14-day trial with 2 live briefs generated from real data.

**Unfair advantage:** First-mover in "narrative brief vs dashboard" for multi-stack companies. Vertical templates for agencies, SaaS, and professional services that any platform's native AI cannot match across stacks. Distribution via HubSpot Partner ecosystem and ClickUp Integrations Marketplace.

### Solo Build Plan
1. Weeks 1–2: HubSpot + ClickUp + QuickBooks OAuth; scheduled weekly metric pull; error handling and rate limits.
2. Weeks 3–4: AI narrative synthesis (GPT-4o or Claude); Slack + email delivery; brief template builder.
3. Weeks 5–6: Review/annotate workflow before distribution; stale-data warnings; week-over-week comparison.
4. Weeks 7–8: Stripe; 14-day trial with 2 live briefs; onboarding wizard with vertical template selection.
5. Weeks 9–12: Pilot 8 agencies and PS firms through HubSpot Partner community + ClickUp Marketplace.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-08-16
**Strongest part:** The CSW Friday ritual is still real; the empty category is not.
**Open question:** Is there any multi-stack (CRM+PM+billing) narrative brief that Brief.ai/Data Parrot still cannot do?

---

---

## #8 — AuthTrack  ·  70/100  ·  NEW
First added: 2026-08-16 | Last updated: 2026-08-16 | Score delta this week: —

> See which prior auths are inside the 7-day / 72-hour clock — and which denials still have no specific reason.

### Score Breakdown
- Solo Buildability:   14/20  (CSV/fax log + calendar clocks + denial-reason fields; no EHR writeback in v1; HIPAA still applies)
- Value Clarity:       16/20  (“this PA blows the CMS clock on Thursday” is obvious to a biller)
- Market Timing:       14/20  (CMS-0057-F clocks and specific-denial rules live since 1 Jan 2026; FHIR PA APIs due 1 Jan 2027; Linear Health automates Athena specialty groups, not 2–10 provider fax shops)
- B2B Monetisation:    14/20  ($149–299/mo for a billing coordinator’s time; one avoided write-off pays for a year)
- Pull Factor:         12/20  (biller Facebook groups; not public-viral)

**Strengths:**
- Operational CMS clocks are already binding; 2027 MIPS “at least one electronic PA” creates a documentation ramp.
- Linear Health, Waystar, CoverMyMeds, Availity serve mid-market / specialty / pharmacy — the 2–10 provider Excel tracker is still the workflow.
- Spreadsheet-first avoids the 4-week EHR integration that kills solo scope.

**Risks:**
- HIPAA + PHI handling from day one.
- Linear Health or clearinghouses ship a cheap tracker SKU.
- Tiny practices may not pay $149 if they believe “the payer has to comply, not us.”

**Verdict:** Enter as a clock + denial-reason log for small practices still on Excel/fax. Do not build portal automation in v1.

### The Pitch
**Problem:** Since 1 January 2026, Medicare Advantage, Medicaid, CHIP, and FFE QHP payers must decide standard prior auths in 7 calendar days and urgent ones in 72 hours, and every denial must include a specific reason. Billing coordinators at 2–10 provider practices still track this in a spreadsheet next to the fax machine. They miss clocks, they cannot prove a vague denial, and they will need a clean log before 2027 electronic-PA attestation.

**Solution:** AuthTrack is the PA status board: each request gets a clock, a channel (fax/portal/phone), a denial-reason field, and a reminder before the CMS window closes. v1 is CSV import + form entry — not an Athena integration, not a FHIR client.

**Target customer:** Billing coordinator / office manager at a 2–10 provider US practice (PT, specialty lite, independent primary care) that is not on Athena+Linear Health. Buyer: office manager. User: the biller who owns the Excel PA tab.

**Why now:** The clocks are live, not upcoming. The FHIR API mandate is 1 Jan 2027. Practices that do not have a log now will invent one badly six months before MIPS.

**Why they buy without being sold to:** After a denied MRI with no specific reason and a missed 7-day follow-up, the biller pastes the spreadsheet into AuthTrack, sees two clocks already red, and stops using Excel that week.

**Revenue model:** $149/mo (1 location, 200 PAs). $249/mo (3 locations + reminder SMS). $299/mo (export pack for appeals). Annual −2 months. 14-day trial with sample CSV.

**Unfair advantage:** CMS-clock templates + denial-reason required field sized for fax-era shops that enterprise PA platforms ignore.

### Solo Build Plan
1. Weeks 1–3: PA log (CSV import); 7-day / 72-hour clocks; denial-reason required on deny.
2. Weeks 4–5: Email/SMS reminders; aging report; appeal packet PDF.
3. Weeks 6–7: HIPAA BAA flow; audit log; role-based access.
4. Weeks 8–9: Stripe; sample-CSV onboarding.
5. Weeks 10–12: Pilot 6 small practices via biller Facebook groups and local MGMA chapters.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** Regulation is already in force; the buyer is a person with a spreadsheet, not a health-system IT committee.
**Open question:** Will tiny practices pay, or will they wait for their clearinghouse to add a free clock?

---

## #9 — BreakWatch  ·  67/100  ·  NEW
First added: 2026-08-16 | Last updated: 2026-08-16 | Score delta this week: —

> Know which of your vendors shipped a breaking API change before production does.

### Score Breakdown
- Solo Buildability:   15/20  (changelog crawlers + OpenAPI diff + Slack; contract tests later)
- Value Clarity:       14/20  (needs a sentence of setup; “41% of breaking changes are unannounced” lands with eng leads)
- Market Timing:       11/20  (Specway 2026: 68% of integrations take 3× estimate, 2.3 breaking changes/year; Optic/Speakeasy/Bump.sh exist — wedge is consumer-side watch, not producer docs)
- B2B Monetisation:    14/20  ($149–399/mo for a 5–30 person SaaS that maintains 8+ customer-facing integrations)
- Pull Factor:         13/20  (eng Twitter after an outage; incident posts travel)

**Strengths:**
- Specway’s 2026 integration report names the exact failure: undocumented breaking changes, OAuth overhead, silent 200s.
- Producer tools (Bump, Speakeasy) help API vendors; consumers of HubSpot/Stripe/Shopify still find out in prod.
- Incident-shaped onboarding: “paste the APIs that paged you last quarter.”

**Risks:**
- Status pages + vendor changelogs + Optic watchers already “good enough.”
- Unified API vendors (Merge, Apideck) absorb monitoring.
- Changelog formats are inconsistent; false positives fatigue the channel.

**Verdict:** Enter as consumer-side breaking-change inbox for small SaaS integration teams. Last seat — kill if Optic ships a cheap “watch these 10 vendor APIs” SKU.

### The Pitch
**Problem:** Specway’s 2026 API Integration Complexity Report: 68% of integrations take 3.2× the estimate; the average API ships 2.3 breaking changes a year; 41% of those ship with no prior notice. A 15-person SaaS maintaining HubSpot, Stripe, QuickBooks, and Shopify integrations finds out when customers file tickets. Producer-side doc tools do not watch the APIs you consume.

**Solution:** BreakWatch watches the vendor APIs you depend on — changelogs, OpenAPI diffs, status pages — and opens a Slack item when a field disappears or an auth flow changes. You subscribe to endpoints, not to a new iPaaS.

**Target customer:** Eng lead / founding engineer at a 5–30 person SaaS with 5–15 outbound integrations. Buyer: CTO. Users: the two engineers on integration on-call.

**Why now:** AI agents made stale field mappings a liability, not just a dashboard bug (Ampersand 2026). Integration debt is now an on-call problem.

**Why they buy without being sold to:** After a silent HubSpot field rename corrupts a week of deals, the eng lead adds HubSpot to BreakWatch and requires a Slack ping before the next change hits prod.

**Revenue model:** $149/mo (10 watched APIs). $249/mo (30 APIs + OpenAPI diff). $399/mo (contract-test hooks). Annual −2 months. 14-day trial.

**Unfair advantage:** Consumer-side watchlist of the 20 APIs SMB SaaS actually breaks on — not a general API catalog.

### Solo Build Plan
1. Weeks 1–3: Changelog + OpenAPI watchers for Stripe, HubSpot, Shopify, QBO; Slack alerts.
2. Weeks 4–5: Diff UI (removed fields, auth changes); mute/noise controls.
3. Weeks 6–7: GitHub Action that comments on PRs when a watched spec moved.
4. Weeks 8–9: Stripe; “paste last incident” onboarding.
5. Weeks 10–12: Pilot 6 SaaS teams via r/SaaS and integration-engineer Slack.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-08-16
**Strongest part:** Specway quantified the pain this year; producer tools do not cover the consumer.
**Open question:** Does Optic or Speakeasy already sell “watch vendor APIs you don’t own”?

---

## #10 — FlowTrace  ·  62/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-08-16 | Score delta this week: −5

> One dashboard to see what all your AI agents are doing — and stop a runaway task before it costs real money.

### Score Breakdown
- Solo Buildability:   11/20  (multi-framework log ingestion with different APIs per platform; hard but achievable if scoped to OpenAI + Claude + Zapier only for v1)
- Value Clarity:       13/20  (−1 — “agent governance” now means AUP PDFs at $99/mo; spend kill-switch needs extra explanation)
- Market Timing:       11/20  (−3 — SanctumShield $99/mo owns mid-market Agent Governance messaging; Helicone/Langfuse cover spend dashboards; runtime pause across OpenAI+Claude+Zapier still thin)
- B2B Monetisation:    14/20  ($149–599/month; AI-native companies have tooling budgets; runaway-agent prevention has direct cost-avoidance ROI)
- Pull Factor:         12/20  (−2 — category noise; must stay ruthlessly on runaway spend pause)

**Strengths:**
- 27% of enterprises have no real-time way to stop a runaway agent (VentureBeat 2026). Notable Capital (VC, July 2026) explicitly calls the coordination layer the "missing infrastructure."
- Cross-platform log ingestion (OpenAI + Claude + Zapier) that no platform's native dashboard has — each only sees its own agents.
- "What just happened?" retrospective after an incident is a more honest entry point than proactive governance pitches.

**Risks:**
- Solo buildability is genuinely hard: each platform has different log formats, APIs, and rate limits. Copilot logs are nearly inaccessible programmatically.
- Anthropic or OpenAI could ship native cross-agent orchestration with shared audit logs, removing the need for an external layer.
- The market of "15–100 person AI-native companies running 3+ agents simultaneously" may be smaller than it appears in 2026.

**Verdict:** Last seat. Runtime spend kill-switch only — or remove next run.

### The Pitch
**Problem:** Fast-growing companies in 2026 run AI agents from multiple platforms simultaneously — a Copilot agent in Teams, a Zendesk bot, a Claude-based GitHub code reviewer, a Zapier lead-routing agent. These agents operate in silos with no shared log, no shared spend view, and no human escalation path. When something goes wrong — a runaway agent makes $500 in unexpected API calls, a bot auto-replies to 50 customers with wrong product information — no one can reconstruct the timeline. 27% of enterprises have no real-time way to stop a runaway agent before the bill arrives (VentureBeat / Camunda 2026 State of Agentic Orchestration report).

**Solution:** FlowTrace is a lightweight coordination panel that sits above your existing AI tools. It reads agent activity logs via API and webhook, maintains a shared timeline of agent decisions and actions, surfaces decisions that need human review, and lets you set spending and action limits across all agents. When an agent hits a limit or makes a flagged decision, FlowTrace pauses it and pings the right human in Slack. It is not a new agent platform — it is the control layer for the agents you already have.

**Target customer:** Engineering lead / ops manager at a 15–100 person AI-native or AI-forward company running 3–10 AI agents from multiple platforms. Buyer: eng lead or COO. Users: engineering team + operations. Company does not yet have a dedicated AI governance function. Runs OpenAI, Claude, or Zapier agents in production — not Microsoft enterprise stack.

**Why now:** Agent sprawl is a brand-new 2026 organisational problem that emerged as every major SaaS platform shipped its own agent. Notable Capital published research in July 2026 identifying the "coordination layer" as the critical missing infrastructure for the agentic era. The problem is real, but SanctumShield ($99/mo AUP + risk report) and Helicone/Langfuse (spend dashboards) filled the adjacent shelves. The remaining hole is a hard pause across OpenAI+Claude+Zapier — not another policy PDF.

**Why they buy without being sold to:** After an AI agent makes an unintended API call costing $500, or auto-replies to a customer thread with incorrect information, the engineering lead sets up FlowTrace that afternoon so it can never happen again without human approval.

**Revenue model:** $149/month (3 agent connections, 30-day log, spend alerts). $299/month (10 agent connections, 90-day log, hard spend limits, Slack escalation). $599/month (unlimited + approval workflows + custom action-type blocklist). 14-day trial.

**Unfair advantage:** Cross-platform log ingestion (OpenAI + Claude + Zapier) that platform-native dashboards cannot replicate across stacks. The "incident retrospective" onboarding flow turns the trial into a self-closing pitch for any team that has already experienced a runaway agent.

### Solo Build Plan
1. Weeks 1–3: OpenAI usage API + Claude API log ingestion; Zapier webhook receiver; shared agent activity timeline view.
2. Weeks 4–5: Spend tracking (OpenAI usage API, Claude usage API); runaway-agent detection (spend spike, action-count spike); Slack escalation.
3. Weeks 6–7: Hard spend limits (per-agent monthly cap, returns 402 to caller); per-agent action-type blocklist.
4. Weeks 8–9: Stripe; incident-retrospective demo flow ("replay your last agent incident"); onboarding for 5-agent teams.
5. Weeks 10–12: Pilot 5 AI-native companies through Anthropic Builder Community and AI engineer Slack groups.

### Critic's Assessment
**Rating:** 5/10 | **Last critique:** 2026-08-16
**Strongest part:** SanctumShield answered the board-artifact job at $99; the remaining job is a real 402 across vendors.
**Open question:** Is anyone paying for a cross-vendor pause, or do they just set limits in OpenAI’s own dashboard?

---
---

## Removed this run
| Entry | Last score | Reason |
|-------|------------|--------|
| WholesaleDesk | 70 → 52 | **Orderwerks**, **Zoey**, and **WizCommerce** already ship QuickBooks-native B2B buyer portals — R5 “no SMB portal below Shopify” fails launch canary |
| QuoteDock | 69 → 54 | **FasterQuotes**, **Vesel**, **Navix**, **Wisor** parse/forward RFQ email into comparisons — R5 kill condition (paste UX under $100-ish shipper SKU) met |
| DataReady | 65 → 48 | **Datris.ai hosted** is live; **HubSpot Data Agent** is native — R5 “exit without 2+ pilots” |
| PromptFence | 63 → 45 | **RAIC**, **PromptWall**, **SanctumShield ($99/mo)** densify SMB Shadow AI allowlist+audit — last seat expired |
