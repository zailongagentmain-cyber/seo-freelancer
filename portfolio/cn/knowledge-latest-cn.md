# SEO/AI/GEO Trends Knowledge Base — Round 245

**Generated:** April 4, 2026, 18:10 GMT+8
**Topic:** 286 — "March 2026 Core Update Rolling (April 3-4), Illyes Googlebot 2MB Limit Clarification + Mt. AI GEO Architecture (llms.txt → JSON-LD → Entity Graph → Provenance), ChatGPT Ads Low CTR vs $100M Pilot, Evergreen Content Disruption, AI Job Cuts as Top Layoff Reason"

---

## 10-Finding Summary Table

| # | Finding | Source | Score |
|---|---------|--------|-------|
| 1 | March 2026 Core Update actively rolling as of April 3-4; up to 2-week rollout; Mueller confirms multi-team, staged deployment | SEJ/Google | 9/10 |
| 2 | Illyes clarifies Googlebot 2MB byte limit: headers count toward limit, external resources get separate counters, truncation = permanent content loss | SEJ/Illyes | 9/10 |
| 3 | Duane Forrester's 4-layer GEO architecture: llms.txt → JSON-LD machine layer → entity graph → provenance (far beyond simple TOC) | SEJ/Duane Forrester | 9/10 |
| 4 | llms.txt audit: LLM bots essentially absent from CDN logs (1,000 AEM domains); Googlebot dominates — raises serious llms.txt ROI question | SEJ/AEM audit | 8/10 |
| 5 | ChatGPT Ads pilot: $100M annualized revenue in 6 weeks, 600+ advertisers; but CTR as low as 0.91% vs 6.4% Google benchmark; self-serve launching April | SEJ/Reuters | 8/10 |
| 6 | Grokipedia continues dropping post-March 2026 Core Update; same pattern across Google, AI Overviews, AI Mode, and ChatGPT — "Mt. AI" confirmed | SERoundTable/Glenn Gabe | 8/10 |
| 7 | Evergreen content losing value: -32pp in publisher plans; AI effective at summarizing bread-and-butter content; "antithesis to AI slop" framing | SEJ | 7/10 |
| 8 | Mueller answers sitemap splitting: group by content type, split by freshness (theoretical recrawl benefit), avoid 50k URL cap, hreflang sitemaps | SEJ/Mueller | 7/10 |
| 9 | AI leads all cited reasons for US job cuts in March 2026 at 25% of total (Challenger report) — SEO/disruption context | SEJ/Matt Southern | 7/10 |
| 10 | ChatGPT Ads economics: $50K-$100K Criteo commitments, premium CPMs, ~80% SMB interest; self-serve expansion signals broader monetization push | SEJ/Reuters | 7/10 |

---

## Deep Dive 1: March 2026 Core Update — Rolling Now (April 3-4)

**Source:** SEJ, Google, April 3-4 2026
**Data scope:** Live rollout — day 1-2

### Status
- Google began rolling out March 2026 Core Update this week (March 27 start)
- As of April 3-4: **actively rolling** — industry volatility high
- Rollout may take up to 2 weeks total
- Spam update completed in under 20 hours (March 25) — precursor to core update
- Last broad core update: December 29, 2025 (3-month gap)

### Mueller: Multi-Team, Staged Deployment
John Mueller (Google Search Relations) clarified on Bluesky:
- Core updates don't use a single deployment mechanism
- Different teams/systems contribute changes
- Components require step-by-step rollouts
- Explains wave-like volatility pattern (not one-shot)

### Industry Impact
- Roger Montti notes spam update proximity may not be coincidence — spam clearing logically precedes quality reassessment
- Ranking changes expected throughout early April
- Google recommendation: wait at least 1 week after rollout finishes before analyzing Search Console data
- Compare against baseline period before March 27

---

## Deep Dive 2: Illyes Clarifies Googlebot 2MB Limit — Technical Deep Dive

**Source:** Google Blog "Inside Googlebot", SEJ reporting, April 1-2 2026
**Data scope:** Official Google documentation + podcast

### The 2MB Limit — What It Actually Means
- Googlebot is ONE client of a centralized crawling platform (15MB default)
- Google Shopping, AdSense, other products route through same system under different crawler names
- **HTTP request headers count toward the 2MB limit**
- **External resources (CSS, JS, images) each get separate byte counters**
- 2MB limit is a **Search-specific override** of the platform's 15MB default
- When Googlebot hits 2MB: it **stops fetching and passes truncated content to indexing as if complete** — anything past 2MB is NEVER indexed

### Illyes + Splitt Page Weight Discussion
- Median mobile homepage: 845 KB (2015) → 2,362 KB (2025) — ~3x growth (Web Almanac 2025)
- Illyes publicly questions whether Google's own structured data recommendations contribute to page bloat
- Splitt promises future episode on reduction techniques
- 2MB limit is a policy, not a permanent technical floor — may change as web evolves

### SEO Implications
- **Cyrus Shepard (Zyppy SEO):** If very large pages have content not getting indexed, check page size
- Large inline base64 images, heavy inline CSS/JS, oversized nav menus are primary culprits
- Structured data bloat is now an Illyes-raised concern — worth auditing

---

## Deep Dive 3: GEO Architecture Beyond llms.txt — 4-Layer Stack

**Source:** SEJ, Duane Forrester, April 2, 2026

### The Honest Problem With llms.txt
- llms.txt is a table of contents — flat, no relationship model
- Cannot express: Product A belongs to Family B, Feature X deprecated in v3.2, Person Z is spokesperson for Topic Q
- **Critical audit finding:** 1,000 AEM domain CDN logs — LLM bots essentially absent from llms.txt requests; Googlebot dominates
- Maintenance burden: every strategic change requires updating both live site AND the file
- Better approach: draw from authoritative data sources programmatically

### The 4-Layer Architecture
**Layer 1: JSON-LD as Machine-Facing Fact Layer**
- Pages with valid structured data: **2.3x more likely to appear in Google AI Overviews**
- Princeton GEO research: clear structural signals → **up to 40% higher visibility in AI-generated responses**
- Treat JSON-LD as machine-facing fact layer, not rich-snippet play
- Precision required on: product attributes, pricing states, feature availability, organizational relationships

**Layer 2: Entity Relationship Mapping**
- Express the graph, not just nodes
- Products → Categories → Industry Solutions → Use Cases → Authoritative Source
- Implement as JSON-LD graph extension OR headless CMS endpoint
- Eliminates flat-list hallucinations during AI comparison queries

**Layer 3: Content API Endpoints + Model Context Protocol**
- Programmatic, authoritative access to brand information
- Structured APIs replace static file maintenance
- Headless CMS as source of truth (no second content layer to maintain)

**Layer 4: Provenance Metadata**
- Timestamps, authorship, source chains
- Trust signals that travel with content through AI pipelines
- Longato AEM audit: provenance signals increasingly critical for AI citation decisions

### Strategic Implication
- llms.txt is a starting point, not a destination
- Standards landscape still forming — early architectural thinkers will define future patterns
- The question is not whether to build it, but how to prioritize the layers

---

## Deep Dive 4: ChatGPT Ads — $100M Pilot vs 0.91% CTR

**Source:** SEJ, Reuters, eMarketer, April 2-3 2026

### The Numbers
- **$100M+ annualized revenue** in first 6 weeks of US pilot (Reuters)
- **600+ advertisers** in pilot
- **$50K-$100K** Criteo commitment ranges reported (premium pricing)
- **~80% of SMBs** signaled interest in ChatGPT Ads
- Self-serve advertiser capabilities: launching April 2026
- Expansion into additional countries beyond US

### The CTR Problem
- Reported CTR: **as low as 0.91%** in ChatGPT (SEJ/eMarketer)
- Google Search benchmark: **6.4% average CTR**
- ChatGPT Ads CTR is approximately **7x lower** than Google Search
- This is the critical gap: momentum vs. proven channel value

### Strategic Assessment
- Pilot was clearly designed to be controlled, premium, brand-friendly (not ad-influences-answers)
- Premium CPMs and high barriers = not broad mid-market onboarding
- 0.91% CTR raises serious efficiency questions for performance advertisers
- $100M annualized sounds impressive but annualized ≠ $100M booked revenue (6-week pilot data annualized)
- For SEO/GEO professionals: ChatGPT Ads doesn't change AI citation dynamics — it adds a paid layer on top of an existing discovery behavior

---

## Deep Dive 5: Grokipedia — Continuing "Mt. AI" Collapse Post-Core Update

**Source:** SERoundTable, Glenn Gabe, April 2-3 2026

### The Pattern
- Grokipedia surged initially after scaling AI-generated content
- Then dropped heavily in Google (February 2026)
- Now: **continuing to drop with March 2026 Core Update**
- Same trajectory confirmed across: **Google Search, AI Overviews, AI Mode, ChatGPT**

### Glenn Gabe's "Mt. AI" Thesis — Confirmed
> "Drop in Google and you can drop heavily in AI Search."
- AI platforms (ChatGPT, AI Mode, AI Overviews) appear to run on existing Google index signals
- Sites that violate Google's quality signals likely face simultaneous penalties across all AI surfaces
- Favicon also gone missing (unrelated to algorithm, but compound reputational damage in SERPs)

### Lesson for SEOs
- AI-generated content scaling without genuine E-E-A-T signals is a high-risk strategy
- The "surge then drop" pattern is now documented across multiple AI platforms simultaneously
- "Beware Mt. AI" — Glenn Gabe's framing is becoming industry standard

---

## Comparison vs Topic 285

| Topic 285 | Topic 286 |
|-----------|-----------|
| SISTRIX Germany AIO CTR data (265M lost clicks) | March 2026 Core Update rolling live |
| Gemini tripled traffic, ChatGPT stagnant | Illyes 2MB Googlebot limit — technical deep dive |
| ChatGPT Ads cost disadvantage framing | ChatGPT Ads $100M pilot — CTR vs revenue paradox |
| Grokipedia initial collapse report | Grokipedia continuing to drop post-update |
| AI userbot ≠ AI citation (SISTRIX Beus) | llms.txt → 4-layer GEO architecture (Duane Forrester) |
| AIO category variance (health 24%+, recipes 1%) | Evergreen content disruption (-32pp publisher shift) |
| SISTRIX Q1 Changelog | Mueller sitemap splitting rationale |
| AIO cache distortion (1 bot visit = 1000s queries) | AI leads job cuts at 25% (Challenger, March 2026) |
| 60% Position-1 CTR drop in Germany | Structured data → 2.3x AIO inclusion rate |
| Google March Core Update starting | Self-serve ChatGPT Ads launching April |

---

## Key Quotes

### Mueller on Core Update Staging (Bluesky)
> "One is about spam, one is not about spam. If with some experience, you're not sure whether your site is spam or not, it's unfortunately probably spam."

### Illyes on 2MB Limit
> "When Googlebot hits 2MB, it stops fetching and passes the truncated content to indexing as if it were the complete file. Anything past 2MB is never indexed."

### Duane Forrester on GEO Architecture
> "llms.txt is a table of contents. That is a starting point, not a destination."

### SEJ on Evergreen Content Crisis
> "Fair to say the majority of evergreen content will not drive the value it did five years ago. The antithesis to AI slop will help your business be profitable."

---

## Sources
- SEJ: Google Core Update, Crawl Limits & Gemini Traffic Data (April 4, 2026)
- SEJ: ChatGPT Ads — New Acquisition Channel Or Just Another Brand Tax? (April 3, 2026)
- SEJ: Llms.txt Was Step One — Here's The Architecture That Comes Next (April 2, 2026)
- SEJ: Google Answers Why Some SEOs Split Their Sitemap Into Multiple Files (April 3, 2026)
- SEJ: How To Do Evergreen Content In 2026 (April 1, 2026)
- SEJ: AI Leads All Reasons For U.S. Job Cuts In March (April 2, 2026)
- SERoundTable: Grokipedia Continues To Drop in Search And AI Search (April 3, 2026)
- Google Blog: Inside Googlebot (via SEJ reporting)
- Reuters: OpenAI Ads Pilot Exceeds $100M Annualized Revenue (March 26, 2026)
- eMarketer: OpenAI ChatGPT Ads CTR data
- AEM CDN Audit: Longato.ch llms.txt analysis

---

*GenDate: 2026-04-04 18:10 GMT+8 — Round 245, Topic 286*
