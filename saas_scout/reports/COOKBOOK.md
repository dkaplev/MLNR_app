# SaaS Opportunity Cookbook
Last updated: 2026-10-02 | Entries: 10/10

> R15 note: Three removed. **RuleFlow removed** — Canarie's Radar module confirmed to cover federal regulatory monitoring + triggered execution, narrowing RuleFlow's horizon-scanning moat to FRTracker obligation extraction alone; displaced by stronger new entries. **IntegSecPack removed** — Vanta Customer Trust Agent live with AI-agent questionnaire automation, 6-month kill timeline accelerating. **ChurnDetect removed** — Zendesk QA Spotlight confirmed as account-level churn predictor from support conversations; open question answered. Three added: **MCPGate** (MCP runtime OAuth proxy, 74), **StackClean** (SaaS zombie killer, 73), **ImpactDeck** (EU AI Act Art. 27 FRIA lifecycle SaaS, 71). CRAReport +1 (CSA confirms no-API as "operating reality for foreseeable near term"). AgentCreds +2 (SEP-1046 + 2026-07-28 MCP spec shipped). DentPay -2 (Samera AI launches US Associate Pay Calculator). DORAIncident -2 (Copla, Resiplan, DORA GRC confirmed as purpose-built competitors). ModelReg -3 (AegisAI confirmed live SaaS with SR 26-2/OCC 2026-13 coverage). AgentAudit -2 (Cisco MCP Scanner + OSS scanners appearing; protected by < 2-week rule).

---

## #1 — CRAReport  ·  80/100  ·  IMPROVED
First added: 2026-09-04 | Last updated: 2026-10-02 | Score delta this week: +1

> Turn a 24-hour CRA incident window into a 10-minute SRP submission — without an API that does not exist yet.

### Score Breakdown
- Solo Buildability:   16/20  (SBOM/vuln feed ingestion + timeline engine + web-form-ready draft pack; no ERP integrations required)
- Value Clarity:       16/20  (product security lead who just discovered an exploited CVE understands the 24h clock immediately)
- Market Timing:       19/20  (+1 — CSA research note September 18 2026 labels no-API as "operating reality for foreseeable near term rather than a temporary inconvenience"; the gap is now officially documented by a major security authority)
- B2B Monetisation:    17/20  (€15M fine ceiling + one avoided misreport justifies $299–799/month with zero argument)
- Pull Factor:         12/20  (PSIRT Slack, ENISA stakeholder community, EU product security mailing lists; first-mover SEO on "CRA SRP submission" is the durable asset)

**Strengths:**
- ENISA's AR User Manual (September 9, 2026) published a 55-page guide for manual submission — confirming the portal is real, live, and manual-only for the foreseeable future.
- CRAevidence.com and ENISA's own FAQ both confirm "API may be considered in future phase" with no committed date, making CRAReport's automation bridge valuable for months to years.
- 24h Early Warning → 72h Notification → 14-day Final Report is a three-stage workflow problem; no CSIRT tooling vendor has built a product-security–facing SRP prep layer.

**Risks:**
- ENISA could announce an API roadmap date at any time, collapsing the manual-prep thesis.
- Large IT GRC vendors (ServiceNow, Archer) could add a CRA SRP export module to existing vulnerability management workflows.
- The market of "manufacturers with EU-market products under CRA" is well-defined but requires outbound education of a relatively new regulation.

**Verdict:** #1 position confirmed. No API, no competition, enforcement live. Build and distribute now.

### The Pitch
**Problem:** From 11 September 2026, EU Cyber Resilience Act Article 14 requires manufacturers of products with digital elements to report actively exploited vulnerabilities and severe security incidents to ENISA's Single Reporting Platform. The clock is strict: 24-hour Early Warning, 72-hour fuller Notification, 14-day Final Report. ENISA launched the SRP one day before its own legal deadline and confirmed it will not provide an API at initial release — every submission must be entered through a web form. A product security team discovering a critical CVE at 3 PM on a Thursday has under 24 hours to locate product metadata, map affected Member States, draft a technically accurate early warning, and manually enter it into a portal they may have never used. Failure carries fines up to €15M or 2.5% of global turnover.

**Solution:** CRAReport ingests the manufacturer's SBOM or vulnerability management feed, maps active CVEs against the CRA's reporting criteria, assembles a pre-filled SRP draft pack (product name, version, EUVD/CVE identifier, affected Member States, incident description), and tracks the 24h/72h/14-day submission deadlines per incident. The security team reviews, approves, and copies the structured output into the ENISA portal — cutting a multi-hour form assembly process to under 15 minutes per report.

**Target customer:** Product security lead / PSIRT manager / VP Engineering at a 20–500 person company shipping software or embedded products (IoT, industrial, consumer electronics, B2B SaaS) into EU markets. Buyer: Head of Product Security or CTO. User: the engineer who currently owns CRA compliance. Company has at least one product that would trigger CRA reporting obligations.

**Why now:** CRA Article 14 reporting obligations became live on 11 September 2026. ENISA's own FAQ confirms: "no API will be provided at the initial release of the SRP." The CSA research note from September 18, 2026 states: "manufacturers should treat manual entry as the operating reality for the foreseeable near term rather than a temporary inconvenience." The compliance need is real, the tooling gap is documented, and the first major incident for an unprepared company is the strongest possible conversion trigger.

**Why they buy without being sold to:** A PSIRT engineer who just received a CVE that triggers 24-hour reporting loads CRAReport, confirms SRP applicability in 30 seconds via the scope check, maps the SBOM entry to the ENISA form fields automatically, and pastes the draft into the portal — instead of spending 4 hours figuring out what to write. The second report is a reflex.

**Revenue model:** $299/month (1 product family, 5 users, 12-month incident log). $499/month (5 product families + Jira/GitHub integration + draft review). $799/month (unlimited + SBOM auto-ingest + SSO + priority SLA). Annual −2 months. Free CRA Scope Questionnaire (does CRA Article 14 apply to you?) as lead generation.

**Unfair advantage:** First-mover with ENISA SRP field mapping as a product fixture; SEO for "CRA SRP submission tool" is unclaimed territory; SBOM-to-SRP automation is a durable, defensible primitive that no CSIRT or GRC vendor has productised.

### Solo Build Plan
1. Weeks 1–3: CRA scope questionnaire (free lead magnet); SRP field map (product name, version, CVE/EUVD, Member States, incident type); incident record with 24h/72h/14-day deadline tracker.
2. Weeks 4–5: SBOM ingest (CycloneDX/SPDX parser); CVE-to-SRP applicability check; pre-filled draft pack generator (text ready to paste into ENISA portal).
3. Weeks 6–7: GitHub Issues / Jira webhook for CVE-assigned tickets; email alerts at 18h/66h/12-day before each deadline; audit log.
4. Weeks 8–9: Stripe; 14-day trial with sample SBOM scenario; multi-product family support.
5. Weeks 10–12: Pilot 6 product security teams via FIRST.org, ENISA stakeholder lists, and EU Cyber Week (October 2026).

### Critic's Assessment
**Rating:** 9/10 | **Last critique:** 2026-10-02
**Strongest part:** ENISA's AR User Manual + CSA research note together constitute official third-party documentation that the gap is permanent and the deadline is live. The distribution moat (SEO + PSIRT community) is clear.
**Open question:** At what point does ENISA publish a committed API timeline, and will CRAReport have enough installed-base momentum to survive the resulting "wait for the API" objection?

---

## #2 — DentPay  ·  77/100  ·  DECLINED
First added: 2026-07-16 | Last updated: 2026-10-02 | Score delta this week: −2

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (CSV-first rule engine; no PMS writeback required in v1)
- Value Clarity:       18/20  (OM ritual is self-evident; the Friday spreadsheet is a universal dental-practice pain)
- Market Timing:       15/20  (−2 — Samera AI launched US-facing Associate Pay Calculator with "automated pay splits, deductions, and multi-clinic control" language directly matching DentPay's thesis; still UK/Dentally focused but the US positioning is now explicit)
- B2B Monetisation:    16/20  (wrong paycheck = employer liability; $149–399/month is cheap next to a payroll dispute)
- Pull Factor:         12/20  (study clubs; US outreach via OD user groups; CPA referral program)

**Strengths:**
- Samera AI's "Before vs After" example still shows Dentally + Xero — the US OD/Dentrix/Eaglesoft + Gusto/ADP production-split bridge is not yet claimed.
- Dentivize remains analytics dashboards (take-home % visualization), not a pay calculation engine with anomaly flagging.
- Sticky once pay rules are configured — wrong paycheck means employer liability; switching cost is existential.

**Risks:**
- Samera AI's US expansion is explicit and accelerating; if they ship OD/Dentrix CSV ingest in Q4 2026, DentPay's window closes.
- Netchex and CareStack now advertise native hygienist productivity tracking; the OD/Dentrix→Gusto bridge remains unclaimed but the window is tightening.
- Relationship-heavy sales; CPA/advisor trust needed for paycheck-math credibility.

**Verdict:** Hold. US OD/Dentrix CSV-first beachhead still open but Samera AI's US launch is the most credible threat to date — build and ship in Q4 2026 before they add OD integration.

### The Pitch
**Problem:** US dental practices paying associates and hygienists on production still spend hours each pay period exporting Open Dental or Dentrix reports, pasting into Excel, applying lab fees, write-offs, and card-fee deduction rules, then hoping the spreadsheet matches the contract. Open Dental's Provider Payroll report is raw material, not a pay engine. Samera AI automated this for UK practices (Dentally + Xero); their US site now advertises "automated pay splits" and "multi-clinic control," but their worked example still shows Dentally/Xero. The US OD/Dentrix/Eaglesoft → Gusto/ADP production-split reconciliation is unbuilt.

**Solution:** DentPay imports OD/Dentrix production exports, applies per-provider pay rules once (percentage splits, lab-fee deductions, write-off thresholds, card-fee recovery), flags anomalies before payout, and exports a Gusto/ADP-ready approval pack. Office managers review exceptions; they do not rebuild formulas.

**Target customer:** Office manager / owner at a 1–3 location US dental practice on Open Dental or Dentrix with associates or hygienists on production splits. Buyer: practice owner. User: the OM who runs payroll.

**Why now:** Samera's US expansion confirms willingness-to-pay in this category. The US PMS-specific layer (OD/Dentrix CSV ingest + Gusto/ADP export) is the unclaimed wedge that UK tools haven't productised yet.

**Why they buy without being sold to:** An OM who spent Sunday correcting a hygienist underpay uploads last month's OD export, sees the same correct total with three flagged lab mismatches, and refuses to go back to Excel.

**Revenue model:** $149 / $249 / $399 per practice per month. 30-day trial. CPA referral program at 15%.

**Unfair advantage:** US OD/Dentrix rule templates + anomaly library built before Samera completes their US OD integration; study-club distribution; PE roll-ups won't chase at $149.

### Solo Build Plan
1. Weeks 1–3: OD Provider Payroll CSV ingest; rule builder (%, lab deduction, write-off, card-fee); pay summary PDF.
2. Weeks 4–5: Anomaly flags; period-over-period comparison; Gusto CSV export.
3. Weeks 6–7: Dentrix production report path; multi-provider approval flow.
4. Weeks 8–9: Stripe; sample-file onboarding.
5. Weeks 10–12: Pilot 8 practices via OD user groups and dental study clubs.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-10-02
**Strongest part:** Samera's own US page still shows Dentally/Xero — the OD/Dentrix CSV path is documented as unclaimed.
**Open question:** Will Samera AI ship Open Dental integration in Q4 2026, and if so, can DentPay establish enough installed base to survive on product quality and switching cost?

---

## #3 — MCPGate  ·  74/100  ·  NEW
First added: 2026-10-02 | Last updated: 2026-10-02 | Score delta this week: —

> Service accounts, tool allowlists, and tamper-proof audit logs for remote MCP servers — deployed in 10 minutes.

### Score Breakdown
- Solo Buildability:   15/20  (HTTP reverse proxy + OAuth 2.1 token validation + NDJSON audit log; scoped to HTTP/SSE transport only in v1; achievable in 3 months)
- Value Clarity:       15/20  (engineering lead who has read the 2026-07-28 MCP spec understands the product in one sentence; requires MCP familiarity)
- Market Timing:       16/20  (2026-07-28 MCP Auth spec revision confirmed; SEP-1046 client credentials shipped in TypeScript/Python/Ruby SDKs; "implement auth for all these MCP servers" sprint is live at every AI-native company right now)
- B2B Monetisation:    14/20  ($149–599/month for AI-native teams; OSS self-hosted tier drives adoption; cloud tier captures teams that don't want to self-host)
- Pull Factor:         14/20  (developer-viral via OSS + GitHub stars + Hacker News; "MCP gateway" is a searchable category being created in real time)

**Strengths:**
- The 2026-07-28 MCP spec mandated OAuth 2.1 for HTTP-based MCP servers and deprecated Dynamic Client Registration in favor of Client ID Metadata Documents — every team with remote MCP servers needs to implement this now.
- MCP-native protocol awareness (inspecting JSONRPC tool_call messages to enforce allowlists) is not replicable by generic API gateways without MCP-specific logic.
- OSS-first distribution creates the PLG moat: GitHub stars, HN launch, and "MCPGate" as the default answer to "how do I secure my MCP servers?"

**Risks:**
- Anthropic, WorkOS, or AWS could ship a first-party MCP OAuth management product as a platform feature.
- Engineers may roll their own thin wrapper using Nginx + auth_request rather than pay $149/month for MCPGate.
- The market narrows to companies running their own remote MCP servers — teams using only hosted/marketplace MCP tools (Cursor built-ins, Claude.ai integrations) don't need MCPGate.

**Verdict:** Enter as OSS-first with a SaaS cloud for teams who don't want to self-host. Be the default "how do I auth my MCP servers" answer on GitHub and HN.

### The Pitch
**Problem:** The 2026-07-28 MCP authorization specification formalized OAuth 2.1 for HTTP-based remote MCP servers, and SEP-1046's client credentials grant shipped in TypeScript, Python, and Ruby SDKs. Yet 95% of AI agent production rollouts still hit authentication failures as the top breaking issue (traversaal.ai Q2 2026). Engineering teams building production agentic systems must now implement per-agent service accounts, tool-level allowlists, and structured audit logs across every MCP server they run — and every team is building the same thin scaffolding from scratch. A 15-person AI-native company running 8 MCP servers and 12 agents has no standard product for this.

**Solution:** MCPGate is a reverse proxy for remote MCP servers. Deploy it with Docker Compose: define which MCP server endpoints it protects, register each agent as an OAuth client (private_key_jwt recommended, client secrets for compatibility), and configure tool allowlists per agent. Agents call MCPGate's endpoint instead of MCP servers directly. MCPGate validates the token against the 2026-07-28 spec, checks the tool call against the agent's allowlist, proxies allowed calls, and returns 403 with a structured reason code for blocked calls. Every call — allowed or blocked — writes to a tamper-proof NDJSON audit log.

**Target customer:** Engineering lead or platform architect at a 10–100 person AI-native or AI-forward company running 2+ remote MCP servers in production with 3+ unattended AI agents. Buyer: CTO/Head of Platform. Users: the 1–3 platform engineers responsible for AI agent infrastructure. Company is in a regulated industry or has enterprise customers asking for agent audit trails.

**Why now:** The 2026-07-28 MCP spec revision made HTTP MCP auth non-optional for production deployments. SEP-1046 shipped the OAuth client credentials SDK primitives. The engineering blog posts are being written this month; the "implement auth for your MCP servers" sprint is the current project at every company deploying agents at scale. MCPGate is that sprint, shipped.

**Why they buy without being sold to:** An engineering lead whose production incident postmortem reads "MCP server tool called with shared token — no audit trail of which agent triggered the action, which customer data was accessed, or why" deploys MCPGate that afternoon, maps 12 agent clients to 8 MCP servers with tool allowlists, and adds it as a required step in the AI agent deployment runbook before the next sprint.

**Revenue model:** Free OSS tier (Docker Compose, local dashboard, unlimited; self-hosted). $149/month Cloud (managed MCPGate endpoint, 30-day audit log, web dashboard). $299/month Teams (multi-instance, SSO, 90-day log, Slack alerts on blocked calls, team shared config). $599/month Enterprise (custom log retention, SIEM export via webhook, SLA). Annual −2 months.

**Unfair advantage:** MCP-native JSONRPC inspection (knows the difference between tools/list and tools/call at the protocol level); pre-built OAuth client profiles for Claude Code, Cursor, and the top 10 public MCP servers; OSS repo as permanent distribution moat and the default GitHub answer for "MCP auth proxy."

### Solo Build Plan
1. Weeks 1–3: HTTP/SSE reverse proxy (Go or Node); OAuth 2.1 token validation (audience binding, expiry, scope); JSONRPC tool_call inspection; per-agent tool allowlist; 403 on blocked calls; NDJSON audit log to stdout.
2. Weeks 4–5: Docker Compose packaging; local web dashboard (registered agents, recent calls, blocked events); client registry (client ID → allowed tools, token metadata).
3. Weeks 6–7: GitHub Action for deployment validation; OSS launch on GitHub with working Docker Compose example; MIT license.
4. Weeks 8–9: Stripe; SaaS cloud managed proxy endpoint (dedicated subdomain per customer); 30-day log retention with search.
5. Weeks 10–12: Hacker News launch ("Show HN: MCPGate — OAuth proxy and audit log for remote MCP servers"); pilot 5 AI-native companies via Anthropic Builders community and MCP Discord.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-10-02
**Strongest part:** The 2026-07-28 spec + SEP-1046 create a concrete, documented, time-stamped demand moment; the OSS lead magnet is the proven developer-tool distribution pattern.
**Open question:** Will Anthropic or WorkOS ship a production-grade MCP OAuth management console before MCPGate reaches critical mass on GitHub?

---

## #4 — AgentCreds  ·  74/100  ·  IMPROVED
First added: 2026-09-25 | Last updated: 2026-10-02 | Score delta this week: +2

> Pre-configured OAuth service accounts for every AI agent — so your team stops sharing the admin token.

### Score Breakdown
- Solo Buildability:   15/20  (credential vault + OAuth client profile library + per-agent scope mapping; the SDK primitives are published)
- Value Clarity:       15/20  (+1 — SEP-1046 and the 2026-07-28 MCP spec make the "service account per agent" story concrete and citable; engineering leads now have a specific spec to point to)
- Market Timing:       17/20  (+1 — SEP-1046 accepted October 2025, shipped in TypeScript/Python/Ruby SDKs; 2026-07-28 MCP Auth spec revision confirmed; Ampersand 2026: 45% authentication blocker, 47% permissions blocker; moment is NOW)
- B2B Monetisation:    14/20  ($149–499/month; engineers are trained to pay for auth infrastructure; usage-based on agents managed is a natural expansion vector)
- Pull Factor:         13/20  (eng Twitter/LinkedIn; "how we stopped sharing the admin token" post template is a built-in growth content moment)

**Strengths:**
- SEP-1046 shipped in the TypeScript, Python, and Ruby MCP SDKs — the specification is live, the primitives are available, and the market moment is confirmed.
- Ampersand 2026 State of Agentic Integrations: 45% authentication/credentials deployment blocker, 47% "what agents are allowed to do" blocker — both are AgentCreds' core thesis.
- No IAM incumbent (Okta, HashiCorp, Teleport) has designed a purpose-built interface for AI agent service accounts with pre-built OAuth profiles for the top SaaS APIs.

**Risks:**
- Okta or HashiCorp could announce AI-agent–specific service account features as a platform extension.
- MCPGate (also new to this cookbook) partially overlaps: MCPGate handles the proxy/enforcement layer, AgentCreds handles the credential/profile management layer — both are needed but a customer might conflate them.
- If the MCP ecosystem consolidates on a single hosted identity provider (e.g., Anthropic's own OIDC), a third-party service-account manager loses its wedge.

**Verdict:** Keep. The spec crystallization is the strongest signal yet. MCPGate and AgentCreds are complementary (credentials management vs runtime enforcement), not duplicative.

### The Pitch
**Problem:** AI agents in production are credentialed with shared API keys, repurposed service accounts with admin-level permissions, or long-lived tokens that nobody knows how to rotate. The Ampersand 2026 State of Agentic Integrations report found authentication/credentials as the second-biggest deployment blocker (45%) and "defining what agents are allowed to do" third (47%). SEP-1046's OAuth client credentials grant — now shipped in the TypeScript, Python, and Ruby MCP SDKs — defines how AI agents should authenticate using short-lived, scoped tokens and private key JWT assertions. Most engineering teams have the spec; none have a product that translates it into a credential registry with pre-built OAuth profiles for the 50 SaaS APIs agents most commonly call.

**Solution:** AgentCreds is a credential registry for AI agents. Create a service account per agent (not per team), upload the agent's RSA key pair (or let AgentCreds generate one), and select from pre-built OAuth profiles for the top 50 APIs (GitHub, Slack, HubSpot, Salesforce, Linear, Notion, Google Workspace, Stripe, Jira, Zendesk...). AgentCreds issues a scoped token for each agent–API pair following the 2026-07-28 MCP Auth spec and SEP-1046 private_key_jwt method. When a token approaches expiry, AgentCreds rotates it automatically. The engineer sees a dashboard: which agents have credentials to which APIs, scope granted, last-used timestamp, and any anomalous call patterns.

**Target customer:** Engineering lead / platform architect at a 20–200 person B2B SaaS company deploying 3+ unattended AI agents in production. Buyer: CTO/Head of Platform. Users: engineers deploying agents who currently share service account tokens or distribute API keys manually. Company uses 5+ SaaS APIs that agents need access to.

**Why now:** SEP-1046 shipped Q4 2025 and is in all major MCP SDKs. The 2026-07-28 MCP Auth spec revision confirmed OAuth 2.1 + client credentials as the standard for unattended agents. The engineering community is now building agent auth infrastructure from the spec; AgentCreds is the product layer that removes that scaffolding work.

**Why they buy without being sold to:** An engineering lead whose company just passed a SOC 2 audit with a finding of "AI agents are credentialed with shared admin tokens — no per-agent scope, no rotation policy" opens AgentCreds, maps each agent to a separate client with scoped pre-built profiles, and closes the audit finding in a day rather than a sprint.

**Revenue model:** $149/month (up to 5 agents + 10 API profiles). $299/month (20 agents + unlimited profiles + SSO). $499/month (unlimited + private_key_jwt key management + SIEM webhook + SLA). Annual −2 months. Free tier: 1 agent, 3 profiles, manual rotation.

**Unfair advantage:** Pre-built OAuth client profiles for the 50 most-used SaaS APIs by AI agents, updated as API auth specs change; SEP-1046-native key management (private_key_jwt) that IAM incumbents haven't productised; complements MCPGate for teams that need both credential management and runtime enforcement.

### Solo Build Plan
1. Weeks 1–3: Agent registry (agent name, key pair, API profiles); OAuth client credentials flow (private_key_jwt + client secrets); token issuance and storage per agent-API pair.
2. Weeks 4–5: Pre-built OAuth profiles for top 10 APIs (GitHub, Slack, HubSpot, Salesforce, Notion, Linear, Stripe, Jira, Zendesk, Google Workspace); token rotation scheduler.
3. Weeks 6–7: Dashboard (agent → API credential map, last-used, anomaly flags); audit log export.
4. Weeks 8–9: Stripe; free tier gating; SOC 2 finding template ("how AgentCreds closed audit finding X").
5. Weeks 10–12: Pilot 5 engineering teams via Anthropic Builders community, YC Slack, and engineering blog post ("We stopped sharing the admin token — here's how").

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-10-02
**Strongest part:** The Ampersand 2026 survey quantifies the exact blocker (45%+47%), and SEP-1046 provides the technical foundation that separates AgentCreds from a generic credential vault.
**Open question:** Will Okta or HashiCorp Vault ship a dedicated "AI agent service account" SKU before AgentCreds reaches 50 paying customers?

---

## #5 — StackClean  ·  73/100  ·  NEW
First added: 2026-10-02 | Last updated: 2026-10-02 | Score delta this week: —

> Finds the 20% of your SaaS stack that nobody uses — before it auto-renews again.

### Score Breakdown
- Solo Buildability:   16/20  (email invoice forwarding + bank/card feed parser + owner assignment + renewal calendar + Slack alerts; well-scoped for a solo developer; no bank API required for free tier)
- Value Clarity:       17/20  ("Found 11 orphaned subscriptions totaling $980/month" is a self-closing demo that requires no explanation)
- Market Timing:       12/20  (Subsight on waitlist October 2026; CostLoop.app basic tier exists; Torii/Zylo serve enterprise; SMB mid-tier at $29–99/month is thin but contested; Techaisle 2026 names token shock + AI spend unpredictability as #1 SMB IT challenge)
- B2B Monetisation:    14/20  ($29–99/month per team; high volume compensates for modest per-customer MRR; finance teams have clear budget authority for cost-reduction tools)
- Pull Factor:         14/20  ("I saved $X/month in 10 minutes" screenshots travel on Slack and LinkedIn; the discovery moment is inherently shareable)

**Strengths:**
- Email invoice forwarding as the zero-friction entry point eliminates the biggest adoption barrier (reluctance to share bank credentials); Plaid/card feed adds for paid tiers.
- Usage data from Google Workspace/Okta (last-login date per seat) turns "who uses this?" from a question into a one-click report — a feature that Subsight and CostLoop don't have.
- The "Renew or Cancel?" decision workflow with an audit record turns a passive renewal into a deliberate choice — durable moat against lazy competitors.

**Risks:**
- Subsight (on waitlist as of October 2026) could launch before StackClean and claim the PLG narrative in the SMB SaaS spend tier.
- Ramp, Brex, or Mercury could add SaaS-specific renewal alerts as a native feature of their business banking products.
- Plaid fees at commercial scale ($0.30–$0.60/connection/month) can erode margins if the free tier grows faster than paid conversions.

**Verdict:** Enter with email-forward-first discovery (no bank API required in free tier). Differentiate on SSO usage data. Ship before Subsight exits waitlist.

### The Pitch
**Problem:** The average 20-person company manages 20–60 software tools and wastes 25–30% of its SaaS budget on unused or underutilized licenses — roughly $9,000–$10,800/year for a team spending $3,000/month (Gartner 2026). A former employee's full Figma seat stays active for 8 months after their last day. Three different project management tools adopted by three different teams share the billing card. Nobody knows who added that $600/month Zapier plan or why. Enterprise solutions (Zylo at $2K+/month, Torii at $500+/month) serve the Fortune 500. SMBs use a Google Sheet that nobody updates — or nothing at all until a surprise auto-renewal shows up in the bank statement.

**Solution:** StackClean starts with forwarded invoices: forward your SaaS billing emails to your StackClean inbox, and it parses vendor names, amounts, renewal dates, and billing cycles automatically — no bank access required to start. For paid tiers, StackClean connects to bank/card feeds via Plaid or CSV upload to detect recurring charges automatically, pulls last-login data from Google Workspace or Okta to score each subscription's usage health, and assigns an owner per tool. When a renewal approaches, the assigned owner gets a one-line decision request: "Renew, downgrade, or cancel?" The response is logged as an audit record.

**Target customer:** Operations lead, office manager, or founder at a 10–100 person company spending $1,500–$8,000/month across 20–60 SaaS tools. Buyer: founder/COO/ops lead. User: the person who currently tracks subscriptions in a Google Sheet that hasn't been updated since the last offboarding. Industries: agencies, dev shops, consulting firms, B2B SaaS startups.

**Why now:** AI-powered tools have multiplied the average SaaS stack 2–3× since 2024, and every AI assistant comes with its own billing. Techaisle 2026 names AI spend unpredictability ("token shock") as the #1 SMB IT challenge. Subsight launched on waitlist October 2026, confirming unmet demand exists in the $29–99/month tier but no dominant player has shipped yet.

**Why they buy without being sold to:** After forwarding last month's Stripe receipts to their StackClean inbox and seeing 11 orphaned subscriptions totaling $980/month (including a full Figma seat for an intern who left in February), the ops lead purchases before the trial ends — without a demo, a call, or a sales email.

**Revenue model:** Free (forward up to 5 invoices/month, manual entry, basic renewal calendar). $29/month (unlimited invoice forwarding + renewal alerts + owner assignment). $59/month (+ bank/card feed via Plaid/CSV + Slack alerts). $99/month (+ Google Workspace/Okta last-login data + team ownership report + annual cost summary). Annual −2 months.

**Unfair advantage:** Email-forward-first onboarding removes the bank-credential friction that kills 80% of competitor trials; SSO last-login integration turns usage health from a manual survey into an automated score; the "Renew or Cancel?" decision audit trail creates compliance-grade records no spreadsheet can match.

### Solo Build Plan
1. Weeks 1–3: Email inbox (ForwardMX or similar) → invoice parser (vendor name, amount, billing date, renewal date); subscription dashboard; manual entry fallback.
2. Weeks 4–5: Renewal calendar; 30/7/1-day email + Slack alerts; owner assignment per subscription; "Renew/Cancel?" decision capture with timestamp.
3. Weeks 6–7: Bank/card CSV upload parser; Plaid integration for paid tier; recurring charge auto-detection.
4. Weeks 8–9: Google Workspace API (last-login date per tool domain); Okta integration for paid tier; usage health score per subscription; Stripe.
5. Weeks 10–12: Pilot 20 teams via Reddit r/SaaS, Product Hunt, ops lead LinkedIn communities; "I saved $X in 10 minutes" referral content template.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-02
**Strongest part:** The "found $980/month in orphaned subscriptions on first use" retrospective demo is self-closing — same pattern as ChurnDetect's retrospective demo but even more visceral because the savings are immediate.
**Open question:** Will Ramp or Brex add SaaS-specific renewal alerts natively to their business banking product, making StackClean's core alert function redundant for companies that already use these banking platforms?

---

## #6 — DORAIncident  ·  72/100  ·  DECLINED
First added: 2026-09-18 | Last updated: 2026-10-02 | Score delta this week: −2

> File your 4-hour DORA major incident notification in one click — not in three browser tabs and a spreadsheet.

### Score Breakdown
- Solo Buildability:   14/20  (ITS 2025/302 template builder + NCA-portal aware deadline engine + dry-run simulator; hard but scoped)
- Value Clarity:       15/20  ("your 4-hour clock started 2 hours ago" is visceral for any DORA-regulated compliance officer)
- Market Timing:       14/20  (−2 — Copla (DORA incident module), Resiplan/regulation-dora.eu (full DORA SaaS), DORA GRC (doragrc.com), and activeMind.cloud all confirmed as purpose-built DORA incident reporting tools; the space has more specialised competitors than last assessment; SME workbench + dry-run simulator is still unique)
- B2B Monetisation:    16/20  (ESMA SREP enforcement underway; a €10M fine makes $399/month invisible)
- Pull Factor:         13/20  (DORA compliance communities share tools via FS-ISAC, DORA Alliance, and fintech Slack)

**Strengths:**
- ESMA published fresh Operational Instructions in September 2026; multi-NCA fragmentation confirmed (CBI Portal, AFM Portal, BaFin MVP, ACPR, FCA all distinct portals).
- The dry-run simulator (pre-incident rehearsal with a test classification scenario) is explicitly unbuilt by Copla, Resiplan, or DORA GRC.
- SME fintech/payment firms (<€50M revenue) are explicitly underserved by Resiplan's enterprise-tier pricing.

**Risks:**
- Copla, Resiplan, and DORA GRC are all credible, purpose-built DORA tools — the space is no longer thin.
- Vendorica covering multiple NCAs would eliminate the multi-NCA fragmentation moat.
- BaFin plans SOAP API for incident reporting — if live, the German portal gap narrows.

**Verdict:** Hold. Pre-incident dry-run simulator + SME pricing is still a defensible wedge. Watch for a Vendorica multi-NCA confirmation.

### The Pitch
**Problem:** DORA Article 19 requires three-stage major incident reporting: initial notification within 4 hours of classification (and no later than 24 hours after first detection), intermediate update, and final report within one month. Each stage uses ITS 2025/302 XML or JSON templates with mandatory fields that differ by NCA — BaFin requires reports via its MVP portal, CBI uses its own portal, AFM has a separate submission channel, ACPR and FCA are distinct. When an incident is classified as major at 10 PM on a Friday, the CISO and compliance officer have 4 hours to produce a structured, NCA-specific submission from an incident that is still unfolding. Most firms are doing this in three browser tabs, a spreadsheet, and a copy of last quarter's incident report for reference.

**Solution:** DORAIncident is the pre-incident workbench and live reporting tool for DORA-regulated financial entities. In preparation: maintain the asset register and function catalog, configure NCA jurisdiction, and run quarterly dry-run classification scenarios. When a real incident fires: DORAIncident watches the 4h/72h/1-month clocks, pre-populates ITS 2025/302 mandatory fields from the asset register, routes for review, and exports the NCA-specific format. The firm reviews the output; they do not build the XML under time pressure.

**Target customer:** Compliance officer / CISO at a 50–500 person EU-licensed fintech, payment processor, investment firm, or insurance company subject to DORA. Buyer: CISO/CCO/CRO. Users: the 2–5 people in the DORA incident response chain. Not a Tier-1 bank with 500 compliance staff.

**Why now:** ESMA published updated Operational Instructions in September 2026. First SREP enforcement cycle is underway — regulators are using incident reporting quality as a supervisory signal. The firms that have not yet completed their first real major incident submission are the highest-urgency buyers.

**Why they buy without being sold to:** After a 90-minute incident response scramble where nobody could find the correct NCA XML template, the compliance officer runs a DORAIncident dry run with their last two incidents — sees the pre-populated fields and 4h clock — and purchases before the next board risk committee meeting.

**Revenue model:** $399/month (1 entity, ITS 2025/302 templates for 2 NCAs, quarterly dry-run). $599/month (3 NCAs + asset register + Jira/Slack incident trigger). $999/month (unlimited NCAs + multi-entity governance + SSO). Annual −2 months. Free dry-run simulator (one classification scenario, no incident export) as lead generation.

**Unfair advantage:** Pre-incident dry-run simulator (no competitor offers this); pre-built ITS 2025/302 template library per NCA (BaFin, CBI, AFM, ACPR, FCA) maintained as a versioned artifact updated with ESA Q&A publications; SME pricing below Resiplan's enterprise tier.

### Solo Build Plan
1. Weeks 1–3: ITS 2025/302 template model (initial/intermediate/final per NCA); 4h/72h/1-month clock engine; incident record with classification criteria from RTS 2024/1772.
2. Weeks 4–5: Asset register and CIF (Critical/Important Function) catalog; pre-population of NCA template fields from asset register.
3. Weeks 6–7: Dry-run simulator (test classification scenario with sample incident data; output a draft initial notification without live submission); Slack incident trigger webhook.
4. Weeks 8–9: Stripe; NCA-specific XML/JSON export (BaFin MVP format, ITS 2024/2956 JSON); 14-day trial.
5. Weeks 10–12: Pilot 5 EU fintech CCOs via DORA Alliance, FS-ISAC EU chapter, and RegTech meetups.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-02
**Strongest part:** The dry-run simulator is a differentiated onboarding mechanism with no competitive equivalent — running a rehearsal before a real incident is a documented best practice that no competitor has productised.
**Open question:** Is Vendorica covering all 5 major NCAs with working integrations, and if so, does DORAIncident's multi-NCA template library still matter?

---

## #7 — AuthTrack  ·  71/100  ·  UNCHANGED
First added: 2026-08-16 | Last updated: 2026-10-02 | Score delta this week: —

> See which prior auths are inside the 7-day / 72-hour clock — and which denials still have no specific reason.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — CSV/fax log + CMS-clock engine + denial-reason fields; no EHR writeback in v1; HIPAA applies)
- Value Clarity:       16/20  (unchanged — "this PA blows the CMS clock on Thursday" is obvious to any billing coordinator)
- Market Timing:       14/20  (unchanged — CMS-0057-F clocks live since 1 Jan 2026; FHIR PA APIs due 1 Jan 2027; Open Dental preauth module confirmed as basic status tracking only; Staffingly at $34–39/specialist/week is outsourcing, not software)
- B2B Monetisation:    14/20  (unchanged — $149–299/month; one avoided write-off pays for the year)
- Pull Factor:         13/20  (unchanged — biller Facebook groups; not publicly viral)

**Strengths:**
- CMS-0057-F clocks are binding. Open Dental's preauth module tracks submission status but does not enforce CMS-specific 7-day/72-hour windows or require a specific denial reason on every denial.
- Staffingly's outsourced dental PA service confirms there is a workflow (and a budget) but not a software alternative for small practices.
- Spreadsheet-first avoids the 4-week EHR integration that kills solo scope.

**Risks:**
- HIPAA + PHI handling from day one.
- Clearinghouses (Availity, Waystar) could ship a cheap clock tracker as a bundled feature.
- Small practices may wait for their clearinghouse rather than pay $149 for a standalone tool.

**Verdict:** Hold unchanged. FHIR PA API mandate (Jan 2027) creates a second inflection point for practices that need a log before the mandate.

### The Pitch
**Problem:** Since 1 January 2026, Medicare Advantage, Medicaid, CHIP, and FFE QHP payers must decide standard prior authorizations in 7 calendar days and urgent ones in 72 hours, and every denial must include a specific reason. Billing coordinators at 2–10 provider practices still track this in a spreadsheet next to the fax machine. They miss clocks, they cannot prove a vague denial, and they will need a clean log before the January 2027 electronic-PA attestation mandate. Open Dental's preauth module tracks submission status but does not enforce CMS window compliance or require a denial-reason field.

**Solution:** AuthTrack is the PA status board: each request gets a clock (7-day or 72-hour), a channel (fax/portal/phone), a denial-reason required field on every denial, and a reminder before the CMS window closes. v1 is CSV import + form entry — not an Athena integration, not a FHIR client.

**Target customer:** Billing coordinator / office manager at a 2–10 provider US practice (PT, specialty lite, independent primary care) that is not on a platform like Athena with Linear Health. Buyer: office manager. User: the biller who owns the Excel PA tab.

**Why now:** The clocks are live, not upcoming. The FHIR API mandate is January 2027. Practices that do not have a log now will invent one badly six months before MIPS.

**Why they buy without being sold to:** After a denied MRI with no specific reason and a missed 7-day follow-up, the biller pastes the spreadsheet into AuthTrack, sees two clocks already red, and stops using Excel that week.

**Revenue model:** $149/month (1 location, 200 PAs). $249/month (3 locations + reminder SMS). $299/month (export pack for appeals). Annual −2 months. 14-day trial with sample CSV.

**Unfair advantage:** CMS-clock templates + denial-reason required field sized for fax-era shops that enterprise PA platforms ignore.

### Solo Build Plan
1. Weeks 1–3: PA log (CSV import); 7-day/72-hour CMS clocks; denial-reason required on deny.
2. Weeks 4–5: Email/SMS reminders; aging report; appeal packet PDF.
3. Weeks 6–7: HIPAA BAA flow; audit log; role-based access.
4. Weeks 8–9: Stripe; sample-CSV onboarding.
5. Weeks 10–12: Pilot 6 small practices via biller Facebook groups and local MGMA chapters.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-02
**Strongest part:** Regulation is already in force; the buyer is a person with a spreadsheet, not a health-system IT committee.
**Open question:** Will tiny practices pay $149/month or will they wait for their clearinghouse to add a free clock SKU?

---

## #8 — ModelReg  ·  71/100  ·  DECLINED
First added: 2026-09-04 | Last updated: 2026-10-02 | Score delta this week: −3

> OCC exam ready on AI governance — before the examiner asks the question your model inventory can't answer.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — model inventory + validation evidence vault + OCC exam-readiness quiz; no bank system integrations required)
- Value Clarity:       15/20  (unchanged — "OCC exam readiness score for AI governance" is a 10-second pitch for a bank CCO who just received an exam notice)
- Market Timing:       11/20  (−3 — AegisAI confirmed live as a SaaS platform at aegisaicompliance.com with comprehensive SR 26-2/OCC Bulletin 2026-13 coverage, readiness assessments, model inventory, vendor diligence, and board reporting templates for exactly ModelReg's target; primary competitive threat has materialized)
- B2B Monetisation:    17/20  (unchanged — community banks already pay $15K–$50K/year in consultant fees for model risk reviews; $299–799/month is trivial)
- Pull Factor:         12/20  (unchanged — ABA, ICBA, compliance study groups share tools; not publicly viral)

**Strengths:**
- OCC Bulletin 2026-13 is live — replaces SR 11-7 and adds AI-specific obligations for model governance, validation, and third-party oversight.
- AegisAI appears to be primarily a template library (purchasable templates, assessments) rather than a recurring SaaS with automated monitoring. A persistent monitoring + evidence-gathering SaaS is still unbuilt at the community bank price point.
- OCC Request for Information on AI governance (noted in OCC Bulletin text) is forthcoming — will intensify examiner focus.

**Risks:**
- AegisAI's readiness assessment + template suite is highly credible and aligned exactly to SR 26-2 / OCC 2026-13. Even if it's template-based, it captures the "get compliant" budget before ModelReg.
- AegisAI could add recurring SaaS features (automated monitoring, live evidence collection) with their existing customer base.
- The OCC RFI process could delay examiner focus on AI governance for 12–18 months, reducing urgency.

**Verdict:** Hold. AegisAI's live presence is the biggest competitive threat yet, but its template-library model vs. ModelReg's recurring monitoring SaaS is the key differentiation to test. Differentiate explicitly on "automated ongoing monitoring" vs. "template pack."

### The Pitch
**Problem:** OCC Bulletin 2026-13 replaces SR 11-7 as the interagency model risk management standard, explicitly covering AI-enabled, vendor-managed, and rapidly-changing model environments. Community banks, credit unions, and fintechs must now produce evidence: a current model inventory, validation workpapers, monitoring metrics, change-control records, third-party oversight documentation, and board-visible reporting — aligned to the updated SR 26-2 language. AegisAI has launched a template library addressing this. But templates still require manual evidence collection and updating. The gap is a persistent SaaS that monitors model health automatically and assembles exam-ready evidence without a manual sprint.

**Solution:** ModelReg maintains a live model inventory with risk tiers, runs automated monitoring checks (did the model's performance drift? did a vendor update the model without notification? did the validation schedule lapse?), and generates an OCC Exam Readiness dashboard. When an examiner notice arrives, the CCO exports a structured evidence pack: inventory, validation records, monitoring history, vendor oversight documentation, board reporting cadence.

**Target customer:** CCO / CRO / model risk officer at a US community bank, credit union, or fintech lender with 1–50 AI models in production (including vendor-provided models used for credit decisions, fraud, or BSA/AML). Buyer: CCO. Users: model risk analyst + compliance team.

**Why now:** OCC Bulletin 2026-13 is live. AegisAI's template library confirms willingness-to-pay in this space. The OCC has signaled a forthcoming RFI on AI governance — a future enforcement intensification moment.

**Why they buy without being sold to:** A CCO who receives an OCC exam notice, runs ModelReg's free OCC Exam Readiness quiz, gets a score of 4/10 with three critical gaps highlighted (model inventory incomplete, no validation schedule, no board reporting cadence), and signs up for the trial before the exam team arrives.

**Revenue model:** $299/month (up to 10 models, exam readiness dashboard, evidence pack export). $499/month (50 models + vendor model monitoring + board report). $799/month (unlimited + SSO + custom OCC exam prep workflow). Annual −2 months. Free OCC Exam Readiness Quiz as lead generation.

**Unfair advantage:** OCC-aligned monitoring automation (drift detection, validation schedule lapse, vendor change alerts) that AegisAI's template library cannot do by definition; SR 26-2/OCC 2026-13 field mapping that is updated as the OCC issues Q&As; first-mover SEO on "OCC SR 26-2 compliance SaaS."

### Solo Build Plan
1. Weeks 1–3: Model inventory (risk tier, intended use, owner, vendor, validation date, monitoring cadence); free OCC Exam Readiness quiz; SR 26-2 gap analysis.
2. Weeks 4–5: Monitoring check scheduler (validation lapse alerts, performance-metric input form, vendor change log); board reporting template.
3. Weeks 6–7: Evidence pack export (inventory PDF, validation workpaper log, monitoring history, board deck).
4. Weeks 8–9: Stripe; 14-day trial; OCC exam notice trigger onboarding ("I just received an exam notice").
5. Weeks 10–12: Pilot 5 community banks via ABA compliance training network and ICBA member services.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-02
**Strongest part:** The OCC Exam Readiness quiz as a lead magnet + "exam notice trigger" onboarding flow creates a self-closing conversion mechanism with no pitch required.
**Open question:** Is AegisAI adding recurring SaaS monitoring features, and if so, at what price point and timeline?

---

## #9 — ImpactDeck  ·  71/100  ·  NEW
First added: 2026-10-02 | Last updated: 2026-10-02 | Score delta this week: —

> Your FRIA and DPIA in one living record — versioned every time your AI system changes.

### Score Breakdown
- Solo Buildability:   14/20  (Art. 27 FRIA six-section form + Art. 35 DPIA integration + version history + change-trigger webhooks; form-heavy but achievable solo in 3 months; no integrations required for v1)
- Value Clarity:       15/20  (DPO who just produced a static FRIA via KLA or Witness and received a client question "has this been updated since you added the LLM component?" understands ImpactDeck immediately)
- Market Timing:       16/20  (EU AI Act Art. 27 FRIA obligations live August 2, 2026 for specifically-obligated deployers; CNIL April 2026 harmonized DPIA+FRIA template creates structural standard; free generators validate demand but provide no lifecycle management; no persistent SaaS below ~€500/month confirmed)
- B2B Monetisation:    14/20  ($99–299/month; DPOs and GCs at fintech/HR-tech/insurtech deploying high-risk AI have clear compliance budget; one CNIL enforcement action more than justifies the price)
- Pull Factor:         12/20  (IAPP Europe community; DPO LinkedIn groups; client-sharing link creates viral growth when DPOs send evidence packs to enterprise clients asking for proof)

**Strengths:**
- The FRIA is not a one-time document: it must be re-done when system purpose, data types, or affected populations change. No tool tracks this lifecycle — every generator produces a static PDF.
- CNIL's April 2026 harmonized DPIA+FRIA template created a widely-adopted structure that ImpactDeck can implement as the canonical form, ensuring regulatory alignment.
- DPO-to-client sharing link (read-only evidence view) is a viral growth vector: when DPOs send their evidence pack to enterprise clients, those clients become ImpactDeck leads.

**Risks:**
- ellamind's elladoc explicitly names FRIA generation as a feature; if they add persistent version history, ImpactDeck's lifecycle differentiator collapses.
- KLA Digital or Witness could add "save my FRIA and notify on changes" as free features to their existing generators.
- The specifically-obligated FRIA deployer set is narrower than "all high-risk AI deployers": it applies to (1) public bodies, (2) credit-scoring systems (Annex III §5(b)), and (3) life/health insurance pricing (Annex III §5(c)) — plus private entities providing public services. This limits addressable market.

**Verdict:** Enter as the lifecycle management layer on top of the static-generator gap. Target specifically the three FRIA-obligated private deployer segments.

### The Pitch
**Problem:** From 2 August 2026, EU AI Act Article 27 requires deployers of certain high-risk AI systems — specifically credit-scoring systems, life/health insurance pricing models, and private entities providing public services using Annex III systems — to conduct a Fundamental Rights Impact Assessment before first use. The FRIA must complement (not replace) the GDPR Article 35 DPIA; CNIL published a harmonized combined template in April 2026. Free generators (KLA Digital, Witness, Startege) produce a static PDF covering the six mandatory Art. 27(1) sections. But a FRIA is a living document: it must be updated when the AI system's purpose changes, when new categories of affected persons are added, when oversight measures are modified. After an update, the deployer must be able to demonstrate which version was in force when, who approved it, and what changed. No tool below ~€500/month manages this lifecycle.

**Solution:** ImpactDeck is the persistent FRIA + DPIA record for EU AI Act deployers. Set up takes 30 minutes: input system description, populate the six FRIA sections (mapping to Art. 27(1)(a)–(f)) and the linked DPIA elements, build the risk register, and capture the DPO sign-off. When a system change occurs — new data source, expanded geography, updated model weights — the DPO or engineering lead creates a new version with a change note. ImpactDeck maintains the complete version history, sends re-assessment reminders based on the review schedule, and generates an evidence pack (current FRIA, change log, sign-off timestamps) for client requests or supervisory authority notifications under Art. 27(3).

**Target customer:** DPO or legal counsel at a 20–500 person company in one of three FRIA-obligated segments: (1) fintech deploying credit-scoring AI, (2) insurtech deploying life/health insurance pricing AI, or (3) B2B SaaS used by EU public bodies for HR/recruitment screening. Buyer: DPO/GC. Users: DPO + the engineering lead who triggers system changes.

**Why now:** FRIA obligations are live as of August 2, 2026 for the specifically-obligated deployer categories. CNIL's harmonized DPIA+FRIA template (April 2026) created a widely-adopted structural standard. Static generators have validated demand but left the lifecycle management problem unsolved. The first wave of enterprise clients asking vendors for proof-of-FRIA is arriving right now.

**Why they buy without being sold to:** A DPO who produced a FRIA using KLA's free generator in August, then received an email from a large enterprise client asking "please provide your current FRIA as of the date of our contract execution, including any updates since your LLM component was added in September" — has no answer without ImpactDeck. They migrate the KLA PDF into ImpactDeck in an afternoon.

**Revenue model:** $99/month (1 AI system, FRIA + DPIA sections, version history, PDF export, 3 users). $199/month (5 systems + CI/CD webhook trigger for version creation + client sharing link). $299/month (unlimited systems + SSO + DPA template bundle + authority notification log). Annual −2 months. Free FRIA scope check quiz (does Art. 27 apply to your deployment?) as lead generation.

**Unfair advantage:** CNIL April 2026 harmonized DPIA+FRIA template as the structural backbone means ImpactDeck is natively aligned to the most-adopted EU guidance; webhook-triggered versioning (connect your CI/CD deploy pipeline) is a technical moat no static generator can replicate; DPO-to-client sharing link creates viral growth through enterprise procurement requests.

### Solo Build Plan
1. Weeks 1–3: Art. 27 FRIA six-section form (system description, duration, affected persons, fundamental-rights risks, human oversight, governance/complaints) + Art. 35 DPIA integration; risk register; PDF/ZIP export; basic version history.
2. Weeks 4–5: Change record creation (DPO notes what changed + approves new version); re-assessment reminder engine (date-based + webhook trigger); version diff view.
3. Weeks 6–7: Client/auditor read-only share link; sign-off/attestation capture per version; authority notification log (Art. 27(3)).
4. Weeks 8–9: Stripe; free FRIA scope check quiz; 14-day trial with pre-populated example (fintech credit scoring).
5. Weeks 10–12: Pilot 5 DPOs via IAPP Europe, CNIL stakeholder community (public consultation participants), and EU AI Act Slack/Discord.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-02
**Strongest part:** The version-history + re-assessment webhook is a genuine technical moat over every static generator; the "enterprise client asks for current FRIA" onboarding trigger is specific and self-closing.
**Open question:** Will ellamind or KLA Digital add persistent version history to their free FRIA generators, eliminating the lifecycle tracking gap that ImpactDeck is built on?

---

## #10 — AgentAudit  ·  69/100  ·  DECLINED
First added: 2026-09-25 | Last updated: 2026-10-02 | Score delta this week: −2

> Scan every MCP server your agents talk to — find the privilege-escalation risks before you ship to production.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — CLI scanner + CVE check + scope classification + GitHub Action; OSS-first is the right distribution; achievable in 3 months)
- Value Clarity:       14/20  (unchanged — "2,000+ npm MCP packages with zero dedicated security scanning" is self-evident to an engineering lead who has installed 10 of them)
- Market Timing:       15/20  (−2 — Cisco MCP Scanner and general MCP Security Scanner referenced in practitioner blogs; OSS scanners appearing in the space; first-mover advantage narrowing but paid SaaS tier still unbuilt)
- B2B Monetisation:    14/20  (unchanged — $149–399/month for teams that need CI gate + dashboard + scheduled rescans; free CLI is PLG engine)
- Pull Factor:         11/20  (unchanged — security community shares tools via HN, eng Twitter, and #security Slack; after a CVE in a widely-used MCP package the category becomes immediately viral)

**Strengths:**
- 2,000+ npm MCP packages with no dedicated security tooling remains confirmed; Cisco and generic scanners are mentioned but without a dedicated SaaS product layer.
- Free CLI scan creates viral PLG: engineering leads share "AgentAudit found a privilege escalation in tool X" on LinkedIn/Twitter.
- GitHub Action CI gate creates stickiness: once in the pipeline, removal requires an explicit decision.

**Risks:**
- Cisco MCP Scanner and other OSS scanners could cover the free CLI use case, leaving only the dashboard/CI gate as the paid differentiator — a thinner wedge.
- Anthropic or Cursor shipping native MCP security audit in their IDE would immediately capture the dev-tools segment.
- The MCP security scanning problem is well-understood by security researchers — a well-funded OSS project could commoditize the scanner before a paid tier gains traction.

**Verdict:** Keep for this run (protected by < 2-week rule). Re-evaluate next run against Cisco MCP Scanner scope and Anthropic/Cursor native security features.

### The Pitch
**Problem:** The MCP ecosystem has grown from fewer than 200 npm packages to over 2,000 in six months. Each package is a potential tool-injection surface: a malicious or misconfigured MCP server can instruct an agent to execute arbitrary tool calls, escalate privileges, or exfiltrate data through legitimate-looking tool schemas. Yet there is no dedicated security scanner for MCP packages — the same tools a developer installs in Cursor, Claude Code, or VS Code to give agents file system access, database access, or API access are deployed with no CVE check, no scope classification, and no audit of whether the permissions the server requests match what the tool actually needs.

**Solution:** AgentAudit is a CLI scanner and CI gate for MCP packages. Run `agentaudit scan <server-url>` before connecting an MCP server: it checks the package against CVE databases, classifies the scope of permissions requested (read-only vs write vs system), flags mismatches between declared tool descriptions and actual permission requirements, and produces a risk score. The GitHub Action fails the PR if a newly-connected MCP server has unreviewed permissions. The SaaS dashboard tracks all MCP servers connected in the org with their scan history and approval status.

**Target customer:** Engineering lead / security engineer at a 10–200 person company deploying AI agents via MCP. Buyer: CTO/CISO. Users: platform engineers deploying agents in development. Particularly relevant for companies in regulated industries (fintech, healthcare, legaltech) where agent tool access to customer data creates compliance exposure.

**Why now:** The MCP ecosystem grew 10× in 6 months as Claude Desktop, Cursor, VS Code, Windsurf, and Claude Code all standardized on MCP. Every company deploying agents is installing MCP packages with the same due-diligence gap — no CVE check, no permission audit. The first major MCP-based security incident will make AgentAudit the obvious tool to install retroactively.

**Why they buy without being sold to:** An engineering lead who installs AgentAudit on their existing MCP stack and finds that 3 of their 12 connected servers request filesystem write access that none of their workflows require — and one of them has a known CVE in its dependency tree — ships the GitHub Action that day.

**Revenue model:** Free CLI (unlimited local scans, no dashboard, no CI gate). $149/month (GitHub Action CI gate + org-level MCP server registry + 30-day scan history). $299/month (+ scheduled rescans + Slack alerts on new CVEs for connected servers + SSO). $399/month (+ API + custom rule library + SOC2-ready audit log export). Annual −2 months.

**Unfair advantage:** First dedicated MCP security scanner (not a generic API gateway or OSS dependency checker); MCP-specific permission scope classification (knows what "filesystem write" means in the MCP tool schema context); GitHub Action as the stickiest PLG mechanism in developer tooling.

### Solo Build Plan
1. Weeks 1–3: MCP package scanner (CVE check via OSV.dev, scope classification engine, permission-vs-description mismatch detection); CLI with `scan` and `report` commands; JSON and human-readable output.
2. Weeks 4–5: GitHub Action (fail PR on high-severity findings, comment with scan summary); OSS launch on GitHub.
3. Weeks 6–7: SaaS dashboard (org MCP server registry, scan history, approval workflow); Slack alert on new CVE for a connected server.
4. Weeks 8–9: Stripe; free tier gating; Hacker News launch.
5. Weeks 10–12: Pilot 5 AI-native companies; "AgentAudit found X in production" case study template.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-02
**Strongest part:** The GitHub Action CI gate creates the most durable PLG moat in developer security tooling — once in the pipeline, it stays.
**Open question:** What is the scope of Cisco's MCP Scanner, and does it provide a free CLI that covers AgentAudit's free-tier use case?

---

## Removed this run
| Entry | Last score | Reason |
|-------|------------|--------|
| RuleFlow | 71 | Canarie's Radar module confirmed to monitor federal/state regulatory changes, filter by product/jurisdiction, and trigger policy reviews — directly covering RuleFlow's core horizon-scanning differentiator; displaced by higher-scoring new entries at equal total score |
| IntegSecPack | 68 | Vanta Customer Trust Agent launched with 95% acceptance rate on AI-agent security questionnaires; Vanta accelerating toward full AI-agent compliance coverage; kill timeline shortened to < 3 months |
| ChurnDetect | 62 | Zendesk QA Spotlight confirmed (June 2026) to analyze 100% of support interactions for account-level churn risk prediction; the open question from Run 12 is answered — Zendesk now explicitly does account-level churn detection from support conversations |
