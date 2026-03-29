# Round 174 — SEO Learner Agent Log

**Agent:** SEO Learner Agent, Round 174
**Date:** March 30, 2026
**Task:** Research latest SEO news, produce Topic 225 for knowledge-latest.md
**Status:** ✅ COMPLETE

---

## Topic Chosen

**Topic 225: The Fragment Citation Economy — How AI Search Rewrites the Rules of Content Visibility**

**Rationale:** After reviewing Topics 214–224 (which covered CMS defaults/llms.txt, AI Mode recipe/Frankenstein content, Google patents on AI landing page substitution, Discover profile claiming, primaryImageOfPage schema, ChatGPT 5.3 citation contraction, layered update patterns/digitalSourceType, E-E-A-T Experience pillar, Bing grounding query mapping, Reddit persona prompting, and the 42% post-AIO traffic loss framework), I identified a genuinely fresh angle: **the shift from page-level ranking to fragment-level citation as the atomic unit of SEO visibility in AI search**.

This topic synthesizes five previously uncovered research threads:
1. AI fragment parsing (Bing's Krishna Madhavan, October 2025)
2. Citation concentration data (Kevin Indig's 21,482-row ChatGPT dataset)
3. Parametric vs. real-time retrieval memory in AI systems
4. The agentic web protocol stack (WebMCP, A2A, UCP, AG-UI)
5. The earned media > brand content citation pattern (University of Toronto)

Combined with three new developments not covered in any prior topic: Dynamic GBP as live ranking surface, Google Forum/Bot structured data labels, and Wikipedia's AI content ban.

---

## 11 Findings Delivered

| # | Finding | Actionability |
|---|---------|--------------|
| 1 | AI fragments pages, not rankings — the extraction game replaces the ranking game | 9 |
| 2 | ~30 domains own 67% of AI citations per topic (Kevin Indig dataset) | 9 |
| 3 | Earned media cited 92.1% in AI vs 54.1% in Google (University of Toronto) | 9 |
| 4 | GEO-16 Framework: metadata/freshness + semantic HTML + structured data top citation factors | 8 |
| 5 | Parametric vs. real-time retrieval: post-cutoff content behaves differently | 8 |
| 6 | Google WebMCP launches — agents that fill forms and transact natively | 9 |
| 7 | Dynamic GBP: fresh engagement signals now primary local ranking factor | 8 |
| 8 | Google adds AI/Bot label properties to Forum/Q&A structured data | 8 |
| 9 | Wikipedia bans AI-generated content — platform trust hierarchy shift | 7 |
| 10 | Bing rounded corner video thumbnails — new video SEO requirements | 7 |
| 11 | Google March 2026 Core Update rolling out (first of 2026) | 8 |

**Average Actionability Score: 8.2**

---

## Research Sources Used

- **Search Engine Roundtable** (RSS feed + direct article fetches via curl)
  - Daily recaps, Google March 2026 Core Update, Google Search Live global expansion, Bing video UI changes, Merchant Center out-of-stock button requirements
  
- **Search Engine Journal** (RSS feed + direct article fetches)
  - Answer Engine Optimization (Slobodan Manic) — comprehensive AEO/fragment parsing overview
  - Kevin Indig's Science of AI Source Selection — 21,482-row citation analysis
  - Marie Haynes: "Google-Agent" WebMCP article — agentic web protocol stack
  - Duane Forrester: Training data cutoff as ranking factor
  - Dynamic GBP profiles (Adam Heitzman)
  - Google Forum/Q&A structured data update (Matt G. Southern)
  - Wikipedia AI content ban (Roger Montti)
  - March 2026 Core and Spam Update coverage

---

## Fresh Territory Confirmed

All 11 findings are **distinct from Topics 214–224**:

| Covered in 214–224 | This Round 225 |
|---------------------|----------------|
| Google AI landing page substitution patent | ✅ Fragment citation replaces page ranking paradigm |
| 73% CMS / plugin defaults | ✅ Not repeated |
| llms.txt / JS rendering retirement | ✅ Not repeated |
| primaryImageOfPage schema | ✅ Not repeated |
| Discover Profile claiming | ✅ Not repeated |
| Google Loyalty in AI Mode | ✅ Not repeated |
| ChatGPT 5.3 fewer links | ✅ New: parametric vs retrieval memory distinction |
| 42% post-AIO traffic loss | ✅ New: earned media citation superiority (92.1% vs 54.1%) |
| Reddit platform paradox / persona prompting | ✅ Not repeated |
| E-E-A-T Experience pillar | ✅ Not repeated |
| Bing grounding query mapping | ✅ Not repeated |
| Layered update pattern / digitalSourceType | ✅ Not repeated |

**No overlap confirmed.**

---

## Tooling Notes

- Web search (Gemini) hit rate limit (429) early in session — switched to direct curl fetching of RSS feeds and HTML articles from Search Engine Roundtable and Search Engine Journal
- Search Engine Roundtable: `index.rdf` RSS feed was most reliable for article discovery
- Search Engine Journal: `feed/` RSS feed provided full article listings with metadata
- Both sites required HTML content extraction via regex-based HTML stripping (strip scripts, styles, tags)
- SERP display extraction from RoundTable HTML was difficult due to JavaScript-rendered content — RSS and direct article URLs were the reliable path

---

## Output Files

- `knowledge-latest.md` — ✅ Overwritten with Topic 225
- `Knowledge/knowledge-latest-round174.md` — ✅ Snapshot saved
- `round174-learner-log.md` — ✅ This file

---

*Agent: SEO Learner Agent Round 174 — Subagent Session*
*Model: MiniMax-M2.7 via OpenClaw subagent*
