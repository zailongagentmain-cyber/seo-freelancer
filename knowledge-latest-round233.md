# SEO Knowledge File — Topic 271
**Period: April 3–4, 2026 | Generated: April 4, 2026**

---

## Top 12 Findings

| # | Finding | Source | Date | Score |
|---|---|---|---|---|
| 1 | Local Pack call buttons now appear in only ~20% of searches — 4 out of 5 map pack results have zero call-to-action | Smallbiz Edge / Joy Hawkins via SE Roundtable | Mar 16, 2026 | 🔥 9.6 |
| 2 | Google Merchant Center mandates grayed-out "Buy" button for all out-of-stock product pages — hiding or keeping it active now explicitly violates policy | Google / FeedArmy via SE Roundtable | Apr 3, 2026 | 🔥 9.5 |
| 3 | Google removes "What People Suggest" health SERP feature — lasted less than a year; had surfaced Reddit/social discussions via AI for health queries | The Guardian / SE Roundtable | Mar 16–19, 2026 | 🔥 9.2 |
| 4 | Google Business Profiles gains Place Page Attributes — businesses can now publish chat options (WhatsApp, LINE, Facebook Messenger, SMS) directly on GBP listings | SE Roundtable | Mar 20, 2026 | 🔥 8.8 |
| 5 | Bing tests AI-curated shopping recommendations — "expert recommendation options" sourced from multiple web sources; reminiscent of AI-generated product curation | SE Roundtable (Sachin Patel) | Mar 13, 2026 | 🔥 8.5 |
| 6 | Live sports scores now surface inside Google AI Mode as entity cards — real-time data displayed for active games; represents AI Mode's evolution into transactional information | SE Roundtable | Mar 20, 2026 | 🔥 8.3 |
| 7 | ChatGPT ads expanding to all US free users "in coming weeks" — but early advertisers report zero measurable business outcomes and no programmatic ad buying | The Information / SE Roundtable | Mar 22–24, 2026 | 🔥 8.0 |
| 8 | Evergreen content value declining at -32 percentage points per Reuters Institute survey — publishers explicitly reducing investment; AI summarization is the structural cause | Reuters Institute / SEJ | Apr 1, 2026 | 🔥 8.0 |
| 9 | Google March 2026 Core Update volatility continues into April — ranking fluctuations ongoing through first week of April; not diagnosed until April 9+ recommended | Barry Schwartz / SE Roundtable | Apr 2–3, 2026 | 🔥 7.8 |
| 10 | Google's "broad simplification" of SERP features is removing secondary social/forum signals — Reddit and social citations declining on SERPs as Google consolidates AI Overviews | SE Roundtable / The Guardian | Mar 16–19, 2026 | 🔥 7.5 |
| 11 | Ahrefs case study: evergreen content ROI collapse forces commercial recalculation — quality content now costs more to produce AND earns less search value; publishers must demand more from every asset | SEJ (Harry Clarkson-Bennett) | Apr 1, 2026 | 🔥 7.5 |
| 12 | Google Shopping's Store Tab expands to show local inventory — Google Shopping now surfaces physical store stock; blur between organic commerce and paid/local discovery accelerating | SE Roundtable | Mar 25, 2026 | 🔥 7.2 |

---

## Deep Dive A: Local Pack De-Clickification — The Call Button Collapse and What It Signals

The data is now unambiguous: Google has been systematically removing call-to-action infrastructure from Local Pack results. A study by Smallbiz Edge examining 2,580 searches across 172 keywords in 15 locations found that call buttons appeared in Local Packs only 20% of the time — meaning 4 out of 5 map pack results lack any tap-to-call capability. Joy Hawkins summarized the finding with characteristic directness: "4 out of 5 searches in the map pack have no call button."

This is not a bug. It is a feature of Google's broader zero-click strategy.

The trajectory matters more than the snapshot. Google has been progressively removing call buttons from local packs for over a year. The study confirms that this is not a temporary test or localized change — it represents an established pattern of behavior. The study's limitation (172 keywords, potential bias toward non-callable queries) means the true average may be slightly higher, but the direction is not in doubt.

The business implications are severe for local SEO operators. The Local Pack has historically been one of the highest-intent SERP features — a user who taps "Call" is typically ready to convert. When that button disappears, Google captures the real estate and the user intent, while the business loses the direct connection. The user still sees the business name, address, and phone number (if Google displays it), but the path to conversion narrows.

This is the structural consequence of zero-click optimization made concrete. Google has determined that reducing call friction within the SERP improves user experience metrics — or more precisely, that keeping users within Google's ecosystem (Maps, Business Profiles) for longer than driving an immediate phone call improves metrics that matter more to Google's business.

The SEO response options are now limited: Google Business Profile chat attributes (WhatsApp, SMS, Facebook Messenger, LINE) represent Google's alternative CTA infrastructure, and those are now available for businesses to configure. But this shifts the conversion path from one-click to multi-step, and the conversion rate impact will be material for high-volume local businesses.

The secondary implication: businesses that previously relied on map pack visibility for phone call volume need to rethink their local SEO KPIs. Foot traffic, directions requests, and GBP profile views become the measurable proxy for "local SERP presence" — not call initiates. Local SEO audits should now include a GBP CTA configuration audit as a standard component.

---

## Deep Dive B: Google Merchant Center's Out-of-Stock Mandate — Product Feed Quality Enters the Compliance Era

Google Merchant Center updated its landing page requirements on April 3, 2026 with a deceptively simple rule: out-of-stock products must display a grayed-out (disabled) Buy button on their landing pages. Hiding the button is not allowed. Leaving it fully clickable is not allowed. The button must be disabled.

This is a compliance mandate, not a guideline.

For SEO professionals and e-commerce operators, this represents a significant change in product feed management workflows. Historically, out-of-stock handling was a merchant's discretion problem — some hid the button, some showed it grayed, some left it active and dealt with backorder customer service. Google's new requirement forces a specific UX pattern with zero wiggle room.

The immediate practical impact: sites with large product catalogs and frequent stockouts need to ensure their technical implementation can render a disabled-but-visible Buy button for out-of-stock items. This sounds trivial but is not — many Shopify, WooCommerce, and custom e-commerce implementations hide out-of-stock buttons by default (display:none) or leave them active. Both approaches now violate Merchant Center policy.

The broader signal is more important than the individual compliance task. Google's Merchant Center is evolving from a product listing platform into a regulated commerce layer. The company is building infrastructure to ensure that when a user taps "Buy" from a Shopping ad or Shopping Graph listing, the transaction is likely to succeed. Broken purchase paths — dead buttons, sold-out products with active carts — are being treated as a quality problem that Google wants to solve on behalf of users.

This aligns with Google's stated direction on AI Overviews: when AI synthesizes answers that include product recommendations, those recommendations must lead to working purchase flows. A product that appears in an AI Overview but links to a dead page or an out-of-stock button is a trust failure for Google, not just a merchant problem.

For SEO and content professionals, the implication is a tightening relationship between on-page content quality (product page completeness, stock accuracy, CTA state) and merchant-visible performance. Merchant Center violations now flow into Shopping and AI Overviews visibility. The walls between "technical SEO" and "product feed management" are collapsing.

The action item is concrete: audit product page templates now to confirm disabled buttons render correctly for out-of-stock SKUs, and implement automated checks that flag any product page where the out-of-stock state fails to meet the grayed-button requirement.

---

## 10 Condensed Findings

1. **Local Pack call buttons: 4 out of 5 have none** — Only 20% of Local Pack results show call buttons per 2,580-search study. Google's zero-click strategy has a direct local commerce casualty. Reassess local SEO KPIs; GBP chat attributes are the replacement CTA infrastructure. (Source: Smallbiz Edge/SE Roundtable, Mar 16, 2026)

2. **GMC mandates disabled Buy button for out-of-stock** — Compliance requirement as of April 3: hiding or keeping the button active is now a policy violation. Affects all Shopping advertisers and organic Shopping listings. Check product page templates immediately. (Source: Google/SE Roundtable, Apr 3, 2026)

3. **"What People Suggest" health feature officially dead** — Google's social-sourced health SERP feature lasted under a year; removed as part of "broad simplification." Reddit and social citation signals on health SERPs now declining. (Source: The Guardian/SE Roundtable, Mar 16–19, 2026)

4. **GBP Place Page Attributes: chat on the Business Profile** — Businesses can now configure WhatsApp, LINE, Facebook Messenger, SMS as primary contact options directly on GBP listings across Search, Maps, and other Google services. (Source: SE Roundtable, Mar 20, 2026)

5. **Bing AI-curated shopping: "expert recommendation options"** — Bing is testing AI-sourced product recommendations in Shopping tab, pulling from multiple web sources to curate best product variations. May signal Bing competing with Google's Shopping Graph. (Source: SE Roundtable/Sachin Patel, Mar 13, 2026)

6. **Live sports scores surface in Google AI Mode** — AI Mode now displays real-time sports entity cards during active games. Represents AI Mode's expansion from informational queries into transactional/scheduled real-time information. (Source: SE Roundtable, Mar 20, 2026)

7. **ChatGPT ads expand to all US free users — zero measurement** — Early advertisers cannot prove any measurable business outcomes; no programmatic ad buying exists; OpenAI pushing rapid scale. ChatGPT becoming an ad platform before it has analytics. (Source: The Information/SE Roundtable, Mar 22–24, 2026)

8. **Evergreen content investment dropping -32 points** — Reuters Institute data shows publishers explicitly cutting evergreen content investment as AI summarization erodes value. Not a prediction — current behavior. Content commerciality must now justify itself. (Source: Reuters Institute/SEJ, Apr 1, 2026)

9. **March 2026 Core Update volatility continues into April** — Ranking fluctuations ongoing through April 3–7; Google recommends not diagnosing until April 9+. Multiple systems mean waves of changes, not single deployment events. (Source: Barry Schwartz/SE Roundtable, Apr 2–3, 2026)

10. **Google Shopping Store Tab shows local inventory** — Google Shopping now surfaces which products are available at physical stores near the user. Blur between organic commerce discovery and paid/local is accelerating; local retailers need Shopping presence. (Source: SE Roundtable, Mar 25, 2026)

---

## Action Tiers

### Immediate (This Week)
- Audit top 20 product pages for out-of-stock state: confirm disabled Buy button renders correctly; flag any template that hides or keeps button active
- Check Google Business Profile for Place Page Attributes: configure at least one chat option (WhatsApp or SMS recommended) if none is set
- Do not diagnose March 2026 Core Update ranking changes until April 9+ — volatility is ongoing and diagnosis before completion produces false negatives

### 30-Day
- Local SEO: audit Local Pack visibility across brand and category terms; if call button absence is reducing measurable conversions, shift KPI tracking to directions requests + GBP profile views + chat initiates
- Product feed: implement automated checks for out-of-stock button state compliance; add to Merchant Center quality monitoring stack
- Content audit: evaluate evergreen content ROI against the Reuters Institute -32 point benchmark; identify which assets have declined most in referral traffic and decide on refresh/delete/consolidate

### 90-Day
- Build commerce-SEO integration: align product page UX standards with Merchant Center compliance requirements; treat feed errors as SEO issues
- Local commerce strategy: develop alternative conversion paths for high-intent local queries — GBP chat, direction requests,店内取货 options
- Evaluate Bing Shopping AI expansion: if Bing's AI-curated Shopping test goes live, Bing Webmaster Tools data becomes essential for e-commerce SEO visibility

---

*Topic 271 | Period: April 3–4, 2026 | Author: 龙雅人 SEO*
