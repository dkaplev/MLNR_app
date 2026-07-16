# Source Coverage Audit — 2026-07-16 Cookbook Run

Purpose: make the scout’s information diet visible so we do not overfit to a few loud sources and miss other worthy ones.

---

## 1. Relevant source classes (what *should* be in the diet)

These are the source types that are relevant for solo B2B SaaS opportunity scouting — independent of whether this run used them.

| Class | Why it matters | Typical examples |
|-------|----------------|------------------|
| A. Analyst / industry surveys | Named, ranked SMB/IT pains with year stamps | Techaisle, Gartner summaries, Menlo, Bessemer |
| B. Aggregated complaint / idea DBs | Bottom-up pain from reviews, Reddit, Upwork | BigIdeasDB, G2/Capterra trend roundups |
| C. Vendor / competitor primary pages | Falsify “greenfield” claims; price wedges | Product sites, pricing pages, compare pages |
| D. Buyer-guide roundups | Category density; who owns which segment | “Best X software 2026” articles |
| E. Regulation / official + regtech | Hard deadlines, penalty math, tooling waves | EU AI Act tooling, Hadrius, Legalithm |
| F. Engineering / OSS signals | Emerging categories before commercial products | GitHub trending, Ruflo, SpecSeal, Kiro |
| G. Trade / vertical specialist blogs | Niche workflows incumbents ignore | StableTrack (equine), construction field blogs |
| H. Integration / API research | Maintenance tax for B2B SaaS builders | Specway, Apideck, MuleSoft Connectivity |
| I. Community raw voice | Unfiltered pain, not vendor marketing | Reddit, HN, Indie Hackers, Slack communities |
| J. Product discovery feeds | What is launching *this week* | Product Hunt, Launch HN, BetaList |
| K. Job / freelance demand | Recurring outsourced tasks = product gaps | Upwork frequency, “hiring for X” posts |
| L. Academic / standards | Evaluation gaps, protocol maturity | LangChain surveys, OTel GenAI, MCP auth roadmap |
| M. Prior cookbook + deltas | Compounding memory; avoid rediscovering dead ideas | COOKBOOK.md, delta_*.md |

---

## 2. Coverage scorecard for this run

| Class | Used? | Intensity | Bias risk if underused |
|-------|-------|-----------|------------------------|
| A. Analyst surveys | **Yes** | High (Techaisle repeatedly) | Overweight “named 2026 IT challenges” |
| B. Complaint aggregators | **Yes** | High (BigIdeasDB) | Same pains recycle every week |
| C. Competitor primaries | **Yes** | High (reassessment stage) | Good — this is how removals happened |
| D. Buyer guides | **Yes** | Medium–high | Can make niches look more crowded than SMB reality |
| E. Regulation / regtech | **Yes** | High (Article 50 wave) | Deadline ideas dominate near Aug 2 |
| F. Engineering / OSS | **Partial** | Medium | Miss early OSS→commercial wedges |
| G. Vertical specialist | **Partial** | Low–medium (equine, construction, medspa) | Over-index horizontal AI/SaaS |
| H. Integration research | **Yes** | Medium (Specway, Apideck, MuleSoft) | — |
| I. Community raw voice | **Weak** | Low (indirect via secondary articles) | **Major blind spot** |
| J. Product discovery feeds | **No** | None | Miss “already launched yesterday” |
| K. Job / freelance demand | **Indirect** | Via BigIdeasDB Upwork freqs only | Miss fresh Upwork spikes |
| L. Academic / standards | **Partial** | LangChain survey, OTel notes | — |
| M. Prior cookbook | **Yes** | Required baseline | — |

**Headline bias for this run:** heavy on analyst blogs + competitor SEO pages + regulation tooling; light on Reddit/HN/Product Hunt primary browsing and raw job-market signals.

---

## 3. Sources actually consulted (by stage)

### 3.1 Stage 1 — Scout (prescribed queries 1–10 + follow-ons)

#### Query 1 — B2B SaaS / SMB unmet needs

| Source | Used | Pain points / ideas extracted |
|--------|------|-------------------------------|
| [Techaisle — 2026 Top 10 SMB Business Issues & IT Challenges](https://www.techaisle.com/blog/668-2026-smb-top-10-business-issues-tech-priorities-agentic-ai-shift) | **Yes — core** | Token Shock / AI cost unpredictability (#1 IT); Data Trust & Sanitization for AI (#2); Shadow AI governance (#4); SaaS Silos (#5); profitable growth + cost control as business #1/#2; compliance as #8 |
| [BigIdeasDB — Top Business Pain Points 2026](https://bigideasdb.com/business-pain-points-2026) | **Yes — core** | Manual reporting/analytics #1 (33.3%); broken onboarding (32.6%); lead data quality (31.3%); support that won’t scale; notification overload; bookkeeping/reconciliation; legal compliance; spreadsheet inventory; **offboarding security**; clinical workflow chaos |
| Lurika — SMB analytics failure | Yes | Multi-source data never joins without engineer or spreadsheet tax → feeds ReportGlue |
| Bubble — onboarding software 2026 | Light | Onboarding/IT provisioning gaps (already crowded — Gusto/Rippling/Deel) |

**Ideas scored from this cluster:** ReportGlue (entered #1); DataReady (entered #3); offboarding watched via EasyRevoke; TokenShock reassessed/removed.

#### Query 2 — AI agent workflow integration

| Source | Used | Pain points / ideas extracted |
|--------|------|-------------------------------|
| VentureBeat — agentic orchestration survey | Yes | Most “agents” still chatbot wrappers; fiscal control lag (27% no real-time stop); hybrid control plane preferred |
| Thorsten Meyer — agent bottleneck = plumbing | Yes | 46% cite integration with existing systems as #1 challenge (not models) |
| TechTimes — agents stall at login | Yes | Authentication wall; 82% IT leaders cite data integration; MCP OAuth/SAML roadmap immature |
| Orbilon / MuleSoft Connectivity Benchmark 2026 | Yes | 95% report integration problems; only ~27% apps connected; half of agents siloed; 36% of IT time on custom integrations |
| Agentbrisk — AI cost attribution | Yes (also TokenShock reassessment) | Finance vs engineering cost views; Langfuse/Helicone attribution models |

**Ideas:** DataReady (data trust for agents); AgentAuth gateway (watched, too heavy for solo MVP); FlowLock reassessment (governance squeezed).

#### Query 3 — Compliance / regulation automation

| Source | Used | Pain points / ideas extracted |
|--------|------|-------------------------------|
| Hadrius $27M agentic compliance (finserv) | Yes | Agentic compliance for RIAs — crowded/funded, not solo |
| Vanta enterprise compliance roundup | Yes | Continuous monitoring vs checklists; enterprise ACV |
| MarketIntelo — AI-native compliance | Yes | EU AI Act as net-new category (~$2.1B cited); CSRD/ESG vertical expansion |
| Glean — industries with AI compliance needs | Yes | High-risk / agentic workflow compliance beyond content labeling |
| DiscloseKit, AiCompliBot, AIR Blackbox, Legalithm, Augment Intent | **Yes — heavy** | Article 50 tooling explosion → ArticleShield −10 |

**Ideas:** ArticleShield pivot to technical SDK; ComplianceLayer already dead last run; CSRD Lite watched but not entered.

#### Query 4 — Developer tooling / OSS gaps

| Source | Used | Pain points / ideas extracted |
|--------|------|-------------------------------|
| LangChain State of Agent Engineering 2026 (via paperclipped) | Yes | 89% observability vs 52% offline evals; governance immature → AgentEval watchlisted |
| Prefactor — evals vs observability | Yes | Watching ≠ evaluating; rollback rates without evals |
| OpenTelemetry for AI agents | Yes | Multi-agent trace correlation still experimental |
| GitHub Ruflo / Citadel / OpenPraxis | Yes | OSS orchestration + guidance packages → FlowLock commercial wedge narrowed |

**Ideas:** SpecDrift kept with caution; AgentEval not entered (Braintrust/LangSmith densify); FlowLock removed.

#### Query 5 — Vertical SaaS niches

| Source | Used | Pain points / ideas extracted |
|--------|------|-------------------------------|
| YouStartups / ISHIR vertical SaaS guides | Light | Construction, healthcare sub-verticals, legal, HOA as themes |
| Dazlab — underserved market signals | Yes | Spreadsheet macros + multi-tool workarounds as opportunity markers |
| SaasOpportunities — construction jobsites $640M | Yes | Daily reporting, sub prequal, safety — then verified crowded |
| ExpiryEdge / Vertikal / Billy / MeltPlan — subcontractor prequal 2026 | Yes | Prequal/COI space has Billy, ExpiryEdge, Procore, TradeTapp — not greenfield |
| BuildLog, Voice Log Pro, DokuAI, Raken | Yes | Voice daily logs already productized → watchlist only |
| Medspa buyer guides (SproutSage, NexioBit, Zenoti, MDware) | **Yes** | Aesthetic Record, Zenoti, PatientNow, Lobbie, Oxhy… → MedSpa OS removed |
| StableTrack + Vetspire + PetDesk vet specialty | **Yes** | Solo ambulatory equine offline gap → EquineField entered |

#### Query 6 — Spreadsheet / repetitive workflow

| Source | Used | Pain points / ideas extracted |
|--------|------|-------------------------------|
| CSW Solutions — AI replacing SMB spreadsheets (Jul 2026) | **Yes** | 4–5h weekly CRM+PM+billing report → ReportGlue core anecdote |
| ERPLite — spreadsheet cost-of-delay | Yes | AI-native ERP keying reduction; parallel-run migration |
| Coworker / Workast / MLDeep automation posts | Light | Cross-system coordination tax; automate 2–3 workflows first |

#### Query 7 — No-code / low-code frustrations

| Source | Used | Pain points / ideas extracted |
|--------|------|-------------------------------|
| Lowcode.agency capabilities/limits 2026 | Yes | Vendor lock-in, performance ceilings, niche API integration walls |
| ECOSIRE / Tech-Champion no-code backlash | Yes | Orphaned citizen apps; shadow IT; “no source to audit” |
| Gartner/Kissflow LCAP commentary | Light | Citizen development strategic but needs CoE governance |

**Ideas considered:** CitizenAudit / orphaned no-code inventory — scored ~67, did not enter top 10.

#### Query 8 — API integration pain

| Source | Used | Pain points / ideas extracted |
|--------|------|-------------------------------|
| Specway API Integration Complexity Report 2026 | **Yes — core** | 68% take 3× estimate; 41% breaking changes unannounced; 2.3 breaks/year → SchemaWatch |
| Apideck — third-party dependency / what breaks | Yes | Silent field renames; pagination/cursor expiry; maintenance as permanent tax |
| Inovaflow — managing integrations at scale | Yes | Inflection at 5–10 integrations; credential vaults; normalized errors |
| Medium/Vovance — 7 API challenges 2026 | Light | Webhook reliability; auth diversity |

#### Query 9 — Remote / hybrid coordination

| Source | Used | Pain points / ideas extracted |
|--------|------|-------------------------------|
| Utiliko / Neroia / Futuramo collaboration 2026 | Yes | Too many tools; gap after the meeting ends |
| Coommit — AI coordination tax | Yes | Individual AI velocity ↑, team decision latency ↑; stack consolidation 5–9 tools |
| LoomStack — AI eng coordination bottleneck | Yes | Need “service mesh for agents” — overlaps FlowLock/governance |
| Ping, ClearFeed, Suptask, Plain, SLA Buddy | **Yes** | Slack SLA/helpdesk densified → SLADesk −8 |

#### Query 10 — EU AI Act / GDPR tooling (also Stage 3 for ArticleShield)

Covered under Query 3 competitor set — DiscloseKit countdown, AiCompliBot SME comparison, AIR Blackbox OSS scanners, Legalithm workstream map, Augment coding-tool compliance.

---

### 3.2 Stage 3 — Reassessment searches (existing cookbook)

| Cookbook entry | Key sources used | Extracted change signal |
|----------------|------------------|-------------------------|
| ArticleShield | DiscloseKit, AiCompliBot, AIR Blackbox, Legalithm, Augment | Checklist/scanner land-grab; technical SDK still thinner → 81→71 |
| SaaSScope | Substly, Primo, Inventoria, Cledara, SpendHound, Zendikt, GetPrimo | SMB SaaS management crowded → 80→70 |
| MatchFlow | Growthy, HelloBooks, Booke AI, Ledger Brief, bookkeeping-services.com | Botkeeper still dead; alternatives active → 78→73 |
| MedSpa OS | SproutSage, NexioBit, Zenoti guides, MDware | Purpose-built competitors numerous → 78→60 **removed** |
| QuoteDock | FreightMynd, VelocityOS | Still TMS/forwarder-first; zero-integration wedge holds → 77→75 |
| SpecDrift | Kiro docs/blogs, SpecSeal, Living Specs mentions | Native/community drift tools appearing → 75→71 |
| TokenShock | Langfuse, Helicone, AICost.ai, Inventoria, Agentbrisk | CFO forecasting white space closing → 74→65 **removed** |
| CleanAudit | Xorabyte, AuditBadger, AuditPath, Clovra | Sub-$300 SOC 2 automation common → 73→61 **removed** |
| FlowLock | Ruflo GitHub/releases, ShadowLock, PrivacyPal, Shadow Warden | OSS governance + shadow-AI security → 72→63 **removed** |
| SLADesk | Ping, ClearFeed, Suptask, Plain, Halp/Atlassian | Slack SLA category filled for IT/support → 77→69 |

### 3.3 Extra scout searches (beyond the 10 prescribed queries)

| Search theme | Sources | Extracted |
|--------------|---------|-----------|
| Shadow AI governance SMB | Shadow Warden, ShadowLock, PrivacyPal | Blockers exist; “agent-ready data prep” still open → DataReady |
| Construction daily voice reports | BuildLog, DokuAI, Voice Log Pro, Raken | Crowded → not entered |
| Specialty vet / equine | StableTrack, Vetspire HOOF, VetRec, PetDesk | Solo ambulatory gap → EquineField |
| Employee offboarding revocation | EasyRevoke, Passwork, AccessOwl, FirstHR, Torii | EasyRevoke already owns lean-team wedge → watchlist only |

---

## 4. Idea ← source lineage (what made the cut / what didn’t)

| Outcome | Idea | Primary source lineage |
|---------|------|------------------------|
| **Entered #1** | ReportGlue | BigIdeasDB #1 + CSW Solutions Friday report anecdote + Techaisle SaaS silos |
| **Entered #3** | DataReady | Techaisle Data Trust/Shadow AI + MuleSoft/TechTimes agent integration + gap vs ShadowLock/PrivacyPal |
| **Entered #4** | SchemaWatch | Specway 2026 + Apideck maintenance tax + Inovaflow 5–10 connector inflection |
| **Entered #9** | EquineField | StableTrack ambulatory gap blog + Vetspire/VetRec enterprise contrast |
| Kept | QuoteDock, MatchFlow, ArticleShield, SpecDrift, SaaSScope, SLADesk | Prior cookbook + competitor falsification sources above |
| Removed | MedSpa OS, TokenShock, FlowLock, CleanAudit | Buyer guides + pricing pages + OSS releases |
| Watched only | EasyRevoke/offboarding, AgentEval, construction voice logs, CitizenAudit, AgentAuth | Seen but lost on score or solo-buildability |

---

## 5. Blind spots — sources relevant but **not** used this run

These are the bias risks you asked about. Next run should deliberately sample at least 2–3 items from each unused class.

| Blind spot | Why it matters | Suggested next-run probes |
|------------|----------------|---------------------------|
| **Reddit primary threads** | Unfiltered vertical hate (r/Veterinary was watchlisted last week but not re-opened raw) | r/smallbusiness, r/sysadmin, r/Bookkeeping, r/medspa, r/equine, r/supplychain |
| **Hacker News / Show HN** | Early product launches + “Ask HN: what do you hate” | Front page + Ask HN pain threads week-of |
| **Product Hunt / Launch HN** | Prevent inventing ideas that launched 3 days ago | PH “SaaS” + “AI” this week |
| **G2 / Capterra review mining (primary)** | Used via secondary roundups only | Direct scrape of 1-star themes for PatientNow-class targets |
| **Indie Hackers / Stripe Atlas / MicroConf** | Solo-founder validated niches | IH “what I’m building” + revenue screenshots |
| **Twitter/X / LinkedIn ops communities** | Where “Token Shock” and “tool sprawl” narratives spread | Ops Nation, CFO Alliance mentions |
| **Job boards / Upwork (primary)** | BigIdeasDB Upwork freqs are lagged aggregates | Live Upwork: bookkeeping, COI chase, inventory spreadsheets |
| **GitHub Trending (broad)** | Only Ruflo/Kiro-adjacent repos checked | Trending + “awesome-*” for agent eval, MCP auth |
| **App Store / Chrome Web Store reviews** | Field mobile pain for construction/vet | Equine / contractor app 1-star themes |
| **SEC / official EU AI Act text** | Relied on vendor interpretations of Article 50 | Primary regulation + Code of Practice PDFs |
| **Podcasts / operator interviews** | Qualitative “why we switched” | Acquired, Lenny, niche vet/construction pods |
| **University / hospital procurement lists** | Specialty vet buying reality | Ignored this run |

---

## 6. Concentration risk (what dominated scoring)

Rough share of *decisive* evidence this run:

1. **Techaisle + BigIdeasDB** — ~30% of new-entry justification (ReportGlue, DataReady, TokenShock kill)
2. **Competitor landing pages / “best of 2026” guides** — ~35% of removals and declines (MedSpa, SaaSScope, CleanAudit, SLADesk, ArticleShield)
3. **Specway / Apideck / MuleSoft** — ~10% (SchemaWatch)
4. **Vertical specialist blogs** — ~10% (EquineField; construction rejected)
5. **OSS GitHub** — ~10% (FlowLock/SpecDrift)
6. **Community primary sources** — ~5% or less

That skew is useful for *falsifying* crowded ideas, but weak for *discovering* non-SEO pains. The cookbook can become a mirror of what vendors already write about.

---

## 7. Recommendations for next run (bias controls)

1. **Quota the diet:** for Stage 1, require ≥2 findings from classes I/J/K (community, launches, jobs) before scoring — not only A/B/C.
2. **One “anti-Techaisle” pass:** deliberately search outside SMB-IT-challenge vocabulary (e.g. trades, clinics, logistics dock workers).
3. **Launch canary:** 15 minutes on Product Hunt + Show HN before finalizing NEW entries — kill anything that already shipped.
4. **Keep competitor falsification** (class C/D) — it correctly removed four weak seats this week; do not loosen that.
5. **Log this audit every run** as `source_audit_YYYY-MM-DD.md` next to the delta so coverage drift is visible week over week.

---

## 8. File map for this run

| Artifact | Path |
|----------|------|
| Cookbook | `saas_scout/reports/COOKBOOK.md` |
| Delta | `saas_scout/reports/delta_2026-07-16.md` |
| This audit | `saas_scout/reports/source_audit_2026-07-16.md` |
