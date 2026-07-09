# ChatGPT Project Adapter

Use this adapter when running Thesis Reader inside a ChatGPT Project.

## Runtime Rules

- Use the project files as loop references.
- For a new paper, URL, report, or note, start with the Triage Brief.
- Ask before entering the full verified reading loop.
- During follow-up discussion, preserve only durable insights.
- Keep outputs product-neutral by default: synthesize broad UX / HCI / AI PM directions and takeaway points, not any specific product, device, company project, or user project.
- Do not center Robot Phone, phone hardware, embodied devices, or any named product unless the source or user explicitly requests that product lens.
- At the end of verified reading and discussion, generate a Paper Knowledge Package.
- Ask whether to enter `research-knowledge-base`.

## Handoff Prompt

`是否将这篇内容转入 Research Knowledge Base Loop？`

Options:

1. Add to knowledge base
2. Generate Knowledge Card draft only
3. Skip for now

If the user approves, load the `research-knowledge-base` loop and use the Paper Knowledge Package as input.
