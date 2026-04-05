# Knowledge File — Round 262 (topic290)

**Topic:** March 2026 Core Update Rolling Into April, AI Referral Traffic Wars: Gemini Overtakes Perplexity, Page Size vs. Crawl Budget Cracks, and the Pivot from Evergreen SEO to "Content With a Purpose"
**Round:** 262
**Date:** April 6, 2026
**Status:** LEARNER Complete

---

## Executive Summary

Round 262 captures the SEO landscape as the March 2026 Core Update continues its rollout into early April, with the March 2026 Spam Update already completed in under 20 hours. Three major developments define this cycle: (1) **Google Gemini has overtaken Perplexity as an AI referral traffic source** — doubling its traffic between November 2025 and January 2026, signaling a shift in the AI search referral ecosystem; (2) **Gary Illyes published detailed technical explainers** on Googlebot's 2MB byte limit and why page size genuinely matters for indexing — HTTP headers count toward the limit and content beyond 2MB is silently dropped; (3) **Evergreen content SEO is in structural decline** — AI Overviews have eroded informational click-through rates so severely that publishers are pivoting to "micro-conversion" content strategies with clear commercial purpose. The agentic web standards (MCP, A2A) continue maturing with NLWeb as Google's publisher-facing protocol, while SEOs are being told to think of GEO not as a tactic but as a byproduct of building a quality brand.

---

## 10 Key Findings

### Finding 1: March 2026 Core Update Is Rolling Into April — First Broad Core Update in 3 Months
**Source:** Search Engine Journal / Google Search Central
**Date:** March 27, 2026 (rollout began); extends into early April 2026

Google began rolling out the **March 2026 Core Update** on March 27, 2026 — the first broad core update since the December 2025 core update finished on December 29, 2025. This is a **three-month gap** between broad core updates. A separate February 2026 Discover Core Update only affected Google's Discover feed, not traditional Search rankings. Key facts:

- Rollout expected to take **up to 2 weeks**, meaning volatility continues into mid-April
- Google described it as a "regular update designed to better surface relevant, satisfying content from all types of sites"
- John Mueller confirmed on Bluesky that spam and core updates don't overlap mechanically — "one is about spam, one is not about spam" — but they may be logically related as part of Google's broader quality reassessment
- Mueller also clarified that core updates don't follow a single deployment mechanism — different teams contribute changes that may roll out in stages, explaining the wave-like pattern of ranking volatility

**Why it matters:** Sites that haven't seen ranking changes since December may finally see movement as April progresses. Google recommends waiting at least one week after the rollout finishes before analyzing Search Console data. Compare against a baseline period from before March 27.

---

### Finding 2: March 2026 Spam Update Completed in Under 20 Hours — Fastest Rollout Yet
**Source:** Ahrefs Google Algorithm Updates / Search Engine Journal
**Date:** March 24-25, 2026

The **March 2026 Spam Update** completed in under 20 hours — remarkably fast compared to typical multi-day spam update rollouts. This is the spam counterpart to the March 2026 Core Update, deployed just two days before the core update began. The speed suggests Google's spam detection systems have become more automated and precise. Sites impacted may be those "seeking short-term gains while ignoring best practices," per Google's standard spam update language.

**Why it matters:** The combination of a fast spam update followed immediately by a broad core update suggests Google is running a coordinated quality crackdown — spam elimination feeds into the broader content quality assessment in the core update.

---

### Finding 3: Gemini Referral Traffic More Than Doubles, Overtakes Perplexity — AI Search Referral Wars
**Source:** SE Ranking via Search Engine Journal
**Date:** January 2026 (data period: November 2025 – January 2026)

Google **Gemini more than doubled its referral traffic to websites** between November 2025 and January 2026 — a 115% combined increase over two months, coinciding with the Gemini 3 launch. In January 2026:

- **Gemini sent 29% more referral traffic than Perplexity globally**, and **41% more in the U.S.**
- ChatGPT still generates about **80% of all AI referral traffic**, but its lead over Gemini narrowed from ~22x in October 2025 to ~8x by January 2026
- All AI platforms combined account for about **0.24% of global internet traffic**, up from 0.15% in 2025 — still small but growing

**Why it matters:** For the first time, Gemini is sending more referral traffic than Perplexity. SEOs should add Gemini to their AI referral tracking alongside ChatGPT and Perplexity. This shifts the GEO (Generative Engine Optimization) conversation — Gemini's citation preferences may need dedicated optimization strategies.

---

### Finding 4: Gary Illyes Explains Googlebot's 2MB Byte Limit — HTTP Headers Count, External Resources Get Separate Counters
**Source:** Search Engine Journal / Google's Gary Illyes
**Date:** April 2026

Gary Illyes published a detailed technical blog post explaining **how Googlebot works within Google's centralized crawling architecture** and the mechanics of the 2MB byte limit Google published earlier in 2026:

- Googlebot is **one client of a centralized crawling platform** — Google Shopping, AdSense, and other products route requests through the same system under different crawler names
- **HTTP request headers count toward the 2MB limit** — meaning large cookie headers or custom headers consume crawl budget
- **External resources (CSS, JavaScript) get their own separate byte counters** — they don't double-count against the page HTML limit
- When Googlebot hits 2MB, it **stops fetching and passes the truncated content to indexing as if it were complete** — anything past 2MB is never indexed, silently
- The 2MB limit is a **Search-specific override of the platform's 15MB default** — other Google clients have different limits
- The limit is **not permanent** and may change as the web evolves

**Why it matters:** Pages with large inline base64 images, heavy inline CSS/JavaScript, or oversized navigation menus may have content silently dropped from indexing. SEOs should verify critical content loads within the first 2MB, especially for large pages.

---

### Finding 5: Pages Are Getting Larger — Median Mobile Homepage Hits 2,362 KB; Structured Data Bloat Questioned
**Source:** Search Engine Journal / Google's Gary Illyes and Martin Splitt
**Date:** April 2026

On a **Search Off the Record podcast**, Gary Illyes and Martin Splitt discussed page weight growth and its impact on crawling:

- Web pages have grown **nearly 3x over the past decade**
- The 2025 Web Almanac reports a **median mobile homepage size of 2,362 KB** — approaching but still below the 2MB (2,048 KB) Googlebot limit
- Illyes raised the question of whether **structured data that Google asks websites to add is contributing to page bloat** — an noteworthy self-critical observation from Google
- Splitt said he plans to address specific techniques for reducing page size in a future episode

**Why it matters:** While the median page is technically under 2MB, the margin is thin. Sites adding extensive schema markup, AI-generated content, or interactive elements could easily exceed the limit. Google's own question about structured data bloat is notable — publishers following Google's rich results recommendations may be inadvertently harming their own crawl efficiency.

---

### Finding 6: Multi-Sitemap Strategies Validated by John Mueller — Organization Over Simplicity
**Source:** Search Engine Journal / Google's John Mueller
**Date:** April 2026

John Mueller answered a question on Reddit about **why websites split sitemaps into multiple files** rather than keeping everything in one place. His answer validated several legitimate use cases:

- **Tracking different URL groups** (e.g., product detail pages vs. product category pages) — enables grouping in the Page Indexing Report
- **Split by content freshness** — evergreen content in a separate sitemap; theoretically a search engine might check it less often (unconfirmed)
- **Proactively splitting** to avoid hitting the 50,000 URL cap urgently
- **Hreflang sitemaps** — can take significant space; the 50K URL limit could make files too large
- **Automated sitemap generation** — "my computer did it, I don't know why"

**Why it matters:** Enterprise SEOs have long used multi-sitemap strategies for organizational and tracking purposes. Mueller's confirmation provides Google's explicit endorsement of these approaches. Not all sitemap complexity is unnecessary — some reflects genuine technical and strategic needs.

---

### Finding 7: Evergreen Content SEO Is in Structural Decline — "Bread-and-Butter" Content No Longer Profitable
**Source:** Search Engine Journal — "How To Do Evergreen Content In 2026 (And Beyond)"
**Date:** April 1, 2026

A major analysis on Search Engine Journal made the case that **traditional evergreen SEO content is structurally losing value**:

- **AI Overviews have eroded clicks** for informational queries — users get answers directly in the SERP
- Publishers report they plan to focus on **more original investigations and less on evergreen content** (down 32 percentage points per Reuters Institute survey)
- The affiliate cull of sites like Forbes Advisor demonstrated that **quantity over quality at scale no longer works**
- E-E-A-T requirements have **raised the cost of quality content** — working with experts, unique imagery, video, data — while simultaneously reducing the traffic value of that content
- The new content tiering model: **Tier 1 = revenue/conversions; Tier 2 = registrations, links, shares; Tier 3 = page views, engagement metrics**

**Why it matters:** The traditional "build it and they will come" evergreen content strategy — create a comprehensive guide, update it annually, collect traffic — is economically broken for most publishers. Content must now have a clear commercial purpose or audience journey role from the moment it's commissioned.

---

### Finding 8: GEO as a Byproduct, Not a Tactic — "Being Cited in AI Is a Happy Byproduct of Building a Quality Brand"
**Source:** Search Engine Journal — "How To Do Evergreen Content In 2026 (And Beyond)"
**Date:** April 1, 2026

The article makes a critical reframing of the GEO (Generative Engine Optimization) debate:

- "Everyone is obsessed with getting cited or being visible in AI" — the **wrong approach**
- Getting cited in AI should be framed as **"a happy byproduct of building a quality brand with an efficient, joined-up approach to marketing"**
- The five content pillars for the AI era: **(1) Strategy first, automation second** — AI as infrastructure, not a shortcut; **(2) Visceral storytelling** — safe content is invisible content; **(3) Multimodal optimization**; **(4) Audience psychology and analytics**; **(5) Ethics and authenticity**
- Prompting AI is **like briefing a junior writer** — a vague brief produces generic fluff; a structured brief with context, constraints, and tone guidelines produces usable output

**Why it matters:** The GEO gold rush has led many publishers to chase AI citations as a primary tactic. The more sustainable framing is that GEO success is a lagging indicator of brand quality, authority, and content distinctiveness — not something that can be reverse-engineered through technical hacks alone.

---

### Finding 9: The 5-Pillar AI Content Trust Framework — Why Volume Doesn't Fix the Trust Crisis
**Source:** Search Engine Journal — "The 5-Pillar Framework For AI Content That Audiences Actually Trust"
**Date:** April 4, 2026

A detailed framework for content that performs in the AI era identifies **three forces eroding trust simultaneously**:

1. **Algorithmic gatekeeping** — platforms built AI filters that detect and suppress low-quality, inauthentic content
2. **The authenticity crisis** — consumers in 2026 can detect generic AI-generated output ("slop") instantly; the brain is a prediction machine that ignores what it can easily predict
3. **Audience sophistication** — readers have now seen tens of thousands of AI-generated pieces and developed pattern recognition

The five-pillar framework:
- **Pillar 1:** AI-powered content strategy — strategy first, automation second; build architecture before prompting
- **Pillar 2:** Visceral storytelling — limbic system reacts before logic; emotional permission must be granted before reason engages
- **Pillar 3:** Multimodal optimization — text alone is no longer sufficient; video, data visualizations, unique imagery
- **Pillar 4:** Audience psychology and analytics — micro-conversions over clicks; focus on behaviors that lead to valuable conversions
- **Pillar 5:** Ethics and authenticity — getting this wrong undermines everything else

**Why it matters:** The framework provides a practical structure for creating content that survives both AI filters and human skepticism. Brands that invest in authentic, distinctive content will increasingly stand out as AI-generated "slop" becomes the default baseline.

---

### Finding 10: MCP Hits 97M Monthly SDK Downloads; A2A Has 150+ Supporting Organizations — Agentic Web Standards Accelerating
**Source:** Search Engine Journal — "MCP, A2A, NLWeb, And AGENTS.md: The Standards Powering The Agentic Web"
**Date:** April 2026

The article tracks the **maturation of standards powering the agentic web**:

- **MCP (Model Context Protocol):** Anthropic's open standard for connecting AI apps to tools/data/workflows; reached **97 million monthly SDK downloads** in just over a year; adopted by OpenAI (March 2025), Google (April 2025), and Microsoft (May 2025); over **10,000 public MCP servers** built by the community
- **A2A (Agent2Agent Protocol):** Google's protocol for agent interoperability; launched April 9, 2025; donated to Linux Foundation June 2025; **version 0.3 shipped with 150+ supporting organizations** including Salesforce, SAP, ServiceNow, PayPal, Atlassian, Microsoft, AWS
- **NLWeb:** Google's proposed standard for making website content machine-readable — positioned as the publisher-facing layer of the agentic web
- **AGENTS.md:** A proposed standard for how AI agents should interact with websites and services

The Linux Foundation's **Agentic AI Foundation (AAIF)** now has 8 platinum members: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, and OpenAI — competitors building shared infrastructure.

**Why it matters:** The agentic web infrastructure is being built by the same companies that compete in AI. Publishers should monitor NLWeb developments as a potential future-proofing strategy for making their content agent-accessible.

---

## Key Theme This Round

**"Crawl Budget Cracks, Referral Traffic Shifts, and the Death of Set-It-And-Forget-It Content"**

The dominant theme of Round 262 is the **convergence of three quiet crises** in SEO:

1. **A technical crisis** — Googlebot's 2MB limit is now a real indexing boundary, not theoretical; pages that exceed it silently lose content from Google's index; this affects not just large pages but any page where HTTP overhead + HTML + inline resources exceed 2MB
2. **A traffic crisis** — Gemini is now a legitimate referral source, but AI platforms collectively still represent only 0.24% of internet traffic; the promise of AI referral traffic replacing organic search remains overstated in the near term
3. **A content economics crisis** — the traditional evergreen content model (comprehensive guides, updated annually, passive traffic) is economically broken; AI Overviews have structurally changed the value equation; publishers must now justify every content investment against a clear commercial purpose

The through-line: **the old SEO playbook — create comprehensive content, optimize for keywords, build links, wait for rankings — is insufficient in 2026**. The new playbook requires technical precision (crawl budget, page size, structured data efficiency), strategic clarity (why does this content exist in the customer journey?), and creative distinctiveness (why would a human choose this over AI-generated slop?).

---

## Related Prior Rounds

- **Round 261** (topic289): The Zero-Click Search Era & AI Trust Crisis — 55-65% no-click rate, March 2026 Core Update rollout begin, 5-Pillar AI Content Trust Framework
- **Round 260** (topic288): Agentic Web Standards — MCP, A2A, NLWeb, Publisher Traffic Crisis
- **Round 259** (topic287): GEO vs. SEO Convergence — AI citation optimization, brand authority for AI search
- **Round 258** (topic286): Helpful Content System Evolution — E-E-A-T as the core ranking signal, author expertise requirements
- **Round 257** (topic285): December 2025 Core Update Fallout — 3-month gap analysis, ranking volatility patterns

---

*Next Round Forward: The March 2026 Core Update is expected to complete its rollout by approximately April 10, 2026. Watch for post-update ranking recovery patterns, AI referral traffic tracking (especially Gemini's sustained growth trajectory), and any new Google guidance on the 2MB crawl limit.*
