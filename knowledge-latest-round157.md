# knowledge-latest-round157.md — Round 157

**Date:** 2026-03-29
**Topic:** Search Chaos Week — Core Update D-Day, AI SERP Anatomy, and the Agentic Web Goes Live
**Round:** 157
**Sources:** SERoundTable (Barry Schwartz), Search Engine Land, Glenn Gabe, Brodie Clark, Aleyda Solis, Sachin Patel, Len, The Information, Microsoft Ads Blog, Google Blog, Twitter/X community

---

## 核心发现

### 1. GOOGLE MARCH 2026 CORE UPDATE 正式上线——预计两周完成，首个年度核心更新

**最新状态（2026年3月27日 05:14 AM ET）：**

- 通过 Google Search Status Dashboard 正式发布（incident ID: 7eTbAa2jWdToLkraZj5y）
- 这是 2026 年首个 broad core update
- Spam Update（3月24-25日，19.5小时完成）完成后仅两天即启动
- **Google 原话：** "a regular update designed to better surface relevant, satisfying content for searchers from all types of sites"
- 官方预计完成时间：约两周（部分行业人士认为可能更长）
- Google **未发布配套博客文章**，未宣布具体目标
- 影响范围：全球、所有语言、所有内容类型
- **非惩罚性**——是对优质页面的提升，而非对低质页面的打击

**历史数据参考：**
- December 2025 Core Update: 12月11日 → 12月29日（18天）
- June 2025 Core Update: 6月30日 → 7月17日（17天）
- March 2025 Core Update: 3月13日 → 3月27日（14天）

**战略含义：** 这是观察 Google 2026 年内容质量判断方向的关键窗口。考虑到 Round 155 揭示的 AI Overviews 导致出版商流量 -42% 的背景，这个 core update 被业界寄予厚望——但 Google 的口径是"regular update"，暗示不会对 AI Overview 争议做出直接响应。建议等待两周后再做 Search Console 数据判断。

---

### 2. GOOGLE SEARCH LIVE 全球扩展——200+国家，Gemini 3.1 Flash Live 支持

**最新进展（2026年3月26日官宣，27日全面上线）：**

- Google Search Live 扩展至所有 AI Mode 可用的地区（200+ 国家和领土）
- 核心驱动：**Gemini 3.1 Flash Live** 新音频/语音模型
- 特性：多语言原生（用户用自己的语言对话，AI 也用用户语言回应）、实时摄像头交互、对话可随时深入
- 使用方式：打开 Google App（Android/iOS）→ 点击搜索栏 Live 图标 → 语音提问 → 获得音频回复 + 深入链接

**对 SEO 的影响：**

语音优先的 AI Mode 搜索意味着：
- 内容需要更强的**口语化可读性**（AI 口述时流畅度）
- 问答结构（Q&A format）更加重要——AI 直接朗读答案
- 长尾问题的自然语言变体会获得更多曝光
- "Featured snippet" 风格的内容更容易被语音选中

**战略含义：** Google 正在将 AI Mode/Search Live 打造成"对话式互联网的新入口"。内容策略需要从"关键词密度"转向"自然语言问答覆盖"。

---

### 3. GOOGLE AI OVERVIEWS 引流机制出现三种新测试——引用格式剧烈变动

**三种并行测试（2026年3月24-27日）:**

#### 3A. 巨大引用块出现在 AI Overviews 底部

- 测试格式：超大蓝色引用卡片堆叠在 AI 摘要正下方
- 类似 SGE（Search Generative Experience）时代的引用格式复古
- Glenn Gabe 描述："就像表格合并单元格一样的一整块巨大蓝框，包含略缩图（价值存疑）、网站名、favicon、描述和标题"
- Barry Schwartz 评价："这东西很丑，但也许更显眼，带来更多点击？"
- 可能是测试版 Bug，不会大规模推出——但表明 Google 在测试引用格式的变化

#### 3B. AI Mode 中链接改为 Overlay Cards（泡泡链接）——点击率受损

- 测试形式：AI Mode 中的品牌/网站引用不再直接跳转，而是弹出 Overlay Card
- Brodie Clark 录像展示：用户需要**额外一次点击**才能到达目标网站
- 对比：正常情况下点击品牌名直接跳转；新测试中需要先关掉泡泡再点击
- **直接后果：** 从 AI Mode 引流到网站的点击量下降
- Google 上个月刚改善了 AI Mode 内链——这可能是为了与那次改善保持一致的测试，但代价是流量

#### 3C. "SKIP DIGGING, START GUIDED RESEARCH" CTA 引导至 Web Guide 风格 SERP

- 测试触发：某些查询显示"Skip digging, start guided research"按钮
- 点击后进入类似 Web Guide 的 AI 组织化 SERP（按主题分类，而非传统链接列表）
- 2025年7月 Web Guide 首次推出（Labs），12月扩展到 All Tab，现在测试主动 CTA 引导
- Barry Schwartz 自述使用体验："我经常点击'Classic Search'切换回标准 SERP"——但对某些查询确实有帮助
- 战略含义：如果这个 CTA 大规模推出，SEO 的战场从"传统排名"扩展到"在 AI 组织化结果中如何呈现"

---

### 4. BING WEBMASTER TOOLS AI PERFORMANCE REPORTS—— grounding query ↔ page 双向映射正式上线

**重大升级（2026年3月24日官宣）：**

Microsoft Ads Blog 和 Bing Webmaster Tools 联合发布：Bing AI Performance Report 新增 **Grounding Query – Page Mapping** 功能。

**具体功能：**
- 选择某个 grounding query → 查看被引用的所有页面
- 选择某个页面 → 查看驱动其被引用的所有 grounding queries
- 支持 Copilot、Bing AI summaries 及部分合作伙伴集成
- Aleyda Solis 实测截图：双向映射清晰可见

**为什么这是重大突破：**
这是主要搜索引擎中**首次出现的可操作 AI 引用测量工具**。SEO 从业者第一次能够：
- 具体知道哪些查询触发了 Bing AI 对其内容的引用
- 量化页面级别的 AI 可见性
- 将内容更新与实际 AI 引用变化关联

**Google Search Console 仍然缺失同等功能**——Bing 在 AI 可见性可测量性方面暂时领先。

**局限：** 数据仍为采样（非完整日志），且公告发在 Microsoft Ads Blog 而非 Bing 博客——暗示商业化意图（广告商优先）。

---

### 5. GOOGLE 确认用 AI 重写 SERP 标题链接——"小而窄"测试引发出版商愤怒

**最新确认（2026年3月21日）：**

The Verge 报道 + Google 确认：Google 正在用 AI 生成某些文章在 SERP 上的标题链接（Title Links），不只是复制 Title Tag。

**Google 确认口径：**
- "small and narrow" test
- 影响新闻站点，但不限于新闻站点
- Google 表示"更广泛推出时可能不使用生成式 AI"——但未解释替代方案是什么

**Barry Schwartz 的立场（SERoundTable）：**
- 2021年 Google 就开始生成自定义 Title Links，这次"新"的是频率和 AI 介入程度
- 对"不写 title tag 或写得差的网站"有帮助
- 但对专业出版商而言：标题是品牌叙事的重要组成部分，被 AI 随意改写有声誉风险

**行业批评汇总（Round 155 追踪，本轮更新）：**
- Bastian Grimm（Peak Ace AG）：改变含义和语气，超出格式调整范围
- Brodie Clark：文章标题被重写，但含义在过程中丢失
- Nilay Patel（The Verge 主编）："Google 正在破坏传统10个蓝色链接，重写成最糟糕的垃圾"

**历史模式警示：** Round 155 分析过——Discover AI 标题：2025年12月"小"→2026年1月重新归类为"功能"→现在对传统 Search 用相同语言。"测试→功能→默认"的路径是预谋的。

---

### 6. GOOGLE ADS PMax 重大更新——AUDIENCE EXCLUSIONS、新报告、季节性主题

**三项重要更新（2026年3月27日）：**

#### 6A. First-Party Audience Exclusions（首次支持）
- PMax 广告主现在可以**排除**特定第一方受众群体
- 之前 PMax 自动覆盖所有受众，无法精细控制
- 这对于想要保护高价值客户（避免向已有客户重复投放）的广告主是重大改进

#### 6B. 全面 Audience Reporting
- 新增完整受众报告功能
- 广告主可以看到哪些受众触发了转化
- 支持 Network Segmentation（版位分类报告）

#### 6C. 季节性主题（Seasonal Themes）功能
- Google 正在推动广告主在 Asset Groups 中直接应用季节性主题（如 Easter）
- AI 自动调整创意素材以匹配季节性语境
- LinkedIn 帖子显示：Google 在推动广告主采用

**Google Ads API v23.2 同步发布：** 开发者需要关注。

---

### 7. GOOGLE ADS "CHAT" → "ADS ADVISOR"——品牌重命名透露 AI 广告策略

**最新动态（2026年3月27日）：**

Google Ads 将界面中的"Chat"按钮/版块**重命名为"Ads Advisor"**。

- 2026年1月首次发现时叫"Chat"
- Google 似乎更愿意称其为"Advisor"而非"Chat"
- 功能：通过对话式 AI 帮助广告主优化广告系列
- 这与 Google 整体的 Agentic Commerce 战略一致（UCP/A2A 协议）

---

### 8. GOOGLE MERCHANT CENTER 双规——车辆广告数据质量问题 + 缺货按钮要求

**两项政策更新（2026年3月）：**

#### 8A. 车辆广告数据质量警告（4月中旬生效）
- Google Merchant Center 将开始突出显示与车辆广告相关的数据质量问题
- 预计4月中旬正式实施

#### 8B. 缺货产品需要灰色"Buy Now"按钮（4月生效）
- Google Merchant Center 新规：缺货产品必须将 Buy Now 按钮置灰
- 不可用产品不能显示为可用状态
- 预计4月生效
- 适用于所有电商产品列表

---

### 9. CHATGPT 广告全面开放——接近所有美国免费用户，测量数据严重不足

**重大扩张（2026年3月22日）：**

The Information 独家报道 + Glenn Gabe 转发：

- OpenAI 宣布 ChatGPT 将在**未来几周内**向所有美国免费版和低成本版用户展示广告
- 从试点到全面开放的巨大跳跃

**广告效果测量现状（广告主困境）：**

据两家代理商高管反馈：
- **无法证明广告产生了任何可衡量的业务成果**
- OpenAI 不提供自动化购买接口——靠打电话、发电子表格和邮件人工对接
- 没有像 Google Ads 那样的标准性能数据报告
- 几乎没有定向选项
- OpenAI 建议广告主："提供更多文本和视觉变体，可提升广告展示频率和效果"——但没有实际数据支持

**战略含义：** ChatGPT Ads 目前是"买了也不知道有没有效"的状态。但随着全面开放和数据改进，这将成为品牌在 AI 原生界面中获取曝光的新战场。

---

### 10. BING AI IMAGE SEARCH 新界面 + MICROSOFT 发布 AI 性能 DASHBOARD 博文

**两项 Bing 更新（2026年3月24-27日）：**

#### Bing AI Image Search 新测试界面
- 右侧出现"New Version"或"Try AI-curated Image Search"按钮
- 点击后显示："AI is working on gathering best results for '[query]'..."
- 新界面：分类布局（categorized layout），而非传统网格
- Microsoft 描述："Use AI-powered image search to find higher quality images faster with curated layouts."
- **Bing 测试圆角（rounded corners）视频缩略图**——比传统直角更圆润

#### Microsoft Ads Blog 发布 AI Performance Dashboard 博文
- 这是 AI Performance 功能首次在 Ads Blog 正式宣告（而非 Webmaster Blog）
- 暗示微软将 AI 可见性工具定位为**广告商工具**，而非 SEO 工具
- Fabrice Canel（微软）预告："还有很多要来，敬请期待。"

---

## 延续自 Round 155 的关键框架（保持有效）

- **Google-Agent 用户代理（3月20日）**：AI 系统身份标识已确认，用于 Project Mariner 等 Google 基础设施 Agent
- **Agentic Web 五协议体系**：MCP/A2A/UCP/A2UI/AG-UI + WebMCP——机器对机器交互基础设施就绪
- **Google March 2026 Spam Update**：19.5小时完成（史上最快），spam 检测实时化
- **AI 可见性测量工具批评**（Pedro Dias）："卖的是置信区间的蜡笔画"——测量 ≠ 排名 ≠ 收入
- **流量崩溃结构性数据**：AI Overviews 后 -42%，突发新闻 +103%，常青内容 -40%
- **Perplexity 是唯一默认实时检索的平台**：绕过训练截止日期，始终引用最新内容
- **Q&A 格式是 AI 原生格式**：微软明确支持；隐藏内容对 AI 可能完全不可见
- **E-E-A-T 跨平台通用**：不仅是 Google 信号，也是 Bing Copilot、ChatGPT 等的统一偏好

---

## Actionable 选题建议

**topic211: Google Search Live Goes Global — How Voice-First AI Mode Changes SEO Content Strategy Forever**

框架：
1. 事件：Search Live 扩展至200+国家，Gemini 3.1 Flash Live 支持
2. 为什么重要：语音优先的 AI Mode 是搜索的新界面形态
3. 内容影响：口语化、可朗读性、Q&A 格式成为新的排名维度
4. 技术实现：如何在现有内容中嵌入"语音友好"结构
5. 长尾语义覆盖：自然语言问题变体的内容布局策略
6. 行动清单：30天内为你的内容添加语音优先版本

**topic212: The AI Overview引流正在崩溃——Overlay Cards、Web Guide、Big Citation Blocks 三大测试解析**

框架：
1. 事件：Google 同时测试三种 AI Overviews 引用格式变化
2. Overlay Cards：额外点击导致 CTR 下降的实测影响
3. 巨大引用块：SGEReturn 的视觉和 UX 分析
4. Guided Research CTA：Web Guide SERP 对传统排名的冲击
5. 出版商的困境：Google 的自然状态是吸收内容而非发送流量
6. 应对策略：如何在 AI 摘要被截流的情况下保持可见性
7. 数据支撑：42% 流量消失背后的机制（Round 155 数据）

**topic213: Bing AI Citation Mapping — The First Measurable AI Attribution Tool (And What to Do With It)**

框架：
1. 功能详解：grounding query ↔ page 双向映射的实际操作
2. 首次可测量性：SEO 第一次能看到"哪些查询触发了我内容的 AI 引用"
3. 与 Google 的对比：GSC 缺失功能，Bing 暂时领先
4. 数据局限性：采样数据，非完整日志
5. 战略性应用：基于 AI 引用数据的内容优化闭环
6. 行动建议：现在就去 Bing Webmaster Tools 激活并监控 AI Performance Report
7. 预告：Microsoft 暗示还有更多 AI 可见性工具即将发布

---

## 新趋势摘要（Round 157）

- 🔴 **Google March 2026 Core Update 正式上线**（3/27，预计两周完成）——首个年度核心更新，非惩罚性，聚焦"relevant, satisfying content"
- 🔴 **Google Search Live 全球扩展**（200+国家）——Gemini 3.1 Flash Live，多语言原生，语音+摄像头 AI Mode
- 🔴 **AI Mode 引流机制三路并行测试**：Overlay Cards（-CTR）、巨大引用块（视觉回归）、Guided Research CTA（Web Guide 引导）
- 🟡 **Google 确认 AI 重写 SERP 标题**——"小而窄"测试，出版商愤怒，历史上"测试→功能→默认"路径预谋清晰
- 🟡 **Bing AI Performance Dashboard 双向映射正式上线**——grounding query ↔ page 可追踪，SEO 首次获得可操作 AI 引用数据
- 🟡 **ChatGPT Ads 即将向所有美国用户开放**——效果测量严重缺失，自动化购买接口不存在
- 🟡 **Google Ads PMax 三项重大更新**：Audience Exclusions（首次支持）、全面报告、季节性主题
- 🟡 **Google Ads "Chat" → "Ads Advisor"**——品牌重命名透露 AI 广告策略方向
- 🟢 **Bing AI Image Search 新界面**——AI curated layouts + rounded corners 测试
- 🟢 **Google Merchant Center 两项新规**：车辆广告数据质量警告（4月中）+ 缺货按钮必须变灰（4月生效）
- 🟢 **Google-Agent UA（3/20）已确认运作**——Project Mariner 等 Google Agent 身份标识，代理网络基础设施就绪

---

*生成时间：2026-03-29 11:30 GMT+8*
*主要来源：SERoundTable (Barry Schwartz), Search Engine Land (Danny Goodwin, Glyn Evans), Glenn Gabe, Brodie Clark, Aleyda Solis, Sachin Patel, Len, The Information (opens signup), Microsoft Ads Blog (Fabrice Canel), Google (@rajanpatel), Twitter/X community*
