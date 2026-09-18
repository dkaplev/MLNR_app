# SaaS Opportunity Cookbook
Last updated: 2026-09-18 | Entries: 10/10

> R13 note: **MCPCostMonitor removed** — MCPSpend.com (mcpspend.com) shipped live, free tier 25K calls/month, Pro at $29/month; identical product at 10× lower price kills the wedge. **BriefDesk removed** — displaced from top-10 as three new entries score higher. **MarkPack removed** — displaced from top-10; still viable but the window is narrowing. **CRAReport enters at #2** — EU CRA vulnerability reporting obligations started September 11, 2026 (this week). **DORAIncident enters at #5** — DORA incident reporting enforcement expected 2026, first SREP assessments underway. **IntegSecPack enters at #9** — 68% of B2B SaaS companies lost/delayed enterprise deals due to integration security; AI agent authentication is a 2026-specific new procurement ask.

---

## #1 — DentPay  ·  80/100  ·  UNCHANGED
First added: 2026-07-16 | Last updated: 2026-09-18 | Score delta this week: —

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (CSV-first rule engine; OD ADP time-card export confirmed but no plug-and-play production-% payroll bridge exists)
- Value Clarity:       18/20  (OM ritual self-evident; HRPayPick 2026 confirms gap in all three major US PMS systems)
- Market Timing:      17/20  (Samera still UK Dentally/SOE; Comparisoft 2026 confirms no native OD/Dentrix/Eaglesoft production-% payroll integration)
- B2B Monetisation:   16/20  (sticky once configured; wrong paycheck = employer liability)
- Pull Factor:        13/20  (study clubs; US outreach guide for discovery calls)

**Strengths:**
- HRPayPick 2026 and Comparisoft 2026 both confirm: no payroll platform has native plug-and-play integration with OD, Dentrix, and Eaglesoft for production-% pay. Gap is durable.
- OD Time Cards export to ADP Workforce Now CSV — but ONLY hours, not production %. Production reconciliation is still manual every pay period.
- Sticky once pay rules configured — switching cost is existential (wrong paycheck = employer liability).

**Risks:**
- Dental Intelligence or Dentrix itself could deepen native pay math in a platform update.
- ADP's established Henry Schein relationship could eventually produce a native production-% bridge.
- Relationship-heavy sales; CPA/advisor trust needed for paycheck-math credibility.

**Verdict:** Hold #1. US OD CSV-first beachhead still open; ADP/OD integration only covers hours, not production %.

### The Pitch
**Problem:** US dental practices paying associates and hygienists on production still spend hours each pay period exporting Open Dental or Dentrix reports, pasting into Excel, applying lab fees, write-offs, and card-fee rules, then hoping the spreadsheet matches the contract. Open Dental's Provider Payroll report outputs raw production data — it is not a pay engine. OD Time Cards export to ADP Workforce Now, but only hours — not production percentages. Comparisoft 2026 confirms: most payroll platforms handle percentage-of-production only if you manually calculate the figure and enter it as a bonus. No platform does the reconciliation automatically across OD, Dentrix, and Eaglesoft simultaneously.

**Solution:** DentPay imports OD/Dentrix production exports, applies per-provider pay rules once, flags anomalies before payout, and exports an approval pack to Gusto/ADP. Office managers review exceptions; they do not rebuild formulas.

**Target customer:** Office manager / owner at 1–3 location US dental practice on Open Dental or Dentrix with associates or hygienists on production splits.

**Why now:** Production % pay is still the norm. UK tools (Samera/Dentivize) proved analytics willingness-to-pay in the UK; the US PMS vendors have not productised the reconciliation layer despite confirmed demand.

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
**Strongest part:** HRPayPick 2026 + Comparisoft 2026 both confirm the gap independently. ADP/OD integration covers hours only.
**Open question:** Will practices trust a solo tool with paycheck math without a CPA partnership from day one?

---

## #2 — CRAReport  ·  77/100  ·  NEW
First added: 2026-09-18 | Last updated: 2026-09-18 | Score delta this week: +77

> File your ENISA vulnerability notice in minutes — not days of legal back-and-forth.

### Score Breakdown
- Solo Buildability:   14/20  (CycloneDX/SPDX SBOM import + ENISA template generator + clocks; OSS primitives exist for SBOM scanning; legal-correctness validation is the hard part)
- Value Clarity:       17/20  (CRA vulnerability reporting obligations started September 11, 2026 — this week; "what do I report to ENISA?" is a live, immediate pain)
- Market Timing:       18/20  (perfect window: obligations just started, no purpose-built SaaS exists, Vanta/Drata retrofit will take 6–12 months)
- B2B Monetisation:    15/20  ($199–699/month for software companies with EU market exposure; clear ROI vs. €15M or 2.5% global turnover fines)
- Pull Factor:         13/20  (security engineer communities; engineering leaders share when they solve a painful compliance blocker)

**Strengths:**
- Timing is as good as it gets: CRA vulnerability reporting obligations became enforceable on September 11, 2026 — seven days before this analysis. No established SaaS tooling exists.
- SBOM tooling (Syft, Trivy, CycloneDX, SPDX) is mature OSS — the gap is ENISA notification workflow and clock automation, not dependency scanning.
- The free "CRA Scope Questionnaire" (are you in scope?) is the highest-intent lead magnet possible — every software company selling to the EU needs to answer it.

**Risks:**
- Scope ambiguity is the biggest adoption blocker: many SaaS companies don't know if they're "manufacturers of products with digital elements" and will wait for a lawyer to tell them before purchasing.
- Vanta, Drata, or OneTrust will retrofit CRA support within 6–12 months, leveraging existing trust with 10,000+ customers.
- SBOM maintenance over a product's lifecycle is genuinely hard — transitive dependencies, version drift, license changes. Underestimating this collapses the value prop.

**Verdict:** Enter now. The 6-month window before enterprise GRC platforms retrofit CRA support is the entire opportunity.

### The Pitch
**Problem:** The EU Cyber Resilience Act (Regulation 2024/2847) entered vulnerability disclosure reporting obligations into force on September 11, 2026. Every manufacturer of products with digital elements sold in the EU — SaaS vendors, IoT firmware makers, embedded software publishers — must now report actively exploited vulnerabilities to ENISA within 24 hours (early warning) and 72 hours (detailed report). Security teams know how to patch CVEs; they do not know how to file to ENISA, how to classify severity under CRA criteria, or how to maintain the SBOM documentation that supports it. Consultants charge €5,000–15,000 per incident report. SBOM maintenance is manual and ad hoc. The regulation is live and most affected companies have zero process.

**Solution:** CRAReport is the CRA compliance workbench: it imports your SBOM from CycloneDX or SPDX (or runs Syft/Trivy against your Docker image), classifies incoming CVEs against CRA severity criteria, pre-fills the ENISA notification template from your SBOM and CVE data, and tracks the 24h / 72h reporting clocks. When a vulnerability is discovered, CRAReport opens a case, alerts the right owner, and generates the regulatory submission draft — legal reviews a structured document instead of starting from a blank page. Free "CRA Scope Questionnaire" (5 questions) determines if your product is in scope.

**Target customer:** SaaS companies and cloud-hosted software vendors (15–200 employees) selling into the EU market. Buyer: CTO or Head of Security. User: security engineer + compliance officer. Initially cloud/SaaS companies where the SBOM is a Docker image manifest, not embedded firmware — the simpler starting scope.

**Why now:** CRA vulnerability reporting obligations became active September 11, 2026. No SaaS tool exists for ENISA notification workflows. Vanta and Drata are US-centric SOC 2 platforms that will take 6–12 months to retrofit EU-specific CRA reporting modules. Penalties can reach €15M or 2.5% of global annual turnover.

**Why they buy without being sold to:** A security engineer who discovers an actively exploited CVE in a dependency Googles "how to report to ENISA under CRA" and finds no clear process. CRAReport's free Scope Questionnaire tells them they're in scope. The ENISA notification template fills itself from their CVE details. They purchase before submitting the first report.

**Revenue model:** $199/month (1 product, SBOM maintenance, ENISA notifications, 24/72h clocks). $499/month (3 products + team assignment + evidence archive). $699/month (unlimited + API + CSIRT integration). Annual −2 months. 14-day trial with SBOM import from CycloneDX/SPDX.

**Unfair advantage:** CRA vulnerability reporting is brand-new as of September 11, 2026. A founder who ships CRAReport's ENISA template tool in the next 4–6 weeks becomes the brand Google indexes for "CRA ENISA vulnerability report" before enterprise GRC platforms finish their roadmap reviews. First-mover SEO in a regulatory moment is a real and durable distribution moat.

### Solo Build Plan
1. Weeks 1–3: CRA Scope Questionnaire (free, 5 questions); CycloneDX/SPDX SBOM import; vulnerability intake form (CVE ID, product, affected versions); 24h/72h clock tracker; ENISA early-warning template generator.
2. Weeks 4–5: CVE severity classifier (CRA criteria: active exploitation, broad impact, CVSS ≥7); Slack/email alerts on clock approach; report history archive.
3. Weeks 6–7: Syft/Trivy Docker image scan integration; multi-product SBOM inventory; component ownership assignment; member-state authority directory (which authority to notify by country).
4. Weeks 8–9: Stripe; 14-day trial; JIRA/GitHub issue linker for vulnerability tracking workflow.
5. Weeks 10–12: Pilot 6 EU-facing software companies via OWASP EU chapters, EU-focused developer Slack communities, and HN/EU founder communities.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-18
**Strongest part:** Timing is unambiguous — CRA reporting obligations started 7 days ago. The first-mover SEO window is real and finite.
**Open question:** Will scope ambiguity ("are we a manufacturer of products with digital elements?") delay purchasing until the first ENISA enforcement action? If so, the sales cycle is 6–12 months longer than the timing signal suggests.

---

## #3 — RuleFlow  ·  74/100  ·  IMPROVED
First added: 2026-08-16 | Last updated: 2026-09-18 | Score delta this week: +1

> New federal rules become a checklist and an evidence folder — not another unread PDF in Slack.

### Score Breakdown
- Solo Buildability:   13/20  (FRTracker-class obligation feed + Asana/Jira tasks + evidence ZIP; legal-correctness review is the hard part)
- Value Clarity:       16/20  ("this rule changed — here is what you must do by when" is a 15-second pitch for a CCO)
- Market Timing:       17/20  (+1 from 16: CRA reporting obligations started Sept 11, 2026 — the category of "turning new regulations into actionable obligation lists" just got a third high-profile mandate alongside DORA and EU AI Act; YC Fall 2026 RFS for AI-native compliance infra remains validated; FRTracker still a free research primitive with no mid-market workflow layer)
- B2B Monetisation:    17/20  (community banks and fintech lenders already pay six figures in fines and consultants; $399–799/mo is cheap next to that)
- Pull Factor:         11/20  (compliance communities share tools quietly; not LinkedIn-viral)

**Strengths:**
- FRTracker already extracts must/shall/may-not obligations deterministically — the missing product is "new rule → owner → due date → evidence," not another AI summariser.
- CRA Sept 11 + DORA enforcement expected 2026 + SR 26-2/OCC 2026-13 validate that regulatory obligation management is a multi-market need, not a one-regulation bet.
- Traceable, non-black-box extraction is a selling point for auditors.

**Risks:**
- FRTracker (or a well-funded RegTech) adds the workflow layer and collapses the wedge.
- Wrong obligation mapping creates legal liability; product must be sold as "monitoring," not advice.
- Mid-market fintech buyer count is smaller than it appears.

**Verdict:** Hold and strengthen. CRA/DORA/SR 26-2 convergence validates the category; US fintech vertical remains the beachhead.

### The Pitch
**Problem:** A four-person compliance team at a community bank or fintech lender tracks Federal Register changes in a shared spreadsheet and a Slack channel of PDFs. CUBE and AscentAI sell this to Tier-1 banks. FRTracker (free) now extracts individual must/shall obligations from 989K+ documents — but it is a research tool, not a system of record. When a final rule drops, nobody owns the checklist, and the exam asks for evidence that does not exist.

**Solution:** RuleFlow turns each relevant obligation into a task with an owner, a due date, and an evidence slot. It watches the agencies you care about, diffs proposed vs final, and opens Asana/Jira items mapped to the source passage. At exam time you export a folder: rule, obligation, who did what, attached proof.

**Target customer:** CCO / compliance analyst at a 20–200 person US fintech lender, community bank, or payments firm. Not a broker-dealer mega-firm. Buyer: CCO or General Counsel. Users: the 2–6 people who currently paste Federal Register links into Slack.

**Why now:** YC's Fall 2026 RFS asked for AI-native compliance infrastructure. The open primitive (FRTracker) exists; the mid-market workflow layer does not. Enterprise RegTech still starts at six figures. Three concurrent regulation waves (DORA, CRA, SR 26-2) validate the category across markets simultaneously.

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
**Strongest part:** The primitive is free and public; the unpaid job is workflow + evidence, which is exactly what a 4-person team will pay for. CRA/DORA/SR 26-2 convergence confirms the category timing.
**Open question:** Will FRTracker itself add "send to Jira" and eat the wedge?

---

## #4 — ModelReg  ·  74/100  ·  UNCHANGED
First added: 2026-09-04 | Last updated: 2026-09-18 | Score delta this week: —

> Turn SR 26-2 examiner expectations into a board-ready AI governance evidence folder — before the exam letter arrives.

### Score Breakdown
- Solo Buildability:   14/20  (policy templates + model inventory + evidence log + board report; no ML engineering required; legal validation is the constraint)
- Value Clarity:       16/20  ("exam letter trigger" — examiners are now asking about AI governance before formal guidance; AegisAI Evidence Tracker still "coming soon")
- Market Timing:       17/20  (OCC announced forthcoming AI-specific RFI; AegisAI Evidence Tracker still email waitlist as of Sept 18; SR 26-2 is principles-based — banks must tell their own compliance story)
- B2B Monetisation:    15/20  ($299–599/month vs $5K–20K compliance consultant; community bank budget is real)
- Pull Factor:         12/20  (compliance officer peer networks at ABA/IBAT events; exam-letter FOMO travels fast)

**Strengths:**
- AegisAI Evidence Tracker is still "coming soon" — email waitlist only. Free assessment + $29/$49/$99 template kits. No operational SaaS product has launched.
- OCC confirmed it will issue an AI-specific RFI "in the near future" — examiners ask AI governance questions before formal guidance lands, per documented examiner findings.
- SR 26-2 is principles-based: "the bank must tell its own compliance story" — a software tool that organizes this story is the exact unpaid job.

**Risks:**
- AegisAI Evidence Tracker launches within 3 months (still the main kill signal).
- OCC issues prescriptive AI examination procedures, reducing the "tell your story" differentiation.
- Community banks trust their core vendor (Jack Henry, FIS, Fiserv) for compliance tools — distribution through core vendors is hard.

**Verdict:** Hold. AegisAI Evidence Tracker launch remains the primary watch signal.

### The Pitch
**Problem:** SR 26-2 / OCC Bulletin 2026-13 replaced SR 11-7 in April 2026, requiring community banks and fintechs to govern AI/ML models, vendor LLMs, and third-party AI products. The most common 2026 examiner finding: "the bank's existing model risk policy does not reference AI/ML or foundation models at all." Examiners are now asking about AI governance during routine CAMELS exams before formal AI-specific examination procedures exist. AegisAI Compliance sells a free browser assessment and $29–99 PDF template kits — but its operational Evidence Tracker is still an email waitlist. The job of "tracking which AI systems are approved, who owns them, what validation was done, and where the board-level evidence lives" has no SaaS home for a 4-person compliance team at a community bank.

**Solution:** ModelReg maintains the AI system inventory (vendor LLMs, internal models, embedded AI in core banking), maps each to SR 26-2 obligations (validation, monitoring, vendor due diligence), tracks evidence ownership and due dates, and exports a board-ready governance summary when the exam letter arrives.

**Target customer:** Chief Risk Officer / Compliance Officer at a 50–500 person US community bank, credit union, or regulated fintech. Buyer: CRO or CEO. Users: compliance analyst + model risk officer. Annual exam creates a recurring urgency cycle.

**Why now:** SR 26-2 is live. OCC announced an AI-specific RFI. AegisAI Evidence Tracker is still waitlist-only. The community bank compliance officer who took the free AegisAI assessment has a score and a gap list but no operational tool to close those gaps.

**Why they buy without being sold to:** A compliance officer who received an AegisAI gap report with 12 open items pastes those items into ModelReg's free import, assigns owners, and sets due dates. The first exam prep report generates itself. They purchase before the 14-day trial expires.

**Revenue model:** $299/month (1 institution, AI inventory, obligation tracking, board-ready report). $499/month (3 institutions + vendor due diligence workflow). $599/month (unlimited + API + external auditor view). Annual −2 months.

**Unfair advantage:** AegisAI gap report → ModelReg import is the conversion funnel. Community bank exam cycles create a recurring urgency event. AegisAI Evidence Tracker launch is the kill signal to watch but has been "coming soon" for 4+ months.

### Solo Build Plan
1. Weeks 1–3: AI system inventory (name, type, vendor, use case, risk tier); SR 26-2 obligation library; owner + due date + evidence slot per obligation.
2. Weeks 4–5: AegisAI gap import (CSV from assessment); board report generator (SR 26-2 maturity summary).
3. Weeks 6–7: Vendor due diligence checklist per third-party AI product; exam prep export ZIP.
4. Weeks 8–9: Stripe; AegisAI gap-import onboarding; 14-day trial.
5. Weeks 10–12: Pilot 5 community banks via ABA community banking track and IBAT compliance events.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-09-04
**Strongest part:** AegisAI Evidence Tracker is the natural predecessor tool — giving ModelReg a warm-lead pipeline of institutions with a completed gap assessment and no operational tool to close the gaps.
**Open question:** AegisAI Evidence Tracker launch within 3 months?

---

## #5 — DORAIncident  ·  73/100  ·  NEW
First added: 2026-09-18 | Last updated: 2026-09-18 | Score delta this week: +73

> Never miss a DORA incident reporting clock — classified, structured, submitted in hours.

### Score Breakdown
- Solo Buildability:   14/20  (ICT incident intake + DORA classification checklist + 4h/72h/30-day clocks + authority-specific report templates; authority template library requires ongoing maintenance)
- Value Clarity:       16/20  ("your incident report is due in 68 hours" is self-explanatory to a compliance officer; "Incident Dry Run" lead magnet is immediately useful)
- Market Timing:       17/20  (DORA in force Jan 2025; first enforcement for incident reporting failures and Register deficiencies expected 2026 supervisory cycle; SREP assessments including DORA findings are underway; most EU fintech shops have no purpose-built incident tracker)
- B2B Monetisation:    15/20  ($499–1,199/month for regulated EU financial entities; compliance budget is real)
- Pull Factor:         11/20  (compliance officer communities; LinkedIn-active EU RegTech crowd; word of mouth after an incident-first demo)

**Strengths:**
- DORA enforcement signals in 2026 are specific: "incident reporting failures" and "Register of Information deficiencies" are the named targets. These are not hypothetical.
- Vanta/Drata are US-centric SOC 2 platforms that retrofitted DORA support as an add-on — authority-specific report templates (AFM, BaFin, ACPR, PRA, DNB) require EU regulatory expertise they don't have.
- "Incident Dry Run" feature (simulate a scenario against DORA criteria before a real event) is both the best product demo and the most useful free tool in the category.

**Risks:**
- Low incident frequency (3–4 major incidents/year for a payment fintech) may undercut $499/month subscription value — companies pay for insurance they rarely use.
- 27 EU member states = 27 potential competent authority formats; maintaining templates for all is a significant ongoing content burden.
- Riskonnect, AuditBoard, or MetricStream could ship a "DORA Module" in Q4 2026 with their existing enterprise relationships.

**Verdict:** Enter now, start with payment institutions and crypto-asset service providers. Narrow to the 5 most active competent authorities: AFM, BaFin, ACPR, FCA, DNB.

### The Pitch
**Problem:** Under DORA (EU Regulation 2022/2554, in force since January 17, 2025), EU financial entities must classify significant ICT incidents, send an early warning to their competent authority within 4 hours of classification, file an intermediate report within 72 hours, and submit a final report within 1 month. Supervisors have explicitly signalled that 2026 enforcement will target incident reporting failures and Register of Information deficiencies. Competent authorities are finding: late initial notifications, misclassified incidents (under-reporting is a risk), and final reports lacking adequate root cause analysis. Most payment institutions and crypto-asset service providers manage this with SharePoint folders, email chains to the compliance officer, and manual Excel trackers — tools built for annual audits, not live incident clocks on a Friday evening.

**Solution:** DORAIncident is the DORA incident reporting workbench: it classifies ICT incidents against DORA criteria (availability, authenticity, integrity, confidentiality), starts the 4h/72h/1-month clocks automatically, pre-fills the report template for the relevant competent authority (AFM, BaFin, ACPR, FCA, DNB), and routes the draft for internal approval via Slack/email. The final submission is structured, on time, and archived for SREP inspection. "Incident Dry Run" lets teams simulate a scenario against DORA criteria before a real event — the best demo is also the best preparation.

**Target customer:** EU payment institutions, e-money institutions, and crypto-asset service providers (20–200 employees). Buyer: Chief Risk Officer / Compliance Director. User: IT risk manager + compliance analyst handling the overnight incident triage. DORA-regulated, tech-native, faster procurement than banks.

**Why now:** DORA has been in force since January 2025. Supervisors explicitly announced enforcement expectations for 2026. First SREP assessments including DORA findings are underway. The first enforcement actions for reporting failures are expected before year-end. Most fintech-sized regulated entities have no purpose-built incident management tool.

**Why they buy without being sold to:** After a payment platform outage lasting 3.5 hours, the risk manager has 30 minutes to decide whether to file an early warning with the FCA. They paste the incident timeline into DORAIncident, receive a classification (major: yes), see the clock at 3h 12m remaining, and click "generate draft." The draft arrives in their inbox in 8 minutes. They purchase before the next incident.

**Revenue model:** $499/month (1 entity, unlimited incidents, 5 authority templates, evidence archive). $799/month (3 entities + Register of Information module). $1,199/month (unlimited + API + SREP evidence pack + expert template review). Annual −2 months. 14-day trial with Incident Dry Run feature (unlimited, no account required).

**Unfair advantage:** Authority-specific report templates (AFM, BaFin, ACPR, FCA, DNB) maintained by someone who reads the actual guidance — not a US-centric GRC platform retrofitting DORA as a checkbox module. The "Incident Dry Run" as a free tool creates trial demand from exactly the companies that will become paying customers after the first real incident.

### Solo Build Plan
1. Weeks 1–3: ICT incident intake form (DORA classification checklist: availability, integrity, confidentiality, authenticity affected services); 4h/72h/30-day clock automation; authority template library for AFM, BaFin, ACPR, FCA, DNB.
2. Weeks 4–5: Incident Dry Run (free, no login) — simulate scenario, get classification + clock preview; Slack/email approval routing for internal sign-off.
3. Weeks 6–7: Evidence upload per incident; SREP evidence pack export; intermediate/final report pre-fill from initial classification data.
4. Weeks 8–9: Stripe; 14-day trial with dry-run conversion flow; Register of Information basic template module.
5. Weeks 10–12: Pilot 5 EU payment institution / CASP compliance officers via EU RegTech conferences, DORA compliance forums, and FinTech EU communities.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-18
**Strongest part:** Incident Dry Run as a free tool creates the most realistic trial mechanism — users experience the product during preparation for a real incident, the exact moment they feel the pain most acutely.
**Open question:** Will low incident frequency (3–4 major incidents/year for a typical payment fintech) prevent companies from paying $499/month for a "rarely used" workflow tool — or does the regulatory penalty for a missed clock justify the subscription?

---

## #6 — ClaimSnap  ·  72/100  ·  DECLINED
First added: 2026-09-11 | Last updated: 2026-09-18 | Score delta this week: −2

> AI damage photo classification → Xactimate-format supplement brief — for public adjusters, not carrier platforms.

### Score Breakdown
- Solo Buildability:   15/20  (GPT-4V image classification + Xactimate line-item mapping + PDF brief; no Xactimate API; all output side)
- Value Clarity:       16/20  (retrospective demo on real loss photos is self-closing; public adjuster pain is acute)
- Market Timing:       14/20  (−2: XactAI now ships AI photo LABELING inside Xactimate — not photo-to-estimate generation, but it is a creeping threat; public adjuster segment remains unserved at $149/month)
- B2B Monetisation:    15/20  ($149/month for public adjusters; seasonal demand spikes justify annual plans)
- Pull Factor:         12/20  (NAPIA/TAPIA distribution; adjuster peer networks share tools that close more claims)

**Strengths:**
- XactAI (Verisk) adds AI photo descriptions and labels inside Xactimate — but this is DOCUMENTATION assistance (labeling existing photos), not photo-to-estimate generation. ClaimSnap's output (AI classifies damage type → generates Xactimate-format line items for a supplement claim) is still unaddressed by XactAI.
- Public adjuster segment (~50,000 licensed US public adjusters) has no purpose-built tool at $149/month confirmed. Verisk/Xactimate targets carriers, not independent/public adjusters.
- Seasonal demand spikes (hurricane season) create predictable high-conversion windows.

**Risks:**
- XactAI "AI Estimator" (plain-language job description → structured Xactimate estimate) is a direction Verisk is clearly moving toward — if they add photo-based line item generation, ClaimSnap is directly threatened.
- GPT-4V damage classification accuracy in edge cases (water damage vs. mold, structural vs. cosmetic) may require human-in-the-loop validation.
- Public adjuster firms vary wildly in tech adoption; many are one-person shops with no tooling budget.

**Verdict:** Still viable but XactAI's trajectory narrows the window. Accelerate or reconsider by the next quarterly run.

### The Pitch
**Problem:** Public insurance adjusters and independent adjusters preparing property damage supplement claims spend hours manually reviewing field photos, classifying damage, and translating observations into Xactimate line items. Xactimate (Verisk) has added XactAI photo labeling — but this generates text descriptions of photos for documentation, not damage classification that maps to estimate line items. The ~50,000 licensed US public adjusters and independent adjusters have no tool at $149/month that reads their field photos and produces a Xactimate-format supplement brief. Carrier platforms (CoreLogic Symbility, Hover) serve insurance companies, not the adjuster on the roof.

**Solution:** ClaimSnap accepts field damage photos via mobile upload, uses vision AI (GPT-4V / Claude Vision) to classify damage type by room and component, maps classifications to the most common Xactimate line items, and generates a formatted supplement brief PDF the adjuster can use as the basis for their claim. It does not write the final Xactimate estimate — it structures the first draft so the adjuster spends 30 minutes instead of 3 hours.

**Target customer:** Licensed public adjuster or independent adjuster at a 1–20 person firm handling residential and light commercial property claims. Buyer = user. Revenue driver: more claims closed per month, higher supplement success rate.

**Why now:** XactAI's trajectory confirms Verisk is moving toward AI-assisted estimation, but the current product assists carriers and contractors who already know what to document. The public adjuster on-site at a storm-damaged property has field photos and no structured workflow — a window that remains open in 2026.

**Why they buy without being sold to:** A public adjuster who uploaded last month's hurricane photos, ran ClaimSnap's free trial on a closed claim, and saw the AI-classified line items match 87% of what they submitted manually — that adjuster purchases and tells their NAPIA chapter.

**Revenue model:** $149/month (1 user, 20 claims/month). $249/month (3 users + firm-wide claim history). $399/month (10 users + API + custom line-item library). Annual −2 months. Free retrospective demo on 1 closed claim (no account required).

**Unfair advantage:** The retrospective demo (run AI on your last closed claim, see how many supplement line items you missed) is the strongest possible free trial — users experience an aha moment with their own real loss data before purchasing.

### Solo Build Plan
1. Weeks 1–3: Mobile photo upload; GPT-4V damage classification by room (roof, interior, structural, appliances); Xactimate line-item mapping library (top 150 residential items).
2. Weeks 4–5: Supplement brief PDF generator; room-by-room breakdown; confidence score per item.
3. Weeks 6–7: Multi-claim history; retrospective demo flow (free, no login, 1 closed claim).
4. Weeks 8–9: Stripe; NAPIA/TAPIA outreach; adjuster referral program.
5. Weeks 10–12: Pilot 8 public adjusters via NAPIA/TAPIA chapters and storm-season outreach.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-11
**Strongest part:** Retrospective demo (run AI on your last closed claim) is a self-closing mechanism. XactAI confirmed public adjuster gap — its current feature is labeling within their app, not adjuster-facing generation.
**Open question:** Is Verisk building toward a public-adjuster-facing photo-to-estimate product in the next 12 months? Monitor XactAI roadmap announcements at Verisk Xactimate user conferences.

---

## #7 — HOAEnforce  ·  72/100  ·  DECLINED
First added: 2026-09-11 | Last updated: 2026-09-18 | Score delta this week: −1

> AI photo + state-specific notice — from property walk to violation letter in 4 minutes.

### Score Breakdown
- Solo Buildability:   15/20  (mobile camera + GPT-4V violation classification + state notice template library; no full AMS required; HIPAA-equivalent not applicable)
- Value Clarity:       16/20  (property walk photo → violation notice is a workflow the manager feels every day; 4-minute demo is obvious)
- Market Timing:       14/20  (−1: CINC's Cephai+ now states it "auto-analyzes violations & drafts communications" — not confirmed as photo-based but creeping; Vantaca's HOAi does AI photo analysis for ARC review, not violation enforcement; 370,000 HOAs in US still underserved)
- B2B Monetisation:    15/20  ($199–499/month for management companies; per-community pricing possible)
- Pull Factor:         12/20  (CAI chapter distribution; property managers share tools that reduce notice-drafting time)

**Strengths:**
- Vantaca HOAi does AI photo analysis for Architectural Review Committee (ARC) requests — not routine violation detection from property walks. The specific workflow (manager walks property → takes photo → AI classifies violation → generates state-specific notice) is still unaddressed.
- CINC Cephai+ "auto-analyzes violations" is a text-and-data workflow automation, not confirmed AI photo detection from field photos.
- State legislation continues tightening: FL HB 919, CA AB 3182, TX HB 614 all increase required disclosures per notice — making state-specific templates more valuable over time.

**Risks:**
- CINC Cephai+ "auto-analyzes violations" is ambiguous — if this includes photo processing from the mobile app, the wedge narrows significantly. Watch for CINC product announcements at CAI conferences.
- Vantaca adding violation-detection to their HOAi agents (currently ARC-focused) is a clear product direction.
- Property management software is sticky — getting management companies to add another tool to the manager's phone requires a clear workflow wedge.

**Verdict:** Hold but watch CINC Cephai+ closely — one product announcement could collapse the differentiation.

### The Pitch
**Problem:** HOA property managers at management companies walk communities, photograph violations (unauthorized modifications, landscaping violations, parking infractions), return to the office, and manually draft violation notices using state-specific disclosure requirements. Florida HB 919, California AB 3182, and Texas HB 614 have all increased the required disclosures that must appear in violation notices. CINC, Vantaca, and Enumerate are full Association Management Systems with enterprise pricing — none has an AI photo-to-notice workflow for the field inspection that happens 40 times a week. Vantaca HOAi does AI photo analysis for ARC requests submitted by homeowners, not for violation detection by managers in the field.

**Solution:** HOAEnforce is the AI violation workbench: the manager opens the mobile app, photographs the violation, HOAEnforce classifies it (unauthorized structure, landscaping, vehicle), maps it to the applicable CCR rule for that community, and generates a state-compliant violation notice PDF ready to send. The manager reviews and sends in 4 minutes instead of returning to the office to draft.

**Target customer:** Property managers at 5–50 HOA management companies managing 20+ communities per manager. Buyer: management company owner / operations director. User: on-site property manager. Management companies, not self-managed HOA boards (they lack the workflow volume).

**Why now:** State legislation tightening (FL, CA, TX) makes each notice more legally complex, increasing the value of automated state-specific templates. Full AMS platforms (CINC, Vantaca) are adding AI incrementally — the field-inspection workflow is the last uncovered gap.

**Why they buy without being sold to:** A property manager who spent 45 minutes drafting violation notices after a morning walk installs HOAEnforce, photographs a parking violation, and sees the Florida-compliant draft notice ready to send in 4 minutes. They demo it to their operations director at the next team meeting.

**Revenue model:** $199/month (1 management company, unlimited communities). $349/month (3 managers + branded notices). $499/month (unlimited managers + API + AMS integration hooks). Annual −2 months. 14-day trial with 10 sample violations processed.

**Unfair advantage:** State-specific violation notice template library (FL, CA, TX, AZ, NV as initial states) updated as state legislation evolves — the legal compliance layer that no photo-processing OSS tool provides. Distribution through CAI chapter meetings where the same property managers gather monthly.

### Solo Build Plan
1. Weeks 1–3: Mobile camera interface; GPT-4V violation classification (unauthorized structure, landscaping, vehicle/parking, modification, trash/debris); CCR rule mapping per community.
2. Weeks 4–5: State-compliant notice template library (FL, CA, TX first); violation notice PDF generator with required disclosures.
3. Weeks 6–7: Violation history per community/unit; management company dashboard; bulk-notice workflow.
4. Weeks 8–9: Stripe; 10-violation free trial; CAI chapter outreach.
5. Weeks 10–12: Pilot 6 management companies via CAI chapter presentation and property management Facebook groups.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-11
**Strongest part:** State-specific notice templates updated by legislation are a compliance moat that photo-processing tools and generic AI assistants cannot replicate without domain expertise.
**Open question:** Will CINC Cephai+ add photo-based violation detection from field inspections at its next product release cycle?

---

## #8 — AuthTrack  ·  71/100  ·  IMPROVED
First added: 2026-08-16 | Last updated: 2026-09-18 | Score delta this week: +1

> See which prior auths are inside the 7-day / 72-hour clock — and which denials still have no specific reason.

### Score Breakdown
- Solo Buildability:   14/20  (CSV/fax log + calendar clocks + denial-reason fields; no EHR writeback in v1; HIPAA still applies)
- Value Clarity:       16/20  ("this PA blows the CMS clock on Thursday" is obvious to a biller)
- Market Timing:       15/20  (+1 from 14: CMS-0062-P proposed rule extends PA requirements to drugs — comment period closed June 15, 2026; if finalized, AuthTrack's addressable market expands significantly; clocks still live for non-drug PAs since Jan 2026)
- B2B Monetisation:    14/20  ($149–299/mo for a billing coordinator's time; one avoided write-off pays for a year)
- Pull Factor:         12/20  (biller Facebook groups; not public-viral)

**Strengths:**
- CMS-0062-P (proposed rule extending CMS-0057-F PA requirements to drugs) had comment period close June 15, 2026 — if finalized, AuthTrack's market expands to include drug PA tracking, a dramatically larger workflow volume.
- CMS-0057-F clocks already binding since Jan 2026: 7-day standard, 72-hour expedited, specific denial reasons required.
- Small practice fax-shop market (2–10 providers, Excel PA tracker) still has no purpose-built clock tool.

**Risks:**
- HIPAA + PHI handling from day one.
- Linear Health or clearinghouses ship a cheap tracker SKU.
- Drug PA rule (CMS-0062-P) is still proposed — finalization timeline is uncertain.

**Verdict:** Hold. Drug PA rule expansion is a significant positive signal if finalized; watch the rulemaking calendar.

### The Pitch
**Problem:** Since January 1, 2026, Medicare Advantage, Medicaid, CHIP, and FFE QHP payers must decide standard prior auths in 7 calendar days and urgent ones in 72 hours, and every denial must include a specific reason. Billing coordinators at 2–10 provider practices still track this in a spreadsheet next to the fax machine. They miss clocks, they cannot prove a vague denial, and they will need a clean log before 2027 electronic-PA attestation. CMS-0062-P proposes extending PA clock and specific-denial requirements to drugs — if finalized, the workflow burden at small practices roughly doubles.

**Solution:** AuthTrack is the PA status board: each request gets a clock, a channel (fax/portal/phone), a denial-reason field, and a reminder before the CMS window closes. v1 is CSV import + form entry — not an Athena integration, not a FHIR client.

**Target customer:** Billing coordinator / office manager at a 2–10 provider US practice (PT, specialty lite, independent primary care) not on Athena+Linear Health. Buyer: office manager. User: the biller who owns the Excel PA tab.

**Why now:** The clocks are live, not upcoming. CMS-0062-P would extend requirements to drugs — the proposed rule adds urgency to building the tool before the rule is finalized. Practices that build good habits now integrate smoothly when their payers go live with FHIR APIs in 2027.

**Why they buy without being sold to:** After a denied MRI with no specific reason and a missed 7-day follow-up, the biller pastes the spreadsheet into AuthTrack, sees two clocks already red, and stops using Excel that week.

**Revenue model:** $149/mo (1 location, 200 PAs). $249/mo (3 locations + reminder SMS). $299/mo (export pack for appeals + drug PA module when CMS-0062-P is finalized). Annual −2 months.

**Unfair advantage:** CMS-clock templates + denial-reason required field sized for fax-era shops that enterprise PA platforms ignore.

### Solo Build Plan
1. Weeks 1–3: PA log (CSV import); 7-day / 72-hour clocks; denial-reason required on deny.
2. Weeks 4–5: Email/SMS reminders; aging report; appeal packet PDF.
3. Weeks 6–7: HIPAA BAA flow; audit log; role-based access.
4. Weeks 8–9: Stripe; sample-CSV onboarding.
5. Weeks 10–12: Pilot 6 small practices via biller Facebook groups and local MGMA chapters.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** Regulation is already in force; the buyer is a person with a spreadsheet, not a health-system IT committee. Drug PA extension would significantly expand the addressable workflow.
**Open question:** Will tiny practices pay, or will they wait for their clearinghouse to add a free clock?

---

## #9 — IntegSecPack  ·  71/100  ·  NEW
First added: 2026-09-18 | Last updated: 2026-09-18 | Score delta this week: +71

> Stop losing enterprise deals to integration security reviews — generate your AI-agent compliance pack in an afternoon.

### Score Breakdown
- Solo Buildability:   14/20  (integration architecture builder + 85-question response library + dossier generator; legal validation is the constraint; no ML engineering required)
- Value Clarity:       15/20  (68% of B2B SaaS lost deals over integration security; "here is your integration security pack" is a concrete deliverable)
- Market Timing:       16/20  (agentic AI created an entirely new category of procurement questions in 2026: agent authentication, least-privilege agent scoping, audit logging for automated actions — existing trust centers like Whistic and Vanta Trust Report don't have these sections)
- B2B Monetisation:    14/20  ($149–499/month; companies have real budget for tools that close enterprise deals)
- Pull Factor:         12/20  (sales engineers share when it closes a deal; YC founder communities are highly referral-driven)

**Strengths:**
- 68% of B2B SaaS companies lost or delayed an enterprise deal due to integration-related security concerns (Ampersand 2026 State of Agentic Integrations Report). The pain is current and quantified.
- The "AI agent integration section" — covering agent authentication, least-privilege OAuth scoping, audit logging for agentic actions, and data residency for AI inference — is the 2026-specific procurement ask that Whistic, SecurityPal, and Vanta Trust Report do not yet have formalized.
- "Trial = close a pending deal" is the strongest possible free trial mechanism for a security document tool.

**Risks:**
- Direct competitors: Whistic, SecurityPal, Vanta Trust Report, Drata Trust Center — all solve the security questionnaire problem for general integrations. Whistic has 25,000+ companies sharing profiles.
- Vanta will add an "AI agent integration" section to their Trust Report within 12 months.
- Legal liability risk: if an integration description in the generated dossier is incorrect, the company may face liability when a buyer relies on it.

**Verdict:** Enter as the "AI agent integration security" specialist. Whistic/Vanta cover general integrations; this fills the 2026 agentic-specific gap that standard trust centers haven't reached yet.

### The Pitch
**Problem:** 68% of B2B SaaS companies have lost or delayed an enterprise deal because of integration-related security or compliance concerns (Ampersand 2026). Enterprise security teams reviewing AI-forward products in 2026 now ask questions that no existing security trust center covers: What OAuth scopes does your agent request? How is the agent's identity scoped and rotated? What audit log exists for actions taken by your AI agent in our systems? Where does data accessed during agent inference reside? These are the questions that a founding engineer spends 3 weeks answering by hand — often for every enterprise deal independently — because Whistic and Vanta Trust Report were designed for the 2022 integration security review, not the 2026 agentic one.

**Solution:** IntegSecPack generates a reusable AI-agent integration security dossier from a structured builder. The founder describes their integration architecture — OAuth scopes, data flows, agent identity management, audit logging, storage locations, encryption approach — through a 45-minute guided process. IntegSecPack produces a packaged dossier (PDF + JSON + hosted URL) with 85 questions answered, including a dedicated "AI Agent Integration" section covering the 2026-specific procurement asks. When the next enterprise security questionnaire arrives, 80% is pre-answered.

**Target customer:** B2B SaaS founder or VP Engineering at a 15–150 person company with 3–15 customer-facing integrations and at least one AI agent or MCP-connected workflow. Buyer: founder or VP Sales. User: founding engineer or sales engineer who currently fills security questionnaires manually. First-use trigger: a stalled enterprise deal with an open security questionnaire.

**Why now:** In 2026, every B2B SaaS adding an AI agent or MCP integration faces a new wave of security questions that 2023's standard questionnaire didn't cover. Enterprise security teams have formalized "agentic integration" as a separate review category. The Ampersand 2026 report quantifies the scale: 68% of companies have lost/delayed deals. Whistic and Vanta Trust Report have not yet shipped an AI-agent-specific template.

**Why they buy without being sold to:** A B2B SaaS founder who just lost a $120K/year deal because the buyer's security team couldn't get comfortable with their Claude agent's Salesforce integration scope runs IntegSecPack during a 14-day trial, generates their dossier, shares the hosted URL in the next deal's due diligence. The deal closes. The trial converts.

**Revenue model:** $149/month (1 integration profile, 10 questionnaire exports/month, hosted URL). $299/month (5 profiles + AI-agent section + custom branding). $499/month (unlimited + questionnaire intake parser — paste a PDF questionnaire, get pre-populated answers). Annual −2 months. 14-day trial with 1 full dossier generated.

**Unfair advantage:** First to formalize the "AI Agent Integration Security" section as a distinct questionnaire category with 2026-specific questions (agent OAuth scoping, audit logging for agentic actions, data residency for AI inference). Distribution through YC alumni, Anthropic Builder Community, and AI-forward SaaS founders who are the exact people building MCP integrations and hitting enterprise security walls.

### Solo Build Plan
1. Weeks 1–3: Integration architecture builder (OAuth scopes, data flows, agent identity, audit logging, storage, encryption); 85-question response library with SaaS integration patterns; AI Agent Integration section (20 agent-specific questions).
2. Weeks 4–5: PDF/JSON dossier generator; SOC 2/ISO 27001/CSF framework mapping; hosted shareable URL with access controls.
3. Weeks 6–7: Questionnaire intake parser (paste PDF questionnaire → AI maps to existing answers); version tracking (what changed since last quarter).
4. Weeks 8–9: Stripe; 14-day trial with 1 full dossier; onboarding flow for "I have a pending deal" use case.
5. Weeks 10–12: Pilot 6 B2B SaaS founders via YC alumni forum, Anthropic Builder Community, and Lenny's Newsletter / Cerebral Valley communities.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-09-18
**Strongest part:** The "AI Agent Integration" section is a genuine 2026-specific gap in Whistic/Vanta Trust Report — it's narrow enough to differentiate and broad enough to matter across the growing population of AI-integrated SaaS companies.
**Open question:** Can IntegSecPack differentiate from Whistic's 25,000-company head start long enough to build a network effect before Vanta ships an AI-agent-specific Trust Report section?

---

## #10 — ChurnDetect  ·  70/100  ·  UNCHANGED
First added: 2026-07-31 | Last updated: 2026-09-18 | Score delta this week: —

> Find the customers about to leave — 90 days before they tell you — from the support tickets they are already sending.

### Score Breakdown
- Solo Buildability:   15/20  (Zendesk/Intercom API + AI ticket classification + Slack alerts = 3 months feasible for a focused MVP)
- Value Clarity:       17/20  ("retrospective demo on your last churned account" is self-closing; no pitch required after that demo)
- Market Timing:       13/20  (Teravictus still live, still usage-based at $25/week, still no G2/Capterra reviews; Zendesk Intelligent Triage expanded but still ticket-level sentiment, not account-level churn)
- B2B Monetisation:    15/20  ($199–599/month; CS budget exists; protecting $30K ARR easily justifies $349/month)
- Pull Factor:         13/20  (CS AI category noise; retrospective demo still the wedge)

**Strengths:**
- Teravictus remains the main competitor — still no G2 or Capterra reviews as of September 18, 2026. $25/week base pricing, usage-based, Zendesk-only, 30-day history. ChurnDetect differentiators intact: 6-month historical, Intercom connector, account-level aggregation vs. ticket-level alerting.
- Retrospective demo (see the 8 tickets before your last churned account) remains the strongest self-closing sales mechanism in this cookbook.
- 60% of B2B software buyers regretted their purchase in 18 months (Helply 2026); churn risk in tickets is a persistent and growing signal source.

**Risks:**
- Zendesk's native "Intelligent Triage" classifies intent and sentiment per ticket — if Zendesk adds account-level churn prediction as a native feature, the differentiation narrows significantly.
- PII/SOC2 considerations for storing and scanning customer support data require explicit consent flows.
- Teravictus may receive its first G2/Capterra reviews by next quarter, increasing its perceived credibility.

**Verdict:** Hold retrospective-demo wedge. Teravictus still without public reviews; account-level differentiation intact.

### The Pitch
**Problem:** B2B SaaS companies discover customer churn risk almost exclusively at renewal time, when the decision is already made. 60% of B2B buyers regretted their purchase in the past 18 months. The warning signals — frustration in tickets, repeated unresolved issues, competitor mentions, escalating response times — are buried in the support inbox. CS teams classify tickets by "resolved / open," not by "churn risk." A $50K ARR customer silently decides to cancel three months before renewal; the first official indication is a "not renewing" email.

**Solution:** ChurnDetect connects to Zendesk or Intercom, reads the past 6 months of support tickets using AI, and classifies each conversation by churn risk language, unresolved issue patterns, feature gaps, and competitive mentions. It generates a weekly list of "accounts at risk" with the specific threads that triggered the flag.

**Target customer:** Customer success manager / VP CS at 10–150 person B2B SaaS company with 100+ customers. Buyer: VP CS or CRO. Uses Zendesk or Intercom. Does not have Gainsight or ChurnZero. Company runs $1M–15M ARR.

**Why now:** LLMs in 2026 classify "this is taking way too long to resolve" as churn risk where keyword filters miss it. The cost is under $0.001 per ticket. Enterprise CS platforms are priced at $20–30K/year, leaving the 10–150 person SaaS with no dedicated churn-detection layer.

**Why they buy without being sold to:** A CS manager who lost a $30K account to silent churn runs the free ChurnDetect retrospective on that account's last 8 tickets, sees the risk flags she missed 90 days ago, and purchases immediately.

**Revenue model:** $199/month (up to 500 accounts + Zendesk). $349/month (unlimited accounts + Intercom/Zendesk + Slack alerts). $599/month (unlimited + API + custom risk taxonomy). 14-day trial. Annual −2 months.

**Unfair advantage:** Historical retrospective demo that turns the free trial into a self-closing pitch. Vertical risk taxonomies (SaaS-specific, agency-specific) that generic sentiment tools do not have.

### Solo Build Plan
1. Weeks 1–3: Zendesk API connector; 6-month historical ticket ingestion; AI risk classification per thread.
2. Weeks 4–5: Account-level aggregation; weekly digest email + Slack; risk score per account.
3. Weeks 6–7: Intercom connector; custom risk terms; "at risk" list with flagged quotes.
4. Weeks 8–9: Stripe; retrospective demo generator; explicit data consent flow.
5. Weeks 10–12: Pilot 8 SaaS companies through CS leader Slack communities and Product Hunt launch.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** The retrospective demo on a recently churned account is a self-closing conversion mechanism unlike anything else in the cookbook.
**Open question:** Will Zendesk turn topic+sentiment into an account-health SKU in H2 2026?

---

## Removed this run
| Entry | Last score | Reason |
|-------|------------|--------|
| MCPCostMonitor | 74 → REMOVED | **MCPSpend.com** (mcpspend.com) launched live: stdio proxy wrapping MCP servers, per-tool/project/customer cost attribution, free tier 25K calls/month, Pro at $29/month. Identical product at 10× lower price. Kill signal confirmed. |
| BriefDesk | 67 → DISPLACED | Displaced from top-10 by CRAReport (77), DORAIncident (73), and IntegSecPack (71). HubSpot QBO native sync (April 2026) narrows the differentiation further. |
| MarkPack | 69 → DISPLACED | Displaced from top-10. Commission sent first RFI requests to 30+ AI companies (Sept 1, 2026) — enforcement is real, but AnnexOps/EUAgentAI/RiskWatch all live as competitors. Dec 2 marking grace ~75 days remaining. |
