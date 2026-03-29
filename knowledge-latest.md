# SEO Knowledge Latest

**Date:** March 30, 2026
**Topic Number:** 223
**Topic:** Ecommerce SEO in the AI Commerce Era: Feed Compliance, Loyalty Programs, and the New Product Ranking Surface

---

## Finding 1: Google Merchant Center Requires Grayed-Out Buy Buttons on Out-of-Stock Product Pages

**Details:** Google Merchant Center updated its landing page requirements to mandate that out-of-stock products display a grayed-out (disabled) "Buy" or "Add to Cart" button. Hiding the button entirely or keeping it fully active and clickable are both violations. The requirement states: "For 'out of stock' items, the 'Buy' button must be greyed out on your product landing page." Google will cross-reference the button state against the `availability` attribute in your product data feed. Violations result in product disapprovals and removal from Shopping Ads. For SEOs: this is a technical product page requirement that directly affects Google Shopping eligibility. Audit all product pages to ensure out-of-stock variants display a disabled button, update your product data feed attribute in sync, and add server-side logic to toggle button state based on real-time inventory — not just when a page is re-crawled.

**Source:** Search Engine Roundtable (Barry Schwartz) / Google Merchant Center documentation
**Date:** March 26, 2026
**Actionability Score:** 8

---

## Finding 2: Google Loyalty Program Expands to AI-First Surfaces (AI Mode + Gemini) — 14 Countries

**Details:** Google Ads and Merchant Center expanded Loyalty program features to surface member benefits on Google's AI-first shopping surfaces (AI Mode and Gemini), in addition to standard Shopping ads and local inventory ads. New capabilities include: (1) Highlight key perks — member pricing and member shipping annotations appear directly on product listings; (2) Expanded local/regional visibility — loyalty annotations now work on local inventory ads and regional Shopping ads; (3) International expansion — loyalty features now available in 14 countries including US, UK, Germany, France, Japan, India, Australia, Brazil, Canada, Italy, Mexico, Netherlands, South Korea, and Spain; (4) AI-first surfaces — loyalty benefits are explicitly surfaced to shoppers in AI Mode and Gemini responses. Google states the goal is to "build stronger customer relationships and drive long-term growth by integrating loyalty benefits directly into product listings." For SEOs and advertisers: brands with loyalty programs should ensure their Merchant Center data feed includes loyalty-specific attributes; programs not yet integrated with Merchant Center are invisible to AI Mode shoppers. This creates a new ranking/relevance factor specific to AI shopping surfaces.

**Source:** Search Engine Roundtable (Barry Schwartz) / Google Merchant Center / LinkedIn (Arpan Banerjee)
**Date:** March 27, 2026
**Actionability Score:** 9

---

## Finding 3: Google Performance Max Gets Audience Exclusions, Budget Reporting, and Placement Segmentation

**Details:** Google Ads announced a significant update to Performance Max (PMax) with four new features: (1) First-party audience exclusions — advertisers can now exclude specific first-party audiences (e.g., existing customers, cart abandoners) from seeing ads, preventing cannibalization between PMax and other campaigns; (2) Budget reporting — granular visibility into which audiences and placements are consuming budget within PMax; (3) Full audience reporting — complete breakdown of audience signal performance across PMax inventory; (4) Network segmentation in placement reporting — visibility into which specific websites, apps, and surfaces are showing PMax ads. These changes address the two most persistent complaints about PMax: lack of transparency and lack of control over where and to whom ads serve. For SEOs working with ecommerce clients: PMax now intersects more directly with organic shopping visibility (via Merchant Center integration), and audience exclusions can prevent PMax from bidding on queries already addressed by high-converting organic product pages — reducing wasted spend and protecting organic-to-paid synergy.

**Source:** Search Engine Roundtable (Barry Schwartz) / Google Ads
**Date:** March 27, 2026
**Actionability Score:** 8

---

## Finding 4: Google Shopping Ads Expand to 15 New European Markets — Two-Phase Rollout

**Details:** Google is expanding Shopping Ads eligibility to 15 additional European markets in a two-phase rollout over the coming months. Phase one (sooner): Cyprus, Luxembourg, Moldova, North Macedonia, Malta, Liechtenstein. Phase two (later): Bulgaria, Croatia, Lithuania, Slovenia, Serbia, Bosnia and Herzegovina, Montenegro, Estonia, Latvia. Artur Mosiak (LinkedIn, covered by Hana Kobzová on PPC News Feed) noted this expansion is designed "to help retailers capture peak demand right when it matters most." This is a significant geographic expansion for Shopping Ads into smaller European markets that previously had limited or no access. For SEOs and advertisers: (1) Ecommerce sites targeting these markets should prepare product data feeds with localized pricing, language, and shipping attributes; (2) These markets represent new Shopping Ad competition — local retailers previously not visible on Google Shopping now compete with international brands; (3) Organic product listings in these markets may face less competition in traditional organic results as Shopping Ads expand. The action: audit your product feed coverage for these 15 countries and ensure structured data supports Google's localized shopping surfaces.

**Source:** Search Engine Roundtable (Barry Schwartz) / LinkedIn (Artur Mosiak) / PPC News Feed
**Date:** March 26, 2026
**Actionability Score:** 8

---

## Finding 5: Google Merchant Center Vehicle Ads: Data Quality Disapproval Criteria Now Explicitly Documented

**Details:** Google announced it will highlight data quality account issues related to Vehicle ads within Merchant Center starting mid-April 2026. The documentation now explicitly lists five categories of data mismatch that trigger disapproval: (1) Vehicle availability mismatch — vehicle availability on the landing page must match the data feed; (2) Vehicle condition mismatch — the `condition` attribute must match the landing page; (3) Vehicle price mismatch — price in data feed must match the landing page; (4) Vehicle mileage mismatch — mileage must match; (5) Mismatched vehicle information — VIN, brand, or model must match across data feed and landing page. Google will display the specific issue and fix instructions in the Merchant Center account issues page. For SEOs managing automotive ecommerce: this is a wake-up call for crawl-sync discipline between product data feeds and website content. Any dynamic content on vehicle description pages (price, mileage, availability) must be programmatically synchronized with the data feed — not updated manually or occasionally. Implement automated validation that flags feed/landing page discrepancies before upload.

**Source:** Search Engine Roundtable (Barry Schwartz) / Google Merchant Center
**Date:** March 27, 2026
**Actionability Score:** 8

---

## Finding 6: AI Mode Overlay Cards Reduce Direct Click-Throughs — Google Adds Friction to Branded Mentions

**Details:** Google is testing changing links within AI Mode from direct click-throughs to overlay cards (bubble/bubble link treatment). When a brand is mentioned in an AI Mode response, users previously could click directly to the website. In the new test, clicking a brand mention shows an overlay card first — the user must click again to visit the site. Brodie Clark documented this on X and SERPAlerts: "Instead of clicking through directly to the website when a brand is mentioned, the bubble link treatment now means the user has to click again if they want to visit the website." This follows Google's consistent pattern of adding friction to outbound links in AI surfaces — reducing direct click-through rates from AI-generated responses. For SEOs: branded mentions in AI Mode are becoming less likely to generate direct visits. The strategic implication: AI citation presence alone is insufficient — brands must ensure the pages being cited in AI Mode are optimized for the conversions that matter (purchases, sign-ups, leads), since the path from AI citation to site visit now has additional friction. Monitor your AI Mode referral traffic separately from organic traffic in GA4.

**Source:** Search Engine Roundtable (Barry Schwartz) / Brodie Clark (X/SERPAlerts)
**Date:** March 24, 2026
**Actionability Score:** 8

---

## Finding 7: Google AI Overviews Appear <6% of the Time for Breaking News vs. 60%+ for Health Queries — Topic Varies Dramatically

**Details:** New data from Newzdash (reported via Search Engine Roundtable, March 25, 2026) quantifies the dramatic variance in AI Overview trigger rates across topic categories. While AI Overviews appear more than 60% of the time for health-related queries, they appear in fewer than 6% of breaking news queries. This is significant for content strategy and AI citation planning: the AI Overview suppression for hard news is deliberate — Google appears to suppress AI Overviews for rapidly evolving stories where the model cannot confidently synthesize accurate information in real time. This creates a meaningful SEO asymmetry: for evergreen health, finance, and how-to content, AI Overviews are a dominant visibility surface; for breaking news and time-sensitive journalism, organic search and news features remain the primary traffic drivers. For SEOs: if your content strategy spans both news and evergreen informational content, measure AI citation performance separately by topic vertical — they are operating under fundamentally different algorithmic rules.

**Source:** Search Engine Roundtable (Barry Schwartz) / Newzdash
**Date:** March 25, 2026
**Actionability Score:** 8

---

## Finding 8: Google Business Profile Performance Metrics Now Tracks Offer Views and Clicks

**Details:** Google added documentation to the Google Business Profile "Understand available performance metrics" help page for a new Offer data section. This section shows the number of times customers viewed and clicked on offers on a Business Profile — directly within GBP's performance dashboard. While the feature was not yet live for all businesses at time of documentation, the help page update signals imminent broader rollout. Previously, offer performance in GBP was not separately tracked in the profile's native analytics. For local SEOs: this makes GBP offers a trackable investment — if you're running local promotions, seasonal offers, or member discounts via GBP, you can now measure their direct view and click performance in the same dashboard as calls, direction requests, and website clicks. The action: audit your current GBP offer strategy and prepare to make offers more prominent if they drive measurable engagement — because they can now be measured.

**Source:** Search Engine Roundtable (Barry Schwartz) / Google Business Profile Help / LinkedIn (Hiroko Imai)
**Date:** March 25, 2026
**Actionability Score:** 7

---

## Finding 9: Google Shopping Ads Political Content Policy Update Effective April 16 — 9 Countries Require Election Advertiser Verification

**Details:** Google announced a significant tightening of its Shopping Ads political content policy, effective April 16, 2026. The update implements additional restrictions on political content in Shopping ads and requires election advertiser verification in nine countries: Argentina, Australia, Chile, Israel, Mexico, New Zealand, South Africa, United Kingdom, and United States. India will see outright prohibition of some Shopping Ads featuring political content. Google will require merchants running Shopping ads with political content in the affected countries to complete election ads verification. This policy applies exclusively to Shopping ads (not Search ads). For SEOs and advertisers: any ecommerce or lead-gen site running Shopping Ads that touch political topics, political merchandise, campaign-related products, or issue-advocacy content in the affected countries must complete Google's election advertiser verification process before April 16, 2026. Non-compliant ads will be suspended. This is a compliance deadline with direct business impact.

**Source:** Search Engine Roundtable (Barry Schwartz) / Google Ads Policy
**Date:** March 26, 2026
**Actionability Score:** 8

---

## Finding 10: Google Ads Retires Legacy Ad Format Requirements (March 17) — Responsive Search Ads Remain

**Details:** Google retired multiple legacy Google Ads format requirement policies effective March 17, 2026. Specifically discontinued: Form ad requirements, Image quality requirements, Responsive ad requirements, and Text ad requirements policies. Ginny Marvin (Google) clarified: "This is just a notification that the policies around old ad formats that no longer in use are also being retired. This doesn't affect existing ad formats like Responsive Search Ads, Responsive Display Ads, etc. and has zero impact on any of your existing ads and campaigns." These were policy artifacts from ad formats Google has phased out. For SEOs working with PPC teams: this is an administrative cleanup — not a structural change — but it reduces the compliance documentation burden for legacy ad format audits. Ensure your ad policy documentation is updated to remove references to the retired requirements. The practical impact on active campaigns is zero.

**Source:** Search Engine Roundtable (Barry Schwartz) / Google Ads (Ginny Marvin)
**Date:** March 25, 2026
**Actionability Score:** 7

---

## Finding 11: Google Business Profiles Gains Place Page Attributes — Chat Methods Expand (WhatsApp, LINE, KakaoTalk)

**Details:** Google added a new "Place page attributes" section to Google Business Profiles. The section allows businesses to display additional attributes on their Business Profile across Search, Maps, and other Google services. Notably, the new attributes include a primary chat method selection with expanded options beyond previous versions: Facebook Messenger, KakaoTalk, LINE, WhatsApp, and text messaging. This was first spotted via Japanese user registration options (Shoichi Hasegawa on X). For local SEOs: this is a significant expansion of GBP's engagement surface for businesses with international or younger demographics. WhatsApp, LINE, and KakaoTalk are dominant messaging platforms in specific markets (Europe, Latin America, Japan, South Korea, Southeast Asia). Businesses not previously offering chat via GBP now have expanded options. Adding a visible chat method can increase engagement signals on GBP — which the 2026 Local Search Ranking Factors report confirms are climbing as ranking factors. The action: audit your current GBP chat setup and evaluate whether adding WhatsApp or other messaging options increases engagement for your demographic.

**Source:** Search Engine Roundtable (Barry Schwartz) / LinkedIn (Shoichi Hasegawa)
**Date:** March 23, 2026
**Actionability Score:** 7
