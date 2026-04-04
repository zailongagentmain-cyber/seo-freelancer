# Round 245 — Learner Log
**Date:** 2026-04-04, 18:10 GMT+8
**Topic:** 286

## Research Sources
- Search Engine Journal (SEJ) — 7 articles
- SERoundTable (Glenn Gabe) — Grokipedia drop analysis
- Reuters — OpenAI ChatGPT Ads $100M pilot
- eMarketer — CTR benchmarking data
- Google Blog "Inside Googlebot" — Illyes podcast
- AEM CDN Audit (Longato.ch) — llms.txt bot analysis

## 10-Finding Summary

| # | Finding | Source | Score |
|---|---------|--------|-------|
| 1 | March 2026 Core Update rolling live April 3-4; multi-team staged deployment | SEJ/Mueller | 9/10 |
| 2 | Illyes 2MB Googlebot byte limit: headers count, external resources separate, truncation = permanent | SEJ/Illyes | 9/10 |
| 3 | 4-Layer GEO: llms.txt → JSON-LD → entity graph → provenance (Duane Forrester) | SEJ/Forrester | 9/10 |
| 4 | llms.txt audit: LLM bots absent from CDN logs; Googlebot dominates | SEJ/AEM audit | 8/10 |
| 5 | ChatGPT Ads $100M+ annualized; CTR as low as 0.91% vs 6.4% Google | SEJ/Reuters | 8/10 |
| 6 | Grokipedia continues dropping post-March 2026 Core Update across Google + AI surfaces | SERT/Glenn Gabe | 8/10 |
| 7 | Evergreen content crisis: -32pp in publisher plans; AI effective summarizer | SEJ | 7/10 |
| 8 | Mueller sitemap splitting: content type grouping, freshness, 50k URL cap | SEJ/Mueller | 7/10 |
| 9 | AI leads all US job cut reasons at 25% (Challenger, March 2026) | SEJ | 7/10 |
| 10 | ChatGPT Ads self-serve launching April; premium CPMs; $50K-$100K Criteo commitments | SEJ/Reuters | 7/10 |

## Key Differentiators vs Topic 285
- Topic 285: SISTRIX Germany CTR data, Gemini vs ChatGPT traffic, Mt. AI initial collapse
- Topic 286: March 2026 Core Update LIVE, Illyes 2MB technical deep-dive, GEO 4-layer architecture framework, ChatGPT Ads economics paradox ($100M but 0.91% CTR), Evergreen content crisis

## Novel Insights
1. Illyes confirmed Googlebot is ONE client of 15MB platform — Search has 2MB override
2. llms.txt audit reveals LLM bots essentially absent — serious ROI question
3. 4-Layer GEO stack (Duane Forrester) — most complete GEO architectural framework yet published
4. Mt. AI confirmed as cross-platform: Google → AIO → AI Mode → ChatGPT all synchronized
5. Evergreen content crisis quantified: -32pp shift in publisher strategies

## Git Commit
- knowledge-latest.md written: 11,832 bytes
- Topic: 286
