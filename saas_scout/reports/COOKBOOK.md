# SaaS Opportunity Cookbook
Last updated: 2026-11-13 | Entries: 10/10

---

## #1 — CRAReport  ·  86/100  ·  IMPROVED
First added: 2026-09-18 | Last updated: 2026-11-13 | Score delta this week: +1

> Turn the ENISA SRP web form into an auditable, multi-product reporting pipeline — before the 72-hour clock runs out.

### Score Breakdown
- Solo Buildability:   17/20  (SRP scraping + form-fill automation + deadline engine; no API means persistent UI scraping, non-trivial but solo-scoped)
- Value Clarity:       18/20  (Nov 4 SRP v1.3 upgrade confirmed: drafts visible only to the AR who created them — multi-team companies can't share draft state; "72-hour clock + nobody else can see the draft" is a 10-second pitch)
- Market Timing:       18/20  (SRP v1.3 is fourth version update in 54 days. No API at initial release; Finland CSIRT says "spring 2027" at earliest. BitHive/OSPulse/CVD Portal all say "you submit yourself." Obligation gap is widening, not closing.)
- B2B Monetisation:    18/20  ($299–$799/mo for EU software product teams; compliance lawyers already billing $400/hr for the same manual workflow)
- Pull Factor:         15/20  (CRA Art. 14 Slack communities, ENISA stakeholder working groups; legal ops teams share compliance tooling quietly)

**Strengths:**
- ENISA FAQ explicitly states no API in initial release (FAQ 15); Finland CSIRT expects one "from spring 2027." The gap is confirmed at least 6 months wide.
- SRP drafts are stored locally in individual AR accounts (confirmed in NIS-2-Templates.com guide) — multi-person companies literally cannot collaborate on a draft without a third-party layer.
- Three version updates in 54 days (v1.1 Oct 12, v1.2.1 Oct 20, v1.3 Nov 4) signal active regulatory change — schema validation tooling becomes more valuable, not less.

**Risks:**
- ENISA ships the API in Q1 2027 and closes the form-fill gap.
- A large GRC platform (Drata, Vanta, Tugboat Logic) adds CRA Art. 14 as a module with dedicated engineering.
- Schema changes in v1.4+ require rapid product updates to maintain accuracy — a continuous maintenance burden for a solo founder.

**Verdict:** Hold #1. SRP API still 6+ months away; the multi-AR draft-sharing problem is new this week and strengthens the case.

### The Pitch
**Problem:** Since 11 September 2026, EU manufacturers of products with digital elements must report actively exploited vulnerabilities to ENISA's Single Reporting Platform within 24 hours (early warning) and 72 hours (full notification), then file a final report within 14 days. SRP v1.3 launched November 4 — the fourth schema change in 54 days. The platform has no API; every notification is entered through a web form. Worse, drafts are stored locally in the individual AR's account: if the engineer who starts the early warning goes off shift, no one else on the team can open it. Mid-market software teams with multiple products and multiple ARs are building ad-hoc spreadsheet workarounds to coordinate what the platform itself cannot.

**Solution:** CRAReport monitors your registered products against ENISA's EUVD and CISA KEV feeds for newly exploited CVEs, pre-fills notification drafts (all mandatory fields, correct deadlines, correct schema version), and routes them to the right AR for review and submission. Teams see every open notification's clock status, AR owner, and submission state from one dashboard. At schema change events, CRAReport auto-validates existing drafts against the new SRP version and flags fields that changed.

**Target customer:** VP Engineering / CISO / compliance lead at a 20–300 person EU software company manufacturing products with digital elements (SaaS platforms, embedded devices, industrial software). Buyer: CISO or Legal. Users: the 2–4 engineers and legal ops staff who currently manage CRA notifications manually. Companies with 3–20 registered products benefit most — single-product companies may not need the coordination layer.

**Why now:** CRA Article 14 obligations began September 11, 2026. SRP v1.3 is the fourth version in 54 days. ENISA's own FAQ (Question 15) states explicitly: "no API will be provided at the initial release." The Finnish CSIRT publicly expects one "from spring 2027." Every week without an API is a week of compounding manual burden — and a week of compound SEO moat for the first tool that ranks for "CRA SRP automation."

**Why they buy without being sold to:** A compliance lead whose team missed the 24-hour early warning because the engineer who found the CVE at 11pm couldn't share the draft with the morning team runs a CRAReport trial, sees all open notifications with their clocks, and cancels the emergency Saturday Zoom call. The product pays for itself in the first incident.

**Revenue model:** $299/mo (1 product, 3 ARs, deadline alerts). $499/mo (5 products, 10 ARs, schema diff alerts, Slack/email escalation). $799/mo (unlimited products + SSO + evidence export ZIP per notification). Annual −2 months. 14-day trial with one live product scan and a sample notification pack.

**Unfair advantage:** CRA SRP schema diff engine (v1.0 → v1.1 → v1.2.1 → v1.3 documented; each change tested against live form fields) + first-mover SEO for "CRA Article 14 reporting" before enterprise GRC vendors wake up. The no-API gap is a forcing function that keeps this market open until at least spring 2027.

### Solo Build Plan
1. Weeks 1–3: EUVD + CISA KEV feed ingestion; product CVE monitoring; 24/72-hour clock engine; email alerts when a CVE matches a registered product.
2. Weeks 4–5: SRP form-field mapping (all mandatory fields per schema v1.3); draft pre-fill export (PDF/Word); multi-AR assignment with deadline ownership.
3. Weeks 6–7: Draft sharing and state sync (import partially-completed SRP fields from AR to AR); schema diff engine (flags changed fields between SRP versions).
4. Weeks 8–9: Stripe; evidence pack export (notification + timeline + AR log per submission).
5. Weeks 10–12: Pilot 6 EU software firms through CRA compliance Slack communities and ENISA stakeholder working group contacts.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-11-13
**Strongest part:** The multi-AR draft-sharing problem is a confirmed, documented platform limitation — not an assumed pain. The 54-day/4-version change cadence is objective evidence that the schema-diff moat compounds over time.
**Open question:** Does ENISA announce a Q1 2027 API beta between now and the end of November? If yes, the remaining window is 6–9 months; plan to reach first revenue by February.

---

## #2 — WorkAuditAI  ·  84/100  ·  IMPROVED
First added: 2026-10-09 | Last updated: 2026-11-13 | Score delta this week: +2

> Seven weeks until four California workplace AI laws take effect — your HR documentation is not ready.

### Score Breakdown
- Solo Buildability:   16/20  (questionnaire intake → policy/notice generator → evidence log; no EHR, no ATS, no payroll integration required; pure document workflow)
- Value Clarity:       18/20  (Jan 1, 2027 is 7 weeks away; "are you ready for AB 1883?" is a 15-second pitch to any CA employer using AI tools)
- Market Timing:       18/20  (EmployArmor confirmed hiring-only: ATS integration, bias audits, 17 state AI hiring laws. NOT covering AB 1883/AB 1331/SB 951/SB 947. DLA Piper + K&S published Nov 2026 advisories. No tool covers the 4-law bundle.)
- B2B Monetisation:    17/20  ($299–$799/mo vs. a $3,000 attorney advisory hour; CA employers with 50+ employees are trained to pay for compliance infrastructure)
- Pull Factor:         15/20  (employment law attorneys and HR consultants share tools when facing a compliance wave; "got a tool ready for AB 1883" is a differentiator in Nov 2026)

**Strengths:**
- EmployArmor's FAQ explicitly confirms CCPA ADMT + AI hiring scope only. Zero coverage of SB 947 (ADS disciplinary decisions), AB 1883 (neural data/emotion recognition surveillance), AB 1331 (bathroom surveillance), SB 951 (Cal-WARN AI displacement).
- King & Spalding and DLA Piper both published "four new CA laws" advisories in November 2026 — the attorney advisory market is validating demand without competing on tooling.
- SB 947 effective July 1, 2027 gives 8 more months of sales runway for the ADS documentation component even after Jan 1, 2027 urgency subsides.

**Risks:**
- ADP, Workday, or BambooHR ships a CA AI compliance module in their December 2026 release notes — instant kill condition.
- EmployArmor expands to cover the 4-law bundle (FAQ page hasn't changed in 3+ runs but it could).
- California enforcement is light in year one, reducing urgency after January 1.

**Verdict:** Urgency is at peak — 7 weeks until AB 1883, AB 1331, SB 951 effective dates. Build and sell before January 1; convert early buyers to annual contracts before Q2 enforcement ramp.

### The Pitch
**Problem:** On September 30, 2026, California's Governor signed four AI workplace laws. AB 1883 (neural data/emotion recognition surveillance, effective Jan 1, 2027), AB 1331 (bathroom surveillance restrictions, effective Jan 1, 2027), SB 951 (Cal-WARN AI displacement disclosure, effective Jan 1, 2027), and SB 947 (No Robo Bosses Act — ADS disciplinary/termination decisions with human corroboration, effective July 1, 2027). California employers using ANY AI tool for monitoring, scoring, or decision-making now face a documentation burden most haven't started. EmployArmor covers AI hiring across 17 states and 20+ cities — but its FAQ explicitly scopes to CCPA ADMT and AI hiring tools only. Zero coverage of the four new laws. DLA Piper and King & Spalding published November 2026 advisories. Law firms are billing time — their clients need a product.

**Solution:** WorkAuditAI conducts a 20-minute intake of your AI tool stack and surfaces: (1) which tools trigger AB 1883's neural/emotion recognition prohibition, (2) whether any surveillance technology violates AB 1331, (3) whether any workforce reductions linked to automation require the new SB 951 Cal-WARN disclosure, and (4) whether any disciplinary or termination decisions use ADS and therefore require human corroboration under SB 947. It then generates the required documentation: a plain-language AI tool inventory, employee notification templates, human-corroboration workflow for ADS-influenced discipline, and Cal-WARN checklist for AI displacement events. All documents are version-locked to the specific law and date — when guidance updates, the system flags which documents need re-signing.

**Target customer:** HR Director / General Counsel at a 50–2,000 employee California-based company using AI tools for scheduling, performance monitoring, hiring, or workforce management. Buyer: General Counsel or Head of HR. Users: HR ops + legal ops. Particularly urgent for companies in tech, healthcare, logistics, and retail where monitoring tools are common.

**Why now:** January 1, 2027 is 7 weeks away. AB 1883 and AB 1331 have no grace period. Any CA employer using emotion-detection software or neural data tools in the workplace is already non-compliant from January 1 without a prohibition and documentation in place. The attorney advisory market is publishing "what to do now" content — their clients are actively looking for tools to operationalize the advice.

**Why they buy without being sold to:** An HR Director who gets forwarded the DLA Piper November 2026 advisory, runs WorkAuditAI's free inventory scan on their 12 AI tools, sees that two of them (a performance monitoring platform with facial expression scoring and a scheduling tool using biometric data) may implicate AB 1883 — and books a purchase before the year-end holiday freeze. The tool turns "read this advisory" into "here are your three flagged tools and your required documentation."

**Revenue model:** $299/mo (inventory of 1–10 AI tools, documentation pack for 1 law bundle, 1 seat). $499/mo (unlimited tools, all 4 laws, 5 seats, audit trail). $799/mo (multi-entity, ADS corroboration workflow with HR approval chain, SSO). Annual −2 months. Free 10-tool inventory scan as lead magnet (shows risk exposure, withholds the documentation pack).

**Unfair advantage:** The 4-law bundle documentation pack that employment attorneys are charging $3,000/hour to produce — systematized and versioned. Distribution: employment law firms and HR consultants who need a tool to give clients, not a 200-page advisory they can't execute.

### Solo Build Plan
1. Weeks 1–2: AI tool intake questionnaire (20 questions); rule engine for AB 1883/AB 1331/SB 951/SB 947 triggers; risk exposure summary PDF.
2. Weeks 3–4: Document generator (employee notification templates, ADS corroboration workflow, Cal-WARN AI displacement checklist); version-locking to law and effective date.
3. Weeks 5–6: Dashboard (tool inventory × law × risk status); re-sign alerts when guidance updates.
4. Weeks 7–8: Stripe; free inventory scan funnel; legal review of ToS (tool is "monitoring and documentation," not "legal advice").
5. Weeks 9–12: Pilot 10 companies via employment law firm referrals (K&S/DLA Piper client networks) and HR consultant partnerships.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-11-13
**Strongest part:** EmployArmor confirmed out of scope for 3 consecutive runs. Attorney advisory market is producing demand without producing tools. 7-week urgency creates the fastest trial-to-paid conversion of any entry in the cookbook.
**Open question:** Does ADP/Workday ship a CA AI compliance module in December 2026? Watch HR tech release notes the week of Dec 10. If yes, pivot WorkAuditAI immediately to the multi-state angle (NY AI Labor Information Act + CO AI Act + TX TRAIGA).

---

## #3 — AgentDrift  ·  76/100  ·  NEW
First added: 2026-11-13 | Last updated: 2026-11-13 | Score delta this week: —

> Every AI coding agent commit is clean. After 90 days, your codebase isn't. AgentDrift shows you the slope before it becomes a rewrite.

### Score Breakdown
- Solo Buildability:   15/20  (tree-sitter AST fingerprinting + GitHub App + rolling trend engine; not trivial but well within 3-month solo scope; no ML needed)
- Value Clarity:       15/20  ("40% of AI-generated PRs diverge architecturally" is quantified and quotable; needs one chart to self-explain, but the chart is compelling)
- Market Timing:       17/20  (AI coding agent adoption peaked in 2026; EchoSift "Inadequate PR Validation" scores 83 with 8% growth; DiffCI is free/open source CLI and covers test-selection but NOT architectural coherence; no commercial product for this exact problem)
- B2B Monetisation:    14/20  ($199–$499/mo for engineering leads with explicit productivity-ROI framing; dev tools with concrete "lines of tech debt recovered" metrics command premium pricing)
- Pull Factor:         15/20  (engineering leads share "this is what AI coding is doing to our codebase" posts on X/LinkedIn; the demo — showing 90-day consistency score decay — is inherently viral)

**Strengths:**
- The problem is quantified by practitioners: Angel Kurten (October 2026) documented 40% of AI PRs diverging architecturally; DiffCI's own data shows agents "chose their own test files 928 times and ran the full suite 282 times" — the agent confidence gap is documented.
- DiffCI (free, MIT CLI) validates test-selection but explicitly does NOT address architectural coherence. The EchoSift "Inadequate PR Validation" lane (score 83, 8% growth) is the fastest-growing developer tool pain cluster right now.
- The moat is the rolling trend: single-PR consistency is DIY-able (Angel Kurten built it on a weekend); a 30-PR rolling drift window that quantifies whether the codebase is getting worse over time is a product, not a script.

**Risks:**
- CodeRabbit already does advisory code style feedback; a "consistency check" extension of its `path_instructions` could commoditize this.
- The problem is currently solved by 10x engineers who write the drift detection themselves — solo tools often lose to the fraction of teams with an opinionated senior architect.
- Target buyer (engineering leads who care about architectural coherence) is a small subset of all engineering teams.

**Verdict:** Enter as the codebase coherence trend monitor for teams using AI coding agents at scale. The "30-PR rolling window" framing — codebase health over time, not single-PR scoring — is the product moat no open-source tool has.

### The Pitch
**Problem:** AI coding agents in 2026 write correct syntax, passing tests, and green CI. What they cannot maintain is architectural coherence with the rest of the codebase. Angel Kurten (October 2026) documented that 40% of AI-generated PRs diverged in pattern when measured against AST fingerprints of the existing codebase — using different error handling strategies, import styles, async approaches, or logging conventions than the surrounding code. No single commit is "wrong." The aggregate over 90 days is a rewrite-sized problem. Traditional linters catch syntax and style; they cannot measure whether today's code uses the same architectural patterns as last month's code, let alone whether the trend is worsening.

**Solution:** AgentDrift installs as a GitHub App (or GitLab integration), fingerprints the dominant patterns of your existing codebase using AST analysis (error handling strategies, import style, async patterns, logging conventions, retry approaches), scores each new PR's consistency against that fingerprint, and plots a rolling 30-PR coherence trend. When the codebase drift score drops for three consecutive sprints, AgentDrift opens a "codebase health alert" issue with the specific patterns diverging most rapidly. It does not block merges — it shows the trend before an engineering manager asks "why does this codebase feel inconsistent?"

**Target customer:** Engineering Lead / VP Engineering / Staff Engineer at a 15–200 person company that merged AI-generated code into production weekly for 3+ months. Buyer: Engineering Lead or VPE. Users: the team leads who review AI PRs. AI-accelerated companies on Cursor, Claude Code, or GitHub Copilot where code velocity is high enough that drift is becoming visible.

**Why now:** AI coding agent adoption went from experiment to default workflow for many teams in mid-2026. The first cohort of teams running AI agents at scale for 6+ months is now hitting the coherence problem for the first time. EchoSift's "Inadequate PR Validation" cluster (score 83, 8% growth as of July 2026) is the fastest-growing developer tool pain signal in a cooling overall market. DiffCI (free MIT CLI, launched September 2026) validates test selection but explicitly scopes away from architectural coherence — leaving the category open.

**Why they buy without being sold to:** An engineering lead who has been using Claude Code for 4 months installs AgentDrift's free 30-day trial, sees that the codebase's consistency score dropped from 0.87 to 0.61 since agents started, and books an annual contract before the next sprint planning meeting. The trend chart is the pitch — no demo required.

**Revenue model:** $199/mo (1 repo, 30-PR rolling window, weekly digest). $349/mo (5 repos + Slack/Linear integration, per-PR score badge in PR title). $499/mo (unlimited repos + team-level trend dashboard + monthly coherence report PDF). Annual −2 months. Free 30-day trial on 1 repo with historical backfill on the last 90 PRs.

**Unfair advantage:** The rolling drift trend — not single-PR scoring — is the defensible product. GitHub Actions can run a one-off consistency check; they cannot show you that your codebase was 87% coherent in August and is 61% coherent in November and that the weekly rate of decline is accelerating. First mover on "AI coding governance" framed as codebase health rather than policy compliance.

### Solo Build Plan
1. Weeks 1–3: tree-sitter AST fingerprinting for 3 languages (TypeScript, Python, Go); extract dominant patterns (error handling, import style, async strategy); per-PR consistency score (0–1) against rolling baseline.
2. Weeks 4–5: GitHub App (read PR diffs, comment with score badge); 30-PR rolling trend chart; codebase health score over time (time series).
3. Weeks 6–7: Drift alert (opens GitHub issue when consistency score drops 15%+ over 3 sprints); per-pattern breakdown ("error handling diverged most this sprint").
4. Weeks 8–9: Stripe; free trial flow with historical backfill (last 90 PRs scored against current fingerprint); onboarding for AI-accelerated teams.
5. Weeks 10–12: Pilot 8 engineering teams via AI coding communities (Cursor Discord, Claude Code early access, r/MachineLearning engineering channels) and X/LinkedIn engineering lead audience.

### Critic's Assessment (Round 1 → Round 2)

**Round 1 Critique:**
- Target is too broad: "teams using AI coding agents" is every team now. Narrow to teams where agents are merging 50+ PRs/week — that's maybe 5% of teams.
- Direct competitors ignored: CodeClimate, SonarQube, CodeScene all do code health trends. Why is this different?
- Is the 40% divergence figure reproducible? Angel Kurten measured one codebase over a few months. Is this a universal number or an outlier?
- Build plan underestimates the AST parsing complexity per language. Supporting TypeScript, Python, and Go in 3 weeks is aggressive.
- Rating: 5/10

**Round 1 Refinements:**
- Narrow target: teams running AI coding agents at 50+ merged AI PRs/month. Add a free "AI PR ratio" scan to self-select the right buyers.
- Differentiation from CodeClimate/SonarQube: those tools measure code quality (complexity, duplication, test coverage). AgentDrift measures architectural consistency — do new files use the same patterns as the existing codebase? CodeClimate would score a file "A" even if it uses a completely different error handling pattern than the rest of the repo.
- Acknowledge the measurement uncertainty; position as "early signal" not "ground truth" — the trend matters more than the exact score.
- Build plan: scope to TypeScript only in Week 1-3; Python in Week 4; Go after launch.

**Round 2 Critique:**
- "Architectural consistency" is still abstract to a time-pressed VPE. What is the concrete 30-second ROI?
- The 30-PR window is arbitrary. Why 30? What if a team merges 200 PRs/month?
- Pricing: $199-$499/mo may be too low to get engineering leads to care about procurement; too high to get individual engineers to pay personally. The buyer-user split needs clarity.
- Is AgentDrift defensible once CodeRabbit adds "consistency trends" as a feature at $24/mo?
- Rating: 7/10

**Round 2 Refinements (Final Pitch):**
- Reframe the ROI as: "AgentDrift prevented the 3-month rewrite that would have cost $200K in engineering time."
- Window is configurable (30/50/100 PRs); default 30 is a starting point.
- Pricing is per-organization, not per-seat — the VPE buys it, engineers use it.
- CodeRabbit differentiation: they flag per-PR style issues (advisory). AgentDrift shows the codebase-level trend — a fundamentally different product scope.

**Final Rating:** 7/10 | **Last critique:** 2026-11-13
**Strongest part:** The rolling trend chart is a genuinely new product in a confirmed EchoSift pain lane with 8% growth. DiffCI explicitly scopes away from architectural coherence, leaving the product category open.
**Open question:** Is the problem self-solving once engineering teams establish `AGENTS.md` / `.cursorrules` files with explicit architectural constraints? Monitor whether Cursor/Claude Code ships a "codebase rule enforcement" feature in Q1 2027.

---

## #4 — DentPay  ·  70/100  ·  DECLINED
First added: 2026-07-16 | Last updated: 2026-11-13 | Score delta this week: −6

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — CSV-first rule engine; WageTime shows it's buildable)
- Value Clarity:       16/20  (unchanged — OM ritual self-evident; but WageTime demo showing exact same Nguyen/Morales examples weakens differentiation story)
- Market Timing:       13/20  (−4 — WageTime (wagetime.com) has production splits as payroll earning codes + Dental Canvas + Dentolize; Gusto Medical Edition now listed for dental production splits; market is filling)
- B2B Monetisation:    15/20  (unchanged — dental practices still pay for time-saving tools)
- Pull Factor:         10/20  (−3 — with WageTime, Dental Canvas, Dentolize now discoverable, study-club word-of-mouth faces more noise)

**Strengths:**
- DentPay's anomaly detection (flags when OD-reported labs differ from actual invoice; flags when write-off deductions exceed contract cap) is not replicated by WageTime's earning-code model — WageTime runs the percentage but does not catch per-pay-period contract violations.
- dentpay.tech is live with the exact product vision, showing the OD/Dentrix CSV import and anomaly flagging workflow.
- The sticky onboarding (pay rules configured once; wrong paycheck = liability; switching cost is existential for the OM who owns the workflow) still holds.

**Risks:**
- WageTime (wagetime.com) explicitly shows Dr. Nguyen production percentage calculation — same use case. WageTime is built as a payroll system, not an auditor, but as it matures it will add anomaly detection.
- Dental Intelligence (OD/Dentrix/Eaglesoft native) could deepen pay math with a platform update.
- Dentolize (dentolize.com) calculates commissions from treatments and payments already in the system — no CSV export needed.

**Verdict:** Defend the anomaly-detection moat. The USP is no longer "it calculates production pay" (WageTime/Dentolize do this). The USP must be "it catches the lab mismatch and write-off cap error before the check clears." Rewrite positioning around the Friday morning anomaly report.

### The Pitch
**Problem:** US dental practices paying associates and hygienists on production spend hours each pay period exporting Open Dental or Dentrix reports, applying lab fees and write-off rules in Excel, and hoping the spreadsheet matches the contract. WageTime (wagetime.com) now handles production splits as earning codes inside payroll. But the percentage is only half the problem. The other half: the actual lab invoice ($3,100) doesn't match what Open Dental reported ($2,650). The contract caps write-off deductions at $200, but the formula deducted all $480. These errors — invisible in any payroll system that trusts the production export — are the ones that generate Friday night texts from associates and Sunday morning liability reviews.

**Solution:** DentPay imports OD/Dentrix production exports, applies per-provider pay rules, and then flags anomalies before export: lab invoices that don't match OD-reported labs, write-off deductions that exceed contract caps, missing lab allocations for cases marked closed. Office managers see three clean pay calculations and two red flags — not a rebuilt formula, not a payroll dispute.

**Target customer:** Office manager / owner at a 1–3 location US dental practice on Open Dental or Dentrix with associates or hygienists on production splits. Buyer and User: the office manager who owns both the Excel and the Friday payroll ritual.

**Why now:** WageTime and Dental Canvas prove the category is real and gaining awareness. The gap WageTime leaves is the per-contract anomaly check — the difference between "ran the percentage" and "caught the lab mismatch." DentPay owns that gap; it must own it loudly.

**Why they buy without being sold to:** An OM who spent Sunday resolving a hygienist underpay because write-off caps were applied wrong uploads last month's OD export, sees the same total with two flagged contract violations, and refuses to go back to Excel. The retrospective check on a previous payroll dispute is the demo.

**Revenue model:** $149 / $249 / $399 per practice per month. 30-day trial. CPA/dental consultant referral 15%.

**Unfair advantage:** Per-contract anomaly detection (lab mismatch, write-off cap, missing allocation) built from real OD/Dentrix export patterns — the edge case library that takes WageTime years to replicate. Study-club distribution and CPA referral channels where enterprise payroll vendors don't compete.

### Solo Build Plan
1. Weeks 1–3: OD Provider Payroll CSV ingest; pay rule engine; anomaly detection (lab mismatch, write-off cap, missing allocation).
2. Weeks 4–5: Anomaly report (flagged items vs. prior period); Gusto CSV export.
3. Weeks 6–7: Dentrix path; multi-provider approval workflow.
4. Weeks 8–9: Stripe; sample-file onboarding showing a real mismatch catch.
5. Weeks 10–12: Pilot 8 practices via OD user groups and CPA referrals.

### Critic's Assessment (Round 1 → Round 2)

**Round 1 Critique:**
- WageTime shows literally the Dr. Nguyen example from DentPay's own marketing — this is not a differentiation, this is the same demo. The anomaly detection must be the lead, not a footnote.
- dentpay.tech exists — is DentPay competing with its own idea, or is it the same company? Confusion risk in the market.
- CPA partnership trust is still the unresolved go-to-market barrier: who is guaranteeing the math?
- Rating: 5/10

**Round 1 Refinements:**
- Lead with the anomaly detection, not the percentage calculation. "WageTime runs the math. DentPay catches the mismatch."
- dentpay.tech is the product — the cookbook entry IS dentpay.tech (solo founder's current build).
- CPA partnership: build a "CPA verification badge" into the product — CPA countersigns the anomaly report. Turns the trust problem into a feature.

**Round 2 Critique:**
- The anomaly detection moat is thin unless you can prove WageTime won't add it in 6 months as a "contract verification" feature.
- The market is now 4+ tools (WageTime, Dental Canvas, Dentolize, dentpay.tech) — the "no good software exists" premise is weakening.
- $149-$399/month: is a 1–3 location dental practice the right buyer size? They might buy dentpay.tech or WageTime before they buy both.
- Rating: 6/10

**Round 2 Refinements (Final):**
- Position DentPay as the QA layer on top of WageTime/Dentolize: "run your payroll engine of choice; run DentPay's anomaly check before you export." Makes it complementary, not competing.
- Narrow target to 2–5 location practices (more complex, more anomaly surface area).

**Final Rating:** 6/10 | **Last critique:** 2026-11-13
**Strongest part:** The anomaly detection use case (lab mismatch, write-off cap) is not replicated by earning-code payroll systems. It is a real, documented production failure mode.
**Open question:** Will WageTime add a "contract verification" or "anomaly check" module as it matures? Watch their changelog. If yes, DentPay must pivot to dental-specific analytics (producer scorecards, case-mix analysis) to find its next moat.

---

## #5 — IntegWatch  ·  70/100  ·  DECLINED
First added: 2026-10-16 | Last updated: 2026-11-13 | Score delta this week: −2

> Know when a customer's integration is silently failing — before they file a ticket.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — changelog crawlers + API health polling + per-customer alert routing is a focused solo build)
- Value Clarity:       16/20  (unchanged — "your integration broke at 2am for one customer and you found out at 9am via Zendesk" is obvious pain)
- Market Timing:       14/20  (−2 — Nango now has request-level logs per connection with OpenTelemetry export; Merge has automated issue detection; Ampersand has typed per-customer connection events. Kill condition IS met for teams using unified API platforms. Remaining gap: teams with custom-built integrations not using Nango/Merge/Ampersand.)
- B2B Monetisation:    14/20  (unchanged — integration engineering budget exists; "one customer churning from a silent integration failure" is an easy ROI story)
- Pull Factor:         11/20  (unchanged — integration engineers share outage post-mortems; word-of-mouth is real but quiet)

**Strengths:**
- Ampersand, Nango, and Merge now serve the per-customer integration health use case for teams using unified API platforms. IntegWatch's thesis narrows to custom-built integrations — but this is a large segment: Prismatic's 2026 survey shows 60%+ of B2B SaaS companies build their own integrations.
- The "one customer's connection failed silently" problem is confirmed by Ampersand's own blog (Oct 2026): "Agents deployed as isolated projects can lead to agent sprawl, with duplicated connections, inconsistent security, and no central view."
- IntegWatch's wedge for custom integrations is durable: Nango/Merge/Ampersand require adopting their platform; IntegWatch works on top of whatever the team already built.

**Risks:**
- Kill condition now met for teams using Nango/Merge/Ampersand (all three have per-customer connection health). TAM shrinks to custom-integration shops only.
- If Nango reaches 50%+ market share in unified APIs, the remaining custom-integration market may be too small.
- Prismatic (integration platform provider) could ship a monitoring layer for custom-built connectors at lower cost.

**Verdict:** Hold. The custom-integration market is confirmed large (60%+ build their own). Position explicitly against "already on Nango/Merge" to avoid overlap — IntegWatch's value prop is "works on whatever you built," not "works with our platform."

### The Pitch
**Problem:** B2B SaaS companies running custom-built integrations (not Nango, not Merge, not Apideck) discover broken customer connections when customers file tickets. Ampersand's 2026 integration report confirms: without per-customer observability, a healthy service can hide a stale or failed sync for one account. Prismatic's 2026 survey shows 60%+ of B2B SaaS still build their own connectors — their teams hit the "engineering load shifts to 80% integrations" tipping point and still have no alerting layer. The unified API platforms solve this for new integrations; IntegWatch solves it for the integrations already in production.

**Solution:** IntegWatch monitors per-customer integration health using lightweight instrumentation (SDK or webhook) added to existing connectors. When a customer's sync hasn't completed in its expected window, when an OAuth token refresh silently fails, or when an API endpoint's response time spikes, IntegWatch opens a Slack alert with the customer name, connector type, last-known-good timestamp, and suggested recovery action. No re-architecture required — it wraps what you already built.

**Target customer:** Engineering lead / founder at a 10–100 person B2B SaaS company with 5–20 customer-facing integrations built in-house. Buyer: CTO or Head of Engineering. Users: the integration on-call engineer and customer success team. Company does NOT use Nango/Merge/Ampersand — their integrations predate the unified-API era.

**Why now:** The first wave of B2B SaaS built their integrations in 2020–2023 without observability. Those integrations are now 3–5 years old, handling production traffic, and failing silently for customers. The per-customer observability tooling (Nango, Ampersand) arrived in 2025–2026 for new integrations. The gap is the brownfield estate.

**Why they buy without being sold to:** An integration engineer who spent a Monday morning finding a customer's Salesforce sync had been failing for 72 hours adds IntegWatch's SDK wrapper to their connector, sees the first per-customer health timeline, and realizes they have 3 other customers with stale syncs they didn't know about.

**Revenue model:** $199/mo (10 connectors, 100 customers). $349/mo (50 connectors, 500 customers + on-call escalation routing). $599/mo (unlimited + API + SOC 2 audit log). Annual −2 months. Free tier: 1 connector, 10 customers, forever.

**Unfair advantage:** Works on custom-built connectors the unified-API platforms can't retrofit. The first SDK wrapper for brownfield integrations is a category moat — not because it's hard to replicate, but because no funded team is targeting the brownfield segment.

### Solo Build Plan
1. Weeks 1–3: SDK wrapper for Node.js/Python connectors; heartbeat ping + sync completion event; per-customer health timeline.
2. Weeks 4–5: OAuth token refresh monitoring (tracks last-refresh, alert on silent failure); Slack alert with customer identity and recovery suggestion.
3. Weeks 6–7: Dashboard (per-customer connection health heatmap; aging syncs); alert configuration per connector type.
4. Weeks 8–9: Stripe; "wrap your first connector in 10 minutes" onboarding.
5. Weeks 10–12: Pilot 6 B2B SaaS teams via integration-engineering communities (Prismatic's Slack, r/SaaS, indie-hacker channels).

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-11-13
**Strongest part:** Nango/Merge/Ampersand confirm the category by launching their own observability — but they require platform adoption. IntegWatch is for teams that won't re-architect.
**Open question:** Does Nango ship a "monitoring only" tier (no platform adoption required) that wraps custom connectors? If yes, IntegWatch's moat collapses. Monitor Nango's changelog monthly.

---

## #6 — FieldSyncQBO  ·  68/100  ·  DECLINED
First added: 2026-11-06 | Last updated: 2026-11-13 | Score delta this week: −10

> ServiceTitan teams hit the same closed-month QBO wall every month — and the workaround takes a QBO admin, a reopened period, and a bookkeeper on the phone.

### Score Breakdown
- Solo Buildability:   15/20  (ServiceTitan API + QBO API + exception detection engine; ST has a documented API; more complex than a simple CSV importer)
- Value Clarity:       14/20  (−2 — Jobber's native QBO integration now rolling out; must reframe around ServiceTitan specifically; "ST closed-month block" is specific but requires setup explanation)
- Market Timing:       12/20  (−4 — Jobber's native QBO sync launched Oct 29, 2026 for Jobber Payments payout reconciliation — 4 of the 8 original GripeVote complaints were Jobber-specific. Remaining ServiceTitan-specific pain is real but TAM is narrower.)
- B2B Monetisation:    14/20  (unchanged — ServiceTitan customers are larger field service companies; willing to pay $200-500/mo for accounting pain relief)
- Pull Factor:         13/20  (unchanged — bookkeeper Facebook groups and ServiceTitan community)

**Strengths:**
- ServiceTitan's own help documentation confirms the closed-month block is structural: "if the accounting period is closed, any additional exports will be blocked and ServiceTitan will display an error message." The workaround (reopen QBO period, re-export, re-close) is documented and tedious.
- ServiceTitan customers tend to be larger (10–50+ technician shops) with more sophisticated accounting needs — they pay more and have higher switching stakes than Jobber shops.
- The exception-handling problem (account-name mismatches blocking exports, duplicate transaction errors) is documented across ServiceTitan Capterra reviews.

**Risks:**
- Jobber's native integration rollout (Oct 29, 2026) addressed the core Jobber → QBO reconciliation pain from GripeVote. FieldSyncQBO's most cited evidence is now partially invalidated.
- ServiceTitan has significantly more engineering resources than Jobber — it could ship a native QBO closed-month correction flow faster.
- The remaining market (ServiceTitan shops with active QBO closed-month errors) may be small enough that $200-500/mo doesn't justify solo development investment.

**Verdict:** Reframe from "field service → QBO reconciliation" to "ServiceTitan QBO exception handler." TAM is narrower but the buyer is more sophisticated and the problem is structurally confirmed in ST's own docs. Validate TAM before building.

### The Pitch
**Problem:** ServiceTitan shops that close their QuickBooks accounting period on the 28th of each month (ServiceTitan's own recommended schedule) routinely hit a wall: an export from ServiceTitan fails with error 6200 "Account Period Closed." The fix requires a QBO admin to reopen the period, re-export the batch, then re-close — a multi-step process that interrupts the bookkeeper's close workflow. Separately, account-name mismatches between ServiceTitan customers and QBO customers silently block export batches, requiring manual reconciliation. ServiceTitan's help docs document both problems with multi-step workarounds. Bookkeepers who run monthly closes for multiple ServiceTitan clients handle this every month.

**Solution:** FieldSyncQBO monitors ServiceTitan export batches, pre-validates account-name matches against the QBO chart of accounts before the export runs, detects pending transactions in closed periods and routes them through period-override requests with the minimum necessary permissions, and flags the exception to the bookkeeper with the specific fix required. Bookkeepers configure their ServiceTitan + QBO connections once; FieldSyncQBO manages the exception surface they currently handle manually.

**Target customer:** Bookkeeper / controller at a ServiceTitan field service company (HVAC, plumbing, electrical) with 10–50 technicians, closing books monthly. Particularly valuable for bookkeeping firms managing multiple ServiceTitan clients simultaneously. Buyer: the bookkeeper or controller. User: same person.

**Why now:** Jobber has just launched its native QBO sync (October 2026) — confirming that field service → QBO reconciliation is a category worth solving. But Jobber is not ServiceTitan. ServiceTitan's customer base is larger and more sophisticated; the closed-month exception problem is documented in their own help center and Capterra reviews. The validation from Jobber's decision to invest in this problem is signal, not competition.

**Why they buy without being sold to:** A bookkeeper who handles 5 ServiceTitan clients and spends the last week of every month reopening QBO periods and fixing account-name mismatches sets up FieldSyncQBO's pre-validation for one client, runs the close with zero errors, and signs up for all five clients before the next month-end.

**Revenue model:** $199/mo per ServiceTitan connection. $349/mo (3 connections + multi-client dashboard). $599/mo (unlimited connections + bookkeeping firm white-label). Annual −2 months. Free 1-month trial on 1 connection.

**Unfair advantage:** ServiceTitan API exception patterns documented from real production errors; bookkeeping firm distribution (one firm manages 10+ ST clients = 10 monthly subscriptions from one sales call).

### Solo Build Plan
1. Weeks 1–3: ServiceTitan API connection; QBO API connection; account-name mismatch pre-validator; export batch status monitor.
2. Weeks 4–5: Closed-month detection (flags transactions destined for a closed QBO period before export runs); bookkeeper exception dashboard.
3. Weeks 6–7: Period-override workflow (minimum-permission QBO request for specific transaction correction); audit trail per correction.
4. Weeks 8–9: Stripe; bookkeeping firm multi-client dashboard.
5. Weeks 10–12: Pilot 5 bookkeeping firms through ServiceTitan community and bookkeeper Facebook groups.

### Critic's Assessment (Round 1 → Round 2)

**Round 1 Critique:**
- The GripeVote evidence that launched this entry was largely Jobber-specific (4 of 8 complaints). ServiceTitan has fewer validated public complaints — the evidence base is now thinner.
- TAM is genuinely narrow: how many bookkeepers serve ServiceTitan-specifically? ST is not Jobber; it's larger companies.
- The solo buildability concern: ST API has rate limits and authentication complexity that could eat 2 of the 3 months.
- Rating: 5/10

**Round 1 Refinements:**
- Acknowledge that the Jobber component is now addressed natively. Reframe around ServiceTitan explicitly.
- TAM validation step added to build plan (Week 1-2: validate with 10 bookkeeper interviews before writing code).
- Narrow build scope to exception detection only (not automated fix) in v1.

**Round 2 Critique:**
- The "exception detection" value prop requires the bookkeeper to still manually fix the exception — FieldSyncQBO catches it earlier but doesn't remove the manual work. What is the actual time saved?
- ServiceTitan customers tend to be larger companies with dedicated finance staff who may already have workarounds.
- Rating: 6/10

**Round 2 Refinements (Final):**
- Position as a "pre-flight check" that eliminates the error before the bookkeeper starts the close — saves 45–90 minutes per monthly close per client. Quantify this in onboarding.
- Target bookkeeping firms (not individual practices) as the primary buyer — one firm paying for 10 ST client connections is the right unit economics.

**Final Rating:** 6/10 | **Last critique:** 2026-11-13
**Strongest part:** ServiceTitan's own help documentation confirms the closed-month block is structural — this is a platform limitation, not a user error.
**Open question:** Does ServiceTitan ship a "smart export" that handles closed-period exceptions natively? Monitor ST product update announcements in December 2026.

---

## #7 — DocParity  ·  65/100  ·  DECLINED
First added: 2026-11-06 | Last updated: 2026-11-13 | Score delta this week: −6

> Block the merge when code changed but the docs didn't — the check CodeRabbit can suggest but can't enforce.

### Score Breakdown
- Solo Buildability:   15/20  (GitHub App + path-filter engine + namespace policy config; straightforward solo build)
- Value Clarity:       14/20  (−2 — CodeRabbit path_instructions can flag docs drift advisory; multiple repos already have DIY docs-drift CI workflows; the differentiation is "blocking" vs "advisory," which requires more explanation)
- Market Timing:       13/20  (−3 — CodeRabbit path_instructions and DIY GitHub Actions workflows (sydlexius/stillwater and bmad-code-org/BMAD-METHOD, both merged March-April 2026) confirm the detection problem is solved. The remaining gap is ENFORCEMENT — blocking the merge. This is a smaller, more specific need.)
- B2B Monetisation:    13/20  (−2 — $24/mo CodeRabbit Pro gives advisory drift detection; DocParity must justify $100-300/mo for the enforcement layer. Buyer is now a team lead or DevEx engineer, not a VP.)
- Pull Factor:         10/20  (unchanged — developer tools with blocking enforcement are shared through engineering team forums)

**Strengths:**
- CodeRabbit's path_instructions are advisory only ("flag documentation under docs/ that may need updating"). The CI workflow in sydlexius/stillwater explicitly labels itself "MUST NOT be added as a required status check; it is informational by design." DocParity's blocking enforcement remains unserved.
- EchoSift "Inefficient PR Review for Mixed Changes" (score 114, volume 34, growing 6%) remains the highest-scored developer tool pain cluster — the category is validated.
- DocParity's GitHub App approach enables namespace-level policy (define which code namespaces must have corresponding docs namespaces) that YAML path_instructions cannot replicate.

**Risks:**
- CodeRabbit adds a "custom checks" (pass/fail enforcement) mode that extends path_instructions into blocking behavior — their docs already mention "Custom checks — pass/fail conditions you define."
- The EchoSift pain cluster is specifically about reviewing MIXED PRs (code + docs in one PR), not about enforcing docs updates. DocParity may be solving the adjacent problem, not the primary pain.
- Teams that want enforcement can configure their own required GitHub Action — the marginal buyer who needs DocParity specifically is narrower than assumed.

**Verdict:** Defend the enforcement gap. The DIY solutions are advisory by design. DocParity's blocking enforcement with per-namespace policy is a distinct product. Must launch before CodeRabbit custom checks become blocking.

### The Pitch
**Problem:** CodeRabbit (March 2026) can flag when code changes without docs updates — but only as an advisory comment. The existing CI workflow patterns (paths-filter + "docs: not-required" label) are advisory by design. The team merges the PR anyway. EchoSift's highest-scoring developer pain cluster (score 114, 34 open complaints, 6% growth) is the "Inefficient PR Review for Mixed Changes" — the seam between code review and documentation tooling where every reviewer on both sides decides the gap is the other team's problem.

**Solution:** DocParity is a GitHub App that enforces docs-code parity as a BLOCKING required status check. Configure per-namespace policy (this code path → that docs path, required to change together). When a PR modifies `src/api/**` without touching `docs/api/**`, the check fails and the PR cannot merge until docs are updated or a maintainer explicitly waives the check. No advisory comment — a red ✗ in the merge status panel.

**Target customer:** Engineering lead / DevEx engineer at a 10–200 person software company with an active docs site and a recurring "docs are always stale" complaint in retrospectives. Buyer: Engineering Lead. User: every engineer who submits PRs. The trigger is "we keep merging PRs without updating docs and it breaks onboarding."

**Why now:** CodeRabbit path_instructions (March 2026) validated the docs-drift detection category but explicitly do not block merges. The DIY workflows in public repos confirm demand for detection — and explicitly label themselves non-blocking. The enforcement gap is the product gap.

**Why they buy without being sold to:** An engineering lead who spent a sprint on docs recovery because six consecutive PRs shipped without updating the API reference installs DocParity, configures the `src/api → docs/api` policy, and watches the first six PRs fail the check. No more docs debt from that namespace. The first passing PR proves the product works.

**Revenue model:** $99/mo (1 repo, 5 namespace policies). $199/mo (5 repos, unlimited policies + waiver audit log). $399/mo (unlimited repos + SSO + team-level compliance reports). Annual −2 months. Free for open-source repos. 14-day trial.

**Unfair advantage:** Blocking enforcement with namespace-level policy configuration that YAML advisory configs cannot replicate. First mover on "docs enforcement" before CodeRabbit custom checks exit beta.

### Solo Build Plan
1. Weeks 1–3: GitHub App; path-filter engine (glob-based namespace pairs); required status check integration.
2. Weeks 4–5: Namespace policy config UI; waiver workflow (maintainer overrides with reason logged); PR comment explaining what docs path was expected.
3. Weeks 6–7: Multi-repo support; waiver audit log; weekly compliance digest (how many waivers granted, which namespaces triggered most).
4. Weeks 8–9: Stripe; free open-source tier; onboarding wizard for first namespace policy.
5. Weeks 10–12: Pilot 6 companies via developer tools communities and GitHub Marketplace.

### Critic's Assessment (Round 1 → Round 2)

**Round 1 Critique:**
- CodeRabbit already says "Custom checks — pass/fail conditions you define." This is a potential kill condition already in CodeRabbit's roadmap. DocParity's remaining window may be very short.
- "Blocking enforcement" is a religious debate in engineering teams — many teams prefer advisory to avoid gate fatigue. Is the market for blocking enforcement really large enough?
- The build plan is straightforward; the market is the risk. Not the build.
- Rating: 6/10

**Round 1 Refinements:**
- Accept that blocking enforcement has a divisive audience. Target specifically teams that have already TRIED advisory and failed — "you've used CodeRabbit's path instructions for 2 months and docs are still stale."
- Waiver workflow with audit log is essential — teams need an escape valve or they disable the check.

**Round 2 Critique:**
- If CodeRabbit custom checks go blocking, DocParity's differentiation is gone overnight. This is a timing risk, not a business moat.
- EchoSift pain score 114 is specifically about "mixed changes" (code + docs in one PR) being hard to REVIEW — that's different from the enforcement problem DocParity solves.
- Rating: 6/10

**Round 2 Refinements (Final):**
- Note that the EchoSift signal and the DocParity product are adjacent but distinct. DocParity's core user is not "someone who finds mixed PRs hard to review" but "an engineering team that wants to prevent mixed PRs from shipping without docs coverage."
- The two problems reinforce each other: enforce parity → fewer mixed PRs → easier reviews.

**Final Rating:** 6/10 | **Last critique:** 2026-11-13
**Strongest part:** The existing DIY workflows explicitly label themselves non-blocking ("MUST NOT be added as a required status check") — this is a confirmed market decision, not an oversight.
**Open question:** Does CodeRabbit ship blocking "custom checks" in Q4 2026 or Q1 2027? If yes, DocParity must pivot to multi-platform enforcement (GitLab + Bitbucket) or a richer namespace analytics product.

---

## #8 — MCPDock  ·  65/100  ·  DECLINED
First added: 2026-10-23 | Last updated: 2026-11-13 | Score delta this week: −2

> One managed, schema-validated, access-controlled MCP server registry for teams that need an approved catalog — not a Kubernetes operator.

### Score Breakdown
- Solo Buildability:   15/20  (MCP registry API + schema validation + access control + team approval workflows; well-scoped for a solo build; ToolHive's open-source registry server shows what the stack looks like)
- Value Clarity:       14/20  (unchanged — "10,000+ MCP servers, your team needs an approved 10" is a clear pitch; but ToolHive Registry Server now partially covers this for Kubernetes-native teams)
- Market Timing:       14/20  (−2 — ToolHive Registry Server now has schema validation for publisher-provided extensions (committed Feb 2026), access control, audit trail, named catalogs, API endpoint. ToolHive is still Kubernetes-focused (thv-operator). The managed SaaS registry for non-Kubernetes teams remains unserved.)
- B2B Monetisation:    13/20  (unchanged — $149-$499/mo per organization; teams using AI agents have tooling budgets)
- Pull Factor:         9/20   (unchanged — engineering teams share their MCP setups; a curated approved catalog is a shareable artifact)

**Strengths:**
- ToolHive Registry Server requires self-hosted deployment via Kubernetes. No managed SaaS option for the 90% of teams not running Kubernetes.
- The "approved catalog" use case (CTO wants to know which MCP servers the team is using; security team needs a whitelist) is not covered by ToolHive's self-hosted approach.
- Warpgate (usewarpgate.com) has health monitoring and per-tool latency — but no schema validation or approved-catalog governance.

**Risks:**
- Stacklok ships a managed/hosted ToolHive tier — this is the primary kill condition.
- MCP server governance gets absorbed into broader AI governance platforms (SimpleAct, Vanta, etc.) as a feature.
- The MCP ecosystem consolidates around 2–3 major server providers (Anthropic, OpenAI, Cloudflare) who maintain their own curated registries.

**Verdict:** Hold on the "approved catalog for non-Kubernetes teams" position. ToolHive confirmed schema validation but its deployment model is a moat in MCPDock's favor. Must reach first paying customers before Stacklok ships a managed tier.

### The Pitch
**Problem:** Teams using Claude Desktop, Cursor, or Windsurf in production now run 5–20 MCP servers providing tools to their AI agents. The official MCP server index has 10,000+ entries. Security-conscious teams — and every company receiving SOC 2 or vendor questionnaires — need an approved catalog: a curated, schema-validated list of which MCP servers are permitted, who approved them, and what tools they expose. Stacklok's ToolHive Registry Server (open-source, with schema validation and access control) addresses this for Kubernetes-native teams. The 90% of teams not running Kubernetes have no equivalent.

**Solution:** MCPDock is a managed SaaS registry for MCP servers. Teams add MCP server URLs or image references, MCPDock validates them against the official registry schema and ToolHive publisher-provided extension schema, routes them through a configurable approval workflow (security team reviews, manager approves), and publishes an approved catalog that Claude Desktop / Cursor / Windsurf can consume via a single managed registry URL. Audit trail included; version-locked approved catalog exported as JSON for compliance evidence.

**Target customer:** Head of Engineering / CISO at a 20–200 person company deploying AI coding agents (Cursor, Claude Code) across an engineering team. Buyer: CISO or Head of Engineering. User: DevOps / DevEx lead who manages the AI tooling stack.

**Why now:** MCP servers are production infrastructure in 2026. Stacklok's ToolHive Registry Server proves the category by launching schema validation — but requires Kubernetes. MCPDock is the managed SaaS version.

**Why they buy without being sold to:** A DevOps lead who gets asked "what MCP servers is the team running?" by the CISO spends 3 days auditing Claude Desktop config files across 40 engineering laptops. MCPDock's approved catalog makes the answer one URL — and the CISO gets a JSON export for the audit.

**Revenue model:** $149/mo (10 approved servers, 5 seats). $299/mo (unlimited servers, 20 seats + Slack approval workflow). $499/mo (SSO + audit export + compliance PDF). Annual −2 months. Free for single-user teams.

**Unfair advantage:** Managed SaaS with zero Kubernetes dependency — the operational gap Stacklok's ToolHive explicitly leaves open. First to integrate with the ToolHive registry schema standard means importing and validating existing ToolHive registries is a first-class feature.

### Solo Build Plan
1. Weeks 1–3: MCP server ingestion (URL + image reference); schema validation against official registry spec + ToolHive publisher-provided extensions; approved catalog JSON export.
2. Weeks 4–5: Approval workflow (request → review → approve/reject with reason); team permissions (who can propose vs. approve).
3. Weeks 6–7: Managed registry URL that Cursor/Claude Desktop can consume directly; audit trail per server action; version-locked catalog snapshots.
4. Weeks 8–9: Stripe; free single-user tier.
5. Weeks 10–12: Pilot 6 engineering teams via AI coding communities (Cursor Discord, Claude Code Slack).

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-11-13
**Strongest part:** ToolHive Registry Server is Kubernetes-only — the managed SaaS gap is confirmed by Stacklok's own product scope.
**Open question:** Does Stacklok ship a managed/hosted ToolHive tier at any price point before Q2 2027? This is the single kill condition. Monitor stacklok.com blog monthly.

---

## #9 — CredVerify  ·  64/100  ·  IMPROVED
First added: 2026-10-09 | Last updated: 2026-11-13 | Score delta this week: +1

> Credential 1–50 physicians in a new state without a credentialing coordinator or a $1,500/month software seat.

### Score Breakdown
- Solo Buildability:   13/20  (CAQH API + payer enrollment forms + PSV workflows + OIG/SAM monitoring; complex but well-defined scope; HIPAA BAA required)
- Value Clarity:       15/20  (unchanged — "physician who can't see patients because credentialing stalled = $20K/month in lost revenue" is 10-second math)
- Market Timing:       14/20  (+1 — Rivon Health has 0 verified user reviews on GetApp as of November 2026. Their case studies are promotional. No external validation of paying customer volume. Market penetration is still low; gap remains open for 6–50 provider groups that won't pay Modio's $1,000+/month.)
- B2B Monetisation:    13/20  (unchanged — $39-$199/mo per physician group; Rivon's white-glove service model at $1,500+ leaves a pure-SaaS gap)
- Pull Factor:         9/20   (unchanged — physician practice managers share tools through state medical society networks)

**Strengths:**
- Rivon Health GetApp listing: "No reviews" as of November 2026. GetApp says "0 user reviews" despite Rivon being founded in late 2025. This strongly suggests Rivon has not achieved significant market penetration — the case studies are promotional testimonials, not independent validation.
- Modio Health (acquired, $1,000+/month minimum) still serves enterprise health systems. The 6–50 provider group has no affordable pure-SaaS option confirmed.
- CMS 1,500 form + CAQH ProView + OIG/SAM monitoring are well-defined integrations with public APIs — the build is scoped.

**Risks:**
- Rivon Health could be getting traction without public reviews (many enterprise healthcare SaaS companies don't have Capterra/GetApp reviews). The "0 reviews" is not proof of no customers.
- State medical licensing boards have unpredictable API availability — some states require fax-based submissions even in 2026.
- Healthcare compliance requirements (HIPAA, state-specific credentialing rules) add legal liability for a solo product.

**Verdict:** Hold. Rivon's 0 verified reviews after 12+ months suggests limited market penetration. The 6–50 provider pure-SaaS gap is confirmed.

### The Pitch
**Problem:** A physician group practice expanding to new states needs each provider credentialed with payers and licensed in the new state before billing can begin. The manual path (CAQH ProView management, state board applications, payer enrollment, OIG/SAM monitoring) takes 90–180 days and costs $78,400 in lost revenue per provider if done wrong (documented in Rivon Health's own case study). Modio Health serves enterprise health systems at $1,000+/month minimum. Rivon Health offers white-glove services starting at $39/month but has no verified user reviews as of November 2026, suggesting limited self-service market penetration.

**Solution:** CredVerify automates the credentialing workflow for physician groups: CAQH ProView setup and attestation, state license application tracking, payer enrollment status across UHC/Aetna/Cigna/Humana, continuous OIG/SAM exclusion monitoring, and DEA registration status. Groups manage 1–50 providers from one dashboard; each provider's credentialing checklist is auto-populated from their existing CAQH profile.

**Target customer:** Practice administrator / office manager at a 2–50 provider independent physician group or specialty practice. Buyer and User: practice administrator or credentialing coordinator. Groups expanding to new states or adding providers to an existing payer mix are the primary trigger.

**Why now:** Modio Health was acquired (triggering customer uncertainty and pricing changes). Rivon Health has 0 verified reviews after 12+ months of operation — the market has not found its self-service tool yet. CMS 1,500 forms remain the standard; the workflow is well-defined.

**Why they buy without being sold to:** A practice administrator who lost 3 months waiting for a physician's new payer enrollment while billing was blocked imports the physician's CAQH profile into CredVerify, sees all missing documents and outstanding attestations identified in 10 minutes, and starts the enrollment process the same afternoon.

**Revenue model:** Free up to 3 providers. $99/mo (up to 15 providers + OIG/SAM monitoring). $249/mo (unlimited providers + payer enrollment tracking + appeal workflow). Annual −2 months.

**Unfair advantage:** Self-service pure-SaaS with CAQH API integration — Modio requires implementation, Rivon requires a service engagement. CredVerify lets a practice administrator run credentialing without hiring a coordinator or engaging a service firm.

### Solo Build Plan
1. Weeks 1–3: CAQH ProView API integration; NPPES provider lookup; OIG/SAM exclusion monitoring; provider credentialing checklist from CAQH profile data.
2. Weeks 4–5: Payer enrollment status tracker (UHC, Aetna, Cigna, Humana); state license tracking (NPI + CAQH state data).
3. Weeks 6–7: HIPAA BAA flow; audit log; document upload and verification tracking.
4. Weeks 8–9: Stripe; free 3-provider tier.
5. Weeks 10–12: Pilot 5 physician groups through state medical society networks and medical billing Facebook groups.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-11-13
**Strongest part:** Rivon Health's 0 verified reviews is a signal that the market has not found its self-service tool — the gap is real and open.
**Open question:** Does Rivon Health announce a paying customer milestone (25+ groups) in Q4 2026 or Q1 2027? If yes, the market is moving toward Rivon and CredVerify's window narrows. Monitor Rivon's LinkedIn for growth announcements.

---

## #10 — AgentAudit  ·  62/100  ·  DECLINED
First added: 2026-09-25 | Last updated: 2026-11-13 | Score delta this week: −6

> The Trust Registry for AI agent packages — the one place where a Trust Score means something, because it's publicly auditable and free.

### Score Breakdown
- Solo Buildability:   14/20  (trust registry + multi-engine scanner + OWASP MCP mapping; CI/CD integration; well-scoped but ongoing maintenance burden as new MCP servers ship daily)
- Value Clarity:       13/20  (−2 — "scan this MCP server before you install it" is clear; but Snyk Agent Scan, Cisco MCP Scanner, NVIDIA SkillSpector all do this; must lead with Trust Registry differentiation, not scanning)
- Market Timing:       12/20  (−4 — Snyk Agent Scan (Invariant Labs mcp-scan rebrand), Cisco MCP Scanner, NVIDIA SkillSpector, Tencent A.I.G, Hecate, ship-safe, Microsoft Agent Governance Toolkit all entered the space in 2026. The scanning layer is commoditizing. Trust Registry is the only remaining differentiation.)
- B2B Monetisation:    12/20  (unchanged — free scanning + paid Trust Registry subscriptions; enterprise security teams pay for trust infrastructure)
- Pull Factor:         11/20  (unchanged — developer security community shares trust scores; "X Trust Score" in GitHub README is a shareable badge)

**Strengths:**
- AgentAudit's Trust Registry (public database of audited packages with Trust Scores, OWASP MCP mapping, independent multi-agent verification) has no equivalent in any competitor. Snyk sends data to their API; Hecate/ship-safe/NVIDIA run locally. Neither builds a public Trust Score database.
- The "free forever" unlimited scanning tier is the strongest distribution moat in the category — every other tool requires a Snyk token, a Cisco API key, or cloud calls.
- AgentAudit's 19/20 self-scoring vs mcp-scan's 7/20 is based on features (OWASP mapping, CI/CD, Trust Registry, free tier) that are genuinely differentiated.

**Risks:**
- 7+ commercial and open-source tools now compete in MCP security scanning. Market noise obscures differentiation.
- Microsoft Agent Governance Toolkit (released April 2026, MIT, sub-millisecond runtime policy enforcement) is from Microsoft — distribution and trust advantages are hard to match.
- NVIDIA SkillSpector and Cisco MCP Scanner are from large enterprise vendors — enterprise security buyers may default to vendor-familiar tools rather than independent registries.

**Verdict:** Defend the Trust Registry. The scanning layer has commoditized. AgentAudit's moat is the data asset (a public, independently audited Trust Score database), not the scanning engine. Reframe marketing from "security scanner" to "Trust Registry for AI agents." Monetize through enterprise Trust Registry subscriptions, not scan volume.

### The Pitch
**Problem:** Teams installing MCP servers for Claude Code, Cursor, and Windsurf in 2026 have no independent, transparent Trust Score for the packages they're running. Snyk Agent Scan sends component data to Snyk's proprietary API. Cisco MCP Scanner requires Cisco AI Defense API credentials. NVIDIA SkillSpector runs locally but produces a 0–100 score with no public validation history. None of them maintain a publicly auditable, independently verifiable trust database — the analog to npm's public vulnerability database for the agent security era.

**Solution:** AgentAudit maintains a public Trust Registry: every audited npm package, pip package, MCP server, and AgentSkill gets a Trust Score (0–100) backed by multi-agent security audits, OWASP MCP Top 10 mapping, and a public audit history. Teams scan packages against the registry before installation (free, unlimited, no API key required) and subscribe to registry updates via CI/CD. Enterprise plans include private registry entries for internal MCP servers, continuous monitoring for Trust Score changes on installed packages, and SOC 2 evidence export.

**Target customer:** Security lead / DevOps engineer at a 20–500 person company deploying AI coding agents (Cursor, Claude Code) with internal security review requirements. Buyer: Head of Security or CTO. User: DevOps engineer who manages the AI toolchain. The trigger: "our security team asked what packages our AI agents are running."

**Why now:** MCP server count crossed 10,000+ in 2026 (Databricks $499K/year case). Teams can't manually vet 10,000 packages. The scanning tools validate their own scores privately; AgentAudit's public audit history is the only independent trust infrastructure available.

**Why they buy without being sold to:** A security engineer who needs to answer "is this MCP server safe to install?" runs AgentAudit's free CLI, sees a Trust Score with 3 specific findings and an OWASP MCP mapping, and subscribes to get alerts when that score changes. The free scan is the demo; the Trust Score change alert is the subscription.

**Revenue model:** Free: unlimited public registry queries, CLI scan, Trust Score. $149/mo (private registry + CI/CD integration + Trust Score change alerts for 20 packages). $399/mo (unlimited packages + team dashboard + SOC 2 evidence export). Annual −2 months.

**Unfair advantage:** Public audit history — every Trust Score change is published with the reason. No other tool in the category makes its security reasoning transparent. This is the SEO moat ("AgentAudit X package Trust Score") and the enterprise trust moat ("we can show auditors our source").

### Solo Build Plan
1. Weeks 1–3: Public Trust Registry (npm/pip/MCP server lookup by identifier); multi-agent audit pipeline (static analysis + OWASP MCP pattern matching); Trust Score (0–100).
2. Weeks 4–5: CLI scanner (free, unlimited, no API key); CI/CD GitHub Action; Trust Score badge for README.
3. Weeks 6–7: Trust Score change alert (notify when an installed package's score drops); private registry entries for internal MCP servers.
4. Weeks 8–9: Stripe; SOC 2 evidence export (audit report per installed package); enterprise trust audit workflow.
5. Weeks 10–12: Pilot 6 security teams via AI security communities and Cursor/Claude Code developer channels.

### Critic's Assessment (Round 1 → Round 2)

**Round 1 Critique:**
- The Trust Registry moat is only valuable if teams discover packages through AgentAudit. With 10,000+ MCP servers, discovery is the problem — does AgentAudit index all of them, or only audited ones? If only audited ones, it's incomplete.
- Microsoft AGT is from Microsoft — enterprise security buyers will default to it. Trust Scores from an independent startup compete against vendor credibility.
- The "free forever" model: who funds the ongoing audit pipeline?
- Rating: 5/10

**Round 1 Refinements:**
- AgentAudit should index all MCP servers (even unaudited) with a "pending audit" status — completeness is the Trust Registry's value, not just audited entries.
- Microsoft AGT is a runtime governance framework, not a pre-deployment registry — these are complementary, not competing. Position accordingly.
- Revenue model: free queries fund the discovery layer; enterprise subscriptions fund the audit pipeline.

**Round 2 Critique:**
- If AgentAudit indexes 10,000+ MCP servers with pending audit status, it's a directory, not a trust infrastructure. The Trust Score only means something if the audit quality is high — which requires real engineering time.
- Snyk has the resources to maintain scan quality. An independent registry may not.
- Rating: 6/10

**Round 2 Refinements (Final):**
- Focus Trust Registry on 500 "highest-install" MCP servers (Databricks, Cloudflare, Stripe, etc.) with full audits — not exhaustive coverage. Quality > completeness. The 10,000 tail can wait; the 500 widely-installed packages need Trust Scores.

**Final Rating:** 6/10 | **Last critique:** 2026-11-13
**Strongest part:** Public audit history with OWASP MCP mapping is the only independent trust infrastructure in a category filling with vendor-specific tools.
**Open question:** Does agentaudit.dev announce a commercial tier in Q1 2027 (ending "free forever")? If yes, enterprise adoption will accelerate before the announcement window closes.

---

## Removed this run

| Entry | Last score | Reason |
|-------|------------|--------|
| AuthTrack | 65 → 57 | Direct clone competitor: **AuthTrack Pro** (authtrackpro.com) tracks PA due dates, overdue items, denials for clinics and enterprise teams. **Adulis Health** explicitly implements CMS 7-day/72-hour deadline tracking with proactive alerts for specialty practices. **EasyPA** has deadline countdowns and is CMS-0057-F ready. The tiny beachhead (2–5 provider fax shops not on FHIR) is too narrow to sustain a solo product. Displaced by #3 AgentDrift (76). |
