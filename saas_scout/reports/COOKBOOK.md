# SaaS Opportunity Cookbook
Last updated: 2026-10-16 | Entries: 10/10

> R17 note: **AgentCreds removed** — Bifrost virtual key lifecycle (per-VK MCP allowlist auto-sync, orphaned-credential reconciliation) and Arcade immutable per-action audit logs are expanding into the credential management layer; the machine-vs-user identity distinction requires too much buyer education at -3 from Run 16. **IntegWatch enters** — 2026 State of Agentic Integrations report quantifies integration reliability as the #1 agentic AI blocker (52% of companies); no product monitors per-customer OAuth connection health specifically for agentic SaaS. **ModelReg displaced** — SR 26-2 applicability scope explicitly confirmed as "$30B+ primarily"; community banks are formally carved out unless model use is significant. **CRAReport +1** — ENISA SRP v1.1 released Oct 12 with no API announcement; version churn confirms ongoing workflow burden. **WorkAuditAI +2** — zero HRIS vendor shipped CA AI module; Hirschfeld Kraemer "Five-Step Audit" confirms attorney referral channel active. **AgentAudit +1** — agentaudit.dev explicitly "free forever, no enterprise upsells" — paid SaaS tier gap confirmed permanent.

---

## #1 — CRAReport  ·  83/100  ·  IMPROVED
First added: 2026-09-11 | Last updated: 2026-10-16 | Score delta this week: +1

> Cut your CRA vulnerability reporting time from hours to minutes — the ENISA SRP portal has no API, so someone has to bridge it.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — SRP form automation + multi-step deadline tracker + evidence ZIP; achievable solo in 3 months)
- Value Clarity:       19/20  (unchanged — SRP is LIVE; first users experiencing manual pain IN PRACTICE; "I just submitted my first SRP notification and it took 3 hours" is now real testimony)
- Market Timing:       19/20  (+1 — SRP v1.1 released Oct 12, 2026 — just 4 days ago; version updates create new AR documentation burden and confirm ENISA is actively evolving without an API; open-source software steward obligations kick in Dec 11, 2027, extending the opportunity timeline further)
- B2B Monetisation:    17/20  (unchanged — EU manufacturers already pay legal/compliance consultants €5K+ per vulnerability incident; $200–500/mo is cheap by comparison)
- Pull Factor:         13/20  (unchanged — EU product security communities share pain; PSIRTs and DevSecOps channels are active; first-mover SEO on "CRA SRP reporting" captures search)

**Strengths:**
- ENISA FAQ still explicitly states "no API will be provided at the initial release" — this is official policy, not speculation. The moat is permanent until ENISA changes course publicly.
- SRP v1.1 released Oct 12, 2026 with updated documentation — version churn means ARs must re-learn the workflow; the multi-step form complexity is confirmed ongoing.
- The multi-step notification structure (Early Warning → 72h → Final Report) creates ongoing workflow value, not a one-time form.

**Risks:**
- If ENISA announces an API roadmap date, the kill condition is known and the window closes.
- The SRP is used by Assigned Representatives (ARs) — the buyer is the EU representative role, which may be outsourced to a legal firm.
- Initial adoption base is EU manufacturers; non-EU companies exporting to EU may lag 6–12 months.

**Verdict:** Hold #1. SRP v1.1 live with no API. Version churn reinforces the opportunity. First-mover SEO window still open.

### The Pitch
**Problem:** From September 11, 2026, manufacturers of products with digital elements sold in the EU must report actively exploited vulnerabilities and severe incidents through ENISA's Single Reporting Platform (SRP). The SRP has no API at initial release — every submission requires a human to log in with EU Login + MFA, navigate the 5-step form workflow, submit an Early Warning within 24 hours, a 72-hour Notification, and a Final Report, with each step having distinct mandatory fields. ENISA released SRP v1.1 on October 12, 2026 with updated guidance — version changes require ARs to re-read 55-page documentation and relearn form fields. A software manufacturer releasing 50 products across 10 EU member states could face dozens of concurrent active notifications at different stages, each with deadline clocks running in parallel. The ENISA FAQ explicitly states: "no Application Programming Interface (API) will be provided at the initial release of the SRP, so notifications must be submitted through the platform interface. API functionality may be considered in a future phase."

**Solution:** CRAReport is the workflow manager that sits above the SRP portal. You log incidents in CRAReport with product ID, affected versions, and CVSS data. CRAReport tracks the three-stage deadline clock for each incident, pre-fills the SRP form fields from your incident data, and prompts the AR at the right moment to review and submit each stage. Evidence attachments are managed in one place. At audit time, you export the full incident folder: submission timestamps, field values, reviewer log.

**Target customer:** Product security / PSIRT lead or Assigned Representative at a 20–500 person EU software or IoT hardware manufacturer. Buyer: CISO or Head of Product Security. User: the AR who physically submits to the SRP portal. Not a tier-1 telco; not a one-person indie — mid-market manufacturers with 5–50 covered products.

**Why now:** The SRP went live September 11, 2026. SRP v1.1 released October 12. ENISA FAQ explicitly confirms "no API." The first month of real usage is generating firsthand pain from ARs experiencing the manual workflow for the first time. No automation tooling exists. First-mover SEO on "CRA SRP reporting software" is unclaimed.

**Why they buy without being sold to:** An AR who just spent 3 hours submitting their first SRP Early Warning notification — filling in 40+ fields across 5 screens, losing their session once, and manually cross-checking the 72-hour deadline — searches for "CRA SRP reporting tool" and finds CRAReport. The free single-incident trial shows the workflow takes 15 minutes instead of 3 hours.

**Revenue model:** $199/month (1–10 concurrent active incidents; 3 products). $349/month (up to 30 incidents; 15 products; deadline dashboard). $599/month (unlimited incidents + multi-AR team + audit export). Annual −2 months. 14-day trial.

**Unfair advantage:** First-mover SEO in a regulation that went live 5 weeks ago. The product is the bridge that ENISA's FAQ says will not be built on their side. Community content strategy: publish "CRA SRP guide for ARs" that ranks before ENISA's own guidance.

### Solo Build Plan
1. Weeks 1–3: ENISA SRP form field mapping (v1.1 schema); incident data model (product, version, CVE, classification, CVSS); 3-stage deadline clock (24h / 72h / Final).
2. Weeks 4–5: Deadline dashboard; Slack/email alerts per stage; multi-incident view for practices with parallel active incidents.
3. Weeks 6–7: Evidence attachment manager; pre-fill export (field-by-field SRP mapping for AR review); incident audit log.
4. Weeks 8–9: Stripe; free single-incident trial; SEO content ("CRA SRP reporting guide for manufacturers").
5. Weeks 10–12: Pilot 5 EU manufacturers via ENISA CRA community channels and EU product security (PSIRT) Slack groups.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-10-09
**Strongest part:** ENISA's own FAQ is the product roadmap — they confirm the gap in writing. SRP v1.1 confirms ongoing evolution without an API.
**Open question:** If ENISA publishes an API roadmap date in Q1 2027, does CRAReport's exit strategy depend on being acquired by a GRC platform before that API ships?

---

## #2 — WorkAuditAI  ·  79/100  ·  IMPROVED
First added: 2026-10-09 | Last updated: 2026-10-16 | Score delta this week: +2

> Know which AI tools your managers rely on before the January deadline does.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — AI tool inventory form + SB 947 decision documentation workflow + Cal/WARN template generator; form-based, no HRIS integration in v1; solo-buildable in 3 months)
- Value Clarity:       17/20  (+1 — Hirschfeld Kraemer published a specific "Five-Step Audit" article with Step 1 as "inventory your AI tools" — GC who reads this advisory understands the product in 30 seconds without a pitch; multiple law firms now have named compliance frameworks that map directly to WorkAuditAI's product)
- Market Timing:       18/20  (unchanged — AB 1883 + SB 951 effective Jan 1, 2027; 11 weeks; zero SaaS competitor shipped; ADP/Workday confirmed no CA-specific module in active development; NY AI Labor Information Act passed both chambers awaiting Hochul signature, expanding TAM)
- B2B Monetisation:    15/20  (unchanged — HR/legal compliance budget exists at 100+ employee companies; $199–599 is a clear value purchase)
- Pull Factor:         14/20  (+1 — Hirschfeld Kraemer "Five-Step Audit" article + Morgan Lewis advisory + Plutux.ai analysis all published within days of signing; attorney referral network confirmed active; law firm distribution confirmed as a zero-CAC channel that started immediately)

**Strengths:**
- Three California laws signed 16 days ago — no competing SaaS exists. ADP and Workday confirmed rebuilding marketing/sales collateral around the new rules, NOT shipping new compliance modules.
- Multiple employment law firms published specific "Five-Step Audit" frameworks within days of signing — Step 1 in every framework is "inventory your AI tools," which IS the WorkAuditAI product's free tier.
- NY AI Labor Information Act passed both chambers (June 2026) awaiting Governor Hochul's signature — if signed, TAM expands beyond California significantly.

**Risks:**
- Governor Newsom's signing message noted AB 1883 "lacks key definitions" — regulatory ambiguity could narrow the addressable problem.
- ADP / Workday could add a "California AI laws" module using existing HRIS integrations — Plutux.ai estimates 9-month window before large vendors catch up.
- California-only scope limits TAM initially; other states (NY, IL) may follow but timeline uncertain.

**Verdict:** Enter immediately. Attorney advisory distribution + Jan 1 deadline = near-zero CAC acquisition window that closes in 11 weeks. No HRIS vendor confirmed to be shipping a competing module.

### The Pitch
**Problem:** On September 30, 2026, California signed three workplace AI laws: SB 947 (effective July 1, 2027) prohibits relying solely on automated decision systems for discipline or termination, requiring documented human review; AB 1883 (effective January 1, 2027) restricts AI-powered surveillance tools that infer employee emotions or collect neural data; SB 951 (effective January 1, 2027) requires enhanced Cal/WARN disclosures when automation drives qualifying layoffs. HR and legal teams at 100–2,000 person companies with California workers must now: inventory every AI tool influencing an employment decision, document independent human review for ADS-based discipline/termination decisions, assess and restrict AI surveillance tools, and update Cal/WARN procedures. Hirschfeld Kraemer, Morgan Lewis, and Baker Donelson published client advisories with identical Step 1: "conduct a straightforward audit of the software and platforms your company uses to hire, manage, monitor, evaluate, or terminate California-based employees." No purpose-built SaaS exists.

**Solution:** WorkAuditAI is the compliance operating layer for California's workplace AI laws. It runs a guided AI tool inventory (what tools, which HR decisions do they influence, which California employees are affected), then builds a workflow for each obligation: a surveillance tool classifier (AB 1883), a mandatory human-review documentation workflow for ADS-influenced discipline decisions (SB 947), a Cal/WARN AI-disclosure template generator (SB 951), and an audit trail exportable to counsel or regulators on demand.

**Target customer:** HR Director / VP People or General Counsel at a 100–2,000 person company with at least 50 California-based employees. Buyers: GC and CHRO jointly. Users: HR Operations and HR Business Partners who document employment decisions. Industries: tech, finance, logistics — any employer using AI-assisted performance management, productivity monitoring, or hiring tools.

**Why now:** SB 947, AB 1883, and SB 951 were all signed September 30, 2026 — 16 days ago. AB 1883 and SB 951 take effect January 1, 2027 (11 weeks away). SB 947 takes effect July 1, 2027. Employment attorneys are issuing specific "Five-Step Audit" frameworks this week. No SaaS tool built for these laws exists. ADP and Workday are rebuilding sales collateral, not shipping modules. The 11-week window is the highest-urgency, zero-competition acquisition moment this product will ever have.

**Why they buy without being sold to:** An employment attorney sends a client advisory about SB 947 with a "Five-Step Audit." Step 1 is "inventory your AI tools." The GC googles "California SB 947 compliance software" or "workplace AI audit tool," finds WorkAuditAI's free AI inventory form, completes Step 1 in 20 minutes, and purchases the full workflow to complete Steps 2–5 the same afternoon.

**Revenue model:** $199/month (1–50 CA employees; AI inventory + AB 1883 surveillance classifier + SB 951 Cal/WARN template). $349/month (50–300 CA employees + SB 947 human-review documentation workflow + employee data-request response). $599/month (300+ CA employees + counsel export pack + RBAC + full audit trail). Annual −2 months. Free: guided AI tool inventory (Step 1 of every attorney checklist) with no purchase required.

**Unfair advantage:** First SaaS built specifically for California's September 30, 2026 workplace AI laws. Employment attorney referral networks distribute at zero CAC — the free inventory IS the product firms recommend to clients. First-mover SEO on "California SB 947 compliance," "AB 1883 workplace AI," and "workplace AI risk assessment" before any competitor exists.

### Solo Build Plan
1. Weeks 1–2: CA Workplace AI intake questionnaire; AI tool inventory (HR systems, productivity monitors, hiring tools, performance management); decision-category mapping (hiring, performance, discipline, layoff).
2. Weeks 3–4: AB 1883 surveillance tool classifier (infer emotion / collect neural data); SB 947 decision workflow (ADS flag → independent human review form → corroboration record → written post-use notice generator).
3. Weeks 5–6: Cal/WARN AI-disclosure template (SB 951 layoff disclosure language); employee data-request response workflow (SB 947 § data description obligation).
4. Weeks 7–8: Stripe; attorney partnership landing page; SHRM and HR compliance newsletter placements.
5. Weeks 9–12: Pilot 10 companies through employment counsel referrals (Hirschfeld Kraemer, Morgan Lewis advisories cite "Workplace AI Risk Assessment" — contact those firms' labor practice groups).

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-10-16
**Strongest part:** Attorney "Five-Step Audit" frameworks published by multiple firms within days of signing create a distribution channel that costs nothing and starts immediately — the law firm IS the sales team.
**Open question:** Will ADP or Workday ship a "California AI laws" compliance module within 9 months (before SB 947 goes live July 1, 2027), leveraging HRIS integrations to provide richer automated audit trails than a form-based tool can?

---

## #3 — DentPay  ·  78/100  ·  UNCHANGED
First added: 2026-07-16 | Last updated: 2026-10-09 | Score delta this week: —

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — CSV-first rule engine; dentpay.tech pilot confirms the technical approach is correct)
- Value Clarity:       19/20  (unchanged — dentpay.tech piloting with real practices validates market; "same total with three flagged lab mismatches" is a demonstrable live demo)
- Market Timing:       17/20  (unchanged — Samera.ai still UK-only; dentpay.tech still in pilot "leave your email" mode; no paying customers at scale confirmed for any US production-pay tool)
- B2B Monetisation:    16/20  (unchanged)
- Pull Factor:         10/20  (unchanged — dentpay.tech capturing early study-club referral channel)

**Strengths:**
- dentpay.tech (ClinixFlows) launched May 2026 as "revenue infrastructure" — still in pilot mode; no announced paying customer scale or funding raise; competition is pre-revenue.
- Samera.ai's UK "how it works" page explicitly shows "Dentally and Xero" API link — the US Open Dental / Dentrix path is still unclaimed by any live product at scale.
- Production % pay reconciliation remains a distinct category from general payroll — Gusto/ADP have no production split logic.

**Risks:**
- dentpay.tech is directly executing the same thesis; first-mover distribution advantage is being captured.
- Dental Intelligence (analytics) or Open Dental itself could deepen native pay math in a feature update.
- Relationship-heavy sales; CPA/advisor trust needed for paycheck-math credibility.

**Verdict:** Hold. dentpay.tech validates the market but is in pilot stage; differentiation is possible on Dentrix+Eaglesoft path or multi-location PE group pricing.

### The Pitch
**Problem:** US dental practices paying associates and hygienists on production still spend hours each pay period exporting Open Dental or Dentrix reports, pasting into Excel, applying lab fees, write-offs, and card-fee rules, then hoping the spreadsheet matches the contract. Open Dental's Provider Payroll report is raw material, not a pay engine. Samera automated this for UK Dentally+Xero; Gusto deposits pay but does not reconcile OD production rules. HRPayPick 2026 confirms no payroll platform has native plug-and-play integration with all three major US PMS systems. dentpay.tech is piloting but still pre-scale — the market is large enough for competition.

**Solution:** DentPay imports OD/Dentrix production exports, applies per-provider pay rules once, flags anomalies before payout, and exports an approval pack to Gusto/ADP. Office managers review exceptions; they do not rebuild formulas.

**Target customer:** Office manager / owner at 1–3 location US dental practice on Open Dental or Dentrix with associates or hygienists on production splits.

**Why now:** Production % pay still the norm; UK tools (Samera/Dentivize) proved analytics willingness-to-pay; US PMS vendors have not productised the reconciliation layer.

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
**Strongest part:** dentpay.tech piloting confirms the thesis with real market evidence; ClinixFlows has not announced funding or paying customer scale — the first-mover advantage is still contestable.
**Open question:** Does dentpay.tech's head start in the study-club referral channel foreclose the primary distribution path for a second entrant, or does the dental community's fragmentation leave room for a Dentrix-focused alternative?

---

## #4 — IntegWatch  ·  72/100  ·  NEW
First added: 2026-10-16 | Last updated: 2026-10-16 | Score delta this week: —

> Know which customer's integration is about to fail before your AI agent exposes it.

### Score Breakdown
- Solo Buildability:   15/20  (OAuth token expiry detection for top-10 integrations + per-customer uptime tracking; main complexity is handling different OAuth refresh flows per provider; achievable solo in 3 months)
- Value Clarity:       16/20  (free connection health scan shows specific at-risk customers immediately; "8 customers' Salesforce tokens expire this week" is self-evident to any engineering lead who has experienced silent agent failures)
- Market Timing:       16/20  (2026 State of Agentic Integrations report: integration reliability is the #1 agentic AI deployment blocker at 52%; no product monitors per-customer OAuth connection health specifically for agentic SaaS; emerging NOW because AI agents made integration failures existential)
- B2B Monetisation:    14/20  ($199–799/month for agentic SaaS company; integration monitoring is a recognized spend category; clear cost-avoidance ROI from prevented enterprise deal losses)
- Pull Factor:         11/20  ("we prevented 8 customer integrations from failing before the agent hit them" is a shareable CS team story; distribution through Nango/Apideck/Ampersand developer communities where target customers already live)

**Strengths:**
- 2026 State of Agentic Integrations report (Ampersand, June 2026): 52% cite integration reliability as #1 agentic blocker; 68% spend 25%+ of engineering time maintaining integrations; 68% lost/delayed enterprise deals due to integration security/compliance concerns — all three metrics point at the same gap.
- Existing integration infrastructure tools (Nango, Merge, Apideck) help companies build better integrations but do NOT surface per-customer connection health to the CS team — the customer-scoped view is structurally absent from their dashboards.
- The "free connection scan showing token expiry dates" is a self-closing conversion mechanism: the product demonstrates the problem before the trial ends.

**Risks:**
- Nango, Apideck, or Merge could add "customer connection health alerts" as a native feature — they already have the per-customer connection data and clear incentive.
- Datadog/PagerDuty can monitor API calls; enterprise teams may build custom alerting rather than pay $199/month.
- The market of "agentic SaaS companies with 50+ customer connections" may be smaller than the broader integration reliability pain suggests — some are very small teams.

**Verdict:** Enter as the per-customer integration health monitor for agentic SaaS companies. The customer-CS framing (not just engineering monitoring) is the structural moat over platform-native monitoring.

### The Pitch
**Problem:** B2B SaaS companies shipping AI agents in 2026 depend on their customer-facing integrations being reliable. The 2026 State of Agentic Integrations report found that integration reliability is the #1 blocker to shipping AI agents, cited by 52% of companies — ahead of hallucinations and engineering bandwidth. Engineering teams spend 25%+ of their time maintaining existing integrations. Most critically: 68% of B2B SaaS companies have lost or delayed enterprise deals because of integration-related security or compliance concerns. When an AI agent fails because a customer's Salesforce OAuth token silently expired three weeks ago, the first notification is a customer ticket — or worse, a churn email. Existing monitoring tools alert on server failures and API latency. None surface "Customer Acme Corp's HubSpot connection has been failing silent retries for 4 days" before the customer notices.

**Solution:** IntegWatch monitors every customer's OAuth connection to the integrations your AI agents depend on. You define which integrations matter for each customer tier; IntegWatch checks them on a configurable schedule, catches expired tokens before they fail in production, flags rate limit approach, and opens a Slack alert with the specific customer name, integration, and error reason before your agent fails visibly. The CS team sees "3 customers at risk this week" in a dashboard ordered by tier — not a generic API error log.

**Target customer:** Engineering lead / VP Engineering at a 15–100 person B2B SaaS company that has shipped AI agents to paying customers with 5+ customer-facing integrations. Buyer: VP Engineering or CTO. Users: (1) engineers who own integration on-call and (2) CS team who proactively reach out before customers notice. Does not replace Nango/Merge/Apideck — sits on top of them as the reliability layer.

**Why now:** The 2026 State of Agentic Integrations report is the clearest catalyst — integrations "used to be background data pipes. Now, they are the bottleneck for the AI era." When integrations fail in an agentic product, the AI agent misbehaves — consequences are immediate, visible, and sometimes irreversible. No product monitors per-customer OAuth connection health specifically for agentic companies. Nango, Merge, and Apideck users can add IntegWatch without replacing anything.

**Why they buy without being sold to:** An engineering lead whose agent silently failed for 12 customers because their Salesforce OAuth tokens expired on the same day — and who found out through customer tickets — runs IntegWatch's free connection health scan. The scan shows 8 more customers with tokens expiring in the next 14 days. They purchase before the scan completes.

**Revenue model:** $199/month (up to 50 monitored connections; 5 integrations; 15-minute polling; Slack alerts). $399/month (up to 250 connections; 20 integrations; 5-minute polling; PagerDuty + webhook). $799/month (enterprise: unlimited connections + SLA-mode monitoring + per-customer uptime reports + customer-facing status page integration). Annual −2 months. Free: one-time connection health scan (token expiry dates + recent error rates; no polling setup required).

**Unfair advantage:** Customer-scoped view ("Acme Corp's Salesforce connection has a 94% uptime this quarter vs. your 98.3% average") that platform-native dashboards are not designed to surface to CS teams. Distribution through Nango/Apideck/Ampersand developer communities where target customers already live. First-mover SEO on "agentic integration monitoring" and "AI agent OAuth connection monitoring."

### Solo Build Plan
1. Weeks 1–3: OAuth token expiry detection for top-10 integrations (Salesforce, HubSpot, Slack, Google, GitHub, QuickBooks, Shopify, Zendesk, Notion, Airtable); per-customer connection health dashboard (last checked, token status, recent error rate).
2. Weeks 4–5: Polling scheduler (15-min/5-min tiers); Slack alert on token expiry warning (48h/24h/expired); rate limit proximity alerts; customer-tier tagging.
3. Weeks 6–7: Per-customer uptime report (monthly rolling); integration reliability dashboard (% uptime per integration across all customers); error pattern detection.
4. Weeks 8–9: Stripe; free connection scan (token expiry + error rates, no polling required); PagerDuty integration; CS team view (at-risk customers ordered by ARR tier).
5. Weeks 10–12: Pilot 8 agentic SaaS companies through Ampersand developer community, Nango Discord, and 2026 State of Agentic report share communities.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-16
**Strongest part:** The 2026 State of Agentic report quantifies the exact problem with three distinct data points; the free token-expiry scan is a strong self-demonstrating conversion mechanism.
**Open question:** If Nango or Merge adds customer-scoped integration health alerts and proactive token refresh as a native feature, does IntegWatch's value proposition collapse immediately, or is the CS-layer framing (proactive customer outreach before failures, not just engineering alerting) a durable differentiation?

---

## #5 — AuthTrack  ·  70/100  ·  IMPROVED
First added: 2026-08-16 | Last updated: 2026-10-16 | Score delta this week: +1

> See which prior auths are inside the 7-day / 72-hour clock — and which denials still have no specific reason.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — CSV/fax log + calendar clocks + denial-reason fields; HIPAA applies)
- Value Clarity:       16/20  (unchanged — "this PA blows the CMS clock on Thursday" is obvious to a biller)
- Market Timing:       14/20  (+1 — AuthTrack Pro Aug 17, 2026 post reveals pivot toward "high authorization volume" teams — imaging facilities, hospitals, SNFs; the 2–10 provider small practice market is confirmed less contested; FHIR API mandate is 11 weeks away)
- B2B Monetisation:    14/20  (unchanged — $149–299/mo; one avoided write-off pays for a year)
- Pull Factor:         12/20  (unchanged — biller Facebook groups)

**Strengths:**
- AuthTrack Pro's Aug 2026 LinkedIn post reveals pivot toward "high authorization volume" healthcare organizations — imaging facilities, hospitals, SNFs. The 2–10 provider small practice market is explicitly the gap they're moving away from.
- Regulation is now 9.5 months live — buyers have documented losses that make the pain concrete and undeniable.
- FHIR API mandate (Jan 1, 2027) is 11 weeks away — practices building a log now will have the cleanest path to electronic attestation.

**Risks:**
- AuthTrack Pro is still building in this space; their upmarket pivot could reverse.
- Honey Health (agentic AI for end-to-end PA automation) is moving into smaller practices.
- Tiny practices may wait for their clearinghouse to add a free clock tracker.

**Verdict:** Hold. AuthTrack Pro's upmarket pivot opens the 2–10 provider small practice segment. The denial-reason audit pack and CMS clock export for appeals remain the differentiation.

### The Pitch
**Problem:** Since 1 January 2026, Medicare Advantage, Medicaid, CHIP, and FFE QHP payers must decide standard prior auths in 7 calendar days and urgent ones in 72 hours, and every denial must include a specific reason. Billing coordinators at 2–10 provider practices still track this in a spreadsheet next to the fax machine. They miss clocks, they cannot prove a vague denial, and they will need a clean log before 2027 electronic-PA attestation. AuthTrack Pro (authtrackpro.com) launched in June 2026 — but their August 2026 messaging reveals they're targeting "high authorization volume" teams at imaging facilities and hospitals, explicitly pivoting away from the 2–10 provider small practice.

**Solution:** AuthTrack is the PA status board with CMS-clock compliance: each request gets a deadline clock, a channel (fax/portal/phone), a required denial-reason field (vague denials are flagged), and an alert before the CMS window closes. At appeals time, you export a packet: submission date, payer clock, denial reason, follow-up log.

**Target customer:** Billing coordinator / office manager at a 2–10 provider US practice (PT, specialty lite, independent primary care) not on Athena+Linear Health. Buyer: office manager. User: the biller who owns the Excel PA tab.

**Why now:** The clocks are 9.5 months live. Practices that missed clock windows in January–October 2026 now have documented losses. The FHIR API mandate (1 Jan 2027) is 11 weeks away — practices building a log now will have the cleanest path to electronic attestation. AuthTrack Pro's upmarket pivot is confirmed, leaving the small-practice segment less contested.

**Why they buy without being sold to:** After a denied MRI with no specific reason and a missed 7-day follow-up, the biller pastes the spreadsheet into AuthTrack, sees two clocks already red, and stops using Excel that week.

**Revenue model:** $149/mo (1 location, 200 PAs). $249/mo (3 locations + reminder SMS). $299/mo (export pack for appeals). Annual −2 months. 14-day trial with sample CSV.

**Unfair advantage:** CMS-clock breach documentation + denial-reason enforcement specifically for fax-era small practices that AuthTrack Pro's upmarket pivot leaves unserved.

### Solo Build Plan
1. Weeks 1–3: PA log (CSV import); 7-day / 72-hour clocks; denial-reason required on deny; vague-denial flag.
2. Weeks 4–5: Email/SMS reminders; aging report; appeal packet PDF (submission date + clock + denial reason + follow-up log).
3. Weeks 6–7: HIPAA BAA flow; audit log; role-based access.
4. Weeks 8–9: Stripe; sample-CSV onboarding.
5. Weeks 10–12: Pilot 6 small practices via biller Facebook groups and local MGMA chapters.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-16
**Strongest part:** AuthTrack Pro's explicit upmarket pivot (August 2026) leaves the small-practice market less contested than it appeared 4 weeks ago.
**Open question:** Will AuthTrack Pro reverse their upmarket pivot and return to the small-practice segment if their enterprise targets prove too complex to acquire?

---

## #6 — ImpactDeck  ·  70/100  ·  IMPROVED
First added: 2026-09-11 | Last updated: 2026-10-16 | Score delta this week: +1

> Manage your FRIA and DPIA as a living record — not a PDF you generate once and forget.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — FRIA + DPIA workflow builder + version history; clean SaaS build)
- Value Clarity:       15/20  (unchanged — "show me your FRIA" from an auditor = immediate trigger)
- Market Timing:       13/20  (+1 — elladoc GDPR DPIA module confirmed STILL "Planned" as of October 2026; ellamind's product page shows "Planned: DPIA, Art. 9, Art. 35" — the combined lifecycle gap is confirmed open; EU AI Act compliance software market growing at $1.14B in 2026 → $4.05B by 2031)
- B2B Monetisation:    14/20  (unchanged)
- Pull Factor:         14/20  (unchanged — EU AI Act communities share tools; DPO networks are active)

**Strengths:**
- elladoc's DPIA module is explicitly "Planned" on their product page as of October 2026 — the combined FRIA+DPIA lifecycle in a persistent, version-controlled system is confirmed still unclaimed.
- teamazing.com 2026 analysis states "tools missing any of these four modules [Art. 30 processing register, AI Act risk classification, DPIA, unified audit log] are no longer competitive" — validates the combined approach.
- Static generators (KLA, AI DPIA Pro) validate demand but export PDF — no lifecycle management, no version history, no change triggers.

**Risks:**
- elladoc's roadmap includes DPIA — when GDPR DPIA ships, ellamind becomes a direct full-stack competitor.
- The Annex III high-risk deadline shift to December 2027 reduces urgency for the broader high-risk AI market.
- Demand from specifically-obligated Aug 2 cohort may be smaller than total high-risk AI Act market suggested.

**Verdict:** Hold. The lifecycle management moat (vs static PDF generators) is real. The window is 3–6 months before elladoc ships DPIA.

### The Pitch
**Problem:** EU AI Act Article 27 FRIA obligations have been live since August 2, 2026 for specifically-obligated deployers — credit scoring (Annex III §5(b)), life and health insurance pricing (§5(c)), and private entities providing public services. GDPR Article 35 DPIA has been mandatory for high-risk data processing since 2018. Both assessments involve overlapping risk identification, stakeholder mapping, and mitigation planning. Free static generators (KLA Digital's browser-based DPIA+FRIA, AI DPIA Pro) validate demand and produce a one-time PDF. elladoc covers Art. 27 FRIA in its documentation workflow. None provide a persistent, versioned lifecycle record: when your AI system changes, when your vendor's model is updated, when a regulatory Q&A shifts your risk classification — there is no system that re-triggers assessment and tracks the delta.

**Solution:** ImpactDeck is the FRIA + DPIA lifecycle manager. The initial assessment is guided and fast (30–60 minutes). Every subsequent system change, vendor update, or regulation clarification triggers a version-controlled review. The audit trail shows who assessed what, when, what changed, and what the current risk status is. Regulators and DPOs can see a living record, not a stale PDF dated to initial deployment.

**Target customer:** Data Protection Officer / AI Governance Lead at a 50–500 person EU company deploying high-risk AI systems. Buyer: DPO or GC. User: DPO + the team implementing the AI system.

**Why now:** Art. 27 FRIA obligations are live for specifically-obligated deployers. No lifecycle tool exists — only static generators. elladoc's DPIA module is still "planned." The window to establish as the lifecycle standard is 3–6 months before elladoc ships DPIA.

**Why they buy without being sold to:** A DPO who generated a FRIA PDF 3 months ago is asked "has anything changed since the initial FRIA?" They have no answer — the PDF is stale and there's no audit trail. ImpactDeck's change-triggered review workflow makes that question answerable in 5 minutes.

**Revenue model:** $199/month (1 AI system; FRIA + DPIA; version history). $349/month (5 systems + multi-user + DPO dashboard). $599/month (unlimited systems + API + regulator export). Annual −2 months. Free: single FRIA assessment (PDF export; no lifecycle features).

**Unfair advantage:** Version-controlled lifecycle record vs static PDF generators. Combined FRIA+DPIA in one flow matches CNIL's April 2026 harmonised template. Distribution through DPO networks and EU AI Act compliance forums where ellamind/KLA are not yet present.

### Solo Build Plan
1. Weeks 1–3: Art. 27 FRIA guided questionnaire (10 sections from ENISA/CNIL templates); GDPR Art. 35 DPIA sections; shared risk register.
2. Weeks 4–5: Version history + change trigger (system update → re-assessment prompt); delta view between versions.
3. Weeks 6–7: DPO dashboard (all active systems + FRIA/DPIA status + next review date); regulator export (PDF + JSON).
4. Weeks 8–9: Stripe; free FRIA generator (PDF) as lead gen; GDPR DPIA module.
5. Weeks 10–12: Pilot 6 companies through EU AI Act compliance Slack groups and CNIL / European DPO Association channels.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-16
**Strongest part:** elladoc's DPIA module confirmed "Planned" as of October 2026 — the combined lifecycle moat is confirmed open and will remain so for months.
**Open question:** When elladoc ships its planned GDPR DPIA module, does ImpactDeck's moat depend entirely on version history and lifecycle tracking, and is that enough to retain customers who can get FRIA+DPIA in one place from elladoc?

---

## #7 — AgentAudit  ·  68/100  ·  IMPROVED
First added: 2026-09-25 | Last updated: 2026-10-16 | Score delta this week: +1

> Block malicious MCP packages before they reach your production agent — not after the incident report.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — Trust Registry + GitHub App CI gate + team dashboard; agentaudit-dev OSS validates the architecture; the paid tier is the SaaS layer on top)
- Value Clarity:       15/20  (unchanged — agentaudit-dev's real Trust Registry with real packages proves this is a real security layer, not a hypothetical)
- Market Timing:       12/20  (+1 — agentaudit-dev explicitly "free forever, no enterprise upsells" — they will NOT build a commercial tier; the paid GitHub App + org-level policy + CISO dashboard is now confirmed permanently open as a complementary product, not a competitive threat)
- B2B Monetisation:    14/20  (unchanged — enterprise security budgets; supply chain security is a known spend category)
- Pull Factor:         13/20  (unchanged — incident post + "we blocked a malicious MCP package" story = eng Twitter virality)

**Strengths:**
- agentaudit-dev explicitly stated: "Free forever. No freemium tiers, no enterprise upsells. Security shouldn't be gated." — this is a confirmed commitment that removes the primary kill condition from Run 16.
- The paid SaaS tier (team dashboard + organization-level policy + continuous monitoring) is explicitly unlaunched and confirmed open.
- agentaudit.co.uk ("Agent Audit") is a completely separate product focused on AI receipts and audit evidence for compliance — NOT a competitor; confirms the MCP security registry space is distinct.

**Risks:**
- agentaudit-dev could reverse their "free forever" commitment if they need revenue.
- Cisco MCP Scanner and other OSS security tools are appearing — free alternatives may satisfy enough of the market.
- The "Trust Registry" as community-driven database has data quality risks.

**Verdict:** Hold with increased conviction — agentaudit-dev's "free forever" commitment removes the primary kill condition. The paid GitHub App + org-level dashboard is confirmed open.

### The Pitch
**Problem:** AI agents increasingly rely on Model Context Protocol (MCP) servers — npm packages that expose tools to models. The ecosystem has grown to 2,000+ MCP packages, with no systematic supply-chain security layer. agentaudit-dev's open-source AgentAudit CLI + Trust Registry validates real packages against known security findings. But it is "free forever" by design — no enterprise commercial tier will be built by the OSS project. Engineering teams need a team-level policy layer: org-wide package allowlists, a CI gate that blocks builds containing unauthorized MCP packages, a dashboard showing which packages each team is using and their current security status, and alerts when a previously-safe package gets flagged.

**Solution:** A SaaS layer on top of the open AgentAudit Trust Registry: GitHub App (not just Action) + org-level package policy + team dashboard. Every repository in the organization runs the scan automatically. New MCP package = instant Trust Registry check. Flagged package = PR blocked, reviewer alerted, audit record created. The CISO gets a dashboard showing every MCP package in use across all teams and their security status.

**Target customer:** CISO / Security Engineering lead at a 50–500 person company actively using MCP-based AI agents in production. Buyer: CISO or VP Engineering. Users: security team + each engineering team running AI agents.

**Why now:** agentaudit-dev's OSS proves the technical approach, validates real user demand (npm downloads), and provides a ready-made Trust Registry data source. The "free forever" commitment confirms the paid enterprise SaaS layer is permanently open. Inkog Labs (Oct 2026): 84% of scanned MCP server repos had security findings.

**Why they buy without being sold to:** After a security team discovers an MCP package with a prompt injection vulnerability that was silently used in production for 3 weeks, they install the AgentAudit GitHub App, see 14 other packages across 6 repos that need review, and purchase the enterprise dashboard to manage ongoing policy.

**Revenue model:** $199/month (up to 5 repos + Trust Registry scan + PR blocking). $399/month (up to 20 repos + org policy + Slack alerts). $799/month (enterprise: unlimited repos + CISO dashboard + custom risk rules + SOC 2 export). Annual −2 months.

**Unfair advantage:** Trust Registry data source (open, maintained by agentaudit-dev community) + GitHub App org-level policy layer that the OSS CLI cannot provide. Builds on, rather than competes with, the OSS — potential to partner with agentaudit-dev for official SaaS tier.

### Solo Build Plan
1. Weeks 1–3: GitHub App (vs standalone Action) with org-level installation; Trust Registry API integration; PR-blocking on unsafe packages.
2. Weeks 4–5: Org package allowlist policy builder; team dashboard (repos + packages + status); package change alerts.
3. Weeks 6–7: CISO summary report (org-wide MCP package inventory + risk distribution); custom risk rules.
4. Weeks 8–9: Stripe; free trial (unlimited repos, read-only; no PR blocking); security newsletter placements.
5. Weeks 10–12: Pilot 5 security-conscious engineering teams; explore partnership with agentaudit-dev for official hosted tier.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-16
**Strongest part:** agentaudit-dev's "free forever" commitment is now a confirmed structural feature of the market, not a temporary state — the paid SaaS tier is permanently open.
**Open question:** agentaudit-dev has AGPL + commercial license written and could reverse the "free forever" decision if funded. How durable is their commitment to free, and what is the signal to watch?

---

## #8 — CredVerify  ·  68/100  ·  UNCHANGED
First added: 2026-10-09 | Last updated: 2026-10-09 | Score delta this week: —

> Your 40-provider group's malpractice, DEA, and hospital privileges — one dashboard, no spreadsheet.

### Score Breakdown
- Solo Buildability:   11/20  (provider profile + renewal calendar + CAQH import + HIPAA BAA; state licensing data is publicly available but content work is substantial; achievable solo in 3 months if focused on top-5 states and 3 credential types first)
- Value Clarity:       14/20  (lapsed DEA registration = prescribing halt; voided payer contract = revenue loss; trigger events are immediate and concrete for any practice administrator)
- Market Timing:       15/20  (Alder VC 2026 explicitly names mid-market physician group credentialing as underserved; Modio Health acquired by Health Carousel, removing the primary mid-market option; enterprise incumbents symplr and Intellicheck start at $50K/year)
- B2B Monetisation:    16/20  (compliance-critical; one avoided lapsed malpractice certificate pays for 2 years of subscription; $299–799/month is defensible vs $50K enterprise alternative)
- Pull Factor:         12/20  (MGMA chapters and credentialing coordinator LinkedIn groups share tools; not publicly viral)

**Strengths:**
- Modio Health (the primary mid-market option) was acquired by Health Carousel — acquisition displacement creates a window for a dedicated replacement.
- CAQH profiles already hold most of the credential data practices maintain — CAQH import is a zero-friction onboarding path.
- Compliance-critical + immediate financial consequence (payer contract void) = high willingness to pay without extensive education.

**Risks:**
- HIPAA BAA required from day one — adds legal overhead for a solo founder.
- State licensing data accuracy across 50 jurisdictions requires ongoing maintenance — wrong renewal deadlines create liability.
- MGMA or a health-system-adjacent vendor could enter this segment with an existing provider directory.

**Verdict:** Enter with a narrow beachhead: top-5 US states, 3 credential types (DEA, state medical license, malpractice), CAQH import. Expand breadth only after first 10 paying customers.

### The Pitch
**Problem:** Physician groups, outpatient surgery centers, and specialty clinics with 10–100 providers manage credentialing — state medical license renewals, DEA registrations, malpractice coverage verification, hospital privilege expirations, and payer re-enrollment — manually. For a 40-provider orthopedic group, this means a full-time credentialing coordinator maintaining a spreadsheet of 200+ renewal dates across 50+ licensing jurisdictions and 15 payers. A single lapsed DEA registration halts prescribing. An expired malpractice certificate can void a payer contract mid-year. Enterprise credentialing platforms (symplr, Intellicheck, Verity) start at $50K/year. Modio Health — the closest mid-market option — was acquired by Health Carousel in 2026, leaving the 10–100 provider group without a purpose-built affordable alternative.

**Solution:** CredVerify is the centralized credentialing dashboard for mid-market physician groups. Each provider gets a profile with all their credentials, licenses, and renewals tracked in one place. The system alerts the credentialing coordinator 90/60/30 days before any expiration, generates a renewal preparation checklist per jurisdiction, and maintains a verification-ready record for payer audits and hospital privilege reapplications. v1 is database-first — CAQH import for onboarding, no EHR integration.

**Target customer:** Credentialing coordinator / Practice Administrator at a 10–100 provider specialty group (orthopedics, neurology, anesthesia, GI, dermatology) or outpatient surgery center in the US. Buyer: Practice Administrator or CFO. Users: credentialing coordinator (primary) + individual providers (self-service renewal prompts).

**Why now:** Modio Health's acquisition created an active vacancy in the mid-market credentialing tool category. Alder VC's 2026 analysis confirms the gap. Enterprise platforms start at $50K/year — 10x above what a 20–50 provider group will pay.

**Why they buy without being sold to:** After a provider's malpractice certificate lapses unnoticed and a payer contract voids mid-year, the administrator searches "physician credentialing tracking software group practice." CredVerify's free 5-provider tier shows a live renewal calendar. The administrator imports CAQH data, sees 3 expirations in the next 60 days that weren't on the coordinator's spreadsheet, and converts to paid the same session.

**Revenue model:** $299/month (1–20 providers; top-5 state licensing + DEA + malpractice). $499/month (21–60 providers + payer audit pack + hospital privilege tracking). $799/month (61–100 providers + CAQH sync + unlimited locations + reporting). Annual −2 months. Free tier: 5 providers, 3 credential types, renewal calendar.

**Unfair advantage:** CAQH import as zero-friction onboarding (most groups already maintain CAQH). Purpose-built for 10–100 provider groups that enterprise platforms ignore and that Modio Health no longer serves.

### Solo Build Plan
1. Weeks 1–3: Provider profile (DEA + state medical license + malpractice + hospital privileges); renewal calendar; 90/60/30-day email alerts; CSV import.
2. Weeks 4–5: CAQH profile import (CAQH ProView XML export parsing); document upload per credential type; payer audit export pack (verification-ready PDF).
3. Weeks 6–7: HIPAA BAA click-wrap; audit log; role-based access (admin vs coordinator vs provider self-service).
4. Weeks 8–9: Stripe; free 5-provider tier (no card required); FSMB data integration for state medical license verification.
5. Weeks 10–12: Pilot 5 groups through MGMA chapter demonstrations and credentialing coordinator LinkedIn groups (NAMSS).

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-09
**Strongest part:** Modio Health's acquisition created a real market gap at exactly the moment Alder VC is publishing research calling it underserved — rare confluence of displacement and validation.
**Open question:** Can a solo founder maintain accurate, current renewal deadline data across 50 state licensing jurisdictions without a credentialing domain expert, and what is the liability exposure if a renewal alert fires at the wrong deadline?

---

## #9 — StackClean  ·  67/100  ·  IMPROVED
First added: 2026-10-02 | Last updated: 2026-10-16 | Score delta this week: +1

> Kill the SaaS zombie seats before finance finds them on the card statement.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — Google Workspace/Okta API + SSO login history + SaaS catalog; technically straightforward)
- Value Clarity:       15/20  (unchanged — "here are 12 seats nobody has used in 90 days" is self-evident)
- Market Timing:       12/20  (+1 — Subsight confirmed as bank-statement-only with NO Google Workspace or Okta SSO integration; their own blog advises "cross-check SSO" as a manual step — explicitly validating the pain StackClean solves and confirming Subsight cannot detect the zombie seat StackClean targets)
- B2B Monetisation:    14/20  (unchanged — Subsight's waitlist pricing creates downward pressure; SSO-based differentiation is the only premium justification)
- Pull Factor:         12/20  (unchanged — ops/finance communities share "we saved $X" stories)

**Strengths:**
- Subsight confirmed: their "Integrations & Notifications" page lists only Slack; their blog advises manual SSO cross-checking as a separate step — the SSO usage data moat is confirmed intact.
- Subsight's bank-statement-parser approach misses apps billed annually (no monthly statement), SSO-only apps (no recurring card charge), and inactive seats that are still being billed.
- Zylo, Torii, Zluri (enterprise) require months of implementation and start at $20K+/year — the SMB gap persists above the Subsight price point.

**Risks:**
- Subsight could add Workspace/Okta integration in their first few months of live operation — KILL CONDITION if they do.
- Substly already has basic SSO usage detection for Office 365.
- The SMB SaaS management space is now genuinely competitive at every price point.

**Verdict:** Hold only on the SSO usage data moat. If Subsight announces Google Workspace/Okta integration in the next 4 weeks, remove immediately.

### The Pitch
**Problem:** The average 50-person company runs 80+ SaaS subscriptions, with an estimated 30% unused or redundant. Bank-statement-based trackers (Subsight, CostLoop, Cledara) now exist for SMBs — but they miss the hidden zombie: the seat that is still being billed because the employee never formally cancelled, but also hasn't logged in for 4 months. Subsight's own blog article on "SaaS cost audit" advises "cross-check SSO and ask teams directly" as a manual step — because their bank-statement parser cannot see login history. Bank parsers see the charge. They cannot see the login.

**Solution:** StackClean connects to Google Workspace or Okta (one OAuth click) and surfaces every SaaS app with at least one user who has not logged in for 90 days. The weekly digest shows: zombie seats by app, the cost per zombie seat per month, and the specific users to deprovision. One click generates the cancellation shortlist with savings total.

**Target customer:** Ops lead / founder / IT admin at a 20–200 person company using Google Workspace or Okta SSO with 20+ SaaS applications. Buyer: Ops lead or CFO. May already use Subsight for invoice tracking — uses StackClean as the SSO layer Subsight cannot provide.

**Why now:** Subsight launched October 2026 and validated SMB SaaS management demand with 100+ early adopters — but confirmed bank-statement-only with no SSO integration. The SSO-based differentiation is the gap that Subsight's success made explicit.

**Why they buy without being sold to:** The Ops lead runs StackClean's free "zombie seat scan" (Google Workspace OAuth, 5 minutes), sees 12 unused seats across 4 apps totalling $2,700/year, and purchases the full tracker before the free trial ends — even if they already have Subsight.

**Revenue model:** $149/month (Google Workspace, up to 100 users; zombie scan + weekly digest). $249/month (Okta, up to 250 users + team SaaS catalog + cancellation workflow). $399/month (SSO + bank statement + Slack + API). Annual −2 months. Free: one-time zombie scan showing top-5 zombie seats (Workspace only; no purchase required).

**Unfair advantage:** SSO login data reveals inactive seats that bank-statement parsers structurally cannot detect. Subsight's own documentation validates this gap by advising manual SSO cross-checking.

### Solo Build Plan
1. Weeks 1–3: Google Workspace Admin SDK OAuth; SSO login event ingestion; 90-day inactivity detection per user per app; SaaS app catalog generation from Workspace OAuth apps.
2. Weeks 4–5: Zombie seat report (app, user, last login, monthly cost, savings if cancelled); weekly digest email + Slack.
3. Weeks 6–7: Okta connector; app ownership assignment; cancellation workflow (generate a cancel checklist with user migration steps).
4. Weeks 8–9: Stripe; free zombie scan (top-5 seats, no card required); Subsight comparison landing page (invoice vs SSO coverage).
5. Weeks 10–12: Pilot 10 companies via YC Startup School ops community, Product Hunt launch, and Subsight-adjacent content marketing.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-16
**Strongest part:** Subsight's own documentation advises manual SSO cross-checking — their product confirms the gap StackClean fills by not filling it themselves.
**Open question:** Subsight has 100+ early adopters and momentum — if they announce Workspace/Okta integration in the next 30 days, does StackClean's moat collapse before first revenue?

---

## #10 — ModelReg  ·  67/100  ·  DECLINED
First added: 2026-09-11 | Last updated: 2026-10-16 | Score delta this week: -1

> Prove your community bank's AI governance to the next Fed examiner — without ValidMind's price tag.

### Score Breakdown
- Solo Buildability:   13/20  (unchanged — model inventory + validation status + drift alerts + exam prep; community bank feature set is simpler than enterprise)
- Value Clarity:       14/20  (unchanged — "OCC exam asks for your model inventory" is a 10-second pitch for any CRO)
- Market Timing:       10/20  (-1 — SR 26-2 explicitly confirmed: "expected to be most relevant to banking organizations with over $30 billion in total assets"; community banks under $10B are formally carved out unless "model use is significant"; OCC Bulletin 2025-26 "clarified that annual validation was not a community bank requirement"; exam pressure on small banks is weaker than previously assessed)
- B2B Monetisation:    16/20  (unchanged — community banks pay six figures in fines; $500–1500/month is trivially justified if triggered)
- Pull Factor:         14/20  (unchanged — banking exam prep is word-of-mouth within community banking networks)

**Strengths:**
- AegisAI (confirmed competitor) is a template+assessment service — no recurring monitoring SaaS. Community banks that buy AegisAI still lack ongoing model monitoring.
- ValidMind AWS Marketplace: $5,000/model/year — still far above community bank range.
- Openlayer's Basic tier is FREE but limited to 1 member and 5 projects — no community bank CRO is evaluating this tier.

**Risks:**
- SR 26-2 scope now confirmed as "$30B+ primarily" — community banks are explicitly less exposed than previously modeled.
- Openlayer free tier exists; community banks could cobble together monitoring without a dedicated tool.
- OCC explicitly clarified annual validation is not a community bank requirement — the exam pressure driver is weaker.

**Verdict:** Hold one final run. SR 26-2 scope clarification weakens the exam driver for community banks. The opportunity depends on community banks with "significant model use" (fintech partnerships, vendor AI tools) proactively seeking SR 26-2 alignment. Next run: drop if no competitive signal from community banking networks.

### The Pitch
**Problem:** SR 26-2, issued jointly by the Federal Reserve, OCC, and FDIC on April 17, 2026, extends model risk management expectations to AI systems, LLMs, and agentic architectures. While explicitly most relevant to banks over $30B in assets, community banks under $10B that have adopted vendor AI tools, fintech partnerships, or automated lending decision systems are also receiving examiner questions. ValidMind, Monitaur, and SAS MRM all start at enterprise pricing — ValidMind's AWS Marketplace lists $5,000/model/year. Openlayer's free tier limits to one member and five projects. AegisAI offers template packs and one-time assessments — not recurring monitoring SaaS. The community bank that finishes the AegisAI assessment has a PDF but no system of record for ongoing validation status, drift alerts, or exam-ready evidence.

**Solution:** ModelReg is the model risk management SaaS sized for community banks and fintechs under $10B in assets. It maintains the model inventory (every AI/ML tool in production), tracks validation status and next-review dates, sends alerts when a model's performance metrics drift, and generates an exam-prep package aligned to SR 26-2 / OCC 2026-13 evidence expectations. Self-serve, $499/month.

**Target customer:** Chief Risk Officer / Model Risk Officer at a community bank or fintech under $10B in assets that has adopted vendor AI tools or automated decision systems. Buyer: CRO or CCO. Users: model risk team (1–3 people) and internal audit.

**Why now:** SR 26-2 exam cycles began Q2 2026. Community banks with fintech partnerships or vendor AI tools are in scope despite the primary applicability threshold. AegisAI validates demand but is template-only.

**Why they buy without being sold to:** A CRO receives an MRA citing "inadequate model inventory and validation documentation." They search "community bank SR 26-2 compliance software," find ModelReg's free 10-model inventory, and convert when they see the gap between their documentation and examiner expectations.

**Revenue model:** $499/month (up to 20 models; inventory + validation tracking + drift alerts). $799/month (up to 50 models + vendor model oversight + exam prep pack). $1,499/month (unlimited models + audit integration + board reporting). Annual −2 months. Free: 10-model inventory assessment.

**Unfair advantage:** Sized for SR 26-2's proportionality principle — community bank feature set, community bank price point. First-mover SEO on "community bank SR 26-2 compliance" before Openlayer/Yields build a self-serve SMB tier.

### Solo Build Plan
1. Weeks 1–3: Model inventory (name, type, purpose, data sources, validation date, next review); validation status tracker; document upload per model.
2. Weeks 4–5: Drift alert framework (outcome monitoring thresholds; alert on performance degradation); vendor model diligence module.
3. Weeks 6–7: SR 26-2 evidence gap analysis; exam-prep package export.
4. Weeks 8–9: Stripe; free 10-model inventory; ABA/ICBA community bank newsletter placements.
5. Weeks 10–12: Pilot 5 community banks through state banking association networks.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-10-16
**Strongest part:** AegisAI's template-only nature confirms the monitoring gap exists; ValidMind $5K/model confirms the price gap.
**Open question:** SR 26-2 is explicitly most relevant to $30B+ banks — is the community bank segment actually experiencing exam pressure from this guidance, or is ModelReg solving a problem community banks don't yet feel? Monitor ABA exam feedback from community bank members.

---

## Removed this run
| Entry | Last score | Reason |
|-------|------------|--------|
| AgentCreds | 69 → 66 | Bifrost virtual key lifecycle (per-VK MCP allowlist auto-sync, orphaned-credential reconciliation) and Arcade immutable per-action audit logs are expanding into credential management territory. Gateway-level virtual key lifecycle covers the primary use case; the machine-vs-user identity distinction requires too much buyer education to maintain self-evident value. Displaced by IntegWatch (72). |
