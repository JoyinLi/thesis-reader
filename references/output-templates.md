# Output Templates

Use these templates when the user asks for a specific output format. Adapt section depth to the source quality and user goal.

## Triage Brief (Pre-Loop Screening)

Use this by default immediately after receiving a new paper, report, technical blog, URL, PDF, or research note. The goal is to help decide whether the source deserves a full Thesis Reader deep read.

Constraints:

- Maximum 500 Chinese characters.
- This is a reading-value assessment, not a verified deep read.
- Clearly separate known source information from inference.
- Use professional Chinese unless the user requests another language.

Required structure:

- **核心介绍**: 这篇研究 / 内容试图解决什么问题？核心观点是什么？
- **对 AI 未来发展的意义**: 它可能改变什么能力边界、研究方向或产品可能性？
- **价值判断**: high / medium / low, with one sentence reason.
- **是否值得精读**: yes / maybe / no, with one sentence reason.
- **可信度与限制**: 当前依据是论文全文、摘要、官方介绍、截图、用户笔记还是二手文章？哪些地方尚无法确认？

End with:

`是否进入完整 Thesis Reader verified reading loop？`

## Structured Deep Read

1. **论文基本信息**
   - 研究领域与核心问题
   - 作者 / 机构 / 发表时间 / 来源
   - 行文结构
   - 主要贡献一句话总结

2. **研究动机**
   - 现有方法存在什么问题
   - 为什么这项研究有必要
   - 它试图改变哪个默认假设

3. **核心方法 / 模型 / 框架**
   - 关键思路
   - 创新点
   - 与传统方法的区别
   - 用通俗语言解释核心机制

4. **实验设计 / 论证方法**
   - 数据集 / 样本 / 材料
   - 评价指标
   - 对比基线
   - 主要结果
   - 证据强度判断

5. **结论与局限**
   - 论文得出了什么结论？
   - 作者提到的不足与未来工作
   - 论文没有充分证明、实验覆盖不足或假设过强的地方
   - 是否适用于当前 ai 时代？
   - 放到今天的大模型、agent、多模态、人机交互语境下，仍然成立的部分是什么？
   - 放到今天已经不够的部分是什么？

6. **个人理解（用通俗语言）**
   - 这篇论文到底在解决什么问题？
   - 用非技术读者也能理解的语言解释核心问题、核心方法和核心结论
   - 对用户所在领域（hci、ai ux、ai pm）有什么启发？
   - 可以如何复现 / 改进？
   - 有哪些当下的学术演进、相关研究脉络或值得继续追的方向？
   - 它真正有价值的地方
   - 可能被误读、过度营销或错误迁移的地方

7. **对 ai / ux / hci / ai pm 的启发**
   - 可以转化成什么产品能力
   - 界面需要新增哪些状态、控制点或解释层
   - 对 agent、multimodal、memory、trust、evaluation 的影响

8. **可复现 / 可改进 / 可作品集化**
   - 最小 demo
   - 关键交互流程
   - 数据或模拟方式
   - 评价指标
   - 作品集叙事角度

## Paper Knowledge Package

Use this after the verified reading loop and meaningful discussion, or when the user explicitly asks to export the paper into a downstream knowledge loop. This is a handoff object, not a public-facing summary.

```md
# Paper Knowledge Package

## Source Metadata
- Title:
- Authors:
- Institution / venue:
- Year / date:
- Source type:
- Primary source inspected: yes / no / partial
- Source confidence: high / medium / low

## Verified Core
- Core thesis:
- Research problem:
- Claimed contribution:
- Method or mechanism:
- Key evidence:
- Evidence strength: strong / medium / weak / unknown
- Author-stated limitations:
- Independent critique:

## Discussion Synthesis
- Concepts clarified:
- User conclusions:
- Disagreements or corrections:
- Open questions:
- What became clearer after discussion:

## AI / UX / HCI Translation
- System capability implied:
- Interface implication:
- User control or agency issue:
- Failure mode:
- Evaluation signal:
- Portfolio relevance:

## Knowledge Base Recommendation
- Add to knowledge base: yes / maybe / no
- Suggested domains:
- Suggested concepts:
- Suggested methods:
- Suggested UX patterns:
- Related existing beliefs:
- Belief update type: new / strengthen / weaken / challenge / none
- Confidence and limits:

## Handoff Gate
是否将这篇内容转入 Research Knowledge Base Loop？
1. Add to knowledge base
2. Generate Knowledge Card draft only
3. Skip for now
```

## Quick Brief

Use this when the user explicitly asks for a shorter summary instead of the default triage gate.

- **一句话结论**:
- **为什么重要**:
- **核心方法**:
- **最关键证据**:
- **最大局限**:
- **值得精读吗**: yes / maybe / no, with one sentence reason.
- **对用户的价值**: focus on ai, ux, hci, product, or portfolio relevance.

## Bilingual Note

Use paired paragraphs or a two-column table only when the user explicitly asks for bilingual output.

| 中文 | English |
|---|---|
| 核心观点 | core idea |
| 方法解释 | method explanation |
| 设计启发 | design implication |

Keep English precise and natural. Do not mechanically translate Chinese phrasing.

## Xiaohongshu Research Post

Use this when the user asks for public-facing content.

- **标题**: sharp, curiosity-driven, not clickbait.
- **200字正文**: explain the study, why it matters, and what designers/product people should learn.
- **图文页结构**:
  1. 核心观点 / 研究一句话
  2. 研究架构或方法
  3. 证据与论证方式
  4. 关键概念解释
  5. 对 ai 产品 / ux / hci 的影响

Style: clean, professional, high-signal. Avoid exaggerated claims.

For 4-6 page image-text decks after multi-turn discussion, use [xiaohongshu-visual-deck.md](xiaohongshu-visual-deck.md).

## Poster Style Branches

Use these branches when producing Xiaohongshu visual decks, poster scripts, Figma layout specs, or image-generation prompts. Ask the user which style they want before drafting poster pages. If the user does not choose a style, chooses an unknown style, or asks for the default, use the clean professional visual system already defined in [xiaohongshu-visual-deck.md](xiaohongshu-visual-deck.md).

Across all visual style branches, shapes are not fixed assets. Choose shapes from the content relationship on that page: nested circles for layered scope, rings for containment, paths for process, split panels for contrast, matrices for evaluation, loops for feedback, fracture or warning forms for risk, and sparse nodes for networks. Shapes must clarify the idea, carry visual taste, and preserve simplicity. Do not repeat a decorative motif merely because it appeared in a reference image.

### Default Clean Research Deck

Use this branch when no specific style is selected. Follow the Default Visual System in [xiaohongshu-visual-deck.md](xiaohongshu-visual-deck.md): simplified iOS keynote / product-launch feeling, large title, generous whitespace, restrained subtitle, one dominant highlight color, thin dividers, soft panels, clean callouts, and simple geometric diagrams. Use only the shapes needed to explain the page's concept.

### Neo-Vintage Print

Use this branch for dense, editorial research posters that should feel like a contemporary AI/HCI zine printed on old technical manual paper.

- **Core mood**: neo-vintage technical print, academic poster, risograph zine, engineering manual, high-signal social research card.
- **Canvas**: vertical 3:4 or 4:5; use visible page numbers, series labels, thin outer borders, and a modular grid.
- **Background**: warm off-white or aged paper, subtle fiber texture, light grain, mild ink noise. Avoid glossy gradients, dark tech backgrounds, and clean corporate white.
- **Typography**: oversized bold black title, strong Chinese sans-serif headline, compact supporting text, small all-caps English metadata. Mix large numerals with tight captions.
- **Layout**: asymmetric but grid-disciplined. Use panels, dividers, index columns, numbered steps, footer strips, side labels, and boxed callouts. Keep every block aligned to a visible grid.
- **Color palette**: black text; electric blueprint blue for line art and emphasis; muted teal-green for panels; warm vermilion or orange-red for warnings, dots, labels, and contrast. Use cream as the base. Limit to 3 accent colors.
- **Graphic language**: content-derived technical diagrams, such as nested rings, process paths, matrices, contour fields, sparse nodes, dashed connectors, small icon boxes, crosshair marks, circle/square markers, and simple geometric overlays. Blue wireframe waveforms are optional, not mandatory; use them only when they explain flow, transformation, uncertainty, or layered structure.
- **Information density**: medium-high. Each page may contain a headline, subtitle, diagram, 2-4 compact text blocks, and one footer insight, but avoid unreadable paragraphs.
- **Page rhythm**: cover or thesis page; framework or comparison page; method/process page; risk or limitation page; implication or takeaway page.
- **Use for**: prompt/context/harness/loop concepts, AI system workflows, evaluation methods, research frameworks, conceptual comparisons, and design implications that benefit from technical diagramming.
- **Avoid**: fixed decorative shapes, repeated visual motifs without semantic purpose, watercolor, hand-drawn scrapbook, cyberpunk neon, heavy 3D, soft glassmorphism, childish stickers, photo collages, random decoration, and decorative elements that do not encode meaning.

Image prompt starter:

```text
Neo-vintage technical print poster, vertical 3:4, warm aged paper texture, bold black Chinese and English sans-serif typography, modular editorial grid, thin black borders and dividers, page number and series metadata, content-derived technical diagram shapes that match the page concept, blueprint-blue line work used only where it explains structure or relation, muted teal panels, vermilion warning accents, dotted halftone texture, compact research-card layout, precise AI/HCI technical manual feeling, high but readable information density, clean alignment, risograph ink grain, no fixed decorative motif, no glossy gradients, no stock photos, no cartoon style.
```

## Portfolio Translation

Use this when the user wants to turn research into a portfolio project.

1. **设计命题**
   Convert the research into a user-facing problem statement.
2. **目标用户与场景**
   Name the user, context, trigger, and pain point.
3. **系统能力**
   Specify what the ai system must perceive, infer, remember, decide, or generate.
4. **关键交互**
   Include user input, agent planning, system feedback, intervention, recovery, and final output.
5. **界面模块**
   Define status panel, task tree, memory scope, confidence indicator, intervention button, or other relevant modules.
6. **评估方式**
   Include task success, user trust, correction rate, cognitive load, latency, and failure recovery.
7. **作品集叙事**
   Explain why this project shows future-facing ai interaction judgment.
