# AI引用基础设施：重塑2026年GEO的技术与政策力量

**主题：** 286 — llms.txt、网站声誉滥用、2026年3月核心更新、代理式AI购物
**日期：** 2026年4月5日
**作者：** 龙雅人

---

## 基础设施层——第257轮遗漏了什么

第257轮探索了AI引用经济的"输出端"：LLM如何引用品牌、感知如何在各平台漂移，以及零点击GEO框架。第258轮转向**基础设施层**——决定内容是否被引用的技术和政策机制。

本轮有三个关键发展：

- **llms.txt** 作为LLM内容供给的正式网络标准出现
- Google **2026年3月核心更新** 及其在AI引用时代对**网站声誉滥用**的持续强化
- **代理式AI购物** 作为新的SEO威胁向量崛起

本轮引入了以往轮次未涉及的新角度。

---

## llms.txt——LLM可读内容的新标准

**来源：** llmstxt.org（官方规范）、Mintlify、Cursor、Anthropic | **日期：** 2026年4月

**llms.txt** 规范是一个放在网站根目录的markdown文件（`/llms.txt`），为LLM提供网站内容的结构化、优先级摘要导航。与robots.txt（告诉爬虫跳过什么）或sitemap.xml（列出页面）不同，llms.txt是**LLM原生**的：它以针对上下文窗口效率优化的格式，向AI系统提供网站内容的精简"电梯演讲"。

规范支持两种文件类型：

- **/llms.txt** — 面向快速LLM吸收的摘要导航
- **/llms-full.txt** — 可选的深度阅读完整内容

### 与robots.txt和sitemap.xml的区别

| 文件 | 用途 | 读取阶段 |
|------|------|---------|
| robots.txt | 告诉爬虫忽略什么 | 爬取阶段 |
| sitemap.xml | 列出所有页面，无语义优先级 | 爬取阶段 |
| llms.txt | 为AI系统打造的精选品牌简报 | 推理阶段 |

### 当前采用情况

包括 **Mintlify**（数千个开发者文档站点）、**Cursor** 和 **Anthropic** 在内的主要文档平台已率先采用。不断增长的社区目录（directory.llmstxt.cloud）追踪LLM友好站点。

### 战略意义

随着LLM越来越依赖llms.txt来理解网站（而非抓取完整HTML），发布高质量llms.txt文件的品牌将在AI引用准确性方面获得**结构性优势**。该文件成为向AI系统提供的"品牌简报"。

**行动：** 为你的主要网络资产创建 /llms.txt 和 /llms-full.txt，并在每次重大内容发布时更新。

---

## 2026年3月核心更新——完整分析

**来源：** Search Engine Roundtable（Barry Schwartz）| **日期：** 2026年3月27日宣布

Google于2026年3月27日（星期五）大约凌晨5:14（ET）正式宣布**2026年3月核心更新**。这是2026年的首次核心算法更新，此前1月和2月经历了激烈的排名波动。

关键背景：Google同期还发布了**2026年3月垃圾邮件更新**（3月24-25日），表明质量和垃圾政策同时执行。

### 谁赢谁输

**赢家：**

- 拥有强大 **E-E-A-T**（经验、专业性、权威性、可信度）的网站
- 发布原创、第一手体验内容的网站
- 对所有内容（包括第三方）拥有明确编辑所有权的网站

**输家：**

- 内容单薄、批量生产的网站
- 第三方内容繁重且缺乏编辑监督的网站
- **INP / Core Web Vitals** 评分较差的网站
- 大规模AI生成内容出现检测迹象的网站

### INP / Core Web Vitals维度

**INP（下次绘制的交互）** 取代FID成为Core Web Vital，到2026年3月，它是Google所有评估框架中**实时活跃测量**的指标。INP测量整个用户生命周期中页面的响应能力——不仅仅是首次交互。

INP > 200ms的页面会受到主动惩罚。对于JavaScript繁重的页面、第三方聊天小部件和结账流程，这是一个关键的优化目标。

### 同时进行的垃圾邮件更新——史上最快

2026年3月垃圾邮件更新在**不到24小时内**完成（3月24日下午3:20 ET启动，3月25日上午10:40 ET结束）。这一速度表明Google已改进其垃圾邮件检测基础设施，可能正在向**实时垃圾邮件过滤**发展，而非批量更新。

---

## 网站声誉滥用政策——算法执行阶段已启动

**来源：** Search Engine Roundtable、Google Search Central | **日期：** 政策自2024年5月生效；2026年3月升级

Google的**网站声誉滥用**政策——针对托管旨在利用宿主网站排名信号的第三方内容的网站——最初仅通过**手动操作**执行（2024年5月Danny Sullivan确认）。到2026年3月，该政策已进入**算法执行阶段**。

该政策具体针对：

- **信誉良好宿主上的第三方内容** —— 带有宿主网站权威性但缺乏编辑监督的新闻稿、附属合作伙伴内容、赞助板块
- **过期域名滥用** —— 重新部署过期域名并填充新第三方内容以继承现有PageRank
- **规模化内容滥用** —— 纯粹为操纵排名而设计的AI生成或批量生产内容

### 双倍惩罚效应

这直接威胁到依赖高权威网站放大第三方内容的内容分发模式。在AI引用时代，这也意味着：

> 如果一个网站让低质量第三方内容占据主导，引用该网站的AI系统会将品牌与低质量信息关联——损害第257轮讨论的品牌引用图谱。

**双倍惩罚：** Google降低排名，AI系统降低引用关联。

### 如何审核你的网站

1. 识别所有第三方发布内容的页面（子域名、/partner/、/sponsored/板块）
2. 验证编辑监督存在并有文档记录
3. 添加清晰的"赞助内容"披露
4. 确保第三方内容不占据页面内容区域的主导地位
5. 审核你内容组合中的过期域名

---

## 代理式AI购物——SEO价值链正在断裂

**来源：** Search Engine Journal（Roger Montti）| **日期：** 2026年4月4日

**代理式AI购物** —— AI代理代表用户自主浏览、比较和购买产品 —— 可能不会立即威胁SEO排名，但根本改变了**流量价值链**。

当AI代理代表用户购买时，点击进入交易页面，而非信息博客文章。SEO价值从"获得点击"转变为"成为代理选择的结账体验"。

这代表了**传统排名与商业结果的结构性脱钩**。Roger Montti（SEJ）指出，SEO从业者今天不必对代理式AI购物感到恐慌，但趋势指向SEO成为**信任信号层**而非**流量获取渠道**。

**影响：**

- 随着AI代理绕过传统漏斗，信息内容排名的商业价值将下降
- 在代理商务时代，GEO和品牌权威可能比关键词排名更重要
- 品牌应为AI代理发现优化产品/服务页面，而非仅为关键词排名

---

## Google AI Mode + Gemini 3——综合质量升级

**来源：** Search Engine Roundtable | **日期：** Gemini 3参考2025年11月，2026年3月活跃

Google的**AI Mode**（Google搜索内的对话式AI搜索界面）现由**Gemini 3**驱动，代表了推理和响应质量的重大升级。

借助Gemini 3，AI Mode综合多源答案的能力有所提高，这意味着：

1. **AI引用将更准确但也更挑剔** —— 只有满足Gemini 3综合质量阈值的内容才会被引用
2. 未能达到阈值的内容即使在传统SERP上排名，也会被**更少引用**

随着Gemini 3驱动的AI Mode成为默认搜索体验，内容优化必须考虑Gemini 3综合引擎认为权威的内容——这是与传统PageRank不同的信号。

---

## 新的AI Overview格式——大规模引用块测试

**来源：** Search Engine Roundtable（Mordy Oberstein）| **日期：** 2026年3月26日

Google正在**测试一种新的AI Overview格式**，该格式在AI Overview底部显示大型引用块。这与之前部署的紧凑型内联引用标记不同。

这一测试表明Google正在探索AI Overview内**更透明的来源归属**，让用户更清楚地了解哪些页面促成了AI生成的答案。

**对GEO的意义：** 如果此格式广泛推出，被大规模引用块引用的页面可能会获得显著的品牌可见度和引荐流量。这是一个值得监控的新GEO KPI。

---

## 2026年AEO框架——SEO + GEO + AEO收敛

**来源：** Azib Yaqoob AEO Framework | **日期：** 2026年3月24日

**答案引擎优化（AEO）** 学科正迅速与GEO和传统SEO收敛为统一的**"AI可见度"**框架。

Azib Yaqoob AEO框架提出了一个专门为"2026年引擎"设计的4步系统：

1. **实体清晰度** —— 作为权威实体可被明确识别
2. **问答结构** —— 将内容格式化为明确的问答对
3. **来源可信度信号** —— 引用、数据和第一手经验
4. **跨平台一致性** —— 确保同一品牌实体在所有AI平台上被认可

---

## SEO/GEO从业者的10个可操作项目

1. **为每个主要网络资产创建 /llms.txt。** 这是先发优势领域——大多数竞争对手尚未行动。

2. **审核网站上所有第三方内容的声誉滥用风险。** 确保编辑监督并添加清晰的"赞助内容"披露。

3. **对所有高流量页面进行INP审核。** INP > 200ms的页面会受到主动惩罚。重点关注JavaScript繁重的页面和结账流程。

4. **将Googlebot允许列表更新到新的 /crawling 端点IP。** Google爬虫基础设施从/search迁移到/crawling端点意味着旧的基于IP的允许列表可能正在阻止合法爬虫。

5. **重新评估SEO与GEO投资分配。** 如果代理式AI购物继续增长，将预算转向品牌权威建设和面向AI代理发现的产品/服务页面优化。

6. **发布原创、第一手体验内容。** E-E-A-T的"经验"元素现在在核心更新中受到主动奖励。

7. **在每个主要主题页面添加问答结构内容。** AEO框架将明确的问答对作为AI引用的最优格式。

8. **监控AI Overview引用块测试。** 追踪Google的大规模引用块测试是否扩展到你的主题类别。

9. **多元化AI平台存在。** 不要仅针对Google AI Overviews进行优化。Perplexity、ChatGPT Search和DeepSeek各有不同的引用偏好。

10. **将SEO服务重新品牌为"AI可见度"或"答案引擎优化"。** AEO框架是真实的，客户已开始点名要求。

---

## 来源表

| # | 来源 | 标题 | 日期 |
|---|---|---|---|
| 1 | llmstxt.org | llms.txt官方规范网站 | 2026年4月 |
| 2 | Search Engine Roundtable（Barry Schwartz） | "Google March 2026 Core Update Is Rolling Out" | 2026年3月27日 |
| 3 | Search Engine Roundtable（Barry Schwartz） | "Google March 2026 Spam Update Unleashed (& Finished)" | 2026年3月24-25日 |
| 4 | Search Engine Journal（Roger Montti） | "Why Agentic AI Shopping Feels Unnatural And May Not Threaten SEO" | 2026年4月4日 |
| 5 | Search Engine Roundtable（Mordy Oberstein） | "Google Tests Huge Block of Citations at Bottom of AI Overviews" | 2026年3月26日 |
| 6 | Search Engine Roundtable | "Google AI Mode Now Powered By The New Gemini 3" | 2025年11月（2026年3月参考） |
| 7 | Google Search Central文档 | INP作为实时Core Web Vital文档 | 2026年3月更新 |
| 8 | 奶爸建站笔记 | "Google爬虫IP迁移：从/search到/crawling" | 2026年3月31日 |
| 9 | Azib Yaqoob（AEO框架） | "The Azib Yaqoob AEO Framework — 4 Steps for Engines of 2026" | 2026年3月24日 |
| 10 | Mintlify博客 | Mintlify为数千个文档站点添加llms.txt支持 | 2024年11月 |
| 11 | Singsys博客 | "Google March 2026 Core Update: What SEOs Need to Know Now" | 2026年4月2日 |
| 12 | Search Engine Journal | "Google March 2024 Core Update: Reducing Unhelpful Content By 40%" | 2024年3月5日 |

---

*文章生成：2026年4月5日 | 第258轮 | 主题286*
*龙雅人 SEO内容作家*
