# SEO Knowledge Latest

**Date:** March 29, 2026
**Topic Number:** 215
**Topic:** LLM & AI Search SEO: Structured Data, Markdown Crawlers, Anchor Text & Citation Link Loss — The 2026 AI Search Ecosystem

---

## Finding 1: ChatGPT & Perplexity Treat Structured Data as Plain Text — Not Special Format

**Details:** A February 2026 study by Mark Williams-Cook revealed that ChatGPT and Perplexity do not process JSON-LD structured data as a special semantic format. When he inserted a fake company address exclusively in schema markup (not in visible HTML), both AI engines read and parroted the fake address in responses — confirming they treat structured data as plain text on a page rather than as a special data signal. This challenges the prevailing SEO industry narrative that schema markup provides preferential treatment in AI citation systems. Google's John Mueller has stated "it depends" on whether schema helps LLMs, while Microsoft has explained how schema does help Copilot. The practical takeaway: schema markup is still valuable for traditional SEO and some AI systems, but it should not be treated as a "magical GEO formula." Publishers should ensure key business information appears in visible, plain-text content — not hidden solely in schema markup.

**Source:** Search Engine Roundtable / Mark Williams-Cook / LinkedIn
**Date:** February 6, 2026
**Actionability Score:** 8

---

## Finding 2: Google Still Recommends Visible Anchor Text — Title/Aria Attributes Not Sufficient

**Details:** Google's John Mueller reinforced in February 2026 that visible anchor text remains the recommended approach for providing context to search engines. Responding to a question about whether aria-label has replaced the title attribute for link context, Mueller said: "I'd focus on the visible anchor text, if you want to provide more context for search engines. Make it obvious to everyone what the linked page is for." This is particularly relevant in 2026 as mobile browsers historically did not support the title attribute, and aria-label is primarily an accessibility (a11y) equivalent rather than an SEO signal. SEO practitioners should ensure all hyperlinks contain descriptive, visible anchor text — not rely on title attributes or aria-label as the primary context provider. This is especially important for internal links where anchor text signals topical relationships to both Google and LLM crawlers.

**Source:** Search Engine Roundtable / John Mueller (Bluesky)
**Date:** February 13, 2026
**Actionability Score:** 7

---

## Finding 3: March 2026 Core Update Rolls Out March 27 — First Broad Core Update of 2026

**Details:** Google initiated the rollout of its March 2026 Core Update on March 27, 2026 — the first broad core algorithm update of the year. The update is projected to take approximately two weeks to fully deploy across all regions and languages. Google describes this as a "regular update" designed to enhance surfacing of more relevant and satisfying content. A spam update concluded just two days prior, and a Discover-focused update ran in February 2026, meaning three significant Google updates occurred in close succession. This proximity may cause elevated ranking volatility through mid-April 2026. SEOs are advised to avoid reactive changes during the rollout period; instead, focus on publishing original, experience-driven content, building topical authority, and maintaining clean technical architecture. The update reinforces the importance of comparative value, intent alignment, and content depth.

**Source:** Coalition Technologies / Search Engine Journal / Search Engine Roundtable
**Date:** March 27, 2026
**Actionability Score:** 9

---

## Finding 4: Reddit CEO Pushes Google & OpenAI for Better Citation Links in AI Responses

**Details:** Reddit CEO Steve Huffman spoke on the Reddit Q4 2025 earnings call about his desire for Google and OpenAI to provide better citation links that drive users from AI answer interfaces back into Reddit's conversational content. Huffman described the current citation model — where AI systems paraphrase content and provide a small numbered circle link — as "additive" but not optimal for driving engaged traffic. He noted that "relationships are healthy" with both companies and that "there's a lot of movement there." The broader SEO implication: as AI-generated answers increasingly dominate SERPs, publishers are losing traditional organic clicks. Even when cited, the traffic conversion from AI citations to actual site visits is unclear. Publishers should develop strategies to capture attention within AI answer contexts themselves and consider how to make their content compelling enough to earn direct visits beyond citations.

**Source:** Search Engine Roundtable / Reddit Q4 2025 Earnings Call
**Date:** February 9, 2026
**Actionability Score:** 7

---

## Finding 5: Google Warns Against Serving Raw Markdown to LLM Crawlers — Calls It "Stupid"

**Details:** Google's John Mueller has issued a direct warning against the emerging practice of serving raw Markdown files to LLM crawlers and bots. Responding to a Reddit discussion about the risk/reward of serving Markdown to AI agents, Mueller listed critical concerns: (1) LLMs may not recognize Markdown as anything other than a text file, (2) links within Markdown may not be properly parsed or followed, (3) site navigation, headers, footers, and sidebars would be lost, and (4) serving a text file when crawlers expect an HTML page could confuse systems. Mueller went further on Bluesky: "Converting pages to markdown is such a stupid idea. Did you know LLMs can read images? WHY NOT TURN YOUR WHOLE SITE INTO AN IMAGE?" This directly contradicts Dries Buytaert's reported success (hundreds of requests within an hour from ClaudeBot, GPTBot, and OAI-SearchBot after making pages available as Markdown). The practical advice: if serving Markdown to LLMs, ensure it contains the same structure, navigation, and link equity as HTML pages — but be aware of potential crawl and ranking risks.

**Source:** Search Engine Roundtable / John Mueller (Bluesky/Reddit)
**Date:** February 4, 2026
**Actionability Score:** 8

---

## Finding 6: Google Uses LLMs.txt for Other Purposes — Not LLM Content Discovery

**Details:** Google's Gary Illyes confirmed in January 2026 that Google's primary use of the llms.txt file (a proposed standard for signaling content permissions for LLM crawlers) is not for discovering content to train on, but for other internal purposes. This clarification matters for SEOs and publishers who have been creating llms.txt files hoping to control how their content is used by AI systems. While the llms.txt initiative is useful for some AI companies as a permissions signal, Google has been clear that it is not using llms.txt as a discovery mechanism for its own AI products. Publishers should not rely on llms.txt as a primary AI SEO strategy — rather, it remains a supplementary signal for AI companies that voluntarily respect it.

**Source:** Search Engine Roundtable / Gary Illyes
**Date:** January 6, 2026
**Actionability Score:** 7

---

## Finding 7: Google Confirms Comments Link Spam Has No Effect on SEO

**Details:** Google's search team confirmed in January 2026 that comment link spam — links injected by users in blog comments, forum posts, or other user-generated content — has no measurable effect on a website's search rankings. This aligns with Google's long-standing position that most comment spam is ignored or devalued by their algorithms. However, this does not mean comment links are harmless: they can still be crawled, can contribute to a site's overall link profile noise, and may be interpreted as a signal in very edge cases. Google's John Mueller clarified that while comment links don't help rankings, actively building comment links as a link building strategy is also a waste of time — Google's algorithms are sophisticated enough to discount them. The strategic takeaway: do not invest in comment spam or automated comment posting as an SEO tactic; it provides zero ranking benefit.

**Source:** Search Engine Roundtable / Google
**Date:** January 19, 2026
**Actionability Score:** 6

---

## Finding 8: Google Permits Inter-Site Brand Linking at "Reasonable Scale"

**Details:** Google clarified in January 2026 that linking related brand websites together is perfectly acceptable at reasonable scale. This is significant for businesses that operate multiple websites, brands, or publications under common ownership. Google's position: cross-linking between your own properties is a natural editorial decision and is not considered a manipulative link scheme — provided the links are genuine editorial choices and not artificial link networks. The "reasonable scale" qualifier is important: if a business links hundreds of its own sites together in a reciprocal or unnatural pattern, that could still trigger pattern-based link scheme detection. For SEO practitioners managing multi-property portfolios, this confirmation provides green-light authority to build topical clusters with contextual interlinks — as long as the linking pattern mirrors what a human editor would naturally do.

**Source:** Search Engine Roundtable / Google
**Date:** January 14, 2026
**Actionability Score:** 7

---

## Finding 9: ChatGPT Gains Local Knowledge Panels — AI Citations Expanding to Local SEO

**Details:** OpenAI has expanded ChatGPT's local search capabilities, adding knowledge panel-style information for local businesses directly in ChatGPT responses. This development signals that AI citation surfaces are no longer limited to informational and transactional queries — they now encompass local business information as well. For local SEO practitioners, this is a significant development: businesses previously focused solely on Google Business Profile optimization now need to consider how they appear in AI-generated local knowledge panels. The same principles apply: accurate NAP (Name, Address, Phone) consistency across the web, quality citations in authoritative directories, and review signals. The difference is that in AI-generated responses, these signals are synthesized rather than displayed in a traditional SERP format.

**Source:** Search Engine Roundtable / OpenAI
**Date:** December 22, 2025
**Actionability Score:** 8

---

## Finding 10: OpenAI Scales Up AI Search Bot (OAI-SearchBot) — AI Search Traffic Growing

**Details:** OpenAI significantly expanded its web crawling and search infrastructure in late 2025, with the OAI-SearchBot making substantial crawling visits to websites during the holiday period. Microsoft also explained how structured data specifically helps Copilot (Bing AI) in ways that differ from how Google uses schema. These developments collectively confirm that AI search platforms are rapidly scaling their content discovery and indexing infrastructure. For SEOs, this means traditional Google SEO remains primary, but optimizing for AI search surfaces (Bing AI, ChatGPT, Perplexity) is increasingly important for sites that receive traffic from these platforms. Key actions: ensure your content is accessible to AI crawlers (robots.txt compliance), provide clear structured data, and maintain authoritative, original content that AI systems can confidently cite.

**Source:** Search Engine Roundtable / OpenAI / Microsoft
**Date:** December 9–28, 2025
**Actionability Score:** 8

---

## Finding 11: Schema Markup's Role in AI Systems — "It Depends" (Mueller)

**Details:** John Mueller from Google provided nuanced guidance on whether structured data (schema markup) helps LLMs and AI systems: "It depends." This measured response reflects the reality that different AI systems use structured data in different ways. Microsoft's Copilot has confirmed it uses schema markup to enhance Bing AI responses. ChatGPT and Perplexity appear to treat schema as plain text rather than a special semantic signal (per the Williams-Cook study). Google's own AI Overviews may use schema as one signal among many, but it is not determinative. The practical implication for SEOs: continue using schema markup because it helps traditional search, helps some AI systems, and causes no harm. But do not assume schema alone will earn preferential treatment in AI citation surfaces. The "it depends" answer reinforces that original, well-written content with clear structure remains the most reliable investment.

**Source:** Search Engine Roundtable / John Mueller
**Date:** January–February 2026
**Actionability Score:** 7

---

*Generated by: SEO Learner Agent — Round 164*
*Sources: Search Engine Roundtable, Coalition Technologies, Search Engine Journal, Mark Williams-Cook, Reddit Q4 2025 Earnings Call, OpenAI, Microsoft, Gary Illyes, John Mueller (Bluesky)*
