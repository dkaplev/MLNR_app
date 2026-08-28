# SaaS Opportunity Cookbook
Last updated: 2026-08-28 | Entries: 10/10

> R10 note: Three definitive kills this run. **TokenBill removed** — Ramp launched free AI Token Spend Management on July 16, 2026 (connects to OpenAI/Anthropic/Cursor/Gemini admin APIs; free standalone tier). **BreakWatch removed** — breakwatch.dev is a live product at €29/month with exactly this use case; FlareCanary + breaking.watch + APIShift also cover consumer-side monitoring. **FlowTrace removed** — TrustLogix (enterprise kill switch), cascadeflow.ai (commercial), aMaze (OSS), tracepath (OSS) now fill the agent governance space. **ModelReg enters** at #3 — AegisAI Compliance sells one-time templates ($99–247), NOT a live SaaS; their planned Evidence Tracker SaaS is still unbuilt; the workflow gap for community bank AI governance is confirmed. **AnnexDesk enters** at #9 — collaborative web SaaS for EU AI Act Annex IV documentation; OSS tools (annex4-cli, @systima/aiact-docs) are CLI/npm only. **AgentPermit enters** at #10 — web dashboard for AI agent permission management; TrustLogix (enterprise) and OSS tools (aMaze, ryanwi) leave SMBs unserved. Run 9 candidates LienLock and CertPayroll confirmed killed: BuildPass.ai ships payment-conditional lien waiver hold; CertifiedPayrollPro ($49–149/month, $0 setup) ships affordable Davis-Bacon certified payroll. DentPay holds #1; RuleFlow and AuthTrack unchanged. AdvisorAlert and ChurnDetect each decline 3 points (RegFin emerges as comprehensive micro-RIA SaaS; Teravictus/SignalHOT/Skopx crowd churn-from-tickets space).

---

## #1 — DentPay  ·  80/100  ·  UNCHANGED
First added: 2026-07-16 | Last updated: 2026-08-28 | Score delta this week: —

> Turn Open Dental / Dentrix production exports into clean associate and hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — CSV-first rule engine; OD API exists for employee data but not production % pay rules)
- Value Clarity:       18/20  (unchanged — OM ritual self-evident; dentpay.tech + numbers walkthrough)
- Market Timing:       17/20  (unchanged — OD ADP export is for time cards, not production-% reconciliation; Dentrix Report Converter validates PDF-to-CSV demand; Sikka ONE API enables competitors but none has shipped a production pay tool)
- B2B Monetisation:    16/20  (unchanged)
- Pull Factor:         13/20  (unchanged — study clubs; US outreach guide for discovery calls)

**Strengths:**
- OD's ADP export is time-card-only (clock in/out); production-% reconciliation from Provider Payroll export remains uncaptured by any payroll platform.
- Dentrix Report Converter ($X/month subscription) proves demand for extracting Dentrix data into structured formats — the pain is real and someone is already paying to solve half of it.
- Sticky once pay rules configured — wrong paycheck = employer liability; switching cost is existential.

**Risks:**
- Dental Intelligence or Dentrix itself could deepen native pay math in a platform update.
- Dentivize with expanded payroll reconciliation features would be a direct threat.
- Relationship-heavy sales; CPA/advisor trust needed for paycheck-math credibility.

**Verdict:** Hold #1. US OD CSV-first beachhead still open; Dentrix Report Converter proves willingness to pay for exactly this class of export-to-structured-data tool.

### The Pitch
**Problem:** US dental practices paying associates and hygienists on production still spend hours each pay period exporting Open Dental or Dentrix reports, pasting into Excel, applying lab fees, write-offs, and card-fee rules, then hoping the spreadsheet matches the contract. Open Dental's Provider Payroll report is raw material, not a pay engine. OD's native ADP export handles time cards only — not production splits. Dentrix Report Converter's subscription model proves that practices will pay monthly just to get Dentrix PDF reports into a spreadsheet. Samera automated this for UK Dentally+Xero; Gusto deposits pay but does not reconcile OD production rules. No payroll platform has native plug-and-play integration with all three major US PMS systems.

**Solution:** DentPay imports OD/Dentrix production exports, applies per-provider pay rules once, flags anomalies before payout, and exports an approval pack to Gusto/ADP. Office managers review exceptions; they do not rebuild formulas.

**Target customer:** Office manager / owner at 1–3 location US dental practice on Open Dental or Dentrix with associates or hygienists on production splits.

**Why now:** Production % pay still the norm; UK tools (Samera/Dentivize) proved analytics willingness-to-pay; US PMS vendors have not productised the reconciliation layer; Dentrix Report Converter's subscription model confirms ongoing-pay demand for export tooling.

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
**Strongest part:** Dentrix Report Converter's recurring subscription model proves OMs will pay monthly for export tooling — DentPay is the same pattern with pay-rule intelligence on top.
**Open question:** Will practices trust a solo tool with paycheck math without a CPA partnership from day one?

---

## #2 — RuleFlow  ·  73/100  ·  UNCHANGED
First added: 2026-08-16 | Last updated: 2026-08-28 | Score delta this week: —

> New federal rules become a checklist and an evidence folder — not another unread PDF in Slack.

### Score Breakdown
- Solo Buildability:   13/20  (unchanged — FRTracker-class obligation feed + Asana/Jira tasks + evidence ZIP; legal-correctness review is the hard part)
- Value Clarity:       16/20  (unchanged — "this rule changed — here is what you must do by when" is a 15-second pitch for a CCO)
- Market Timing:       16/20  (unchanged — YC Fall 2026 RFS asked for AI-native compliance infrastructure; FRTracker now at 994K+ documents with obligation extraction but no workflow layer; Isora GRC targets GLBA Safeguards Rule, not FR obligation→task→evidence for fintech lenders)
- B2B Monetisation:    17/20  (unchanged — community banks and fintech lenders already pay six figures in fines and consultants; $399–799/mo is cheap)
- Pull Factor:         11/20  (unchanged — compliance communities share tools quietly; not LinkedIn-viral)

**Strengths:**
- FRTracker now at 994K+ Federal Register documents, 933K+ extracted obligations, 26-state coverage — the free primitive is growing, confirming the upstream data layer exists; the missing layer is still workflow.
- YC's Fall 2026 RFS validates the category; enterprise RegTech (CUBE, AscentAI, FinregE) still starts at six figures.
- Isora GRC covers GLBA Safeguards Rule §314.4 specifically — not the FR obligation→Jira/Asana workflow for fintechs and community banks across all agencies.

**Risks:**
- FRTracker adds Slack/Jira webhook and eats the core wedge.
- Wrong obligation mapping creates legal liability; product must be "monitoring," not advice.
- Mid-market fintech buyer count is smaller than it looks.

**Verdict:** Hold. FRTracker still a research primitive; obligation→task→evidence workflow for US depository / fintech lending remains unclaimed.

### The Pitch
**Problem:** A four-person compliance team at a community bank or fintech lender tracks Federal Register changes in a shared spreadsheet and a Slack channel of PDFs. FRTracker (free) now extracts 933K+ individual must/shall obligations from 994K+ documents with daily updates and state-level coverage — but it is a research tool, not a system of record. When a final rule drops, nobody owns the checklist, and the exam asks for evidence that does not exist. Enterprise RegTech (CUBE, AscentAI, FinregE) sells this to Tier-1 banks. Isora GRC serves GLBA Safeguards Rule compliance specifically. The 4-person compliance team at a 50-person fintech lender has no affordable, workflow-oriented option.

**Solution:** RuleFlow turns each relevant obligation into a task with an owner, a due date, and an evidence slot. It watches the agencies you care about, diffs proposed vs final, and opens Asana/Jira items mapped to the source passage. At exam time you export a folder: rule, obligation, who did what, attached proof.

**Target customer:** CCO / compliance analyst at a 20–200 person US fintech lender, community bank, or payments firm. Not a broker-dealer mega-firm. Buyer: CCO or General Counsel. Users: the 2–6 people who currently paste Federal Register links into Slack.

**Why now:** YC's Fall 2026 RFS (23 Jul) asked for AI-native compliance infrastructure that maps activities to rules, filings, and evidence. FRTracker (free public research tool, not commercialised) covers the data layer; the mid-market workflow layer does not exist. Enterprise RegTech still starts at six figures.

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
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** The primitive is free and growing (994K+ documents as of August 2026); the unpaid job is workflow + evidence, which is exactly what a 4-person team will pay for.
**Open question:** Will FRTracker itself add "send to Jira" and eat the wedge?

---

## #3 — ModelReg  ·  72/100  ·  NEW
First added: 2026-08-28 | Last updated: 2026-08-28 | Score delta this week: +72

> Turn your SR 26-2 AI model inventory from a stale spreadsheet into an exam-ready system — before the FDIC examiner asks.

### Score Breakdown
- Solo Buildability:   16/20  (CRUD inventory + email reminders + PDF board deck; no ML, no real-time data feeds; clearly shippable solo in 3 months)
- Value Clarity:       14/20  (exam deficiency finding is the trigger; "the examiner didn't see your evidence folder" is a 10-second pitch to a CCO who just received one)
- Market Timing:       15/20  (SR 26-2 / OCC Bulletin 2026-13 issued April 17, 2026; examiners asking about AI governance now; AegisAI sells templates only — $99–247 one-time; their SaaS Evidence Tracker is planned but not launched)
- B2B Monetisation:    14/20  ($149–399/month; community banks pay $50–500/month for ABA/ICBA compliance subscriptions; willingness established)
- Pull Factor:         13/20  (community banker networks share tools; ICBA + ABA conference distribution; exam-finding stories travel within state banking associations)

**Strengths:**
- AegisAI Compliance confirmed as templates-only ($99 Starter Kit, $247 Full Kit, one-time purchase) — their planned Evidence Tracker SaaS is "being built" per their site, not yet launched. The workflow SaaS gap is confirmed.
- SR 26-2 / OCC Bulletin 2026-13 (April 2026) and the free AegisAI gap calculator together create the "exam finding → awareness → purchase" funnel without any outbound sales.
- 5,000+ community banks and credit unions in the $100M–$5B asset range; CIMCON and enterprise MRM vendors price at $20K+/year, leaving this tier completely underserved.

**Risks:**
- AegisAI launches their planned Evidence Tracker SaaS at <$200/month — direct kill signal.
- Core banking vendors (FIS, Jack Henry, Fiserv) add AI governance modules — distribution kill signal.
- Scope creep into model validation consulting creates legal liability; tool must be "inventory and documentation," not "validation."

**Verdict:** Enter as the workflow SaaS layer AegisAI's templates assume exists. Free gap assessment as lead magnet; paid SaaS for ongoing inventory + evidence + board reporting.

### The Pitch
**Problem:** Since April 2026, SR 26-2 and OCC Bulletin 2026-13 require US community banks and credit unions to maintain documented AI model inventories — who owns each model, its risk tier, use case, approval status, validation schedule, and board-reporting evidence. These institutions have 0–2 compliance staff. AegisAI Compliance sells one-time editable template kits ($99–247): you fill out a spreadsheet, and the spreadsheet immediately starts going stale. No owner alerts, no validation schedule reminders, no board report generator, no evidence trail. Their own SaaS Evidence Tracker is listed as "being built." CIMCON and established MRM vendors price at enterprise levels for Tier-1 banks. The 5,000 community banks in the $100M–$5B asset tier have no purpose-built, affordable, ongoing workflow tool.

**Solution:** ModelReg is the AI model inventory and governance workflow for community banks. Each AI system — credit-scoring models, fraud detection tools, employee-use AI apps, vendor AI tools — gets an entry: owner, risk tier, use case, approval status, last validated date, next review date, and evidence attachments. When validation is overdue, the owner gets a reminder. When the board meeting approaches, ModelReg generates a one-click board deck insert: model count, risk tiers, open items, examiner-ready summary. At exam time, the compliance officer exports a folder — not a spreadsheet — mapping each SR 26-2 expectation to evidence on file.

**Target customer:** BSA officer / compliance manager / CIO at a US community bank or credit union with $100M–$5B in assets. 1–3 compliance staff. Not a Tier-1 bank. Not a fintech with a dedicated model risk team. Buyer: compliance officer or CIO. User: compliance analyst who maintains the model register and prepares board materials.

**Why now:** SR 26-2 and OCC Bulletin 2026-13 were issued April 17, 2026. Examiners are already asking community banks about AI governance in fall 2026 exam cycles. AegisAI's own free calculator identifies "AI vendor inventory is incomplete" as the #1 gap — but their product sells you a spreadsheet template, not a live system. The window to be the SaaS workflow layer on top of this validated pain is confirmed open.

**Why they buy without being sold to:** A compliance officer who just received an FDIC exam report noting "AI governance documentation was incomplete and lacked owner assignments and validation schedules" buys ModelReg the same week. The examiner's finding writes the product pitch. No demo, no cold email needed.

**Revenue model:** $149/month (1 institution, 25 model entries, board deck generator, email reminders). $249/month (unlimited models + evidence vault + validation schedule tracking). $399/month (multi-entity: bank + holding company + subsidiaries + SSO). Annual −2 months. 14-day trial. Free SR 26-2 gap assessment (lead magnet, same concept as AegisAI's free calculator but software-connected, not template-driven).

**Unfair advantage:** Free SR 26-2 gap assessment as lead magnet with direct upgrade path to live SaaS system (vs. AegisAI's template kit that disconnects after purchase). First-mover in workflow (not templates) for SR 26-2 community bank AI governance. Distribution through ABA, ICBA, and state banking association conferences where compliance peers share tools actively.

### Solo Build Plan
1. Weeks 1–3: AI model inventory form (owner, risk tier, use case, vendor, approval status, last validated, next review date); dashboard view; CSV import from existing spreadsheets.
2. Weeks 4–5: Automated email reminders for overdue validation reviews and upcoming review dates; role-based access (compliance officer, board viewer, auditor).
3. Weeks 6–7: Evidence upload per model entry; FDIC/Fed/NCUA examiner export pack (ZIP with model list + evidence mapping + validation status); audit log of all changes.
4. Weeks 8–9: Board deck insert generator (risk tier distribution chart, validation status summary, open items list, quarterly update narrative); Stripe; free gap assessment tool as lead magnet.
5. Weeks 10–12: Pilot 5 community banks via ABA Community Banker newsletter outreach, ICBA membership directories, and LinkedIn compliance groups.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-08-28
**Strongest part:** AegisAI sells templates that prove willingness to pay — but their SaaS Evidence Tracker is explicitly "being built," confirming the gap. The exam-finding → purchase funnel requires zero outbound sales.
**Open question:** When will AegisAI ship their planned Evidence Tracker SaaS, and at what price point?

---

## #4 — MarkPack  ·  72/100  ·  DECLINED
First added: 2026-08-03 | Last updated: 2026-08-28 | Score delta this week: −1

> Ship Article 50 evidence — chatbot disclosure, C2PA marks, and an audit folder — before the inspector asks.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — C2PA middleware + disclosure snippets + evidence ZIP)
- Value Clarity:       16/20  (unchanged — AI Office complaint form is live; "show me Art. 50 proof" is a real ask from legal)
- Market Timing:       16/20  (−1 — enforcement started Aug 2, 2026 but zero fines or formal actions as of Aug 21; market timing confirmed but enforcement momentum not yet building; Dec 2 grace period still the forcing function)
- B2B Monetisation:    14/20  (unchanged — $199–499/mo for genAI product teams shipping EU-facing content)
- Pull Factor:         12/20  (unchanged — compliance buyers; eng Twitter/GitHub for SDK)

**Strengths:**
- Art. 50 enforcement legally active since Aug 2; complaint channel is open and public can file on any EU-facing chatbot in minutes. Zero fines as of Aug 21 is not "no enforcement" — it is the pre-enforcement window where the first case is still forming.
- Dec 2 grace for machine-readable marking (Art. 50(2)) creates a concrete 3-month deadline for teams who shipped before Aug 2 without watermarks — the most urgent wedge is this specific sprint.
- Obligation→artifact mapping + CI fail-on-missing-marks is a solo-shaped wedge vs consulting slideware.

**Risks:**
- Zero enforcement actions as of Aug 21 weakens "buyer urgency" — some engineering leads will say "nobody has been fined yet, we'll wait."
- Platform-native C2PA (Adobe, model providers) could commoditize marking.
- Demand may cliff after Dec 2 grace if enforcement remains weak.

**Verdict:** Stay on engineering evidence pack + CI, positioned as the Dec 2 compliance sprint — not a long-term ongoing monitoring tool if enforcement stays quiet.

### The Pitch
**Problem:** From 2 August 2026, EU AI Act Article 50 transparency duties apply and are enforceable. Chatbots must disclose AI interaction; generative systems need machine-readable marking (C2PA-class) — with a grace period to 2 December 2026 for systems already on the market before 2 August (EC FAQ / Omnibus). As of 21 August, zero formal enforcement actions have been issued — but the complaint channel is open, and any competitor or consumer can file against a non-compliant chatbot in minutes. Mid-market product teams have Notion checklists, not an evidence folder an auditor can open: disclosure screenshots, marking pipeline config, role owners, and change logs.

**Solution:** MarkPack is the technical compliance kit: drop-in disclosure components, C2PA/content-credential marking in the generation path, and a one-click evidence pack (ZIP/PDF) mapping each Art. 50 obligation to proof. Built for eng + legal together — not consultants selling slideware.

**Target customer:** Eng lead + counsel at 15–150 person companies shipping EU-facing chatbots or generative content (SaaS, media, agencies). Buyer: CTO/GC. Users: eng implementing marks + compliance owning the evidence folder.

**Why now:** Obligations are live as of 2 August 2026; the Dec 2 marking grace is a 3-month sprint window for teams who shipped before August without watermarks. Zero enforcement actions as of Aug 21 is the calm before the first case — which regulators have stated they are actively monitoring for.

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
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** Dec 2 grace creates a concrete sprint window; complaint channel is live and public.
**Open question:** Will buyers wait for the first actual Art. 50 fine before investing in evidence packs, shrinking the addressable sprint window?

---

## #5 — AdvisorAlert  ·  71/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-08-28 | Score delta this week: −3

> Catch compliance gaps before the SEC exam does — continuous monitoring built for independent RIAs, not mega-firms.

### Score Breakdown
- Solo Buildability:   12/20  (unchanged — email scanning in regulated context; SEC API access; false-positive management)
- Value Clarity:       17/20  (unchanged — SEC deficiency letter = immediate pain trigger; CCO who received one understands the product in 10 seconds)
- Market Timing:       13/20  (−3 — RegFin has emerged as an all-inclusive micro-RIA compliance SaaS: archiving + CRM + scheduling + AI email monitoring + MCP server integration at a single all-inclusive price for smaller firms; this directly competes with the micro-RIA beachhead claim)
- B2B Monetisation:    17/20  (unchanged — $299–799/month vs $5K–20K/year compliance consultant)
- Pull Factor:         12/20  (unchanged — RIA compliance community; word-of-mouth through custodian networks)

**Strengths:**
- Hadrius $22M Series A (July 2026, CRV) still validates the RIA compliance automation category. Hadrius targets 1–5,000+ user firms but is complex and expensive.
- RegFin's emergence confirms the micro-RIA SaaS category is viable — but RegFin's breadth (archiving + CRM + scheduling + compliance calendar + AI email monitoring all-inclusive) is harder for a solo founder to match.
- RIAs already pay $5K–20K/year for compliance consultants; $3,600/year automated monitoring remains a clear value comparison.

**Risks:**
- RegFin competes directly on the micro-RIA ($50M–$500M AUM) beachhead with all-inclusive pricing that bundles archiving, CRM, and email monitoring together.
- False positives in email flagging erode trust in a regulated, high-stakes environment.
- AdvisorAlert's positioning as "monitoring tool, not compliance advice" requires careful ToS and legal review.

**Verdict:** Narrow further — lead with compliance calendar as a free standalone tool (RegFin charges for this), then upsell email monitoring. Differentiate on simplicity vs RegFin's breadth.

### The Pitch
**Problem:** Independent registered investment advisors with $50M–$500M AUM typically have 1–5 employees, no dedicated CCO, and rely on an annual compliance consultant for $5,000–$20,000/year. The SEC expects continuous monitoring: reviewing client communications for solicitation violations, sampling marketing content, confirming trades match investment policy statements, maintaining a current compliance calendar. Hadrius validated the category with a $22M Series A — but targets firms with hundreds of employees. RegFin provides broader all-inclusive compliance for smaller firms — but bundles archiving, CRM, scheduling, and AI email monitoring together, making it more complex to adopt than a 1-person RIA needs. The 1–5 person RIA shop that just wants a compliance calendar plus basic email flagging has no simple, affordable, focused entry point.

**Solution:** AdvisorAlert starts with a free compliance calendar (Form ADV due dates, custody rule filings, code of ethics deadlines) that requires zero email connection. When you're ready, add email monitoring: connect Gmail or Outlook, sample 50 client communications per month, and flag language that could constitute testimonials, solicitations, or performance guarantees. The weekly digest is your CCO's to-do list — not a 200-page manual.

**Target customer:** Principal / de-facto CCO at a 1–5 person RIA, $50M–$500M AUM, serving retail or HNW clients on Schwab, Fidelity, or Pershing. Not a broker-dealer, not a family office. Buyer: the principal who is also the CCO.

**Why now:** RegFin's all-inclusive pricing confirms the micro-RIA SaaS market is real — but RegFin's breadth (CRM + archiving + scheduling + AI email) creates a complexity tax that a simpler, focused tool avoids. The SEC's 2026 risk alert cited inadequate communication surveillance as the top deficiency in small RIAs.

**Why they buy without being sold to:** An RIA principal who received an SEC deficiency letter for "inadequate email review" last year starts a free AdvisorAlert calendar trial, connects their inbox, and sees their first flagged communication within 5 minutes. No pitch required.

**Revenue model:** $299/month (email sampling for 1 inbox, compliance calendar, 12 framework checks). $499/month (3 inboxes + marketing content review). $799/month (unlimited + trade surveillance). Annual −2 months. Free compliance calendar as lead generation entry point.

**Unfair advantage:** Free compliance calendar (Form ADV, custody rule, code of ethics deadlines) sized for the 1–5 person shop that RegFin bundles into a paid plan. Distribution through Schwab Advisor Services and Fidelity Institutional partner programs.

### Solo Build Plan
1. Weeks 1–2: Free compliance calendar (ADV, custody, code of ethics deadlines) — ship as a stand-alone lead magnet with no email connection.
2. Weeks 3–4: Gmail/Outlook OAuth; email ingestion; AI flag for testimonials, performance guarantees, solicitation language.
3. Weeks 5–6: Compliance calendar integration with email alerts; marketing content review.
4. Weeks 7–8: Stripe; free-calendar → paid-monitoring conversion funnel; legal review of ToS.
5. Weeks 9–12: Pilot 5 micro-RIAs through Schwab advisor network referrals and IAA or NAPFA regional events.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-28
**Strongest part:** Free compliance calendar as lead magnet differentiates from RegFin's all-in-one bundled approach. Hadrius $22M raise validates the category.
**Open question:** Will RegFin's all-inclusive price undercut AdvisorAlert's value proposition before AdvisorAlert builds a meaningful customer base?

---

## #6 — BriefDesk  ·  71/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-08-28 | Score delta this week: −1

> Your Monday morning leadership brief writes itself — pulled from your real CRM, PM, and billing data, not from memory.

### Score Breakdown
- Solo Buildability:   17/20  (unchanged — 3 OAuth integrations + AI synthesis < $0.02/brief)
- Value Clarity:       17/20  (unchanged — CSW Solutions July 2026 documents exact pain: "4-5 hours every Friday")
- Market Timing:       11/20  (−1 — BriefHQ.ai confirmed weekly brief includes pipeline deal digest and revenue metrics summary from CRM+billing data, not just product engineering context; Briefd at $59-99/month serves consultants specifically; HubSpot INBOUND kill signal still pending September 2026)
- B2B Monetisation:    15/20  (unchanged)
- Pull Factor:         11/20  (unchanged — "weekly brief" category noise)

**Strengths:**
- CSW Solutions (July 2026) documents the exact ritual: CRM tab → PM tab → billing tab → paste into Notion doc on Friday afternoon. Product builds itself around a lived pain.
- BriefHQ's target buyer is engineering/product teams (Linear + GitHub + PostHog); BriefDesk's buyer is ops/EA/founder (HubSpot + ClickUp + QuickBooks). Different stack, different buyer.
- AI synthesis cost is < $0.02 per brief; margin structure is exceptional.

**Risks:**
- BriefHQ's agent layer now covers pipeline deal digest and revenue metrics — marginal overlap with BriefDesk if a prospect uses both HubSpot and Linear.
- HubSpot INBOUND (September 2026) is the kill signal — watch for "weekly cross-stack AI narrative summary" announcement.
- 3 OAuth integrations (HubSpot, ClickUp, QuickBooks) = 3 weeks of auth and rate-limit work before any AI prompt engineering.

**Verdict:** Keep through September 2026 INBOUND watch. Rename before launch (avoid "brief" namespace). One more run — if HubSpot announces narrative summary at INBOUND, remove.

### The Pitch
**Problem:** Professional services firms, agencies, and B2B SaaS companies spend 4–5 hours every Friday manually pulling CRM deal updates, project status from their PM tool, and revenue figures from QuickBooks into a leadership brief. One person — usually the ops manager, EA, or founder — reads from three browser tabs and types into a Notion document. The brief costs $200–500 in staff time to produce, arrives late, and is stale by Monday morning. CSW Solutions documented this workflow in July 2026: "someone would export from system A, copy into the report, go to system B, copy into the report — then hope the math is right."

**Solution:** BriefDesk connects to your HubSpot (or Pipedrive), ClickUp (or Asana/Linear), and QuickBooks (or Xero/Stripe) via API and runs automatically every Friday at 4pm. It pulls key metrics — pipeline movement, project status by owner, revenue vs. target — and synthesises them into a readable narrative brief delivered to Slack or email before 5pm.

**Target customer:** Operations lead / EA / founder at a 10–100 person professional services firm, agency, or B2B SaaS company using HubSpot or Pipedrive + ClickUp or Asana + QuickBooks or Xero. Buyer: founder/COO. User: ops lead or EA who currently builds the brief manually.

**Why now:** AI synthesis costs less than $0.02 per brief. HubSpot, ClickUp, and QuickBooks all publish REST APIs. BigIdeasDB 2026 validates manual reporting as the #1 business pain at 33.3% validation rate across 148K+ complaints. BriefHQ serves product/engineering teams; the ops/EA multi-stack brief buyer is distinct and unserved.

**Why they buy without being sold to:** An ops manager who spent Friday afternoon copy-pasting into a leadership report gets a BriefDesk free trial, connects their HubSpot stack, and receives the same brief automatically at 5pm. They do not buy BriefDesk — they just stop cancelling it after the trial.

**Revenue model:** $149/month (1 stack: 1 CRM + 1 PM + 1 billing source; 1 brief/week). $249/month (2 stacks). $399/month (custom templates + Slack delivery + API access). Annual −2 months. 14-day trial with 2 live briefs from real data.

**Unfair advantage:** Vertical templates for agencies, SaaS, and professional services that BriefHQ (product/eng focus) cannot match. Distribution via HubSpot Partner ecosystem and ClickUp Integrations Marketplace.

### Solo Build Plan
1. Weeks 1–2: HubSpot + ClickUp + QuickBooks OAuth; scheduled weekly metric pull; error handling.
2. Weeks 3–4: AI narrative synthesis; Slack + email delivery; brief template builder.
3. Weeks 5–6: Review/annotate workflow; stale-data warnings; week-over-week comparison.
4. Weeks 7–8: Stripe; 14-day trial with 2 live briefs; onboarding wizard with vertical template selection.
5. Weeks 9–12: Pilot 8 agencies and PS firms through HubSpot Partner community + ClickUp Marketplace.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-08-16
**Strongest part:** The CSW Friday ritual is still real; BriefHQ's product/eng focus leaves the ops/EA buyer genuinely unserved.
**Open question:** Will HubSpot announce a "weekly AI narrative summary" at INBOUND September 2026?

---

## #7 — ChurnDetect  ·  70/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-08-28 | Score delta this week: −3

> Find the customers about to leave — 90 days before they tell you — from the support tickets they are already sending.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — Zendesk/Intercom API + AI ticket classification + Slack alerts = 3 months feasible)
- Value Clarity:       17/20  (unchanged — "retrospective demo on your last churned account" is self-closing)
- Market Timing:       11/20  (−2 — Teravictus launched as a direct Zendesk+Slack churn prediction SaaS; SignalHOT covers Salesforce+ServiceNow+Zendesk; Churn360 and Skopx offer AI health scoring from multi-source signals; space is more crowded than July 2026)
- B2B Monetisation:    15/20  (unchanged)
- Pull Factor:         12/20  (−1 — CS AI category noise increasing; churn prediction is now a standard feature claim; retrospective demo still the differentiation)

**Strengths:**
- Retrospective demo ("see the 8 tickets before your last churned account") is a self-closing sales mechanism that neither Teravictus, SignalHOT, nor Skopx specifically uses as a conversion hook — they show you current risk, not why your last churn happened.
- 60% of B2B software buyers regretted their purchase in 18 months (Helply 2026); churn risk is surfaced in tickets months before renewal.
- Gap between enterprise (Gainsight $30K+, ChurnZero $20K+) and nothing for 10–150 seat SaaS remains — Teravictus and SignalHOT appear early-stage.

**Risks:**
- Teravictus positions directly as "Predict churn from support quality for Zendesk" with Slack alerts — essentially the same product promise.
- SignalHOT and Skopx are more comprehensive platforms that include churn prediction alongside upsell signals and health scores.
- Zendesk's "Intelligent Triage" could be extended to account health if enough customers request it.

**Verdict:** Hold on retrospective demo differentiator — it is the one thing Teravictus/SignalHOT don't offer as a trial mechanism. But the competitive window is narrowing. Next run kill signal: Teravictus reaches 50+ public reviews on G2/Capterra.

### The Pitch
**Problem:** B2B SaaS companies discover customer churn risk almost exclusively at renewal time, when the decision is already made. 60% of B2B buyers regretted their purchase in the past 18 months. The warning signals — frustration in tickets, repeated unresolved issues, competitor mentions, escalating response times — are buried in the support inbox. A $50K ARR customer silently decides to cancel three months before renewal; the first official indication is a "not renewing" email.

**Solution:** ChurnDetect connects to your Zendesk or Intercom, reads the past 6 months of support tickets using AI, and classifies each conversation by churn risk language, unresolved issue patterns, feature gaps, and competitive mentions. It generates a weekly list of "accounts at risk" with the specific threads that triggered the flag. The trial hook: "show me the tickets from my last churned account" — the AI runs a retrospective and shows you the signals you missed 90 days before cancellation. CS teams get a prioritised outreach list before accounts are lost.

**Target customer:** Customer success manager / VP CS at 10–150 person B2B SaaS company with 100+ customers. Buyer: VP CS or CRO. Uses Zendesk or Intercom. Does not have Gainsight or ChurnZero. Company runs $1M–15M ARR.

**Why now:** LLMs classify "this is taking way too long to resolve" as churn risk where keyword filters miss it. The cost is now under $0.001 per ticket. Enterprise CS platforms are priced at $20–30K/year, leaving 10–150 person SaaS with no dedicated churn-detection layer.

**Why they buy without being sold to:** A CS manager who lost a $30K account to silent churn runs the free ChurnDetect retrospective on that account's last 8 tickets, sees the risk flags she missed 90 days ago, and purchases immediately.

**Revenue model:** $199/month (up to 500 accounts + Zendesk). $349/month (unlimited + Intercom + Slack alerts). $599/month (unlimited + API + custom taxonomy). 14-day free trial. Annual −2 months.

**Unfair advantage:** Historical retrospective demo that turns the free trial into a self-closing pitch. Vertical risk taxonomies (SaaS-specific, agency-specific) that generic sentiment tools do not have.

### Solo Build Plan
1. Weeks 1–3: Zendesk API connector; 6-month historical ticket ingestion; AI risk classification per thread.
2. Weeks 4–5: Account-level aggregation; weekly digest email + Slack; risk score per account with evidence thread links.
3. Weeks 6–7: Intercom connector; custom risk terms; "at risk" list with flagged quotes.
4. Weeks 8–9: Stripe; retrospective demo generator (5 historical accounts, auto-classified); explicit data consent flow.
5. Weeks 10–12: Pilot 8 SaaS companies through CS leader Slack communities and Product Hunt launch.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** Retrospective demo on a recently churned account is a self-closing conversion mechanism that emerging competitors haven't copied yet.
**Open question:** When does Teravictus reach enough traction that their Zendesk marketplace presence makes it the default choice over a newer entrant?

---

## #8 — AuthTrack  ·  70/100  ·  UNCHANGED
First added: 2026-08-16 | Last updated: 2026-08-28 | Score delta this week: —

> See which prior auths are inside the 7-day / 72-hour clock — and which denials still have no specific reason.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — CSV/fax log + calendar clocks + denial-reason fields; no EHR writeback in v1; HIPAA still applies)
- Value Clarity:       16/20  (unchanged — "this PA blows the CMS clock on Thursday" is obvious to a biller; beancount.io July 2026 confirms practices need a PA decision log to hold payers to the 7-day/72-hour standard)
- Market Timing:       14/20  (unchanged — CMS-0057-F clocks live since Jan 1, 2026; FHIR PA API mandate is Jan 1, 2027; small practices on fax/Excel still the workflow per multiple 2026 guides; Linear Health serves Athena specialty groups, not 2–10 provider fax shops)
- B2B Monetisation:    14/20  (unchanged — $149–299/mo for a billing coordinator's time; one avoided write-off pays for a year)
- Pull Factor:         12/20  (unchanged — biller Facebook groups; not public-viral)

**Strengths:**
- CMS-0057-F operational rules confirmed live January 1, 2026 for MA/Medicaid/CHIP/QHP payers. Specific-denial-reason requirement is binding regardless of submission method (fax, phone, portal, mail).
- beancount.io July 2026: "Build a prior authorization decision log. Track submission date, payer, request type, the deadline that applies, and the actual decision date. If a payer blows past its deadline, you now have a documented compliance issue you can escalate."
- FHIR API mandate (Jan 1, 2027) creates documentation ramp but does NOT require small practices to build FHIR endpoints — obligations sit with payers; small practices benefit from the payer compliance.

**Risks:**
- HIPAA + PHI handling from day one.
- Linear Health or clearinghouses ship a cheap tracker SKU.
- Tiny practices may not pay $149 if they believe "the payer has to comply, not us."

**Verdict:** Unchanged. Regulation is live, the clock-enforcement angle is confirmed by July 2026 guides, and the small practice Excel/fax workflow persists.

### The Pitch
**Problem:** Since 1 January 2026, Medicare Advantage, Medicaid, CHIP, and FFE QHP payers must decide standard prior auths in 7 calendar days and urgent ones in 72 hours, and every denial must include a specific reason. Billing coordinators at 2–10 provider practices still track this in a spreadsheet next to the fax machine. They miss clocks, they cannot prove a vague denial, and they will need a clean log before 2027 MIPS electronic-PA attestation. Staffingly's July 2026 practice guide confirms: practices need a decision log documenting submission date, payer, request type, applicable deadline, and actual decision date to enforce their rights under CMS-0057-F.

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
**Strongest part:** Regulation is already in force; beancount.io explicitly recommends building exactly this log; the buyer is a person with a spreadsheet, not a health-system IT committee.
**Open question:** Will tiny practices pay, or will they wait for their clearinghouse to add a free clock?

---

## #9 — AnnexDesk  ·  67/100  ·  NEW
First added: 2026-08-28 | Last updated: 2026-08-28 | Score delta this week: +67

> Generate, maintain, and co-author your EU AI Act Annex IV documentation — before December 2027 turns it into a fire drill.

### Score Breakdown
- Solo Buildability:   16/20  (structured document editor + versioning + PDF export; similar complexity to a Notion-like tool for a fixed schema; clearly shippable solo in 3 months)
- Value Clarity:       14/20  (requires the buyer to know they have a high-risk Annex III system; once that's established, the need for collaborative Annex IV documentation is obvious to CTOs and GCs)
- Market Timing:       13/20  (Digital Omnibus deferred Annex III deadline to Dec 2, 2027 — 16 months away; moderate urgency for teams building now; OSS CLI tools (annex4-cli, @systima/aiact-docs) exist but no collaborative web SaaS; Credo AI and Holistic AI are broad governance platforms, not Annex IV-specific)
- B2B Monetisation:    13/20  (€199–499/month; EU compliance SaaS charges comparable rates; per-AI-system pricing is intuitive)
- Pull Factor:         11/20  (legal/compliance buyers; EU AI startup community; conference distribution at AI Act events)

**Strengths:**
- Confirmed gap: annex4-cli (OSS CLI), @systima/aiact-docs (npm package), plusultra-tools (GitHub Action) are all developer CLI tools — no collaborative web SaaS for multi-role teams (eng + legal + product) found.
- Per-AI-system pricing model aligns with the buyer's mental model: each Annex III system needs its own documentation project.
- "Model update workflow" creates natural retention: when your AI model changes, AnnexDesk prompts exactly which Annex IV sections need review — preventing documentation from going stale.

**Risks:**
- Credo AI or Holistic AI ships an Annex IV module as a feature of their broader platform.
- Big Four consulting firms (already serving EU AI Act) package template tooling at low/no cost to retain consulting relationships.
- December 2027 deadline means many teams will procrastinate, compressing the actual addressable window to Q3–Q4 2027.

**Verdict:** Enter as the collaborative web workspace for Annex IV documentation — specifically for 15–200 person AI product teams who can't justify Big Four consulting but need more than a CLI tool.

### The Pitch
**Problem:** Providers of high-risk AI systems in the EU must maintain Annex IV technical documentation across 9 sections — training data governance, system architecture, validation history, risk management, human oversight mechanisms, post-market monitoring, and more — kept current for every material model update. The December 2, 2027 deadline (moved from 2026 by the Digital Omnibus) gives teams building now 16 months. OSS tools like annex4-cli and @systima/aiact-docs generate YAML scaffolds from the command line — but a team of 5 (2 engineers, 1 data scientist, 1 legal, 1 product) needs to co-author, version-control, and audit-trail these documents. When a model update occurs, the documentation immediately goes stale and nobody knows which sections changed. EU regulators have confirmed that documentation must be maintained throughout the system's lifecycle — not assembled once before the deadline.

**Solution:** AnnexDesk is a web-based workspace where each high-risk AI system gets a documentation project: 9 Annex IV sections structured as required fields, with inline guidance text from the regulation so users don't tab between a PDF and a form. Engineers fill technical fields, legal fills compliance claims, product fills system descriptions. Every edit is versioned and timestamped. When a model update occurs, AnnexDesk prompts which sections are affected and asks for review. At audit time, export a hash-chained evidence pack: documentation + complete change log + completeness report, mapped to each Annex IV requirement.

**Target customer:** CTO / VP Engineering / legal counsel at a 15–200 person company building EU-facing AI systems in Annex III categories: credit scoring, CV/biometric screening, medical device software, critical infrastructure, employment decisions. Buyer: CTO or General Counsel. Users: engineering + legal + product who co-own the documentation and need a shared system of record.

**Why now:** Teams building Annex III high-risk AI systems need documentation from development day 1 — not 3 months before the December 2027 deadline. Starting late means retroactively reconstructing training data governance and risk assessments that were never logged during development. The Digital Omnibus created the deadline extension; it did not simplify Annex IV's 9-section structure. Early movers establish documentation habits that regulators will reward with faster review.

**Why they buy without being sold to:** A CTO whose GC flags that their credit-scoring AI qualifies as Annex III high-risk searches for collaborative Annex IV tooling. They find OSS CLI tools requiring Python setup, or Big Four consultants charging €50K to "write" docs that should have been maintained all along. AnnexDesk at €299/month is the only collaborative web option.

**Revenue model:** €199/month (1 AI system, 5 users, full 9-section workspace). €349/month (5 AI systems, unlimited users). €499/month (10 systems + SSO + custom retention + API export). Annual −2 months. 14-day trial with one demo system pre-populated with a credit-scoring example.

**Unfair advantage:** Regulatory text embedded inline (users never tab between PDF and form); model update trigger workflow that prevents documentation from going stale; first collaborative web workspace for Annex IV; distribution through GPAI model providers and EU AI startup communities already engaged with the regulation.

### Solo Build Plan
1. Weeks 1–3: Annex IV 9-section form schema with required fields and inline regulatory text; section completeness status indicator; versioned edit history.
2. Weeks 4–5: Multi-user collaboration (shared editing, comments, section ownership assignment); role-based access (eng, legal, product, auditor).
3. Weeks 6–7: Evidence pack export (ZIP with HTML summary + regulatory citations + change log + completeness report); LEGAL_GAP flag for fields requiring human compliance claims.
4. Weeks 8–9: Model update trigger workflow (mark which sections are affected when model version changes); Stripe; demo system pre-populated with credit-scoring example.
5. Weeks 10–12: Pilot 5 AI product teams via EU AI Act Slack communities, GPAI forums, and LinkedIn EU compliance groups.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-28
**Strongest part:** Confirmed gap — no collaborative web SaaS for Annex IV documentation found; OSS tools are CLI/developer-only; the model update workflow creates ongoing retention rather than a one-time documentation event.
**Open question:** Will teams building today start documentation now (creating immediate demand), or procrastinate until 2-3 months before the December 2027 deadline (compressing the selling window to Q3–Q4 2027)?

---

## #10 — AgentPermit  ·  66/100  ·  NEW
First added: 2026-08-28 | Last updated: 2026-08-28 | Score delta this week: +66

> See exactly which of your AI agents can access your production data — and revoke any agent's permissions in one click.

### Score Breakdown
- Solo Buildability:   12/20  (agent registry + permission log + API gateway integration for 3 platforms; more complex than average but v1 can be manual-registry-first with runtime enforcement as milestone 2; feasible in 3 months for v1)
- Value Clarity:       14/20  ("which of your AI agents can write to your HubSpot?" is a clear question with an obvious answer; incident-driven onboarding removes all education)
- Market Timing:       15/20  (Gartner: 40% of enterprise apps embed agents by year-end 2026; State of AI Agents 2026: 46% cite integration as primary challenge; TrustLogix launched enterprise kill-switch 2026 but targets Fortune 500; aMaze/ryanwi require Docker/K8s expertise; SMB-accessible web SaaS gap confirmed)
- B2B Monetisation:    13/20  ($149–399/month; security governance tools routinely charge this range; direct cost-avoidance ROI from preventing agent incidents)
- Pull Factor:         12/20  (AI agent incident stories travel fast on LinkedIn/X; "my AI agent auto-replied to 50 customers" is the incident post that converts; security community shares governance tools)

**Strengths:**
- Confirmed gap: aMaze (OSS, Docker/K8s required), ryanwi/agent-control-plane (Python, complex setup) are not web SaaS; TrustLogix is enterprise; cascadeflow.ai focuses on agent loop optimization, not permission management. No SMB-accessible web dashboard found.
- Incident-driven onboarding ("what happened in your last AI agent incident?") is the strongest "no-sell" pattern in this run — same mechanism as ChurnDetect's retrospective demo.
- Permission score per agent (read-only = low risk; write access to CRM + Stripe = high risk) makes value self-evident without requiring an incident.

**Risks:**
- Zapier ships native agent permission management within 12–18 months as their agentic features mature.
- Manual-registry v1 is only as accurate as what engineers self-report; value is limited before runtime enforcement exists.
- Market of "20–100 person companies running 5–20 AI agents from multiple platforms" may be smaller than it appears — many companies use one platform (all Zapier or all n8n) where native permission controls suffice.

**Verdict:** Enter as SMB-accessible agent permission registry with incident-onboarding hook. Build runtime enforcement for top 3 platforms (Zapier, OpenAI, Claude) in months 2–3. Last seat — monitor Zapier agentic permission roadmap.

### The Pitch
**Problem:** A 30-person SaaS company in 2026 runs 10+ AI agents: a Zapier lead-routing agent, a Claude code reviewer, an OpenAI customer support bot, a Make.com invoice processor. Each was connected to production systems (HubSpot, Stripe, GitHub, Zendesk) by a different team member, with credentials stored in different places. No one has a single view of which agent has what access. With 10 agents and 50 tools, there are 1,500 potential authorization combinations (State of AI Agents 2026). When something goes wrong — a runaway agent auto-replies to 50 customers with incorrect information, or makes unexpected API calls costing $500 — no one can instantly revoke that agent's permissions across all connected systems. TrustLogix provides this for Fortune 500 companies. OSS tools (aMaze, ryanwi) require Docker/Kubernetes expertise. The 20–100 person AI-forward company has no self-serve web option.

**Solution:** AgentPermit is a web dashboard where you register your AI agents and the systems they connect to. Each agent gets a permission card: which tools it can call, which data it can read/write, and a risk score (read-only low risk; write access to production high risk). When you connect via API gateway, AgentPermit enforces permissions at runtime. For teams that can't modify agent code, it operates as a managed registry with Slack alerts when permission scope looks anomalous. One-click revoke cuts an agent's access across all connected systems immediately.

**Target customer:** CTO / engineering lead at a 20–100 person B2B company running 5–20 AI agents from multiple platforms (Zapier, Make.com, OpenAI, Claude, n8n). Not a Fortune 500 with a dedicated AI security team. Not a solo developer building agents from scratch. Buyer: CTO or head of security. Users: engineering team + ops lead.

**Why now:** Gartner predicts 40% of enterprise apps will embed agents by year-end 2026. For 20–100 person companies, this is already here. TrustLogix's launch of an enterprise kill-switch in 2026 validates the need — and simultaneously confirms the Fortune 500 focus that leaves SMBs without a solution. The OSS tools that exist require infrastructure expertise the typical 2-engineer team doesn't have time to deploy.

**Why they buy without being sold to:** After a Zapier agent auto-replies to 50 customers with wrong product information because its HubSpot write permission was unscoped, the CTO opens AgentPermit that afternoon: "paste what your agent did → we configure permission boundaries so it can't happen again." The incident report writes the product pitch.

**Revenue model:** $149/month (10 agents, permission registry, audit log, Slack alerts). $249/month (unlimited agents + API gateway enforcement for Zapier/OpenAI/Claude + one-click revoke). $399/month (SSO + custom policy rules + compliance export for SOC2/EU AI Act). Annual −2 months. 14-day free trial; free Slack audit bot that detects unregistered AI tools in your workspace as lead generation.

**Unfair advantage:** Incident-driven onboarding hook; free Slack audit bot that auto-discovers AI tool mentions in your workspace channels (zero-setup lead magnet); pricing and UX sized for the 20–100 person company that TrustLogix's enterprise motion ignores.

### Solo Build Plan
1. Weeks 1–3: Agent registry CRUD (agent name, owner, connected tools, permission scope, risk score); manual permission update log with timestamps; permission audit digest email (weekly).
2. Weeks 4–5: Slack one-click revoke notification; permission change alerts; free Slack audit bot that detects unregistered AI tool mentions in workspace channels.
3. Weeks 6–7: API gateway integration for 3 platforms (Zapier webhook receiver, OpenAI API key proxy with scope limits, Claude API key proxy); runtime permission enforcement.
4. Weeks 8–9: Stripe; incident-onboarding flow ("describe your last AI agent incident → we configure your permission matrix"); auto-discovery of AI API keys from 1Password/Doppler integration.
5. Weeks 10–12: Pilot 8 AI-forward companies through Zapier Community + AI engineer Slack groups + LinkedIn AI security posts.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-28
**Strongest part:** Incident-onboarding hook is the strongest "no-sell" pattern in this run. The "which of your AI agents can write to your CRM?" question has no good answer at any SMB today.
**Open question:** Will Zapier's native agentic permission controls (likely in 12–18 months) make an external registry redundant before AgentPermit achieves meaningful customer density?

---

## Removed this run
| Entry | Last score | Reason |
|-------|------------|--------|
| TokenBill | 72 → 52 | **Ramp** launched free AI Token Spend Management on July 16, 2026 — connects directly to OpenAI/Anthropic/Cursor/Gemini admin APIs, free standalone tier without requiring Ramp cards. Kill signal confirmed. |
| BreakWatch | 67 → REMOVED | **breakwatch.dev** is a live product at €29/month doing exactly this; **FlareCanary** (continuous monitoring including MCP schemas, free tier), **breaking.watch** (free for 3 services), and **APIShift** all exist for consumer-side API monitoring. Product name collision + saturated market. |
| FlowTrace | 62 → REMOVED | **TrustLogix** (enterprise kill switch + governance platform, 2026 launch), **cascadeflow.ai** (commercial agent loop optimization), **aMaze** (OSS control plane), **tracepath** (OSS FINRA/EU AI Act audit middleware), **ryanwi/agent-control-plane** (OSS, full policy engine). Agent governance space now has both enterprise and OSS coverage. |

## Run 9 candidates evaluated and killed before ever entering cookbook
| Candidate | Planned score | Kill signal confirmed this run |
|-----------|--------------|-------------------------------|
| LienLock | 72 | **BuildPass.ai** ships payment-conditional lien waiver hold with hard-block feature for US GCs — exact differentiator LienLock would have built |
| CertPayroll | 71 | **CertifiedPayrollPro** ($49–149/month, $0 setup, free trial, no contract) and **LCPcertified** ($145/month for up to 5 active projects) already serve small trade contractors affordably |
