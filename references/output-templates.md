# Output Templates

Use these templates when the user asks for a specific output format. Adapt section depth to the source quality and user goal.

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

## Quick Brief

Use this when the user wants to decide whether a paper is worth reading.

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
