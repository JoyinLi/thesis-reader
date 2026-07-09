---
name: thesis-reader
description: Read, screen, analyze, verify, and synthesize academic papers, research reports, arXiv papers, technical blogs, and paper notes. Use for pre-loop triage briefs, paper deep reading, structured research interpretation, source-grounded summaries, AI/UX/HCI or AI PM implications, portfolio translation, bilingual notes, multi-turn research discussion, Xiaohongshu research posts, 4-6 page visual decks, or a repeatable thesis-reading loop with persistent state, independent review, revision limits, and human approval gates.
---

# Thesis Reader

## Purpose

Turn research sources into rigorous, decision-useful understanding. Separate source claims, evidence, inference, critique, and design implications. Prefer professional Chinese unless the user requests another language.

## Select The Run Mode

- Use a **triage brief** by default whenever the user first provides a paper, research report, technical blog, PDF, URL, abstract, screenshot, or paper note. This is the pre-loop decision gate.
- Use a **single pass** for a quick brief, term explanation, or narrow factual question.
- Use the **verified reading loop** only after the triage brief when the user confirms deeper analysis, or when the user explicitly asks to skip triage and run the full deep read immediately.
- Use the **discussion-to-deck loop** only after a paper summary and meaningful follow-up discussion exist.

Read [loop-protocol.md](references/loop-protocol.md) before starting either loop. Create one state file per paper from [STATE.md](templates/STATE.md); keep run state outside the installed skill directory.

## Handle Sources

1. Identify whether the input is a PDF, URL, abstract, screenshot, pasted text, citation, or user note.
2. Prefer the paper PDF, official project page, author page, conference page, or arXiv record.
3. Label analysis based only on a secondary article when no primary source is available.
4. Stop and request the missing source when the central claims or evidence cannot be inspected.
5. Cite factual claims drawn from web-accessible sources. Never invent metadata, numbers, datasets, results, quotations, or limitations.
6. Mark uncertain statements as inference, interpretation, hypothesis, or open question.

## Run The Pre-Loop Triage Brief

When a new source arrives, first inspect only enough information to make a reading decision: title, abstract, introduction, conclusion, project page, summary, or visibly provided notes. Do not spend the full deep-read budget at this stage.

Produce a Chinese **Triage Brief** in 500 Chinese characters or fewer using [output-templates.md](references/output-templates.md). It must include:

- the paper or content's core idea;
- why it may matter for future AI development;
- a value rating: high / medium / low;
- whether it is worth entering the full verified reading loop: yes / maybe / no;
- source confidence and visible limitations.

After the triage brief, ask whether to continue into the full Thesis Reader verified reading loop. Do not produce the full structured deep read in the same response unless the user explicitly requested full analysis or said to skip the triage gate.

## Run The Verified Reading Loop

Start this loop only when the user confirms after triage, or explicitly asks for full deep analysis.

1. **Preflight**
   Confirm source accessibility, user goal, output mode, and whether current information requires web verification. Initialize the state file.
2. **Orient**
   Capture title, authors, institution, date, venue or source type, field, core problem, and article structure.
3. **Build The Argument Map**
   Extract the thesis, motivation, method, evidence, conclusion, assumptions, limitations, and unresolved questions. Preserve the chain `problem -> method -> evidence -> conclusion`.
4. **Translate**
   Use [ux-hci-lens.md](references/ux-hci-lens.md) only after understanding the research. Convert implications into concrete capabilities, interface states, user controls, risks, and evaluation signals.
5. **Verify**
   Run a separate reviewer pass with [evaluation-rubric.md](references/evaluation-rubric.md). Prefer a fresh verifier agent when available. Give the verifier the source, requested output mode, rubric, and draft, but not the worker's self-justification.
6. **Revise**
   Fix blocking findings and re-run verification. Allow at most two revision rounds unless the user explicitly extends the budget.
7. **Handoff**
   Deliver the verified output with source limitations, remaining uncertainties, and the questions most worth discussing. Update the state file.

Run `python scripts/validate_output.py OUTPUT.md --mode deep-read` when a filesystem and Python are available. Run `python scripts/validate_output.py OUTPUT.md --mode triage-brief` for pre-loop triage outputs. Treat this structural validator as a supplement to, not a replacement for, source-based review.

## Continue Into Discussion And Visual Output

During follow-up discussion, record only durable additions in the run state:

- clarified concepts and corrected misunderstandings;
- user conclusions, disagreements, and open questions;
- new AI/UX/HCI implications;
- decisions about audience, narrative, and visual emphasis.

Do not generate the final Xiaohongshu deck merely because the deep read is complete. Wait for an explicit user request or a clear deck-production step. Then read [xiaohongshu-visual-deck.md](references/xiaohongshu-visual-deck.md), synthesize the paper with the discussion state, and verify the result with the visual-deck section of the rubric.

Before drafting a visual deck or poster, ask which poster style the user wants. Offer available style branches from [output-templates.md](references/output-templates.md), including **Neo-Vintage Print**, plus the existing default visual system. If the user gives no style, gives an unsupported style, or says to use the default, use the current default visual system from [xiaohongshu-visual-deck.md](references/xiaohongshu-visual-deck.md). Record the chosen or defaulted style in the run state.

## Output Modes

Choose the mode requested by the user. Default to **triage brief** for newly supplied sources and **structured deep read** after the user confirms continuation.

- **triage brief**: 500-character pre-loop screening summary and reading-value judgment.
- **structured deep read**: rigorous paper breakdown with six to eight sections.
- **quick brief**: short decision aid when the user explicitly asks for a brief instead of the triage gate.
- **concept explainer**: define and contextualize unfamiliar terms.
- **AI/UX/HCI translation**: emphasize product and interaction implications.
- **portfolio translation**: turn research into a demonstrable project direction.
- **Xiaohongshu post**: produce concise public-facing Chinese content.
- **Xiaohongshu visual deck**: produce a 4-6 page script after paper analysis and discussion.
- **bilingual note**: provide Chinese and English in parallel.

Read [output-templates.md](references/output-templates.md) for the selected format. Read only the other references needed for that run.

## Stop And Escalate

Stop the loop and ask the user when:

- the primary source is inaccessible and the requested claim cannot be verified;
- source metadata or reported results conflict materially;
- the user must choose between competing interpretations or output goals;
- two revision rounds fail the acceptance threshold;
- the next step would publish content, modify an external system, or make an irreversible decision.

Never let the loop change its own acceptance criteria to declare success. Record unresolved issues instead of hiding them.

## Quality Bar

- Preserve the paper's research logic and distinguish author claims from assessment.
- Explain technical concepts plainly without replacing precision with analogy.
- Judge evidence strength; do not equate confident prose with strong evidence.
- Name specific interface patterns, control points, feedback states, evaluation criteria, and risks.
- Make portfolio directions demonstrable through scenario, flow, system capability, interaction pattern, and evaluation signal.
- Prefer compact, high-signal output over generic background.
