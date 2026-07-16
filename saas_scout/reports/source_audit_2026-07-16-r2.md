# Source Coverage Audit — 2026-07-16 R2 (Blind-spot run)

Companion to `delta_2026-07-16-r2.md`. Purpose: prove the diet shifted away from R1 concentration.

---

## 1. Diet quota (planned vs actual)

| Class | R1 intensity | R2 quota | R2 actual | Notes |
|-------|--------------|----------|-----------|-------|
| A. Analyst surveys | High | Cap ≤15% decisive | ~10% | Techaisle/BigIdeasDB only as secondary |
| B. Complaint aggregators | High | Cap | Low | Not primary this run |
| C. Competitor primaries | High | Keep | ~15% | Fairview, Junior, Pact, Spanly, Samera, Open Dental |
| D. Buyer guides | Med-high | Optional | Low | HVAC FSM guides used to *avoid* crowded FSM |
| E. Regulation | High | Light | Light | ArticleShield only |
| F. Engineering / OSS | Partial | **Required** | **High** | mcpsnoop Show HN + GitHub |
| G. Vertical specialists | Partial | **Required** | **High** | Open Dental docs, StableTrack, dental pay, HVAC Pact |
| H. Integration research | Med | Optional | Low | SchemaWatch carried |
| I. Community raw voice | **Weak** | **≥2 findings** | **Met** | HN Ask SaaS bottlenecks; Show HN mcpsnoop; HN org-blindness |
| J. Product discovery | **None** | **≥2 findings** | **Met** | SideKik PH; Anvil GEO; Fairview/Junior canary; Naoma |
| K. Jobs / freelance | Indirect | **≥2 findings** | **Met** | Upwork 1,062 bookkeeping jobs; n8n Exact Online automation job |
| L. Academic / standards | Partial | Optional | Low | — |
| M. Prior cookbook | Yes | Yes | Yes | Full R1 roster loaded |

---

## 2. Sources consulted → pains extracted

### I. Community (HN / Show HN)

| Source | Extracted | Cookbook impact |
|--------|-----------|-----------------|
| Ask HN: B2B SaaS biggest problems (item 46088125) | Distribution > building; low qualified leads; conferences as analog channel; co-founder hiring | No new entry (sales tooling crowded); reinforced "don't build another AI wrapper" |
| Ask HN: bottlenecks / Onboardly reply | Vertical onboarding product exists | Avoided generic onboarding idea |
| Ask HN: org blindness in B2B deals | Deals stall on decision-maker map | Watched only (Gong/ZoomInfo) |
| Ask HN: AI makes building trivial (2026) | Moat = customers/distribution/tech debt | Soft filter on scoring |
| **Show HN: mcpsnoop** + GitHub kerlenton/mcpsnoop | Wireshark for MCP; Inspector wrong data path; CI check mode | **→ MCPLens entered #5** |
| TechTimes on mcpsnoop (Jul 4, 2026) | Corroborated Show HN | MCPLens timing |

### J. Product discovery / launches

| Source | Extracted | Cookbook impact |
|--------|-----------|-----------------|
| SideKik PH (Jul 16, 2026) | SMB CRM launch | No entry (CRM saturated) |
| Anvil + GenRankEngine + Siftly + Citare + Geonimo | GEO/AI visibility crowded | Explicitly skipped |
| Naoma AI demo agent (PH #1 earlier 2026) | Demo bottleneck for B2B SaaS | Watched; crowded sales-AI |
| **Fairview weekly operating report** ($149–699) | Exact ReportGlue job-to-be-done | **→ ReportGlue removed (−15)** |
| **Junior.so weekly reporting** | Slack/email digests from Stripe/CRM/Linear | **→ ReportGlue removed** |
| Pact usepact.io | HVAC agreement tracker $29 | Avoided re-adding HVAC agreements |
| Spanly MCP observability ($41+) | Hosted MCP metrics | Capped MCPLens score; differentiated session Wireshark UX |

### K. Jobs / freelance

| Source | Extracted | Cookbook impact |
|--------|-----------|-----------------|
| Upwork bookkeeping jobs (~1,062 listed) | Reconciliation/QBO/Xero still hired at scale | **MatchFlow +2** |
| Upwork n8n Exact Online bookkeeping workflow job | Buyers pay to automate ledger glue | MatchFlow / automation corroboration |

### G. Boring vertical / anti-Techaisle

| Source | Extracted | Cookbook impact |
|--------|-----------|-----------------|
| Medium / Flowjam / LaunchKit / Redwerk boring SaaS 2026 | HVAC, dental, plumbing as durable niches | Diet steering |
| **Open Dental Provider Payroll docs + blog** | Offices use production reports for % pay; Excel still implied | **→ DentPay #1** |
| Samera AI (UK dental associate pay) | Category validated; Dentally/Xero; US gap | DentPay positioning |
| Gusto dentist payroll page | Deposits/splits at payroll layer, not OD reconciliation | DentPay differentiation |
| StableTrack equine ambulatory (prior) | Still open | EquineField +2 |
| Repair-CRM / FieldPad / ServiceTitan alternatives | Full FSM crowded; solo EPA/offline niches claimed | Avoided FSM platform entry |
| G2/Trustpilot PatientNow 1-stars | Support/contract hate | Confirms MedSpa removal still correct; not re-entered |

### Reddit
Primary `site:reddit.com` query returned weak/no useful hits this session (search tooling gap). Used secondary citations (ServiceAgent HVAC article claiming r/HVAC review reads; LaunchKit "find the subreddit" advice). **Residual blind spot:** direct Reddit thread mining still incomplete — flag for R3.

---

## 3. Concentration comparison

| Decisive cluster | R1 share | R2 share | Direction |
|------------------|----------|----------|-----------|
| Techaisle + BigIdeasDB | ~30% | ~10% | ↓ corrected |
| Competitor SEO / buyer guides | ~35% | ~15% | ↓ |
| Community / Show HN | ~5% | ~25% | ↑ |
| Launch canary | ~0% | ~20% | ↑ |
| Jobs | ~0% | ~10% | ↑ |
| Boring vertical primary | ~10% | ~20% | ↑ |

---

## 4. Ideas considered from blind-spot diet (not all entered)

| Idea | Sources | Score / fate |
|------|---------|--------------|
| DentPay | OD docs, Samera, Gusto, IH dental | **77 ENTERED** |
| MCPLens | mcpsnoop Show HN, Spanly, MintMCP | **73 ENTERED** |
| ReportGlue defend | Fairview, Junior canary | **63 REMOVED** |
| HVAC Pact clone | usepact.io | Rejected — occupied |
| GEO brand monitor | Anvil/Siftly/… | Rejected — crowded |
| Full HVAC FSM | FieldPad/Jobber/… | Rejected — crowded |
| B2B org-chart lite | HN org blindness | ~65 watched |
| Vendor spreadsheet AP | ProcIndex | ~67 watched |

---

## 5. Remaining blind spots after R2

1. **Direct Reddit HTML threads** — search API weak; manually open r/dentistry, r/HVAC, r/Bookkeeping next run.
2. **Indie Hackers primary posts** (not roundup blogs) — still secondary.
3. **Official EU AI Act PDF** — still vendor-mediated for ArticleShield.
4. **Podcasts / operator interviews** — unused.

---

## 6. Process rule adopted

Before any idea can occupy cookbook rank #1–3, R3+ must show:
1. at least one **I/J/K** primary source, and
2. a **launch canary** check (PH + web for product name / job-to-be-done).

R1 ReportGlue failure mode must not recur.
