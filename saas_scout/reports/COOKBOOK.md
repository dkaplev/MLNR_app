# SaaS Opportunity Cookbook
Last updated: 2026-07-25 | Entries: 10/10

> R3 note: Launch-canary heavy. EquineField removed (StableTrack ships the wedge). MCPLens removed (Spanly hosted+sidecar). SchemaWatch cut hard (Specway third-party OpenAPI monitoring). Growthy compresses MatchFlow. DentPay still #1 (Samera UK-only; OD docs still Excel path).

---

## #1 — DentPay  ·  79/100  ·  IMPROVED
First added: 2026-07-16 | Last updated: 2026-07-25 | Score delta this week: +2

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — CSV-first rule engine still the right MVP)
- Value Clarity:       18/20  (+1 — OM ritual remains self-evident; live dentpay.tech LP sharpens the one-liner)
- Market Timing:       16/20  (+1 — Jul 2026 reconfirm: OD Provider Payroll docs still point offices at production exports for % pay; Samera AI still Dentally/SOE+Xero UK, not US OD/Dentrix)
- B2B Monetisation:    16/20  (unchanged — $149–399/practice)
- Pull Factor:         13/20  (unchanged — study clubs / dental FB; not eng-Twitter viral)

**Strengths:**
- Category validated by Samera UK; US Open Dental/Dentrix beachhead still open on launch canary
- Sticky once pay rules configured (wrong-paycheck switching cost)
- Founder GTM asset exists (dentpay.tech) without changing market facts

**Risks:**
- Dental Intelligence / PMS vendors could deepen native pay math
- Relationship-heavy sales; CPA/advisor trust needed
- Lab/write-off edge cases dominate support

**Verdict:** Stay #1. Beachhead = US OD practices, 2–8 providers on production %, CSV-first.

### The Pitch
**Problem:** US dental practices paying associates/hygienists on production still spend hours each pay period exporting Open Dental or Dentrix reports, pasting into Excel, applying lab fees, write-offs, and card-fee rules, then hoping the spreadsheet matches the contract. Open Dental’s Provider Payroll report is raw material, not a pay engine. Samera automated this for UK Dentally+Xero; Gusto deposits pay but does not reconcile OD production rules.

**Solution:** DentPay imports OD/Dentrix production exports, applies per-provider pay rules once, flags anomalies before payout, and exports an approval pack to Gusto/ADP. Office managers review exceptions; they do not rebuild formulas.

**Target customer:** Office manager / owner at 1–3 location US dental practice on Open Dental or Dentrix with associates or hygienists on production splits.

**Why now:** Production % pay still the norm; UK tools proved willingness to pay; US PMS vendors have not productized the reconciliation layer.

**Why they buy without being sold to:** An OM who spent Sunday fixing a hygienist underpay uploads last month’s OD export, sees the same total with three flagged lab mismatches, and refuses to go back to Excel.

**Revenue model:** $149 / $249 / $399 per practice. 30-day trial. CPA referral 15%.

**Unfair advantage:** US OD/Dentrix rule templates + anomaly library; study-club distribution PE roll-ups won’t chase at $149.

### Solo Build Plan
1. Weeks 1–3: OD Provider Payroll CSV ingest; rule builder; pay summary PDF.
2. Weeks 4–5: Anomaly flags; vs last period; Gusto CSV export.
3. Weeks 6–7: Dentrix path; multi-provider approval.
4. Weeks 8–9: Stripe; sample-file onboarding.
5. Weeks 10–12: Pilot 8 practices via dental groups / OD user groups.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-07-25
**Strongest part:** Concrete ritual + US/UK competitive asymmetry still holds on canary.
**Open question:** Will practices trust a solo tool with paycheck math without a CPA partnership from day one?

---

## #2 — DataReady  ·  74/100  ·  IMPROVED
First added: 2026-07-16 | Last updated: 2026-07-25 | Score delta this week: +2

> Make your messy SaaS data safe and usable for AI agents — before the first hallucination.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged)
- Value Clarity:       16/20  (unchanged — “don’t feed dirty CRM to the agent”)
- Market Timing:       17/20  (+2 — Anthropic 2026 State of AI Agents: 46% cite integration as top barrier, 42% data quality; Techaisle “Data Trust & Sanitization for AI” remains #2 IT challenge)
- B2B Monetisation:    14/20  (unchanged — $199–599)
- Pull Factor:         13/20  (unchanged)

**Strengths:** Enablement wedge (“agent fuel”) not blocker; mid-market feels integration tax harder than enterprises with platform teams.
**Risks:** MCP gateways / PrivacyPal-class tools densify; redaction trust without services.
**Verdict:** Keep “prep HubSpot/Zendesk for agents” — do not become another MCP control plane.

### The Pitch
*(Core carried; timing updated.)* SMB/mid-market teams want agents on CRM/support data but stall on dirty PII-laden exports. DataReady redacts, shapes, and exposes an agent-ready endpoint so pilots stop dying at plumbing.

**Target customer:** Ops/eng lead at 20–200 person B2B SaaS or services firm running HubSpot/Zendesk + first agent pilot.  
**Revenue:** $199 / $399 / $599.  
**Unfair advantage:** Vertical connectors + redaction presets that ship in a week, not a platform RFP.

### Solo Build Plan
Unchanged: HubSpot/Zendesk connectors → PII redaction → agent endpoint → pilot 5 teams.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-07-25
**Strongest part:** Grounded in Anthropic integration/data-quality numbers, not generic “AI opportunity.”
**Open question:** Can a solo founder earn redaction trust without a services bench?

---

## #3 — QuoteDock  ·  73/100  ·  DECLINED
First added: 2026-06-19 | Last updated: 2026-07-25 | Score delta this week: -1

> Compare 5 carrier quotes in 3 minutes instead of 3 hours — paste, upload, or forward anything.

### Score Breakdown
- Solo Buildability:   17/20  (unchanged)
- Value Clarity:       16/20  (unchanged)
- Market Timing:       11/20  (−1 — FreightMynd/Wisor deepen forwarder quote automation; still TMS/forwarder-upmarket, not zero-integration SMB shipper, but category heat rises)
- B2B Monetisation:    16/20  (unchanged)
- Pull Factor:         13/20  (unchanged)

**Strengths:** Zero-integration shipper wedge still distinct from CargoWise-class AI.
**Risks:** Downmarket move by freight AI vendors; email-forward UX must stay dead simple.
**Verdict:** Hold paste/forward SMB shipper wedge; do not chase forwarder TMS.

### The Pitch
*(Core unchanged.)* SMB shippers without TMS still normalize multi-format carrier quotes by hand. Forward email → 90-second comparison.  
**Revenue:** $199 / $499 / $999.

### Critic's Assessment
**Rating:** 8/10 | **Last critique:** 2026-07-25
**Open question:** Will FreightMynd-class vendors ship a $199 shipper SKU?

---

## #4 — PromptFence  ·  71/100  ·  NEW
First added: 2026-07-25 | Last updated: 2026-07-25 | Score delta this week: —

> Stop Shadow AI leaks — approve which prompts and tools staff can use, without enterprise DLP.

### Score Breakdown
- Solo Buildability:   15/20  (browser extension + workspace allowlist + audit log; do not build full DLP)
- Value Clarity:       15/20  (“ex-employee pasted customer list into ChatGPT” is a board-level sentence)
- Market Timing:       15/20  (Techaisle 2026: Governance of Shadow AI as top IT challenge; CSA/offboarding blogs stress AI app access; enterprises have DLP, 20–100 person firms have a Google Doc policy)
- B2B Monetisation:    14/20  ($149–399/mo for 25–100 seats; security budget exists post-scare)
- Pull Factor:         12/20  (peer share after an incident; otherwise outbound to ops/IT)

**Strengths:**
- Clear gap between “enterprise DLP” and “nothing”
- Ties to offboarding + SaaS sprawl without competing as full SaaS management
- Solo-feasible as allowlist + logging first

**Risks:**
- Nightfall/Harmonic/enterprise DLP downmarket
- Extension-distribution and false-positive fatigue
- Policy product can feel like “nanny software”

**Verdict:** Beachhead = 20–80 person companies with Google/Microsoft workspace + unmanaged ChatGPT/Claude usage.

### The Pitch

**Problem:** Staff at small companies paste customer data, contracts, and source into ChatGPT/Claude/Copilot with no inventory of tools, no approval path, and no audit trail. Enterprise DLP is priced and complex for a 40-person firm. IT “policies” live in a Notion page nobody reads. Techaisle’s 2026 SMB IT challenges elevate Shadow AI governance alongside data trust — the scare is real; the SMB product is not.

**Solution:** PromptFence is a lightweight Shadow AI control plane: discover AI tools in use, allow/deny by team, require a one-click acknowledgment for risky paste patterns, and keep an exportable audit log. Browser extension + admin console — not a network appliance.

**Target customer:** Ops lead / fractional IT at 20–80 person B2B firms (agencies, SaaS, professional services). Buyer: founder/ops. Users: all staff via extension.

**Why now:** Agent and chatbot usage exploded; boards ask “where did our data go?”; enterprise vendors ignore sub-100 headcount.

**Why they buy without being sold to:** After one Slack incident (“did we paste the customer CSV into ChatGPT?”), the founder installs PromptFence the same afternoon and requires allowlisted AI apps only.

**Revenue model:** $149/mo (up to 25 seats). $249/mo (100 seats + SSO). $399/mo (audit export + SIEM webhook). 14-day trial.

**Unfair advantage:** Incident-shaped onboarding (“paste your last scare”) + templates for agencies/SaaS that enterprise DLP won’t bother with.

### Solo Build Plan
1. Weeks 1–3: Chrome extension allowlist for ChatGPT/Claude/Gemini; admin dashboard.
2. Weeks 4–5: Paste-risk heuristics; acknowledgment modal; audit CSV.
3. Weeks 6–7: Google Workspace / M365 group sync; team policies.
4. Weeks 8–9: Stripe; incident-report PDF for leadership.
5. Weeks 10–12: Pilot 10 agencies via ops Slack communities.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-07-25
**Strongest part:** Names a board-scary job enterprise tools overshoot.
**Open question:** Will staff revolt / sideload, making the product shelfware?

---

## #5 — ArticleShield  ·  71/100  ·  IMPROVED
First added: 2026-07-10 | Last updated: 2026-07-25 | Score delta this week: +3

> Ship Article 50 technical compliance — C2PA, disclosures, and an audit trail — as an SDK, not a PDF checklist.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged — SDK + middleware; checklist apps are noise)
- Value Clarity:       15/20  (unchanged for eng buyers)
- Market Timing:       16/20  (+3 — Art. 50 applies 2 Aug 2026; Commission transparency guidelines published 20 Jul 2026; high-risk deferred but Art. 50 not postponed; ~8 days to force date)
- B2B Monetisation:    14/20  (unchanged)
- Pull Factor:         12/20  (unchanged — compliance buyers; eng Twitter for SDK)

**Strengths:** Hard deadline still real; technical marking (C2PA) is the only survivable wedge vs checklist land-grab.
**Risks:** Post-deadline demand may cliff; Adobe/platform native marking; solo support load.
**Verdict:** Engineering SDK only — exit or niche hard after Aug–Dec transition window.

### The Pitch
*(Core unchanged; deadline urgency updated.)* Generative product teams need machine-readable marking and disclosure evidence, not another PDF checklist. ArticleShield is the drop-in C2PA/disclosure SDK + audit trail for eng teams shipping EU-facing AI content before/at Art. 50.

**Revenue:** $199 / $499 / $999 by volume.  
**Open question:** Post-deadline enforcement intensity.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-07-25
**Strongest part:** Deadline + Commission guidelines are concrete timing.
**Open question:** Will buyers pay after 2 Aug, or only in the panic week before?

---

## #6 — InventoryGrid  ·  70/100  ·  NEW
First added: 2026-07-25 | Last updated: 2026-07-25 | Score delta this week: —

> Replace the inventory spreadsheet for wholesalers who can’t afford NetSuite — counts, PO alerts, stockouts.

### Score Breakdown
- Solo Buildability:   15/20  (SKU list, locations, PO alerts, CSV import; not a full WMS)
- Value Clarity:       16/20  (BigIdeasDB 2026: spreadsheet inventory among top SMB pains; Upwork freelancers hired to “fix the sheet”)
- Market Timing:       13/20  (chronic pain, not a new regulation — window is “still Excel” not “hot AI”)
- B2B Monetisation:    14/20  ($149–299/mo vs stockout/overbuy cost)
- Pull Factor:         12/20  (trade groups; less viral)

**Strengths:** Spreadsheet incumbent = easy switch story; clear ROI on one stockout avoided.
**Risks:** inFlow/Sortly/Katana mid-market; scope creep into full WMS kills solo build.
**Verdict:** Ruthless MVP: multi-location counts + reorder alerts + CSV — refuse MRP features.

### The Pitch

**Problem:** Small wholesalers and light manufacturers (5–40 people) track stock in Google Sheets. Counts drift, reorder points are tribal knowledge, and Upwork freelancers get hired to rebuild the sheet after every mess. Enterprise WMS is absurd; “simple” apps either lack multi-location or turn into mini-ERPs.

**Solution:** InventoryGrid is the inventory spreadsheet that won’t rot: SKUs, locations, cycle counts, reorder alerts, and PO export. Import from CSV; no warehouse robot promises.

**Target customer:** Ops owner at wholesale / light manufacturing / specialty retail, 5–40 staff, 200–5,000 SKUs. Buyer: owner/ops. Users: warehouse lead + bookkeeper.

**Why now:** SMB cost pressure (Techaisle inflation/costs) makes stockouts and overbuy painful; AI hype hasn’t fixed the sheet.

**Why they buy without being sold to:** After a missed wholesale order from a “row that was wrong,” the owner uploads the sheet and sets reorder points the same week.

**Revenue model:** $149/mo (1 location). $249/mo (3 locations). $299/mo (unlimited locations + barcode). Annual −2 months.

**Unfair advantage:** Vertical templates (e.g. specialty food, parts) + “sheet import in 10 minutes” onboarding.

### Solo Build Plan
1. Weeks 1–3: SKU/location model; CSV import; on-hand adjustments.
2. Weeks 4–5: Reorder points; email/Slack alerts; low-stock report.
3. Weeks 6–7: PO draft export; simple barcode phone scan.
4. Weeks 8–9: Stripe; sample datasets by vertical.
5. Weeks 10–12: Pilot 8 wholesalers via trade Facebook groups.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-07-25
**Strongest part:** Spreadsheet replacement clarity.
**Open question:** Can you win against Sortly/inFlow on price alone without a vertical wedge?

---

## #7 — MatchFlow  ·  68/100  ·  DECLINED
First added: 2026-06-19 | Last updated: 2026-07-25 | Score delta this week: -7

> The only bookkeeping copilot built for bookkeepers managing multiple clients — not for clients managing their own books.

### Score Breakdown
- Solo Buildability:   14/20  (unchanged)
- Value Clarity:       15/20  (−1 — Growthy now owns the “13 of 247 need you” sentence in market SEO)
- Market Timing:       12/20  (−4 — Growthy ships multi-client triage + per-client memory; Booke overlay; Botkeeper gone but category filled)
- B2B Monetisation:    14/20  (−1 — price pressure vs Growthy $99–199)
- Pull Factor:         13/20  (−1)

**Strengths:** Demand still real (Upwork bookkeeping volume); white-label freelancer angle.
**Risks:** Growthy is the default “Botkeeper alternative” narrative now; Intuit native AI.
**Verdict:** Only keep if white-label/Upwork distribution is explicit — otherwise next run exit.

### The Pitch

**Problem:** Independent bookkeepers managing 5–20 QBO/Xero clients still burn dozens of hours on categorization and reconciliation. Botkeeper shut down; the job did not. Growthy and Booke now claim the AI overlay — but freelancers on Upwork still sell manual cleanup, proving incomplete coverage and price/friction gaps for solo bookkeepers.

**Solution:** MatchFlow stays the multi-client exception-queue copilot with white-label packaging for freelance bookkeepers who cannot or will not join Growthy’s alpha constraints.

**Target customer:** Solo/small bookkeeping firms, $80K–$300K revenue, 5–20 clients — especially Upwork/white-label operators.

**Why now:** Refugee demand persists; Growthy invite/alpha constraints leave a messy long tail.

**Why they buy without being sold to:** A freelancer who lost Botkeeper and was waitlisted elsewhere needs a queue that works on their QBO exports this week.

**Revenue model:** $99 / $199 / $349 by client count. White-label +$50.

**Unfair advantage:** White-label + Upwork playbook, not another Growthy SEO clone.

### Solo Build Plan
1. Weeks 1–3: QBO CSV/API exception queue for 1 firm, multi-client switcher.
2. Weeks 4–5: Confidence scores; bulk approve; write-back.
3. Weeks 6–7: Xero path; white-label subdomain.
4. Weeks 8–9: Stripe; Upwork landing.
5. Weeks 10–12: 10 freelancer pilots.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-07-25
**Strongest part:** Honest about Growthy — survival is distribution, not feature parity.
**Open question:** Is white-label enough, or is the seat already gone?

---

## #8 — SpecDrift  ·  67/100  ·  DECLINED
First added: 2026-07-16 | Last updated: 2026-07-25 | Score delta this week: -2

> Catch when your AI-generated code diverges from your spec — before the architecture review does.

### Score Breakdown
- Solo Buildability: 15/20 · Value Clarity: 13/20 · Market Timing: 13/20 (−1) · B2B Monetisation: 13/20 · Pull Factor: 13/20 (−1)
**Key change:** Free drift CLIs + IDE hooks continue; paid team dashboard still the only monetizable layer.
**Verdict:** Team dashboard + CI gate or lose to free CLIs next run.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-07-25
**Open question:** AWS/Kiro native drift feature.

---

## #9 — SchemaWatch  ·  66/100  ·  DECLINED
First added: 2026-07-16 | Last updated: 2026-07-25 | Score delta this week: -7

> Know when a vendor API’s live responses change shape — even when they never publish OpenAPI.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — canary harness)
- Value Clarity:       14/20  (−1 — Specway now owns “OpenAPI broke” narrative)
- Market Timing:       12/20  (−2 — Specway third-party OpenAPI monitoring is explicit; must own runtime response canary)
- B2B Monetisation:    13/20  (−1)
- Pull Factor:         11/20  (−3 — MCP watcher fatigue spills into “another API watcher”)

**Strengths:** Runtime response-shape canary still distinct when vendors ship no OpenAPI.
**Risks:** Specway/Optic/Bump expand; DIY cron+diff.
**Verdict:** Reposition hard to “no-spec vendors / shadow JSON” or exit next run.

### The Pitch

**Problem:** Integrations break when a vendor changes a JSON field type or nests a key — often without a changelog or public OpenAPI. Specway-class tools watch published specs; many billing/legacy APIs never publish one. Teams learn from customer tickets.

**Solution:** SchemaWatch hits your recorded golden responses on a schedule, diffs live shapes, and alerts Slack before customers do. Built for the ugly APIs without docs.

**Target customer:** Eng lead at 5–50 person companies with 3+ brittle third-party connectors.

**Why now:** Agent and automation volume multiplies silent breaks; OpenAPI tooling doesn’t cover undocumented APIs.

**Why they buy without being sold to:** After one weekend firefight on a silent Stripe-adjacent or regional PSP change, the team adds canaries for every vendor.

**Revenue model:** Free / $79 / $149 / $249.

**Unfair advantage:** Fixture library for “no OpenAPI” vendors; GitHub Action canary pack.

### Solo Build Plan
1. Weeks 1–2: Capture golden response; scheduled fetch; JSON shape diff.
2. Weeks 3–4: Slack alerts; ignore rules; CI action.
3. Weeks 5–6: Multi-env; team workspace.
4. Weeks 7–8: Stripe; vendor fixture templates.
5. Weeks 9–12: Launch to integration-heavy indie SaaS.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-07-25
**Strongest part:** Honest reposition away from Specway’s OpenAPI lane.
**Open question:** Is “no OpenAPI” a big enough paid market?

---

## #10 — FlatToken  ·  65/100  ·  NEW
First added: 2026-07-25 | Last updated: 2026-07-25 | Score delta this week: —

> Predictable AI bills for SMBs — caps, alerts, and department chargeback without FinOps theater.

### Score Breakdown
- Solo Buildability:   15/20  (OpenAI/Anthropic usage APIs → budgets → Slack alerts)
- Value Clarity:       15/20  (Techaisle 2026: token-shock / AI cost unpredictability returns as #1 budget anxiety)
- Market Timing:       13/20  (real pain; Helicone/Langfuse/OpenAI dashboards already partial)
- B2B Monetisation:    12/20  ($99–249; race with free vendor dashboards)
- Pull Factor:         10/20  (finance shares screenshots; weak viral)

**Strengths:** CFO-friendly “no surprise bill” pitch; pairs with Shadow AI story.
**Risks:** Vendor native spend dashboards; was previously retired as TokenShock — only re-enter as thin wedge.
**Verdict:** Probation seat — department caps + Slack for non-eng SMBs, or drop next run.

### The Pitch
**Problem:** SMBs pilot ChatGPT/Claude APIs, then get a surprise invoice. Native dashboards are eng-centric; FinOps tools are enterprise.

**Solution:** FlatToken connects provider usage, sets hard/soft caps by team, Slack-alerts at 50/80/100%, and exports a chargeback CSV for finance.

**Target customer:** Finance + eng lead at 15–100 person companies spending $500–5,000/mo on LLM APIs.

**Revenue:** $99 / $149 / $249.

### Critic's Assessment
**Rating:** 5/10 | **Last critique:** 2026-07-25
**Open question:** Why won’t OpenAI’s own limits page kill this?

---

## Removed this run
| Entry | Last score | Reason |
|-------|------------|--------|
| EquineField | 72 → 48 | **StableTrack** ships offline ambulatory equine PMS (SOAP, barn billing, sync) at $199–299 — wedge closed |
| MCPLens | 73 → 62 | **Spanly** Show HN + hosted demo + language-agnostic sidecar — hosted Wireshark-for-MCP claimed |
| SaaSScope | 67 → 60 | Substly/Primo/AutoCISO/EasyRevoke densify SMB SaaS discovery + offboarding |
