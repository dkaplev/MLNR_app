# SaaS Opportunity Cookbook
Last updated: 2026-10-23 | Entries: 10/10

> R18 note: **ImpactDeck removed** — SimpleAct and Nordis both shipped live FRIA+DPIA lifecycle management (confirmed in EU AI Act/GDPR compliance SaaS searches Oct 23, 2026); the "lifecycle vs. static PDF" moat is now shared by 4+ direct competitors all live in October 2026. **MCPDock enters** — 10,000+ public MCP servers, 97M monthly SDK downloads, 41% of enterprises running MCP in production; no managed cloud SaaS for version control, health checks, and approved-catalog API; Databricks published Sept 2026 that unmonitored MCP servers burned $499K/year in silent retries. **CRAReport +1** — SRP upgraded to v1.2.1 on October 20, 2026 (third version update in 42 days of operation, still no API). **WorkAuditAI +1** — EmployArmor confirmed to cover AI HIRING laws (CCPA ADMT), not CA workplace AI surveillance/ADS-termination (SB 947, AB 1883, SB 951); no HRIS vendor shipping competing module confirmed by Seyfarth Shaw Oct 6 analysis. **StackClean +1** — Subsight blog post explicitly advises "manual SSO cross-check" as a separate step; confirms zero SSO integration planned. **ModelReg -2** — no community bank exam pressure signal found for second consecutive run; SR 26-2 scope unchanged; FINAL WARNING.

---

## #1 — CRAReport  ·  84/100  ·  IMPROVED
First added: 2026-09-11 | Last updated: 2026-10-23 | Score delta this week: +1

> Cut your CRA vulnerability reporting time from hours to minutes — the ENISA SRP portal has no API, so someone has to bridge it.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — SRP form automation + multi-step deadline tracker + evidence ZIP; achievable solo in 3 months)
- Value Clarity:       19/20  (unchanged — SRP is LIVE; ARs have now been submitting for 42 days and generating firsthand pain testimony; "took 3 hours" is now documented experience)
- Market Timing:       20/20  (+1 — SRP upgraded to v1.2.1 on October 20, 2026 — three version updates in 42 days of operation, with no API announced; ENISA FAQ still explicitly states "no API will be provided at the initial release"; open-source software steward obligations kick in Dec 11, 2027, further extending the runway; "the platform will continue to be improved over the coming months" per ENISA launch statement)
- B2B Monetisation:    17/20  (unchanged — EU manufacturers already pay legal/compliance consultants €5K+ per vulnerability incident; $200–500/mo is cheap by comparison)
- Pull Factor:         13/20  (unchanged — EU product security communities share pain; PSIRTs and DevSecOps channels active; first-mover SEO on "CRA SRP reporting" still unclaimed)

**Strengths:**
- ENISA FAQ explicitly states "no API will be provided at the initial release" — this is official policy in writing. The moat is permanent until ENISA changes course publicly.
- Three version updates (SRP v1.0 Sept 11 → v1.1 Oct 12 → v1.2.1 Oct 20) in 42 days of operation confirms active evolution of the form workflow without any API. ARs must re-learn changed processes each time.
- The multi-step notification structure (Early Warning → 72h → Final Report) with per-step mandatory fields creates ongoing workflow value that a one-time document generator cannot replace.

**Risks:**
- If ENISA announces an API roadmap date, the kill condition is known and the window closes.
- The SRP is used by Assigned Representatives (ARs) — the buyer is the EU representative role, which may be outsourced to a legal firm rather than an in-house buyer.
- Non-EU companies exporting to EU may lag 6–12 months in experiencing the manual workflow pain.

**Verdict:** Hold #1. SRP v1.2.1 on Oct 20 — three version updates in 42 days — confirms ongoing form evolution without an API. First-mover SEO window still open and uncontested.

### The Pitch
**Problem:** From September 11, 2026, manufacturers of products with digital elements sold in the EU must report actively exploited vulnerabilities and severe incidents through ENISA's Single Reporting Platform (SRP). The SRP has no API at initial release — every submission requires a human to log in with EU Login + MFA, navigate the 5-step form workflow, submit an Early Warning within 24 hours, a 72-hour Notification, and a Final Report, with each step having distinct mandatory fields. ENISA released SRP v1.1 on October 12 and v1.2.1 on October 20, 2026 — three version updates in 42 days, each requiring ARs to re-read updated documentation and relearn changed processes (v1.2.1 changed the Secondary AR invitation workflow). The ENISA FAQ explicitly states: "no Application Programming Interface (API) will be provided at the initial release of the SRP, so notifications must be submitted through the platform interface. API functionality may be considered in a future phase."

**Solution:** CRAReport is the workflow manager that sits above the SRP portal. You log incidents in CRAReport with product ID, affected versions, and CVSS data. CRAReport tracks the three-stage deadline clock for each incident, pre-fills the SRP form fields from your incident data, and prompts the AR at the right moment to review and submit each stage. Evidence attachments are managed in one place. At audit time, you export the full incident folder: submission timestamps, field values, reviewer log.

**Target customer:** Product security / PSIRT lead or Assigned Representative at a 20–500 person EU software or IoT hardware manufacturer. Buyer: CISO or Head of Product Security. User: the AR who physically submits to the SRP portal. Not a tier-1 telco; not a one-person indie — mid-market manufacturers with 5–50 covered products.

**Why now:** The SRP went live September 11, 2026 and has already evolved to v1.2.1 by October 20. ENISA FAQ explicitly confirms "no API." The first 42 days of real usage are generating firsthand pain from ARs experiencing the manual workflow. No automation tooling exists. First-mover SEO on "CRA SRP reporting software" is unclaimed.

**Why they buy without being sold to:** An AR who just spent 3 hours submitting their first SRP Early Warning notification — filling in 40+ fields across 5 screens, losing their session once, and manually cross-checking the 72-hour deadline — searches for "CRA SRP reporting tool" and finds CRAReport. The free single-incident trial shows the workflow takes 15 minutes instead of 3 hours.

**Revenue model:** $199/month (1–10 concurrent active incidents; 3 products). $349/month (up to 30 incidents; 15 products; deadline dashboard). $599/month (unlimited incidents + multi-AR team + audit export). Annual −2 months. 14-day trial.

**Unfair advantage:** First-mover SEO in a regulation that went live 42 days ago. The product is the bridge that ENISA's FAQ says will not be built on their side. Community content strategy: publish "CRA SRP guide for ARs" that ranks before ENISA's own guidance; track every SRP version update and publish changelogs before ARs read them.

### Solo Build Plan
1. Weeks 1–3: ENISA SRP form field mapping (v1.2.1 schema); incident data model (product, version, CVE, classification, CVSS); 3-stage deadline clock (24h / 72h / Final).
2. Weeks 4–5: Deadline dashboard; Slack/email alerts per stage; multi-incident view for ARs with parallel active incidents.
3. Weeks 6–7: Evidence attachment manager; pre-fill export (field-by-field SRP mapping for AR review); incident audit log.
4. Weeks 8–9: Stripe; free single-incident trial; SEO content ("CRA SRP reporting guide for manufacturers", changelog for each SRP version).
5. Weeks 10–12: Pilot 5 EU manufacturers via ENISA CRA community channels and EU product security (PSIRT) Slack groups.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-10-09
**Strongest part:** ENISA's own FAQ is the product roadmap — they confirm the gap in writing. Three version updates in 42 days confirm ongoing form evolution without an API.
**Open question:** If ENISA publishes an API roadmap date in Q1 2027, does CRAReport's exit strategy depend on being acquired by a GRC platform before that API ships?

---

## #2 — WorkAuditAI  ·  80/100  ·  IMPROVED
First added: 2026-10-09 | Last updated: 2026-10-23 | Score delta this week: +1

> Know which AI tools your managers rely on before the January deadline does.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — AI tool inventory form + SB 947 decision documentation workflow + Cal/WARN template generator; form-based, no HRIS integration in v1; solo-buildable in 3 months)
- Value Clarity:       18/20  (+1 — Seyfarth Shaw published "California Just Expanded Regulation of Workplace AI Beyond CCPA ADMT" Oct 6, 2026, with SB 947/AB 1883/SB 951 detailed analysis; GC who reads any of 4+ major law firm advisories understands the product in 30 seconds; EmployArmor confirmed to cover CCPA ADMT/AI HIRING laws — different laws, different product — WorkAuditAI's specific obligation scope remains uncrowded)
- Market Timing:       18/20  (unchanged — AB 1883 + SB 951 effective Jan 1, 2027; 10 weeks; zero SaaS for the specific SB 947/AB 1883/SB 951 obligations confirmed; ADP/Workday no module)
- B2B Monetisation:    15/20  (unchanged)
- Pull Factor:         14/20  (unchanged — attorney advisory distribution confirmed active; Seyfarth Shaw Oct 6 analysis adds a 5th major law firm to the referral channel alongside Hirschfeld Kraemer, Morgan Lewis, Baker Donelson, and California Public Agency Labor blog)

**Strengths:**
- EmployArmor (the only adjacent AI compliance SaaS found this run) confirmed as covering CCPA ADMT and AI HIRING screening laws — explicitly different from SB 947 (ADS-based discipline/termination), AB 1883 (workplace surveillance), and SB 951 (Cal/WARN). The specific obligation set WorkAuditAI targets remains uncrowded.
- Seyfarth Shaw's October 6, 2026 analysis adds a 5th major employment law firm to the referral distribution channel — "California just expanded regulation of workplace AI beyond CCPA ADMT" confirms the distinct obligation scope.
- 10 weeks to January 1, 2027 (AB 1883 + SB 951 effective date) remains the primary urgency driver; SB 947 follows July 1, 2027 for the ADS-based discipline workflow module.

**Risks:**
- Governor Newsom's signing message noted AB 1883 "lacks key definitions" — regulatory ambiguity could narrow the addressable problem before first revenue.
- ADP / Workday could add a "California AI laws" module using existing HRIS integrations.
- California-only scope limits TAM initially; NY AI Labor Information Act still unsigned (awaiting Hochul by year-end).

**Verdict:** Hold and accelerate. Five major law firm advisory networks are now active distribution channels. The specific SB 947/AB 1883/SB 951 obligation set remains uncrowded. 10 weeks to first deadline.

### The Pitch
**Problem:** On September 30, 2026, California signed three workplace AI laws: SB 947 (effective July 1, 2027) prohibits relying solely on automated decision systems for discipline or termination, requiring documented human review; AB 1883 (effective January 1, 2027) restricts AI-powered surveillance tools that infer employee emotions or collect neural data; SB 951 (effective January 1, 2027) requires enhanced Cal/WARN disclosures when automation drives qualifying layoffs. HR and legal teams at 100–2,000 person companies with California workers must now: inventory every AI tool influencing an employment decision, document independent human review for ADS-based discipline/termination decisions, assess and restrict AI surveillance tools, and update Cal/WARN procedures. Hirschfeld Kraemer, Morgan Lewis, Baker Donelson, Seyfarth Shaw, and the California Public Agency Labor & Employment Blog all published client advisories with identical Step 1: "conduct a straightforward audit of the software and platforms your company uses to hire, manage, monitor, evaluate, or terminate California-based employees." No purpose-built SaaS for these three specific laws exists. EmployArmor covers AI hiring/screening laws (CCPA ADMT) — a different set of obligations from a different law.

**Solution:** WorkAuditAI is the compliance operating layer for California's September 30, 2026 workplace AI laws. It runs a guided AI tool inventory (what tools, which HR decisions do they influence, which California employees are affected), then builds a workflow for each obligation: a surveillance tool classifier (AB 1883), a mandatory human-review documentation workflow for ADS-influenced discipline decisions (SB 947), a Cal/WARN AI-disclosure template generator (SB 951), and an audit trail exportable to counsel or regulators on demand.

**Target customer:** HR Director / VP People or General Counsel at a 100–2,000 person company with at least 50 California-based employees. Buyers: GC and CHRO jointly. Users: HR Operations and HR Business Partners who document employment decisions. Industries: tech, finance, logistics — any employer using AI-assisted performance management, productivity monitoring, or hiring tools.

**Why now:** SB 947, AB 1883, and SB 951 were all signed September 30, 2026. AB 1883 and SB 951 take effect January 1, 2027 (10 weeks away). Five major employment law firms published specific advisories within days of signing. No SaaS tool built for these specific laws exists. ADP and Workday are rebuilding sales collateral, not shipping modules. The 10-week window is the highest-urgency, zero-competition acquisition moment this product will ever have.

**Why they buy without being sold to:** An employment attorney sends a client advisory about SB 947 with a "Five-Step Audit." Step 1 is "inventory your AI tools." The GC googles "California SB 947 compliance software" or "workplace AI audit tool," finds WorkAuditAI's free AI inventory form, completes Step 1 in 20 minutes, and purchases the full workflow to complete Steps 2–5 the same afternoon.

**Revenue model:** $199/month (1–50 CA employees; AI inventory + AB 1883 surveillance classifier + SB 951 Cal/WARN template). $349/month (50–300 CA employees + SB 947 human-review documentation workflow + employee data-request response). $599/month (300+ CA employees + counsel export pack + RBAC + full audit trail). Annual −2 months. Free: guided AI tool inventory (Step 1 of every attorney checklist) with no purchase required.

**Unfair advantage:** First SaaS built specifically for California's September 30, 2026 workplace AI laws. Five employment attorney referral networks distribute at zero CAC — the free inventory IS the product firms recommend to clients. First-mover SEO on "California SB 947 compliance," "AB 1883 workplace AI," and "workplace AI risk assessment" before any competitor exists.

### Solo Build Plan
1. Weeks 1–2: CA Workplace AI intake questionnaire; AI tool inventory (HR systems, productivity monitors, hiring tools, performance management); decision-category mapping (hiring, performance, discipline, layoff).
2. Weeks 3–4: AB 1883 surveillance tool classifier (infer emotion / collect neural data); SB 947 decision workflow (ADS flag → independent human review form → corroboration record → written post-use notice generator).
3. Weeks 5–6: Cal/WARN AI-disclosure template (SB 951 layoff disclosure language); employee data-request response workflow (SB 947 § data description obligation).
4. Weeks 7–8: Stripe; attorney partnership landing page; SHRM and HR compliance newsletter placements.
5. Weeks 9–12: Pilot 10 companies through employment counsel referrals (Hirschfeld Kraemer, Morgan Lewis, Baker Donelson, Seyfarth Shaw advisories — contact labor practice groups directly).

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-10-23
**Strongest part:** Five major law firm advisory networks confirmed publishing "Five-Step Audit" frameworks — the law firm IS the sales team, and the free inventory IS their Step 1.
**Open question:** Will ADP or Workday ship a "California AI laws" compliance module within 9 months (before SB 947 goes live July 1, 2027), leveraging HRIS integrations to provide richer automated audit trails than a form-based tool can?

---

## #3 — DentPay  ·  78/100  ·  UNCHANGED
First added: 2026-07-16 | Last updated: 2026-10-09 | Score delta this week: —

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — CSV-first rule engine; dentpay.tech pilot confirms technical approach)
- Value Clarity:       19/20  (unchanged — "same total with three flagged lab mismatches" is a demonstrable live demo)
- Market Timing:       17/20  (unchanged — dentpay.tech still in pilot "leave your email" mode; ClinixFlows dent-pay.com is a patient collections product — different problem — not a production pay competitor; Samera.ai still UK-only)
- B2B Monetisation:    16/20  (unchanged)
- Pull Factor:         10/20  (unchanged)

**Strengths:**
- dentpay.tech — the direct production-pay competitor — is still in "piloting with US practices on production pay, leave your email" mode after 5 months. No paying customer scale or funding announced.
- ClinixFlows (dent-pay.com), same founder, is a patient collections/payment infrastructure product — NOT a production pay calculator. Different problem, different buyer. The production-pay calculation gap is still unclaimed at scale.
- Production % pay reconciliation remains a distinct category from general payroll — Gusto/ADP have no production split logic.

**Risks:**
- dentpay.tech is directly executing the same thesis; any funding round or paying customer announcement closes the distribution window.
- Dental Intelligence or Open Dental itself could deepen native pay math in a platform update.
- Relationship-heavy sales; CPA/advisor trust needed for paycheck-math credibility.

**Verdict:** Hold. dentpay.tech validates the market but remains pre-scale. ClinixFlows is solving a different (patient payment) problem. The OD/Dentrix production-pay gap is still unclaimed at revenue scale.

### The Pitch
**Problem:** US dental practices paying associates and hygienists on production still spend hours each pay period exporting Open Dental or Dentrix reports, pasting into Excel, applying lab fees, write-offs, and card-fee rules, then hoping the spreadsheet matches the contract. Open Dental's Provider Payroll report is raw material, not a pay engine. Samera automated this for UK Dentally+Xero; Gusto deposits pay but does not reconcile OD production rules. HRPayPick 2026 confirms no payroll platform has native plug-and-play integration with all three major US PMS systems. dentpay.tech is piloting the same idea but remains pre-scale.

**Solution:** DentPay imports OD/Dentrix production exports, applies per-provider pay rules once, flags anomalies before payout, and exports an approval pack to Gusto/ADP. Office managers review exceptions; they do not rebuild formulas.

**Target customer:** Office manager / owner at 1–3 location US dental practice on Open Dental or Dentrix with associates or hygienists on production splits.

**Why now:** Production % pay still the norm; UK tools proved analytics willingness-to-pay; US PMS vendors have not productised the reconciliation layer.

**Why they buy without being sold to:** An OM who spent Sunday fixing a hygienist underpay uploads last month's OD export, sees the same total with three flagged lab mismatches, and refuses to go back to Excel.

**Revenue model:** $149 / $249 / $399 per practice. 30-day trial. CPA referral 15%.

**Unfair advantage:** US OD/Dentrix rule templates + anomaly library; Eaglesoft path as differentiation from dentpay.tech; multi-location PE roll-up pricing.

### Solo Build Plan
1. Weeks 1–3: OD Provider Payroll CSV ingest; rule builder; pay summary PDF.
2. Weeks 4–5: Anomaly flags; vs last period; Gusto CSV export.
3. Weeks 6–7: Dentrix path; multi-provider approval.
4. Weeks 8–9: Stripe; sample-file onboarding.
5. Weeks 10–12: Pilot 8 practices via dental groups / OD user groups.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-10-09
**Strongest part:** dentpay.tech still pre-scale after 5 months confirms the market's friction with distribution — DentPay has time to enter if it differentiates on Dentrix+Eaglesoft and multi-location PE pricing.
**Open question:** Does dentpay.tech's head start in the study-club referral channel foreclose the primary distribution path for a second entrant, or does dental community fragmentation leave room for a Dentrix-focused alternative?

---

## #4 — IntegWatch  ·  72/100  ·  UNCHANGED
First added: 2026-10-16 | Last updated: 2026-10-16 | Score delta this week: —

> Know which customer's integration is about to fail before your AI agent exposes it.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — OAuth token expiry detection for top-10 integrations + per-customer uptime tracking; achievable solo in 3 months)
- Value Clarity:       16/20  (unchanged — free connection health scan shows specific at-risk customers immediately; self-evident to any CS lead who has experienced silent agent failures)
- Market Timing:       16/20  (unchanged — 2026 State of Agentic Integrations report: integration reliability is the #1 agentic AI deployment blocker at 52%; no product monitors per-customer OAuth connection health specifically for agentic SaaS)
- B2B Monetisation:    14/20  (unchanged — $199–799/month for agentic SaaS company)
- Pull Factor:         11/20  (unchanged — CS team story "we prevented 8 customer integrations from failing" is shareable)

**Strengths:**
- 2026 State of Agentic Integrations (Ampersand): 52% cite integration reliability as #1 agentic blocker; 68% spend 25%+ time maintaining integrations; 68% lost/delayed enterprise deals — all three metrics point at the same gap.
- Existing infrastructure tools (Nango, Merge, Apideck) help companies build better integrations but do NOT surface per-customer connection health to the CS team — the customer-scoped view is structurally absent from their dashboards.
- The "free connection scan showing token expiry dates" is a self-closing conversion mechanism: product demonstrates the problem before trial ends.

**Risks:**
- Nango, Apideck, or Merge could add "customer connection health alerts" as a native feature.
- Datadog/PagerDuty can monitor API calls; enterprise teams may build custom alerting.
- The market of "agentic SaaS companies with 50+ customer connections" may be smaller than the broader integration reliability pain suggests.

**Verdict:** Hold. Customer-CS framing (proactive customer outreach before failures, not just engineering alerting) is the structural moat over platform-native monitoring.

### The Pitch
**Problem:** B2B SaaS companies shipping AI agents in 2026 depend on their customer-facing integrations being reliable. The 2026 State of Agentic Integrations report found that integration reliability is the #1 blocker to shipping AI agents, cited by 52% of companies — ahead of hallucinations and engineering bandwidth. When an AI agent fails because a customer's Salesforce OAuth token silently expired three weeks ago, the first notification is a customer ticket — or worse, a churn email. Existing monitoring tools alert on server failures and API latency. None surface "Customer Acme Corp's HubSpot connection has been failing silent retries for 4 days" before the customer notices.

**Solution:** IntegWatch monitors every customer's OAuth connection to the integrations your AI agents depend on. You define which integrations matter for each customer tier; IntegWatch checks them on a configurable schedule, catches expired tokens before they fail in production, flags rate limit approach, and opens a Slack alert with the specific customer name, integration, and error reason before your agent fails visibly. The CS team sees "3 customers at risk this week" in a dashboard ordered by tier — not a generic API error log.

**Target customer:** Engineering lead / VP Engineering at a 15–100 person B2B SaaS company that has shipped AI agents to paying customers with 5+ customer-facing integrations. Buyer: VP Engineering or CTO. Users: engineers who own integration on-call AND CS team who proactively reach out before customers notice.

**Why now:** 2026 State of Agentic Integrations report is the clearest catalyst — integrations "used to be background data pipes. Now, they are the bottleneck for the AI era." No product monitors per-customer OAuth connection health specifically for agentic companies.

**Why they buy without being sold to:** An engineering lead whose agent silently failed for 12 customers because their Salesforce OAuth tokens expired on the same day runs IntegWatch's free connection health scan. The scan shows 8 more customers with tokens expiring in the next 14 days. They purchase before the scan completes.

**Revenue model:** $199/month (up to 50 monitored connections; 5 integrations; Slack alerts). $399/month (up to 250 connections; 20 integrations; PagerDuty + webhook). $799/month (unlimited connections + SLA-mode monitoring + per-customer uptime reports). Annual −2 months. Free: one-time connection health scan.

**Unfair advantage:** Customer-scoped view ("Acme Corp's Salesforce connection has a 94% uptime this quarter") that platform-native dashboards are not designed to surface to CS teams. Distribution through Nango/Apideck/Ampersand developer communities where target customers already live.

### Solo Build Plan
1. Weeks 1–3: OAuth token expiry detection for top-10 integrations; per-customer connection health dashboard.
2. Weeks 4–5: Polling scheduler; Slack alert on token expiry warning (48h/24h/expired); rate limit proximity alerts.
3. Weeks 6–7: Per-customer uptime report; integration reliability dashboard; error pattern detection.
4. Weeks 8–9: Stripe; free connection scan; PagerDuty integration; CS team view.
5. Weeks 10–12: Pilot 8 agentic SaaS companies through Ampersand community, Nango Discord.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-16
**Strongest part:** The 2026 State of Agentic report quantifies the exact problem with three distinct data points; the free token-expiry scan is a strong self-demonstrating conversion mechanism.
**Open question:** If Nango or Merge adds customer-scoped integration health alerts and proactive token refresh as a native feature, does IntegWatch's value proposition collapse immediately, or is the CS-layer framing a durable differentiation?

---

## #5 — AuthTrack  ·  70/100  ·  UNCHANGED
First added: 2026-08-16 | Last updated: 2026-10-16 | Score delta this week: —

> See which prior auths are inside the 7-day / 72-hour clock — and which denials still have no specific reason.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — CSV/fax log + calendar clocks + denial-reason fields; HIPAA applies)
- Value Clarity:       16/20  (unchanged — "this PA blows the CMS clock on Thursday" is obvious to a biller)
- Market Timing:       14/20  (unchanged — AuthTrack Pro confirmed pivoting upmarket; FHIR API mandate 10 weeks away)
- B2B Monetisation:    14/20  (unchanged)
- Pull Factor:         12/20  (unchanged — biller Facebook groups)

**Strengths:**
- AuthTrack Pro's Aug 2026 LinkedIn post confirms pivot toward "high authorization volume" imaging facilities, hospitals, SNFs — the 2–10 provider small practice segment is confirmed less contested.
- Regulation is 9.5 months live — buyers have documented losses that make the pain concrete.
- FHIR API mandate (Jan 1, 2027) is 10 weeks away — practices building a log now will have the cleanest path to electronic attestation.

**Risks:**
- AuthTrack Pro's upmarket pivot could reverse.
- Honey Health (agentic AI for end-to-end PA automation) is moving into smaller practices.
- Tiny practices may wait for their clearinghouse to add a free clock tracker.

**Verdict:** Hold. AuthTrack Pro's upmarket pivot opens the small-practice segment. Denial-reason audit pack and CMS clock export for appeals remain the differentiation.

### The Pitch
**Problem:** Since 1 January 2026, Medicare Advantage, Medicaid, CHIP, and FFE QHP payers must decide standard prior auths in 7 calendar days and urgent ones in 72 hours, and every denial must include a specific reason. Billing coordinators at 2–10 provider practices still track this in a spreadsheet. They miss clocks, they cannot prove a vague denial, and they will need a clean log before 2027 electronic-PA attestation. AuthTrack Pro launched in June 2026 but their August 2026 messaging reveals they're targeting "high authorization volume" teams at imaging facilities and hospitals — explicitly pivoting away from the 2–10 provider small practice.

**Solution:** AuthTrack is the PA status board with CMS-clock compliance: each request gets a deadline clock, a channel (fax/portal/phone), a required denial-reason field (vague denials are flagged), and an alert before the CMS window closes. At appeals time, you export a packet: submission date, payer clock, denial reason, follow-up log.

**Target customer:** Billing coordinator / office manager at a 2–10 provider US practice (PT, specialty lite, independent primary care) not on Athena+Linear Health. Buyer: office manager. User: the biller who owns the Excel PA tab.

**Why now:** The clocks are 9.5 months live. Practices that missed clock windows have documented losses. The FHIR API mandate (1 Jan 2027) is 10 weeks away. AuthTrack Pro's upmarket pivot is confirmed.

**Why they buy without being sold to:** After a denied MRI with no specific reason and a missed 7-day follow-up, the biller pastes the spreadsheet into AuthTrack, sees two clocks already red, and stops using Excel that week.

**Revenue model:** $149/mo (1 location, 200 PAs). $249/mo (3 locations + reminder SMS). $299/mo (export pack for appeals). Annual −2 months. 14-day trial with sample CSV.

**Unfair advantage:** CMS-clock breach documentation + denial-reason enforcement specifically for fax-era small practices that AuthTrack Pro's upmarket pivot leaves unserved.

### Solo Build Plan
1. Weeks 1–3: PA log (CSV import); 7-day / 72-hour clocks; denial-reason required on deny; vague-denial flag.
2. Weeks 4–5: Email/SMS reminders; aging report; appeal packet PDF.
3. Weeks 6–7: HIPAA BAA flow; audit log; role-based access.
4. Weeks 8–9: Stripe; sample-CSV onboarding.
5. Weeks 10–12: Pilot 6 small practices via biller Facebook groups and local MGMA chapters.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-16
**Strongest part:** AuthTrack Pro's explicit upmarket pivot leaves the small-practice market less contested.
**Open question:** Will AuthTrack Pro reverse their upmarket pivot and return to the small-practice segment if their enterprise targets prove too complex to acquire?

---

## #6 — MCPDock  ·  69/100  ·  NEW
First added: 2026-10-23 | Last updated: 2026-10-23 | Score delta this week: —

> Every production MCP server — healthy, versioned, and owned — in one dashboard without Kubernetes.

### Score Breakdown
- Solo Buildability:   14/20  (MCP server registry + scheduled health checks + schema fingerprinting + approved-catalog API + team access controls; solid 3-month solo scope if scoped to top-20 MCP servers and HTTP/SSE transports only)
- Value Clarity:       14/20  (needs brief setup context — "your agent silently failed because an internal MCP server returned malformed JSON for 48 hours" resonates immediately with anyone who has experienced it; Databricks $499K/year case makes the ROI concrete)
- Market Timing:       15/20  (MCP grew from 0 to 10,000+ servers and 97M monthly SDK downloads in 18 months; 41% of enterprises running MCP in production as of Stacklok 2026 survey; YC Summer 2026 RFS explicitly named MCP tooling; no managed SaaS exists — only self-hosted OSS alternatives requiring Kubernetes)
- B2B Monetisation:    14/20  ($99–599/month for dev/platform teams; managed-vs-self-hosted willingness-to-pay is proven in adjacent spaces like managed Postgres and managed Redis; Databricks case provides $499K ROI anchor)
- Pull Factor:         12/20  (platform engineering teams share operational tools through Nango Discord, Anthropic developer community, and YC company Slack; "we prevented $X in silent MCP retry costs" is a shareable Slack post)

**Strengths:**
- 10,000+ public MCP servers and 97 million monthly SDK downloads (Anthropic, May 2026) with no managed operational registry — only flat public directories and self-hosted OSS tools requiring Kubernetes.
- Databricks (Sept 2026): 7 internal MCP servers with loose schema validation burned $499K/year in silent retry costs and 12,000 engineering hours. Published by Databricks as a cautionary case — gives buyers a concrete ROI anchor.
- YC Summer 2026 RFS explicitly listed "Software for Agents — MCP" as a priority category, confirming investor and founder conviction in the operational infrastructure gap.

**Risks:**
- ToolHive Registry Server (Stacklok, open-source) and MCP Runtime (open-source, Kubernetes-native) provide much of the same functionality as self-hosted OSS. If Stacklok launches a managed hosted tier, MCPDock's moat evaporates.
- FastMCP Gateway (Prefect Horizon) bundles an MCP registry inside their full orchestration platform — teams already using Prefect get this for free.
- MCP protocol is evolving rapidly (new transport options, authentication changes); a solo founder must track protocol changes continuously to stay current.

**Verdict:** Enter as the managed cloud MCP server registry — no Kubernetes, 10-minute setup, schema validation and health checks included. Primary kill condition: Stacklok launching a managed hosted ToolHive tier.

### The Pitch
**Problem:** The Model Context Protocol ecosystem has grown to 10,000+ public servers and 97 million monthly SDK downloads as of May 2026, with 41% of enterprises already running MCP in some production stage. Engineering teams deploying AI agents face a consistent operational failure: MCP servers are copied from GitHub READMEs, pinned to no specific version, health-checked by no one, and owned by no one. Databricks published in September 2026 that 7 internal MCP servers with loose JSON schema validation burned an estimated $499,000/year in silent retry costs and 12,000 engineering hours in wasted wait time. When an internal server drifts, returns malformed tool responses, or silently updates its behavior, the agent misbehaves — and teams find out through degraded outputs or customer complaints, not monitoring alerts. Open-source alternatives (ToolHive, MCP Runtime) solve this but require Kubernetes infrastructure and a dedicated DevOps team to self-host.

**Solution:** MCPDock is a managed cloud registry for the MCP servers your agents depend on. You register each server — internal or third-party — with an owner, an approved version, a health endpoint, and an expected tool-response schema fingerprint. MCPDock polls each endpoint on a configurable schedule, validates tool-call response shapes, and alerts Slack when a server goes unhealthy, drifts from its pinned version, or starts returning unexpected schemas. Product engineers query a single approved-catalog API endpoint to discover which servers are healthy and approved for production — the catalog self-updates as the platform team approves new versions.

**Target customer:** Platform engineering lead or Head of Platform at a 30–150 person company that has deployed 5+ AI agents consuming internal or third-party MCP servers. Buyer: VP Engineering or CTO. Users: (1) platform engineers who register, approve, and monitor servers; (2) product engineers who build agents against the approved catalog.

**Why now:** MCP adoption crossed into enterprise production in 2026 — 41% of enterprises already running it. YC's Summer 2026 RFS explicitly listed agentic infrastructure and MCP tooling. The protocol was donated to the Linux Foundation (December 2025), signaling permanence. Databricks published a quantified case study of the exact operational failure MCPDock prevents. No managed SaaS exists for teams that want operational catalog management without self-hosting overhead.

**Why they buy without being sold to:** A platform engineering lead who cannot answer "which MCP servers are we running and are they healthy?" runs MCPDock's free 10-server catalog scan. The scan shows 2 deprecated versions, 1 unhealthy endpoint, and 3 servers with schema drift. They purchase the dashboard before the scan report expires.

**Revenue model:** $99/month (up to 10 servers; health checks + version alerts; 3 team members). $299/month (up to 50 servers + approved-catalog API + schema validation + team access control + Slack alerts). $599/month (unlimited + custom health check policies + audit log + SSO + schema drift detection). Annual −2 months. Free: one-time catalog scan (10 servers, no registration required).

**Unfair advantage:** First managed SaaS that treats MCP server health as an operational responsibility, not a self-hosting exercise. Approved-catalog API endpoint creates switching costs — every agent codebase integrates against MCPDock's /catalog endpoint. First-mover SEO on "MCP server registry managed" and "MCP server health monitoring" — both unclaimed phrases in October 2026.

### Solo Build Plan
1. Weeks 1–3: MCP server registry (name, owner, pinned version, endpoint URL, health check config, tool schema fingerprint); scheduled health checks (every 15 min); Slack alert on unhealthy server or schema drift.
2. Weeks 4–5: Approved-catalog API endpoint (/catalog returns list of approved, healthy servers with current metadata); version pinning UI; ownership assignment.
3. Weeks 6–7: Team access control (platform team: read/write; product team: read-only); server change audit log; deprecation workflow.
4. Weeks 8–9: Stripe; free 10-server catalog scan (no account required); "MCP server ops for production AI teams" SEO guide.
5. Weeks 10–12: Pilot 8 teams through Anthropic developer community, Nango Discord, and YC W27 agentic companies.

### Critic's Assessment
**Rating:** 6.5/10 | **Last critique:** 2026-10-23
**Strongest part:** Databricks' $499K quantified case study makes the ROI concrete; the approved-catalog API creates switching costs that a self-hosted OSS registry cannot replicate easily.
**Open question:** When Stacklok/ToolHive launches a managed hosted tier (likely early 2027 given enterprise demand), does MCPDock's first-mover advantage in the managed SaaS space translate to a customer retention moat via schema fingerprints and historical health data?

---

## #7 — AgentAudit  ·  68/100  ·  UNCHANGED
First added: 2026-09-25 | Last updated: 2026-10-16 | Score delta this week: —

> Block malicious MCP packages before they reach your production agent — not after the incident report.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — Trust Registry + GitHub App CI gate + team dashboard; agentaudit-dev OSS validates the architecture)
- Value Clarity:       15/20  (unchanged — agentaudit-dev's real Trust Registry proves this is a real security layer)
- Market Timing:       12/20  (unchanged — agentaudit-dev "free forever, no enterprise upsells" — the paid GitHub App + org-level policy + CISO dashboard is confirmed permanently open)
- B2B Monetisation:    14/20  (unchanged — enterprise security budgets; supply chain security is a known spend category)
- Pull Factor:         13/20  (unchanged — "we blocked a malicious MCP package" story = eng Twitter virality)

**Strengths:**
- agentaudit-dev explicitly stated: "Free forever. No freemium tiers, no enterprise upsells. Security shouldn't be gated." — confirmed commitment removes primary kill condition.
- The paid SaaS tier (team dashboard + organization-level policy + continuous monitoring) is explicitly unlaunched and confirmed open.
- agentaudit.co.uk ("Agent Audit") is a completely separate product focused on AI receipts and audit evidence for compliance — NOT a competitor.

**Risks:**
- agentaudit-dev could reverse their "free forever" commitment if funded.
- Cisco MCP Scanner and other OSS security tools are appearing.
- The "Trust Registry" as community-driven database has data quality risks.

**Verdict:** Hold. agentaudit-dev's "free forever" commitment removes the primary kill condition. The paid GitHub App + org-level dashboard is confirmed open. Note: MCPDock (#6) is a distinct product (operations/registry vs. security/trust); same ecosystem, different buyer and problem.

### The Pitch
**Problem:** AI agents increasingly rely on Model Context Protocol (MCP) servers — npm packages that expose tools to models. The ecosystem has grown to 10,000+ MCP packages, with no systematic supply-chain security layer. agentaudit-dev's open-source AgentAudit CLI + Trust Registry validates real packages against known security findings. But it is "free forever" by design — no enterprise commercial tier will be built by the OSS project. Engineering teams need a team-level policy layer: org-wide package allowlists, a CI gate that blocks builds containing unauthorized MCP packages, a dashboard showing which packages each team is using and their current security status, and alerts when a previously-safe package gets flagged.

**Solution:** A SaaS layer on top of the open AgentAudit Trust Registry: GitHub App + org-level package policy + team dashboard. Every repository in the organization runs the scan automatically. New MCP package = instant Trust Registry check. Flagged package = PR blocked, reviewer alerted, audit record created. The CISO gets a dashboard showing every MCP package in use across all teams and their security status.

**Target customer:** CISO / Security Engineering lead at a 50–500 person company actively using MCP-based AI agents in production. Buyer: CISO or VP Engineering. Users: security team + each engineering team running AI agents.

**Why now:** agentaudit-dev's OSS proves the technical approach and provides a ready-made Trust Registry data source. The "free forever" commitment confirms the paid enterprise SaaS layer is permanently open. Inkog Labs (Oct 2026): 84% of scanned MCP server repos had security findings.

**Why they buy without being sold to:** After a security team discovers an MCP package with a prompt injection vulnerability that was silently used in production for 3 weeks, they install the AgentAudit GitHub App, see 14 other packages across 6 repos that need review, and purchase the enterprise dashboard to manage ongoing policy.

**Revenue model:** $199/month (up to 5 repos + Trust Registry scan + PR blocking). $399/month (up to 20 repos + org policy + Slack alerts). $799/month (enterprise: unlimited repos + CISO dashboard + custom risk rules + SOC 2 export). Annual −2 months.

**Unfair advantage:** Trust Registry data source (open, maintained by agentaudit-dev community) + GitHub App org-level policy layer. Builds on, rather than competes with, the OSS.

### Solo Build Plan
1. Weeks 1–3: GitHub App with org-level installation; Trust Registry API integration; PR-blocking on unsafe packages.
2. Weeks 4–5: Org package allowlist policy builder; team dashboard (repos + packages + status); package change alerts.
3. Weeks 6–7: CISO summary report; custom risk rules.
4. Weeks 8–9: Stripe; free trial (unlimited repos, read-only); security newsletter placements.
5. Weeks 10–12: Pilot 5 security-conscious engineering teams; explore partnership with agentaudit-dev.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-16
**Strongest part:** agentaudit-dev's "free forever" commitment is now a confirmed structural feature — the paid SaaS tier is permanently open.
**Open question:** agentaudit-dev has AGPL + commercial license and could reverse the "free forever" decision if funded. How durable is their commitment?

---

## #8 — CredVerify  ·  68/100  ·  UNCHANGED
First added: 2026-10-09 | Last updated: 2026-10-09 | Score delta this week: —

> Your 40-provider group's malpractice, DEA, and hospital privileges — one dashboard, no spreadsheet.

### Score Breakdown
- Solo Buildability:   11/20  (provider profile + renewal calendar + CAQH import + HIPAA BAA; achievable solo in 3 months focused on top-5 states and 3 credential types)
- Value Clarity:       14/20  (lapsed DEA registration = prescribing halt; voided payer contract = revenue loss; trigger events are immediate and concrete)
- Market Timing:       15/20  (Alder VC 2026 names mid-market physician group credentialing as underserved; Modio Health acquired by Health Carousel, removing the primary mid-market option; enterprise incumbents start at $50K/year)
- B2B Monetisation:    16/20  (compliance-critical; one avoided lapsed malpractice certificate pays for 2 years of subscription)
- Pull Factor:         12/20  (MGMA chapters and credentialing coordinator LinkedIn groups share tools)

**Strengths:**
- Modio Health (primary mid-market option) acquired by Health Carousel — acquisition displacement creates a window.
- CAQH profiles already hold most credential data — zero-friction onboarding path.
- Compliance-critical + immediate financial consequence = high willingness to pay without extensive education.

**Risks:**
- HIPAA BAA required from day one — adds legal overhead.
- State licensing data accuracy across 50 jurisdictions requires ongoing maintenance.
- MGMA or a health-system-adjacent vendor could enter this segment.

**Verdict:** Enter with narrow beachhead: top-5 US states, 3 credential types (DEA, state medical license, malpractice), CAQH import. Expand only after first 10 paying customers.

### The Pitch
**Problem:** Physician groups, outpatient surgery centers, and specialty clinics with 10–100 providers manage credentialing manually. For a 40-provider orthopedic group, this means a full-time credentialing coordinator maintaining a spreadsheet of 200+ renewal dates. A single lapsed DEA registration halts prescribing. Enterprise credentialing platforms start at $50K/year. Modio Health — the closest mid-market option — was acquired by Health Carousel in 2026, leaving the 10–100 provider group without a purpose-built affordable alternative.

**Solution:** CredVerify is the centralized credentialing dashboard for mid-market physician groups. Each provider gets a profile with all their credentials, licenses, and renewals tracked in one place. The system alerts the coordinator 90/60/30 days before any expiration, generates a renewal preparation checklist per jurisdiction, and maintains a verification-ready record for payer audits. v1 is database-first — CAQH import for onboarding, no EHR integration.

**Target customer:** Credentialing coordinator / Practice Administrator at a 10–100 provider specialty group (orthopedics, neurology, anesthesia, GI) or outpatient surgery center in the US. Buyer: Practice Administrator or CFO. Users: credentialing coordinator + individual providers.

**Why now:** Modio Health's acquisition created an active vacancy in the mid-market credentialing tool category. Alder VC's 2026 analysis confirms the gap. Enterprise platforms start at $50K/year — 10x above what a 20–50 provider group will pay.

**Why they buy without being sold to:** After a provider's malpractice certificate lapses unnoticed and a payer contract voids mid-year, the administrator imports CAQH data into CredVerify, sees 3 expirations in the next 60 days that weren't on the coordinator's spreadsheet, and converts to paid the same session.

**Revenue model:** $299/month (1–20 providers). $499/month (21–60 providers + payer audit pack). $799/month (61–100 providers + CAQH sync + reporting). Annual −2 months. Free tier: 5 providers, 3 credential types.

**Unfair advantage:** CAQH import as zero-friction onboarding. Purpose-built for 10–100 provider groups that enterprise platforms ignore.

### Solo Build Plan
1. Weeks 1–3: Provider profile; renewal calendar; 90/60/30-day email alerts; CSV import.
2. Weeks 4–5: CAQH profile import; document upload; payer audit export pack.
3. Weeks 6–7: HIPAA BAA click-wrap; audit log; role-based access.
4. Weeks 8–9: Stripe; free 5-provider tier.
5. Weeks 10–12: Pilot 5 groups through MGMA chapter demonstrations and NAMSS LinkedIn groups.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-09
**Strongest part:** Modio Health's acquisition created a real market gap at exactly the moment Alder VC is publishing research calling it underserved.
**Open question:** Can a solo founder maintain accurate, current renewal deadline data across 50 state licensing jurisdictions without a credentialing domain expert, and what is the liability exposure if a renewal alert fires at the wrong deadline?

---

## #9 — StackClean  ·  68/100  ·  IMPROVED
First added: 2026-10-02 | Last updated: 2026-10-23 | Score delta this week: +1

> Kill the SaaS zombie seats before finance finds them on the card statement.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — Google Workspace/Okta API + SSO login history + SaaS catalog; technically straightforward)
- Value Clarity:       15/20  (unchanged — "here are 12 seats nobody has used in 90 days" is self-evident)
- Market Timing:       13/20  (+1 — Subsight blog post "What Is the Best Subscription Tracker of 2026?" explicitly states for SSO/ERP integrations users need a dedicated "Enterprise SaaS Management Platform" — not Subsight; their own positioning confirms they will NOT add SSO integration, and advises it as a manual cross-check step. The SSO moat is now validated by Subsight's own product strategy, not just an absence of integration.)
- B2B Monetisation:    14/20  (unchanged)
- Pull Factor:         12/20  (unchanged — ops/finance communities share "we saved $X" stories)

**Strengths:**
- Subsight blog post Oct 2026 explicitly distinguishes their product (subscription tracker for startups) from "Enterprise SaaS Management Platform" (for SSO/ERP integration at scale). They recommend the latter category for SSO needs — validating that Subsight will NOT add Workspace/Okta integration as it would put them in a different market.
- Subsight's bank-statement approach misses apps billed annually, SSO-only apps, and inactive seats still being billed.
- Zylo, Torii, Zluri (enterprise) require months of implementation and start at $20K+/year — the SMB gap above Subsight persists.

**Risks:**
- Subsight could still decide to build SSO integration if they see sufficient demand. KILL CONDITION if they do.
- Substly already has basic SSO usage detection for Office 365.
- The SMB SaaS management space is genuinely competitive at every price point.

**Verdict:** Hold. Subsight's own product positioning confirms they will NOT enter the SSO-usage-data market — their blog post is a product strategy declaration, not just a gap. StackClean's SSO differentiation is structurally secured by Subsight's positioning choice.

### The Pitch
**Problem:** The average 50-person company runs 80+ SaaS subscriptions, with an estimated 30% unused or redundant. Bank-statement-based trackers (Subsight, CostLoop, Cledara) now exist for SMBs — but they miss the hidden zombie: the seat that is still being billed because the employee never formally cancelled, but also hasn't logged in for 4 months. Subsight's own blog article explicitly states that SSO/ERP integrations require a separate "Enterprise SaaS Management Platform" — because their bank-statement parser cannot see login history. Bank parsers see the charge. They cannot see the login.

**Solution:** StackClean connects to Google Workspace or Okta and surfaces every SaaS app with at least one user who has not logged in for 90 days. The weekly digest shows zombie seats by app, cost per zombie seat, and the specific users to deprovision. One click generates the cancellation shortlist with savings total.

**Target customer:** Ops lead / founder / IT admin at a 20–200 person company using Google Workspace or Okta SSO with 20+ SaaS applications. Buyer: Ops lead or CFO. May already use Subsight for invoice tracking — uses StackClean as the SSO layer Subsight cannot provide.

**Why now:** Subsight launched October 2026 and validated SMB SaaS management demand with 100+ early adopters — but confirmed bank-statement-only with no SSO integration, and explicitly positioned SSO as a different market. The SSO-based differentiation is the gap that Subsight's success and positioning make explicit.

**Why they buy without being sold to:** The Ops lead runs StackClean's free "zombie seat scan" (Google Workspace OAuth, 5 minutes), sees 12 unused seats across 4 apps totalling $2,700/year, and purchases the full tracker — even if they already have Subsight.

**Revenue model:** $149/month (Google Workspace, up to 100 users). $249/month (Okta, up to 250 users + team SaaS catalog). $399/month (SSO + bank statement + Slack + API). Annual −2 months. Free: one-time zombie scan showing top-5 zombie seats.

**Unfair advantage:** SSO login data reveals inactive seats that bank-statement parsers structurally cannot detect. Subsight's own product strategy validates the gap by explicitly NOT competing.

### Solo Build Plan
1. Weeks 1–3: Google Workspace Admin SDK OAuth; SSO login event ingestion; 90-day inactivity detection; SaaS app catalog from Workspace OAuth apps.
2. Weeks 4–5: Zombie seat report; weekly digest email + Slack.
3. Weeks 6–7: Okta connector; cancellation workflow.
4. Weeks 8–9: Stripe; free zombie scan (top-5 seats, no card required); Subsight comparison landing page.
5. Weeks 10–12: Pilot 10 companies via YC Startup School ops community and Product Hunt.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-16
**Strongest part:** Subsight's own blog post is a product strategy declaration that StackClean's SSO moat is structurally protected — they confirmed they won't enter this market.
**Open question:** Subsight has 100+ early adopters and momentum — if they reverse course and announce Workspace/Okta integration in the next 30 days, does StackClean's moat collapse before first revenue?

---

## #10 — ModelReg  ·  65/100  ·  DECLINED  ⚠️ FINAL WARNING
First added: 2026-09-11 | Last updated: 2026-10-23 | Score delta this week: -2

> Prove your community bank's AI governance to the next Fed examiner — without ValidMind's price tag.

### Score Breakdown
- Solo Buildability:   13/20  (unchanged — model inventory + validation status + drift alerts + exam prep; community bank feature set is simpler than enterprise)
- Value Clarity:       14/20  (unchanged — "OCC exam asks for your model inventory" is a 10-second pitch for any CRO)
- Market Timing:       8/20  (-2 — no community bank exam pressure signal found for a second consecutive run; SR 26-2 explicitly confirmed as "$30B+ primarily" with community banks carved out unless model use is significant; OCC Bulletin 2025-26 explicitly stated annual validation is NOT a community bank requirement; ABA and ICBA community banking news produces no SR 26-2 exam findings for community banks; ModelReg thesis depends on exam pressure that has not materialized in two consecutive research cycles)
- B2B Monetisation:    16/20  (unchanged — community banks pay six figures in fines; $500–1500/month is trivially justified if triggered)
- Pull Factor:         14/20  (unchanged — banking exam prep is word-of-mouth within community banking networks)

**Strengths:**
- AegisAI (confirmed competitor) is a template+assessment service — no recurring monitoring SaaS. Community banks that buy AegisAI still lack ongoing model monitoring.
- ValidMind AWS Marketplace: $5,000/model/year — still far above community bank range.
- Openlayer's Basic tier is FREE but limited to 1 member and 5 projects.

**Risks:**
- SR 26-2 scope confirmed as "$30B+ primarily" — community banks are explicitly less exposed than previously modeled.
- OCC explicitly clarified annual validation is not a community bank requirement — the exam pressure driver is weaker.
- No community banking association (ABA, ICBA) news found about SR 26-2 exam findings at community banks in two consecutive runs.

**Verdict:** FINAL WARNING. SR 26-2 community bank exam pressure signal has failed to materialize in two consecutive research cycles. Remove next run unless (a) ABA/ICBA publishes SR 26-2 exam feedback for community banks under $10B, or (b) OCC issues RFI on community bank AI governance citing examination findings.

### The Pitch
**Problem:** SR 26-2, issued jointly by the Federal Reserve, OCC, and FDIC on April 17, 2026, extends model risk management expectations to AI systems, LLMs, and agentic architectures. While explicitly most relevant to banks over $30B in assets, community banks under $10B that have adopted vendor AI tools, fintech partnerships, or automated lending decision systems are also receiving examiner questions. ValidMind lists $5,000/model/year on AWS Marketplace. AegisAI offers template packs and one-time assessments — not recurring monitoring SaaS.

**Solution:** ModelReg is the model risk management SaaS sized for community banks and fintechs under $10B. It maintains the model inventory, tracks validation status and next-review dates, sends alerts when a model's performance metrics drift, and generates an exam-prep package aligned to SR 26-2 evidence expectations.

**Target customer:** Chief Risk Officer / Model Risk Officer at a community bank or fintech under $10B in assets that has adopted vendor AI tools. Buyer: CRO or CCO. Users: model risk team (1–3 people) and internal audit.

**Why now:** SR 26-2 exam cycles began Q2 2026. Community banks with fintech partnerships or vendor AI tools are in scope despite the primary applicability threshold. AegisAI validates demand but is template-only.

**Why they buy without being sold to:** A CRO receives an MRA citing "inadequate model inventory and validation documentation." They search "community bank SR 26-2 compliance software," find ModelReg's free 10-model inventory, and convert when they see the gap between their documentation and examiner expectations.

**Revenue model:** $499/month (up to 20 models). $799/month (up to 50 models + exam prep pack). $1,499/month (unlimited models + audit integration + board reporting). Annual −2 months. Free: 10-model inventory assessment.

**Unfair advantage:** Sized for SR 26-2's proportionality principle at community bank price point. First-mover SEO on "community bank SR 26-2 compliance" before Openlayer/Yields build a self-serve SMB tier.

### Solo Build Plan
1. Weeks 1–3: Model inventory; validation status tracker; document upload per model.
2. Weeks 4–5: Drift alert framework; vendor model diligence module.
3. Weeks 6–7: SR 26-2 evidence gap analysis; exam-prep package export.
4. Weeks 8–9: Stripe; free 10-model inventory; ABA/ICBA community bank newsletter placements.
5. Weeks 10–12: Pilot 5 community banks through state banking association networks.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-10-23
**Strongest part:** AegisAI's template-only nature confirms the monitoring gap exists; ValidMind $5K/model confirms the price gap.
**Open question:** SR 26-2 is explicitly most relevant to $30B+ banks — is the community bank segment actually experiencing exam pressure from this guidance, or is ModelReg solving a problem community banks don't yet feel? REMOVAL TRIGGER: No ABA/ICBA community bank exam signal by next run = immediate removal.

---

## Removed this run
| Entry | Last score | New score | Reason |
|-------|-----------|-----------|--------|
| ImpactDeck | 70 | 63 | SimpleAct (live: FRIA + DPIA + version history + audit trail) and Nordis (live: AI Act + GDPR + RoPA + DPIA + monitoring + evidence vault) both shipped combined FRIA+DPIA lifecycle management in October 2026. The "lifecycle vs. static PDF" moat now faces 4+ direct live competitors (SimpleAct, Nordis, GeraCompliance, Grecta). elladoc DPIA still planned but irrelevant — SimpleAct and Nordis already cover the combined lifecycle gap ImpactDeck was built to fill. Displaced by MCPDock (69). |
