# Thesis Reader Contract

## Output: Paper Knowledge Package

Thesis Reader produces a Paper Knowledge Package after the verified reading loop and meaningful discussion are complete, or when the user explicitly asks to export the current research state.

This package is the platform-independent handoff object for downstream loops such as `research-knowledge-base`.

## Required Fields

- Source metadata
- Verified core thesis
- Research problem
- Method or mechanism
- Key evidence and evidence strength
- Author-stated limitations
- Independent critique
- Discussion synthesis
- AI / UX / HCI implications
- Portfolio relevance
- Open questions
- Suggested knowledge-base links

## Human Gate

Before sending the package into `research-knowledge-base`, ask the user:

`是否将这篇内容转入 Research Knowledge Base Loop？`

Options:

1. Add to knowledge base
2. Generate Knowledge Card draft only
3. Skip for now

Do not silently write long-term knowledge, indexes, or research beliefs without user approval.

## Downstream Contract

The package should conform to `research-knowledge-base/CONTRACT.md` as the input to the Knowledge Base Loop.
