# Thesis Reader

A reusable loop for source-grounded paper reading, AI/UX/HCI translation, multi-turn discussion, research-to-visual-deck synthesis, and research-knowledge-base handoff.

## Structure

```text
LOOP.md
CONTRACT.md
SKILL.md
agents/openai.yaml
adapters/generic-agent.md
adapters/chatgpt-project.md
adapters/codex.md
references/output-templates.md
references/ux-hci-lens.md
references/xiaohongshu-visual-deck.md
references/loop-protocol.md
references/evaluation-rubric.md
references/knowledge-base-handoff.md
templates/STATE.md
scripts/validate_output.py
```

## Two Layers

- **Thesis Reader Skill** defines source handling, research analysis, output modes, and AI/UX/HCI translation.
- **Thesis Reading Loop** adds triage, preflight, persistent state, an independent verifier, up to two revision rounds, stop rules, human approval gates, and downstream handoff.

The skill can still answer narrow questions in one pass. Use the verified loop for full paper reads, synthesis, portfolio translation, and long-running discussion.

## Verified Loop

```text
source intake
-> triage brief
-> human decision
-> argument map
-> requested output
-> independent verification
-> bounded revision
-> discussion memory
-> paper knowledge package
-> knowledge-base handoff gate
```

Create a fresh state file from `templates/STATE.md` for each paper. Store run state with the paper project or output, not inside the installed skill directory.

## Knowledge Base Handoff

After verified reading and meaningful discussion, Thesis Reader can generate a `Paper Knowledge Package`.

The package is a platform-independent handoff object for `research-knowledge-base`.

Before downstream handoff, the loop must ask:

```text
是否将这篇内容转入 Research Knowledge Base Loop？
1. Add to knowledge base
2. Generate Knowledge Card draft only
3. Skip for now
```

Thesis Reader must not silently update long-term knowledge indexes, concept maps, or research beliefs.

## Visual Deck Styles

Before creating a visual deck or poster, the loop asks for a poster style. Available branches live in `references/output-templates.md`.

- `Default Clean Research Deck`: the existing clean, keynote-like research deck.
- `Neo-Vintage Print`: aged paper, modular editorial grid, blueprint line work, teal/vermilion accents, halftone texture, and dense technical-poster composition.

Visual shapes are never fixed template assets. The loop should choose shapes from the content relationship: rings for containment, paths for process, panels for contrast, loops for feedback, matrices for evaluation, or warning forms for risk. If the user does not choose a supported style, the loop falls back to `Default Clean Research Deck`.

## Structural Validation

When Python and a filesystem are available:

```bash
python scripts/validate_output.py path/to/output.md --mode triage-brief
python scripts/validate_output.py path/to/output.md --mode deep-read
python scripts/validate_output.py path/to/package.md --mode paper-knowledge-package
python scripts/validate_output.py path/to/deck.md --mode visual-deck
```

The script checks required structure. The reviewer rubric remains responsible for factual grounding, evidence quality, and inference boundaries.
