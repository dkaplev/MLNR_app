# SaaS Opportunity Cookbook
Last updated: 2026-10-09 | Entries: 10/10

> R16 note: **MCPGate removed** — 9+ competing MCP gateways (Bifrost, MCPZERO, mspstack, agentgateway, Arcade, Traefik Hub, Obot, IBM ContextForge, Docker MCP) now all cover the OSS gateway thesis. **DORAIncident removed** — DoraGuard (€1,500/yr SME) and DoraPilot (small banks + ICT vendors) now explicitly serve the SME DORA market. **WorkAuditAI enters** — California SB 947/AB 1883/SB 951 signed Sept 30, 2026; AB 1883+SB 951 effective Jan 1, 2027 (12 weeks); zero SaaS competitor exists. **CredVerify enters** — mid-market physician group credentialing (10–100 providers) confirmed underserved by Alder VC 2026 analysis; enterprise incumbents start at $50K/year. CRAReport +2 (SRP now LIVE, ENISA FAQ confirms no API). DentPay +1 (dentpay.tech piloting; Samera still UK-only). StackClean -7 (Subsight launched with 100+ early adopters). AgentCreds -5 (Bifrost/Arcade/MCPZERO cover MCP OAuth flows; credential lifecycle gap remains).

---

## #1 — CRAReport  ·  82/100  ·  IMPROVED
First added: 2026-09-11 | Last updated: 2026-10-09 | Score delta this week: +2

> Cut your CRA vulnerability reporting time from hours to minutes — the ENISA SRP portal has no API, so someone has to bridge it.

### Score Breakdown
- Solo Buildability:   15/20  (SRP form automation + multi-step deadline tracker + evidence ZIP; no API = scrape/form-fill; achievable solo in 3 months)
- Value Clarity:       19/20  (+1 — SRP is now LIVE; first users experiencing manual pain IN PRACTICE; "I just submitted my first SRP notification and it took 3 hours" is now real testimony)
- Market Timing:       18/20  (+1 — SRP mandatory from Sept 11, 2026; ENISA FAQ explicitly confirms "no API at initial release, may be considered in future"; early adopter pain is NOW)
- B2B Monetisation:    17/20  (EU manufacturers already pay legal/compliance consultants €5K+ per vulnerability incident; $200-500/mo is cheap by comparison)
- Pull Factor:         13/20  (EU product security communities share pain; PSIRTs and DevSecOps channels are active; first-mover SEO on "CRA SRP reporting" captures search)

**Strengths:**
- ENISA's own FAQ uses the phrase "no API will be provided at the initial release" — this is official policy, not speculation. The moat is permanent until ENISA changes course.
- The multi-step notification structure (Early Warning → 72h → Final Report) creates ongoing workflow value, not a one-time form.
- CSA research note (Sept 18, 2026) called "manual entry as operating reality for foreseeable near term" — industry analyst validation.

**Risks:**
- If ENISA announces an API roadmap date, the kill condition is known and the window closes.
- The SRP is used by Assigned Representatives (ARs), not individual developers — the buyer is the EU representative role, which may be outsourced to a legal firm.
- Initial adoption base is EU manufacturers; non-EU companies exporting to EU may lag 6–12 months.

**Verdict:** Hold #1. SRP live, pain confirmed, no API. First-mover SEO window is open now.

### The Pitch
**Problem:** From September 11, 2026, manufacturers of products with digital elements sold in the EU must report actively exploited vulnerabilities and severe incidents through ENISA's Single Reporting Platform (SRP). The SRP has no API at initial release — every submission requires a human to log in with EU Login + MFA, navigate the 5-step form workflow, submit an Early Warning within 24 hours, a 72-hour Notification, and a Final Report, with each step having distinct mandatory fields. A software manufacturer releasing 50 products across 10 EU member states could face dozens of concurrent active notifications at different stages, each with deadline clocks running in parallel. The 55-page AR User Manual published September 9, 2026 documents this manually. CSA (Cloud Security Alliance) published a research note September 18, 2026 labelling manual entry as "the operating reality for foreseeable near term."

**Solution:** CRAReport is the workflow manager that sits above the SRP portal. You log incidents in CRAReport with product ID, affected versions, and CVSS data. CRAReport tracks the three-stage deadline clock for each incident, pre-fills the SRP form fields from your incident data, and prompts the AR at the right moment to review and submit each stage. Evidence attachments are managed in one place. At audit time, you export the full incident folder: submission timestamps, field values, reviewer log.

**Target customer:** Product security / PSIRT lead or Assigned Representative at a 20–500 person EU software or IoT hardware manufacturer. Buyer: CISO or Head of Product Security. User: the AR (Assigned Representative) who physically submits to the SRP portal. Not a tier-1 telco; not a one-person indie — mid-market manufacturers with 5–50 covered products.

**Why now:** The SRP went live September 11, 2026. The ENISA FAQ explicitly states "no API will be provided at the initial release." The first month of real usage is generating firsthand pain from ARs experiencing the manual workflow for the first time. No automation tooling exists. First-mover SEO on "CRA SRP reporting software" is unclaimed.

**Why they buy without being sold to:** An AR who just spent 3 hours submitting their first SRP Early Warning notification — filling in 40+ fields across 5 screens, losing their session once, and manually cross-checking the 72-hour deadline — searches for "CRA SRP reporting tool" and finds CRAReport. The free single-incident trial shows the workflow takes 15 minutes instead of 3 hours.

**Revenue model:** $199/month (1–10 concurrent active incidents; 3 products). $349/month (up to 30 incidents; 15 products; deadline dashboard). $599/month (unlimited incidents + multi-AR team + audit export). Annual −2 months. 14-day trial.

**Unfair advantage:** First-mover SEO in a regulation that went live 4 weeks ago. The product is the bridge that ENISA's FAQ says will not be built on their side. Community content strategy: publish "CRA SRP guide for ARs" that ranks before ENISA's own guidance.

### Solo Build Plan
1. Weeks 1–3: ENISA SRP form field mapping; incident data model (product, version, CVE, classification, CVSS); 3-stage deadline clock (24h / 72h / Final).
2. Weeks 4–5: Deadline dashboard; Slack/email alerts per stage; multi-incident view for practices with parallel active incidents.
3. Weeks 6–7: Evidence attachment manager; pre-fill export (field-by-field SRP mapping for AR review); incident audit log.
4. Weeks 8–9: Stripe; free single-incident trial; SEO content ("CRA SRP reporting guide for manufacturers").
5. Weeks 10–12: Pilot 5 EU manufacturers via ENISA CRA community channels and EU product security (PSIRT) Slack groups.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-10-09
**Strongest part:** ENISA's own FAQ is the product roadmap — they confirm the gap in writing. The product exists because a regulator explicitly said "no API for now."
**Open question:** If ENISA publishes an API roadmap date in Q1 2027, does CRAReport's exit strategy depend on being acquired before that API ships?

---

## #2 — DentPay  ·  78/100  ·  IMPROVED
First added: 2026-07-16 | Last updated: 2026-10-09 | Score delta this week: +1

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — CSV-first rule engine; dentpay.tech pilot confirms the technical approach is correct)
- Value Clarity:       19/20  (+1 — dentpay.tech piloting with real practices validates market; "same total with three flagged lab mismatches" is a demonstrable live demo)
- Market Timing:       17/20  (unchanged — Samera.ai still UK-only; "how it works" shows Dentally/Xero API; no US OD/Dentrix integrations confirmed)
- B2B Monetisation:    16/20  (unchanged)
- Pull Factor:         10/20  (-3 — dentpay.tech is now a live competitor capturing the early study-club referral channel; pull factor now split)

**Strengths:**
- dentpay.tech piloting with real US practices confirms market fit and technical feasibility.
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
**Strongest part:** dentpay.tech piloting confirms the thesis with real market evidence.
**Open question:** Does dentpay.tech's head start in the study-club referral channel foreclose the primary distribution path for a second entrant?

---

## #3 — WorkAuditAI  ·  77/100  ·  NEW
First added: 2026-10-09 | Last updated: 2026-10-09 | Score delta this week: —

> Know which AI tools your managers rely on before the January deadline does.

### Score Breakdown
- Solo Buildability:   15/20  (AI tool inventory form + SB 947 decision documentation workflow + Cal/WARN template generator; form-based, no HRIS integration in v1; solo-buildable in 3 months)
- Value Clarity:       16/20  (AB 1883 + SB 951 effective Jan 1, 2027 — 12 weeks; employment attorney advisories are the trigger; GC who searches "California SB 947 compliance tool" understands in 30 seconds)
- Market Timing:       18/20  (laws signed Sept 30, 2026 — 9 days ago; zero SaaS competitor exists; employment attorneys issuing advisories this week; perfect first-mover window)
- B2B Monetisation:    15/20  (HR/legal compliance budget exists at 100+ employee companies; comparable: EEO audit tools at $500–2K/mo; $199–599 is a clear value purchase)
- Pull Factor:         13/20  (SHRM chapters and employment law networks share compliance tools rapidly; attorney referrals to clients = strong zero-CAC distribution)

**Strengths:**
- Three laws signed 9 days ago — no competing SaaS exists.
- Employment attorneys are issuing client advisories with Step 1 = "inventory your AI tools" — that inventory IS the product's top-of-funnel.
- AB 1883 + SB 951 effective January 1, 2027 creates a 12-week forcing function with real $500/violation penalties (SB 947).

**Risks:**
- Governor Newsom's signing message noted AB 1883 "lacks key definitions" — regulatory ambiguity in what constitutes covered surveillance could narrow the addressable problem.
- ADP / Workday / ServiceNow HR could add a "California AI compliance" module using their existing HRIS integrations.
- California-only scope limits TAM initially; other states may follow but timeline is uncertain.

**Verdict:** Enter immediately. Attorney advisory distribution + Jan 1 deadline = near-zero CAC acquisition window that closes in 12 weeks.

### The Pitch
**Problem:** On September 30, 2026, California signed three workplace AI laws: SB 947 (effective July 1, 2027) prohibits relying solely on automated decision systems for discipline or termination, requiring documented human review; AB 1883 (effective January 1, 2027) restricts AI-powered surveillance tools that infer employee emotions or collect neural data; SB 951 (effective January 1, 2027) requires enhanced Cal/WARN disclosures when automation drives qualifying layoffs. HR and legal teams at 100–2,000 person companies with California workers must now: inventory every AI tool influencing an employment decision, document independent human review for ADS-based discipline/termination decisions, assess and restrict AI surveillance tools, and update Cal/WARN procedures. Baker Donelson, Mintz, and Hirschfeld Kraemer all published client advisories on October 1, 2026, each recommending a "Workplace AI Risk Assessment" as the mandatory first step. No purpose-built SaaS exists.

**Solution:** WorkAuditAI is the compliance operating layer for California's workplace AI laws. It runs a guided AI tool inventory (what tools, which HR decisions do they influence, which California employees are affected), then builds a workflow for each obligation: a surveillance tool classifier (AB 1883), a mandatory human-review documentation workflow for ADS-influenced discipline decisions (SB 947), a Cal/WARN AI-disclosure template generator (SB 951), and an audit trail exportable to counsel or regulators on demand.

**Target customer:** HR Director / VP People or General Counsel at a 100–2,000 person company with at least 50 California-based employees. Buyers: GC and CHRO jointly. Users: HR Operations and HR Business Partners who document employment decisions. Industries: tech, finance, logistics — any employer using AI-assisted performance management, productivity monitoring, or hiring tools.

**Why now:** SB 947, AB 1883, and SB 951 were all signed September 30, 2026 — 9 days ago. AB 1883 and SB 951 take effect January 1, 2027 (12 weeks away). SB 947 takes effect July 1, 2027. Employment attorneys are issuing client advisories this week. No SaaS tool built for these laws exists. The 12-week window is the highest-urgency, zero-competition acquisition moment this product will ever have.

**Why they buy without being sold to:** An employment attorney sends a client advisory about SB 947 with a 5-step compliance checklist. Step 1 is "inventory your AI tools." The GC googles "California SB 947 compliance software" or "workplace AI audit tool," finds WorkAuditAI's free AI inventory form, completes Step 1 in 20 minutes, and purchases the full workflow to complete Steps 2–5 the same afternoon.

**Revenue model:** $199/month (1–50 CA employees; AI inventory + AB 1883 surveillance classifier + SB 951 Cal/WARN template). $349/month (50–300 CA employees + SB 947 human-review documentation workflow + employee data-request response). $599/month (300+ CA employees + counsel export pack + RBAC + full audit trail). Annual −2 months. Free: guided AI tool inventory (Step 1 of every attorney checklist) with no purchase required.

**Unfair advantage:** First SaaS built specifically for California's September 30, 2026 workplace AI laws. Employment attorney referral networks distribute at zero CAC — the free inventory IS the product firms recommend to clients. First-mover SEO on "California SB 947 compliance," "AB 1883 workplace AI," and "workplace AI risk assessment" before any competitor exists.

### Solo Build Plan
1. Weeks 1–2: CA Workplace AI intake questionnaire; AI tool inventory (HR systems, productivity monitors, hiring tools, performance management); decision-category mapping (hiring, performance, discipline, layoff).
2. Weeks 3–4: AB 1883 surveillance tool classifier (infer emotion / collect neural data); SB 947 decision workflow (ADS flag → independent human review form → corroboration record → written post-use notice generator).
3. Weeks 5–6: Cal/WARN AI-disclosure template (SB 951 layoff disclosure language); employee data-request response workflow (SB 947 § data description obligation).
4. Weeks 7–8: Stripe; attorney partnership landing page; SHRM and HR compliance newsletter placements.
5. Weeks 9–12: Pilot 10 companies through employment counsel referrals (Baker Donelson, Mintz advisories cite "Workplace AI Risk Assessment" — contact those firms' labor practice groups).

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-10-09
**Strongest part:** Attorney advisories published the day after signing create a distribution channel that costs nothing and starts immediately — the law firm IS the sales team.
**Open question:** Will ADP or Workday ship a "California AI laws" compliance module within 12 weeks, leveraging their HRIS integrations to provide a richer automated audit trail than a form-based tool can?

---

## #4 — AuthTrack  ·  69/100  ·  DECLINED
First added: 2026-08-16 | Last updated: 2026-10-09 | Score delta this week: -2

> See which prior auths are inside the 7-day / 72-hour clock — and which denials still have no specific reason.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — CSV/fax log + calendar clocks + denial-reason fields; HIPAA applies)
- Value Clarity:       16/20  (unchanged — "this PA blows the CMS clock on Thursday" is obvious to a biller)
- Market Timing:       13/20  (-1 — CMS-0057-F clocks have been live for 9 months; AuthTrack Pro (authtrackpro.com) is building in exactly this space; Honey Health agentic AI adding end-to-end PA automation)
- B2B Monetisation:    14/20  (unchanged — $149–299/mo; one avoided write-off pays for a year)
- Pull Factor:         12/20  (unchanged — biller Facebook groups)

**Strengths:**
- Regulation is 9 months into enforcement — buyers now have evidence of the problem, not just fear of it.
- AuthTrack Pro's existence (LinkedIn June 2026) validates the market as real and payable.
- Linear Health, Waystar, CoverMyMeds still serve mid-market and enterprise — 2–10 provider Excel tracker gap persists.

**Risks:**
- AuthTrack Pro is building the same product with a head start.
- Honey Health (agentic AI for end-to-end PA automation) is moving into smaller practices.
- Tiny practices may wait for their clearinghouse to add a free clock tracker.

**Verdict:** Hold, but window is narrowing. The first-mover differentiation must be in the denial-reason audit pack and CMS clock export for appeals — not the basic tracker which AuthTrack Pro already covers.

### The Pitch
**Problem:** Since 1 January 2026, Medicare Advantage, Medicaid, CHIP, and FFE QHP payers must decide standard prior auths in 7 calendar days and urgent ones in 72 hours, and every denial must include a specific reason. Billing coordinators at 2–10 provider practices still track this in a spreadsheet next to the fax machine. They miss clocks, they cannot prove a vague denial, and they will need a clean log before 2027 electronic-PA attestation. AuthTrack Pro (authtrackpro.com) launched in June 2026 as a basic tracker — but lacks CMS clock breach documentation for appeals and denial-reason required-field enforcement.

**Solution:** AuthTrack is the PA status board with CMS-clock compliance: each request gets a deadline clock, a channel (fax/portal/phone), a required denial-reason field (vague denials are flagged), and an alert before the CMS window closes. At appeals time, you export a packet: submission date, payer clock, denial reason, follow-up log.

**Target customer:** Billing coordinator / office manager at a 2–10 provider US practice (PT, specialty lite, independent primary care) not on Athena+Linear Health. Buyer: office manager. User: the biller who owns the Excel PA tab.

**Why now:** The clocks are 9 months live. Practices that missed clock windows in January-September 2026 now have documented losses that make the pain concrete. The FHIR API mandate (1 Jan 2027) is 12 weeks away — practices building a log now will have the cleanest path to electronic attestation.

**Why they buy without being sold to:** After a denied MRI with no specific reason and a missed 7-day follow-up, the biller pastes the spreadsheet into AuthTrack, sees two clocks already red, and stops using Excel that week.

**Revenue model:** $149/mo (1 location, 200 PAs). $249/mo (3 locations + reminder SMS). $299/mo (export pack for appeals). Annual −2 months. 14-day trial with sample CSV.

**Unfair advantage:** CMS-clock breach documentation + denial-reason enforcement specifically for fax-era shops that AuthTrack Pro does not yet include.

### Solo Build Plan
1. Weeks 1–3: PA log (CSV import); 7-day / 72-hour clocks; denial-reason required on deny; vague-denial flag.
2. Weeks 4–5: Email/SMS reminders; aging report; appeal packet PDF (submission date + clock + denial reason + follow-up log).
3. Weeks 6–7: HIPAA BAA flow; audit log; role-based access.
4. Weeks 8–9: Stripe; sample-CSV onboarding.
5. Weeks 10–12: Pilot 6 small practices via biller Facebook groups and local MGMA chapters.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-09
**Strongest part:** Regulation is 9 months live — the problem is no longer theoretical.
**Open question:** Will AuthTrack Pro add the denial-reason enforcement and appeals packet before any new entrant can differentiate on it?

---

## #5 — ImpactDeck  ·  69/100  ·  DECLINED
First added: 2026-09-11 | Last updated: 2026-10-09 | Score delta this week: -2

> Manage your FRIA and DPIA as a living record — not a PDF you generate once and forget.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — FRIA + DPIA workflow builder + version history; no AI model integration required; clean SaaS build)
- Value Clarity:       15/20  (unchanged — "show me your FRIA" from an auditor = immediate trigger; EU-obligated deployers understand in 30 seconds)
- Market Timing:       12/20  (-2 — elladoc now covers Art. 27 FRIA with 14 obligation types; AI DPIA Pro launched with combined FRIA+DPIA wizard; Annex III deadline shifted to Dec 2, 2027 reducing urgency for many deployers; the specifically-obligated Aug 2 cohort is smaller than initially estimated)
- B2B Monetisation:    14/20  (unchanged — DPO/compliance teams at 50-500 person companies have budgets)
- Pull Factor:         14/20  (unchanged — EU AI Act communities share tools; DPO networks are active)

**Strengths:**
- elladoc's DPIA module is still "Planned" — the combined DPIA+FRIA lifecycle in a persistent, version-controlled system is still unclaimed.
- The specifically-obligated deployers (Annex III §5(b) credit scoring, §5(c) life/health insurance pricing, public bodies) CANNOT defer — their FRIA obligation was live August 2, 2026.
- Static generators (KLA, AI DPIA Pro) validate demand but export PDF — no lifecycle management, no version history, no change triggers.

**Risks:**
- elladoc's roadmap includes DPIA — when GDPR DPIA ships, ellamind becomes a direct full-stack competitor.
- The Annex III high-risk deadline shift to December 2027 (Digital Omnibus Reg. (EU) 2026/1744) reduces urgency for the broader high-risk AI market.
- Demand from the specifically-obligated Aug 2 cohort may be smaller than the total high-risk AI Act market suggested.

**Verdict:** Hold. The lifecycle management moat (vs static PDF generators) is real. But the window is narrowing as elladoc's DPIA ships.

### The Pitch
**Problem:** EU AI Act Article 27 FRIA obligations have been live since August 2, 2026 for specifically-obligated deployers — credit scoring (Annex III §5(b)), life and health insurance pricing (§5(c)), and private entities providing public services. GDPR Article 35 DPIA has been mandatory for high-risk data processing since 2018. Both assessments involve overlapping risk identification, stakeholder mapping, and mitigation planning. Free static generators (KLA Digital's browser-based DPIA+FRIA, AI DPIA Pro) validate demand and produce a one-time PDF. elladoc covers Art. 27 FRIA in its documentation workflow. None provide a persistent, versioned lifecycle record: when your AI system changes, when your vendor's model is updated, when a regulatory Q&A shifts your risk classification — there is no system that re-triggers assessment and tracks the delta.

**Solution:** ImpactDeck is the FRIA + DPIA lifecycle manager. The initial assessment is guided and fast (30–60 minutes). Every subsequent system change, vendor update, or regulation clarification triggers a version-controlled review. The audit trail shows who assessed what, when, what changed, and what the current risk status is. Regulators and DPOs can see a living record, not a stale PDF dated to initial deployment.

**Target customer:** Data Protection Officer / AI Governance Lead at a 50–500 person EU company deploying high-risk AI systems (credit scoring, insurance pricing, recruitment tools, or public-service-adjacent automation). Buyer: DPO or GC. User: DPO + the team implementing the AI system.

**Why now:** Art. 27 FRIA obligations are live for specifically-obligated deployers. No lifecycle tool exists — only static generators. elladoc's DPIA module is still "planned." The window to establish as the lifecycle standard (not just another PDF generator) is 3–6 months before elladoc ships DPIA.

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
**Rating:** 7/10 | **Last critique:** 2026-10-09
**Strongest part:** Version-controlled FRIA lifecycle is a real gap that static PDF generators structurally cannot fill.
**Open question:** When elladoc ships its planned GDPR DPIA module, does ImpactDeck's moat depend entirely on version history and lifecycle tracking, and is that enough to retain customers?

---

## #6 — AgentCreds  ·  69/100  ·  DECLINED
First added: 2026-10-02 | Last updated: 2026-10-09 | Score delta this week: -5

> Machine identities for AI agents — scoped, rotatable, and auditable without a pasted API key in the config file.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — SEP-1046 SDK support + vault-backed issuance + audit log; TypeScript-first, credibly solo-buildable)
- Value Clarity:       14/20  (-1 — Bifrost and Arcade now provide MCP OAuth + per-user token storage at the gateway layer; differentiation from gateway tools requires more explanation)
- Market Timing:       12/20  (-3 — Bifrost (Apache 2.0), MCPZERO, Arcade, agentgateway, and 5 more MCP gateways now cover OAuth flows; the "no MCP auth tool" gap from Run 15 is substantially filled at the gateway layer)
- B2B Monetisation:    14/20  (unchanged — platform teams have tooling budgets)
- Pull Factor:         13/20  (-1 — gateway tools have grabbed the eng community attention; credential lifecycle is a narrower story)

**Strengths:**
- Bifrost, MCPZERO, Arcade handle GATEWAY-layer OAuth (routing, per-tool allowlists, token injection at request time). None handle the CREDENTIAL LIFECYCLE below the gateway: agent machine-identity issuance, scoping, rotation schedule, and per-agent audit trail independent of request routing.
- SEP-1046 (private_key_jwt for MCP client assertions) shipped in TypeScript/Python/Ruby SDKs — companies need to manage the private keys themselves. No IAM vendor productized this for agents.
- The "which agent used which credential for what purpose" audit trail is distinct from the gateway's "which tool was called" log.

**Risks:**
- Bifrost or Arcade could add "credential lifecycle" as an enterprise tier in the next 90 days, collapsing the distinction.
- The target market (30–300 person companies running 5+ agents in production) may be smaller than the broader MCP gateway market suggests.
- SPIFFE/SVID approach may be too infrastructure-heavy for companies that already use a gateway.

**Verdict:** Hold but differentiate hard from gateway tools. The credential lifecycle (issuance → scoping → rotation → audit) is the surviving moat — not OAuth flow management which gateways already handle.

### The Pitch
**Problem:** The MCP gateway space exploded in 2026: Bifrost, MCPZERO, agentgateway, Arcade, MSPStack, Traefik Hub, and others now handle the request routing, tool allowlists, and OAuth flows between AI clients and MCP servers. What none of them handle: the machine identity lifecycle for the agents themselves. When an AI agent needs to call Salesforce, GitHub, or Stripe on behalf of the organization (not on behalf of a user), someone provisions a service account or pastes an API key into a config file. That key doesn't rotate. It has no scope limit. When five agents share the same Salesforce admin key and one of them accesses customer PII it had no business touching, nobody can reconstruct which agent did what — because the gateway logs "tool call to Salesforce" but not "which agent identity initiated this session." The 2026 State of Agentic report shows authentication and credentials as a top-3 deployment blocker (45%). Gateways solved request-time auth; nobody solved pre-request identity provisioning.

**Solution:** AgentCreds is the credential lifecycle manager for AI agents — the layer below the gateway. It issues short-lived, scoped machine identities to agents at startup using SEP-1046 private_key_jwt assertions. Each agent gets a scoped credential profile: what systems it can access, with what permissions, for how long. Credentials rotate automatically on schedule. Every credential use is logged to an immutable per-agent audit trail. When an agent hits a system it's not authorized for, AgentCreds rejects the issuance before the request ever reaches the gateway.

**Target customer:** Platform engineer / engineering lead at a 30–300 person company running 5+ AI agents in production using MCP-compatible infrastructure. Already uses a gateway (Bifrost, agentgateway, or MCPZERO). Buyer: CTO / Head of Platform. User: the team deploying and operating AI agent workloads.

**Why now:** SEP-1046 shipped private_key_jwt in TypeScript/Python/Ruby SDKs — companies need to manage those private keys. MCP gateways handle request routing; nobody handles the agent-identity lifecycle that feeds the gateway. The 2026 State of Agentic report (45% cite auth/credentials as top blocker) documents the problem. No IAM incumbent has productised agent machine identities.

**Why they buy without being sold to:** A platform engineer discovers all five production agents share the same Salesforce admin API key, and two of them accessed customer PII with no audit trail. AgentCreds' free agent inventory scan shows the problem in 10 minutes. The engineer sets up scoped identities that afternoon.

**Revenue model:** $199/month (up to 10 agents, 5 integrations, auto-rotation every 30 days). $399/month (50 agents + unlimited integrations + per-agent access policies + 90-day audit log). $799/month (enterprise: SPIFFE/SVID, custom OIDC integration, SOC 2 audit export). Annual −2 months.

**Unfair advantage:** Agent machine-identity lifecycle (issuance → scoping → rotation → audit) that gateway tools structurally cannot provide — they operate at request time, not at identity-issuance time. SEP-1046 private_key_jwt support built specifically for MCP client assertions, not backfitted from human IAM flows.

### Solo Build Plan
1. Weeks 1–3: Agent identity model (agent ID, scope profile, credential issuance); SEP-1046 private_key_jwt generator; short-lived credential issuance on agent startup.
2. Weeks 4–5: Auto-rotation scheduler; scope enforcement (reject issuance outside declared permissions); per-agent credential log.
3. Weeks 6–7: Dashboard (agent roster + current identity + last rotation + scope map + access log); Slack alert on rotation failure or scope breach.
4. Weeks 8–9: Stripe; free agent inventory scan (shows which agents share credentials, which have no rotation); onboarding for 5-agent teams.
5. Weeks 10–12: Pilot 5 platform teams through Anthropic Builder Community and MCP developer Slack.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-09
**Strongest part:** The gateway/identity-lifecycle distinction is technically valid and holds — gateways operate at request time; AgentCreds operates at provisioning time.
**Open question:** Will Bifrost or Arcade ship a "credential lifecycle" enterprise tier in the next 90 days, collapsing the last remaining differentiation?

---

## #7 — CredVerify  ·  68/100  ·  NEW
First added: 2026-10-09 | Last updated: 2026-10-09 | Score delta this week: —

> Your 40-provider group's malpractice, DEA, and hospital privileges — one dashboard, no spreadsheet.

### Score Breakdown
- Solo Buildability:   11/20  (provider profile + renewal calendar + CAQH import + HIPAA BAA; state licensing data is publicly available (FSMB, DEA.gov) but content work is substantial; achievable solo in 3 months if focused on top-5 states and 3 credential types first)
- Value Clarity:       14/20  (lapsed DEA registration = prescribing halt; voided payer contract = revenue loss; trigger events are immediate and concrete for any practice administrator)
- Market Timing:       15/20  (Alder VC 2026 explicitly names mid-market physician group credentialing as underserved; Modio Health acquired by Health Carousel, removing the primary mid-market option; enterprise incumbents symplr and Intellicheck start at $50K/year)
- B2B Monetisation:    16/20  (compliance-critical; one avoided lapsed malpractice certificate pays for 2 years of subscription; $299–799/month is defensible vs $50K enterprise alternative)
- Pull Factor:         12/20  (MGMA chapters and credentialing coordinator LinkedIn groups share tools; not publicly viral)

**Strengths:**
- Modio Health (the primary mid-market option) was acquired by Health Carousel — acquisition displacement creates a window for a dedicated replacement.
- CAQH profiles already hold most of the credential data practices maintain — CAQH import is a zero-friction onboarding path that larger competitors have not optimized.
- Compliance-critical + immediate financial consequence (payer contract void) = high willingness to pay without extensive education.

**Risks:**
- HIPAA BAA required from day one — not optional; adds legal overhead for a solo founder.
- State licensing data accuracy across 50 jurisdictions requires ongoing maintenance — wrong renewal deadlines create liability.
- MGMA or a health-system-adjacent vendor could enter this segment with an existing provider directory.

**Verdict:** Enter with a narrow beachhead: top-5 US states (CA, TX, FL, NY, IL), 3 credential types (DEA, state medical license, malpractice), CAQH import. Expand breadth only after first 10 paying customers.

### The Pitch
**Problem:** Physician groups, outpatient surgery centers, and specialty clinics with 10–100 providers manage credentialing — state medical license renewals, DEA registrations, malpractice coverage verification, hospital privilege expirations, and payer re-enrollment — manually. For a 40-provider orthopedic group, this means a full-time credentialing coordinator maintaining a spreadsheet of 200+ renewal dates across 50+ licensing jurisdictions and 15 payers. A single lapsed DEA registration halts prescribing for that provider. An expired malpractice certificate can void a payer contract mid-year. Enterprise credentialing platforms (symplr, Intellicheck, Verity) start at $50K/year and require multi-month implementations. Modio Health — the closest mid-market option — was acquired by Health Carousel in 2026, leaving the 10–100 provider group without a purpose-built affordable alternative. Alder VC's 2026 vertical SaaS analysis explicitly names this as one of the clearest underserved gaps in healthcare administration.

**Solution:** CredVerify is the centralized credentialing dashboard for mid-market physician groups. Each provider gets a profile with all their credentials, licenses, and renewals tracked in one place. The system alerts the credentialing coordinator 90/60/30 days before any expiration, generates a renewal preparation checklist per jurisdiction, and maintains a verification-ready record for payer audits and hospital privilege reapplications. v1 is database-first — CAQH import for onboarding, no EHR integration, no payer portal automation.

**Target customer:** Credentialing coordinator / Practice Administrator at a 10–100 provider specialty group (orthopedics, neurology, anesthesia, GI, dermatology) or outpatient surgery center in the US. Buyer: Practice Administrator or CFO. Users: credentialing coordinator (primary) + individual providers (self-service renewal prompts for their own licenses).

**Why now:** Modio Health's acquisition created an active vacancy in the mid-market credentialing tool category. Alder VC's 2026 analysis confirms the gap. Enterprise platforms start at $50K/year — 10x above what a 20–50 provider group will pay. The MGMA 2026 administrative burden data shows credentialing errors cost mid-market practices an average of $45K/year in delayed or denied payer contracts.

**Why they buy without being sold to:** After a provider's malpractice certificate lapses unnoticed and a payer contract voids mid-year, the administrator searches "physician credentialing tracking software group practice." CredVerify's free 5-provider tier (no credit card) shows a live renewal calendar. The administrator imports the group's CAQH data, sees 3 expirations in the next 60 days that weren't on the coordinator's spreadsheet, and converts to paid the same session.

**Revenue model:** $299/month (1–20 providers; top-5 state licensing + DEA + malpractice). $499/month (21–60 providers + payer audit pack + hospital privilege tracking). $799/month (61–100 providers + CAQH sync + unlimited locations + reporting). Annual −2 months. Free tier: 5 providers, 3 credential types, renewal calendar.

**Unfair advantage:** CAQH import as zero-friction onboarding (most groups already maintain CAQH — CredVerify makes their existing data useful instantly). Purpose-built for 10–100 provider groups that enterprise platforms ignore and that Modio Health no longer serves.

### Solo Build Plan
1. Weeks 1–3: Provider profile (DEA + state medical license + malpractice + hospital privileges); renewal calendar; 90/60/30-day email alerts; CSV import.
2. Weeks 4–5: CAQH profile import (CAQH ProView XML export parsing); document upload per credential type; payer audit export pack (verification-ready PDF).
3. Weeks 6–7: HIPAA BAA click-wrap; audit log; role-based access (admin vs coordinator vs provider self-service).
4. Weeks 8–9: Stripe; free 5-provider tier (no card required); FSMB data integration for state medical license verification.
5. Weeks 10–12: Pilot 5 groups through MGMA chapter demonstrations and credentialing coordinator LinkedIn groups (National Association of Medical Staff Services / NAMSS).

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-09
**Strongest part:** Modio Health's acquisition created a real market gap at exactly the moment Alder VC is publishing research calling it underserved — rare confluence of displacement and validation.
**Open question:** Can a solo founder maintain accurate, current renewal deadline data across 50 state licensing jurisdictions without a credentialing domain expert, and what is the liability exposure if a renewal alert fires at the wrong deadline?

---

## #8 — ModelReg  ·  68/100  ·  DECLINED
First added: 2026-09-11 | Last updated: 2026-10-09 | Score delta this week: -3

> Prove your community bank's AI governance to the next Fed examiner — without ValidMind's price tag.

### Score Breakdown
- Solo Buildability:   13/20  (unchanged — model inventory + validation status + drift alerts + exam prep; no real-time model monitoring required in v1; community bank feature set is simpler than enterprise)
- Value Clarity:       14/20  (unchanged — "OCC exam asks for your model inventory" is a 10-second pitch for any CRO)
- Market Timing:       11/20  (-1 — Openlayer explicitly now positions for SR 26-2 continuous monitoring; Yields.io also SR 26-2 specific; FDIC FIL-15-2026 adds a third regulatory driver but also more enterprise attention; AegisAI confirmed as template-only not monitoring SaaS)
- B2B Monetisation:    16/20  (unchanged — community banks pay six figures in fines; $500–1500/month is trivially justified)
- Pull Factor:         14/20  (unchanged — banking exam prep is word-of-mouth within community banking networks; ABA and ICBA channels)

**Strengths:**
- AegisAI (confirmed competitor) is a template+assessment service — no recurring monitoring SaaS. Community banks that buy AegisAI still lack ongoing model monitoring and drift detection.
- Openlayer and Yields target enterprise banks ($30B+ assets). SR 26-2 explicitly applies proportionally by "nature, scale, and risk profile" — community banks under $10B get different exam expectations.
- SR 26-2 issued April 17, 2026 (Fed/OCC/FDIC jointly) means examiners began applying it in Q2 2026 exam cycles.

**Risks:**
- Openlayer and Yields are now specifically marketing SR 26-2 compliance; they could release lower-priced tiers.
- ValidMind and Monitaur could expand downmarket with starter pricing.
- Community bank IT budgets are constrained; winning requires a $500/month entry point and self-serve onboarding.

**Verdict:** Hold. AegisAI's template-only nature leaves the monitoring gap. Community bank segment still lacks an affordable recurring SaaS.

### The Pitch
**Problem:** SR 26-2, issued jointly by the Federal Reserve, OCC, and FDIC on April 17, 2026, replaces SR 11-7 and extends model risk management expectations to AI systems, LLMs, and agentic architectures. OCC Bulletin 2026-13 echoes the same expectations. For the first time, community banks and fintechs under $10 billion in assets are receiving examiner questions about their AI model inventory, validation status, ongoing monitoring, and governance evidence. ValidMind, Monitaur, Yields, and SAS Model Risk Management all start at enterprise pricing — six-figure contracts, multi-month implementations. AegisAI Compliance offers SR 26-2 readiness assessments and template packs — but it is a template library and a one-time assessment service, not a recurring monitoring SaaS. The community bank that finishes the AegisAI assessment has a gap report and a PDF — but no system of record for ongoing validation status, drift alerts, or exam-ready evidence collection.

**Solution:** ModelReg is the model risk management SaaS sized for community banks and fintechs under $10B in assets. It maintains the model inventory (every AI/ML tool in production, from vendor-provided underwriting models to internal fraud classifiers), tracks validation status and next-review dates, sends alerts when a model's performance metrics drift outside its validated range, and generates an exam-prep package aligned to SR 26-2 / OCC 2026-13 evidence expectations. The product is $500/month, self-serve, and requires no multi-month implementation.

**Target customer:** Chief Risk Officer / Model Risk Officer / BSA Officer at a community bank or fintech under $10B in assets. Buyer: CRO or CCO. Users: model risk team (1–3 people) and internal audit.

**Why now:** SR 26-2 exam cycles began Q2 2026. Community banks are receiving examiner questions NOW. AegisAI validates demand but is template-only. Enterprise MRM platforms start at $50K+/year. The proportionality principle in SR 26-2 explicitly says smaller institutions get different exam expectations — a tool sized for that reality doesn't exist.

**Why they buy without being sold to:** A CRO receives an MRA (Matters Requiring Attention) from OCC examiners citing "inadequate model inventory and validation documentation." They search for "community bank SR 26-2 compliance software," find ModelReg's free model inventory template, run the free 10-model inventory, and convert when they see the gap between their current documentation and examiner expectations.

**Revenue model:** $499/month (up to 20 models; inventory + validation tracking + drift alerts). $799/month (up to 50 models + vendor model oversight + exam prep pack). $1,499/month (unlimited models + audit integration + board reporting). Annual −2 months. Free: 10-model inventory assessment (no monitoring features).

**Unfair advantage:** Sized for SR 26-2's proportionality principle — community bank feature set, community bank price point. First-mover SEO on "community bank SR 26-2 compliance," "model risk management small bank," before Openlayer/Yields build a self-serve SMB tier.

### Solo Build Plan
1. Weeks 1–3: Model inventory (name, type, purpose, data sources, validation date, next review); validation status tracker; document upload per model.
2. Weeks 4–5: Drift alert framework (outcome monitoring thresholds; alert on performance degradation); vendor model diligence module (third-party DDQ template).
3. Weeks 6–7: SR 26-2 evidence gap analysis (which models lack documentation, validation, or monitoring); exam-prep package export.
4. Weeks 8–9: Stripe; free 10-model inventory; ABA/ICBA community bank newsletter placements.
5. Weeks 10–12: Pilot 5 community banks through state banking association networks.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-09
**Strongest part:** AegisAI's template-only nature confirms the monitoring gap exists and that someone is willing to buy a first product.
**Open question:** When Openlayer or ValidMind releases a self-serve starter tier at $500/month, does ModelReg's community-bank-specific positioning (proportionality framing, ABA/ICBA distribution) provide enough moat to retain its customers?

---

## #9 — AgentAudit  ·  67/100  ·  DECLINED
First added: 2026-09-25 | Last updated: 2026-10-09 | Score delta this week: -2

> Block malicious MCP packages before they reach your production agent — not after the incident report.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — Trust Registry + GitHub Action CI gate + team dashboard; agentaudit-dev OSS validates the architecture; the paid tier is the SaaS layer on top)
- Value Clarity:       15/20  (+1 — agentaudit-dev's real Trust Registry with real packages proves this is a real security layer, not a hypothetical; the GitHub Action demo is live and demonstrable)
- Market Timing:       11/20  (-2 — agentaudit-dev OSS is LIVE with GitHub Action + CLI; free OSS covers the CI gate use case; paid SaaS tier not yet built by anyone; risk that agentaudit-dev adds a paid tier before a competitor can)
- B2B Monetisation:    14/20  (unchanged — enterprise security budgets; supply chain security is a known spend category)
- Pull Factor:         13/20  (unchanged — incident post + "we blocked a malicious MCP package" story = eng Twitter virality)

**Strengths:**
- agentaudit-dev's OSS existence validates the technical approach AND the market need — the Trust Registry is real and being maintained.
- The paid SaaS tier (team dashboard + organization-level policy + continuous monitoring) is explicitly unlaunched — "commercial license available" but no SaaS product.
- agentaudit-dev builds the OSS; a complementary SaaS dashboard + org policy layer is the natural next product.

**Risks:**
- agentaudit-dev could ship a paid SaaS tier before any competitor, capturing the upgrade path from their own OSS user base.
- Cisco MCP Scanner and other OSS security tools are appearing — free alternatives may satisfy enough of the market.
- "Trust Registry" as a community-driven database has data quality risks that could undermine confidence.

**Verdict:** Hold but urgency is high — agentaudit-dev has the distribution advantage from their OSS; the paid team dashboard must launch before they ship their own commercial tier.

### The Pitch
**Problem:** AI agents increasingly rely on Model Context Protocol (MCP) servers — npm packages that expose tools to models. The ecosystem has grown to 2,000+ MCP packages, with no systematic supply-chain security layer. Malicious MCP packages can inject prompts into agent conversations, exfiltrate data through tool calls, or execute arbitrary code in the agent's context. agentaudit-dev's open-source AgentAudit CLI + Trust Registry validates real packages against known security findings, but it is a developer CLI tool. Engineering teams need a team-level policy layer: org-wide package allowlists, a CI gate that blocks builds containing unauthorized MCP packages, a dashboard showing which packages each team is using and their current security status, and alerts when a previously-safe package gets flagged.

**Solution:** A SaaS layer on top of the open AgentAudit Trust Registry: GitHub App (not just Action) + org-level package policy + team dashboard. Every repository in the organization runs the scan automatically. New MCP package = instant Trust Registry check. Flagged package = PR blocked, reviewer alerted, audit record created. The CISO gets a dashboard showing every MCP package in use across all teams and their security status.

**Target customer:** CISO / Security Engineering lead at a 50–500 person company actively using MCP-based AI agents in production. Buyer: CISO or VP Engineering. Users: security team + each engineering team running AI agents.

**Why now:** agentaudit-dev's OSS proves the technical approach, validates real user demand (npm downloads), and provides a ready-made Trust Registry data source. The paid enterprise SaaS layer — org policies, GitHub App, team dashboard, CISO reports — has not been built by anyone including agentaudit-dev.

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
**Rating:** 7/10 | **Last critique:** 2026-10-09
**Strongest part:** agentaudit-dev's own OSS proves the market and provides the data moat (Trust Registry) — the SaaS tier builds on proven infrastructure rather than starting from zero.
**Open question:** If agentaudit-dev ships their own commercial SaaS tier (they have a commercial license agreement written), does this opportunity evaporate immediately or does it become a partnership/acquisition conversation?

---

## #10 — StackClean  ·  66/100  ·  DECLINED
First added: 2026-10-02 | Last updated: 2026-10-09 | Score delta this week: -7

> Kill the SaaS zombie seats before finance finds them on the card statement.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — Google Workspace/Okta API + SSO login history + SaaS catalog; technically straightforward for a developer)
- Value Clarity:       15/20  (unchanged — "here are 12 seats nobody has used in 90 days" is self-evident; zombie scan result IS the pitch)
- Market Timing:       11/20  (-4 — Subsight launched in October 2026 with 100+ early adopters, bank statement parser, renewal calendar, Slack integration, and RBAC; Substly serves the same SMB segment; Cledara adds virtual cards; competition materially increased)
- B2B Monetisation:    14/20  (-1 — Subsight's waitlist pricing and Substly's freemium create downward pressure on willingness to pay; SSO-based differentiation is the only premium justification)
- Pull Factor:         12/20  (unchanged — ops/finance communities share "we saved $X" stories; word-of-mouth through YC Startup School ops channels)

**Strengths:**
- SSO login data (Google Workspace/Okta) reveals inactive seats that bank statement parsers cannot see — this is StackClean's remaining structural moat vs Subsight.
- Subsight's bank-statement-parser approach misses apps billed annually (no monthly statement), SSO-only apps (no recurring card charge), and inactive seats that are still being billed.
- Zylo, Torii, Zluri (enterprise) require months of implementation and start at $20K+/year — the SMB gap persists above the Subsight price point.

**Risks:**
- Subsight could add Workspace/Okta integration in their first few months of live operation — if they do, StackClean's moat collapses.
- Substly already has basic SSO usage detection for Office 365; expanding to Google Workspace would narrow the gap further.
- The SMB SaaS management space is now genuinely competitive at every price point.

**Verdict:** Hold only on the SSO usage data moat. If Subsight announces Google Workspace/Okta integration in the next 4 weeks, remove immediately.

### The Pitch
**Problem:** The average 50-person company runs 80+ SaaS subscriptions, with an estimated 30% unused or redundant. Bank-statement-based trackers (Subsight, CostLoop, Cledara) now exist for SMBs — but they miss the hidden zombie: the seat that is still being billed because the employee never formally cancelled, but also hasn't logged in for 4 months. Bank parsers see the charge. They cannot see the login history. A $200/month design tool with 8 seats that nobody has touched since the project ended keeps appearing as "paid and current" in every bank-based tracker — because the invoice is still arriving on time.

**Solution:** StackClean connects to Google Workspace or Okta (one OAuth click) and surfaces every SaaS app with at least one user who has not logged in for 90 days. The weekly digest shows: zombie seats by app, the cost per zombie seat per month, and the specific users to deprovision. One click generates the cancellation shortlist with savings total. No bank statement import required — login data is more accurate and more granular.

**Target customer:** Ops lead / founder / IT admin at a 20–200 person company using Google Workspace or Okta SSO with 20+ SaaS applications. Buyer: Ops lead or CFO. User: IT admin or Ops. Does NOT use Zylo, Torii, or Zluri (enterprise). May already use Subsight for invoice tracking.

**Why now:** Subsight launched October 2026 and validated SMB SaaS management demand with 100+ early adopters — but Subsight is invoice-only and cannot see SSO login history. The SSO-based differentiation is the gap that Subsight's launch made explicit.

**Why they buy without being sold to:** The Ops lead runs StackClean's free "zombie seat scan" (Google Workspace OAuth, 5 minutes), sees 12 unused seats across 4 apps totalling $2,700/year, and purchases the full tracker before the free trial ends — even if they already have Subsight.

**Revenue model:** $149/month (Google Workspace, up to 100 users; zombie scan + weekly digest). $249/month (Okta, up to 250 users + team SaaS catalog + cancellation workflow). $399/month (SSO + bank statement + Slack + API). Annual −2 months. Free: one-time zombie scan showing top-5 zombie seats (Workspace only; no purchase required).

**Unfair advantage:** SSO login data reveals inactive seats that bank-statement parsers structurally cannot detect. Google Workspace and Okta have free, well-documented APIs for OAuth app usage history. Subsight (the nearest competitor) does not currently have SSO integration.

### Solo Build Plan
1. Weeks 1–3: Google Workspace Admin SDK OAuth; SSO login event ingestion; 90-day inactivity detection per user per app; SaaS app catalog generation from Workspace OAuth apps.
2. Weeks 4–5: Zombie seat report (app, user, last login, monthly cost, savings if cancelled); weekly digest email + Slack.
3. Weeks 6–7: Okta connector; app ownership assignment; cancellation workflow (generate a cancel checklist with user migration steps).
4. Weeks 8–9: Stripe; free zombie scan (top-5 seats, no card required); Subsight comparison landing page (invoice vs SSO coverage).
5. Weeks 10–12: Pilot 10 companies via YC Startup School ops community, Product Hunt launch, and Subsight-adjacent content marketing.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-09
**Strongest part:** The SSO login data moat is a structural, not just a feature, difference from bank-statement trackers — the data source itself is inaccessible to Subsight.
**Open question:** Subsight has 100+ early adopters and momentum — if they announce Workspace/Okta integration in the next 30 days, does StackClean's moat collapse before first revenue?

---

## Removed this run
| Entry | Last score | Reason |
|-------|------------|--------|
| MCPGate | 74 → 63 | Mastra.ai published "9 Best MCP Gateways (Aug 2026)" listing Bifrost, MCPZERO, MSPStack, agentgateway, Arcade, Traefik Hub, Obot, IBM ContextForge, Docker MCP — all covering OSS gateway thesis with OAuth 2.1, per-tool allowlists, and audit logs. The "no OSS reverse proxy" gap is fully closed. |
| DORAIncident | 72 → 65 | DoraGuard (€1,500/year, xBRL-CSV export, EBA-validated) and DoraPilot (small banks + ICT vendors, dual-persona targeting) now explicitly serve the SME DORA market at the price point our entry required. DoraIncident.io itself is live and comprehensive. The SME pricing + differentiation thesis is occupied. |
