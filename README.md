# Thesis Reader

A reusable skill for source-grounded paper reading, AI/UX/HCI translation, multi-turn discussion, and research-to-visual-deck synthesis.

## Structure

```text
SKILL.md
agents/openai.yaml
references/output-templates.md
references/ux-hci-lens.md
references/xiaohongshu-visual-deck.md
references/loop-protocol.md
references/evaluation-rubric.md
templates/STATE.md
scripts/validate_output.py
```

## Two Layers

- **Thesis Reader Skill** defines source handling, research analysis, output modes, and AI/UX/HCI translation.
- **Thesis Reading Loop** adds preflight, persistent state, an independent verifier, up to two revision rounds, stop rules, and human approval gates.

The skill can still answer narrow questions in one pass. Use the verified loop for full paper reads, synthesis, portfolio translation, and long-running discussion.

## Verified Loop

```text
source intake
-> argument map
-> requested output
-> independent verification
-> bounded revision
-> discussion handoff
-> human-approved visual synthesis
```

Create a fresh state file from `templates/STATE.md` for each paper. Store run state with the paper project or output, not inside the installed skill directory.

## Visual Deck Styles

Before creating a visual deck or poster, the loop asks for a poster style. Available branches live in `references/output-templates.md`.

- `Default Clean Research Deck`: the existing clean, keynote-like research deck.
- `Neo-Vintage Print`: aged paper, modular editorial grid, blueprint line art, teal/vermilion accents, halftone texture, and dense technical-poster composition.

If the user does not choose a supported style, the loop falls back to `Default Clean Research Deck`.

## Structural Validation

When Python and a filesystem are available:

```bash
python scripts/validate_output.py path/to/output.md --mode deep-read
python scripts/validate_output.py path/to/deck.md --mode visual-deck
```

The script checks required structure. The reviewer rubric remains responsible for factual grounding, evidence quality, and inference boundaries.
