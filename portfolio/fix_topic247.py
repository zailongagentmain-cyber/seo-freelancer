#!/usr/bin/env python3
"""Fix topic247 EN + CN articles with SEO optimizations"""

import re

# =====================
# EN Article Fixes
# =====================
en_path = '/Users/clawbot/projects/ai-money-projects/seo-freelancer/portfolio/en/topic247-agentic-seo-ai-first-web-architecture-2026.html'

with open(en_path, 'r', encoding='utf-8') as f:
    en_html = f.read()

# 1. Replace {{keywords}} with actual keywords
en_keywords = "Agentic SEO, MCP Protocol, AI First Web Architecture, AI Agent Optimization, Machine to Machine Discovery, Anthropic Model Context Protocol, OpenAI Operator, Computer Use, AI Agent Visibility, Schema.org Markup, Agentic Commerce, AI Agent UX Patterns"
en_html = en_html.replace('"keywords": "{{keywords}}"', f'"keywords": "{en_keywords}"')

# 2. Add FAQPage schema after Article JSON-LD
faqpage_schema_en = '''    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "What is Agentic SEO?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Agentic SEO is the practice of optimizing websites not for human searchers, but for AI agents that research, compare, and execute transactions autonomously. It focuses on AI-Agent Visibility, MCP protocol compatibility, and machine-readable content."
                }
            },
            {
                "@type": "Question",
                "name": "What is the MCP protocol?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "MCP (Model Context Protocol) is an open standard developed by Anthropic that enables AI models to connect to external data sources and services. In SEO terms, it functions as a new discovery mechanism — AI agents can discover and interact with your content via MCP servers, bypassing traditional HTML crawling."
                }
            },
            {
                "@type": "Question",
                "name": "How do AI agents discover content differently from traditional crawlers?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Traditional discovery relies on keyword matching via crawlers. AI agents use capability matching, structured data queries, semantic reasoning, and multi-source comparison. Sites optimized for agentic discovery use comprehensive Schema.org markup, MCP tools, and structured content accessible to machines."
                }
            },
            {
                "@type": "Question",
                "name": "What is AI-Agent Visibility?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "AI-Agent Visibility is the new KPI for agentic SEO — measuring whether your site appears in the consideration set when an AI agent researches options on behalf of a user. A page ranking #3 in Google might never be considered by an AI agent if it lacks structured data and agent-compatible UX."
                }
            },
            {
                "@type": "Question",
                "name": "What Schema.org types are most important for Agentic SEO?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Key schemas include Article schema for content, FAQPage for Q&A, Offer/Product/Service for commerce, HowTo for guides, Review for ratings, and Event for listings. Complete schema property filling is essential — incomplete schema means incomplete agent understanding."
                }
            }
        ]
    }
    </script>'''

# Find the closing of Article JSON-LD script and insert FAQPage after it
en_html = en_html.replace(
    '        }\n    }\n    </script>\n    <style>',
    '        }\n    }\n    </script>\n' + faqpage_schema_en + '\n    <style>'
)

# 3. Fix CN related links to -cn versions in the related section
en_cn_replacements = [
    ('topic82-ai-seo-tools-revolution-2026.html', 'topic82-ai-seo-tools-revolution-2026-cn.html'),
    ('topic81-video-seo-reddit-ai-2026.html', 'topic81-video-seo-reddit-ai-2026-cn.html'),
    ('topic79-ai-citation-optimization-2026.html', 'topic79-ai-citation-optimization-2026-cn.html'),
    ('topic48-answer-engine-optimization-2026.html', 'topic48-answer-engine-optimization-2026-cn.html'),
    ('topic32-ai-overview-optimization-2026.html', 'topic32-ai-overview-optimization-2026-cn.html'),
    ('topic31-zero-click-seo-2026.html', 'topic31-zero-click-seo-2026-cn.html'),
]

# Also update the Chinese titles for related links
en_cn_titles = [
    ('>🤖 AI SEO Tools Revolution 2026: Reshaping Search Optimization</a>', '>🤖 AI SEO Tools Revolution 2026: Reshaping Search Optimization (中文)</a>'),
    ('>🎬 Video SEO & Reddit in AI Era: The New Traffic Code</a>', '>🎬 Video SEO & Reddit in AI Era: The New Traffic Code (中文)</a>'),
    ('>🎯 AI Citation Optimization: How to Get Your Content Cited by AI</a>', '>🎯 AI Citation Optimization: How to Get Your Content Cited by AI (中文)</a>'),
    ('>Answer Engine Optimization: The Complete Guide for 2026</a>', '>Answer Engine Optimization: The Complete Guide for 2026 (中文)</a>'),
    ('>AI Overview Optimization: The Complete Guide for 2026</a>', '>AI Overview Optimization: The Complete Guide for 2026 (中文)</a>'),
    ('>Zero-Click SEO: How to Thrive When No One Clicks</a>', '>Zero-Click SEO: How to Thrive When No One Clicks (中文)</a>'),
]

# Actually the related links in the en article should stay as en links
# Only the CN article needs the -cn links

# 4. Add cross-link to topic246 in intro paragraph
cross_link_en = '<a href="topic246-agentic-seo-ai-first-web-architecture.html">topic246</a>'
en_html = en_html.replace(
    '<p>\nThe rules of SEO are being rewritten',
    f'<p>\nFor a comprehensive overview of the Agentic SEO landscape, see our <strong>related article</strong>: <a href="topic246-agentic-seo-ai-first-web-architecture.html">Agentic SEO & AI-First Web Architecture (EN)</a>. This guide builds on those foundations with 10 new findings.\n</p>\n\n<p>\nThe rules of SEO are being rewritten'
)

with open(en_path, 'w', encoding='utf-8') as f:
    f.write(en_html)

print("EN article fixed")

# =====================
# CN Article Fixes
# =====================
cn_path = '/Users/clawbot/projects/ai-money-projects/seo-freelancer/portfolio/cn/topic247-agentic-seo-ai-first-web-architecture-2026-cn.html'

with open(cn_path, 'r', encoding='utf-8') as f:
    cn_html = f.read()

# 1. Replace {{keywords}} with Chinese keywords
cn_keywords = "Agentic SEO, MCP协议, AI优先网站架构, AI代理优化, 机器对机器发现, Anthropic模型上下文协议, OpenAI Operator, 计算机使用, AI代理可见性, Schema.org标记, 代理商务, AI代理用户体验"
cn_html = cn_html.replace('"keywords": "{{keywords}}"', f'"keywords": "{cn_keywords}"')

# 2. Add FAQPage schema in Chinese
faqpage_schema_cn = '''    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "什么是Agentic SEO？",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Agentic SEO是针对AI代理而非人类搜索者进行网站优化的实践，这些AI代理能够自主地研究、比较和执行交易。它侧重于AI代理可见性、MCP协议兼容性和机器可读内容。"
                }
            },
            {
                "@type": "Question",
                "name": "什么是MCP协议？",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "MCP（模型上下文协议）是Anthropic开发的开放标准，使AI模型能够以标准化方式连接外部数据源和服务。在SEO方面，它作为一种新的发现机制——AI代理可以通过MCP服务器发现并与您的内容交互，绕过传统HTML抓取。"
                }
            },
            {
                "@type": "Question",
                "name": "AI代理如何与传统抓取工具有不同的内容发现方式？",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "传统发现依赖爬虫的关键词匹配。AI代理使用能力匹配、结构化数据查询、语义推理和多源比较。针对代理发现优化的网站使用全面的Schema.org标记、MCP工具和机器可访问的结构化内容。"
                }
            },
            {
                "@type": "Question",
                "name": "什么是AI代理可见性？",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "AI代理可见性是代理SEO的新KPI——衡量您的网站在AI代理为用户研究选项时是否出现在考虑集中。在Google排名第3的页面，如果缺乏结构化数据和代理兼容的用户体验，可能永远不会进入AI代理的考虑范围。"
                }
            },
            {
                "@type": "Question",
                "name": "Agentic SEO最重要的Schema.org类型是什么？",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "关键schema包括：用于内容的Article schema、用于问答的FAQPage、用于商业的Offer/Product/Service、用于指南的HowTo、用于评级的Review和用于列表的Event。完整的schema属性填写至关重要——不完整的schema意味着代理理解不完整。"
                }
            }
        ]
    }
    </script>'''

cn_html = cn_html.replace(
    '        }\n    }\n    </script>\n    <style>',
    '        }\n    }\n    </script>\n' + faqpage_schema_cn + '\n    <style>'
)

# 3. Fix CN related links to -cn versions
cn_related_fixes = [
    ('topic82-ai-seo-tools-revolution-2026.html', 'topic82-ai-seo-tools-revolution-2026-cn.html'),
    ('topic81-video-seo-reddit-ai-2026.html', 'topic81-video-seo-reddit-ai-2026-cn.html'),
    ('topic79-ai-citation-optimization-2026.html', 'topic79-ai-citation-optimization-2026-cn.html'),
    ('topic48-answer-engine-optimization-2026.html', 'topic48-answer-engine-optimization-2026-cn.html'),
    ('topic32-ai-overview-optimization-2026.html', 'topic32-ai-overview-optimization-2026-cn.html'),
    ('topic31-zero-click-seo-2026.html', 'topic31-zero-click-seo-2026-cn.html'),
]

for old, new in cn_related_fixes:
    cn_html = cn_html.replace(f'href="{old}"', f'href="{new}"')

# 4. Add cross-link to topic246-cn in intro paragraph
cn_html = cn_html.replace(
    '<p>\nSEO的规则正在被重写',
    '<p>\n关于Agentic SEO的完整概述，请参阅我们的<strong>相关文章</strong>：<a href="topic246-agentic-seo-ai-first-web-architecture-cn.html">Agentic SEO与AI-First Web架构：AI Agent优化</a>。本指南在此基础上提供10个新发现。\n</p>\n\n<p>\nSEO的规则正在被重写'
)

with open(cn_path, 'w', encoding='utf-8') as f:
    f.write(cn_html)

print("CN article fixed")
print("All fixes applied successfully")
