# SaaS Opportunity Cookbook
Last updated: 2026-09-04 | Entries: 10/10

> Run 11 changes: TokenBill removed (Ramp free AI spend tool confirmed killed July 2026). BreakWatch removed (breakwatch.dev live product). FlowTrace removed (TrustLogix/aMaze/cascadeflow confirmed). AnnexDesk never reached file — killed by AnnexKit (€49/mo) before entry. AgentPermit never reached file — partially killed by Zapier Action Restrictions (zapier.com/govern). **RiskTier** enters as EU AI Act Annex III classification workflow — live obligation, missing Commission guidance, no self-serve tool. **ModelReg** enters from Run 10 analysis — AegisAI Evidence Tracker still waitlisted. **OffboardSafe** enters on SOC 2 CC6.2 finding trigger + AI tool credential gap. **AdvisorAlert** declines 7 points — Compliance Approved ($279/mo), Pulsio ($49/mo), Comply Vault ($299/mo) now compete directly.

---

## #1 — DentPay  ·  80/100  ·  UNCHANGED
First added: 2026-07-16 | Last updated: 2026-09-04 | Score delta this week: —

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — CSV-first rule engine; HRPayPick 2026 confirms no native plug-and-play payroll integration across OD/Dentrix/Eaglesoft simultaneously)
- Value Clarity:       18/20  (unchanged — OM ritual self-evident; production-% reconciliation gap documented and unresolved)
- Market Timing:       17/20  (unchanged — HRmonious confirmed as timekeeping-only (hours flow), NOT production-% rule engine; ScoutIQ is DSO analytics, not pay calculation; Samera still UK-only)
- B2B Monetisation:    16/20  (unchanged)
- Pull Factor:         13/20  (unchanged — study clubs; US outreach guide for discovery calls)

**Strengths:**
- HRPayPick 2026 confirms no payroll platform has native plug-and-play integration with OD, Dentrix, and Eaglesoft simultaneously; production-% reconciliation gap persists.
- HRmonious integrates timekeeping (hours) not production splits; ScoutIQ is DSO financial analytics, not a pay calculation engine. DentPay's "CSV-to-paycheck export with anomaly flags" is still unclaimed.
- Sticky once pay rules configured — wrong paycheck = employer liability; switching cost is existential.

**Risks:**
- Dental Intelligence or Dentrix itself could deepen native pay math in a platform update.
- HRmonious expanding from time-tracking to production-% reconciliation would be a direct threat.
- Relationship-heavy sales; CPA/advisor trust needed for paycheck-math credibility.

**Verdict:** Hold #1. US OD CSV-first beachhead still open; HRmonious and ScoutIQ confirmed as non-competing tools.

### The Pitch
**Problem:** US dental practices paying associates and hygienists on production still spend hours each pay period exporting Open Dental or Dentrix reports, pasting into Excel, applying lab fees, write-offs, and card-fee rules, then hoping the spreadsheet matches the contract. Open Dental's Provider Payroll report is raw material, not a pay engine. HRmonious imports timekeeping data but does not reconcile production splits. HRPayPick 2026 confirms no payroll platform has native plug-and-play integration with all three major US PMS systems for production-based pay.

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
**Strongest part:** HRmonious confirmed as timekeeping-only, not production-% engine — the US export→Excel path is fully intact.
**Open question:** Will practices trust a solo tool with paycheck math without a CPA partnership from day one?

---

## #2 — RuleFlow  ·  73/100  ·  UNCHANGED
First added: 2026-08-16 | Last updated: 2026-09-04 | Score delta this week: —

> New federal rules become a checklist and an evidence folder — not another unread PDF in Slack.

### Score Breakdown
- Solo Buildability:   13/20  (unchanged — FRTracker-class obligation feed + Asana/Jira tasks + evidence ZIP; legal-correctness review is the hard part)
- Value Clarity:       16/20  (unchanged — "this rule changed — here is what you must do by when" is a 15-second pitch for a CCO)
- Market Timing:       16/20  (unchanged — YC Fall 2026 RFS asked for AI-native compliance infrastructure; FRTracker is a free research primitive with no mid-market workflow layer; CUBE/AscentAI remain Tier-1)
- B2B Monetisation:    17/20  (unchanged — community banks and fintech lenders already pay six figures in fines and consultants; $399–799/mo is cheap next to that)
- Pull Factor:         11/20  (unchanged — compliance communities share tools quietly; not LinkedIn-viral)

**Strengths:**
- FRTracker already extracts must/shall/may-not obligations deterministically — the missing product is "new rule → owner → due date → evidence," not another AI summariser.
- YC's July 2026 request validates the category; incumbents sell libraries, not a 4-person compliance team's inbox.
- Traceable, non-black-box extraction is a selling point for auditors.

**Risks:**
- FRTracker (or a well-funded RegTech) adds the workflow layer and collapses the wedge.
- Wrong obligation mapping creates legal liability; product must be "monitoring," not advice.
- Mid-market fintech buyer count is smaller than it looks.

**Verdict:** Hold as the workflow layer on top of public obligation feeds. One vertical first: US fintech lenders / community banks.

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
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** The primitive is free and public; the unpaid job is workflow + evidence, which is exactly what a 4-person team will pay for.
**Open question:** Will FRTracker itself add "send to Jira" and eat the wedge?

---

## #3 — RiskTier  ·  73/100  ·  NEW
First added: 2026-09-04 | Last updated: 2026-09-04 | Score delta this week: +73

> Classify your AI system under EU AI Act Annex III before the market surveillance authority does — documented, signed, ready.

### Score Breakdown
- Solo Buildability:   15/20  (classification wizard + Article 6(3) derogation workflow + PDF classification record + EU database Annex VIII pre-fill = clearly solo-shippable in 3 months)
- Value Clarity:       16/20  (fines up to €15M/3% turnover for non-compliant high-risk systems; GC who needs to produce the Article 6(3) assessment on demand understands this in one sentence)
- Market Timing:       17/20  (Article 6(3) derogations due BEFORE August 2, 2026 for systems already on market; Commission missed its own guidance deadline Feb 2026; no authoritative automated tool exists; national authorities ramping up now)
- B2B Monetisation:    15/20  ($199–799/mo for a GC+CTO team at an EU-facing SaaS; annual subscription justified by guideline-change alerts)
- Pull Factor:         10/20  (EU AI Act compliance community shares tools; legal/eng intersection is a niche but vocal audience)

**Strengths:**
- The European Commission missed its legally required February 2026 guidance deadline — companies are making $15M-penalty-relevant classification decisions with no official tool.
- Annex III obligations are LIVE. Systems placed on EU market before August 2 without a classification record are already non-compliant.
- RiskTier fills the gap between checklist sites (euaiactchecklist.com, confir.eu) and enterprise GRC suites (Credo AI, Modulos at €100K+/year).

**Risks:**
- AnnexKit (€49/mo developer SDK) covers Annex III classification in the CI/CD pipeline — though it's engineering-first, not legal-workflow-first.
- Credo AI or a well-funded EU AI governance platform could bundle classification as a free feature in a broader GRC suite.
- "One-time classification event" perception makes subscription harder to justify without clear annual refresh trigger.

**Verdict:** Enter as the legal-workflow classification tool. AnnexKit is CI/CD-first; RiskTier is GC+CTO-first. Differentiate on the decision workflow, not the technical documentation.

### The Pitch
**Problem:** From August 2, 2026, every EU-facing company with an AI system touching Annex III use cases (recruitment screening, credit scoring, educational grading, biometric processing, medical device adjacent) must formally classify it under Article 6. High-risk? Full conformity assessment, Annex IV technical documentation, EU database registration, ongoing human oversight. Self-declared non-high-risk? Still requires a documented Article 6(3) derogation assessment before market placement and registration in the EU database under Article 49(2). Fines for non-compliance reach €15M or 3% of global turnover. The European Commission was legally required to publish practical classification guidance by February 2026 — and missed the deadline. Product teams are making these decisions blind, using dense regulatory text, draft law-firm memos, and informational checklist sites that produce no auditable artifact.

**Solution:** RiskTier is a structured Article 6 classification workflow for GC + CTO teams. It walks through four statutory gates — Art. 5 prohibited practice screen, Annex I product safety check, Annex III use-case matching, and Art. 6(3) derogation test — with plain-language decision prompts and source citations. At completion, it generates a Classification Record (timestamped, team-signed, versioned, auditable on demand) and pre-fills the EU AI database Annex VIII registration form. For high-risk systems, it creates a structured Annex IV documentation work plan as the engineering next step. Unlike AnnexKit's developer SDK (which decorates inference calls to generate technical documentation from CI/CD telemetry), RiskTier is the prior decision: is this system high-risk or not, and can we prove that conclusion to a market surveillance authority?

**Target customer:** GC + CTO at 15–150 person EU-facing SaaS company with a deployed AI system in a potentially Annex III use case. Buyer: GC or CTO who owns the legal-technical intersection. Users: GC, CTO, and the DPO or compliance analyst who will co-sign the classification record. Not targeting Big Four consulting clients or Fortune 500 — targeting fast-moving EU product companies with no in-house AI legal specialist.

**Why now:** Systems that were already on the EU market before August 2, 2026 needed their classification records in place before that date — companies without them are already non-compliant. National market surveillance authorities are staffing up: the EU AI Office's recruitment drive closed September 8, 2026 for 40 contractual agents including legal and technology officers. The first information requests from national authorities to Annex III system providers are expected in Q4 2026 or Q1 2027. Acting now costs one afternoon. Acting after an information request costs a law firm, remediation, and potential fine.

**Why they buy without being sold to:** A GC who reads about a competitor being asked by a national market surveillance authority to produce their Article 6(3) derogation assessment opens RiskTier's free Art. 5 prohibited-practices screen, confirms their AI system touches Annex III point 4 (education) or point 6 (credit), completes the full classification flow in 20 minutes, co-signs the record with the CTO, and exports the EU database registration prep package — all before noon. The product is used before it is evaluated.

**Revenue model:** $199/mo (1 AI system, classification record + EU database Annex VIII prep). $349/mo (3 systems + team sign-off workflow). $599/mo (unlimited + Commission guideline-change alerts + Annex IV work-plan handoff). Annual −2 months. Free: Art. 5 prohibited-practice screen (no classification record, no database registration — shows what the tool does without the auditable artifact).

**Unfair advantage:** The only guided classification workflow that produces an auditable, timestamped, team-signed Classification Record and pre-fills the EU AI database registration form — not a checklist, not a PDF template, not a CI/CD decorator. Annual subscription justified by a real recurring need: Commission guidance is expected to update as the AI Act's implementing acts are published through 2027.

### Solo Build Plan
1. Weeks 1–3: Classification wizard with 4 Article 6 gates. Plain-language decision prompts. EUR-Lex citation links for each gate. Classification Record generator (PDF + JSON export).
2. Weeks 4–5: Annex VIII data collection form. EU AI database registration pre-fill export. Team review + e-sign workflow (GC and CTO co-sign).
3. Weeks 6–7: Audit trail (who reviewed what, when, what they decided). Version history when the AI system changes scope. Annual review calendar reminder.
4. Weeks 8–9: Stripe. Free Art. 5 prohibited-practice screen as lead magnet. EU-facing SaaS onboarding with Annex III use-case lookup by industry.
5. Weeks 10–12: Pilot 6 EU-facing SaaS teams via EU AI Watch Slack, AI Act Forum, YC EU batch companies, and EU tech legal LinkedIn communities.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-09-04
**Strongest part:** Commission missed its own guidance deadline and obligations are already live — every Annex III-adjacent company is making classification decisions today with no authoritative tool and full penalty exposure.
**Open question:** Will national market surveillance authorities actually issue information requests to SMB-sized EU SaaS in the next 6–12 months, or will enforcement focus on large GPAI providers first — making the urgency perception weak for the specific 15–150 person target customer?

---

## #4 — ModelReg  ·  72/100  ·  NEW
First added: 2026-09-04 | Last updated: 2026-09-04 | Score delta this week: +72

> SR 26-2 exam-ready AI governance — live inventory, evidence folders, board report, in one afternoon.

### Score Breakdown
- Solo Buildability:   14/20  (AI model inventory + evidence folders + board-ready PDF + owner/deadline tracking = 3 months solo-feasible; HIPAA/banking data constraints are the hard part)
- Value Clarity:       17/20  (exam letter = immediate pain trigger; CRO who received an MRA understands the product in one sentence; AegisAI calculator drives self-discovered pain)
- Market Timing:       17/20  (SR 26-2 / OCC Bulletin 2026-13 issued April 2026; AegisAI Evidence Tracker still on email waitlist as of September 2026; exam-letter trigger is live)
- B2B Monetisation:    14/20  ($299–$799/mo; community banks have compliance budgets; annual contracts are the norm; $3K–$9.6K/year is far below their consulting spend)
- Pull Factor:         10/20  (banking compliance community shares tools quietly through state associations and ICBA networks; not public-viral)

**Strengths:**
- AegisAI Compliance's Evidence Tracker is STILL on a public waitlist ("Get notified when the tracker is ready") as of September 4, 2026 — their calculator drives validated demand, their SaaS product doesn't exist yet.
- SR 26-2 / OCC Bulletin 2026-13 creates exam-letter triggers for 5,000+ community banks between $100M–$5B in assets.
- The "templates-only → SaaS opportunity" pattern is airtight: AegisAI's own calculator tells banks they're exposed and then offers a $99 PDF kit — the operational gap is ModelReg's lane.

**Risks:**
- AegisAI Compliance launches their Evidence Tracker SaaS in Q4 2026 — they have the brand relationship and incoming calculator traffic.
- Ncontracts, Venminder, or Quantivate (established community bank compliance tools) add an AI governance inventory module as a feature update.
- Community bank IT procurement is slow; annual contract sales cycles require patience.

**Verdict:** Enter now while the AegisAI waitlist page drives searchers to alternatives. Build distribution through state banking associations independent of any single referral source.

### The Pitch
**Problem:** OCC Bulletin 2026-13 and SR 26-2, issued April 17, 2026, give federal bank examiners a framework for asking community banks about AI governance: which AI systems are in use, who owns them, what is the risk tier, has model validation occurred, and can the institution produce board-level evidence? Roughly 5,000 community banks between $100M and $5B in assets have AI exposure — through vendor products, employee use of ChatGPT and Microsoft Copilot, AI-enhanced core banking systems, and fraud detection models — and most cannot answer exam questions with anything more than a PDF policy and a shared spreadsheet. AegisAI Compliance's free readiness calculator (aligned to SR 26-2 and OCC Bulletin 2026-13) identifies the exact gaps and scores institutions out of 60. Their planned SaaS Evidence Tracker is explicitly described as "being built" — with a "get notified when the tracker is ready" signup as of September 2026. Ncontracts and Venminder serve vendor risk management for community banks, not AI model governance specifically.

**Solution:** ModelReg is the AI governance operating system for community banks: a live inventory where each AI use case gets an owner, a risk tier, a validation schedule, and an evidence folder. Gap workplans (imported from AegisAI calculator output or entered manually) are assigned to owners with due dates and tracked through completion by domain — vendor risk, model risk, data governance, board reporting. Board-ready summary reports are generated automatically. At exam or audit time, the institution exports a structured evidence pack: not a spreadsheet, a document an examiner can open and navigate section by section.

**Target customer:** Chief Risk Officer / Chief Compliance Officer at a $100M–$5B US community bank or credit union. Buyer: CRO or CCO who owns the AI governance gap. Users: compliance team + model risk staff. Annual contracts ($2,988–$9,600/year) aligned to community bank procurement norms. Not targeting Tier-1 banks (CUBE/AscentAI) or fintechs with dedicated GRC teams.

**Why now:** SR 26-2 / OCC Bulletin 2026-13 creates exam-letter triggers that compress remediation timelines to weeks. AegisAI's public calculator confirms and quantifies the gap — and their SaaS evidence tracker hasn't launched. The "AegisAI confirms the gap → nowhere to go for the product" acquisition path is real and live.

**Why they buy without being sold to:** A CRO scores 38/60 on the free AegisAI calculator, identifies "AI vendor inventory is incomplete" and "No board-level reporting owner" as the top gaps, clicks through to the AegisAI Evidence Tracker page, sees an email waitlist, and finds ModelReg. They import the gap list, assign three owners, set due dates, and generate a preliminary evidence workplan before the next compliance committee meeting. One afternoon. No consultant engaged.

**Revenue model:** $299/mo (1 institution, full model inventory + evidence folders + board PDF). $499/mo (3 institutions + validation schedule alerts + examiner export template). $799/mo (unlimited + AegisAI calculator import API + multi-entity rollup). Annual plans ($2,988/$4,788/$9,600/year) as the default given bank procurement cycles. 14-day trial with 3 pre-loaded model templates (ChatGPT / generative AI, core banking AI module, fraud detection model).

**Unfair advantage:** SR 26-2 / OCC Bulletin 2026-13 obligation mapping by domain — the only purpose-built tool for this specific regulatory obligation at under $10K/year. AegisAI calculator CSV output as the fastest onboarding path. Community bank distribution through ICBA, ABA, and state banking associations; the AegisAI waitlist page is a publicly visible list of potential buyers actively looking for this product.

### Solo Build Plan
1. Weeks 1–3: AI model inventory (name, vendor, owner, risk tier, purpose, status). AegisAI calculator gap-list CSV import. Evidence folder per model with document link storage.
2. Weeks 4–5: Validation schedule with email reminders. Gap status tracking (complete/partial/missing/stale). Board-ready summary PDF generator.
3. Weeks 6–7: SR 26-2 obligation mapping by domain (vendor risk, model risk, data governance, board reporting). MRA remediation workplan tracker with owner accountability.
4. Weeks 8–9: Stripe. HIPAA-appropriate data handling for community bank customers. 14-day trial with 3 model templates and sample evidence folder.
5. Weeks 10–12: Pilot 5 community banks via ICBA community bank compliance resources, ABA community banking group, and AegisAI calculator follow-through traffic.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-09-04
**Strongest part:** AegisAI Evidence Tracker is still a waitlist as of September 2026 — AegisAI's own marketing machine is validating the pain and sending buyers to a dead end.
**Open question:** Will AegisAI Compliance launch their Evidence Tracker in Q4 2026 before ModelReg can build distribution through banking associations?

---

## #5 — MarkPack  ·  71/100  ·  DECLINED
First added: 2026-08-03 | Last updated: 2026-09-04 | Score delta this week: −2

> Ship Article 50 evidence — chatbot disclosure, C2PA marks, and an audit folder — before the inspector asks.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — C2PA middleware + disclosure snippets + evidence ZIP; not a full GRC suite)
- Value Clarity:       16/20  (unchanged — AI Office complaint form is live; "show me proof" is no longer hypothetical)
- Market Timing:       16/20  (−1 — enforcement count is zero as of September 4, 2026; Dec 2 marking grace is the forcing function; EU AI Office recruitment drive shows enforcement infrastructure is still building)
- B2B Monetisation:    14/20  (unchanged — $199–499/mo for genAI product teams shipping EU-facing content)
- Pull Factor:         11/20  (−1 — enforcement silence dampens urgency signalling in compliance communities)

**Strengths:**
- The December 2 marking grace period end is a hard calendar forcing function — teams shipping AI-generated content without C2PA marks after that date have a provable violation.
- Obligation→artifact mapping + CI fail-on-missing-marks is a solo-shaped wedge vs consulting slideware.
- Post-deadline enforcement window differs from pre-deadline checklist panic.

**Risks:**
- Zero public enforcement actions as of September 4, 2026 (enforcement gap analysis confirmed by Forkast, bytevyte trackers). Enforcement silence may persist post-December.
- Platform-native C2PA (Adobe, model providers) could commoditize marking.
- Demand may cliff after Dec 2 grace if enforcement remains weak.

**Verdict:** Stay on engineering evidence pack + CI — not another PDF checklist. December 2 grace period is the sprint window; act now while the deadline is real.

### The Pitch
**Problem:** From 2 August 2026, EU AI Act Article 50 transparency duties apply. Chatbots must disclose AI interaction; generative systems need machine-readable marking (C2PA-class) — with a grace period to 2 December 2026 for systems already on the market before August 2. As of September 2026, there are zero public enforcement actions, but national market surveillance authorities are actively staffing up (EU AI Office recruitment closed September 8). Mid-market product teams have Notion checklists, not an evidence folder an auditor can open: disclosure screenshots, marking pipeline config, role owners, and change logs.

**Solution:** MarkPack is the technical compliance kit: drop-in disclosure components, C2PA/content-credential marking in the generation path, and a one-click evidence pack (ZIP/PDF) mapping each Art. 50 obligation to proof. Built for eng + legal together — not consultants selling slideware.

**Target customer:** Eng lead + counsel at 15–150 person companies shipping EU-facing chatbots or generative content (SaaS, media, agencies). Buyer: CTO/GC. Users: eng implementing marks + compliance owning the evidence folder.

**Why now:** Art. 50 obligations are live since August 2, 2026. The Dec 2 marking grace is a forcing function for teams who shipped before August without watermarks. EU AI Office shows zero enforcement but is actively recruiting enforcement staff — Q1 2027 is the realistic first-enforcement window.

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
**Rating:** 7/10 | **Last critique:** 2026-09-04
**Strongest part:** December 2, 2026 grace period end is a hard forcing function — a provable violation for anyone who hasn't marked their pre-existing system by then.
**Open question:** Will buyers pay $199+/mo after Dec 2, or was this a one-time compliance sprint purchase with no retention?

---

## #6 — BriefDesk  ·  71/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-09-04 | Score delta this week: −1

> Your Monday morning leadership brief writes itself — pulled from your real CRM, PM, and billing data, not from memory.

### Score Breakdown
- Solo Buildability:   17/20  (unchanged — 3 OAuth integrations + AI synthesis < $0.02/brief; clearly shippable solo in 3 months)
- Value Clarity:       17/20  (unchanged — CSW Solutions July 2026 documents exact pain: "4-5 hours every Friday"; self-evident ROI)
- Market Timing:       11/20  (−1 — HubSpot UNBOUND conference Sept 16–18 not yet happened; Agent Hub and HubSpot Breeze shipping; kill signal pending but not yet triggered)
- B2B Monetisation:    15/20  (unchanged — $149–$399/month; professional services teams have clear budget for time-back tools)
- Pull Factor:         11/20  (unchanged — "weekly brief" category has signal; rename still important)

**Strengths:**
- CSW Solutions (July 2026) documents the exact ritual: CRM tab → PM tab → billing tab → paste into Notion doc on Friday afternoon. Product builds itself around a lived pain.
- Multi-stack angle (HubSpot+ClickUp+QBO) is what HubSpot Breeze, Monday AI, and Notion AI individually cannot do — each only sees one platform's data.
- AI synthesis cost is < $0.02 per brief; margin structure is exceptional.

**Risks:**
- HubSpot UNBOUND (formerly INBOUND) is September 16–18, 2026. Agent Hub, HubSpot Breeze, and AI CRM synthesis features are the main themes. A "weekly cross-stack AI narrative summary" announcement at UNBOUND would trigger immediate removal.
- 3 OAuth integrations (HubSpot, ClickUp, QuickBooks) = 3 weeks of auth and rate-limit work before any AI prompt engineering.
- BriefHQ.ai, Data Parrot, and HubSpot Breeze Studio build weekly CRM recaps — differentiation must be the multi-stack narrative (not single-stack).

**Verdict:** Keep only if positioned as HubSpot+ClickUp+QBO ops brief — and rename before launch. Kill signal pending: check UNBOUND announcements September 18–19, 2026.

### The Pitch
**Problem:** Professional services firms, agencies, and B2B SaaS companies spend 4–5 hours every Friday manually pulling CRM deal updates, project status from their PM tool, and revenue figures from QuickBooks into a leadership brief. CSW Solutions documented this workflow in July 2026: "someone would export from system A, copy into the report, go to system B, copy into the report — then hope the math is right." The brief costs $200–500 in staff time to produce, arrives late, and is stale by Monday morning.

**Solution:** BriefDesk connects to your HubSpot (or Pipedrive), ClickUp (or Asana/Linear), and QuickBooks (or Xero/Stripe) via API and runs automatically every Friday at 4pm. It pulls key metrics — pipeline movement, project status by owner, revenue vs. target — and synthesises them into a readable narrative brief that arrives in Slack or email before 5pm. Reviewers annotate before it goes to leadership; the AI does the research, the human adds context.

**Target customer:** Operations lead / EA / founder at a 10–100 person professional services firm, agency, or B2B SaaS company using HubSpot or Pipedrive + ClickUp or Asana + QuickBooks or Xero. Buyer: founder/COO. User: ops lead or EA who currently builds the brief manually.

**Why now:** AI synthesis costs less than $0.02 per brief. HubSpot, ClickUp, and QuickBooks all publish REST APIs. BigIdeasDB 2026 validates manual reporting as the #1 business pain at 33.3% validation rate. CSW Solutions documented in July 2026 that SMBs are actively paying in staff hours for exactly this workflow.

**Why they buy without being sold to:** An ops manager who spent Friday afternoon copy-pasting into a leadership report gets a BriefDesk free trial, connects their HubSpot stack, and receives the same brief automatically at 5pm. They do not buy BriefDesk — they just stop cancelling it after the trial.

**Revenue model:** $149/month (1 stack: 1 CRM + 1 PM + 1 billing source; 1 brief/week). $249/month (2 stacks). $399/month (custom templates + Slack delivery + API access). Annual −2 months. 14-day trial with 2 live briefs.

**Unfair advantage:** First-mover in "narrative brief vs dashboard" for multi-stack companies. Vertical templates for agencies, SaaS, and professional services that any platform's native AI cannot match across stacks.

### Solo Build Plan
1. Weeks 1–2: HubSpot + ClickUp + QuickBooks OAuth; scheduled weekly metric pull; error handling and rate limits.
2. Weeks 3–4: AI narrative synthesis; Slack + email delivery; brief template builder.
3. Weeks 5–6: Review/annotate workflow; stale-data warnings; week-over-week comparison.
4. Weeks 7–8: Stripe; 14-day trial with 2 live briefs; onboarding wizard with vertical template selection.
5. Weeks 9–12: Pilot 8 agencies and PS firms through HubSpot Partner community + ClickUp Marketplace.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-09-04
**Strongest part:** The CSW Friday ritual is still real; multi-stack (CRM+PM+billing) narrative is still un-owned by a single platform.
**Open question:** Will HubSpot UNBOUND (September 16–18, 2026) announce a cross-stack AI narrative agent that ingests HubSpot's 1,400+ connected integrations?

---

## #7 — ChurnDetect  ·  70/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-09-04 | Score delta this week: −3

> Find the customers about to leave — 90 days before they tell you — from the support tickets they are already sending.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — Zendesk/Intercom API + AI ticket classification + Slack alerts = 3 months feasible for a focused MVP)
- Value Clarity:       17/20  (unchanged — "retrospective demo on your last churned account" is self-closing; no pitch required after that demo)
- Market Timing:       11/20  (−2 — Teravictus confirmed live at $25/week (~$108/month) with 92% accuracy claim on Zendesk+Slack; direct competitor; Zendesk Intelligent Triage rolled to Professional plans July 2026)
- B2B Monetisation:    15/20  (unchanged — $199–$599/month; CS budget exists; protecting $30K ARR justifies $349/month)
- Pull Factor:         12/20  (unchanged — retrospective demo is the wedge; CS AI category noise continues)

**Strengths:**
- Retrospective demo ("see the 8 tickets before your last churned account") is a self-closing sales mechanism that requires no pitch.
- Teravictus is Zendesk-only; ChurnDetect's multi-source (Zendesk + Intercom) and custom risk taxonomy remain differentiated.
- The gap between enterprise CS platforms ($20–30K+/year) and a $349/month self-serve tool is still large.

**Risks:**
- Teravictus is live at $25/week (~$108/month) with claimed 92% accuracy, Zendesk+Slack integration, read-only OAuth, and all Zendesk plans. Direct, active competitor.
- Zendesk's native "Intelligent Triage" rolled to Professional plans July 2026 — if it expands to account-health prediction, the differentiation narrows.
- PII/SOC 2 considerations for storing and scanning customer support data require explicit consent flows.

**Verdict:** Hold retrospective-demo wedge. Teravictus is real competition but Zendesk-only; Intercom path and custom risk taxonomy keep ChurnDetect differentiated for multi-source buyers.

### The Pitch
**Problem:** B2B SaaS companies discover customer churn risk almost exclusively at renewal time, when the decision is already made. The warning signals — frustration in tickets, repeated unresolved issues, competitor mentions, escalating response times — are buried in the support inbox. CS teams classify tickets by "resolved / open," not by "churn risk." A $50K ARR customer silently decides to cancel three months before renewal; the first official indication is a "not renewing" email.

**Solution:** ChurnDetect connects to your Zendesk or Intercom, reads the past 6 months of support tickets using AI, and classifies each conversation by churn risk language, unresolved issue patterns, feature gaps, and competitive mentions. It generates a weekly list of "accounts at risk" with the specific threads that triggered the flag. CS teams get a prioritised outreach list before accounts are lost — not after.

**Target customer:** Customer success manager / VP CS at 10–150 person B2B SaaS company with 100+ customers on Zendesk or Intercom, running $1M–15M ARR. Does not have Gainsight or ChurnZero.

**Why now:** LLMs in 2026 classify "this is taking way too long to resolve" as churn risk where keyword filters miss it. The cost of this classification is now under $0.001 per ticket. Enterprise CS platforms are priced at $20–30K/year, leaving 10–150 person SaaS with no dedicated churn-detection layer.

**Why they buy without being sold to:** A CS manager who lost a $30K account runs the free ChurnDetect retrospective on that account's last 8 tickets, sees the risk flags she missed 90 days ago, and purchases immediately.

**Revenue model:** $199/month (up to 500 accounts + Zendesk). $349/month (unlimited + Intercom/Zendesk + Slack alerts). $599/month (unlimited + API + custom risk taxonomy + competitor-mention tracking). 14-day free trial.

**Unfair advantage:** Historical retrospective demo on a recently churned account — none of the current competitors offer this as a trial conversion mechanism. Intercom connector + vertical risk taxonomies that Teravictus (Zendesk-only) doesn't have.

### Solo Build Plan
1. Weeks 1–3: Zendesk API connector; 6-month historical ticket ingestion; AI risk classification per thread.
2. Weeks 4–5: Account-level aggregation; weekly digest email + Slack; risk score per account with evidence thread links.
3. Weeks 6–7: Intercom connector; custom risk terms; "at risk" list with flagged quotes.
4. Weeks 8–9: Stripe; retrospective demo generator; explicit data consent flow.
5. Weeks 10–12: Pilot 8 SaaS companies through CS leader Slack communities and Product Hunt launch.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-04
**Strongest part:** The retrospective demo on a recently churned account remains a self-closing conversion mechanism that Teravictus and Zendesk Intelligent Triage don't offer.
**Open question:** Will Teravictus reach 50+ public G2/Capterra reviews by Q1 2027, becoming the default Zendesk churn detection choice over a newer entrant?

---

## #8 — AuthTrack  ·  70/100  ·  UNCHANGED
First added: 2026-08-16 | Last updated: 2026-09-04 | Score delta this week: —

> See which prior auths are inside the 7-day / 72-hour clock — and which denials still have no specific reason.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — CSV/fax log + calendar clocks + denial-reason fields; no EHR writeback in v1; HIPAA still applies)
- Value Clarity:       16/20  (unchanged — "this PA blows the CMS clock on Thursday" is obvious to a biller)
- Market Timing:       14/20  (unchanged — CMS-0057-F clocks live since January 1, 2026; FHIR PA API mandate January 1, 2027; compliance obligations fall on payers, not providers — but clock-tracking and denial-reason documentation is a real operational gap for small practices)
- B2B Monetisation:    14/20  (unchanged — $149–$299/mo for a billing coordinator's time; one avoided write-off pays for a year)
- Pull Factor:         12/20  (unchanged — biller Facebook groups; not public-viral)

**Strengths:**
- Operational CMS clocks are already binding; 2027 MIPS electronic PA attestation creates a documentation ramp.
- Linear Health, Waystar, CoverMyMeds, Availity serve mid-market / specialty / pharmacy — the 2–10 provider Excel tracker is still the workflow.
- Spreadsheet-first avoids the 4-week EHR integration that kills solo scope.

**Risks:**
- HIPAA + PHI handling from day one.
- Linear Health or clearinghouses ship a cheap tracker SKU.
- Tiny practices may not pay $149 if they believe "the payer has to comply, not us" — research confirms compliance obligations do sit with payers, not providers, which may weaken purchase urgency.

**Verdict:** Enter as a clock + denial-reason log for small practices still on Excel/fax. CMS-0057-F compliance sits with payers, but the operational value (tracking clocks, documenting denial reasons, building 2027 MIPS evidence) is real and provable.

### The Pitch
**Problem:** Since January 1, 2026, Medicare Advantage, Medicaid, CHIP, and QHP payers must decide standard prior auths in 7 calendar days and urgent ones in 72 hours, and every denial must include a specific reason. Billing coordinators at 2–10 provider practices still track this in a spreadsheet next to the fax machine. They miss clocks, they cannot prove a vague denial, and they will need a clean log before 2027 electronic-PA attestation.

**Solution:** AuthTrack is the PA status board: each request gets a clock, a channel (fax/portal/phone), a denial-reason field, and a reminder before the CMS window closes. v1 is CSV import + form entry — not an Athena integration, not a FHIR client.

**Target customer:** Billing coordinator / office manager at a 2–10 provider US practice (PT, specialty lite, independent primary care) not on Athena+Linear Health. Buyer: office manager. User: the biller who owns the Excel PA tab.

**Why now:** The clocks are live, not upcoming. The FHIR API mandate is January 1, 2027. Practices that do not have a denial-reason log now will invent one badly six months before MIPS attestation.

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
**Open question:** Will tiny practices pay $149/month, or will they wait for their clearinghouse to add a free clock feature?

---

## #9 — AdvisorAlert  ·  67/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-09-04 | Score delta this week: −7

> Catch solicitation language in your client emails before your next SEC deficiency — at CCO prices, not Big Four rates.

### Score Breakdown
- Solo Buildability:   12/20  (unchanged — email scanning in a regulated context; SEC API access; false-positive management; harder than a typical SaaS build)
- Value Clarity:       15/20  (−2 — Compliance Approved at $279/mo (5 users), Pulsio at $49/mo, Comply Vault at $299/mo, SmartRIA at $149/mo+ all enter market with transparent pricing; "no affordable tool exists" claim is weakened)
- Market Timing:       13/20  (−3 — Compliance Approved's email surveillance tier is at $649/mo, NOT $279/mo — the inbox-scanning gap at sub-$400/mo still exists, but multiple tools now serve the micro-RIA compliance calendar need)
- B2B Monetisation:    17/20  (unchanged — RIA compliance software market clearly paying at $279–$649/mo; Hadrius $27M raise confirms VC conviction)
- Pull Factor:         10/20  (−2 — in a more crowded compliance space, word-of-mouth advantage is smaller; Pulsio and Compliance Approved have established communities)

**Strengths:**
- Compliance Approved's transparent $279/mo pricing validates micro-RIA willingness to pay for compliance SaaS — the market exists and is paying.
- The specific inbox-scanning wedge (flagging client email testimonials/solicitations under Rule 206(4)-1) remains un-addressed at under $400/mo: Compliance Approved's email surveillance is only at the $649/mo tier.
- SEC deficiency letter trigger remains one of the strongest "no-sell" acquisition mechanisms in the cookbook.

**Risks:**
- Compliance Approved adds Gmail/Outlook inbox scanning to their $279/mo tier (currently only at $649/mo) — one feature update eliminates AdvisorAlert's price advantage.
- SmartRIA or Comply Vault could add AI email review; either has the existing RIA customer relationship.
- 1–3 person RIA TAM may be too narrow for a SaaS business; CCO-as-advisor buyer is resistant to tools that feel like self-surveillance.

**Verdict:** Hold but narrowed — the inbox-scanning at sub-$400/mo gap is real, but the market is crowding fast. Position explicitly as the email-inbox surveillance layer at the price point Compliance Approved reserves for $649/mo customers. Must differentiate or be absorbed.

### The Pitch
**Problem:** The micro-RIA CCO — typically the advisor at a 1–3 person firm — monitors client communications manually or not at all. The SEC's 2026 exam risk alert cited inadequate communication surveillance as the top deficiency for small RIAs. The compliance software market has matured: Compliance Approved now covers marketing review + compliance calendar for $279/month, and Pulsio monitors regulatory changes for $49/month. But neither scans the advisor's own Gmail or Outlook inbox for potential testimonial language, solicitation violations, or performance guarantees in client emails. Compliance Approved's email ingest and surveillance tier starts at $649/month — more than twice what a solo advisor will pay. Hadrius ($27M raise, July 2026) targets firms with hundreds of employees. The specific gap — Gmail/Outlook inbox scanning for 206(4)-1 violations at under $400/month for a 1–3 person shop — is still open.

**Solution:** AdvisorAlert connects to Gmail or Outlook (OAuth read-only), samples 50–100 client communications per month, and flags language that could constitute testimonials, performance guarantees, or solicitation violations under SEC Marketing Rule 206(4)-1. It explains each flag in plain English ("flagged because: 'always' + 'returns' in same sentence") and maintains the compliance calendar for Form ADV, custody rule filings, and code of ethics deadlines. The weekly digest is the CCO's to-do list — not a 200-page audit package, not an enterprise GRC console.

**Target customer:** Sole principal / de-facto CCO at a 1–3 person RIA with $50M–$300M AUM. The advisor IS the compliance officer. They use Pulsio ($49/mo) for regulatory monitoring and possibly Compliance Approved ($279/mo) for marketing review — but have no inbox scanning. AdvisorAlert fills the inbox-surveillance layer at $199/month, complementing rather than replacing those tools.

**Why now:** Compliance Approved's $279/mo pricing validates micro-RIA willingness to pay. Hadrius's $27M raise confirms VC conviction in the category. The SEC 2026 risk alert named email surveillance as the top deficiency. The specific inbox-scanning product at the $199/month micro-RIA price point doesn't exist. First-mover window: Compliance Approved could add this to their $279/mo tier at any quarterly release.

**Why they buy without being sold to:** An RIA who received an SEC deficiency letter for "inadequate client communication review" connects their Gmail to AdvisorAlert's free trial, sees their first flagged email (a thank-you note saying "you always grow my money") within 5 minutes, and purchases before the week is out.

**Revenue model:** $199/mo (Gmail/Outlook, 100 email samples/month, compliance calendar). $349/mo (3 inboxes + flagged-phrase library customization + Form ADV filing reminders). $599/mo (trade surveillance via Schwab/Fidelity custodian data + unlimited inboxes + Slack alerts). Annual −2 months. Free: compliance calendar only (no inbox connection) as lead magnet — more specific than Pulsio's regulatory monitoring.

**Unfair advantage:** Gmail/Outlook inbox scanning for 206(4)-1 compliance at $199/mo — cheaper than Compliance Approved's email surveillance tier by more than 50%. Distribution via Schwab Advisor Services and Fidelity Institutional partner programs where 90%+ of micro-RIAs can be reached without outbound sales.

### Solo Build Plan
1. Weeks 1–2: Free compliance calendar (ADV, custody, code of ethics deadlines) — ship as a stand-alone lead magnet with no email connection.
2. Weeks 3–4: Gmail/Outlook OAuth; email ingestion; AI flag for testimonials, performance guarantees, solicitation language with plain-English explainability.
3. Weeks 5–6: Compliance calendar integration with email alerts; marketing content review (PDF/LinkedIn post upload; plain-English flag report).
4. Weeks 7–8: Stripe; free-calendar → paid-monitoring conversion funnel; legal review of ToS positioning ("monitoring tool, not compliance advice").
5. Weeks 9–12: Pilot 5 micro-RIAs through Schwab advisor network referrals and IAA or NAPFA regional events.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-04
**Strongest part:** The inbox-scanning for 206(4)-1 violations at $199/mo is a real, specific gap — Compliance Approved's email surveillance costs $649/mo and no sub-$400 alternative exists.
**Open question:** Does SmartRIA or Comply Vault currently offer Gmail/Outlook inbox scanning in their existing product? If yes, AdvisorAlert's core wedge is already filled.

---

## #10 — OffboardSafe  ·  67/100  ·  NEW
First added: 2026-09-04 | Last updated: 2026-09-04 | Score delta this week: +67

> From SOC 2 finding CC6.2 to evidence pack in 48 hours — before the auditor calls back.

### Score Breakdown
- Solo Buildability:   12/20  (BambooHR/Workday webhook + 25 app connectors + timestamped audit log = heavy but achievable; limiting to 10 apps for MVP narrows scope to manageable)
- Value Clarity:       16/20  (SOC 2 CC6.2 "access termination documentation incomplete" is an audit finding with a named identifier; any IT lead who has received it understands the product in one sentence)
- Market Timing:       13/20  (AccessOwl, Zluri, Reco.ai, Stitchflow exist but target enterprise; AI tool API key revocation — Claude, Cursor, Copilot — is a 2026 gap no existing tool addresses; SOC 2 standard for B2B SaaS deals hardened in 2026)
- B2B Monetisation:    14/20  ($349–599/mo; SOC 2 compliance budget line is established; IT security tool purchases happen after findings, not before)
- Pull Factor:         12/20  (incident-driven; SOC 2 prep communities share tools; security-focused founder communities)

**Strengths:**
- SOC 2 CC6.2 is a named, documented audit finding — the exact trigger that drives same-week purchase decisions in IT teams.
- AI coding tool revocation connectors (Claude, Cursor, GitHub Copilot API keys) address a 2026-specific gap that legacy offboarding tools like AccessOwl don't cover — these tools run on personal API keys outside SSO.
- Ghost-account scanner as a lead magnet creates immediate self-discovery of the problem (a departed employee with 8 active accounts is a more powerful conversion than any sales pitch).

**Risks:**
- AccessOwl, Reco.ai, Zluri, and Stitchflow all address automated SaaS offboarding; the "SMB-priced" differentiation may not be sufficient if these players add transparent pricing.
- Anthropic/Claude API key revocation may not be available via a public programmatic API; GitHub PAT and Slack deactivation are confirmed available.
- Vanta or Drata (SOC 2 compliance platforms) could add an access-termination monitoring module that covers the same apps and leverages their existing customer relationship.

**Verdict:** Enter as the lightweight offboarding layer priced for 20–200 person B2B companies, with AI tool connector coverage as the 2026-specific differentiation. The SOC 2 CC6.2 finding is a precise acquisition trigger.

### The Pitch
**Problem:** When an employee leaves, IT disables their Okta account. But 89% of former employees still have active accounts in apps not federated through SSO: direct-login SaaS (Notion, Figma, Zoom), OAuth-authorized tools (Linear, Loom, Intercom), and personal API keys that are invisible to the IdP — including AI coding tools like GitHub Copilot, Cursor, and Claude that store credentials locally in environment files or tool-specific config. SOC 2 CC6.2 requires a timestamped audit trail proving every access was terminated after departure. The 2026 Verizon DBIR confirmed compromised ex-employee credentials drove 22% of breach incidents. Dedicated offboarding tools (AccessOwl, Zluri) solve this for enterprise security teams with $40K+ budgets. Sub-200 person B2B SaaS companies get a SOC 2 finding and a spreadsheet.

**Solution:** OffboardSafe connects to BambooHR or Workday termination events, fires API-based revocations across 25+ pre-built app connectors (GitHub PATs, Notion workspace removal, Slack direct-login deactivation, Figma, Zoom, Linear, Intercom, Loom, and AI tools: GitHub Copilot license release, Cursor team seat removal), and assembles a SOC 2 CC6.2-formatted audit pack with a timestamp for every revocation. For apps without API revocation, it generates a role-specific manual checklist with completion attestation — so the audit trail is complete even when full automation isn't possible.

**Target customer:** IT admin / ops lead at a 20–200 person B2B SaaS company using Okta + 20+ SaaS apps, running annual SOC 2 Type II or ISO 27001 audits. Buyer: IT lead or CTO-as-IT-admin. Users: IT admin + HR lead who initiates terminations.

**Why now:** SOC 2 Type II is now a table-stakes requirement for B2B SaaS enterprise deals. CC6.2 access termination is consistently a top-5 audit finding for sub-200 person companies — and AI coding tools introduced a new class of personal credentials that appear on no legacy offboarding checklist. The 2026 Verizon DBIR made the ex-employee credential risk explicit. Dedicated tools price at $40K+/year for enterprise teams.

**Why they buy without being sold to:** After a SOC 2 audit return identifies CC6.2 ("access termination documentation incomplete"), the IT lead opens OffboardSafe's free ghost-account scanner, runs it on the last two departed employees, finds 6 active accounts per person that weren't revoked through Okta, and purchases the automated plan before writing the auditor response email.

**Revenue model:** $349/mo (25 app connectors + HRIS auto-trigger + SOC 2 CC6.2 audit pack). $599/mo (50 connectors + custom connector builder + priority SLA). Annual −2 months. Free: ghost-account scanner (manually check one departed employee's known apps across 10 pre-built checks — shows the gap without automation).

**Unfair advantage:** GitHub PAT + Notion + Slack non-SSO + AI tool revocation in one automated sequence — the specific combination that SOC 2 CC6.2 findings demand and that enterprise tools over-engineer at 5× the price. Ghost-account scanner lead magnet creates instant self-discovery of the problem before any sales conversation.

### Solo Build Plan
1. Weeks 1–3: BambooHR + Workday webhook listener. Revocation connectors for 10 most common non-SCIM apps (GitHub PAT revocation, Notion workspace removal, Slack user deactivation, Figma, Zoom, Linear). Timestamped event log.
2. Weeks 4–5: AI tool connectors (GitHub Copilot license release via GitHub API, Cursor team seat removal, GitHub PAT revocation). SOC 2 CC6.2-formatted audit pack PDF generator.
3. Weeks 6–7: Ghost-account scanner (OAuth grant discovery for known apps for one user). Manual checklist + attestation for apps without API revocation. Slack alert to IT lead on completion.
4. Weeks 8–9: Stripe. Free ghost-account scanner as lead magnet. Onboarding with "run on your last departure" first step.
5. Weeks 10–12: Pilot 8 companies via Vanta/Drata user communities, YC community (SOC 2 is universal in YC companies), and security-focused indie hacker / founder communities.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-09-04
**Strongest part:** SOC 2 CC6.2 is a named audit finding — the precise acquisition trigger that converts a curious IT admin into a same-week buyer. Ghost-account scanner turns the free trial into a self-closing pitch.
**Open question:** Will Vanta or Drata add an "access termination automation" module that covers the same 25 apps and leverages their existing compliance-platform customer relationship before OffboardSafe reaches 100 customers?

---

## Removed this run
| Entry | Last score | Reason |
|-------|------------|--------|
| TokenBill | 72 | **Ramp** launched free AI Token Spend Management (July 16, 2026) — free standalone tier connecting directly to OpenAI/Anthropic/Cursor/Gemini admin APIs, no Ramp card required. Kill condition met. |
| BreakWatch | 67 | **breakwatch.dev** is a live product at €29/month. **FlareCanary** (free tier, MCP schema monitoring), **breaking.watch** (free 3 services, monitors 400+ vendors), **APIShift** all launched. Kill condition met. |
| FlowTrace | 62 | **TrustLogix** (enterprise kill switch + governance), **cascadeflow.ai** (commercial inside-the-loop), **aMaze** (OSS Docker/K8s), **ryanwi/agent-control-plane** (OSS Python). Cross-vendor pause market does not appear to have paying buyers. Kill condition met. |

## Near misses — did not reach file (no slot available)
| Entry | Score | Reason not added |
|-------|-------|-----------------|
| AnnexDesk | ~61 | **AnnexKit** (€49/mo, annexkit.dev) launched as a direct collaborative Annex IV documentation SaaS — SDK decorator on inference calls + PDF + trust page. "No collaborative web SaaS found" claim from Run 10 is now false. |
| AgentPermit | ~62 | **Zapier** launched granular App Access Controls + Action Restrictions at zapier.com/govern (Business/Enterprise) — action-level permissioning for 9,000+ apps including MCP-connected tools. Partial kill. Cross-vendor (non-Zapier) gap remains but market is too small to enter alone. |
