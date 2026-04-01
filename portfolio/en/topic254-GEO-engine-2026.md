# Topic 254: The GEO Engine — How Generative AI Selects, Weights, and Rewards Content

**Theme:** As AI search surpasses 2B users and 60% of Google queries end without a click, the game has shifted from ranking on SERPs to being selected, cited, and read by AI systems. This article covers 13 fresh findings on how generative engines pick sources, what writing patterns trigger citations, which entity types AI rewards, and the emerging discipline of GEO (Generative Engine Optimization) — distinct from both traditional SEO and the UI-layer tactics covered in Topics 252–253.

---

## Finding 1: AI Search Has Gone Mainstream — 60% of Queries Now End Without a Click

The numbers marking AI search's dominance have crossed into territory that demands a fundamental strategic rethink. Google's traditional search volume declined by 31% from Q1 2024 to Q1 2026. AI Overviews now reach 2 billion monthly users across more than 200 countries, appearing on approximately 15% to 30% of US Google searches and potentially on nearly half of all Google queries. Most critically, 60% of all Google searches now end without a click — and that figure climbs to 83% when an AI Overview is present. AI search traffic surged by 527% year-over-year, and projections suggest website traffic from AI search will surpass traditional organic search traffic by 2028. These are not leading indicators of a future shift — they describe the present. Publishers who built traffic strategies around Position 1 rankings are now discovering that the new battleground is the AI citation pool, where a page that ranks #8 in traditional results may be the sole cited source for an AI-generated answer. The implication is structural: being in the AI citation pool is not an SEO extra — it is the primary visibility event that matters.

**Source:** Semrush / AI Visibility Index research — "AI Search Trends 2026"

---

## Finding 2: The Semrush AI Visibility Index Reveals Who Wins in AI Search — And How

Semrush launched a dedicated AI Visibility Index in March 2026, positioning itself as the first major SEO platform to offer a systematic benchmark for GEO performance. The index measures brand share of voice across LLM prompts rather than traditional keyword rankings, using a dataset of 213 million+ LLM prompts to track which brands and domains appear most frequently in AI-generated answers. Early findings show a striking top-tier: Samsung leads with 8.2% AI brand share of voice, followed by Apple at 7%, Microsoft at 4.7%, and Amazon at 3.2%. Even more telling, the index shows that consumer brands with strong product schema and named-entity density dominate AI citations in ways that don't map to traditional organic rankings. Semrush has also released an "AI Visibility Essentials" free certification course teaching the mechanics of how AI changes search, signaling that GEO is being institutionalized as a mainstream discipline within the same platform that defined modern SEO.

**Source:** Semrush — "Our AI Visibility Index Reveals Who's Winning in AI Search (and How)"

---

## Finding 3: Declarative Language in Intros Is the Only Universal GEO Signal — Hedging Kills Citations

Kevin Indig's landmark three-part study analyzing 1.2 million ChatGPT responses and 98,000 citation rows has produced the most granular data yet on what AI actually rewards inside content. The finding that cuts across all verticals is this: open with a direct declarative statement — not a question, not context-setting, not preamble. The form is "[X] is [Y]" or "[X] does [Z]." This is the only writing instruction that holds regardless of vertical, content type, or length. Indig found a +14% aggregate lift in AI citation rates for pages that open with declarative language versus those that don't. The data also shows that LLMs actively "penalize" hedging in intros — "This may help teams understand" performs measurably worse than "Teams that do X see Y." GEO requires confident, authoritative assertions in the opening paragraph above any other optimization.

**Source:** Search Engine Journal — "The Science Of What AI Actually Rewards" by Kevin Indig

---

## Finding 4: Entity Types Are Not Equal — DATE and NUMBER Are Universal Positives; PRICE Suppresses Citations

Indig's cross-vertical entity analysis reveals that entity types predicting AI citation are the opposite of what most AEO advice recommends. When analyzing the first 200–250 words of high-cited versus low-cited pages using Google's Natural Language API, DATE entities and NUMBER entities emerged as universal positive signals across all seven verticals studied. PRICE entities suppressed citation in five of six verticals. KG-verified (Knowledge Graph) entities registered as a negative signal, contradicting the widespread advice to "add more brand names and known entities." Content strategists should audit the first 250 words of high-value pages for entity type distribution, prioritizing DATE and NUMBER references over PRICE or brand-name density.

**Source:** Search Engine Journal — "The Science Of What AI Actually Rewards" by Kevin Indig

---

## Finding 5: Heading Structure Is a Binary Signal — Three to Four Headings Outperform None in Zero Verticals

The data shows that heading usage is not a gradient signal — it is binary. Pages either committed to the right number of headings for their vertical or used none at all performed better than pages with three to four headings. In every single vertical studied, three to four headings performed worse than zero headings. This does not mean no headings — it means the optimal heading count is vertical-specific and either needs to be calibrated precisely or stripped entirely. Most content templates used by SEO teams (which typically use H2-H3 structure with 3–5 headings as a default) are actively harmful to GEO performance.

**Source:** Search Engine Journal — "The Science Of What AI Actually Rewards" by Kevin Indig

---

## Finding 6: Corporate Content Dominates AI Citations — Reddit's SEO Win Has Not Translated to GEO

Corporate content — brand-owned articles, official documentation, product pages — dominates AI citation pools in a way that directly contradicts the content marketing industry's recent pivot toward community content. Reddit, which surged as an organic ranking winner after the 2023 Helpful Content Update, has not replicated that dominance in AI citation behavior. AI citation patterns do not mirror what happened to organic search in 2023–2024. The GEO data suggests the opposite: authoritative, brand-owned content with strong entity signals and declarative structure is what AI systems read as credible.

**Source:** Search Engine Journal — "The Science Of What AI Actually Rewards" by Kevin Indig

---

## Finding 7: ChatGPT Launches Precise Location Sharing — "Near Me" Queries Are Now an AI Search Category

OpenAI announced and began rolling out a ChatGPT location sharing feature in late March 2026, enabling users to share their precise device location with ChatGPT for localized results. The feature covers local recommendations, weather, news, and "near me" queries — rolling out to all ChatGPT consumer plans on iOS and web immediately, with Android following. Glenn Gabe dubbed it the "Near Me ChatGPT Update," noting this fundamentally changes how AI chatbots can answer location-dependent queries. With live location sharing, ChatGPT can now serve real-time local results — immediate implications for local SEO and for how businesses with physical locations need to think about their presence in AI chat outputs.

**Source:** Search Engine Roundtable — "ChatGPT Enables Location Sharing For More Localized Near Me Results" (March 31, 2026)

---

## Finding 8: The Google March 2026 Core Update Is Live — And Its GEO Implications Are Already Visible

Google's March 2026 Core Update began rolling out on March 27, 2026, expected to take up to two weeks to fully complete, extending into mid-April 2026. This follows a March 2026 Spam Update completed in just 20 hours — the shortest confirmed spam update in Google's dashboard history. Google's John Mueller explained on Bluesky that core updates involve multiple components pushed individually in stages, consistently taking two to three weeks. For GEO practitioners, core updates change which pages Google's systems pull into AI citation pools. Pages that lose traditional ranking may simultaneously gain AI Overview citations if Google's AI systems re-evaluate their relevance signals.

**Source:** Search Engine Roundtable — "Google On Why Core Updates Take Weeks To Fully Roll Out" (March 31, 2026)

---

## Finding 9: Google Publishes Detailed Googlebot Architecture — 2 MB Limit and Rendering Details Now Fully Explained

Google's Gary Illyes published a comprehensive technical blog post in late March 2026 explaining Googlebot's crawling architecture in byte-level detail. Googlebot fetches up to 2 MB for any URL (excluding PDFs, which get a 64 MB limit). When a page exceeds 2 MB, Googlebot stops at the cutoff and sends truncated content to Google's indexing systems and Web Rendering Service — treating the truncated file as complete. Anything past 2 MB is never fetched, rendered, or indexed. HTTP request headers count toward the 2 MB limit. Every external resource (CSS, JavaScript) gets its own separate byte counter. Critically, meta tags, title tags, canonicals, and structured data should appear early in the HTML to ensure they are processed before the cutoff.

**Source:** Search Engine Journal — "Google Explains Googlebot Byte Limits And Crawling Architecture"

---

## Finding 10: Google's TurboQuant Algorithm Dramatically Improves Vector Search Speed — Changing Retrieval Architecture

Search Engine Land reported in late March 2026 that Google deployed a new algorithm called TurboQuant that dramatically improves the speed of vector search within its indexing infrastructure. Vector search is the backbone of how AI citation systems identify candidate source pages. Faster vector search means Google can evaluate more candidate pages per query, making the AI citation pool wider and more dynamic. For publishers, semantic relevance — how closely a page's conceptual content matches what an AI is looking for — is becoming even more important than keyword matching. Pages semantically rich and conceptually coherent will be evaluated more thoroughly.

**Source:** Search Engine Land — "New Google TurboQuant Algorithm Improves Vector Search Speed" (March 2026)

---

## Finding 11: Education Is a GEO Signal Void — Writing Style Explains Almost Nothing About Citation Likelihood There

Among Indig's vertical-by-vertical analyses, Education stands out as an anomaly: writing style explains almost nothing about citation likelihood in educational content. In education verticals, factors that drive citations in other industries — declarative intro structure, entity density, heading counts — show no meaningful correlation with high citation rates. This likely reflects that AI systems rely more heavily on source authority signals (institutional affiliation, citation counts from external academic sources) than on-page writing patterns. For publishers producing educational content, GEO strategy must focus on demonstrating institutional authority, citing credible external sources, and building domain-level trust signals.

**Source:** Search Engine Journal — "The Science Of What AI Actually Rewards" by Kevin Indig

---

## Finding 12: Semrush Launches ChatGPT Integration — Direct Access to SEO Data Inside AI Conversations

Semrush announced in late March 2026 the launch of an official ChatGPT app giving users direct access to Semrush SEO data inside ChatGPT conversations. Marketers can now use Semrush data — keyword volumes, backlink profiles, traffic estimates — while simultaneously using ChatGPT for content generation, without switching tools. This signals that SEO platforms are actively positioning themselves as infrastructure for the AI search era, not just the Google organic era. The integration suggests a workflow where content briefs are built in Semrush (including GEO-relevant metrics), content is drafted in ChatGPT, and finished content is measured against both traditional SEO KPIs and LLM prompt-level citation rates.

**Source:** Semrush — "Direct Access to Semrush Data in ChatGPT"

---

## Finding 13: Reddit Pro Opens to All Publishers — Community Content Gets AI-Optimized Distribution

Reddit Pro, the platform's official program for helping publishers and brands optimize their Reddit presence, opened to all publishers in March 2026 as a public beta, adding AI-assisted content optimization. While Reddit content has performed well in traditional SEO since 2023, the Reddit Pro expansion specifically targets the AI search distribution layer. Reddit is positioning itself as a preferred content type for AI citation — community discussions and forum-style threads are highly readable by AI systems. Reddit wants its content to be the cited source in AI answers, not just the top-ranking page in organic results. Reddit Pro offers a way to ensure community content is structured and tagged to maximize AI citation probability.

**Source:** Search Engine Land — "Reddit Pro Opens to All Publishers, Adds New Features in Public Beta" (March 2026)
