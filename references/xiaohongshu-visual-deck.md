# Xiaohongshu Visual Deck

Use this reference when the user has already read or summarized a paper, then had a multi-turn discussion with an LM, and now wants to synthesize the paper's core thesis plus conversation highlights into 4-6 Xiaohongshu image-text pages.

## Input To Collect

Before drafting pages, identify:

1. Paper title, institution, author, field, and core thesis.
2. The user's strongest takeaways from the follow-up conversation.
3. Any disagreements, refinements, open questions, or design implications discovered during the discussion.
4. The intended audience: AI practitioner, UX/HCI designer, AI PM, portfolio reviewer, or general reader.
5. Whether the output is a text-only page script, image-generation prompt, Figma/page layout spec, or all of these.
6. Poster style branch. Ask the user to choose from available branches in [output-templates.md](output-templates.md), including **Neo-Vintage Print**, or the default visual system below. If the user does not choose a style or gives an unsupported style, use the default visual system below.

If the source material is missing, ask for the paper summary, conversation notes, or pasted transcript. If only partial notes exist, proceed but mark uncertain claims.

## Visual Reference Handling

If a `thesis` folder, image references, or previously generated paper-summary images are available in the task workspace, inspect them before writing the deck. Summarize their reusable visual rules:

- canvas ratio, usually 3:4 or 4:5 for Xiaohongshu;
- background color, spacing, title placement, typography scale, and card density;
- highlight color and whether it is used for lines, labels, diagrams, or key numbers;
- page rhythm, such as cover page, framework page, method page, implication page;
- diagram style, such as simple boxes, thin lines, large keywords, minimal charts, or keynote-style callouts.

If no reference images are available, use the default visual system below.

## Poster Style Selection

Before drafting a visual deck, ask:

```text
这组海报想用什么视觉风格？可选：Default Clean Research Deck / Neo-Vintage Print。没有偏好我会按默认风格生成。
```

Use the user's selected style only when it matches an available style branch in [output-templates.md](output-templates.md). For **Neo-Vintage Print**, follow its full branch instructions and image prompt starter from that file. For no answer, unknown style, or default request, use the Default Visual System below.

## Default Visual System

Maintain a simplified iOS official keynote / product-launch deck feeling:

- large title, restrained subtitle, clear hierarchy;
- generous whitespace, minimal decoration, no cluttered collage;
- dark or light neutral background depending on the institution's visual language;
- one dominant highlight color per deck;
- thin dividers, soft panels, clean callouts, and simple geometric diagrams;
- 1 core idea per page, 2-4 supporting points at most;
- avoid dense paragraphs, excessive gradients, sticker-like social media decoration, and generic tech backgrounds.

Use institution-consistent visual highlights:

| Institution / source type | Visual direction |
|---|---|
| OpenAI / ChatGPT | neutral black, white, and soft gray; use restrained green or teal only as the highlight |
| NVIDIA | black or charcoal base with NVIDIA green highlight |
| Anthropic / Claude | warm off-white, deep brown or charcoal text, restrained warm accent |
| Google / DeepMind | white or light neutral base; use Google blue, green, yellow, and red sparingly, preferably one accent at a time |
| Apple | white, black, silver gray, glass-like restraint; use color only for emphasis |
| Meta | clean light or dark base with blue accent |
| Microsoft | neutral base with blue accent or subtle four-color reference |
| pure academic paper | no forced brand color; keep black, white, gray, and one quiet accent such as blue, green, or violet |

If exact brand styling is uncertain, infer from the institution's official website, logo, or paper/project page. Do not over-brand academic content.

## Content Strategy

Do not simply compress the paper summary. The deck should reflect what became clearer after the LM conversation:

1. The paper's original argument.
2. The user's updated understanding.
3. The highest-value conceptual distinction.
4. The method or evidence pattern worth learning.
5. The implication for AI products, UX/HCI, AI PM, or portfolio work.

Prefer a strong editorial line. Each page needs a point of view, not just a section label.

## Recommended 4-6 Page Structure

Use 5 pages by default. Expand to 6 pages when the method or design implication needs more room. Use 4 pages when the paper is narrow or the user wants concise social content.

### 4-Page Version

1. **Cover / Core Thesis**
   State the paper's strongest claim in one sentence.
2. **How It Argues**
   Show the method, framework, or evidence logic.
3. **What The Discussion Clarified**
   Summarize the most important insight from the multi-turn LM conversation.
4. **Why It Matters**
   Translate into AI product, UX/HCI, AI PM, or portfolio implications.

### 5-Page Version

1. **Cover / One-Sentence Takeaway**
   Use a sharp title plus a plain-language subtitle.
2. **Research Problem**
   Explain what old assumption or product pattern the paper challenges.
3. **Method / Framework**
   Visualize the mechanism, pipeline, comparison, or conceptual model.
4. **Conversation Insight**
   Summarize what the user and LM figured out beyond the paper summary: distinction, caveat, analogy, critique, or extension.
5. **Design / Product Implication**
   Explain what designers, AI PMs, or HCI researchers should do differently.

### 6-Page Version

1. **Cover / Core Thesis**
2. **Why This Problem Exists**
3. **Method Or Argument Structure**
4. **Key Evidence And Limitation**
5. **LM Conversation: What Became Clearer**
6. **AI / UX / HCI / Portfolio Takeaway**

## Per-Page Writing Rules

For each page, produce:

- **page title**: 6-14 Chinese characters when possible, strong and specific.
- **one-sentence point**: the page's real argument.
- **visual layout**: describe composition, hierarchy, and key visual element.
- **main copy**: 2-4 bullets or short phrases, not a long paragraph.
- **highlight element**: one keyword, number, quote fragment, diagram label, or contrast pair.
- **image prompt**: if the user wants image generation, provide a standalone prompt for that page.

Keep the copy professional and compact. Avoid clickbait, exaggerated certainty, and vague phrases such as "颠覆未来" unless the paper truly supports it.

## Page Script Template

Use this output shape when the user asks for the deck plan:

```md
## 图文总标题
[title]

## 视觉系统
- 风格:
- 背景:
- 主色:
- 高亮色:
- 字体气质:
- 版式规则:

## Page 1
- 标题:
- 一句话观点:
- 画面布局:
- 正文:
- 高亮:
- 生成图 prompt:
```

Repeat for all pages.

## Quality Checklist

Before finalizing, check:

- Does every page contain only one central idea?
- Does the sequence tell a story rather than list paper sections mechanically?
- Does at least one page capture the unique insight from the LM conversation?
- Does the final page translate the paper into concrete AI/UX/HCI/product judgment?
- Does the visual style match the selected branch? For the default branch, keep it close to an iOS keynote deck: sparse, precise, and polished. For Neo-Vintage Print, keep the aged paper, modular grid, blueprint line art, teal/vermilion accents, and technical print density consistent.
- Is the highlight color consistent with the research institution when appropriate?
- If it is a pure academic paper, is the deck clean without forced corporate branding?
