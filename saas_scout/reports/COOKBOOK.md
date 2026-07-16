# SaaS Opportunity Cookbook
Last updated: 2026-07-16 (R2 blind-spot run) | Entries: 10/10

> R2 note: This run deliberately overweighted community, launch, job, OSS, and boring-vertical sources to correct concentration risk from R1 (Techaisle/BigIdeasDB + competitor SEO).

---

## #1 — DentPay  ·  77/100  ·  NEW
First added: 2026-07-16 | Last updated: 2026-07-16 | Score delta this week: —

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (CSV/API ingest from Open Dental + Dentrix reports; rule engine for % splits, lab fees, write-offs; approval PDF — no need to become a full PMS)
- Value Clarity:       17/20  ("4–5 hours of month-end pay math → 20-minute approve" — office managers already do this ritual; Samera documents the UK version of the same pain)
- Market Timing:       15/20  (Samera AI owns UK Dentally/Xero; US practices still export Open Dental Provider Payroll to Excel; Gusto does payroll deposit, not OD production reconciliation)
- B2B Monetisation:    16/20  ($149–299/month per practice vs. overpay risk Samera cites at £25K–£60K/year recovered; US practices already pay for Dental Intelligence-class tools)
- Pull Factor:         13/20  (dental Facebook groups + local study clubs refer tools; less viral than eng Twitter, strong peer density)

**Strengths:**
- Blind-spot source: Indie/boring-vertical thesis + Open Dental's own docs admit offices use Provider Payroll exports for % pay — the glue layer is still spreadsheets
- UK Samera validates category; US Open Dental/Dentrix beachhead is under-served by UK-first tools
- Sticky once pay rules are configured (switching risks a wrong paycheck)

**Risks:**
- Open Dental may deepen native payroll math; Dental Intelligence / Dentrix add-ons encroach
- Dental sales are relationship-heavy; solo founder needs advisor credibility
- Lab-fee and write-off edge cases dominate support load

**Verdict:** Beachhead = US Open Dental practices with 2–8 providers on production % pay; CSV-first, API second.

### The Pitch

**Problem:** US dental practices paying associates and hygienists on production still spend hours each pay period exporting Open Dental or Dentrix reports, pasting into Excel, applying lab fee splits, card fees, and write-off adjustments, then hoping the spreadsheet matches the contract. Open Dental's Provider Payroll report helps but is not a pay engine. Samera AI automated this for UK Dentally+Xero stacks; Gusto can deposit pay but does not reconcile OD production rules. The Friday spreadsheet remains the system of record for thousands of US practices.

**Solution:** DentPay connects (or imports) Open Dental / Dentrix production and income reports, applies per-provider pay rules once, flags anomalies before payout, and exports an approval pack to Gusto/ADP/payroll. Office managers review exceptions; they do not rebuild formulas.

**Target customer:** Office manager / practice owner at a 1–3 location US dental practice on Open Dental or Dentrix with associates or hygienists on production splits. Buyer: owner or office manager. Users: office manager + accountant.

**Why now:** Production-based pay is still the norm; AI made rule engines cheap; UK tools proved willingness to pay; US PMS vendors have not productized the reconciliation layer.

**Why they buy without being sold to:** An office manager who just spent Sunday fixing a hygienist underpay uploads last month's OD export, sees the same pay total with three flagged lab-fee mismatches, and refuses to go back to Excel.

**Revenue model:** $149/month (1 location, up to 5 providers). $249/month (1 location, unlimited providers + lab invoice matching). $399/month (multi-location). 30-day trial. CPA/bookkeeper referral 15%.

**Unfair advantage:** US Open Dental/Dentrix rule templates + anomaly library become switching costs; dental study-club distribution PE roll-ups cannot easily copy at $149.

### Solo Build Plan
1. Weeks 1–3: Open Dental Provider Payroll CSV ingest; rule builder (% production, lab %, write-offs); pay summary PDF.
2. Weeks 4–5: Anomaly flags; side-by-side vs. last month; Gusto CSV export.
3. Weeks 6–7: Dentrix export path; multi-provider approval workflow.
4. Weeks 8–9: Stripe billing; practice onboarding with sample OD files.
5. Weeks 10–12: Pilot 8 practices via dental Facebook groups / local OD user groups.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-07-16
**Strongest part:** Concrete monthly ritual + clear US/UK competitive asymmetry.
**Open question:** Will practices trust a solo tool with paycheck math without a CPA partnership from day one?

---

## #2 — MatchFlow  ·  75/100  ·  IMPROVED
First added: 2026-06-19 | Last updated: 2026-07-16 | Score delta this week: +2

> The only bookkeeping copilot built for bookkeepers managing multiple clients — not for clients managing their own books.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged)
- Value Clarity:       16/20  (unchanged)
- Market Timing:       16/20  (+1 — Upwork shows 1,000+ live bookkeeping jobs; n8n Exact Online automation posts confirm buyers still hire humans/scripts for reconciliation)
- B2B Monetisation:    15/20  (unchanged)
- Pull Factor:         14/20  (+1 — IH/boring-SaaS discourse keeps elevating bookkeeping as durable niche)

**Strengths:** Botkeeper refugee + Upwork demand + B2B2B model still distinct from HelloBooks-as-ledger.
**Risks:** Growthy/Booke AI SEO; Intuit native AI.
**Verdict:** Keep Botkeeper-alternative SEO; Upwork freelancers are both competitors and a channel (white-label).

### The Pitch
*(Carried from prior run with timing update.)* Independent bookkeepers managing 5–20 QBO/Xero clients still burn 40–60 hours/month on reconciliation. Botkeeper is gone; Upwork still lists 1,000+ bookkeeping jobs — proof demand did not disappear into software. MatchFlow is the multi-client exception-queue copilot on top of existing ledgers.

**Target customer:** Independent bookkeepers, $80K–$300K revenue, 5–20 clients.
**Why now:** Refugee search + freelance demand + incomplete Booke/Growthy B2B2B fit.
**Revenue model:** $99 / $199 / $349 by client count.
**Unfair advantage:** Portfolio-native learning + bookkeeper communities.

### Solo Build Plan
Unchanged: QBO/Xero multi-client → exception queue → write-back → Bookkeeper Launch.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-07-16
**Strongest part:** Job-market demand corroborates refugee narrative without relying on Techaisle.
**Open question:** Can white-label for Upwork bookkeepers accelerate distribution?

---

## #3 — QuoteDock  ·  74/100  ·  DECLINED
First added: 2026-06-19 | Last updated: 2026-07-16 | Score delta this week: -1

> Compare 5 carrier quotes in 3 minutes instead of 3 hours — paste, upload, or forward anything.

### Score Breakdown
- Solo Buildability: 17/20 · Value Clarity: 16/20 · Market Timing: 12/20 (−1) · B2B Monetisation: 16/20 · Pull Factor: 13/20
**Key change:** No community falsification; FreightMynd/VelocityOS still TMS-first. Slight timing trim only.
**Verdict:** Hold zero-integration shipper wedge.

### The Pitch
*(Unchanged core.)* SMB shippers without TMS still normalize multi-format carrier quotes by hand. Forward email → 90-second comparison.
**Revenue:** $199 / $499 / $999.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-06-19
**Open question:** SMB downmarket move by FreightMynd/VelocityOS.

---

## #4 — SchemaWatch  ·  73/100  ·  DECLINED
First added: 2026-07-16 | Last updated: 2026-07-16 | Score delta this week: -1

> Know when a vendor API breaks your integration — before your customers do.

### Score Breakdown
- Solo Buildability: 16/20 · Value Clarity: 15/20 · Market Timing: 14/20 (−1) · B2B Monetisation: 14/20 · Pull Factor: 14/20
**Key change:** MCP observability noise (Spanly, mcpsnoop, MintMCP) raises "another watcher" fatigue; core third-party REST/OpenAPI wedge still distinct.
**Verdict:** Stay ruthlessly on vendor OpenAPI/response-shape drift — do not become an MCP gateway.

### The Pitch
*(Unchanged core.)* Specway-class silent breaks; GitHub Action canary for custom connectors.
**Revenue:** Free / $79 / $149 / $249.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-07-16
**Open question:** DIY cron+diff vs. paid willingness.

---

## #5 — MCPLens  ·  73/100  ·  NEW
First added: 2026-07-16 | Last updated: 2026-07-16 | Score delta this week: —

> Wireshark for your team's MCP servers — share the hung call, not the guesswork.

### Score Breakdown
- Solo Buildability:   15/20  (wrap mcpsnoop-class proxy; hosted session store; share links; CI check — feasible; do not build full enterprise gateway)
- Value Clarity:       15/20  (Show HN mcpsnoop: developers instantly get "see real Cursor↔MCP traffic"; team share link is obvious)
- Market Timing:       16/20  (mcpsnoop Show HN + TechTimes July 2026; Inspector cannot see production client path; Spanly exists but focuses SDK metrics, not session Wireshark UX)
- B2B Monetisation:    13/20  ($49–149/month for MCP server authors and platform teams; eng-tool ACV)
- Pull Factor:         14/20  (HN/Show HN native distribution; Cursor/Claude Code communities)

**Strengths:**
- Blind-spot source: primary Show HN + GitHub (kerlenton/mcpsnoop) — not analyst blog
- Clear gap vs. MCP Inspector (wrong data path) and vs. enterprise gateways (MintMCP/Obot/Navil overkill for 5-person teams)
- CI mode (`check` hung/malformed frames) is a natural paid gate

**Risks:**
- Spanly/MCP Cloud/MCPBay already monetizing MCP observability
- OSS mcpsnoop may add hosted tier and own the category
- Security optics of proxying tool traffic

**Verdict:** Hosted session replay + team share + CI for MCP server authors — not another enterprise control plane.

### The Pitch

**Problem:** When Cursor or Claude Code misbehaves with an MCP server — silent skip, hung tool, wrong capability negotiation — developers cannot see the real client↔server frames. MCP Inspector connects as its own client. Show HN's mcpsnoop (July 2026) proved demand for a transparent proxy, but it is local CLI. Teams cannot share a hung session with a teammate or fail CI on malformed frames without building hosting themselves. Enterprise gateways (MintMCP, Obot, Navil) solve SOC2 fleets, not a three-person MCP startup.

**Solution:** MCPLens is hosted Wireshark-for-MCP. Run a one-line shim (or connect our cloud relay), capture live sessions, share a link, replay a call, and fail CI on hung/invalid frames. Built for MCP server authors and small platform teams shipping tools into Cursor/Claude Code.

**Target customer:** Founders/eng leads at 2–20 person companies building MCP servers or internal MCP toolchains. Buyer: eng lead. Users: anyone debugging agent tool calls.

**Why now:** MCP is the de facto tool bus in mid-2026; debugging moved from "is the model dumb?" to "what did the tool actually return?"; Show HN validated the primitive this month.

**Why they buy without being sold to:** After a customer Slack says "your MCP hangs in Cursor," the author pastes an MCPLens session link showing the exact pending tool call — and upgrades for CI so it never ships again.

**Revenue model:** Free: 3 local-import sessions/week. $49/month (solo, 30-day retention). $99/month (team share links). $149/month (CI seats + SSO). Annual −2 months.

**Unfair advantage:** Session-first UX branded for Cursor/Claude Code authors; CI check becomes the default GitHub Action in MCP boilerplates.

### Solo Build Plan
1. Weeks 1–2: Hosted ingest of mcpsnoop-compatible session export; web TUI replay.
2. Weeks 3–4: Live relay option; shareable session URLs; redaction of secrets.
3. Weeks 5–6: `mcplens check` GitHub Action; Slack alert on hung calls.
4. Weeks 7–8: Team workspace; Stripe; docs aimed at MCP authors.
5. Weeks 9–12: Launch Show HN + Cursor forum; dogfood on 3 open-source MCP servers.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-07-16
**Strongest part:** Grounded in a real Show HN primitive, not a survey label.
**Open question:** Does Spanly or mcpsnoop.cloud ship the hosted tier before MCPLens reaches habit?

---

## #6 — DataReady  ·  72/100  ·  DECLINED
First added: 2026-07-16 | Last updated: 2026-07-16 | Score delta this week: -3

> Make your messy SaaS data safe and usable for AI agents — before the first hallucination.

### Score Breakdown
- Solo Buildability: 14/20 · Value Clarity: 16/20 · Market Timing: 15/20 (−2) · B2B Monetisation: 14/20 (−1) · Pull Factor: 13/20
**Key change:** MCP gateway + PrivacyPal/ShadowLock densification from OSS/community week; enablement wedge still real but noisier.
**Verdict:** Keep "agent fuel prep" not blocker positioning.

### The Pitch
*(Core unchanged.)* HubSpot/Zendesk → redaction + agent-ready endpoint.
**Revenue:** $199 / $399 / $599.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-07-16
**Open question:** Redaction trust without a services team.

---

## #7 — EquineField  ·  72/100  ·  IMPROVED
First added: 2026-07-16 | Last updated: 2026-07-16 | Score delta this week: +2

> Practice software built for solo ambulatory equine vets — offline SOAP, barn billing, sync later.

### Score Breakdown
- Solo Buildability: 11/20 · Value Clarity: 16/20 · Market Timing: 15/20 (+1) · B2B Monetisation: 15/20 · Pull Factor: 15/20 (+1)
**Key change:** IH/LaunchKit "boring vertical" discourse + r/HVAC-style community advice ("find the subreddit") reinforces distribution path; StableTrack gap still open vs. Vetspire HOOF hospitals.
**Verdict:** MVP ruthlessly offline SOAP + charges + sync.

### The Pitch
*(Core unchanged.)* Solo ambulatory equine; offline-first; multi-owner invoices.
**Revenue:** $149 / $249 / $299.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-07-16
**Open question:** Non-vet founder trust.

---

## #8 — SpecDrift  ·  69/100  ·  DECLINED
First added: 2026-07-16 | Last updated: 2026-07-16 | Score delta this week: -2

> Catch when your AI-generated code diverges from your spec — before the architecture review does.

### Score Breakdown
- 15 / 13 / 14 (−1) / 13 / 14 (−1)
**Key change:** Community drift CLIs + Kiro hooks continue; category still early.
**Verdict:** Team dashboard + MCP self-check or lose to free CLIs.

### Critic's Assessment
**Rating:** 7/10 | **Open question:** AWS native drift feature.

---

## #9 — ArticleShield  ·  68/100  ·  DECLINED
First added: 2026-07-10 | Last updated: 2026-07-16 | Score delta this week: -3

> Ship Article 50 technical compliance — C2PA, disclosures, and an audit trail — as an SDK, not a PDF checklist.

### Score Breakdown
- 14 / 15 (−1) / 13 (−1) / 14 (−1) / 12
**Key change:** Deadline ~17 days; checklist land-grab complete; technical SDK still the only survivable angle.
**Verdict:** Engineering SDK or exit after Aug 2.

### Critic's Assessment
**Rating:** 6/10 | **Open question:** Post-deadline enforcement demand.

---

## #10 — SaaSScope  ·  67/100  ·  DECLINED
First added: 2026-07-10 | Last updated: 2026-07-16 | Score delta this week: -3

> See every SaaS tool your team uses, what each costs, and which seats you're wasting — without enterprise bloat.

### Score Breakdown
- 15 / 14 (−1) / 11 (−1) / 14 (−1) / 13
**Key change:** SMB SaaS management still crowded (Substly/Primo/Inventoria); free-scan PLG only remaining wedge.
**Verdict:** Niche hard (GW agencies) or lose seat next run.

### Critic's Assessment
**Rating:** 6/10 | **Open question:** Defensible niche left?

---
