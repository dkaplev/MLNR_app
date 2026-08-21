# SaaS Opportunity Cookbook
Last updated: 2026-08-21 | Entries: 10/10

> R7 note: MarkPack +2 (Art. 50 enforcement confirmed, public complaint form live). BriefDesk +1 (briefhq.ai confirmed as product-team navigator only — NOT an ops/EA multi-stack brief; wedge is cleaner). FlowTrace removed — last seat expired, no cross-vendor pause customer evidence (score 62→60). AuthTrack removed — displaced by 3 new higher-scoring entries despite being only 5 days old. BreakWatch removed — displaced. **ModelReg** enters on SR 26-2 (Apr 2026) community bank AI inventory gap. **LienLock** enters on conditional lien waiver + payment hold for GCs. **CertPayroll** enters on IIJA-driven Davis-Bacon certified payroll gap below LCPtracker pricing.

---

## #1 — DentPay  ·  80/100  ·  UNCHANGED
First added: 2026-07-16 | Last updated: 2026-08-21 | Score delta this week: —

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — CSV-first rule engine)
- Value Clarity:       18/20  (unchanged — OM ritual self-evident; dentpay.tech + numbers walkthrough)
- Market Timing:       17/20  (unchanged — Samera FAQ still Dentally + SoE only; custom integrations "tell us what you use," not a live OD/Dentrix SKU; Dentivize still analytics dashboards; OD Provider Payroll still a report)
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
**Rating:** 8/10 | **Last critique:** 2026-08-21
**Strongest part:** Samera's own FAQ still lists Dentally/SoE — the US export→Excel path is intact.
**Open question:** Will practices trust a solo tool with paycheck math without a CPA partnership from day one?

---

## #2 — MarkPack  ·  75/100  ·  IMPROVED
First added: 2026-08-03 | Last updated: 2026-08-21 | Score delta this week: +2

> Ship Article 50 evidence — chatbot disclosure, C2PA marks, and an audit folder — before the inspector asks.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — C2PA middleware + disclosure snippets + evidence ZIP; not a full GRC suite)
- Value Clarity:       17/20  (+1 — AI Office complaint form is live; competitor can file on your chatbot in 5 minutes; "show me proof" is no longer hypothetical)
- Market Timing:       18/20  (+1 — enforcement confirmed Aug 2, 2026; public complaint channel active; Dec 2 marking grace ~3.5 months left; OpenCorpo/PixelOffice are checklists, not evidence+CI packs)
- B2B Monetisation:    14/20  ($199–499/mo for genAI product teams shipping EU-facing content)
- Pull Factor:         12/20  (compliance buyers; eng Twitter/GitHub for SDK)

**Strengths:**
- Art. 50 is now enforceable. Competitors can file a complaint about your chatbot in 5 minutes via the EU AI Office's public complaint form.
- Dec 2 grace creates a concrete ~3.5-month sprint window for marking on systems already in market.
- Obligation→artifact mapping + CI fail-on-missing-marks is a solo-shaped wedge vs consulting slideware.

**Risks:**
- Platform-native C2PA (Adobe, model providers) could commoditize marking.
- AnnexOps/ActProof-class tools may expand into evidence packs.
- Demand may cliff after Dec 2 grace if enforcement activity is weak.

**Verdict:** Evidence pack + CI sprint — Dec 2 grace window is the 90-day forcing function.

### The Pitch
**Problem:** From 2 August 2026, EU AI Act Article 50 transparency duties are fully enforceable. Chatbots must disclose AI interaction; generative systems need machine-readable marking (C2PA-class), with a grace period to 2 December 2026 for systems already on the market before 2 August. The EU AI Office complaint form is live: any person — including a competitor — can report a non-compliant chatbot in five minutes. Mid-market product teams have Notion checklists, not an evidence folder an auditor or inspecting authority can open: disclosure screenshots, marking pipeline config, role owners, change logs.

**Solution:** MarkPack is the technical compliance kit: drop-in disclosure components, C2PA/content-credential marking in the generation path, and a one-click evidence pack (ZIP/PDF) mapping each Art. 50 obligation to proof. Built for eng + legal together — not consultants selling slideware.

**Target customer:** Eng lead + counsel at 15–150 person companies shipping EU-facing chatbots or generative content (SaaS, media, agencies). Buyer: CTO/GC. Users: eng implementing marks + compliance owning the evidence folder.

**Why now:** Obligations are live as of 2 August 2026; the public complaint form means your non-disclosure is one click away from a formal investigation. The Dec 2 marking grace is a forcing function for teams who shipped before August without watermarks.

**Why they buy without being sold to:** Counsel asks "show me Art. 50 proof" and eng has nothing reproducible — MarkPack's evidence pack becomes the answer in one afternoon.

**Revenue model:** $199/mo (1 product). $349/mo (5 products + CI check). $499/mo (SSO + custom retention). Annual −2 months. 14-day trial with a sample evidence pack generated from a demo app.

**Unfair advantage:** Obligation→artifact mapping that updates as Commission guidance evolves; GitHub Action that fails PRs missing marks; focused on mid-market eng teams, not Big Four audit packages.

### Solo Build Plan
1. Weeks 1–3: Disclosure component library; evidence schema; sample pack generator.
2. Weeks 4–5: C2PA/content credentials hook for image/video pipeline (one stack first).
3. Weeks 6–7: CI Action; Slack "evidence incomplete" alert.
4. Weeks 8–9: Stripe; EU-facing SaaS onboarding.
5. Weeks 10–12: Pilot 6 teams via AI Act Slack/Discord + YC EU companies.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-21
**Strongest part:** Complaint form is live — any competitor can file on your chatbot in 5 minutes, making this tangible and urgent rather than theoretical.
**Open question:** Will enforcement produce actual fines before Dec 2, or does the grace window quietly pass without material action?

---

## #3 — AdvisorAlert  ·  74/100  ·  UNCHANGED
First added: 2026-07-31 | Last updated: 2026-08-21 | Score delta this week: —

> Catch compliance gaps before the SEC exam does — continuous monitoring built for independent RIAs, not mega-firms.

### Score Breakdown
- Solo Buildability:   12/20  (email scanning in a regulated context; SEC API access; false-positive management; harder than a typical SaaS build but achievable for a solo founder with legal knowledge)
- Value Clarity:       17/20  (SEC deficiency letter = immediate pain trigger; CCO who received one understands the product in 10 seconds)
- Market Timing:       16/20  (unchanged — Hadrius confirmed enterprise custom-quote only, no public starter tier; $22M Series A now confirmed; Claude Enterprise integration announced July 2026; micro-RIA gap intact)
- B2B Monetisation:    17/20  ($299–799/month vs $5K–20K/year compliance consultant; RIAs are trained to pay for compliance)
- Pull Factor:         12/20  (RIA compliance community is tight; word-of-mouth travels through custodian networks and compliance study groups)

**Strengths:**
- Hadrius $22M raise (July 2026, CRV + YC) validates the RIA compliance automation category; now confirmed to use Claude Enterprise for surveillance — still custom quote, no public micro-RIA tier.
- Micro-RIA beachhead ($50M–$500M AUM, 1–5 employees) is explicitly underserved — Hadrius targets enterprise firms and carries a sales-led, opaque pricing model.
- RIAs already pay $5K–$20K/year for compliance consultants; $3,600/year for automated monitoring is an easy value comparison.

**Risks:**
- Regulated space creates legal positioning risk — must be sold as "monitoring tool," not "compliance advice."
- Hadrius has been noted as aggressive on pricing in competitive situations; could announce micro-RIA starter.
- False positives in email flagging erode trust in a high-stakes regulated environment.

**Verdict:** Keep micro-RIA beachhead. Hadrius custom-quote model confirms price gap.

### The Pitch
**Problem:** Independent registered investment advisors with $50M–$500M AUM typically have 1–5 employees, no dedicated CCO, and rely on an annual compliance consultant for $5,000–$20,000/year. Meanwhile the SEC expects continuous monitoring: reviewing client communications for solicitation violations, sampling marketing content, confirming trades match investment policy statements, maintaining a current compliance calendar. Hadrius's $22M raise in July 2026 validated the category — but Hadrius targets enterprise firms with custom-quote pricing, no self-serve option, and no published starter tier. The 1–5 person RIA shop generates 85% of deficiencies on SEC exams and has no purpose-built affordable tool.

**Solution:** AdvisorAlert connects to your Gmail or Outlook, samples 50 client communications per month, and flags language that could constitute testimonials, solicitations, or performance guarantees. It also maintains your compliance calendar (Form ADV due dates, custody rule filings, code of ethics deadlines) and lets you submit marketing content for a plain-English compliance check. The weekly digest is your CCO's to-do list — not a 200-page manual.

**Target customer:** Principal / de-facto CCO at a 1–5 person RIA, $50M–$500M AUM, serving retail or HNW clients on Schwab, Fidelity, or Pershing. Not a broker-dealer, not a family office. Buyer: the principal who is also the CCO. Users: principal + any administrative staff who handle client communication.

**Why now:** AI communication volume is widening the compliance review gap faster than RIA headcount grows. Hadrius's $22M July 2026 raise — confirmed enterprise-only pricing — validates the category but leaves the micro-RIA segment unaddressed. The SEC's 2026 risk alert cited inadequate communication surveillance as the top deficiency in small RIAs. No affordable tool exists below $5K/year.

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
**Rating:** 7/10 | **Last critique:** 2026-08-21
**Strongest part:** Hadrius $22M July 2026 + Claude Enterprise integration = clearest category validation in the cookbook. Custom-quote-only pricing confirms price gap persists.
**Open question:** Will Hadrius announce a self-serve micro-RIA starter tier (sub-$5K/year) using its Series A capital?

---

## #4 — BriefDesk  ·  73/100  ·  IMPROVED
First added: 2026-07-31 | Last updated: 2026-08-21 | Score delta this week: +1

> Your Monday morning leadership brief writes itself — pulled from your real CRM, PM, and billing data, not from memory.

### Score Breakdown
- Solo Buildability:   17/20  (unchanged — 3 OAuth integrations + AI synthesis < $0.02/brief; clearly shippable solo in 3 months)
- Value Clarity:       17/20  (unchanged — CSW Solutions July 2026 documents exact pain: "4-5 hours every Friday"; self-evident ROI)
- Market Timing:       13/20  (+1 — briefhq.ai confirmed as product-team navigator only, NOT an ops/EA multi-stack brief; wedge cleaner than last run; Data Parrot still HubSpot-only sales brief; multi-stack ops leadership brief remains unclaimed)
- B2B Monetisation:    15/20  (unchanged — $149–399/month; professional services teams have clear budget for time-back tools)
- Pull Factor:         11/20  (unchanged — "weekly brief" category noise; rename before launch remains critical)

**Strengths:**
- CSW Solutions (July 2026) documents the exact ritual: CRM tab → PM tab → billing tab → paste into Notion doc on Friday afternoon. Product builds itself around a lived pain.
- briefhq.ai confirmed as product-decision navigator for software product teams — a different buyer persona and different data sources. Multi-stack ops/EA weekly narrative is still distinct.
- AI synthesis cost is < $0.02 per brief; margin structure is exceptional.

**Risks:**
- HubSpot INBOUND (September 2026) could announce a "weekly cross-stack AI narrative summary" via 1,400+ connected integrations. Watch closely.
- "Narrative brief" vs dashboard remains a positioning risk — some ops leads have accepted dashboards and don't feel the brief pain.
- The rename deadline is this run; launching as "BriefDesk" invites comparison with briefhq.ai.

**Verdict:** Keep. briefhq.ai is not a competitor; the ops/EA multi-stack narrative brief is still open. Rename before launch. HubSpot INBOUND is the kill signal to watch.

### The Pitch
**Problem:** Professional services firms, agencies, and B2B SaaS companies spend 4–5 hours every Friday manually pulling CRM deal updates, project status from their PM tool, and revenue figures from QuickBooks into a leadership brief. One person — usually the ops manager, EA, or founder — reads from three browser tabs and types into a Notion document. The brief costs $200–500 in staff time to produce, arrives late, and is stale by Monday morning. CSW Solutions documented this workflow in July 2026: "someone would export from system A, copy into the report, go to system B, copy into the report — then hope the math is right."

**Solution:** BriefDesk connects to your HubSpot (or Pipedrive), ClickUp (or Asana/Linear), and QuickBooks (or Xero/Stripe) via API and runs automatically every Friday at 4pm. It pulls key metrics — pipeline movement, project status by owner, revenue vs. target — and synthesises them into a readable narrative brief. The brief arrives in Slack or email before 5pm. Reviewers annotate before it goes to leadership; the AI does the research, the human adds context.

**Target customer:** Operations lead / EA / founder at a 10–100 person professional services firm, agency, or B2B SaaS company using HubSpot or Pipedrive + ClickUp or Asana + QuickBooks or Xero. Buyer: founder/COO. User: ops lead or EA who currently builds the brief manually.

**Why now:** AI synthesis costs less than $0.02 per brief. HubSpot, ClickUp, and QuickBooks all publish REST APIs that support weekly automated pulls without screen-scraping. BigIdeasDB 2026 validates manual reporting as the #1 business pain at 33.3% validation rate. briefhq.ai covers product teams (Linear + GitHub + Notion); ops/EA multi-stack (CRM + PM + billing) remains the open wedge.

**Why they buy without being sold to:** An ops manager who spent Friday afternoon copy-pasting into a leadership report gets a BriefDesk free trial, connects their HubSpot stack, and receives the same brief automatically at 5pm. They do not buy BriefDesk — they just stop cancelling it after the trial.

**Revenue model:** $149/month (1 stack: 1 CRM + 1 PM + 1 billing source; 1 brief/week). $249/month (2 stacks; for agencies managing internal + client reporting). $399/month (custom templates + Slack delivery + API access). Annual discount: 2 months free. 14-day trial with 2 live briefs generated from real data.

**Unfair advantage:** First-mover in "narrative brief vs dashboard" for multi-stack ops/EA. Vertical templates for agencies, SaaS, and professional services that any platform's native AI cannot match across stacks. Distribution via HubSpot Partner ecosystem and ClickUp Integrations Marketplace.

### Solo Build Plan
1. Weeks 1–2: HubSpot + ClickUp + QuickBooks OAuth; scheduled weekly metric pull; error handling and rate limits.
2. Weeks 3–4: AI narrative synthesis (GPT-4o or Claude); Slack + email delivery; brief template builder.
3. Weeks 5–6: Review/annotate workflow before distribution; stale-data warnings; week-over-week comparison.
4. Weeks 7–8: Stripe; 14-day trial with 2 live briefs; onboarding wizard with vertical template selection.
5. Weeks 9–12: Pilot 8 agencies and PS firms through HubSpot Partner community + ClickUp Marketplace.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-21
**Strongest part:** briefhq.ai confirmed as product-team navigator only — the ops/EA multi-stack leadership brief is cleaner than previous assessments showed.
**Open question:** Will HubSpot announce a "weekly cross-stack narrative summary" at INBOUND September 2026, killing the wedge?

---

## #5 — RuleFlow  ·  73/100  ·  UNCHANGED
First added: 2026-08-16 | Last updated: 2026-08-21 | Score delta this week: —

> New federal rules become a checklist and an evidence folder — not another unread PDF in Slack.

### Score Breakdown
- Solo Buildability:   13/20  (FRTracker-class obligation feed + Asana/Jira tasks + evidence ZIP; legal-correctness review is the hard part)
- Value Clarity:       16/20  ("this rule changed — here is what you must do by when" is a 15-second pitch for a CCO)
- Market Timing:       16/20  (YC Fall 2026 RFS asked for AI-native compliance infrastructure on 23 Jul; FRTracker is a free research primitive with no mid-market workflow layer; CUBE/AscentAI remain Tier-1; complianceofficer.ai in early access at $149-$1499/mo is broader but not obligation→Jira workflow)
- B2B Monetisation:    17/20  (community banks and fintech lenders already pay six figures in fines and consultants; $399–799/mo is cheap next to that)
- Pull Factor:         11/20  (compliance communities share tools quietly; not LinkedIn-viral)

**Strengths:**
- FRTracker already extracts must/shall/may-not obligations deterministically — the missing product is "new rule → owner → due date → evidence," not another AI summariser.
- YC's July 2026 request validates the category; incumbents sell libraries, not a 4-person compliance team's inbox.
- Traceable, non-black-box extraction is a selling point for auditors.

**Risks:**
- FRTracker (or a well-funded RegTech) adds the workflow layer and collapses the wedge.
- Wrong obligation mapping creates legal liability; product must be "monitoring," not advice.
- complianceofficer.ai (early access, $149-$1499/mo) watches regulations broadly — worth monitoring for workflow features.

**Verdict:** Enter as the workflow layer on top of public obligation feeds. One vertical first: US fintech lenders / community banks.

### The Pitch
**Problem:** A four-person compliance team at a community bank or fintech lender tracks Federal Register changes in a shared spreadsheet and a Slack channel of PDFs. CUBE and AscentAI sell this to Tier-1 banks. FRTracker (free) now extracts individual must/shall obligations from 989K+ documents — but it is a research tool, not a system of record. When a final rule drops, nobody owns the checklist, and the exam asks for evidence that does not exist.

**Solution:** RuleFlow turns each relevant obligation into a task with an owner, a due date, and an evidence slot. It watches the agencies you care about, diffs proposed vs final, and opens Asana/Jira items mapped to the source passage. At exam time you export a folder: rule, obligation, who did what, attached proof.

**Target customer:** CCO / compliance analyst at a 20–200 person US fintech lender, community bank, or payments firm. Not a broker-dealer mega-firm. Buyer: CCO or General Counsel. Users: the 2–6 people who currently paste Federal Register links into Slack.

**Why now:** YC's Fall 2026 RFS (23 Jul) asked for AI-native compliance infrastructure that maps activities to rules, filings, and evidence. The open primitive (FRTracker) exists; the mid-market workflow layer does not. Enterprise RegTech still starts at six figures.

**Why they buy without being sold to:** After a consent order or a nasty FR notice, the CCO pastes last month's "rules we think apply" spreadsheet into RuleFlow, sees three missed effective dates, and refuses to go back to Slack-PDFs.

**Revenue model:** $399/mo (1 agency family + 10 users). $599/mo (3 families + Jira/Asana sync). $799/mo (unlimited + evidence vault + SSO). Annual −2 months. 14-day trial on a saved agency watchlist.

**Unfair advantage:** Obligation→task→evidence mapping for one vertical (US depository / fintech lending) with citations back to primary text — not a 200-jurisdiction library.

### Solo Build Plan
1. Weeks 1–3: Ingest FRTracker API or daily FR deltas; agency watchlist; obligation cards with source quotes.
2. Weeks 4–5: Task export to Asana/Jira; owner + due date; proposed-vs-final diff view.
3. Weeks 6–7: Evidence upload per obligation; exam-pack ZIP/PDF.
4. Weeks 8–9: Stripe; fintech-lending template (lending, BSA/AML notices, CFPB).
5. Weeks 10–12: Pilot 5 CCOs via ABA/community-bank ops groups and fintech compliance Slack.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-21
**Strongest part:** The primitive is free and public; the unpaid job is workflow + evidence, which is exactly what a 4-person team will pay for.
**Open question:** Will FRTracker itself add "send to Jira" or will complianceofficer.ai expand into obligation→task workflow?

---

## #6 — ChurnDetect  ·  73/100  ·  UNCHANGED
First added: 2026-07-31 | Last updated: 2026-08-21 | Score delta this week: —

> Find the customers about to leave — 90 days before they tell you — from the support tickets they are already sending.

### Score Breakdown
- Solo Buildability:   15/20  (Zendesk/Intercom API + AI ticket classification + Slack alerts = 3 months feasible for a focused MVP)
- Value Clarity:       17/20  ("retrospective demo on your last churned account" is self-closing; no pitch required after that demo)
- Market Timing:       13/20  (Zendesk Intelligent Triage rolled to Professional plans Jul 2026; still topic/sentiment per ticket, not account-level churn; gap intact for now)
- B2B Monetisation:    15/20  ($199–599/month; CS budget exists; protecting $30K ARR easily justifies $349/month)
- Pull Factor:         13/20  (CS AI category noise; retrospective demo still the wedge)

**Strengths:**
- Retrospective demo ("see the 8 tickets before your last churned account") is a self-closing sales mechanism that requires no pitch.
- 60% of B2B software buyers regretted their purchase in 18 months (Helply 2026); churn risk is surfaced in tickets months before renewal.
- Gap between enterprise (Gainsight $30K+, ChurnZero $20K+) and nothing for 10–150 seat SaaS is clear and large.

**Risks:**
- Zendesk's native "Intelligent Triage" already classifies intent and sentiment per ticket; account-level health SKU could follow.
- PII/SOC2 considerations for storing and scanning customer support data require explicit consent flows.
- Planhat ($1K+/month, mid-market) could push further downmarket.

**Verdict:** Hold retrospective-demo wedge. Zendesk account-health SKU is the watch signal.

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
**Rating:** 7/10 | **Last critique:** 2026-08-21
**Strongest part:** The retrospective demo on a recently churned account is a self-closing conversion mechanism unlike anything else in the cookbook.
**Open question:** Will Zendesk turn topic+sentiment into an account-health SKU in H2 2026?

---

## #7 — TokenBill  ·  72/100  ·  UNCHANGED
First added: 2026-08-16 | Last updated: 2026-08-21 | Score delta this week: —

> One invoice-level forecast for OpenAI, Claude, and Cursor — before token shock hits the P&L.

### Score Breakdown
- Solo Buildability:   16/20  (email/PDF invoice ingest + vendor price tables + cap alerts; no SDK in the customer's app)
- Value Clarity:       16/20  (Techaisle 2026 "token shock" is the #1 SMB IT budget challenge; "what will AI cost next month?" is obvious)
- Market Timing:       13/20  (pain is #1 SMB IT challenge in 2026; Helicone/Langfuse/vendor consoles exist but are engineer-facing and per-provider; no Ramp/Brex AI category found)
- B2B Monetisation:    15/20  ($149–399/mo vs surprise $8K OpenAI bills; finance will pay for forecastability)
- Pull Factor:         12/20  (CFO Slack/communities share war stories; quieter than eng Twitter)

**Strengths:**
- Techaisle 2026 names unpredictable AI consumption as the budget-constraint evolution of cloud-cost panic; confirmed as #1 SMB IT challenge.
- Wedge is finance, not observability: invoices and card statements, not traces.
- Helicone ($79, proxy) and Langfuse ($29, SDK) do not serve a non-engineer ops/finance buyer.

**Risks:**
- OpenAI / Anthropic / Cursor admin consoles get "CFO forecast" tabs.
- Ramp, Brex, or Mercury add AI-vendor spend categories (no evidence found this week).
- Invoice formats are messy; accuracy below ~90% kills trust.

**Verdict:** Enter as the invoice-level AI spend forecast for 20–100 person companies. Do not build another Langfuse.

### The Pitch
**Problem:** SMBs in 2026 run OpenAI, Anthropic, Cursor, and a handful of other AI tools on usage pricing. Techaisle's 2026 SMB IT survey put budget unpredictability — "token shock" — at the top of the challenge list, ahead of classic cloud optimisation. The engineer can open Helicone. The ops lead and the bookkeeper get PDF invoices they cannot forecast, cannot allocate to teams, and cannot cap.

**Solution:** TokenBill ingests invoices and billing emails from the AI tools you already pay, maps them to a single forecast, and alerts Slack when a vendor is running hot vs last month. No SDK. No proxy in the product. Caps are "tell finance," not "return 402 to the model."

**Target customer:** Ops lead / controller / founder at a 20–100 person B2B company spending $1K–$20K/month across 3+ AI vendors. Buyer: founder or finance. User: the person who currently forwards OpenAI invoices into a sheet.

**Why now:** Usage-based AI billing went from experiment to line item in 2026. Observability tools solved this for engineers. Finance still has PDFs.

**Why they buy without being sold to:** After one $4,000 Cursor+OpenAI month that nobody budgeted, the controller forwards last quarter's invoices into TokenBill, sees the run-rate, and sets a Slack alert the same afternoon.

**Revenue model:** $149/mo (3 vendors, email forward). $249/mo (10 vendors + team allocation). $399/mo (SSO + CSV to QBO). Annual −2 months. 14-day trial.

**Unfair advantage:** Vendor invoice parsers + finance-shaped alerts. Distribution via bookkeeper / fractional-CFO communities, not AI engineer Twitter.

### Solo Build Plan
1. Weeks 1–3: Email-forward ingest for OpenAI, Anthropic, Cursor PDFs; vendor normaliser; monthly total view.
2. Weeks 4–5: Run-rate forecast; vs last month; Slack threshold alerts.
3. Weeks 6–7: Team/cost-centre tags; CSV export.
4. Weeks 8–9: Stripe; sample-invoice onboarding.
5. Weeks 10–12: Pilot 8 companies via fractional-CFO Slack and indie-hacker ops channels.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-21
**Strongest part:** Buyer is finance, which Helicone/Langfuse ignore; Techaisle 2026 names the pain as #1 SMB IT budget challenge.
**Open question:** Will Ramp/Brex or the model vendors ship a good-enough spend forecast before TokenBill gets to 10 paying customers?

---

## #8 — ModelReg  ·  72/100  ·  NEW
First added: 2026-08-21 | Last updated: 2026-08-21 | Score delta this week: —

> Exam-ready AI model inventory for community banks — built to the SR 26-2 standard, not the enterprise GRC standard.

### Score Breakdown
- Solo Buildability:   14/20  (structured register + risk-classification wizard + PDF report generator; no PHI/PII storage in the product itself; 3 months feasible)
- Value Clarity:       16/20  ("show your AI model inventory when the OCC examiner asks" is a 10-second pitch for any bank CCO; SR 26-2 is the examiner's checklist)
- Market Timing:       14/20  (SR 26-2 issued April 17, 2026; first exams under new guidance happening now; AegisAI targets community banks but pricing unconfirmed; 5,000+ US community banks have no affordable option)
- B2B Monetisation:    16/20  (community banks pay $3K–$15K/year for compliance tools routinely; $299–599/month is budget-line; CIMCON/ValidMind start at $30K+/year)
- Pull Factor:         12/20  (bank compliance community shares via ICBA, ABA conferences; not social-viral)

**Strengths:**
- SR 26-2 issued April 2026 — examiners are asking about AI model governance on every exam for the first time; the market has no time to wait.
- 5,000 US community banks + 5,000 credit unions under $5B in assets can't justify $30K+/year enterprise MRM platforms.
- "Exam letter trigger" conversion mechanism: CCO receives an SR 26-2 inquiry, registers their models in ModelReg, produces a compliant PDF in one afternoon.

**Risks:**
- AegisAI Compliance specifically targets SR 26-2 compliance for community banks; if priced at $200-$400/month with easy onboarding, this idea is displaced.
- ncontracts (broad bank compliance platform) could ship an AI model inventory module.
- SR 26-2 explicitly says guidance is "most relevant" to $30B+ banks, which may reduce urgency for smaller institutions.

**Verdict:** Enter as the affordable, exam-focused AI model register for community banks under $5B. AegisAI pricing is the #1 watch signal.

### The Pitch
**Problem:** In April 2026, the Federal Reserve, OCC, and FDIC jointly issued SR 26-2, updating model risk management guidance for the first time since 2011. For community banks and credit unions, this means examiners will now ask — on every examination — whether the institution maintains an AI model inventory documenting every quantitative model, AI system, and vendor-embedded AI tool, with ownership, risk tier, and a documented validation schedule. Enterprise platforms (CIMCON, ValidMind, ModelOp) start at $30,000+/year and are built for $30B+ institutions with dedicated model risk teams. A $500M community bank with 20 AI tools and no model risk officer has nowhere to go.

**Solution:** ModelReg is a web-based AI model register built specifically for community banks and credit unions. CCOs or compliance officers register each model or AI tool through a short SR 26-2-aligned risk classification wizard — purpose, complexity, customer-facing impact, validation frequency — and ModelReg generates an exam-ready inventory report in PDF format, using the exact language OCC examiners use. Traditional models (credit scoring, BSA/AML alerts) and non-traditional AI tools (vendor chatbots, document processors) are tracked in the same register with SR 26-2's classification distinction built in.

**Target customer:** CCO, Chief Risk Officer, or VP of Technology at a US community bank or credit union with $100M–$5B in total assets. Not a $30B+ institution with a dedicated model risk team. Buyer: CCO or Chief Risk Officer. User: compliance officer or IT manager who maintains the inventory.

**Why now:** SR 26-2 was issued April 17, 2026 — every regulatory examination since then is the first under the revised guidance, and examiners are already noting AI governance gaps in examination findings. The FSB's August 2026 consultation on AI sound practices for financial institutions adds a global dimension. Enterprise platforms ignore the community bank segment; AegisAI's pricing for community banks is unconfirmed.

**Why they buy without being sold to:** A CCO who receives an OCC examination request asking to "describe your AI model inventory and risk classification process" pastes the requirement into ModelReg's onboarding wizard, registers the institution's 12 known AI tools in under an hour, and produces a compliant PDF inventory before the 30-day response deadline. The product sells itself the moment the examination letter arrives.

**Revenue model:** $299/month (1 institution, unlimited model records, exam-ready PDF export, validation schedule reminders). $499/month (multi-entity: holding company with up to 5 affiliated institutions). Annual −2 months. 14-day trial with a sample inventory report generated from onboarding responses.

**Unfair advantage:** SR 26-2-specific exam language and report templates drafted from the actual April 2026 guidance text; targeted exclusively at the $100M–$5B community bank and credit union segment that enterprise MRM platforms explicitly do not serve.

### Solo Build Plan
1. Weeks 1–3: Model/AI tool register (name, type, purpose, owner, risk tier, validation date, vendor flag); SR 26-2 risk classification wizard with built-in "in scope vs. out of scope" guidance.
2. Weeks 4–5: Exam-ready inventory PDF report template using OCC/Fed examination language; quarterly validation reminders via email.
3. Weeks 6–7: Vendor AI tool tracking (third-party model name, contract terms, last validation, OCC third-party risk note); changelog audit log.
4. Weeks 8–9: Stripe; onboarding "SR 26-2 gap checker" that compares current inventory against a standard examination checklist; legal disclaimer ("monitoring tool, not model validation or regulatory advice").
5. Weeks 10–12: Pilot 5 community banks via ABA/ICBA community bank compliance groups, bank examiner prep consultants, and community bank BSA/compliance Slack channels.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-21
**Strongest part:** SR 26-2 exam language built into report templates — the CCO hands the examiner a document that speaks the regulator's own vocabulary.
**Open question:** What is AegisAI Compliance's actual pricing for a community bank under $1B in assets — enterprise ($500+/month) or SMB ($200-$400/month)?

---

## #9 — LienLock  ·  72/100  ·  NEW
First added: 2026-08-21 | Last updated: 2026-08-21 | Score delta this week: —

> Get the conditional lien waiver before the payment clears — every draw, every subcontractor.

### Score Breakdown
- Solo Buildability:   16/20  (sub register + draw schedule + conditional waiver status + no-login upload link; simple CRUD workflow; 3 months feasible)
- Value Clarity:       17/20  ("don't pay until you have the waiver" is understood by every GC in 10 seconds; mechanic's lien exposure is visceral)
- Market Timing:       12/20  (IIJA driving 40%+ more commercial construction work vs 2022; PaperBoss tracks lien waiver documents but lacks payment-conditional hold mechanism; specific wedge confirmed open)
- B2B Monetisation:    15/20  ($149–399/month vs $12K–$45K average mechanic's lien resolution cost; strong ROI; GCs already pay for construction software)
- Pull Factor:         12/20  (construction industry peer word-of-mouth at AGC/ABC chapters; not social-viral)

**Strengths:**
- Every GC with subs has faced a missed waiver; the pain is immediate and quantifiable ($12K–$45K per lien dispute, 40% of projects involve a lien claim).
- PaperBoss and TrackMyVendor track lien waiver documents but have no "payment conditional hold" mechanism — the differentiation is the controller's "do not release payment until waivers received" blocker.
- IIJA-driven construction surge brings more small GCs into multi-sub projects for the first time.

**Risks:**
- PaperBoss could add a payment-conditional hold feature to their existing lien waiver module (they're at $29–$149/month, aggressively expanding features).
- Lien waiver templates must be state-specific and legally accurate; errors create GC liability.
- BuilderTrend, Procore, CoConstruct have payment features at higher price points for larger GCs who might push downmarket.

**Verdict:** Enter as the controller-facing "payment hold until waiver received" tool. Lien waiver template library for 50 states is the legal moat.

### The Pitch
**Problem:** General contractors with 10–50 active subcontracts process draws on a project payment schedule — typically 5–8 payment periods per project. Before releasing each draw, they should obtain a conditional lien waiver from each sub: a signed form releasing the sub's right to file a mechanic's lien up to that payment amount. In practice, GCs track this in Excel or forget entirely, because no affordable tool links waiver receipt to payment release. 40% of construction projects involve a lien claim; the average mechanic's lien costs $12,000–$45,000 to resolve.

**Solution:** LienLock tracks each subcontract, each draw period, and the conditional waiver status for every payment. When a draw is ready for release, LienLock sends the sub a no-login link to sign and return the conditional waiver digitally. The controller's dashboard shows a clear blocker: "Draw 3 — waiver received from 11 of 14 subs. Do not release payment for Adams Electrical or Falcon Plumbing until their waivers arrive." Payment is not released until all required waivers are collected or the GC manually overrides with a reason.

**Target customer:** Controller, owner, or project manager at a 2–20 person general contractor managing 10–50 active subcontracts on commercial, multifamily, or light industrial projects. Buyer: owner or controller. Users: PM + accounting.

**Why now:** The IIJA is driving 40%+ more commercial construction work in 2026 vs. 2022, bringing more small GCs into multi-sub projects for the first time. PaperBoss and TrackMyVendor cover COI/W-9 compliance but have no payment-conditional hold mechanism that links waiver receipt to payment release.

**Why they buy without being sold to:** A GC who missed a conditional waiver on Draw 2 — and is now facing a $23,000 mechanic's lien from an electrical sub — uploads their current sub list, enters the active project, and immediately sees which waivers are missing before releasing Draw 3. That's the moment they stop tracking in Excel.

**Revenue model:** $149/month (1 active project, 25 subs, basic waiver collection). $249/month (5 projects, unlimited subs, payment-hold blocker dashboard). $399/month (unlimited projects + lien waiver template library for all 50 states + Stripe payment hold integration). Annual −2 months. 14-day trial with sample waiver collection flow.

**Unfair advantage:** Pre-built conditional and unconditional lien waiver templates for all 50 states with automatic release amount calculation — the legal paperwork that makes this tool immediately useful without a setup consultation.

### Solo Build Plan
1. Weeks 1–3: Project/sub register; draw period schedule; conditional waiver status per sub per draw; no-login sub email link for waiver upload.
2. Weeks 4–5: Controller dashboard with "waiver received/pending/overdue" per draw; automated reminders to subs at 3, 7, and 14 days.
3. Weeks 6–7: Lien waiver template library (top 10 states by construction volume first); unconditional waiver on final payment workflow.
4. Weeks 8–9: Stripe; CSV sub list import; sample project onboarding; legal disclaimer ("templates for reference — verify with local counsel").
5. Weeks 10–12: Pilot 8 GCs via local AGC/ABC chapter meetings and construction-focused Slack communities.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-21
**Strongest part:** "Don't release payment until waiver received" is the specific missing mechanism that every COI/W-9 tool skips — PaperBoss collects documents; LienLock blocks the check.
**Open question:** Will PaperBoss add a payment-conditional hold mechanism to their existing lien waiver module, making LienLock redundant at launch?

---

## #10 — CertPayroll  ·  71/100  ·  NEW
First added: 2026-08-21 | Last updated: 2026-08-21 | Score delta this week: —

> Generate your WH-347 certified payroll in 10 minutes — not 3 hours — every week, every prevailing wage job.

### Score Breakdown
- Solo Buildability:   15/20  (payroll CSV import + DOL wage determination API + WH-347 form population + error flags; federal form complexity is learnable but requires prevailing wage expertise to get right)
- Value Clarity:       16/20  ("upload payroll CSV → 10 minutes → completed WH-347 ready to submit" is immediately understood by any contractor doing Davis-Bacon work)
- Market Timing:       13/20  (IIJA still pumping $500B+ in public works through 2030; Davis-Bacon expanded to 200K+ additional contracts/year in March 2023 final rule; LCPtracker enterprise pricing still starts at $500+/month)
- B2B Monetisation:    15/20  ($149–249/month vs 3–4 hours/week manual work; GCs doing prevailing wage work already budget for compliance tools; clear ROI for anyone doing 1+ WH-347 per week)
- Pull Factor:         12/20  (construction accountants as warm referral channel; prevailing wage compliance groups; not social-viral)

**Strengths:**
- IIJA creating a wave of prevailing wage work for small trade contractors (electrical, roofing, HVAC, masonry) who have never done Davis-Bacon compliance before.
- LCPtracker dominates the enterprise end at $500+/month with professional setup; a $149/month self-serve tool is a clear market gap.
- The DOL wage determination database is a public API — the core data dependency is free and official.

**Risks:**
- Tempede may already address small contractors at affordable pricing (unconfirmed; needs canary check).
- State prevailing wage rules (California DIR, New York, Illinois) are different forms with different complexity; limiting to federal WH-347 in v1 caps the addressable market.
- QuickBooks or Gusto could add a certified payroll module if Davis-Bacon volume grows enough.

**Verdict:** Enter as the federal Davis-Bacon WH-347 tool for 3–20 person trade contractors. California/New York state prevailing wage is v2. Construction accountants are the distribution wedge.

### The Pitch
**Problem:** Every contractor doing federally-funded work under the Davis-Bacon Act must submit a WH-347 Certified Payroll Form to the awarding agency weekly. For a 10-person roofing or electrical contractor getting their first IIJA-funded school renovation project, this means manually transferring payroll data from QuickBooks or Gusto into the federal WH-347 form, calculating prevailing wage rates by classification, apprentice ratios, and fringe benefit credits — then doing this every single week for the project duration. LCPtracker (the dominant certified payroll software) starts at $500+/month and requires professional setup, pricing out the small contractor doing 1–3 prevailing wage jobs per year.

**Solution:** CertPayroll imports your weekly payroll export from QuickBooks Online, Gusto, or CSV, maps workers to their wage classifications and the official DOL wage determinations for the county and project type, and generates a completed, compliance-checked WH-347 PDF ready to submit. It flags common errors before submission: missing apprentice ratio, fringe benefit undercalculation, wrong wage determination for the county. The contractor reviews the flagged items, clicks approve, and the weekly deadline is met — no manual form-filling, no spreadsheet math.

**Target customer:** Owner or office manager at a 3–20 person specialty trade contractor (electrical, plumbing, roofing, masonry, HVAC) doing 1–5 federally-funded public works projects per year. Not a large GC with a compliance team. Buyer: owner or office manager. Users: the same person who currently fills out the WH-347 manually.

**Why now:** The IIJA (2021) is injecting $500B+ in public works construction through 2030, with Davis-Bacon applying to all federally-assisted projects above $2,000 — bringing hundreds of thousands of small trade contractors into prevailing wage compliance for the first time. The March 2023 Davis-Bacon final rule also expanded coverage to an estimated 200,000 additional contracts per year, dramatically widening the market of contractors who need this.

**Why they buy without being sold to:** A roofing contractor who spent 4 hours on a Friday night transferring payroll to a WH-347 form, then got a correction notice from the awarding agency Monday morning, uploads last week's Gusto CSV export into CertPayroll, receives a completed error-checked WH-347 in 12 minutes with the apprentice ratio warning resolved, and starts a subscription before the next pay period.

**Revenue model:** $149/month (3 active prevailing wage projects, QuickBooks/Gusto import, WH-347 PDF export, apprentice ratio tracking, error flags). $249/month (10 projects + state prevailing wage support for top 10 states by construction volume + wage determination lookup assistant). Annual −2 months. Free first project — first month of WH-347 generation at no charge.

**Unfair advantage:** DOL wage determination database integration + error-checking rules built from common WH-347 rejection patterns + construction accountant referral network as distribution — the specific institutional knowledge LCPtracker charges $500+/month for, delivered at $149/month for small contractors doing occasional prevailing wage work.

### Solo Build Plan
1. Weeks 1–3: CSV/QuickBooks/Gusto payroll import; worker-to-classification mapping UI; DOL wage determination API integration for federal county-specific rates.
2. Weeks 4–5: WH-347 form population engine; fringe benefit credit calculation; apprentice ratio checker; common-error flags (wrong classification, missing fringe, ratio violation).
3. Weeks 6–7: Completed WH-347 PDF generator with submission-ready formatting; project register; weekly deadline reminder system.
4. Weeks 8–9: Stripe; sample payroll CSV onboarding; QBO direct integration via QuickBooks Online API.
5. Weeks 10–12: Pilot 8 small trade contractors through local prevailing wage compliance groups, construction accountant referrals, and NECA/SMACNA local chapter contacts.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-21
**Strongest part:** The "upload payroll → 10 minute demo → see your completed WH-347" conversion mechanism is self-closing — the free first project sells the subscription.
**Open question:** Does Tempede already price competitively for small contractors doing 1–5 prevailing wage projects/year, and is it self-service?

---

## Removed this run
| Entry | Last score | Reason |
|-------|------------|--------|
| FlowTrace | 62→60 | Last seat expired. No cross-vendor pause customer evidence found. SanctumShield ($99/mo) and Helicone/Langfuse still hold adjacent shelves. Displaced by 3 new entries scoring 71–72. |
| AuthTrack | 70 | Displaced by 3 new entries (ModelReg 72, LienLock 72, CertPayroll 71). Added Aug 16 — just 5 days ago. CMS PA compliance wedge remains valid; reintroduce if new entries weaken. |
| BreakWatch | 67 | Displaced by 3 new entries. Consumer-side API change watch is a real pain but Specway 2026 data didn't produce strong conversion evidence. Market Timing (11/20) too weak. |
