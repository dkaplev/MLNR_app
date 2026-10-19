# SaaS Opportunity Cookbook
Last updated: 2026-10-19 | Entries: 10/10

> R7 note: Three exits. **TokenBill removed** — Ramp’s AI Token Spend (16 Jul 2026) already forecasts OpenAI, Anthropic, Gemini, and Cursor for finance. **BriefDesk removed** — Brief’s Weekly Brief already joins HubSpot, Stripe, and Linear. **FlowTrace removed** — last-seat kill-switch is now Countersign, AEGIS, and Helicone 429s, with no evidence anyone pays for a Zapier+OpenAI pause. **PactDesk**, **CallLedger**, and **BinderDesk** enter. **BreakWatch** rises because Optic was archived, not because a cheap “watch these vendors” SKU shipped. DentPay holds #1 (Onfolio, 17 Oct 2026, still finds no OD/Dentrix production-pay engine).

---

## #1 — DentPay  ·  80/100  ·  UNCHANGED
First added: 2026-07-16 | Last updated: 2026-10-19 | Score delta this week: —

> Turn Open Dental / Dentrix production exports into clean associate & hygienist pay — without the Friday spreadsheet.

### Score Breakdown
- Solo Buildability:   16/20  (unchanged — CSV-first rule engine)
- Value Clarity:       18/20  (unchanged — OM ritual self-evident)
- Market Timing:       17/20  (unchanged — Onfolio, 17 Oct 2026: Patriot, Gusto, OnPay, and ADP still do not reconcile production rules; OD documents an ADP time-card export, not a pay engine; Dentivize is still a $149/$399 KPI dashboard; Samera’s story is still UK associate pay)
- B2B Monetisation:    16/20  (unchanged)
- Pull Factor:         13/20  (unchanged — study clubs)

**Strengths:**
- Onfolio’s 17 Oct 2026 payroll roundup still cannot name a PMS-native production-pay integration for Dentrix or Eaglesoft. Open Dental’s ADP export is time cards, and it says semi-monthly periods are unsupported on ADP RUN.
- Dentivize remains analytics (production, collections, doctor take-home %) at $149/$399, not a paycheck calculator. dent-pay.com is a collections sync product, a different job.
- Sticky once pay rules are configured — a wrong paycheck is employer liability.

**Risks:**
- Dental Intelligence or Dentrix could deepen native pay math.
- A payroll vendor (Patriot already advertises hygienist production/commission pay) could add an OD CSV importer.
- Relationship-heavy sales; paycheck math needs a CPA-shaped proof.

**Verdict:** Hold #1. The US export-to-Excel path is still intact as of mid-October.

### The Pitch
**Problem:** US dental practices paying associates and hygienists on production still spend hours each pay period exporting Open Dental or Dentrix reports, pasting into Excel, applying lab fees, write-offs, and card-fee rules, then hoping the spreadsheet matches the contract. Open Dental's Provider Payroll report is raw material, not a pay engine. Samera automated this for UK dental groups; Gusto deposits pay but does not reconcile OD production rules. An October 2026 payroll review still could not confirm a Dentrix or Eaglesoft payroll integration, and none of the payroll providers it read name a dental practice-management system as a production-pay source.

**Solution:** DentPay imports OD/Dentrix production exports, applies per-provider pay rules once, flags anomalies before payout, and exports an approval pack to Gusto/ADP. Office managers review exceptions; they do not rebuild formulas.

**Target customer:** Office manager / owner at 1–3 location US dental practice on Open Dental or Dentrix with associates or hygienists on production splits.

**Why now:** Production % pay is still the norm. UK tools proved willingness to pay for associate-pay automation. US payroll vendors added time-card exports and commission fields, not the reconciliation layer.

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
**Strongest part:** Mid-October payroll roundups still describe production pay as a spreadsheet on top of Gusto, not a PMS feature.
**Open question:** Will practices trust a solo tool with paycheck math without a CPA partnership from day one?

---

## #2 — PactDesk  ·  76/100  ·  NEW
First added: 2026-10-19 | Last updated: 2026-10-19 | Score delta this week: —

> Send, sign, and update the DPA — and tell every signed customer when a subprocessor changes.

### Score Breakdown
- Solo Buildability:   17/20  (hosted PDF, email link, version log, public subprocessor page, notify-on-change; not a RoPA suite)
- Value Clarity:       18/20  (a German prospect who will not sign until the DPA is signed understands the product in one sentence)
- Market Timing:       15/20  (MicroGaps 2026: template generators stop at the PDF; €79 suites assume a compliance team; AI vendors keep adding subprocessors)
- B2B Monetisation:    14/20  ($99–$249/mo is the gap under a $2,000/mo stack bought for three EU customers)
- Pull Factor:         12/20  (founder communities forward the same “please sign our DPA” thread)

**Strengths:**
- The missing product is a signing portal plus an Article 28 subprocessor notice, not another privacy-policy generator.
- Iubenda and Termly sell templates. Dastra and similar suites start where a 3-to-20-customer founder does not live.
- Each new model vendor in the stack creates another notice. The list gets more valuable, not less.

**Risks:**
- DocuSign plus a Notion subprocessor page is “good enough” for many founders.
- A privacy-template vendor can add e-sign in a quarter.
- The buyer is price-sensitive; $249/mo has to replace a real hour-count, not a fear.

**Verdict:** Enter as the DPA file for indie B2B SaaS with a handful of EU customers. Do not build a GDPR platform.

### The Pitch
**Problem:** Indie B2B SaaS founders selling into Germany or France get asked for a signed Data Processing Agreement before the contract. They email a PDF, lose track of which version the next ten customers signed, and miss the GDPR Article 28 notice when they add a subprocessor. Template tools (Iubenda, Termly) generate the document. Suites such as Dastra assume a compliance team and start near €79/month with records of processing and DPIAs a three-customer founder does not need. One reported pattern is a founder paying about $2,000 a month in GDPR tooling for three EU customers.

**Solution:** PactDesk is the DPA file. The founder publishes one current DPA and a public subprocessor list. Each prospect gets a link, signs in the browser, and the signed PDF is stored against that customer. When the founder adds a subprocessor, every signed customer gets the notice. There is no RoPA, no DPIA builder, and no “AI compliance score.”

**Target customer:** Founder or ops lead at a 2–30 person B2B SaaS with 3–20 EU customers and no counsel on staff. Buyer: the founder who currently hunts for the last signed PDF. User: that same person.

**Why now:** EU customers ask for the DPA before they buy, and 2026 AI stacks add subprocessors faster than a Notion page stays current. The cheap tools stop at generation. The serious tools assume a DPO.

**Why they buy without being sold to:** The next EU prospect asks for the DPA on a Tuesday. The founder sends a PactDesk link instead of attaching a PDF, sees the signed copy land in the customer row, and stops keeping the tracker in email.

**Revenue model:** $99/mo (20 customers, email sign, subprocessor page). $149/mo (100 customers + change notices). $249/mo (custom DPA versions + CSV export for counsel). Annual −2 months. 14-day trial with a sample DPA.

**Unfair advantage:** The artifact is the signed-customer list tied to a subprocessor changelog. A template download does not know who must be notified.

### Solo Build Plan
1. Weeks 1–3: DPA upload, signer link, stored PDF, customer list.
2. Weeks 4–5: Public subprocessor page; “this changed” email to signed customers.
3. Weeks 6–7: Version history (which customer signed which DPA).
4. Weeks 8–9: Stripe; sample DPA onboarding.
5. Weeks 10–12: Pilot 8 indie SaaS founders via EU-selling communities.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-19
**Strongest part:** The buyer already loses deals on a missing signature, so the demo is “send the link,” not a framework lecture.
**Open question:** Will DocuSign plus a public subprocessor Notion page be good enough that nobody pays $99?

---

## #3 — CallLedger  ·  74/100  ·  NEW
First added: 2026-10-19 | Last updated: 2026-10-19 | Score delta this week: —

> A hash-chained log of every MCP tool call — metadata only — that an auditor can verify without seeing the prompt.

### Score Breakdown
- Solo Buildability:   14/20  (one-line server wrap, OTel spans, append-only hash chain, verify CLI; not a gateway)
- Value Clarity:       15/20  (“what did the agent do with this customer’s data on Tuesday?” is a real question; it still needs one sentence of setup)
- Market Timing:       17/20  (Databricks, 4 Sep 2026, traced silent MCP retries to about $499k/year in tokens; OTel gen-ai/mcp semconv says do not capture tool args by default; Langfuse/Helicone default to full content; ToolHive-class gateways are cluster-scale)
- B2B Monetisation:    16/20  ($249–$599/mo against a compliance block on shipping the agent)
- Pull Factor:         12/20  (incident write-ups travel in eng Slack; compliance buyers are quiet)

**Strengths:**
- The Databricks write-up is a concrete failure: seven MCP servers accepted loose JSON, agents retried silently, and the bill and the lost hours showed up later.
- Regulated teams cannot turn on trace tools that store raw tool arguments. The spec already says not to.
- A verify CLI is a solo-shaped artifact. A Kubernetes MCP gateway is not.

**Risks:**
- The official MCP SDK or a gateway ships metadata-only audit and the wedge closes.
- Teams that already run Langfuse with redaction will not switch.
- “Audit log” can sound like a feature of a bigger security product (PromptFence’s failure mode). Stay on the hash chain.

**Verdict:** Enter as the metadata-only MCP audit log for a 15–80 person product team. Do not build another trace UI.

### The Pitch
**Problem:** A team running an MCP server between a model and Jira, Drive, or internal tools cannot answer “what did the agent do with this customer’s data on Tuesday?” Langfuse, LangSmith, and Helicone capture prompts and tool results by default, which regulated buyers will not deploy. Arize-style instrumentation and the large MCP gateways (ToolHive, MCPJungle, context-forge) do not fit a 50-person product. Databricks described the failure mode on 4 Sep 2026: loose MCP servers accepted almost any JSON, agents retried silently, and the company put the waste near $499,000 a year in tokens plus about 12,000 engineering hours. OpenTelemetry’s gen-ai/mcp conventions, merged January 2026, say instrumentations should not capture tool arguments and results by default. The vendor default does the opposite.

**Solution:** CallLedger wraps the MCP server. Every tools/call, resources/read, and auth event becomes an OpenTelemetry span plus one hash-chained JSON record: tool name, timestamp, caller, argument hash, result hash, sequence number. Raw content stays off unless someone opts in. A verify CLI recomputes the chain. It does not proxy the model and it does not try to pause the agent.

**Target customer:** Eng lead plus the person who answers security questionnaires at a 15–80 person company shipping an MCP-backed agent into a regulated customer. Buyer: CTO or head of security. User: the engineer who owns the MCP server.

**Why now:** MCP moved from demo to production in 2026, the semantic conventions now exist, and a named incident made silent retries a finance problem. The tools that log everything are unsellable where the data is sensitive. The tools that govern a cluster are too big.

**Why they buy without being sold to:** A customer security review asks for the tool-call log. The team either scrambles through stdout or hands over a verify command and a hash chain. The second one is what they keep paying for.

**Revenue model:** $249/mo (one server, 90-day metadata retention, verify CLI). $399/mo (five servers + OTLP export). $599/mo (SSO + signed daily digest). Annual −2 months. 14-day trial on a sample server.

**Unfair advantage:** Default-off content plus a chain an auditor can recompute. Trace products would have to break their own default to copy it.

### Solo Build Plan
1. Weeks 1–3: Python and TypeScript wrap; metadata-only record; local verify CLI.
2. Weeks 4–5: OTLP export; daily signed digest.
3. Weeks 6–7: Opt-in redacted mode; retention controls.
4. Weeks 8–9: Stripe; “point at your MCP server” onboarding.
5. Weeks 10–12: Pilot 5 teams who already failed a security review for lack of a tool-call log.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-19
**Strongest part:** The buyer’s alternative is a trace tool they are not allowed to turn on.
**Open question:** Will the MCP SDK ship this hash chain before anyone pays for it?

---

## #4 — RuleFlow  ·  73/100  ·  UNCHANGED
First added: 2026-08-16 | Last updated: 2026-10-19 | Score delta this week: —

> New federal rules become a checklist and an evidence folder — not another unread PDF in Slack.

### Score Breakdown
- Solo Buildability:   13/20  (unchanged — FRTracker-class feed + tasks + evidence ZIP; legal review is the hard part)
- Value Clarity:       16/20  (unchanged — “this rule changed — here is what you must do by when”)
- Market Timing:       16/20  (unchanged — Yale JREG’s August 2026 rulemaking snapshot still treats FRTracker as the obligation primitive, not a workflow; CUBE’s mid-market Intel still has no public price as of an August 17 2026 check; no “send to Jira” layer found on the primitive)
- B2B Monetisation:    17/20  (unchanged)
- Pull Factor:         11/20  (unchanged)

**Strengths:**
- FRTracker is still cited as a research spine (deterministic obligations, proposed-vs-final diffs), including by Yale Journal on Regulation’s August 2026 review. The unpaid job remains owner, due date, evidence.
- CUBE and Ascent stay quote-only. Third-party ranges for this tier still start in five and six figures. A 4-person compliance team does not run that procurement.
- Traceable extraction is what an examiner will accept. A summary is not.

**Risks:**
- FRTracker, or a funded RegTech, adds the task export and the wedge collapses.
- Wrong obligation mapping is a liability. The product is monitoring, not advice.
- The number of community banks and small fintech lenders who will buy is smaller than the Federal Register makes it look.

**Verdict:** Hold. One vertical: US fintech lenders and community banks. Open question from August is still open.

### The Pitch
**Problem:** A four-person compliance team at a community bank or fintech lender tracks Federal Register changes in a shared spreadsheet and a Slack channel of PDFs. CUBE and AscentAI sell this to larger institutions and do not publish a price a small team can approve. FRTracker extracts individual must/shall obligations from primary documents and is still used as a research tool, including in the August 2026 academic rulemaking snapshot. When a final rule drops, nobody owns the checklist, and the exam asks for evidence that does not exist.

**Solution:** RuleFlow turns each relevant obligation into a task with an owner, a due date, and an evidence slot. It watches the agencies you care about, diffs proposed vs final, and opens Asana/Jira items mapped to the source passage. At exam time you export a folder: rule, obligation, who did what, attached proof.

**Target customer:** CCO / compliance analyst at a 20–200 person US fintech lender, community bank, or payments firm. Not a broker-dealer mega-firm. Buyer: CCO or General Counsel. Users: the 2–6 people who currently paste Federal Register links into Slack.

**Why now:** The open primitive exists and is still not a system of record. Enterprise regulatory-change software is still a demo-and-quote sale. August 2026 rulemaking volume did not produce a mid-market workflow product on top of the feed.

**Why they buy without being sold to:** After a consent order or a nasty FR notice, the CCO pastes last month’s “rules we think apply” spreadsheet into RuleFlow, sees three missed effective dates, and refuses to go back to Slack-PDFs.

**Revenue model:** $399/mo (1 agency family + 10 users). $599/mo (3 families + Jira/Asana sync). $799/mo (unlimited + evidence vault + SSO). Annual −2 months. 14-day trial on a saved agency watchlist.

**Unfair advantage:** Obligation→task→evidence mapping for one vertical (US depository / fintech lending) with citations back to primary text — not a 200-jurisdiction library.

### Solo Build Plan
1. Weeks 1–3: Ingest FRTracker API or daily FR deltas; agency watchlist; obligation cards with source quotes.
2. Weeks 4–5: Task export to Asana/Jira; owner + due date; proposed-vs-final diff view.
3. Weeks 6–7: Evidence upload per obligation; exam-pack ZIP/PDF.
4. Weeks 8–9: Stripe; fintech-lending template (lending, BSA/AML notices, CFPB).
5. Weeks 10–12: Pilot 5 CCOs via community-bank ops groups and fintech compliance Slack.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** The primitive is free and public; the unpaid job is workflow + evidence.
**Open question:** Will FRTracker itself add “send to Jira” and eat the wedge?

---

## #5 — BreakWatch  ·  72/100  ·  IMPROVED
First added: 2026-08-16 | Last updated: 2026-10-19 | Score delta this week: +5

> Know which upstream API changed shape before your agent treats the empty field as success.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — changelog crawlers + response snapshots + Slack)
- Value Clarity:       15/20  (+1 — an October 14 2026 write-up makes the failure mode obvious: the run logs success while the field is gone)
- Market Timing:       14/20  (+3 — Optic was archived on 12 Jan 2026, so the named “cheap vendor-watch SKU” did not ship; oasdiff checks specs you own; DriftGuard is a DEV post, not a product with a price)
- B2B Monetisation:    14/20  (unchanged — $149–$399/mo for a small integration team)
- Pull Factor:         14/20  (+1 — silent agent failures are now a post people forward)

**Strengths:**
- The August kill condition was “Optic ships a cheap watch-these-10-APIs SKU.” Optic’s repo was archived instead. Migrations point at oasdiff, which diffs OpenAPI in CI, not live vendor responses.
- Agents make the old break worse: a missing field becomes a plausible empty result, and the log says success. That pattern was written up on 14 Oct 2026 from production logs, not from a vendor pitch.
- Producer tools (Speakeasy, Bump) still help the API owner. The consumer of HubSpot, Stripe, or an MCP tool still finds out in production.

**Risks:**
- DriftGuard, or the next DEV-post tool, ships the snapshot diff as a paid watchlist.
- Vendor status pages plus a pinned SDK feel “good enough” until the silent week.
- Changelog formats lie. False alarms will get the Slack channel muted.

**Verdict:** Move up. Consumer-side watch of live responses, especially the ones agents call. Leave if a paid “watch these 10” SKU shows up with customers.

### The Pitch
**Problem:** Breaking changes that hurt an agent usually do not throw. Stripe-style versioning only labels the breaks the provider admits. A field rename comes back null, the model decides “nothing was found,” and the run logs success. A 14 Oct 2026 post walked through that failure on a live agent: hardcoded targets that no longer existed absorbed most of a bot’s attempts for weeks, every run green. Contract tests keep passing because they check fixtures, not the live vendor. Optic, the tool teams used to name for breaking-change CI, was archived on 12 Jan 2026. Its suggested replacement diffs OpenAPI specs you already have. It does not watch the HubSpot or MCP response your agent received this morning.

**Solution:** BreakWatch stores the last real response shape for each upstream call you care about — REST JSON or an MCP tools/list — and opens one Slack item when a field disappears, a type changes, or a tool name drops. You subscribe to endpoints. It does not replace your iPaaS and it does not sell you API docs.

**Target customer:** Eng lead at a 5–30 person SaaS whose product or agents call 5–15 APIs they do not own. Buyer: CTO. Users: the two people on integration on-call.

**Why now:** Agent runs hide schema drift inside a successful log line. The open-source checker people used to point at is unmaintained. The replacements check your spec, not the vendor’s last response.

**Why they buy without being sold to:** After a week of green agent runs that wrote nothing useful, the eng lead pastes the three upstream URLs into BreakWatch and requires a Slack ping the next time the shape moves.

**Revenue model:** $149/mo (10 watched endpoints). $249/mo (30 endpoints + MCP tools/list). $399/mo (GitHub comment when a watched shape moved). Annual −2 months. 14-day trial.

**Unfair advantage:** A watchlist of the response shapes small SaaS and agents actually break on, diffed from live calls, not from a spec the vendor forgot to publish.

### Solo Build Plan
1. Weeks 1–3: Scheduled fetch, inferred schema, diff, Slack alert for Stripe, HubSpot, and one MCP tools/list.
2. Weeks 4–5: Mute rules; removed-field vs added-field severity.
3. Weeks 6–7: GitHub comment when a watched shape moves.
4. Weeks 8–9: Stripe billing; “paste the call that lied” onboarding.
5. Weeks 10–12: Pilot 6 teams who have already had a silent agent miss.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-10-19
**Strongest part:** The failure is a green log, which is why changelog subscriptions do not catch it.
**Open question:** Does DriftGuard, or anyone else, ship a paid watchlist of live vendor responses before this does?

---

## #6 — ChurnDetect  ·  72/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-10-19 | Score delta this week: −1

> Find the customers about to leave — 90 days before they tell you — from the support tickets they are already sending.

### Score Breakdown
- Solo Buildability:   15/20  (unchanged — Zendesk/Intercom read + weekly account list)
- Value Clarity:       17/20  (unchanged — retrospective on the last churned account)
- Market Timing:       12/20  (−1 — Zendesk Intelligent Triage is still topic, sentiment, language, and entities, not account health; Pylon now sells account-level churn risk, but only if the team leaves Zendesk for Pylon)
- B2B Monetisation:    15/20  (unchanged)
- Pull Factor:         13/20  (unchanged)

**Strengths:**
- Zendesk’s own help text still describes triage as classification of a new ticket, available on Professional plans, with workflow use tied to the Copilot add-on. That is not an account-health score.
- Pylon’s 2026 positioning confirms the job (support signals → churn) and also confirms Zendesk does not do it. Pylon’s price of entry is a helpdesk migration.
- The retrospective on the account you already lost still closes itself.

**Risks:**
- Pylon, or the next B2B helpdesk, becomes the default and the add-on has no seat.
- Zendesk can add an account rollup without calling it a new SKU.
- Storing ticket text still needs a consent story.

**Verdict:** Hold the Zendesk-resident wedge. Do not pretend the category is empty for teams willing to switch helpdesks.

### The Pitch
**Problem:** B2B SaaS companies discover customer churn risk almost exclusively at renewal time, when the decision is already made. The warning signals — frustration in tickets, repeated unresolved issues, competitor mentions — sit in the support inbox. Zendesk Intelligent Triage classifies a ticket by topic, sentiment, language, and entities so it can be routed. It does not roll those tickets up into “this account is about to leave.” Pylon will do the account rollup if you move the helpdesk. Teams that are staying on Zendesk or Intercom still export nothing.

**Solution:** ChurnDetect connects to Zendesk or Intercom, reads recent tickets, and classifies threads for churn language, unresolved repeats, and competitor mentions. It emails a weekly list of accounts at risk with the thread that triggered the flag. The first session is a retrospective on an account you already lost.

**Target customer:** CS lead at a 10–150 person B2B SaaS on Zendesk or Intercom, 100+ customers, no Gainsight. Buyer: VP CS or the founder. Users: the CS team.

**Why now:** Ticket-level sentiment shipped inside the helpdesk. Account-level risk from those same tickets is being sold as a reason to switch helpdesks, which most teams will not do this quarter.

**Why they buy without being sold to:** A CS manager who lost a meaningful account runs the retrospective on that account’s last tickets, sees the flags from 90 days earlier, and keeps the weekly list.

**Revenue model:** $199/month (up to 500 accounts + Zendesk). $349/month (unlimited + Slack). $599/month (Intercom + custom phrases). 14-day trial. Annual −2 months.

**Unfair advantage:** The historical retrospective on a lost account, run inside the helpdesk the team already pays for.

### Solo Build Plan
1. Weeks 1–3: Zendesk read of historical tickets; risk labels per thread.
2. Weeks 4–5: Account rollup; weekly email; link to the thread.
3. Weeks 6–7: Intercom; Slack.
4. Weeks 8–9: Stripe; retrospective generator; consent note.
5. Weeks 10–12: Pilot 8 Zendesk teams who will not migrate helpdesk.

### Critic's Assessment
**Rating:** 7/10 | **Last critique:** 2026-08-16
**Strongest part:** The retrospective on a lost account does not require a pitch.
**Open question:** Will Zendesk ship the account rollup, or will Pylon’s migration pitch win the buyer first?

---

## #7 — BinderDesk  ·  67/100  ·  NEW
First added: 2026-10-19 | Last updated: 2026-10-19 | Score delta this week: —

> The list of tax documents that are still missing — not another client portal.

### Score Breakdown
- Solo Buildability:   16/20  (email ingest, expected-doc checklist, exception queue; not tax prep)
- Value Clarity:       16/20  (“these 14 clients still have no W-2” is obvious to a preparer)
- Market Timing:       13/20  (BigIdeasDB’s 2026 gap list puts tax-document intake and exceptions on small firms, with generic AI called unreliable; portals already exist, so this is not an empty market)
- B2B Monetisation:    14/20  ($149–$299/mo per firm through filing season; one missed document costs more)
- Pull Factor:          8/20  (preparers refer quietly; this will not travel on LinkedIn)

**Strengths:**
- The paid pain in the 2026 small-business gap list is exception handling, not “store a PDF.”
- A checklist of what is absent is a smaller product than a client portal, and it is what the preparer actually checks each morning.
- Seasonal cash is still cash if the tool is in the workflow before January.

**Risks:**
- SafeSend, Canopy, and the tax suites already chase documents. If their starter tier is cheap, this dies.
- Work is seasonal. Annual contracts will be resisted.
- Generic “AI reads the inbox” is exactly what the source says firms do not trust. The product has to show the missing item, not a summary.

**Verdict:** Enter on probation as the missing-document queue for a small prep firm. Remove next run if a named portal already sells that queue under $150.

### The Pitch
**Problem:** Small tax and bookkeeping firms still collect client documents by email. The 2026 gap write-up that lists this pain points at manual intake plus generic AI that firms do not trust to decide whether a return is complete. The preparer does not need another place to upload a PDF. They need to know which of the 80 clients is missing the W-2, the 1099, or the prior-year return, and which email arrived but does not match the checklist.

**Solution:** BinderDesk reads the client inbox (or a forwarded mailbox), checks each file against that client’s expected list, and shows only the exceptions: missing, unreadable, or not the document requested. It does not prepare the return and it does not replace the tax software.

**Target customer:** Owner or reviewer at a 2–15 person tax or bookkeeping firm that still tracks “waiting on docs” in a spreadsheet. Buyer: the owner. User: the preparer who sends the reminder.

**Why now:** Filing volume did not get simpler, and the 2026 complaint is that generic AI is not trusted for this intake. Firms will pay for a queue that is obviously right or obviously wrong.

**Why they buy without being sold to:** In February the reviewer opens BinderDesk instead of the spreadsheet, sees 14 clients still missing one document, and sends those reminders before lunch.

**Revenue model:** $149/mo (one office, 100 clients, filing-season months). $249/mo (300 clients + reminder email). $299/mo (bookkeeping year-round + tax season). Month-to-month. 30-day trial on last year’s checklist.

**Unfair advantage:** The screen is the exception list, built for one firm’s checklist, not a general client portal.

### Solo Build Plan
1. Weeks 1–3: Client list, expected-doc checklist, manual “received” marks, missing report.
2. Weeks 4–5: Forwarded-email ingest; filename and form-type match; exception reasons.
3. Weeks 6–7: Reminder email for missing items only.
4. Weeks 8–9: Stripe; sample checklist onboarding.
5. Weeks 10–12: Pilot 5 firms before the next filing ramp.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-10-19
**Strongest part:** The buyer already has a spreadsheet whose only job is “who has not sent the form.”
**Open question:** Does SafeSend or Canopy already sell that exception queue cheaply enough that a 5-person firm will not look at a new tool?

---

## #8 — MarkPack  ·  66/100  ·  DECLINED
First added: 2026-08-03 | Last updated: 2026-10-19 | Score delta this week: −7

> A hosted Article 50 evidence folder for the six weeks before the 2 December marking grace ends.

### Score Breakdown
- Solo Buildability:   13/20  (−1 — art50-ci and evidence templates already cover CI checks and marking JSON; the hosted folder is what is left)
- Value Clarity:       15/20  (−1 — “show me proof” is real, and several free or cheap packs now answer a slice of it)
- Market Timing:       13/20  (−4 — obligations have been in force since 2 Aug 2026; marking grace for pre-2-Aug systems ends 2 Dec 2026; SentinelGo, euagentai templates, and the art50-ci CLI now exist)
- B2B Monetisation:    14/20  (unchanged — $199–$499/mo if counsel will pay during the grace window)
- Pull Factor:         11/20  (−1 — the category is noisy)

**Strengths:**
- The Commission’s own FAQ still sets 2 December 2026 as the end of the marking grace for systems already on the market before 2 August. That date is close enough to force a buy.
- art50-ci is a local CLI and a technical preview. It checks configured disclosures and optional C2PA. It does not host the folder counsel opens.
- Teams that will not run a GitHub Action still need a ZIP an auditor can download.

**Risks:**
- After 2 December the urgency collapses if enforcement stays quiet.
- Adobe, model hosts, or a free CLI plus a Drive folder becomes the whole product.
- SentinelGo and one-time €29 packs already occupy “scan my site.”

**Verdict:** Stay only as the hosted evidence folder through the grace date. This is the last run unless a paid pilot exists by December.

### The Pitch
**Problem:** Article 50 transparency duties have applied since 2 August 2026. Machine-readable marking for systems that were already on the market before that date has a grace period until 2 December 2026, per the Commission’s FAQ. A product team that needs to show disclosure and marking proof now has a local CLI (art50-ci), an evidence template (euagentai), and screening sites (SentinelGo, article50.eu). What they still paste into email is a mix of screenshots and a Notion page. Counsel cannot re-run a developer’s laptop check.

**Solution:** MarkPack hosts the evidence folder: disclosure captures, the marking check output, the owner, and the date, exported as one ZIP. It can ingest an art50-ci report. It does not replace the CLI and it does not classify high-risk AI.

**Target customer:** Counsel and the eng lead at a 15–150 person company with an EU-facing chatbot or generator that shipped before 2 August 2026. Buyer: GC or founder. Users: the engineer who runs the check and the counsel who sends the ZIP.

**Why now:** The grace ends 2 December 2026. The free tools prove the check can be automated. They do not give counsel a URL.

**Why they buy without being sold to:** Counsel asks for the pack this week. Eng uploads the CLI output, MarkPack returns a dated ZIP, and that ZIP is what gets sent.

**Revenue model:** $199/mo (1 product, through the grace window, month-to-month). $349/mo (5 products). $499/mo (SSO). 14-day trial that generates a sample ZIP. No annual plan until a customer renews after December.

**Unfair advantage:** A folder that accepts the open checker’s output and is addressed to counsel, sold month-to-month while the grace clock is still running.

### Solo Build Plan
1. Weeks 1–2: Evidence schema; ZIP/PDF; sample pack.
2. Weeks 3–4: Import an art50-ci JSON report; store the hash and timestamp.
3. Weeks 5–6: Disclosure screenshot upload; owner field.
4. Weeks 7–8: Stripe, month-to-month.
5. Weeks 9–10: Pilot 5 teams who already run a checklist and have no folder. Stop if none will pay before December.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-10-19
**Strongest part:** The date is public and close, and the free tools deliberately refuse to be the legal folder.
**Open question:** Does anyone renew after 2 December 2026?

---

## #9 — AdvisorAlert  ·  65/100  ·  DECLINED
First added: 2026-07-31 | Last updated: 2026-10-19 | Score delta this week: −9

> Sample the client inbox for testimonial language — the check Luna still prices on the $1,499 plan.

### Score Breakdown
- Solo Buildability:   12/20  (unchanged — email sampling in a regulated context is still the hard part)
- Value Clarity:       16/20  (−1 — Luna’s free calendar and published plans already explain “RIA compliance software” without this product)
- Market Timing:       11/20  (−5 — Luna publishes Solo $199/mo, Firm $699/mo, Firm Plus $1,499/mo, month-to-month, no demo; email archive and review is listed on Firm Plus, not on Solo)
- B2B Monetisation:    15/20  (−2 — the suite price ceiling for a micro-RIA is now a public $199, so only the inbox slice can still ask for $299)
- Pull Factor:         11/20  (−1 — the category has a named, priced incumbent for this firm size)

**Strengths:**
- Hadrius is still quote-only and still auto-renews annually in its MSA. That part of the August note holds.
- Luna’s own comparison puts email archive and review on Firm Plus ($1,499/mo), not on Solo ($199/mo). A 1–5 person RIA can buy a calendar and still have no sampled inbox.
- The SEC-deficiency story (a client email that is a testimonial) is still a 10-second demo.

**Risks:**
- Luna moves email review down to Solo and this seat disappears.
- Hadrius uses the July raise to publish a starter tier.
- False positives in a regulated inbox end the trial immediately.

**Verdict:** Keep only the inbox-sampling wedge under Luna’s Firm Plus price. The full “micro-RIA compliance suite” pitch is no longer available.

### The Pitch
**Problem:** A 1–5 person RIA can now buy a published compliance calendar and marketing-review tool without a demo. Luna lists Solo at $199/mo and Firm at $699/mo, month-to-month, with policies, a calendar, and marketing-rule review. Email archive and review is on Firm Plus at $1,499/mo. Hadrius still does not publish a price and still sells an annual order form. The principal who is also the CCO still has client email that can say “you always get me great returns,” and the affordable plan they were just offered does not sample it.

**Solution:** AdvisorAlert connects one Gmail or Outlook mailbox, samples recent client threads, and flags testimonial, performance, and solicitation language with the sentence that triggered the flag. It does not draft the firm’s policies and it does not preclear personal trades. Those jobs now have a priced product.

**Target customer:** Principal at a 1–5 person RIA, $50M–$500M AUM, who will not pay $1,499/mo for an email archive. Buyer: the principal. User: the principal.

**Why now:** The suite gap closed in public pricing. The inbox gap is what Luna’s price table still leaves on the expensive plan.

**Why they buy without being sold to:** The principal connects the inbox, sees one flagged sentence from last month, and compares that to a $1,499 archive they do not want.

**Revenue model:** $299/mo (1 mailbox, 50 threads sampled, weekly digest). $499/mo (3 mailboxes). No $799 suite tier. Annual −2 months. Free 14-day sample on one mailbox. Calendar features are out of scope.

**Unfair advantage:** A single check priced under Luna’s email tier, sold to the firm that already has a calendar.

### Solo Build Plan
1. Weeks 1–3: Gmail and Outlook read; flag testimonial and performance language; show the sentence.
2. Weeks 4–5: Weekly digest; sampling cap; explainability line.
3. Weeks 6–7: Legal review of “monitoring, not advice”; export of flagged threads.
4. Weeks 8–9: Stripe.
5. Weeks 10–12: Pilot 5 principals who already pay for a calendar product and not for email review.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-10-19
**Strongest part:** The price table that hurt the old pitch also marks the remaining hole: email review is not on the $199 plan.
**Open question:** Does Luna add email review to Solo before a $299 sampler can get five design partners?

---

## #10 — AuthTrack  ·  58/100  ·  DECLINED
First added: 2026-08-16 | Last updated: 2026-10-19 | Score delta this week: −12

> A prior-auth clock for the practice that has outgrown a free spreadsheet and is not on Linear.

### Score Breakdown
- Solo Buildability:   13/20  (−1 — the fields are now published; the build is multi-user reminders without becoming an EHR integration)
- Value Clarity:       13/20  (−3 — ClinicOps shipped a free Sheet on 3 Aug 2026 with follow-up date, denial reason, and expiration alert)
- Market Timing:       10/20  (−4 — Linear Health’s 21 Aug 2026 guide says a spreadsheet is the right log under about 100–200 active PAs; CMS clocks have been payer-side duties since 1 Jan 2026)
- B2B Monetisation:    11/20  (−3 — the free sheet does the obvious columns; $149 has to buy multi-user reminders, not the idea of a log)
- Pull Factor:         11/20  (−1)

**Strengths:**
- CMS-0057-F still means specific denial reasons and 7-day / 72-hour payer clocks. Practices still need a log even though the API mandate is January 2027.
- Linear’s own guide admits the spreadsheet fails when several people edit it, when there are no timestamps, and when nothing builds the daily worklist. That is the paid wedge.
- Chart-number-only tracking, which ClinicOps also recommends, keeps PHI out of v1.

**Risks:**
- The free sheet is good enough under 100 requests, which is most of the original beachhead.
- Linear, Waystar, or a clearinghouse adds the worklist.
- Practices believe the payer owes the clock, so they will not pay to track it.

**Verdict:** Last seat. Only the multi-staff worklist above the free sheet. Remove next run if that worklist is not visibly paid for.

### The Pitch
**Problem:** Since 1 January 2026, impacted payers have had to decide standard prior auths in 7 calendar days and urgent ones in 72 hours, and denials need a specific reason. Small practices were told to track that in a spreadsheet. On 3 August 2026 ClinicOps published a free Sheet that already has an owner, a follow-up date, a denial reason, and an expiration alert, using chart numbers so the file is not a PHI dump. On 21 August 2026 Linear Health wrote that this kind of spreadsheet is appropriate below roughly 100–200 active requests, and that it fails when two people edit it, when nothing timestamps the change, and when nobody builds today’s worklist. Linear’s product is the submit-and-track automation for groups that want the payer call gone. The 2–10 provider office that is over the free sheet and not ready for Linear still has the fax log.

**Solution:** AuthTrack is that worklist. Each request has a clock, one owner, a denial-reason field, and a reminder before the window closes. v1 imports the ClinicOps-shaped CSV. It does not call the payer and it does not write to the EHR.

**Target customer:** Billing lead at a practice whose PA queue no longer fits one person’s spreadsheet — several billers, overlapping edits, missed follow-ups — and who is not buying Linear. Buyer: office manager. User: the billers.

**Why now:** The clocks are already in force. The free sheet defined the columns. The remaining pain is the queue those columns cannot manage once two people share it.

**Why they buy without being sold to:** Two billers overwrite the same sheet, a follow-up is missed, and the office manager imports the CSV into a board that tells them whose items are due today.

**Revenue model:** $149/mo (1 location, reminders, no SMS). $249/mo (3 locations + SMS). Month-to-month. 14-day trial that imports the sheet they already have. Do not charge for the column template.

**Unfair advantage:** Import of the free sheet plus a daily worklist. The template sites will not run the queue.

### Solo Build Plan
1. Weeks 1–3: CSV import matching the public tracker columns; clocks; one owner; today’s due list.
2. Weeks 4–5: Email reminders; timestamped status changes.
3. Weeks 6–7: Optional SMS; export for appeals.
4. Weeks 8–9: Stripe; “upload the sheet you already use” onboarding.
5. Weeks 10–12: Pilot 5 offices that already tried the free sheet and still miss follow-ups. Stop if they will not pay.

### Critic's Assessment
**Rating:** 6/10 | **Last critique:** 2026-10-19
**Strongest part:** Linear’s own writing draws the line where the spreadsheet stops, which is a narrower and more honest buyer than “anyone with a fax machine.”
**Open question:** How many 2–10 provider offices are actually above 100 active PAs and still unwilling to buy Linear?

---

## Removed this run
| Entry | Last score | Reason |
|-------|------------|--------|
| TokenBill | 72 → 40 | Ramp launched AI Token Spend on 16 Jul 2026: OpenAI, Anthropic, Gemini, and Cursor in one finance view, weekly briefings, spike alerts, limits, and a forecast. The August open question (“will Ramp ship this?”) is answered. |
| BriefDesk | 72 → 48 | Brief’s own docs describe a Weekly Brief agent over HubSpot, Stripe, and Linear. Data Parrot still sends weekly HubSpot sales briefs (starter “Deals to Check” updated 6 Jul 2026). The multi-stack narrative brief is no longer an empty seat. |
| FlowTrace | 62 → 51 | Prior verdict was remove if nobody was paying for a cross-vendor pause. Countersign sells a sub-second freeze across wallet rails. AEGIS is an open-source SIGSTOP for local Claude Code / Codex sessions. Helicone already returns 429s on LLM spend policies. SanctumShield is still a policy pack. No evidence of a paid OpenAI+Claude+Zapier pause. Lowest score after the cuts. |
