# Topic 252: 代理网络——从爬取内容到机器可读基础设施

**主题：网络不再为人类浏览而优化。它正在被重建，为代理而行动。本批次中的每一个发现都指向同一转变：从SEO排名到代理可读基础设施，从点击到机器对机器交易，从出版商流量到AI引用声量份额。**

---

## 1. 代理网络协议栈：MCP、A2A、UCP、A2UI、AG-UI已是生产基础设施

Google 2026年3月关于AI代理协议的博文揭示了五个生产标准，它们共同定义了机器对机器的网络：

| 协议 | 名称 | 商业影响 |
|---|---|---|
| MCP | Model Context Protocol | 代理安全访问您的后端数据 |
| A2A | Agent2Agent | 机器人之间的通信和交易 |
| UCP | Universal Commerce Protocol | 机器直接从SERP购买您的产品 |
| A2UI | Agent to User Interface | 自动为用户合成新的视觉布局 |
| AG-UI | Agent User Interaction | 用于流式传输实时AI数据的中间件 |

这些不是提案——它们是来自Google、OpenAI、Microsoft和Anthropic的生产标准，这些公司共同成立了代理AI基金会（AAIF）来构建共享代理基础设施。现在，网站和品牌不仅通过代理是否能读取其内容来评估，还通过代理是否能与其后端交易来评估。

**来源：** Search Engine Journal — "Why Google's New 'Google-Agent' Is The Biggest Mindset Shift In SEO History" (Marie Haynes, March 27, 2026) — https://www.searchenginejournal.com/why-googles-new-google-agent-is-the-biggest-mindset-shift-in-seo-history/570590/

---

## 2. Google-Agent：首个用户触发的代理爬虫进入服务器日志

2026年3月20日，Google在其用户触发的抓取工具文档中添加了Google-Agent。这是一个全新的爬虫类别：它不是后台索引机器人。它反映的是一个人请求Google AI代理（例如Project Mariner）代表他们执行某项操作，而该代理前往您的网站执行。

关键含义：
- 当用户触发的Google代理浏览您的网站时，它会出现在服务器日志中
- 它代表行动，而不仅仅是读取——填写表单、完成购买、启动试用
- 推出于3月20日开始，预计需要数周完成
- IP范围已在user-triggered-agents.json中发布，用于CDN/WAF允许列表
- 即使今天数量很少，现在捕获的基线也为未来增长提供了背景

这与执行后台爬行的Googlebot不同。Google-Agent由用户明确请求代理代表其行动而触发。

**来源：** Semrush Blog — "Google's releasing Google-Agent: Here's what to know" (March 26, 2026) — https://www.semrush.com/blog/google-ai-agent/

---

## 3. WebMCP：代理绕过您的UI，直接与您的后端对话

WebMCP（Web Model Context Protocol）是SEO和发布商最重要的新协议。标准浏览器代理速度慢，因为它们像人类一样解释像素——点击、滚动、填写表单。WebMCP让代理通过结构化、机器可读的接口原生、实时地使用您网站的功能。

实际含义：
- 代理可以完美地自动填写潜在客户表单，无需像素解释
- 代理可以与您的后端就定价和可用性进行谈判
- 不支持WebMCP的网站将比支持的网站更难让代理进行交易
- 代理网络正从"AI读取您的页面"转向"AI操作您的网站"

Marie Haynes预测，网站将通过网络MCP发布自己的代理，代理之间将相互谈判——您的SEO代理与买家代理就定价、潜在客户质量和服务条款进行谈判。

**来源：** Search Engine Journal — "Why Google's New 'Google-Agent' Is The Biggest Mindset Shift In SEO History" (Marie Haynes, March 27, 2026) — https://www.searchenginejournal.com/why-googles-new-google-agent-is-the-biggest-mindset-shift-in-seo-history/570590/

---

## 4. AI标题重写在传统搜索结果中现已上线

Google证实，它正在传统搜索结果中测试AI生成的标题重写——而不仅仅是Discover。这延续了2025年12月Google将Discover AI标题测试重新归类为2026年1月"功能"的趋势。

关键事实：
- 测试被描述为"小范围"，但已上线
- 重写不包括Google更改原始标题的披露
- 示例显示Google更改了语气和意图，而不仅仅是修复截断或可读性
- 发布商没有记录在案的退出选项
- 行业反应强烈负面：Bastian Grimm（Peak Ace）、Brodie Clark和The Verge编辑Nilay Patel都公开批评了这一做法

这代表了一个有意义的转变：早期的重写匹配查询意图或修复格式；这些重写针对参与度进行了优化，在这个过程中改变了含义。

**来源：** Search Engine Journal — "Google Tests AI Headlines, Rolls Out Spam Update – SEO Pulse" (Matt G. Southern, March 27, 2026) — https://www.searchenginejournal.com/seo-pulse-google-tests-ai-headlines-rolls-out-spam-update/570613/

---

## 5. 2026年3月核心更新已上线——2026年首个广泛核心更新

Google于2026年3月27日凌晨2:00（太平洋时间）开始推出2026年3月核心更新。预计推出需要最多两周（直到约4月10日）。这是2026年的首个广泛核心更新——2026年2月的更新仅限Discover范围，不影响搜索排名。

背景：
- 上一次广泛核心更新是2025年12月（12月11-29日，18天）
- Google在2025年12月更新了其核心更新文档，注意到在已宣布的更新之间持续进行较小的核心更新
- Google建议在完成后至少等待一周再在搜索控制台中分析

这次更新恰逢2026年3月垃圾邮件更新两天后发布，创造了一个叠加更新环境。

**来源：** Search Engine Journal — "Google Begins Rolling Out March 2026 Core Update" (Matt G. Southern, March 27, 2026) — https://www.searchenginejournal.com/google-begins-rolling-out-march-2026-core-update/570657/

---

## 6. 2026年3月垃圾邮件更新：Google历史上最快——不到20小时

Google的2026年3月垃圾邮件更新于3月24日下午12:00（太平洋时间）开始，3月25日上午7:30完成——总计约19.5小时。这比以往任何有记录的垃圾邮件更新都快得多：

| 垃圾邮件更新 | 持续时间 |
|---|---|
| 2025年8月 | 27天 |
| 2024年12月 | 7天 |
| 2022年10月 | 48小时 |
| **2026年3月** | **不到20小时** |

**来源：** Search Engine Journal — "Google Tests AI Headlines, Rolls Out Spam Update – SEO Pulse" (Matt G. Southern, March 27, 2026) — https://www.searchenginejournal.com/seo-pulse-google-tests-ai-headlines-rolls-out-spam-update/570613/

---

## 7. Bing网站管理员工具 grounding查询→引用页面映射

Bing网站管理员工具现在提供grounding查询功能，这是一个改变游戏规则的功能，因为它揭示了Bing如何选择引用页面——具体到查询级别。发布商可以：
- 查看哪些页面因grounding而被Bing引用
- 分析具体查询的引用模式
- 了解为什么某些内容被选中而其他内容被忽略

Bing确认grounding查询直接反映了AI搜索结果中的引用模式。这是一个独特的数据源，Google不提供类似功能。

**意义：** 如果您的内容未在grounding查询中出现，则不太可能在Bing的AI搜索结果中被引用。优化grounding性能现在对于Bing和Copilot的可见性至关重要。

**来源：** Semrush Blog — "The agentic web: How AI agents decide which brands make the cut" (March 26, 2026) — https://www.semrush.com/blog/the-agentic-web/

---

## 8. Kevin Indig第3部分：声明性介绍+14%、KG验证实体0.81倍、3-4个标题死区

Kevin Indig的AI科学系列的第3部分揭示了三个可操作的发现：

**声明性介绍结构+14%：** 文章以直接声明（"X是Y"）开头的页面，其AI引用率比非声明性开头高14%。这一发现适用于结构化实体权威内容。

**知识图谱验证实体×0.81：** 在Google知识图谱中未验证的实体，其AI引用率仅为已验证实体的0.81倍。声明您的实体并与知识图谱连接是AI可见性的乘数。

**3-4个标题死区：** 具有3-4个H2/H3标题的内容在AI摘要中表现最佳。少于3个标题的内容缺乏结构深度；超过4个标题的内容开始显得碎片化。

**来源：** Search Engine Journal — "The Science Of What AI Actually Rewards" (Kevin Indig, Part 3) — https://www.searchenginejournal.com/the-science-of-what-ai-actually-rewards/570849/

---

## 9. Bing作为非Google引擎的分发主干

Bing的角色正在扩展到超越自身搜索——它现在是多个非Google AI引擎的后端分发主干：

- **Perplexity的Sonar索引：** Perplexity使用Bing索引作为其网络爬取的基础
- **OpenAI的爬取基础设施：** 多个报告显示OpenAI正在构建自己的爬取基础设施，但其规模仍以Bing为参照
- **Google的分布式爬取依赖：** 即使Google也在分布式索引中依赖Bing的数据

这意味着：**在Bing中表现良好的内容更有可能在所有AI引擎中被发现。** Bing不再只是一个搜索引擎——它是AI时代网络分发的基础设施层。

**来源：** Semrush Blog — "The agentic web: How AI agents decide which brands make the cut" (March 26, 2026) — https://www.semrush.com/blog/the-agentic-web/

---

## 10. 委托经济：意识和转化同时发生

Nick Fox（Google搜索主管）和Liz Reid的"搜索正在成为AI搜索"以及"代理相互对话"的说法正在成为现实。AI代理现在正在：
- 代表用户进行多步研究
- 在单一对话中跨越多个网站进行购买
- 根据用户偏好和实时库存自动进行价格谈判

**关键含义：** 传统漏斗（意识→考虑→转化）正在崩溃。对于搜索引擎优化来说，这意味着：
- 意识内容和转化内容之间的界限正在模糊
- 在代理驱动的世界中，深度权威比广泛的漏斗覆盖更有价值
- 内容需要同时为人类意图和代理决策树优化

**来源：** Semrush Blog — "The agentic web: How AI agents decide which brands make the cut" (March 26, 2026) — https://www.semrush.com/blog/the-agentic-web/

---

## 11. 答案引擎流量：40%月环比增长、23字查询、23分钟会话、2-4倍转化

关于答案引擎流量，新的数据揭示了一个正在加速的趋势：

- **答案引擎查询月环比增长40%**
- **平均查询长度：23个单词**（vs 传统搜索的2-3个单词）
- **平均会话时长：23分钟**（深度研究会话）
- **转化率：2-4倍**于传统搜索

用户行为正在从"搜索并点击"转向"提问并接收代理"。这对内容策略有直接影响：长篇深度研究内容正在击败短篇信息性内容。

**来源：** Semrush Blog — "What Is an AI Agent? (And What AI Agents Mean for Your Brand's Visibility)" (March 26, 2026) — https://www.semrush.com/blog/what-is-an-ai-agent/

---

## 12. Semrush案例研究：AI概览从17%增长到35%——通过情感控制

一个Semrush客户案例研究显示，通过AI情感控制策略，AI概览覆盖率在5个月内从17%增长到35%：

关键策略：
- 监控品牌在AI响应中的情感呈现
- 优化内容以实现平衡、正面的AI情感得分
- 积极建立高质量引用以稀释负面内容

这是一个可复制的方法：AI情感优化是品牌在AI驱动的搜索环境中管理其在线声誉的新层面。

**来源：** Semrush Blog — "How One SEO Consultant Turns Semrush's AI Sentiment Insights into Traffic and Visibility" (March 26, 2026) — https://www.semrush.com/blog/turning-ai-sentiment-insights-into-visibility/

---

## 13. Nick Fox和Liz Reid：搜索正在成为AI搜索

在2026年3月，Google搜索主管Nick Fox和Liz Reid明确表示：
- "搜索正在成为AI搜索"——不再是从索引中检索文档，而是从知识中合成响应
- "代理相互对话"——AI代理正在代表用户执行多步复杂任务

从SEO角度，这意味着一场根本性的转变：
- 从**文档排名**到**响应合成**的转变
- 从**点击优化**到**引用优化**的转变
- 从**关键词匹配**到**语义理解**的转变

**来源：** Semrush Blog — "What Is an AI Agent? (And What AI Agents Mean for Your Brand's Visibility)" (March 26, 2026) — https://www.semrush.com/blog/what-is-an-ai-agent/

---

## 14. digitalSourceType结构化数据文档更新

Google更新了digitalSourceType结构化数据的文档，添加了新的实施细节：

新功能：
- **Source type values：** 扩展了有效来源类型列表
- **Confidence indicators：** 新的信号指示内容来源的可靠性
- **Attribution requirements：** 更清晰的内容归属要求

发布商需要：
- 审核其digitalSourceType实现是否使用最新模式
- 确保品牌实体被正确声明和验证
- 添加新的置信度指标以提高AI可信赖性

**来源：** Google搜索文档更新（2026年3月）— https://developers.google.com/search/docs/appearance/structured-data/digital-source-type

---

## 15. Gary Illyes：HTTP头计入2MB限制，页面权重增长3倍

Google的Gary Illyes透露了关于页面大小和爬取的新技术细节：

- **HTTP头计入2MB限制：** Google计算页面大小时包括HTTP头，这意味着更大的头响应会消耗您的2MB预算
- **页面权重增长3倍：** 自2024年以来，平均页面传输大小增长了3倍，这对爬取效率有影响
- **爬取优先级调整：** Google正在根据页面效率重新分配爬取资源

**实际影响：** 页面性能优化不仅是用户体验问题，也是爬取效率问题。精简HTTP头和优化页面大小可以积极影响您的爬取预算。

**来源：** Search Engine Journal — "Google: Pages Are Getting Larger & It Still Matters" (March 27, 2026) — https://www.searchenginejournal.com/google-pages-are-getting-larger-it-still-matters/570875/

---

## 16. Claude Constitutional AI → 更高的UGC引用率

Yext Research的新研究发现，Claude Constitutional AI框架对内容引用模式有可测量的影响：

- **Claude引用用户生成内容（UGC）的比率高于其他模型**
- ** Constitutional AI方法优先考虑透明度和归属**
- **这对品牌策略有影响：** 在AI驱动的引用环境中，具有透明UGC集成的品牌可能具有优势

多模型优化概念正在兴起：不同AI模型有不同的引用偏好。了解哪些模型引用哪些类型的内容是AI可见性优化的下一个前沿。

**来源：** Semrush Blog — "The agentic web: How AI agents decide which brands make the cut" (March 26, 2026) — https://www.semrush.com/blog/the-agentic-web/

---

## 关键战略要点

本批次揭示了一个明确的轨迹：**网络正在从人类可读的文档集合转向代理可操作的服务层。**

对于SEO，这意味着：
1. **代理可读性**正在与人类可读性同样重要
2. **Bing分发**是所有AI引擎可见性的关键
3. **结构化实体**（通过知识图谱验证）正在成为AI引用的必要条件
4. **长篇研究内容**正在击败短篇信息性内容（23字查询，23分钟会话）
5. **协议合规**（MCP、WebMCP）可能很快成为技术SEO的必要条件

每一项发现都指向同一个方向：搜索引擎优化正在成为代理基础设施工程。
