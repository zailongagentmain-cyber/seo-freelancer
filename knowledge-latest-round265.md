# Knowledge File — Round 265 (topic293)

**Topic:** March 2026 Core Update Nears Completion, Googlebot 2MB Byte Limit Explained, llms.txt Beyond → Machine-Readable Brand API Stack, MCP/A2A/NLWeb/AGENTS.md — The Agentic Web Standards, AI Shopping Fails to Threaten SEO
**Round:** 265
**Date:** April 6, 2026
**Status:** LEARNER Complete

---

## Executive Summary

Round 265 arrives at the likely completion window of the March 2026 Core Update (~April 6–10). The update is in its final stages, and SEO professionals are beginning to assess its impact. Three major developments frame this cycle: (1) **Google's Gary Illyes clarified the 2MB Googlebot byte limit** — explaining that it's a Search-specific override of a 15MB platform default, and that content past the limit is simply never indexed rather than rejected; (2) **The post-llms.txt architecture debate has crystallized** — industry voices are pushing beyond the flat file approach toward a layered machine-readable content stack: JSON-LD fact sheets, entity relationship graphs, provenance APIs, and AI-specific endpoints; (3) **The agentic web standards landscape is taking shape** — MCP (Model Context Protocol), A2A (Agent-to-Agent), NLWeb, and AGENTS.md are emerging as competing/adjacent protocols that publishers and brands need to understand. Additional developments include ChatGPT Ads launching as a new acquisition channel, the WordPress/Cloudflare EmDash drama, and evidence that AI agentic shopping still feels unnatural to users and poses less SEO threat than feared.

---

## 10 Key Findings

### Finding 1: March 2026 Core Update — Likely Completion Window (April 6–10)
**Source:** Search Engine Journal / Search Engine Roundtable / The HOTH
**Date:** April 4–6, 2026 (rollout started March 27; expected completion ~2 weeks)

The March 2026 Core Update is approaching its expected completion window:

- Google began rolling out the March 2026 Core Update on March 27 — the first broad core update of 2026
- The rollout was expected to take up to two weeks, putting completion at approximately April 6–10
- Glenn Gabe and other rank trackers have been documenting significant ranking movements throughout the rollout
- John Mueller clarified on Bluesky that core updates don't follow a single deployment mechanism — different teams and systems contribute changes that require step-by-step rollouts over weeks
- Roger Montti noted the proximity of the March spam update (completed in under 20 hours, March 24–25) may have fed into the broader quality assessment
- SEO professionals are reporting that the wave-like volatility pattern continues as different Google systems contribute to the rollout at different times
- Google recommends waiting **at least one full week after the rollout finishes** before analyzing Search Console data — meaningful analysis not possible until approximately April 13–17

**Why it matters:** The December 2025 core update was the previous broad core update. Sites haven't had their rankings recalibrated since late December 2025. The completion of this update represents the most significant recalibration of Google Search rankings in over three months.

---

### Finding 2: Gary Illyes Explains Googlebot's 2MB Byte Limit — Content Past Limit Is Never Indexed
**Source:** Search Engine Journal / LinkedIn (Cyrus Shepard)
**Date:** April 3–4, 2026

Google's Gary Illyes, an analyst on Google's Search team, published a detailed blog post explaining how Googlebot works within Google's broader crawling infrastructure:

- **Googlebot is one client of a centralized crawling platform** — Google Shopping, AdSense, and other products all route requests through the same system under different crawler names
- **The 2MB limit is a Search-specific override** of the platform's 15MB default — other crawlers in Google's ecosystem may have different limits
- **HTTP request headers count toward the 2MB limit** — this is often overlooked by SEO professionals
- **External resources (CSS, JavaScript) get their own separate byte counters** — they don't count against the page's fetch budget
- **When Googlebot hits 2MB, it doesn't reject the page** — it stops fetching and passes the truncated content to indexing as if it were complete; anything past 2MB is simply never indexed
- **The 15MB platform default and 2MB Googlebot override** explains why different Google crawlers behave differently in server logs — each client sets its own configuration
- Illyes noted the 2MB limit is **not permanent and may change** as the web evolves

Cyrus Shepard commented on LinkedIn: "If you notice certain content not getting indexed on VERY LARGE PAGES, you probably want to check your size."

**Why it matters:** Large pages with heavy inline base64 images, oversized CSS/JavaScript, or bloated navigation menus may have content that is simply never indexed. This is a technical SEO issue that could cause important content to be invisible to Google.

---

### Finding 3: Pages Are Getting Larger — 3x Growth in a Decade, and Illyes Questions Structured Data Bloat
**Source:** Search Engine Journal (Search Off the Record podcast)
**Date:** April 2–4, 2026

Gary Illyes and Martin Splitt, Developer Advocate at Google, discussed page weight growth on a recent Search Off the Record podcast episode:

- **Web pages have grown nearly 3x over the past decade** — the 2025 Web Almanac reports a median mobile homepage size of 2,362 KB
- The 15MB default applies across Google's broader crawling systems, with individual clients like Googlebot for Search overriding it downward to 2MB
- Illyes **raised whether structured data that Google asks websites to add is contributing to page bloat** — this is a significant admission from a Google engineer
- Pages that were 2MB+ but safely below the platform's 15MB default are now affected by Googlebot's 2MB Search-specific limit
- The implication: as Google asks for more structured data (JSON-LD, schema.org markup), pages grow, and Googlebot's more restrictive limit catches more content

**Why it matters:** Publishers adding extensive structured data markup need to be aware that this contributes to byte count. The 2MB Googlebot limit means content past that threshold is never indexed — including structured data that may be used for AI Overviews. There's a tension between Google's demand for more structured data and its own indexing limits.

---

### Finding 4: Beyond llms.txt — The Machine-Readable Brand Content Stack Takes Shape
**Source:** Search Engine Journal
**Date:** April 2, 2026

The debate over what comes after llms.txt has crystallized into a more structured framework:

- **llms.txt's honest value is legibility** — it provides a clean path into content by flattening it into Markdown, but it has no relationship model
- The structural problem with llms.txt: **it cannot express relationships** between products, features, people, or topics — it's a flat list with no graph
- A proposed layered architecture has emerged (not requiring everything built at once):
  - **Layer 1 — Structured Fact Sheets (JSON-LD)**: Pages with valid structured data are 2.3x more likely to appear in Google AI Overviews; JSON-LD should be treated as a machine-facing fact layer, not just a rich-snippet play
  - **Layer 2 — Entity Relationship Mapping**: Expressing the graph (products → categories → solutions → use cases), implemented as JSON-LD graph extension or headless CMS endpoint
  - **Layer 3 — Provenance APIs**: Programmatically authoritative data sources, reducing the manual maintenance burden of llms.txt
  - **Layer 4 — AI-Specific Endpoints**: Direct machine-readable content feeds designed for AI consumption
- An audit of CDN logs across 1,000 Adobe Experience Manager domains found **LLM-specific bots were essentially absent from llms.txt requests** — Googlebot accounted for the vast majority of file fetches
- The maintenance burden of llms.txt (updating both live site and the file for every change) is an **operational liability for enterprise brands**

**Why it matters:** Brands need to think beyond llms.txt as a checkbox exercise and toward a programmatic, layered content architecture that AI systems can actually consume and cite accurately. The flat file approach won't scale for complex brand content.

---

### Finding 5: MCP, A2A, NLWeb, AGENTS.md — The Standards Powering the Agentic Web
**Source:** Search Engine Journal
**Date:** April 4, 2026

Search Engine Journal published a guide on the emerging standards for the agentic web:

- **MCP (Model Context Protocol)** — An Anthropic-developed protocol for connecting AI models to external data sources and tools; becoming widely adopted as a de facto standard for AI agent content access
- **A2A (Agent-to-Agent)** — A protocol for AI agents to communicate with each other; relevant for multi-agent workflows that may involve content discovery and citation
- **NLWeb** — Mozilla's project to make web content machine-readable through a protocol layer; positioned as an evolution of RSS for the AI era
- **AGENTS.md** — A proposed standard for documenting how AI agents should interact with websites; similar to robots.txt but designed for AI agents rather than crawlers
- These standards are **still forming** — no major AI platform has formally committed to consuming any of them, but early adopters are experimenting
- The article notes that **publishers who understand these protocols early will define the patterns that become standards** — similar to how early adopters of structured data shaped Schema.org

**Why it matters:** As AI agents become a significant consumer of web content, the protocols they use for content discovery and interaction will shape SEO. Understanding MCP, A2A, NLWeb, and AGENTS.md now positions publishers to be early adopters of the next wave of web standards.

---

### Finding 6: Agentic AI Shopping Still Feels Unnatural — May Not Threaten SEO as Feared
**Source:** Search Engine Journal
**Date:** April 3, 2026

An analysis of AI shopping agents found:

- **Agentic AI shopping experiences still feel unnatural to users** — early implementations require significant cognitive load to set up and monitor
- Unlike traditional search (where intent is expressed in a single query), AI shopping agents require multi-step conversations, preference setting, and trust establishment
- The research suggests **users may prefer AI shopping agents for high-stakes, infrequent purchases** (cars, appliances) but stick with traditional search for everyday shopping
- The SEO threat from AI shopping agents may be lower than feared because:
  - Users resist delegating purchasing decisions to AI agents
  - The "last mile" problem — getting users to hand over payment and trust AI to complete transactions — remains unsolved
  - Retailer control over product data and pricing creates fragmentation that AI agents struggle to navigate

**Why it matters:** SEO professionals worried about AI agents replacing search-based product discovery can take some comfort — the user adoption curve for fully agentic shopping is likely to be gradual. However, the implications for product data quality and machine-readable content remain significant.

---

### Finding 7: ChatGPT Ads Launch — New Acquisition Channel or Brand Tax?
**Source:** Search Engine Journal
**Date:** April 3, 2026

OpenAI launched advertising in ChatGPT:

- ChatGPT Ads have begun appearing in ChatGPT's chat interface, creating a **new acquisition channel for brands**
- Early performance data is mixed — some brands report good results for top-of-funnel awareness, while others question the ROI for direct response
- The chat context of ChatGPT Ads creates **different user intent signals than search advertising** — users in a conversational AI context may be in a different mindset than users actively searching for products
- Advertisers need to consider **creative and messaging strategies suited to conversational contexts** — traditional search ad copy may not convert in chat interfaces
- The pricing model and targeting capabilities are still maturing

**Why it matters:** ChatGPT Ads represent the first major advertising format within a conversational AI interface. As AI-native platforms grow their ad businesses, marketers need to develop new creative and targeting strategies for chat-based advertising.

---

### Finding 8: Google Explains Why SEOs Split Sitemaps — No Direct Ranking Benefit
**Source:** Search Engine Journal
**Date:** April 3, 2026

John Mueller answered a question about why some SEOs split their XML sitemaps into multiple files:

- **Splitting sitemaps has no direct ranking benefit** — Google processes all sitemap types equivalently
- Reasons SEOs split sitemaps:
  - **Organization**: Large sites with hundreds of thousands of URLs benefit from logical separation (by section, content type, language)
  - **Maintenance**: Teams can manage their section without affecting others
  - **Diagnostics**: Easier to identify which section has crawl or indexing issues
  - **Prioritization**: Some SEOs use separate sitemaps for different priority tiers
- Mueller noted that Google handles multi-sitemap setups just as efficiently as single files — **the benefit is entirely operational, not algorithmic**

**Why it matters:** Large sites using multiple sitemaps for "SEO purposes" can simplify their approach — the sitemap structure has no ranking impact. Focus on the operational benefits (organization, maintenance, diagnostics) rather than SEO value.

---

### Finding 9: AI Led All Reasons for U.S. Job Cuts in March at 25% — Challenger Report
**Source:** Search Engine Journal (Challenger, Gray & Christmas)
**Date:** April 2, 2026

The March 2026 jobs report from outplacement firm Challenger, Gray & Christmas found:

- **AI led all cited reasons for U.S. job cuts in March at 25% of the total** — the single largest reason for layoffs
- This is consistent with the broader trend of AI automation displacing roles in customer service, content creation, data entry, and basic analysis
- The SEO and digital marketing industries are seeing effects in:
  - Reduced demand for basic SEO task execution (keyword research, meta tag writing)
  - Consolidation of junior-level roles
  - Growing demand for AI supervision and strategy-level skills
- The 59% senior-level SEO job composition (from Finding 6 of Round 264) is consistent with this trend — entry-level work is being automated, leaving senior strategy roles

**Why it matters:** The job market data confirms what SEO professionals are observing anecdotally — AI is automating basic SEO and content tasks. Professionals need to develop senior-level, AI-supervisory skills to remain competitive.

---

### Finding 10: WordPress vs. Cloudflare EmDash — The CMS Wars Heat Up
**Source:** Search Engine Journal
**Date:** April 2–3, 2026

Matt Mullenweg (WordPress) responded to Cloudflare's new EmDash CMS:

- Cloudflare launched EmDash as a streamlined WordPress alternative — prompting Mullenweg to publicly respond
- Mullenweg invoked the Will Smith Oscars slap metaphor ("Keep WordPress out of your mouth") in his response
- SEO implications of the WordPress vs. EmDash competition:
  - **WordPress powers ~43% of all websites** — any change in WordPress's competitive position affects the largest segment of the web
  - Cloudflare's EmDash offers edge-deployed, performance-optimized hosting — potentially addressing WordPress's historical performance weaknesses
  - If EmDash gains traction, **SEO tools and plugins built on WordPress infrastructure** may need to develop EmDash equivalents
  - The debate highlights the ongoing shift toward **edge-computed, performance-first web publishing** — a trend with direct SEO implications

**Why it matters:** The CMS landscape is evolving rapidly. Cloudflare's entry into the CMS market signals that performance (Core Web Vitals, edge computing) will be a competitive differentiator. SEO professionals managing WordPress sites should monitor whether EmDash or similar edge-native platforms gain meaningful market share.

---

## Related Existing Topics
- topic288: Agentic Web Standards — MCP, A2A, NLWeb, and structured content architecture (directly related to Finding 5)
- topic285: Verified Source Packs — AI citation patterns and authoritative sources (context for Findings 4–5)
- topic292: March 2026 Core Update Week Two, Google Zero 65% No-Click (context for Finding 1)
- topic282: GEO/AEO and the Fall of Traditional SEO (context for Findings 4, 6)
- topic104: Answer Engine Optimization (AEO) Framework (context for Findings 4, 6)

## Suggested Article Angle for topic293
"March 2026 Core Update Nears Completion: Googlebot's 2MB Byte Limit Explained, The Machine-Readable Brand Stack Beyond llms.txt, and the Agentic Web Standards Landscape (MCP, A2A, NLWeb, AGENTS.md)"

## Keywords
March 2026 core update completion, Googlebot 2MB byte limit, Gary Illyes Googlebot crawling architecture, pages getting larger, llms.txt beyond architecture, machine-readable brand content stack, JSON-LD entity graph provenance, MCP Model Context Protocol, A2A agent to agent protocol, NLWeb Mozilla, AGENTS.md standard, ChatGPT Ads launch, WordPress Cloudflare EmDash, agentic AI shopping SEO threat, AI job cuts March 2026 Challenger
