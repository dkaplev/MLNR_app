# SaaS Opportunity Cookbook
Last updated: 2026-09-25 | Entries: 10/10

---

## #1 — CRAReport  ·  79/100  ·  IMPROVED
First added: 2026-09-18 | Last updated: 2026-09-25 | Score delta this week: +2

> Manufacturers facing a 24-hour ENISA clock and a browser-only form turn a SBOM into a compliant CRA notification in minutes, not hours.

### Score Breakdown
- Solo Buildability:   15/20  (SBOM import + deadline clock + ENISA SRP form pre-filler; no API means the tool bridges pipeline output to a manual form — actually simplifies scope)
- Value Clarity:       17/20  (unchanged — "24-hour clock, no API, you will retype everything unless you have this" is self-evident to any SBOM-aware security team)
- Market Timing:       18/20  (+2 — ENISA confirmed "no API will be provided at this stage"; SRP went live Sept 11, 2026; 24h early warning + 72h detailed report timelines confirmed under manual-only submission; obligations now enforceable)
- B2B Monetisation:    15/20  (unchanged — software manufacturers with EU market presence; €199–699/month)
- Pull Factor:         14/20  (+1 — first wave of actual SRP registrations creates shareable blog posts; "how we met the 24h CRA deadline" content drives organic inbound)

**Strengths:**
- ENISA's "no API at this stage" confirmation makes the SBOM→SRP bridge a permanent workflow problem, not a temporary gap.
- CRA-decoded.com analysis confirms: a Dependency-Track alert confirming active exploitation → 24h early warning → 72h detailed report chain is exactly the pipeline where manual re-entry causes errors and missed clocks.
- First-mover SEO on "CRA vulnerability reporting software" captures all search volume from the wave of manufacturers registering with ENISA now.

**Risks:**
- ENISA may add a REST API in a future SRP release, collapsing the automation wedge.
- Scope ambiguity (which products are "products with digital elements"?) remains the #1 adoption blocker — manufacturers are still uncertain if they're in scope.
- Legal liability if a pre-filled form contains an error that misrepresents a security incident.

**Verdict:** Hold #1. ENISA "no API" confirmation is the single most important signal this week — it validates the product thesis for at least 12 months.

### The Pitch
**Problem:** From September 11, 2026, manufacturers of products with digital elements must report actively exploited vulnerabilities to ENISA's Single Reporting Platform within 24 hours of awareness, with a detailed follow-up within 72 hours and a final report within 14 days of remediation. ENISA has confirmed no API will be provided "at this stage" — all submissions are manual browser form entry. Companies running modern vulnerability management pipelines (Dependency-Track, Grype, Trivy) have structured CycloneDX or SPDX SBOM data that precisely identifies the affected product, CVE, and scope — but must retype every field into the ENISA portal under time pressure, at whatever hour the vulnerability is discovered.

**Solution:** CRAReport imports your SBOM (CycloneDX or SPDX), cross-references the EUVD to confirm active exploitation status, starts the 24-hour clock automatically, and pre-fills the ENISA SRP notification fields from structured SBOM metadata. The security team reviews the draft, adds context, and exports a submission-ready JSON that maps to the SRP form field by field. Clock status, submission history, and the 14-day final-report deadline are tracked in a single dashboard.

**Target customer:** Product security manager / CISO at a 25–500 person software manufacturer selling products in the EU market — SaaS platforms, IoT devices, on-premise enterprise software. Buyer: CISO or VP Engineering. Users: security team + whoever owns CRA compliance.

**Why now:** CRA reporting obligations became enforceable September 11, 2026. ENISA has explicitly confirmed no API. The first wave of manufacturers filing early warnings is discovering the pain of manual form entry under a 24-hour clock. No purpose-built SaaS tooling exists for this bridge; the market window opened two weeks ago.

**Why they buy without being sold to:** A security engineer whose pipeline flags an actively exploited CVE in a shipped product at 11pm opens the ENISA portal, sees 30 form fields, and looks for anything that pre-fills from the SBOM already sitting in Dependency-Track. CRAReport is the answer they search for at midnight.

**Revenue model:** €199/month (1 product line, up to 12 reports/year, SBOM import). €399/month (5 product lines + clock alerts + multi-user review). €699/month (SSO + audit log export + bulk SBOM management). Annual −2 months. Free "CRA Scope Questionnaire" as lead magnet (determines if you're in scope and what you must report — no login required).

**Unfair advantage:** First-mover SEO in a regulatory niche with zero competitor content; SBOM-native pipeline integration (vs. generic form-filling tools); clock-based urgency dashboard that turns a compliance obligation into a product people actively rely on under pressure.

### Solo Build Plan
1. Weeks 1–3: SBOM ingest (CycloneDX JSON/XML + SPDX JSON); CVE/product matcher; 24h/72h/14-day clock dashboard; ENISA field mapping table.
2. Weeks 4–5: Pre-fill export (JSON matching SRP form fields); draft notification review UI; multi-user review + sign-off.
3. Weeks 6–7: EUVD cross-reference check (confirms exploitation status); audit log; Slack/email clock alerts.
4. Weeks 8–9: Stripe; free scope questionnaire lead magnet (no login, outputs "in scope / out of scope / uncertain" with rationale); product onboarding flow.
5. Weeks 10–12: Pilot 6 software manufacturers via EU CRA communities, ENISA guidance forums, product security Slack groups.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-09-25
**Strongest part:** "No API at this stage" is a permanent structural gap that makes CRAReport's bridge non-redundant for the foreseeable future.
**Open question:** Will ENISA add a REST API to the SRP in 2027 as it "continues to improve and expand functionalities"? That is the single event that collapses the automation thesis.

---

## #2 — DentPay  ·  79/100  ·  DECLINED
First added: 2026-07-16 | Last updated: 2026-09-25 | Score delta this week: −1

> Turn Open Dental / Dentrix production exports into clean associate and hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — CSV-first rule engine; OD/Dentrix export formats are stable)
- Value Clarity:       18/20  (unchanged — OM ritual is self-evident; "spreadsheet becomes a liability every pay period" needs no pitch)
- Market Timing:       16/20  (−1 — Netchex now advertises "native hygienist productivity tracking" for dental practices; CareStack ships built-in Provider Payroll with production calculations + lab cost + daily minimum; HR for Health explicitly handles "percent collection" pay structures. Gap persists for practices on OD/Dentrix using ADP/Gusto, but competition is growing.)
- B2B Monetisation:    16/20  (unchanged)
- Pull Factor:         13/20  (unchanged — dental study clubs; US outreach guide for discovery calls)

**Strengths:**
- HRPayPick 2026 + Comparisoft 2026 still confirm: no payroll platform has native plug-and-play integration with OD, Dentrix, and Eaglesoft simultaneously. Netchex requires practices to adopt Netchex as their payroll platform — no bridge for existing ADP/Gusto users.
- CareStack is an all-in-one PMS cloud alternative — practices already committed to OD or Dentrix won't switch. The OD/Dentrix → ADP/Gusto bridge remains unclaimed.
- Paycheck math errors create employer liability; switching cost is existential; very high retention once configured.

**Risks:**
- Netchex, HR for Health, and CareStack are all growing their dental-specific payroll coverage. If Netchex launches an OD export connector, it closes the primary wedge.
- Dentrix or Dental Intelligence could deepen native pay math in a platform update.
- Relationship-heavy sales; CPA/advisor trust needed for paycheck-math credibility.

**Verdict:** Hold #2. OD/Dentrix beachhead intact; watch for Netchex OD connector announcement.

### The Pitch
**Problem:** US dental practices paying associates and hygienists on production still spend hours each pay period exporting Open Dental or Dentrix reports, pasting into Excel, applying lab fees, write-offs, and card-fee rules, then hoping the spreadsheet matches the contract. Open Dental's Provider Payroll report is raw material — not a pay engine. Netchex handles dental payroll natively but requires practices to switch payroll providers. CareStack ships built-in production payroll but is a competing PMS. Practices on OD or Dentrix with ADP or Gusto have no bridge. HRPayPick 2026 confirms no payroll platform has native integration with OD, Dentrix, and Eaglesoft simultaneously.

**Solution:** DentPay imports OD/Dentrix production exports, applies per-provider pay rules once, flags anomalies before payout, and exports an approval pack to Gusto/ADP. Office managers review exceptions — they do not rebuild formulas.

**Target customer:** Office manager / owner at a 1–3 location US dental practice on Open Dental or Dentrix with associates or hygienists on production splits. Does not want to switch payroll platforms.

**Why now:** Production % pay still the norm; UK tools (Samera/Dentivize) proved analytics willingness-to-pay; US PMS vendors have not productised the reconciliation layer; PE roll-up practices create multi-location demand.

**Why they buy without being sold to:** An OM who spent Sunday fixing a hygienist underpay uploads last month's OD export, sees the same total with three flagged lab mismatches, and refuses to go back to Excel.

**Revenue model:** $149 / $249 / $399 per practice per month. 30-day trial. CPA referral 15%.

**Unfair advantage:** US OD/Dentrix rule templates + anomaly library; study-club distribution; PE roll-ups won't chase at $149.

### Solo Build Plan
1. Weeks 1–3: OD Provider Payroll CSV ingest; rule builder; pay summary PDF.
2. Weeks 4–5: Anomaly flags; vs last period; Gusto CSV export.
3. Weeks 6–7: Dentrix path; multi-provider approval.
4. Weeks 8–9: Stripe; sample-file onboarding.
5. Weeks 10–12: Pilot 8 practices via dental groups / OD user groups.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-09-25
**Strongest part:** Samera's own FAQ still lists Dentally/SoE — the US OD/Dentrix-to-ADP/Gusto path is intact and uncontested by any product that doesn't require a full platform switch.
**Open question:** Will Netchex or HR for Health launch a direct OD/Dentrix export connector before DentPay establishes a customer base?

---

## #3 — DORAIncident  ·  74/100  ·  IMPROVED
First added: 2026-09-18 | Last updated: 2026-09-25 | Score delta this week: +1

> File your 4-hour DORA initial notification and your 72-hour intermediate report to the right NCA — without re-reading five PDFs at 3am.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — NCA template library + clock management + PDF/JSON export; no DORA API exists so submission remains manual; tooling is form-prep, not automated filing)
- Value Clarity:       16/20  (unchanged — "4-hour clock, 5 different NCA portals, one workbench" is obvious to any EU financial entity's ICT risk team)
- Market Timing:       16/20  (+1 — ESMA published DORA Incident Reporting Operational Instructions in September 2026 — fresh guidance just published, creating demand for tooling that maps to the updated instructions; BaFin is planning a SOAP web service interface; multi-NCA fragmentation confirmed: CBI Portal, AFM Portal, BaFin MVP, ACPR portal are all distinct. Vendorica mentioned as building NCA-specific automation but not confirmed for all jurisdictions.)
- B2B Monetisation:    16/20  (unchanged — EU payment institutions, e-money firms, CASPs; DORA compliance budget is real; €399–999/month)
- Pull Factor:         11/20  (unchanged — EU fintech compliance community is tight; LinkedIn posts about DORA readiness drive inbound; not broadly viral)

**Strengths:**
- ESMA published updated Operational Instructions for DORA incident reporting in September 2026 — fresh regulatory guidance creates fresh compliance anxiety and search demand.
- Each NCA uses a different portal (Central Bank of Ireland, AFM, BaFin MVP, ACPR) with different template formats. No unified workbench exists for multi-jurisdiction entities.
- The 4-hour initial notification + 72-hour intermediate report are binding; first enforcement actions in 2026 SREP cycle will focus attention.

**Risks:**
- Vendorica is reported to offer "automated ITS submission and direct NCA integration" — if it covers all 5 major NCAs, it reduces DORAIncident's wedge.
- National portals may eventually interconnect, reducing the multi-NCA coordination problem.
- Scope uncertainty: some smaller EU financial entities are still unclear whether DORA applies to them.

**Verdict:** Enter. ESMA operational instructions just published — creates a fresh demand wave. Multi-NCA fragmentation confirmed and growing.

### The Pitch
**Problem:** EU payment institutions, e-money institutions, and crypto-asset service providers under DORA must file a major ICT-incident initial notification within 4 hours of classification, an intermediate report within 72 hours, and a final report within one month. Each national competent authority — the Central Bank of Ireland, the AFM, BaFin, the ACPR, the FCA — has its own reporting portal, its own template format, and its own submission process. A firm operating in multiple EU jurisdictions must track which authority requires which format, maintain the classification evidence from RTS 2025/301, and ensure field-level consistency across three separate submissions per incident. ESMA published updated Operational Instructions in September 2026. The tools that help today are five PDFs and a shared spreadsheet.

**Solution:** DORAIncident is an incident reporting workbench: the 4h/72h/30-day clocks start automatically when you log an incident, the platform generates the initial notification, intermediate report, and final report for the NCA(s) you select, and maps the RTS fields to each authority's required template. You review, add context, and export a submission-ready file. For firms in multiple jurisdictions, all three submissions are generated from a single incident record.

**Target customer:** ICT Risk / Compliance lead at a 50–500 person EU payment institution, e-money firm, or CASP subject to DORA. Buyer: CRO or CISO. Users: ICT risk team + compliance officer who owns the NCA relationship.

**Why now:** DORA has been in force since January 17, 2025. First enforcement for incident reporting failures is expected in 2026 SREP assessments. ESMA published fresh Operational Instructions in September 2026 — meaning the compliance playbook just changed and every affected firm is re-reading the rules.

**Why they buy without being sold to:** An ICT risk manager who gets paged at 2am for a potential major incident opens DORAIncident, logs the event, and gets a pre-filled DORA initial notification for the CBI portal ready for legal review in 15 minutes instead of 90. The free "Incident Dry Run" (simulate a classification exercise for a fictional incident) shows the value before the real incident arrives.

**Revenue model:** €399/month (1 NCA, clock management, classification evidence log). €699/month (up to 3 NCAs + multi-user + template export). €999/month (5 NCAs + SSO + audit export for SREP). Annual −2 months. Free "Incident Dry Run" as lead magnet (no login required for first simulation).

**Unfair advantage:** Pre-built NCA template library (CBI, AFM, BaFin, ACPR, DNB) mapped to ITS 2025/302 fields; clock-based urgency tool that becomes operationally essential under pressure; first-mover SEO on "DORA incident reporting software."

### Solo Build Plan
1. Weeks 1–3: Incident log; 4h/72h/30-day clocks; RTS 2025/301 classification criteria checklist; evidence attachment.
2. Weeks 4–5: Template generator for CBI + AFM portal formats (JSON/XLSX); field mapping from incident record to NCA template fields.
3. Weeks 6–7: BaFin + ACPR templates; multi-NCA simultaneous export; submission tracking (filed / pending / overdue).
4. Weeks 8–9: Stripe; "Incident Dry Run" free lead magnet (fictional incident, live simulation); onboarding for 3-person ICT risk teams.
5. Weeks 10–12: Pilot 5 EU fintechs through EU fintech compliance Slack, DORA working groups, EBA/ESMA guidance communities.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-25
**Strongest part:** The multi-NCA template fragmentation is structural — each regulator maintains its own portal and format, creating a coordination problem that centralised tools cannot solve without a workbench layer.
**Open question:** Is Vendorica already covering all major NCA jurisdictions with automated ITS submission? If so, DORAIncident needs to differentiate on UX or on the SME fintech segment Vendorica may not serve.

---

## #4 — ModelReg  ·  74/100  ·  UNCHANGED
First added: 2026-08-28 | Last updated: 2026-09-25 | Score delta this week: —

> Your community bank's AI governance policy, evidence folder, and OCC exam response — built and maintained, not improvised the week before the examiner arrives.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — guided questionnaire + evidence vault + policy document generator; legal accuracy is the hard constraint, not technical complexity)
- Value Clarity:       16/20  (unchanged — OCC exam letter = immediate pain trigger; CCO who received SR 26-2 guidance in April knows what they need)
- Market Timing:       16/20  (unchanged — SR 26-2 in force April 17, 2026; OCC Bulletin 2026-13 same day; AegisAI Evidence Tracker still email waitlist only; AICMP.eu is EU-focused, not US SR 26-2; Cardamon targets Revolut-scale fintechs)
- B2B Monetisation:    15/20  (unchanged — community banks pay for compliance tools; $299–799/month vs. $5–10K consultant engagement)
- Pull Factor:         13/20  (unchanged — ABA/ICBA community bank networks are tight; exam-prep anxiety travels quickly)

**Strengths:**
- AegisAI Evidence Tracker is still email waitlist only — the gap remains exactly as documented last week.
- AICMP.eu covers EU AI Act + GDPR + DORA, but not US SR 26-2 / OCC Bulletin 2026-13 — different regulatory regime.
- The "OCC exam readiness assessment" free tool is a sustainable lead-generation mechanism with zero paid alternatives.

**Risks:**
- AegisAI launches Evidence Tracker SaaS at any subscription price — the main warm-lead pipeline and primary competitor risk.
- Canarie.ai now serves community banks with compliance execution automation, though its focus is BSA/AML and fair lending, not AI governance specifically.
- SR 26-2 is principles-based; some banks may conclude they can handle it with existing GRC tools.

**Verdict:** Hold. No material change. AegisAI's evidence tracker launch remains the signal to watch.

### The Pitch
**Problem:** In April 2026, the Federal Reserve issued SR 26-2 and the OCC issued Bulletin 2026-13 — both establishing AI risk management expectations for community banks and mid-size financial institutions. Examiners now expect a written AI governance policy, a model inventory covering vendor-provided AI tools, evidence of human oversight for AI decisions, and documentation showing how the institution monitors AI fairness and model drift. Community banks with $500M–$10B in assets have no dedicated AI governance staff. When the examiner asks, the answer is a mix of vendor SOC2 reports, informal meeting notes, and a slide deck from an outside consultant.

**Solution:** ModelReg guides community banks through SR 26-2 compliance step by step: it builds the AI model inventory from a structured interview, generates a board-ready AI governance policy using the institution's own risk appetite language, creates evidence slots for each key control (human review logs, vendor due diligence, drift monitoring), and produces an exam-ready evidence folder. The CCO reviews and approves; ModelReg maintains the audit trail.

**Target customer:** CCO / Chief Risk Officer at a US community bank or credit union with $200M–$10B in assets, 20–200 employees. Buyer: CCO or CEO. Users: CCO + any compliance analyst. Does not have a dedicated model risk management function.

**Why now:** SR 26-2 and OCC Bulletin 2026-13 are in force as of April 17, 2026. OCC examinations beginning in late 2026 and 2027 will assess compliance. No purpose-built, affordable SaaS tool exists — AegisAI provides free assessments and PDF templates, but its evidence tracking SaaS is email waitlist only.

**Why they buy without being sold to:** A CCO preparing for an OCC exam in Q1 2027 runs the free ModelReg "OCC AI Exam Readiness Assessment," sees 7 gaps in their current documentation, and realises the assessment tool is generating the exact evidence package the examiner will request.

**Revenue model:** $299/month (1 institution, AI model inventory, governance policy generator, 3 users). $499/month (unlimited users + vendor AI assessment pack + exam prep export). $799/month (multi-institution + SSO + custom policy language). Annual −2 months. Free "OCC AI Exam Readiness Assessment" as lead magnet.

**Unfair advantage:** US community bank-specific SR 26-2 / OCC Bulletin 2026-13 policy templates; free exam readiness assessment drives inbound from banks actively preparing; distribution through ABA, ICBA, and community bank compliance networks that Cardamon (Revolut-scale) and AICMP.eu (EU-focused) don't reach.

### Solo Build Plan
1. Weeks 1–3: AI model inventory wizard (vendor tool name, use case, risk level, human-oversight description); policy generator using institution inputs + SR 26-2 template.
2. Weeks 4–5: Evidence vault (control → evidence slot → upload + expiry date); gap analysis dashboard showing which SR 26-2 controls are documented vs. missing.
3. Weeks 6–7: Vendor AI assessment questionnaire (sends to each AI vendor and collects SOC2/model card responses); board report PDF generator.
4. Weeks 8–9: Stripe; free "OCC AI Exam Readiness Assessment" lead magnet (no login; outputs gap summary + "your 3 biggest exam risks").
5. Weeks 10–12: Pilot 5 community banks through ABA compliance forums, ICBA technology council, and OCC exam-prep communities.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-25
**Strongest part:** Free exam readiness assessment creates a "find your own gaps" self-closing loop that doesn't require a sales pitch — AegisAI proved the format works (their free browser tool is their main acquisition channel).
**Open question:** Will AegisAI launch its Evidence Tracker SaaS before ModelReg reaches 50 paying customers? That is the primary competitive risk to monitor weekly.

---

## #5 — RuleFlow  ·  73/100  ·  DECLINED
First added: 2026-08-16 | Last updated: 2026-09-25 | Score delta this week: −1

> New federal rules become a checklist and an evidence folder — not another unread PDF in Slack.

### Score Breakdown
- Solo Buildability:   13/20  (unchanged — FRTracker-class obligation feed + Asana/Jira tasks + evidence ZIP; legal-correctness review is the hard part)
- Value Clarity:       16/20  (unchanged — "this rule changed, here is what you must do by when" is a 15-second pitch for a CCO)
- Market Timing:       15/20  (−1 — Canarie.ai explicitly targets community banks, credit unions, and fintechs with automated compliance workflow execution and built-in evidence capture; Remllo also maps obligations → controls → tasks → evidence for fintech/banks. The mid-market workflow layer RuleFlow was targeting is now partially served by Canarie.)
- B2B Monetisation:    17/20  (unchanged — community banks and fintech lenders already pay six figures in fines and consultants; $399–799/month is cheap next to that)
- Pull Factor:         12/20  (+1 — compliance communities share tools quietly; Canarie's existence validates the category and may increase buyer awareness)

**Strengths:**
- FRTracker still extracts must/shall/may-not obligations deterministically — RuleFlow's workflow layer on top of public obligation feeds remains the unpaid job.
- Enterprise RegTech (FinregE, CUBE, AscentAI) still starts at five figures/year. Canarie targets community banks but its pricing is undisclosed — likely SaaS-tier, not enterprise.
- Traceable, non-black-box obligation extraction with source citations is a genuine moat for auditors.

**Risks:**
- Canarie.ai is a direct competitor in the community bank segment and has a compliance execution product already shipping.
- Remllo maps regulatory obligations to workflows for fintechs — another emerging direct competitor.
- FRTracker itself may add Jira/Asana export and collapse the workflow layer.

**Verdict:** Hold #5 but narrow the wedge: position explicitly against Canarie on "obligation-feed-first" (rules you don't know about yet) vs. Canarie's "execution-first" (automating known recurring tasks). Different entry points for the same compliance buyer.

### The Pitch
**Problem:** A four-person compliance team at a community bank or fintech lender tracks Federal Register changes in a shared spreadsheet and a Slack channel of PDFs. Canarie and Remllo automate recurring compliance workflows — attestations, policy reviews, control testing — but they start from obligations you already know about. When a new final rule drops, nobody owns the checklist, and the exam asks for evidence that does not exist. FRTracker (free) extracts individual must/shall obligations from 989K+ documents — but it is a research tool, not a system of record.

**Solution:** RuleFlow watches the federal agencies you care about, diffs proposed vs. final rule text, and opens Asana/Jira items for each new obligation mapped to the source passage. At exam time you export a folder: rule, obligation, who did what, attached proof. RuleFlow starts from "what changed" — Canarie starts from "what you already do." Together they fill the compliance operating model; RuleFlow is the feed layer.

**Target customer:** CCO / compliance analyst at a 20–200 person US fintech lender, community bank, or payments firm. Not a broker-dealer mega-firm. Buyer: CCO or General Counsel. Users: the 2–6 people who currently paste Federal Register links into Slack.

**Why now:** YC's Fall 2026 RFS (23 Jul) asked for AI-native compliance infrastructure that maps activities to rules, filings, and evidence. Canarie's emergence validates the category. Enterprise RegTech still starts at six figures. The "horizon scanning → obligation → evidence" workflow for mid-market remains unclaimed at $399–799/month.

**Why they buy without being sold to:** After a consent order or a nasty Federal Reserve notice, the CCO pastes last month's "rules we think apply" spreadsheet into RuleFlow, sees three missed effective dates, and refuses to go back to Slack-PDFs.

**Revenue model:** $399/month (1 agency family + 10 users). $599/month (3 families + Jira/Asana sync). $799/month (unlimited + evidence vault + SSO). Annual −2 months. 14-day trial on a saved agency watchlist.

**Unfair advantage:** Obligation→task→evidence mapping for one vertical (US depository / fintech lending) with citations back to primary text. The "new rule discovery" entry point that execution-first tools like Canarie don't cover.

### Solo Build Plan
1. Weeks 1–3: FRTracker API or daily FR deltas; agency watchlist; obligation cards with source quotes.
2. Weeks 4–5: Task export to Asana/Jira; owner + due date; proposed-vs-final diff view.
3. Weeks 6–7: Evidence upload per obligation; exam-pack ZIP/PDF.
4. Weeks 8–9: Stripe; fintech-lending template (lending, BSA/AML notices, CFPB).
5. Weeks 10–12: Pilot 5 CCOs via ABA/community-bank ops groups and fintech compliance Slack.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-25
**Strongest part:** The "obligation-feed-first" positioning is a genuine differentiator from Canarie's execution-first model — but it requires buyers to understand they have two different jobs, and selling that distinction is harder than selling "automate your existing compliance tasks."
**Open question:** Will Canarie add a "regulatory horizon scanning" module, converting from a competitor-in-a-different-lane into a direct threat?

---

## #6 — AgentCreds  ·  72/100  ·  NEW
First added: 2026-09-25 | Last updated: 2026-09-25 | Score delta this week: —

> Ship your AI agent past the security review — with a per-scope credential manifest and rotation schedule, not a shared API key.

### Score Breakdown
- Solo Buildability:   14/20  (OAuth app registration + per-agent profile + approval workflow + audit log; each platform has different OAuth implementation quirks; 10 core integrations in 3 months is tight but achievable with OAuth libraries)
- Value Clarity:       14/20  (DevSecOps teams immediately understand "service account manager for AI agents"; less obvious to a non-technical buyer; the "security review blocker" scenario is highly specific and self-closing)
- Market Timing:       16/20  (Ampersand 2026 State of Agentic Integrations: 45% cite authentication/credentials as a top deployment blocker, 47% cite "defining what agents are allowed to do"; agentic AI entered production at scale in 2026; no dedicated tool exists)
- B2B Monetisation:    16/20  (security tooling budgets are real; $199–699/month is within norms for credential management; one avoided security incident pays for years; clear ROI narrative)
- Pull Factor:         12/20  (DevSecOps communities share tools; "we solved our AI agent auth problem" posts travel on LinkedIn and Hacker News; not broadly viral but well-targeted)

**Strengths:**
- Ampersand 2026 quantifies the exact pain: 45% auth/credentials blocker, 47% "what can agents do" blocker. Two independent data points for the same product.
- No existing product covers AI-agent-specific OAuth provisioning and scope management — IAM platforms (Okta, HashiCorp Vault, Teleport) are generic and not optimised for the agentic workflow.
- First-mover positioning in a category that security teams know they need but haven't had budget to build internally.

**Risks:**
- Okta, HashiCorp Vault, or Teleport add AI agent profile features — the category is large enough for incumbents to notice.
- The market of "companies whose AI agent deployments have been blocked by security reviews" may be smaller than the stat suggests in late 2026.
- Each SaaS platform's OAuth implementation has quirks that make the 10-integration goal harder than it appears.

**Verdict:** Enter. First mover in a clearly quantified, emerging gap; security buyer with existing budget; self-closing scenario.

### The Pitch
**Problem:** B2B SaaS companies deploying AI agents in 2026 face an invisible blocker: the security review. An agent that writes to HubSpot, reads from Salesforce, and posts in Slack needs three separate service accounts — each with scoped OAuth permissions, formal approval, and a rotation schedule. Most teams skip this: they use a shared API key, a developer's personal token, or a "we'll clean this up later" service account with admin scope. When security asks — or when the agent misbehaves — there's no clean answer. Ampersand's 2026 State of Agentic Integrations: 45% of teams cite authentication and credentials as a top deployment blocker; 47% say "defining what agents are allowed to do" blocks shipping.

**Solution:** AgentCreds provisions a named service account per agent workflow. You configure which external system, what minimum OAuth scopes, and who must approve. AgentCreds registers the OAuth app, handles token issuance and rotation, and produces a one-page credential manifest — the document your security review actually needs. No shared keys, no admin tokens, no explaining to the CISO what the agent has access to.

**Target customer:** Head of Security or DevOps lead at a 20–200 person AI-forward B2B SaaS company shipping 2+ AI agent workflows against external SaaS APIs. Buyer: Head of Security or CTO. User: DevOps engineer building agent infrastructure.

**Why now:** Agentic AI entered production at scale in 2026. The first wave of deployments used shared developer credentials. The second wave is hitting security reviews. The IAM incumbents (Okta, HashiCorp Vault, Teleport) were not designed for AI agents operating at machine speed with narrow write-scoped OAuth. The pattern of "one service account per agent per integration" with per-scope approval doesn't exist as a productised workflow anywhere.

**Why they buy without being sold to:** A DevOps lead whose AI agent deployment is blocked pending "documentation of OAuth scopes and a rotation policy" installs AgentCreds, generates the per-agent credential manifest in 20 minutes, and hands it to the security team. The review passes. The agent ships.

**Revenue model:** $199/month (up to 5 agent profiles, 5 integrations, audit log). $399/month (unlimited agents + auto-rotation + approval workflows). $699/month (SSO + export to HashiCorp Vault/Doppler + compliance report PDF). 14-day trial. Annual −2 months.

**Unfair advantage:** Pre-built OAuth profiles for the 10 SaaS APIs that AI agents most commonly call (HubSpot, Salesforce, Slack, GitHub, Jira, Linear, Notion, Stripe, Google Workspace, Zendesk) — reducing setup from days to minutes. Distribution through AI engineering communities actively hitting this exact wall.

### Solo Build Plan
1. Weeks 1–3: OAuth app registration wizard for 5 platforms (HubSpot, Slack, GitHub, Jira, Salesforce); per-agent named credential profile; scope selection UI with "minimum necessary" templates.
2. Weeks 4–5: Immutable audit log (provisioned by, approved by, scopes, last rotation, last used); rotation reminder system (email/Slack alerts).
3. Weeks 6–7: One-page credential manifest export (PDF/JSON) for security review packets; approval workflow (request scope change → security lead approves → credentials issued).
4. Weeks 8–9: Stripe; 14-day trial onboarding; agent archetype templates (CRM reader, ticket-triage agent, code-review bot, lead-enrichment agent).
5. Weeks 10–12: Pilot 5 companies through Anthropic Builder Community, r/AIAgents, DevSecOps Slack communities.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-25
**Strongest part:** The Ampersand 2026 data provides two independent quantified signals (45% auth blocker + 47% "what can agents do" blocker) that together define a product — not just a pain point.
**Open question:** Is the addressable market (companies currently blocked by AI agent security reviews, as opposed to companies that should be doing this but haven't prioritised it) large enough in Q4 2026, or does this need 12 more months of agentic AI adoption to reach critical density?

---

## #7 — AuthTrack  ·  71/100  ·  UNCHANGED
First added: 2026-08-16 | Last updated: 2026-09-25 | Score delta this week: —

> See which prior auths are inside the 7-day / 72-hour clock — and which denials still have no specific reason.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — CSV/fax log + calendar clocks + denial-reason fields; no EHR writeback in v1; HIPAA applies but achievable for a focused solo build)
- Value Clarity:       16/20  (unchanged — "this PA blows the CMS clock on Thursday" is obvious to a biller; the missed-clock scenario is self-closing)
- Market Timing:       14/20  (unchanged — CMS-0057-F operational since Jan 1, 2026; FHIR PA APIs due Jan 1, 2027; entry-level PA platforms price at $500–$2,500/month, far above AuthTrack's $149–299 target; the 2–10 provider fax-era practice is still unserved at this price point)
- B2B Monetisation:    14/20  (unchanged — $149–299/month for a billing coordinator's time; one avoided write-off pays for a year; strong ROI narrative)
- Pull Factor:         13/20  (unchanged — biller Facebook groups are tight; word travels when a tool saves a missed-clock dispute)

**Strengths:**
- Linear Health, Notove AI, Waystar, CoverMyMeds all price at $500–$2,500+/month and target specialty practices and health systems. The 2–10 provider fax-era practice is documented as underserved.
- CMS-0057-F clocks are live and enforceable. 2027 MIPS "at least one electronic PA" creates a documentation ramp that AuthTrack's log satisfies.
- Spreadsheet-first design avoids the 4-week EHR integration that kills solo scope.

**Risks:**
- HIPAA + PHI handling from day one requires BAA flow and careful data governance.
- Clearinghouses (Waystar, Availity) could add a cheap clock-tracker SKU for small practices.
- The FHIR PA API mandate (Jan 2027) may push some small practices to switch to a full PA automation platform, reducing AuthTrack's addressable window.

**Verdict:** Hold. Competitive market at $500+ is documented; $149 price gap is real; FHIR 2027 mandate creates urgency without yet displacing the fax-era workflow.

### The Pitch
**Problem:** Since January 1, 2026, Medicare Advantage, Medicaid, CHIP, and FFE QHP payers must decide standard prior auths within 7 calendar days and urgent ones within 72 hours, and every denial must include a specific reason. Billing coordinators at 2–10 provider practices still track this in a spreadsheet next to the fax machine. Entry-level PA platforms price at $500–$2,500/month and require EHR integration. The 2–10 provider practice on fax/portal has no clock management tool at a price that makes sense.

**Solution:** AuthTrack is the PA status board: each request gets a clock, a channel (fax/portal/phone), a denial-reason field, and a reminder before the CMS window closes. v1 is CSV import + form entry — no Athena integration, no FHIR client.

**Target customer:** Billing coordinator / office manager at a 2–10 provider US practice (PT, specialty lite, independent primary care) that is not on Athena+Linear Health. Buyer: office manager. User: the biller who owns the Excel PA tab.

**Why now:** The clocks are live, not upcoming. The FHIR API mandate is January 1, 2027 — practices that do not have a log now will scramble in the months before the deadline. Entry-level PA platforms won't serve this segment at $149/month.

**Why they buy without being sold to:** After a denied MRI with no specific reason and a missed 7-day follow-up, the biller pastes the spreadsheet into AuthTrack, sees two clocks already red, and stops using Excel that week.

**Revenue model:** $149/month (1 location, 200 PAs). $249/month (3 locations + reminder SMS). $299/month (export pack for appeals). Annual −2 months. 14-day trial with sample CSV.

**Unfair advantage:** CMS-clock templates + denial-reason required field sized for fax-era shops that enterprise PA platforms ignore.

### Solo Build Plan
1. Weeks 1–3: PA log (CSV import); 7-day / 72-hour clocks; denial-reason required on deny.
2. Weeks 4–5: Email/SMS reminders; aging report; appeal packet PDF.
3. Weeks 6–7: HIPAA BAA flow; audit log; role-based access.
4. Weeks 8–9: Stripe; sample-CSV onboarding.
5. Weeks 10–12: Pilot 6 small practices via biller Facebook groups and local MGMA chapters.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-25
**Strongest part:** The price gap between AuthTrack ($149) and entry-level PA automation ($500–$2,500) is now confirmed by multiple market sources — the fax-era practice is explicitly documented as underserved.
**Open question:** Will tiny practices pay $149/month for clock management, or will they wait for their clearinghouse to add a free PA clock as a retention feature?

---

## #8 — AgentAudit  ·  71/100  ·  NEW
First added: 2026-09-25 | Last updated: 2026-09-25 | Score delta this week: —

> Inventory every MCP server your developers have installed — and know which ones have too much access before the auditor asks.

### Score Breakdown
- Solo Buildability:   15/20  (JSON config parsing + npm audit wrapper + scope classification; achievable in 2–3 months; the hard part is accuracy of scope classification, not technical complexity)
- Value Clarity:       14/20  (DevSecOps teams immediately understand "security audit of all your MCP servers"; the free CLI scan is a self-closing demo that requires no explanation)
- Market Timing:       14/20  (MCP became the universal AI tool standard in 2026; npm lists 2,000+ MCP packages; SOC2/ISO27001 auditors starting to ask about AI tooling scope; no dedicated MCP security scanner exists; window is 6–18 months before IDEs build this natively)
- B2B Monetisation:    14/20  ($149–499/month is standard for security tools at 20–200 person companies; comparison: 1Password Teams ~$4/user/month for 25-user team = $100/month baseline)
- Pull Factor:         14/20  (security findings are inherently shareable; "I found 3 overprivileged MCP servers in my config" posts travel fast in DevSecOps communities; free CLI creates organic inbound)

**Strengths:**
- Zero direct competition: no dedicated MCP security scanner exists as of September 2026.
- The free CLI creates a viral discovery mechanism — every security blog post about MCP risks drives inbound.
- Pre-built risk profiles for the 200 most-used MCP packages create a defensible data moat.

**Risks:**
- Anthropic, Cursor, or npm could add native MCP server security scanning — the biggest kill signal.
- The market of companies with both a security function AND active MCP adoption may be small in late 2026.
- MCP package scope declarations are self-reported by the package author — a malicious package can lie, limiting scanner accuracy.

**Verdict:** Enter. First mover in a growing attack surface; viral CLI acquisition; clear security buyer at a standard price point.

### The Pitch
**Problem:** AI development in 2026 runs on MCP. Cursor, Claude Code, and Windsurf users install dozens of MCP servers — each one with declared scopes for filesystem access, web browsing, database reads, API writes, or shell execution. The npm ecosystem now lists 2,000+ MCP packages. Security teams have no visibility: which packages are installed on which developer machines, what each one is allowed to do, whether any packages have known CVEs, and whether scope creep has occurred since the last review. When SOC2 auditors ask about AI tooling permissions, the answer is usually "we'll get back to you." When a malicious MCP package is published, nobody knows which developers installed it.

**Solution:** AgentAudit scans every MCP configuration file in your environment (Claude Desktop, Cursor, Windsurf, and custom MCP configs), builds a complete inventory of installed servers, classifies each by scope category (filesystem, web access, API writes, shell execution), checks package versions against npm advisories and the OSV vulnerability database, and flags packages with known CVEs or unusually broad scopes. Results are presented as a security report and enforced via a GitHub Action that blocks PRs adding unreviewed MCP servers.

**Target customer:** Security engineer or IT lead at a 20–200 person company where developers use AI coding tools with MCP integrations. Buyer: Head of Security or IT Director. Users: security team conducting the AI tooling inventory.

**Why now:** MCP became the universal AI tool standard in 2026 — every major AI coding tool adopted it. The attack surface created by 2,000+ npm MCP packages is real and unscanned. SOC2 and ISO27001 auditors are beginning to include AI tool permissions in scope reviews. No dedicated MCP security scanner exists today.

**Why they buy without being sold to:** A security engineer runs the free AgentAudit CLI against their team's MCP config files, sees three servers with filesystem access to the entire home directory and one package with a known CVE, and raises it in the weekly security review. The findings write the business case.

**Revenue model:** $149/month (25 developer seats, monthly scan, Slack alerts on scope changes). $299/month (100 seats + CI/CD integration + policy-as-code). $499/month (unlimited seats + custom risk rules + quarterly audit export). Free CLI scan — individual developers, no login required. 14-day team trial.

**Unfair advantage:** First dedicated MCP security scanner with CVE correlation; free CLI creates organic inbound from "I found an overprivileged MCP server" blog posts; GitHub Action CI gate establishes the product as infrastructure before competitors react.

### Solo Build Plan
1. Weeks 1–3: CLI scanner — parse claude_desktop_config.json, Cursor .mcp.json, YAML server configs; extract server name, package, declared scopes; CVE check via npm audit / OSV API.
2. Weeks 4–5: Web dashboard (config upload or GitHub integration); inventory view; scope classification (filesystem, web, API writes, database, shell); risk score per server.
3. Weeks 6–7: GitHub Action for CI enforcement; Slack notification when new MCP server added or scope escalates; weekly digest email.
4. Weeks 8–9: Stripe; free CLI → paid dashboard upgrade funnel; "MCP Security Report" PDF for security review packets.
5. Weeks 10–12: Pilot 10 companies via DevSecOps Slack communities, security-focused engineering blogs, GitHub Security advisories channel.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-25
**Strongest part:** The free CLI scan → "I found something scary" → paid team dashboard is the cleanest PLG acquisition loop in this cookbook — no sales pitch needed, the tool closes itself.
**Open question:** Will Anthropic or Cursor ship native MCP server security scanning in the IDE before AgentAudit establishes a user base? The 6–12 month window is the critical build-and-ship timeline.

---

## #9 — IntegSecPack  ·  70/100  ·  DECLINED
First added: 2026-09-18 | Last updated: 2026-09-25 | Score delta this week: −1

> Close the enterprise deal — with an AI-agent integration security evidence pack that answers the CISO questionnaire before it blocks the signature.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — questionnaire template library + evidence upload + trust page generator; no EHR or complex integration required; achievable solo)
- Value Clarity:       16/20  (unchanged — "68% of B2B SaaS lost or delayed enterprise deals over integration security concerns" is a CFO sentence; lost-deal pain is immediate)
- Market Timing:       14/20  (−1 — Vanta launched its Agentic Trust Platform + AI Agent 2.0 in 2026 with explicit AI-agent control frameworks and questionnaire automation; Vanta's LinkedIn post explicitly references "which tools agents call, which RAG documents they access, what prompts/responses are allowed." Kill signal timeline is accelerated — Vanta will likely add AI-agent-specific questionnaire sections within 6 months.)
- B2B Monetisation:    15/20  (unchanged — $149–399/month; sales/RevOps budget; one closed deal pays for 12 months)
- Pull Factor:         11/20  (unchanged — security buyers share tools through Slack + LinkedIn; "we closed a $200K deal by shipping our AI security evidence pack in a day" is a shareable story)

**Strengths:**
- Ampersand 2026: 68% of B2B SaaS lost or delayed enterprise deals due to integration security concerns — this is now the documented top deal-blocker in the category.
- Whistic and SecurityPal still do not have AI-agent-specific questionnaire sections as of September 2026.
- The "pre-sales evidence pack" framing (vs. ongoing GRC compliance) is a distinct product that Vanta's compliance-focused platform doesn't natively serve.

**Risks:**
- Vanta's AI Agent 2.0 and explicit AI-specific framework coverage suggest an AI-agent questionnaire section is coming within 6 months.
- SecurityPal or Whistic could add an AI-agent template — both serve the pre-sales questionnaire market directly.
- The "integration security evidence pack" concept requires B2B SaaS sellers to understand both their integration architecture and AI agent usage well enough to generate accurate evidence.

**Verdict:** Hold but watch closely. Vanta's accelerating AI-specific coverage means the window is narrowing.

### The Pitch
**Problem:** 68% of B2B SaaS companies either lost (16.3%) or delayed (27%) or both (24.7%) an enterprise deal in 2026 because of integration-related security or compliance concerns (Ampersand 2026 State of Agentic Integrations). Enterprise buyers are now asking: "How are your AI agents authenticated against our systems? What do they have access to? What is your audit trail?" Sales cycles stall for weeks while security teams assemble evidence that doesn't exist in a single place.

**Solution:** IntegSecPack generates a pre-sales integration security evidence pack: OAuth scopes and authentication methods for each integration, AI-agent permission model (what each agent can read and write), data retention and processing locations, SOC2 control mapping, and a customisable questionnaire response template for the CISO's security review. Upload your existing SOC2 report and architecture diagram; IntegSecPack maps them to the 47 most common enterprise integration security questions, including the 8 AI-agent-specific sections that Whistic, SecurityPal, and Vanta Trust Report don't yet cover.

**Target customer:** Sales Engineer / Head of Sales at a 15–250 person B2B SaaS company in an active enterprise deal with a security review requirement. Buyer: VP Sales or CTO. Users: Sales engineers + security team drafting questionnaire responses.

**Why now:** AI agents entered production in 2026 and enterprise buyers are adding AI-agent-specific questions to their vendor security reviews — questions that no pre-built questionnaire template yet answers. The standard vendor risk questionnaires (SIG, CAIQ, SOC2-based) predate the agentic era. The evidence pack must be built fresh for each deal today.

**Why they buy without being sold to:** A sales engineer who just received a 47-question security questionnaire with 8 AI-agent-specific questions uploads their architecture diagram and SOC2 report to IntegSecPack, gets a completed first-pass response in 20 minutes, and closes the 3-week security review stall in one afternoon.

**Revenue model:** $149/month (1 evidence pack, up to 10 active deals). $249/month (unlimited packs + questionnaire template library). $399/month (SSO + custom brand + AI-agent-specific evidence module). Annual −2 months. 14-day trial with a sample evidence pack generated from a demo company's architecture.

**Unfair advantage:** The only pre-sales evidence pack with a dedicated AI-agent integration section; maps to the specific questions enterprise CISOs are adding to vendor security reviews in 2026; faster than building from scratch for every deal.

### Solo Build Plan
1. Weeks 1–3: Questionnaire template library (SIG, CAIQ, and the 8 AI-agent-specific questions documented from real enterprise deals); architecture diagram upload + annotation.
2. Weeks 4–5: Evidence pack generator — maps SOC2 controls to questionnaire responses; OAuth scope documentation template; AI-agent permission model form.
3. Weeks 6–7: Deal tracking (which customers have received which pack, which sections remain outstanding); team collaboration (sales + security sign-off).
4. Weeks 8–9: Stripe; demo company sample pack as onboarding; 14-day trial with live evidence pack.
5. Weeks 10–12: Pilot 6 B2B SaaS companies through sales-engineering Slack communities and RevOps forums.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-25
**Strongest part:** The Ampersand 2026 "68% lost or delayed deals" figure is a CFO-level data point that justifies spending $249/month on a product that closes deals.
**Open question:** Will Vanta add an AI-agent-specific questionnaire section to its trust center within the next 6 months — killing the only differentiator that makes IntegSecPack distinct from existing vendor security platforms?

---

## #10 — ChurnDetect  ·  68/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-09-25 | Score delta this week: −2

> Find the customers about to leave — 90 days before they tell you — from the support tickets they are already sending.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — Zendesk/Intercom API + AI ticket classification + Slack alerts = 3 months feasible for a focused MVP)
- Value Clarity:       17/20  (unchanged — "retrospective demo on your last churned account" is self-closing; no pitch required after that demo)
- Market Timing:       12/20  (−1 — MASQON, FeedPulse AI, PulseQA, Finsi, and Pylon all explicitly providing support-ticket churn risk scoring and account-level aggregation; the category is now named and competitive; "churn detection from support tickets" is no longer an unoccupied wedge)
- B2B Monetisation:    13/20  (unchanged — CS budget exists; $199–599/month; protecting $30K ARR justifies $349/month)
- Pull Factor:         11/20  (−1 — category noise; multiple competitors mean "ChurnDetect" competes on positioning, not uniqueness; retrospective demo is still the strongest mechanism but no longer the only one)

**Strengths:**
- Retrospective demo ("see the 8 tickets before your last churned account") remains the strongest self-closing sales mechanism in this cookbook — none of the confirmed competitors feature this as their primary onboarding flow.
- The gap between enterprise (Gainsight $30K+, ChurnZero $20K+) and the competitive multi-tool landscape at $50–$300/month is still large enough for a focused $199–$599/month product.
- Historical 6-month retrospective + Intercom + account-level aggregation is differentiated from MASQON (one-time delivery) and FeedPulse AI (CSV upload only).

**Risks:**
- MASQON, PulseQA, Finsi, and Pylon all confirmed doing real-time account-level churn signal scoring from support tickets.
- Pylon combines support + customer success + account intelligence with churn detection — a potentially stronger combo than a point solution.
- The category is now defined and competitive; ChurnDetect needs to win on execution, not just concept.

**Verdict:** Hold but reposition. The retrospective demo and multi-source real-time connector (Zendesk + Intercom + Slack) are still differentiated. But this entry needs a clearer wedge or it will slip below 65 within two runs.

### The Pitch
**Problem:** B2B SaaS companies discover customer churn risk almost exclusively at renewal time, when the decision is already made. The warning signals — frustration in tickets, repeated unresolved issues, competitor mentions — are buried in the support inbox. CS teams classify tickets by "resolved / open," not by "churn risk." A $50K ARR customer silently decides to cancel three months before renewal; the first official indication is a "not renewing" email.

**Solution:** ChurnDetect connects to your Zendesk and Intercom, reads the past 6 months of support tickets, and classifies each conversation by churn risk language, unresolved issue patterns, feature gaps, and competitive mentions. It generates a weekly list of "accounts at risk" with the specific threads that triggered each flag, along with a priority score. The retrospective demo — which replays the 8 tickets before any churned account — is the free trial experience.

**Target customer:** Customer success manager / VP CS at a 10–150 person B2B SaaS company with 100+ customers. Buyer: VP CS or CRO. Users: CS team. Uses Zendesk or Intercom. Does not have Gainsight or ChurnZero. Company runs $1M–$15M ARR where individual account loss is felt immediately.

**Why now:** LLMs in 2026 classify "this is taking way too long to resolve" as churn risk where keyword filters miss it. The classification cost is under $0.001 per ticket. Enterprise CS platforms are priced at $20–30K/year, leaving $1M–$15M ARR companies with nothing at $199–$599/month.

**Why they buy without being sold to:** A CS manager who lost a $30K account to silent churn runs the free ChurnDetect retrospective on that account's last 8 tickets, sees the risk flags she missed 90 days ago, and purchases immediately. The demo is a historical audit, not a hypothetical.

**Revenue model:** $199/month (up to 500 accounts, Zendesk). $349/month (unlimited accounts + Intercom + Slack alerts). $599/month (API + custom risk taxonomy + competitor-mention tracking). 14-day free trial. Annual −2 months.

**Unfair advantage:** Historical retrospective demo that turns the free trial into a self-closing pitch — MASQON, PulseQA, and FeedPulse don't lead with this. Vertical risk taxonomies (SaaS-specific, agency-specific) that generic sentiment tools don't have.

### Solo Build Plan
1. Weeks 1–3: Zendesk API connector; 6-month historical ticket ingestion; AI risk classification per thread (churn language, sentiment, competitor mentions).
2. Weeks 4–5: Account-level aggregation; weekly digest + Slack alerts; risk score per account with evidence thread links.
3. Weeks 6–7: Intercom connector; custom risk terms; "at risk" list with flagged quotes.
4. Weeks 8–9: Stripe; retrospective demo generator (5 historical accounts, auto-classified); data consent flow.
5. Weeks 10–12: Pilot 8 SaaS companies through CS leader Slack communities and Product Hunt launch.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-09-25
**Strongest part:** The retrospective demo is still the most creative conversion mechanism in this cookbook — historical audit of a real lost account closes itself.
**Open question:** Can ChurnDetect win on execution against MASQON + PulseQA + FeedPulse + Pylon, or is the window for a point solution closing as these broader platforms mature?

---

## Removed this run
| Entry | Last score | Reason |
|-------|------------|--------|
| ClaimSnap | 72 → 67 | **Storm Engine, ClaimScope, R360 Scope ($599/month), DumbRoof.ai** all do AI photo→Xactimate estimates for adjusters and contractors; public adjuster segment is no longer unserved; displaced by AgentCreds and AgentAudit |
| HOAEnforce | 72 → 60 | **ARCH Inspect ($79–199/month)** explicitly does AI Violation Detection + Year-over-Year Property Change AI Detection; **Domus.town** links photos to governing-rule citations, board-approved notices, and audit records; **HOATECH.net** + **LotWize** confirmed; direct kill signal from multiple live products |
