# Codex Adapter

Use this adapter when running Thesis Reader in a repository or coding-agent environment.

## Runtime Rules

- Read `LOOP.md`, `CONTRACT.md`, and `references/loop-protocol.md` before executing a full loop.
- Store per-paper state outside the installed loop directory, for example `runs/{paper_id}/STATE.md`.
- Run available validators after producing structured outputs.
- Generate `handoff/packages/{paper_id}.md` for the Paper Knowledge Package when the user approves a handoff.
- Do not update `research-knowledge-base` indexes or beliefs from Thesis Reader directly.

## Handoff

When the user chooses `Add to knowledge base`, pass `handoff/packages/{paper_id}.md` into `research-knowledge-base` and create a separate PR for knowledge-base updates.
