---
name: thesis-reader
description: read, analyze, and synthesize academic papers, research reports, arxiv papers, technical blogs, and paper notes into a reusable thesis-reading workflow. use when the user asks for paper deep reading, structured research interpretation, ai/ux/hci implications, portfolio translation, bilingual summaries, xiaohongshu-style research posts, 4-6 page visual decks after multi-turn lm discussion, or wants to understand a study's motivation, method, evidence, limitations, and product design meaning.
---

# Thesis Reader

## Overview

Use this skill to turn papers or research articles into a structured, decision-useful reading output. Default to professional Chinese, concise but not shallow, with clear separation between what the source says, what can be inferred, and what matters for ai/ux/hci/product work.

## Source Handling

1. Determine the input type: paper pdf, url, abstract, screenshots, pasted text, citation, or user notes.
2. Prefer primary sources: paper pdf, official project page, author blog, conference page, or arxiv record.
3. If only a secondary article is provided, state that the analysis is based on the provided article unless a primary source is found.
4. If the source is missing, ask for the paper, link, title, or pasted text before doing a full deep read.
5. When using web-accessible sources, cite the source for factual claims. Do not invent metadata, numbers, datasets, results, or limitations.
6. If a claim is uncertain, label it as inference, likely interpretation, or open question.

## Workflow

Use this sequence for full paper reading:

1. **Orient**
   Capture title, authors, institution, publication time, venue or source type, research field, core problem, and article structure.
2. **Extract The Thesis**
   Summarize the main contribution in one sentence. Then explain what the paper is really trying to prove or change.
3. **Motivation**
   Identify the prior problem, why existing methods are insufficient, and why this work is necessary now.
4. **Method**
   Explain the framework, model, experiment design, or conceptual move. Translate technical ideas into plain language without losing precision.
5. **Evidence**
   Extract datasets, tasks, baselines, metrics, major results, ablations, user studies, or qualitative evidence. If evidence is absent or weak, say so.
6. **Conclusion And Limits**
   Separate author-stated conclusions from your own assessment. Include assumptions, failure cases, missing evaluations, and future work.
7. **ai/ux/hci Translation**
   Explain implications for interaction design, agent products, multimodal ux, system feedback, trust, control, memory, evaluation, and portfolio opportunities.
8. **Actionable Output**
   Provide next-step artifacts when useful: demo concept, portfolio project angle, research-note card, xiaohongshu post, bilingual summary, or reproduction plan.

## Output Modes

Choose the output mode from the user request. If unspecified, use **structured deep read**.

- **structured deep read**: rigorous paper breakdown with six to eight sections.
- **quick brief**: short executive summary for deciding whether to read deeply.
- **concept explainer**: define and contextualize unfamiliar terms.
- **ux/hci translation**: emphasize product, interface, and design implications.
- **portfolio translation**: convert the research into a demo, case-study, or design direction.
- **xiaohongshu post**: turn the research into concise public-facing Chinese content.
- **xiaohongshu visual deck**: after a paper summary and multi-turn lm discussion, synthesize the paper thesis and conversation highlights into a 4-6 page xiaohongshu image-text deck with an iOS keynote-like visual style.
- **bilingual note**: provide Chinese and English in parallel.

See [output-templates.md](references/output-templates.md) for reusable structures. See [ux-hci-lens.md](references/ux-hci-lens.md) when translating research into product and interaction design insight. See [xiaohongshu-visual-deck.md](references/xiaohongshu-visual-deck.md) when turning a paper plus follow-up discussion into 4-6 image-text pages.

## Quality Bar

- Be direct. Do not overstate novelty just because a paper sounds impressive.
- Preserve the research logic: problem → method → evidence → conclusion → implication.
- Define technical terms in plain language when they affect understanding.
- Use tables only for exact mappings, comparisons, datasets, metrics, or design implications.
- Avoid long generic background sections. Keep the reading anchored to the paper.
- For ai/ux/hci implications, go beyond "better user experience"; name specific interface patterns, user control points, feedback states, evaluation criteria, and risks.
- When producing portfolio ideas, make them demonstrable: include scenario, user flow, system capability, interaction pattern, and evaluation signal.

## Default Structured Deep Read

Use this structure unless the user asks otherwise:

1. 论文基本信息
2. 研究动机
3. 核心方法 / 模型 / 框架
4. 实验设计 / 论证方法
5. 结论与局限
6. 个人理解：这篇研究到底解决了什么问题
7. 对 ai / ux / hci / ai pm 的启发
8. 可复现、可改进、可放入作品集的方向

Keep summaries compact, but expand the ux/hci implications when the user is preparing portfolio or product strategy work.
