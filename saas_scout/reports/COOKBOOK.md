# SaaS Opportunity Cookbook
Last updated: 2026-11-06 | Entries: 10/10

> **Run 19 (2026-11-06) summary:** SRP v1.3 on Nov 4 strengthens CRAReport (+1). WorkAuditAI hits peak urgency with Jan 1, 2027 deadline 8 weeks out (+2). Two new entries: **FieldSyncQBO** (78, field-service ↔ QBO reconciliation, GripeVote #1 pain cluster Oct 2026) and **DocParity** (71, docs-code drift enforcement, EchoSift pain score 114). Two entries removed: **ModelReg** (no community bank exam signals, two consecutive runs; OCC explicitly excludes gen AI from SR 26-2 scope) and **StackClean** (Substly confirmed with both Google Workspace and Microsoft Entra ID native integration, shadow IT browser extension, and SSO at €95/month — kills the SSO-integration moat). AuthTrack −5 (Adulis Health launches for 5-100 provider practices), CredVerify −5 (Rivon Health launches at $39-$1,499/month).

---

## #1 — CRAReport  ·  85/100  ·  IMPROVED
First added: 2026-09-18 | Last updated: 2026-11-06 | Score delta this week: +1

> Pre-fill ENISA's CRA reporting form from your SBOM — before the 24-hour clock runs out at 3am.

### Score Breakdown
- Solo Buildability:   17/20  (SBOM ingest + vulnerability match + SRP form pre-fill + deadline tracker; no EHR complexity; ENISA SRP v1.3 field schema is public)
- Value Clarity:       20/20  (no submission API = every notification is typed by a human at 3am; "pre-fill the ENISA form in 90 seconds" is a 10-second pitch)
- Market Timing:       20/20  (SRP v1.3 on Nov 4, 2026 — 4th version update in 54 days; Dec 11, 2027 open-source steward wave incoming; competitors all say "you file it yourself")
- B2B Monetisation:   15/20  ($199-499/month; EU manufacturers are trained to pay for compliance tooling; 10,000+ CRA-obligated companies)
- Pull Factor:         13/20  (CRA community on LinkedIn/ENISA working groups; cybersecurity Twitter after a 24h miss; not mainstream viral)

**Strengths:**
- ENISA explicitly stated "no API at initial release" and v1.3 still ships without one — four version updates proves the platform is actively maintained but the API gap is structural, not an oversight.
- BitHive Reporting Desk, OSPulse, and CVD Portal all focus on SBOM monitoring and vulnerability detection; ALL explicitly state "you submit yourself" — the form pre-fill + secondary representative coordination + deadline tracking gap is unowned.
- Multi-product SRP account management (Primary/Secondary Assigned Representatives, one-report-many-products) is documented pain with no tooling solution.

**Risks:**
- ENISA publishes an API in Q1 2027; the core value proposition collapses overnight.
- BitHive or OSPulse adds SRP form pre-fill, closing the gap.
- EU manufacturer count is finite; market is primarily B2B but requires EU-law knowledge to serve credibly.

**Verdict:** Hold #1. SRP v1.3 on Nov 4 adds a Secondary AR invitation workflow change — another form schema update that every manufacturer must track manually. The gap is structural.

### The Pitch
**Problem:** From 11 September 2026, EU manufacturers of products with digital elements must notify ENISA's Single Reporting Platform within 24 hours of becoming aware of an actively exploited vulnerability, with a 72-hour detailed notification and a 14-day final report. ENISA's SRP v1.3 (released 4 November 2026) is the fourth schema update in 54 days. There is no submission API; every notification is typed into a web portal by a named individual with an EU Login account and MFA. If the platform is down, ENISA says to wait and retry — the 24-hour clock does not pause. A manufacturer running 20 products with 5 teams has no tool to coordinate: who is the Secondary AR, which form schema version applies, which deadline is red?

**Solution:** CRAReport ingests your product SBOMs (CycloneDX or SPDX), watches CISA KEV and ENISA EUVD for active exploitation matches, starts the legal clock when a match fires, and pre-fills the ENISA SRP notification form in the current field-schema version. Submission is still manual — no API exists — but the person filing gets a 90-second pre-fill instead of a 20-minute form hunt at 3am. Secondary AR assignments, form version history, and per-product deadline status are tracked in one dashboard.

**Target customer:** Information security lead / product compliance manager at a 15-200 person EU software manufacturer or IoT hardware maker with 1-30 products covered by the CRA. Buyer: CISO or Head of Product Compliance. Users: the 1-3 people who currently hold Primary or Secondary AR roles in ENISA's portal.

**Why now:** CRA Article 14 obligations took effect 11 September 2026. ENISA explicitly confirmed: "no API will be provided at the initial release." The SRP schema has changed four times in 54 days (v1.0 → v1.1 → v1.2.1 → v1.3). Every schema change means every pre-built form template becomes wrong. No tool tracks this automatically. The window between obligation start and competitive market formation is open now.

**Why they buy without being sold to:** A security engineer who missed the first 24-hour window because she was searching for the right ENISA form field gets CRAReport, pre-fills the next notification in 90 seconds, and locks in the Secondary AR for backup. She does not evaluate alternatives because the next 24h window does not wait.

**Revenue model:** €199/month (1 product, 3 users, automated exploitation watch, deadline dashboard). €349/month (10 products, 10 users, Slack/Teams alerts). €499/month (unlimited products, multi-entity, AR delegation management, evidence export pack). Annual −2 months. 14-day trial with sample SBOM import.

**Unfair advantage:** Schema version tracking — every ENISA SRP update is parsed and form pre-fill is updated within 24 hours, before any manufacturer's internal template is refreshed. Distribution through EU cybersecurity law firm newsletters and CRA working groups at ENISA and CEN-CENELEC.

### Solo Build Plan
1. Weeks 1-3: SBOM ingest (CycloneDX JSON, SPDX JSON); CISA KEV + ENISA EUVD daily match; 24h/72h/14d clock engine per finding.
2. Weeks 4-5: SRP v1.3 form pre-fill (all required fields, field-length limits, copy-to-clipboard per field); Secondary AR assignment + notification.
3. Weeks 6-7: Multi-product dashboard; schema version change alert (diff previous vs current field set); evidence pack export (finding + product + submission timestamp).
4. Weeks 8-9: Stripe; ENISA EU Login onboarding guide; sample-SBOM trial wizard.
5. Weeks 10-12: Pilot 6 EU software manufacturers via CRA Slack community + EU cybersecurity law firm referrals (Fieldfisher, NautaDutilh, Hogan Lovells EU Tech practice).

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-11-06
**Strongest part:** Four SRP schema updates in 54 days proves this is a living, evolving obligation — not a one-time setup. Schema version tracking is a durable moat that gets stronger, not weaker, over time.
**Open question:** Will ENISA publish an API roadmap at the December 2026 CRA stakeholder meeting? Any public date = kill condition. Monitor enisa.europa.eu/news.

---

## #2 — WorkAuditAI  ·  82/100  ·  IMPROVED
First added: 2026-09-11 | Last updated: 2026-11-06 | Score delta this week: +2

> Prove your CA workplace AI is compliant before January 1 — the audit log HR can't improvise.

### Score Breakdown
- Solo Buildability:   15/20  (AI tool inventory + policy templates + disclosure generator + human corroboration workflow documentation; no EHR/FHIR complexity; CA employment law is well-documented)
- Value Clarity:       19/20  (Jan 1, 2027 is 8 weeks away; "is AB 1883 in force at your company?" has a one-line answer; EmployArmor confirmed not covering these laws)
- Market Timing:       20/20  (8-week deadline; DLA Piper + King & Spalding published in Nov 2026; EmployArmor FAQ explicitly covers CCPA ADMT only; no HRIS vendor module shipped)
- B2B Monetisation:   15/20  ($299-699/month; HR/employment counsel budget; compliance spend easy to justify vs. $500-$7,500 per violation)
- Pull Factor:         13/20  (5 employment law firms distributing CA workplace AI advisories; LinkedIn HR community shares compliance tools)

**Strengths:**
- EmployArmor confirmed in their own FAQ as covering CCPA ADMT + AI hiring laws only — SB 947, AB 1883, SB 951, and AB 1331 are confirmed unserved. DLA Piper and King & Spalding published November 2026 advisories confirming the four new CA workplace AI laws are distinct from CCPA ADMT.
- Jan 1, 2027 effective date for AB 1883 (neural data/emotion recognition), AB 1331 (bathroom surveillance), and SB 951 (Cal-WARN AI displacement disclosure). SB 947 (No Robo Bosses Act) effective July 1, 2027.
- Five major employment law firms (Seyfarth Shaw, Hunton Andrews Kurth, Hirschfeld Kraemer, King & Spalding, DLA Piper) are actively publishing employer guidance = zero-CAC distribution channels.

**Risks:**
- EmployArmor expands FAQ to cover the four new CA workplace AI laws (KILL CONDITION).
- ADP or Workday ships a "CA AI Workplace Compliance" module in a December product update.
- CA employers challenge the new laws; a TRO delays enforcement and buyers stop urgency purchasing.

**Verdict:** Hold #2. Jan 1 deadline is 8 weeks away and EmployArmor is confirmed as not covering these laws. This is the peak urgency window.

### The Pitch
**Problem:** On September 30, 2026, California signed four AI workplace laws: AB 1883 (prohibits neural data collection and AI emotion recognition in the workplace, effective Jan 1, 2027), AB 1331 (restricts bathroom surveillance, effective Jan 1, 2027), SB 951 (requires Cal-WARN technology displacement disclosures, effective Jan 1, 2027), and SB 947 — the "No Robo Bosses Act" (requires human corroboration for AI-driven discipline/termination, effective July 1, 2027). California employers using AI in scheduling, monitoring, discipline, termination, or workforce planning must comply. EmployArmor covers CCPA ADMT and AI hiring bias laws — explicitly not these four. No HRIS vendor has shipped a compliance module. HR teams are reading law firm PDFs and building their own checklists.

**Solution:** WorkAuditAI gives HR teams a structured compliance workflow for all four laws: an AI tool inventory (which tools are used in which employment decisions), a neural data/emotion-recognition tool audit, Cal-WARN disclosure templates for technology displacement events, and a human-corroboration documentation workflow for SB 947. Each law gets a progress tracker, evidence upload, and a deadline alert. The output is an audit-ready compliance folder a law firm can review in 30 minutes.

**Target customer:** HR Director / Employment Counsel at a California-headquartered company with 100+ employees using AI in scheduling, performance monitoring, discipline, termination, or workforce reduction decisions. Buyer: HR Director or General Counsel. Users: HR ops team + inside employment counsel.

**Why now:** Four laws with Jan 1, 2027 effective dates create a 90-day sprint. EmployArmor covers a different law set (CCPA ADMT). HRIS vendors (Workday, ADP, BambooHR) have not shipped compliance modules. Five major employment law firms are actively distributing compliance guides and can refer SaaS tools to their clients.

**Why they buy without being sold to:** An HR director who received a Seyfarth Shaw email advisory about AB 1883 searches for a tool to audit which software vendors collect biometric or emotional-state data. She finds WorkAuditAI, runs the inventory for 3 tools in 10 minutes, and books a demo for the team. No pitch required after the first tool is inventoried.

**Revenue model:** $299/month (1-200 employees, 4 CA law templates, AI tool inventory, evidence upload). $499/month (200-1,000 employees, unlimited tools, Cal-WARN notice generator, SB 947 corroboration log). $699/month (1,000+ employees, multi-entity, law firm export pack, renewal alerts for expiring policies). Annual −2 months. 14-day trial with one law fully walked through.

**Unfair advantage:** First mover in SB 947/AB 1883/SB 951/AB 1331 specific compliance tooling. Law firm distribution (Seyfarth Shaw, Hunton, HKE, K&S, DLA Piper) are all actively publishing employer guides — a referral network that requires no outbound sales. The Jan 1 deadline creates a forcing function that bypasses typical enterprise procurement cycles.

### Solo Build Plan
1. Weeks 1-3: AI tool inventory (vendor, use case, employment decision type, data collected); AB 1883 neural data/emotion recognition tool audit checklist; law-specific progress tracker.
2. Weeks 4-5: SB 951 Cal-WARN tech displacement disclosure template generator (auto-fills required fields: number affected, job functions automated, technology type, express written statement); AB 1331 bathroom surveillance self-audit.
3. Weeks 6-7: SB 947 human corroboration documentation workflow (ADS use flag, human reviewer identity, corroboration evidence fields, employee notification letter template).
4. Weeks 8-9: Stripe; compliance audit pack PDF export (all four laws, evidence attached, law firm reviewable); 14-day trial with AB 1883 audit pre-built.
5. Weeks 10-12: Pilot 8 companies via law firm referral agreements with Seyfarth Shaw and HKE; LinkedIn HR compliance community.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-11-06
**Strongest part:** Jan 1, 2027 is 8 weeks away and EmployArmor's own FAQ confirms they cover different laws. This is the clearest competitor gap in the cookbook.
**Open question:** Will ADP or Workday ship a "CA AI Workplace Compliance" dashboard before January 1? Monitor their December 2026 release notes.

---

## #3 — FieldSyncQBO  ·  78/100  ·  NEW
First added: 2026-11-06 | Last updated: 2026-11-06 | Score delta this week: —

> Stop re-keying Jobber payments into QuickBooks — reconcile field service billing in one click.

### Score Breakdown
- Solo Buildability:   15/20  (Jobber API + QBO API + fee-breakdown rule engine; 3 months is achievable if scoped to Jobber-only first; ServiceTitan's API is enterprise-gated, not v1 scope)
- Value Clarity:       18/20  (any bookkeeper who can't reconcile QBO understands this in 5 seconds; direct $ pain with no explanation needed)
- Market Timing:       16/20  (GripeVote October 2026 names "money that won't reconcile" as #1 complaint cluster across field service SaaS, 8 of 34 complaints; Jobber has mature public API; native QBO sync exists but is clearly broken)
- B2B Monetisation:   15/20  ($149-299/month vs. 4-8 hours of bookkeeper time monthly; clear ROI; field service owners pay for time-back tools)
- Pull Factor:         14/20  (bookkeeper Facebook/Discord groups; Jobber user community forum; QB ProAdvisor referral network; word travels fast among bookkeepers when something saves 4 hours)

**Strengths:**
- GripeVote October 2026 small business complaints: "money that won't reconcile between tools" is #1 cluster (8/34 complaints), naming Jobber, ServiceTitan, and QuickBooks by name.
- Both Jobber and QBO have mature public APIs; the core reconciliation is a data transformation problem, not an AI/inference problem. Accuracy can be verified deterministically.
- Bookkeeper as champion buyer is ideal: they experience the pain weekly, they evaluate tools independently, and they have authority to subscribe without C-suite approval.

**Risks:**
- Jobber ships a "reconcile with QuickBooks" button in a 2027 product update (KILL CONDITION).
- Synder ($49-299/month) already syncs Stripe/Square payments to QBO — if Jobber uses Stripe, Synder may already partially solve this.
- Accuracy below ~95% erodes bookkeeper trust permanently; handling closed-month corrections requires accounting judgment.

**Verdict:** Buy. This is the strongest new opportunity this week — the #1 empirically-validated pain point with a specific buyer, buildable APIs, and a bookkeeper champion who needs no sales pitch.

### The Pitch
**Problem:** Field service businesses running Jobber or ServiceTitan + QuickBooks Online face a weekly reconciliation failure: card payments land in the bank net of processing fees, so the deposit never matches the invoice total. When a closed month blocks a correcting export, or a tiny account-name mismatch kills the reconciliation run, the bookkeeper spends 4-8 hours hunting the discrepancy manually. The October 2026 GripeVote small business complaints survey named "money that won't reconcile between tools" the #1 pain cluster (8 of 34 complaints) — naming Jobber, ServiceTitan, and QuickBooks explicitly. Jobber's native QBO sync exists but does not handle fee breakdowns, write-offs, or closed-period corrections. Synder handles generic Stripe-to-QBO but does not know Jobber's data model (line-item fees by job, lab fees, write-offs, tip allocations).

**Solution:** FieldSyncQBO reads Jobber payment exports and transaction logs, applies per-processor fee-breakdown rules (Jobber uses Stripe; each processor has a specific net-of-fees format), and writes clean, matched entries to QuickBooks Online with correct account names, category codes, and fee contra-accounts. When a transaction cannot be auto-matched (closed month, refund, chargeback), it surfaces the exception with a specific reason and suggested resolution — the bookkeeper approves exceptions, not formulas.

**Target customer:** Bookkeeper + owner at a 2-20 truck HVAC, plumbing, landscaping, electrical, or pest control company using Jobber + QuickBooks Online. Buyer: owner-operator who reviews books monthly. User: the bookkeeper (often fractional, 10-20 hours/month per client) who currently does the monthly reconciliation in a spreadsheet or by hand.

**Why now:** Jobber's public API (released 2024, matured 2025-2026) now exposes payment transactions with full line-item detail. QBO's API supports journal entry writes. The integration infrastructure is now technically feasible for a solo developer. But Jobber has prioritized scheduling and dispatch features over bookkeeping edge cases, and QBO has focused on payroll — leaving the reconciliation seam unowned. GripeVote confirms the gap is unresolved despite years of "native integration" promises.

**Why they buy without being sold to:** A bookkeeper who spent 6 hours last month hunting a closed-period discrepancy in Jobber+QBO is told about FieldSyncQBO by another bookkeeper in the Jobber Community Forum. She imports last month's data, watches 97% of transactions auto-match, and flags the 3 that need attention. She sends a Stripe payment link to the owner that afternoon. No pitch. No demo.

**Revenue model:** $149/month (Jobber + QBO, 1 location, up to 500 transactions). $249/month (Jobber, 3 locations + multi-entity QBO). $399/month (custom fee rules + Slack exception alerts + bookkeeper white-label dashboard). Annual −2 months. 14-day free trial with 60-day historical import.

**Unfair advantage:** Jobber-specific fee reconciliation templates pre-built for Stripe processing (Jobber's default processor) — including the specific net-of-fees format, tip allocation, and write-off reclassification that Synder's generic Stripe connector doesn't know about. QB ProAdvisor referral network as zero-outbound distribution: bookkeepers who specialize in trades clients recommend to their entire client base simultaneously.

### Solo Build Plan
1. Weeks 1-3: Jobber API → transaction + payment export ingest; QBO OAuth; Stripe fee-breakdown rule engine; 97% auto-match algorithm for bank-net-of-fees reconciliation.
2. Weeks 4-5: Closed-period detection and correcting-entry suggestion; account-name normalization (handles common Jobber → QBO naming mismatches); exception surface UI (table of unmatched transactions with reason + suggested fix).
3. Weeks 6-7: QBO journal entry writer (write approved matches directly); Slack exception alerts; 60-day historical import wizard.
4. Weeks 8-9: Stripe payment; 14-day trial with historical import; bookkeeper onboarding flow (not owner onboarding).
5. Weeks 10-12: Pilot 8 field service firms via Jobber Community Forum, QB ProAdvisor directory outreach, and r/QuickBooks bookkeeper communities.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-11-06
**Strongest part:** GripeVote #1 complaint cluster (8/34) is unusually strong empirical evidence — most SaaS ideas rely on surveys or founder intuition, not a ranked complaints dataset from October 2026.
**Open question:** Does Synder's Jobber connector already handle closed-month corrections and Stripe fee breakdowns? If yes, the differentiation narrows significantly. Test Synder's Jobber integration before building.

---

## #4 — DentPay  ·  76/100  ·  DECLINED
First added: 2026-07-16 | Last updated: 2026-11-06 | Score delta this week: −2

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — CSV-first rule engine; OD/Dentrix exports are well-documented)
- Value Clarity:       17/20  (unchanged — OM ritual self-evident; production-% pain clear to any dental office manager)
- Market Timing:       15/20  (−2: dentpay.tech now discoverable in search with polished product page; Warp $20/month AI payroll appears in dentist payroll rankings)
- B2B Monetisation:   16/20  (unchanged — $149-399/month is well below annual CPA compliance cost)
- Pull Factor:         12/20  (−1: more noise in dental payroll space; dentpay.tech is now a named competitor in the same channels)

**Strengths:**
- HRPayPick 2026 confirms: "no payroll platform has native plug-and-play integration with all three major US PMS systems" — Gusto explicitly has no native Dentrix or Eaglesoft integration; ADP integration varies in depth.
- Dental practice payroll is sticky: wrong paycheck = employer liability. Switching cost is existential once pay rules are configured.
- Study club and OD user group distribution provides zero-CAC word-of-mouth among exactly the 1-3 location practices who need this.

**Risks:**
- dentpay.tech (ClinixFlows, Mays Zaitouni) is live with the same CSV-first approach — identical product positioning. Market may not support two players at this price point.
- Dental Intelligence or Dentrix deepens native pay math in a platform update.
- Warp ($20/month AI payroll) is aggressive on price in a space that was previously uncontested.

**Verdict:** Hold but monitor dentpay.tech scale. If dentpay.tech shows funding or Product Hunt traction, reconsider next run.

### The Pitch
**Problem:** US dental practices paying associates and hygienists on production still spend hours each pay period exporting Open Dental or Dentrix reports, pasting into Excel, applying lab fees, write-offs, and card-fee rules, then hoping the spreadsheet matches the contract. Open Dental's Provider Payroll report is raw material, not a pay engine. Gusto deposits pay but does not reconcile OD production rules. HRPayPick 2026 confirms no payroll platform has native plug-and-play integration with all three major US PMS systems (Dentrix, Eaglesoft, Open Dental).

**Solution:** DentPay imports OD/Dentrix production exports, applies per-provider pay rules once, flags anomalies before payout, and exports an approval pack to Gusto/ADP. Office managers review exceptions; they do not rebuild formulas.

**Target customer:** Office manager / owner at 1-3 location US dental practice on Open Dental or Dentrix with associates or hygienists on production splits.

**Why now:** Production % pay still the norm; UK tools (Samera/Dentivize) proved analytics willingness-to-pay; US PMS vendors have not productised the reconciliation layer.

**Why they buy without being sold to:** An OM who spent Sunday fixing a hygienist underpay uploads last month's OD export, sees the same total with three flagged lab mismatches, and refuses to go back to Excel.

**Revenue model:** $149 / $249 / $399 per practice. 30-day trial. CPA referral 15%.

**Unfair advantage:** US OD/Dentrix rule templates + anomaly library; study-club distribution; PE roll-ups won't chase at $149.

### Solo Build Plan
1. Weeks 1-3: OD Provider Payroll CSV ingest; rule builder; pay summary PDF.
2. Weeks 4-5: Anomaly flags; vs last period; Gusto CSV export.
3. Weeks 6-7: Dentrix path; multi-provider approval.
4. Weeks 8-9: Stripe; sample-file onboarding.
5. Weeks 10-12: Pilot 8 practices via dental groups / OD user groups.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-11-06
**Strongest part:** HRPayPick 2026 confirms the integration gap across all three PMS systems. The production-% reconciliation problem is real and recurring.
**Open question:** Has dentpay.tech reached scale (Product Hunt launch, paying customers announced)? Their discoverability in search is now confirmed but paying-customer count is unknown. This determines whether the market supports two players.

---

## #5 — IntegWatch  ·  72/100  ·  UNCHANGED
First added: 2026-10-16 | Last updated: 2026-11-06 | Score delta this week: —

> Know when a customer's integration broke — before they open a support ticket.

### Score Breakdown
- Solo Buildability:   14/20  (webhook health pings + OAuth token expiry detection + per-customer status page; no MCP complexity; 3 months feasible)
- Value Clarity:       15/20  (CS lead who lost a customer to a silent integration failure understands in 10 seconds; needs one sentence of setup)
- Market Timing:       15/20  (unchanged — Deloitte/MuleSoft 2026 Connectivity Benchmark: 957 avg enterprise apps, only 27% integrated, 86% of IT leaders fear agent integration complexity; no Nango/Merge/Apideck native per-customer health alert found)
- B2B Monetisation:   15/20  ($199-499/month; CS/expansion budget; one avoided churn pays for a year)
- Pull Factor:         13/20  (CS communities share "how we reduced integration-related churn" case studies; LinkedIn CS leaders)

**Strengths:**
- Deloitte/MuleSoft 2026 Connectivity Benchmark confirms agent integration chaos (27% of APIs ungoverned, 86% of IT leaders fear complexity without integration). IntegWatch's per-customer health alerting is distinct from internal API monitoring.
- Kill conditions (Nango, Merge, Apideck, Ampersand adding per-customer connection health alerts) have not been confirmed in two consecutive runs.
- The "2026 State of Agentic Integrations" primary signal remains unchallenged.

**Risks:**
- Nango or Merge ships "per-customer integration health dashboard" in a product update (KILL CONDITION).
- The integration monitoring market consolidates around unified API vendors who absorb health monitoring.
- Solo buildability requires maintaining OAuth polling for 20+ integrations without breaking on rate limits.

**Verdict:** Unchanged. No kill signals found. Deloitte/MuleSoft 2026 strengthens the category signal but doesn't change the competitive landscape.

### The Pitch
**Problem:** A 30-person B2B SaaS company maintains integrations with Salesforce, HubSpot, Slack, and QuickBooks for its customers. When a customer's OAuth token expires, their webhook breaks, or their API key is rotated without notice, the integration silently stops working. The first signal is a customer support ticket — often 3-7 days after the break, sometimes after the customer has already decided to churn. The CS team has no proactive view of which customer integrations are healthy. The "2026 State of Agentic Integrations" report found that integration failures are now the #1 cause of unplanned churn for SaaS companies with 5+ outbound integrations.

**Solution:** IntegWatch connects to your SaaS via API, polls per-customer integration health (OAuth token validity, webhook delivery rates, API call success rates), and alerts your CS team in Slack when a specific customer's integration is degrading — before the customer notices. Each alert includes the customer name, the failing integration, the last successful sync, and a suggested fix ("their Salesforce token expired — click to trigger re-auth email").

**Target customer:** VP of Customer Success / Head of CS at a 20-150 person B2B SaaS company with 100+ customers using at least one native integration. Buyer: VP CS or CRO. Users: CS team + integration on-call engineer.

**Why now:** AI agents made stale integration data a first-order problem: an agent that acts on outdated CRM data is not just unhelpful — it's dangerous. The 2026 State of Agentic Integrations report documented that integration-related churn accelerated 40% in 2026 as customers expected real-time data for AI workflows.

**Why they buy without being sold to:** A CS manager who lost a $60K ARR account to a silent Salesforce sync failure runs IntegWatch on her current book of business, discovers 4 customers with expired tokens, reaches out proactively, and prevents at least one churn. She does not need a pitch after that.

**Revenue model:** $199/month (up to 200 monitored connections, 3 integration types, Slack alerts). $349/month (1,000 connections, 10 types, email + Slack). $499/month (unlimited + API access + white-label per-customer health page). Annual −2 months. 14-day trial.

**Unfair advantage:** Per-customer integration health view (not internal API monitoring) is the gap that unified API vendors have not closed because it requires knowing which customer's connection broke, not just which API endpoint is slow.

### Solo Build Plan
1. Weeks 1-3: OAuth token expiry detection for Salesforce, HubSpot, QBO, Slack; webhook delivery health (200/4xx/5xx ratio per customer); customer connection status table.
2. Weeks 4-5: Slack alert with customer name + failing integration + fix suggestion; alert suppression for known maintenance windows.
3. Weeks 6-7: Per-customer health timeline (last healthy, first failed, duration); re-auth email trigger.
4. Weeks 8-9: Stripe; CS team onboarding; customer-side health status page (optional share link).
5. Weeks 10-12: Pilot 8 SaaS companies via CS community Slack and Product Hunt.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-11-06
**Strongest part:** The "proactive vs. reactive" framing is a CS leader's dream — prevents churn rather than explaining it.
**Open question:** Will Nango, Merge, Apideck, or Ampersand add a "per-customer connection health" dashboard in their next major release? This is the single kill condition to watch.

---

## #6 — DocParity  ·  71/100  ·  NEW
First added: 2026-11-06 | Last updated: 2026-11-06 | Score delta this week: —

> Every code change that breaks your API docs gets caught in the PR — not three weeks later in a support ticket.

### Score Breakdown
- Solo Buildability:   15/20  (GitHub App + PR webhook handler + file-linkage rule engine + CI check; standard GitHub App architecture; 3 months achievable)
- Value Clarity:       14/20  (needs one sentence of context — "docs-code drift" isn't instantly obvious; but after one production incident from stale docs, the pitch writes itself)
- Market Timing:       14/20  (EchoSift July 2026 pain score 114 — highest of any developer tool gap tracked — growing 6% in a cooling market; no dominant player in the seam between code review and docs tooling)
- B2B Monetisation:   13/20  ($49-249/month; GitHub Marketplace; developer tool pricing is competitive but PLG via free OSS tier reduces sales overhead)
- Pull Factor:         15/20  (GitHub stars build fast when a tool prevents a production incident; eng Twitter loves "this GitHub Action saved our docs review" posts; Mintlify/Docusaurus communities are active)

**Strengths:**
- EchoSift's July 2026 developer tool pain tracking scored "Inefficient PR Review for Mixed Changes" at 114 — the single highest pain score across all tracked lanes — with volume of 34 and growing at 6% in a market where average pain scores are declining.
- The seam is structurally unowned: code review tools (CodeRabbit, GitHub, Graphite) explicitly scope to code; docs platforms (Mintlify, Gitbook, Readme) don't gate on PRs. Each has decided the gap belongs to the other side.
- Free OSS tier creates a GitHub star moat that compounds without sales effort.

**Risks:**
- CodeRabbit or GitHub Copilot adds "docs weren't updated" to its AI code review suggestions (KILL CONDITION — could happen within months).
- Developer tool monetization at >$49/month requires a compelling paid dashboard beyond the free GitHub Action.
- The linkage rule configuration (which code file maps to which docs file) requires per-repo setup that creates friction in the free-to-paid conversion.

**Verdict:** Add with monitoring. The EchoSift signal is unusually strong and the seam is genuinely unowned. Watch CodeRabbit's changelog for docs-enforcement features.

### The Pitch
**Problem:** Engineering teams at developer-facing companies maintain both source code and documentation in the same repository. When a developer adds a new API endpoint, renames a function, or changes a response schema, the code review happens in the PR. The documentation update — if it happens at all — is reviewed informally by a human or not at all. EchoSift's July 2026 developer tool pain tracking scored "Inefficient PR Review for Mixed Changes" at 114, the highest of any gap tracked, growing 6% in a cooling market. Code review tools explicitly scope to code; docs platforms don't gate on PRs. Neither has claimed the seam. The result: a function is renamed in a PR on Tuesday, the docs still show the old name, a developer builds against the stale docs on Friday, and a support ticket arrives the following Monday.

**Solution:** DocParity is a GitHub App that runs alongside your existing code review. When a PR modifies a source file (function signature, API route, schema export), DocParity checks whether the linked documentation file was also updated in the same PR. Linkage rules are defined once per repo in a YAML config or via Mintlify/Docusaurus auto-discovery. When a code change has no matching docs update, DocParity fails the GitHub Check with a specific, actionable message: "Function getUserById in users/api.ts was modified but docs/api/users.mdx was not updated in this PR." Engineers fix it before merge. The free GitHub Action is the PLG entry point; the paid dashboard shows docs drift over time.

**Target customer:** Eng lead / VP Engineering at a 20-150 person B2B SaaS company with a public-facing API, CLI, or developer-facing product. Company maintains docs in Markdown files in the same repo (Docusaurus, MkDocs, Mintlify, or Readme). Buyer: VP Engineering or Head of DevEx. Users: entire engineering team.

**Why now:** EchoSift's 2026 tracking shows this is the highest-pain unclaimed gap in developer tooling. Mintlify (20K+ customers) and Docusaurus (100K+ repos) provide auto-discovery integration paths that eliminate manual YAML configuration — the technical precondition for a clean PLG experience now exists. GitHub's Checks API (required for PR gating) is stable and well-documented.

**Why they buy without being sold to:** After a production incident where the API docs showed the old response format for two weeks after a code change, the VP Engineering adds DocParity to the CI pipeline. The first failed check surfaces 4 undocumented API changes already in the main branch. She does not want to remove it.

**Revenue model:** Free (open-source GitHub Action, up to 5 linkage rules, community support). $49/month per organization (unlimited rules, Slack alerts on failed checks, PR failure summaries). $149/month (team dashboard: docs drift heatmap, PRs merged without docs update over 90 days, per-engineer docs debt score). $249/month (custom rule DSL, Mintlify/GitBook push sync, priority support). Annual −2 months.

**Unfair advantage:** First-mover in docs-code linkage enforcement. Free OSS GitHub Action builds GitHub star moat. Mintlify and Docusaurus integration partnerships for auto-discovery (eliminates manual YAML setup). The rule DSL pattern ("if src/*.ts changes, check docs/*.md") generates LinkedIn posts that drive organic discovery.

### Solo Build Plan
1. Weeks 1-3: GitHub App scaffold (OAuth, webhook handler); PR file diff parser; linkage rule engine (YAML config: "if src/*.ts changed, check docs/*.md"); GitHub Check API pass/fail.
2. Weeks 4-5: Actionable failure messages per changed function (not just "docs missing" — "function X in file Y has no corresponding docs update"); Mintlify auto-discovery (read Mintlify config to infer doc↔code linkage).
3. Weeks 6-7: Slack notification on failed checks; web dashboard (org-level docs drift: PRs merged without docs update over 90 days; heatmap by engineer).
4. Weeks 8-9: Stripe; free OSS repo Product Hunt launch; GitHub Marketplace listing; Mintlify/Docusaurus community announcements.
5. Weeks 10-12: Pilot 10 companies via GitHub Marketplace + Mintlify community Discord + Twitter/LinkedIn eng lead outreach.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-11-06
**Strongest part:** EchoSift score 114 is the strongest empirical validation for a developer tool gap in this run — unusually specific, volume-backed, and growing in a cooling market.
**Open question:** Does CodeRabbit already detect when a code change requires a docs update? If their AI review surfaces this naturally (even without a formal CI block), the demand shifts from "tool I buy" to "feature I already have."

---

## #7 — AgentAudit  ·  68/100  ·  UNCHANGED
First added: 2026-08-28 | Last updated: 2026-11-06 | Score delta this week: —

> Every AI agent in your org gets a trust score, a permission boundary, and an audit log — before your CISO asks.

### Score Breakdown
- Solo Buildability:   14/20  (MCP server verification + trust registry + GitHub App + org policy engine; agentaudit-dev OSS validates the architecture; CISO dashboard is paid SaaS)
- Value Clarity:       15/20  (security buyer understands "audit log for every agent action" in one sentence; board report is the artifact)
- Market Timing:       14/20  (EchoSift confirms agent tooling demand growing 7%; agentaudit-dev "free forever" creates trust data moat; paid SaaS tier permanently open)
- B2B Monetisation:   13/20  ($299-699/month; security budget exists; CISO dashboard + org policy is a recurring spend)
- Pull Factor:         12/20  (security Twitter after an agent incident; not publicly viral but travels in CISO networks)

**Strengths:**
- agentaudit-dev "free forever" OSS commitment creates a trust data moat: every free user is a future paid customer referral and a source of agent behavior patterns.
- Distinct from MCPDock (#8): AgentAudit is security/trust (what did the agent do, is it trustworthy, what are its permissions), MCPDock is operations/registry (what servers exist, are they healthy, is the schema valid).
- EchoSift autumn 2026 confirms agent security category growing 7% in developer tools.

**Risks:**
- agentaudit-dev reverses its "free forever" commitment and launches a commercial tier that competes directly with the paid SaaS.
- Anthropic or OpenAI ship native cross-agent audit logs in their enterprise dashboard.
- The "CISO needs an AI agent report" use case turns out to be a consulting engagement, not a SaaS purchase.

**Verdict:** Unchanged. No new kill signals. Category demand confirmed growing. Paid SaaS tier (GitHub App + org policy + CISO dashboard) remains open.

### The Pitch
**Problem:** Companies in 2026 deploy AI agents from multiple platforms: Cursor agents, Claude-based GitHub reviewers, Zapier automation agents, OpenAI Assistants. Each operates with its own permissions, its own tool access, and its own decision history. When an agent takes an unexpected action — sending an email to the wrong list, writing to production data, making an API call that costs $500 — no one can reconstruct what it was permitted to do, what tools it had access to, or what triggered the action. CISOs are receiving board-level questions about AI agent governance that they cannot answer.

**Solution:** AgentAudit gives every AI agent a trust score, a declared permission boundary, and a tamper-evident audit log. It integrates as a GitHub App (for code-generating agents) and as an MCP server verification layer (for tool-using agents). Org-level policy rules define which agents are permitted to call which tool categories. The CISO dashboard shows board-ready summaries: agents deployed, permission boundaries, flagged deviations, and incident history.

**Target customer:** CISO / Head of Security at a 20-200 person company deploying 3+ AI agents in production. Buyer: CISO or VP Engineering. Users: security team + engineering leads who own agent deployments.

**Why now:** Agent sprawl accelerated in 2026 as every major platform shipped an agent feature. CISOs have no audit framework for AI agents specifically — existing SIEM tools capture API calls but don't understand agent intent, permission boundaries, or tool-use patterns.

**Why they buy without being sold to:** After an agent sends a customer-facing email with wrong product information, the CISO uses AgentAudit's free tier to audit what that agent was permitted to do. The free audit report surfaces 2 other agents with overly broad permissions. She buys the CISO dashboard to bring that report to the board.

**Revenue model:** Free (agentaudit-dev OSS; trust registry for up to 5 agents; public audit log). $299/month (GitHub App + org policy enforcement + alert on permission deviation). $499/month (MCP server verification + CISO dashboard + board report PDF). $699/month (unlimited + SSO + SIEM integration). Annual −2 months.

**Unfair advantage:** Trust data moat from agentaudit-dev free users; MCP server verification is distinct from and complementary to MCPDock's registry; first-mover CISO dashboard for AI agent governance.

### Solo Build Plan
1. Weeks 1-3: Trust registry (agent ID, declared permissions, tool access list); MCP server verification (schema validation, permission boundary check); agentaudit-dev OSS release.
2. Weeks 4-5: GitHub App (flag code-generating agents; audit PR actions); org policy rule engine (allow/deny tool categories per agent type).
3. Weeks 6-7: CISO dashboard (agents deployed, permission deviations, incident log); board report PDF generator.
4. Weeks 8-9: Stripe; SIEM integration (Splunk/Datadog webhook); alert on permission deviation.
5. Weeks 10-12: Pilot 6 security teams via CISO networks and Anthropic Builder Community.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-11-06
**Strongest part:** "Free forever" OSS builds a trust data moat that grows without sales effort. The agentaudit-dev community is the pipeline.
**Open question:** Will Anthropic or OpenAI ship a native cross-platform agent audit log in their enterprise tier by mid-2027? This is the CISO's preferred outcome (vendor-native) vs. a third-party tool.

---

## #8 — MCPDock  ·  67/100  ·  DECLINED
First added: 2026-10-23 | Last updated: 2026-11-06 | Score delta this week: −2

> One managed registry for every MCP server in your org — with schema validation, health checks, and an approved-catalog API.

### Score Breakdown
- Solo Buildability:   14/20  (MCP Registry API spec + health check endpoints + schema validation + managed hosting; OSS (ToolHive) validates the architecture; no Kubernetes required for the managed SaaS version)
- Value Clarity:       15/20  (Databricks $499K/year silent retry case study from loose JSON schema = 10-second pitch; "stop paying for bad schema validation" is obvious)
- Market Timing:       14/20  (−1: Warpgate launches as managed MCP gateway with real-time health monitoring, per-tool latency, and 30-day uptime history; Stacklok ToolHive still self-hosted/Kubernetes-only; primary kill condition NOT met)
- B2B Monetisation:   14/20  ($499-1,499/month; enterprise AI teams have tooling budgets; Databricks case study gives pricing anchor)
- Pull Factor:         10/20  (MCP community on Discord/X; enterprise AI teams don't post about their registry choices publicly)

**Strengths:**
- Databricks $499K/year silent retry case study (7 internal MCP servers, loose JSON schema, 12,000 engineering hours/year) is the strongest single case study in the cookbook.
- Stacklok ToolHive confirmed still Kubernetes-only ("SaaS-managed: Appropriate for teams with no Kubernetes infrastructure... Out of scope for most enterprises described in this guide"). No hosted tier launched.
- ContextForge (IBM, self-hosted) and Warpgate (managed gateway) exist but neither is a managed MCP registry with approved-catalog API + schema validation at scale.

**Risks:**
- Stacklok launches hosted ToolHive tier (KILL CONDITION). Monitor stacklok.com blog.
- Warpgate (usewarpgate.com) adds schema validation and an approved-catalog API to its gateway product, converging on MCPDock's value proposition.
- MCP standardization moves fast enough that registry governance becomes a platform-native feature.

**Verdict:** Hold but monitor Warpgate closely. Warpgate's health monitoring feature partially overlaps with MCPDock's scope. The registry + schema validation angle remains unowned.

### The Pitch
**Problem:** A large engineering team running 10+ MCP servers faces three invisible costs: (1) loose JSON schema validation causing silent retries ($499K/year at Databricks for 7 servers); (2) no approved-catalog — agents discover servers ad hoc, with no governance layer deciding which servers are production-ready; (3) health monitoring is Kubernetes-only (ToolHive, ContextForge) or requires self-hosting, leaving teams without managed uptime tracking. MCP went from 0% to 5.4% of all dev tool launches in 2026 (DevHunt). 41% of enterprises already run MCP in production. The governance layer has not kept pace.

**Solution:** MCPDock is the managed MCP server registry: an approved-catalog API (only schema-validated, health-checked servers appear in the catalog), per-server health monitoring (uptime, latency, schema drift), and a governance dashboard (who added which server, when, what schema version). No Kubernetes required. Schema validation catches loose JSON before agents retry silently.

**Target customer:** Senior engineer / platform engineer at a 50-500 person company running 10+ MCP servers in production. Buyer: VP Engineering or Head of Platform. Users: engineering teams consuming MCP servers + security/governance teams.

**Why now:** MCP is the fastest-growing dev tool category in 2026. 41% of enterprises are in production. The governance layer has not caught up. ToolHive (Stacklok) requires Kubernetes and is self-hosted only. No managed SaaS registry with schema validation and approved-catalog API exists.

**Why they buy without being sold to:** After silent retries from a loose schema burn $50K in a quarter, the VP Engineering runs MCPDock's free schema audit on their existing servers, sees 3 servers with validation errors, and subscribes before the meeting with the CFO.

**Revenue model:** $499/month (up to 20 servers, schema validation, 30-day uptime history, approved-catalog API). $999/month (unlimited servers, schema drift alerts, SIEM-compliant audit log). $1,499/month (custom catalog policies, SSO, SLA). Annual −2 months. Free schema audit (upload server manifest, get validation report).

**Unfair advantage:** First managed SaaS MCP registry (all alternatives require Kubernetes or self-hosting). Databricks case study as the "before" story. MCP Registry API spec compliance means any MCP client works out of the box.

### Solo Build Plan
1. Weeks 1-3: MCP Registry API spec implementation; server registration (GitHub URL, container image, or manifest upload); JSON schema validation engine; approved/pending/rejected catalog states.
2. Weeks 4-5: Health check polling (GET /health, /readiness, latency p95); 30-day uptime history; schema drift detection (compare current schema to registered version).
3. Weeks 6-7: Approved-catalog API (authenticated endpoint returning only approved, healthy servers); audit log (who registered, who approved, schema version history).
4. Weeks 8-9: Stripe; free schema audit tool (upload manifest → validation report without registering); managed SaaS hosting (no Kubernetes required).
5. Weeks 10-12: Pilot 5 enterprise AI teams via MCP Discord, Anthropic Builder Community, and LinkedIn AI platform engineers.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-11-06
**Strongest part:** The Databricks $499K/year silent retry case study is a CFO-level pain point that bypasses the "do we need this?" conversation entirely.
**Open question:** Has Warpgate added schema validation and an approved-catalog API to its gateway product? If yes, the registry-specific differentiation narrows to managed hosting vs. self-managed gateway. Check Warpgate's changelog monthly.

---

## #9 — AuthTrack  ·  65/100  ·  DECLINED
First added: 2026-08-16 | Last updated: 2026-11-06 | Score delta this week: −5

> See which prior auths are inside the 7-day / 72-hour CMS clock — before the payer owes you a specific denial reason.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — CSV/fax log + calendar clocks + denial-reason fields; no EHR writeback in v1; HIPAA applies)
- Value Clarity:       14/20  (unchanged — "this PA expires Thursday" is obvious to any biller; CMS clocks give the urgency a number)
- Market Timing:       11/20  (−3: Adulis Health explicitly targets "5-100 provider specialty practices" with CMS 7-day/72-hour clock tracking and proactive alerts; EasyPA has live FHIR API submission with UnitedHealthcare/Humana; PracticeEHR has built-in PA tracking inside its EHR)
- B2B Monetisation:   14/20  (unchanged — $149-299/month; one avoided write-off pays for a year)
- Pull Factor:         12/20  (unchanged — biller Facebook groups; not public-viral)

**Strengths:**
- CMS-0057-F clocks are binding since Jan 1, 2026. The compliance obligation is real and ongoing.
- The 2-10 provider practice on a fax/Excel workflow is a specific, identifiable segment that Adulis Health (5-100 providers) and EasyPA (EHR-integrated) may not fully reach at the 2-5 provider end.
- Spreadsheet-first avoids the EHR integration that kills solo scope.

**Risks:**
- Adulis Health targets "5-100 provider specialty practices" with CMS clock tracking — directly overlapping the target segment.
- EasyPA now has live FHIR API submission with UnitedHealthcare and Humana, with Jan 1, 2027 electronic PA mandate providing their growth catalyst.
- PracticeEHR has built PA tracking inside its EHR — practices already on PracticeEHR won't consider a standalone tool.

**Verdict:** Hold for one more run but the market is getting crowded at the small practice level. If Adulis Health announces pricing below $199/month, reconsider removal.

### The Pitch
**Problem:** Since January 1, 2026, Medicare Advantage, Medicaid, CHIP, and FFE QHP payers must respond to standard prior auths within 7 calendar days and urgent ones within 72 hours, with every denial requiring a specific reason. Billing coordinators at 2-5 provider practices still track this in a spreadsheet next to the fax machine. Adulis Health serves 5-100 provider specialty practices; EasyPA requires EHR integration; PracticeEHR assumes you are already on their platform. The 2-5 provider independent practice on Excel and fax is still unserved.

**Solution:** AuthTrack is the PA status board for 2-5 provider practices: each request gets a CMS clock, a channel (fax/portal/phone), a denial-reason required field, and a reminder before the window closes. v1 is CSV import + form entry — not an Athena integration, not a FHIR client. The 2027 electronic-PA MIPS attestation requires a clean log; AuthTrack builds it from day one.

**Target customer:** Billing coordinator / office manager at a 2-5 provider US practice (PT, specialty lite, independent primary care) not on a practice management system with built-in PA tracking. Buyer: office manager. User: the biller who owns the Excel PA tab.

**Why now:** The CMS clocks are live. The FHIR mandate is Jan 1, 2027. Practices without a tracking log now will invent one badly in the next six months. Adulis and EasyPA serve larger or EHR-integrated practices; the 2-5 provider independent market remains open.

**Why they buy without being sold to:** After a denied MRI with no specific reason and a missed 7-day follow-up, the biller pastes the spreadsheet into AuthTrack, sees two clocks already red, and stops using Excel that week.

**Revenue model:** $149/month (1 location, 200 PAs). $249/month (3 locations + reminder SMS). $299/month (export pack for appeals + HIPAA BAA). Annual −2 months. 14-day trial with sample CSV.

**Unfair advantage:** CMS-clock templates + denial-reason required field sized for fax-era 2-5 provider practices that Adulis Health and EasyPA ignore.

### Solo Build Plan
1. Weeks 1-3: PA log (CSV import); 7-day / 72-hour clocks; denial-reason required on deny.
2. Weeks 4-5: Email/SMS reminders; aging report; appeal packet PDF.
3. Weeks 6-7: HIPAA BAA flow; audit log; role-based access.
4. Weeks 8-9: Stripe; sample-CSV onboarding.
5. Weeks 10-12: Pilot 6 small practices via biller Facebook groups and local MGMA chapters.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-11-06
**Strongest part:** CMS clocks are binding now; the buyer is a person with a spreadsheet, not a health-system IT committee.
**Open question:** Has Adulis Health published pricing? If their entry-tier is under $149/month, the 2-5 provider beachhead disappears entirely.

---

## #10 — CredVerify  ·  63/100  ·  DECLINED
First added: 2026-09-25 | Last updated: 2026-11-06 | Score delta this week: −5

> CAQH to credentialed in one dashboard — built for the 15-100 provider group that Modio forgot.

### Score Breakdown
- Solo Buildability:   13/20  (−1: Rivon Health proves the product is buildable; CAQH ProView XML parsing + OIG/SAM monitoring + expiration tracker; HIPAA; complexity is real but validated)
- Value Clarity:       15/20  (unchanged — expired DEA or lapsed malpractice = payer enrollment rejected = revenue stop; obvious pain)
- Market Timing:       11/20  (−4: Rivon Health launched at $39-$1,499/month with CAQH tracking, PSV workflows, OIG/SAM monitoring, and provider portal — directly filling the mid-market gap)
- B2B Monetisation:   15/20  (unchanged — $99-499/month; credentialing coordinators already have budget for tools)
- Pull Factor:         9/20  (−1: Rivon Health has distribution advantage as a named alternative to Modio Health; CredVerify's first-mover distribution story is weakened)

**Strengths:**
- Modio Health remains enterprise-priced ($1,000-$3,000/month minimum). Medallion remains at $200-$500/provider/month. The price gap below $500/month is real.
- CAQH ProView is free and mandatory; every physician group uses it. The integration is a known workflow, not speculative.
- The mid-market credentialing gap (15-100 providers) is confirmed by multiple comparison sites as a structural problem.

**Risks:**
- Rivon Health ($39-$1,499/month) is now a live direct competitor with CAQH management, PDF auto-fill, PSV workflows, continuous OIG/SAM monitoring, and a provider portal — explicitly positioning as a Modio Health alternative.
- Medallion drops to a lower price tier targeting 5-20 provider groups.
- CAQH ProView adds better integration APIs that enable new entrants more easily.

**Verdict:** Borderline. Rivon Health has entered the target market at the right price. If Rivon Health establishes strong customer count before a solo founder builds, this opportunity closes. Monitor Rivon's Product Hunt and G2 reviews over the next run.

### The Pitch
**Problem:** A physician group with 15-50 providers manages credentialing — CAQH attestations, DEA registrations, malpractice coverage, hospital privileges, payer enrollment — across a spreadsheet and email threads. Modio Health starts at $1,000+/month for small deployments and targets 20+ provider enterprise groups. Medallion charges $200-500/provider/month. CAQH ProView (free) is mandatory but provides no workflow, no expiration tracking, no OIG/SAM exclusion monitoring. A lapsed CAQH attestation or expired malpractice policy stops a provider from seeing patients. The mid-market group (15-100 providers) is squeezed between a free tool with no workflow and enterprise platforms at enterprise prices.

**Solution:** CredVerify automates the CAQH cycle: it reads CAQH ProView exports, tracks expiration dates for every credential (DEA, malpractice, board certification, state licenses), monitors OIG and SAM exclusion lists daily, and assembles payer enrollment packets from verified data. The practice administrator sees a live credential dashboard; providers get expiration alerts 90, 60, and 30 days out; the credentialing coordinator stops maintaining a spreadsheet.

**Target customer:** Practice administrator / credentialing coordinator at a 15-100 provider US physician group (independent, MSO, or specialty practice). Buyer: COO or Practice Administrator. Users: credentialing coordinator + department managers tracking individual providers.

**Why now:** Rivon Health has entered the market, validating that the product is buildable and that buyers will pay. The acquisition-gap from Modio Health (acquired 2025) created a window when their existing customers looked for alternatives. That window is still open, but narrowing.

**Why they buy without being sold to:** A credentialing coordinator who received a payer rejection for a lapsed malpractice certificate runs CredVerify's free CAQH audit, sees 3 providers with expirations in the next 60 days, and subscribes before the next payer enrollment deadline.

**Revenue model:** $99/month (up to 10 providers, CAQH expiration tracking, OIG/SAM monitoring). $299/month (25 providers + payer enrollment packet assembly). $499/month (100 providers + PSV workflow + provider portal). Annual −2 months. Free CAQH audit (upload CAQH export → expiration report without subscribing).

**Unfair advantage:** Free CAQH audit as a self-serve lead magnet — any credentialing coordinator can run it in 60 seconds with their existing CAQH export. OIG/SAM daily exclusion monitoring is a compliance requirement that every credentialing team needs but few have automated.

### Solo Build Plan
1. Weeks 1-3: CAQH ProView export parser (XML/CSV); expiration date extractor for DEA, malpractice, state licenses, board certs; 90/60/30-day email alerts.
2. Weeks 4-5: OIG/SAM daily exclusion monitoring (API integration + per-provider alert); CAQH re-attestation deadline tracker.
3. Weeks 6-7: Payer enrollment packet assembler (PDF auto-fill from CAQH data); provider self-upload portal.
4. Weeks 8-9: Stripe; free CAQH audit tool (lead magnet); HIPAA BAA flow.
5. Weeks 10-12: Pilot 6 physician groups via MGMA chapters and healthcare attorney referrals.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-11-06
**Strongest part:** Free CAQH audit as a self-serve lead magnet — zero friction entry that surfaces real credential gaps without requiring a sales call.
**Open question:** How many paying customers does Rivon Health have? If they have 50+ paying groups in the 15-100 provider segment, the market may be claimed. Check their G2 reviews and LinkedIn customer announcements.

---

## Removed this run
| Entry | Last score | Reason |
|-------|------------|--------|
| ModelReg | 65 | Two consecutive runs with no community bank exam signals. OCC Bulletin 2026-13 explicitly states SR 26-2 is "most useful for $30B+ banks" and explicitly excludes gen AI and agentic AI from scope. Removal condition stated in Run 18 is met. |
| StackClean | 68 → 56 | Substly confirmed with both Google Workspace and Microsoft Entra ID native integration, continuous shadow IT monitoring via browser extension, and RBAC at €95-120/month. The SSO integration moat that defined StackClean's differentiation is now filled by a live, priced competitor. |
