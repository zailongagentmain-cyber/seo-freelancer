# Round 208 Learner Log

**Date:** April 1, 2026  
**Topic Produced:** 252  
**Theme:** The Agentic Web — From Crawled Content to Machine-Legible Infrastructure  
**Files Produced:** `knowledge-latest-round208.md`, `knowledge-latest.md` (overwrite)

---

## Research Process

### Step 1: Read Topic 251 (knowledge-latest.md)
Confirmed Topic 251 covered: TurboQuant, Dual-Memory Architecture, ClaudeBot 38K:1 ratio, Bing as backbone, Dynamic GBP, Publisher Traffic Collapse 42%, digitalSourceType, E-commerce GEO study (Columbia/MIT), University of Toronto earned media dominance, Citation attempts KPI, IndexNow protocol, AI Overview 1-in-4 trigger rate, Bing grounding, entity-first indexing.

### Step 2: Web Research

**Sources scraped:**

1. **Search Engine Journal** (searchenginejournal.com) — SEO news front page
   - Fetched: "The Science Of What AI Actually Rewards" (Kevin Indig, Part 3) — https://www.searchenginejournal.com/the-science-of-what-ai-actually-rewards/570849/
   - Fetched: "Why Google's New 'Google-Agent' Is The Biggest Mindset Shift In SEO History" (Marie Haynes) — https://www.searchenginejournal.com/why-googles-new-google-agent-is-the-biggest-mindset-shift-in-seo-history/570590/
   - Fetched: "Google Begins Rolling Out March 2026 Core Update" — https://www.searchenginejournal.com/google-begins-rolling-out-march-2026-core-update/570657/
   - Fetched: "So Your Traffic Tanked: What Smart CMOs Do Next" — https://www.searchenginejournal.com/so-your-traffic-tanked-what-smart-cmos-do-next/570708/
   - Fetched: "Answer Engine Optimization: How To Get Your Content Into AI Responses" — https://www.searchenginejournal.com/answer-engine-optimization-how-to-get-your-content-into-ai-responses/570055/
   - Fetched: "Google Tests AI Headlines, Rolls Out Spam Update – SEO Pulse" — https://www.searchenginejournal.com/seo-pulse-google-tests-ai-headlines-rolls-out-spam-update/570613/
   - Fetched: "Google Explains Googlebot Byte Limits And Crawling Architecture" — https://www.searchenginejournal.com/google-explains-googlebot-byte-limits-and-crawling-architecture/570961/
   - Fetched: "Google: Pages Are Getting Larger & It Still Matters" — https://www.searchenginejournal.com/google-pages-are-getting-larger-it-still-matters/570875/

2. **Semrush Blog** (semrush.com/blog/)
   - Fetched: "Google's releasing Google-Agent: Here's what to know" — https://www.semrush.com/blog/google-ai-agent/
   - Fetched: "The agentic web: How AI agents decide which brands make the cut" — https://www.semrush.com/blog/the-agentic-web/
   - Fetched: "What Is an AI Agent? (And What AI Agents Mean for Your Brand's Visibility)" — https://www.semrush.com/blog/what-is-an-ai-agent/
   - Fetched: "How One SEO Consultant Turns Semrush's AI Sentiment Insights into Traffic and Visibility" — https://www.semrush.com/blog/turning-ai-sentiment-insights-into-visibility/

3. **Web Search** (Gemini, rate-limited after ~4 calls)
   - "AI search citation Perplexity ChatGPT Gemini April 2026 new research" → returned broad synthesis on Perplexity vs. ChatGPT vs. Gemini citation patterns, Perplexity's 90%+ community platform citation rate
   - "Perplexity Gemini Claude citation study 2026 ranking factors" → returned Yext Research Claude UGC citation finding, multi-model optimization concept, Perplexity 40% faster research finding

### Step 3: What Was Genuinely New vs. Already Covered

**Already covered in Topic 251 (NOT duplicated):**
- TurboQuant
- Dual-Memory Architecture
- ClaudeBot 38K:1 ratio
- Bing as backbone / IndexNow (acknowledged but new angle on Perplexity building Sonar index and OpenAI building own index)
- Dynamic GBP
- Publisher Traffic Collapse 42% (organic traffic decline mentioned again but with NEW 40% month-over-month answer engine growth stat)
- digitalSourceType (new documentation update details)
- E-commerce GEO study (Columbia/MIT)
- University of Toronto earned media dominance (reaffirmed with new detail on consumer electronics 92.1% vs 54.1%)
- Citation attempts KPI

**New findings in Topic 252:**
1. Agentic web protocol stack (MCP, A2A, UCP, A2UI, AG-UI) — live production standards
2. Google-Agent user-triggered crawler — Project Mariner, first action-oriented crawler
3. WebMCP — native agent-to-backend interaction, not pixel scraping
4. AI headline rewrites in traditional search (not just Discover)
5. March 2026 core update (first broad core update of 2026)
6. March 2026 spam update fastest ever (under 20 hours)
7. Bing Webmaster Tools grounding query → cited page mapping
8. Kevin Indig Part 3: declarative intro +14%, KG-verified entities 0.81x, 3-4 headings dead zone
9. Bing as distribution for non-Google engines (Perplexity Sonar, OpenAI plans)
10. Delegate economy concept — awareness + conversion collapsing
11. Answer engine traffic: 40% MoM growth, 23-word queries, 23-min sessions, 2-4x conversion
12. Semrush case study: AI Overview 17%→35% in 5 months via sentiment control
13. Nick Fox / Liz Reid: "Search is becoming AI Search" and "agents talking to each other"
14. digitalSourceType structured data documentation update (new implementation details)
15. Gary Illyes: HTTP headers count toward 2MB limit, 3x page weight growth
16. Claude Constitutional AI → higher UGC citation rate (Yext Research)

### Git Commit

```
git add knowledge-latest-round208.md knowledge-latest.md round208-learner-log.md
git commit -m "Round 208: Topic 252 - Agentic Web, Google-Agent, WebMCP, March 2026 Core Update, AI citation science"
```

### Challenges Encountered
- Web search hit 429 rate limit after ~4 successful calls (Gemini free tier: 20 requests/day)
- Had to switch to targeted web_fetch for specific article URLs rather than broad search queries
- Most high-value content came from fetching specific SEJ and Semrush article pages
- Content from late March 2026 (March 27-31) was the freshest available as of April 1, 2026
