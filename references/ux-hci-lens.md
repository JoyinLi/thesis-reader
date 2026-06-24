# AI / UX / HCI Translation Lens

Use this reference when the user asks what a paper means for interaction design, ai products, ai pm work, or portfolio strategy.

## Core Questions

Ask these questions after understanding the paper:

1. What new system capability does this research make more plausible?
2. What will the user need to understand, control, correct, or trust?
3. What hidden state must become visible in the interface?
4. What failure mode does the research introduce or reduce?
5. What new evaluation metric should designers care about?
6. What design artifact could demonstrate this insight in a portfolio?

## Translation Targets

Map research insights into concrete interface implications:

| Research implication | Product / interaction translation |
|---|---|
| model plans over long tasks | task tree, progress hierarchy, interruption and resume controls |
| model uses tools or skills | skill invocation log, tool permission prompt, reversible action history |
| model has uncertainty | confidence indicator, source grounding, ask-before-act threshold |
| model uses memory | memory scope indicator, editable memory card, temporary vs persistent memory choice |
| model is multimodal | input modality state, camera/mic context preview, ambiguity repair |
| model can act proactively | attention demand level, user consent boundary, quiet vs active mode |
| model simulates or predicts outcomes | preview, counterfactual comparison, rollback path |
| model personalizes behavior | preference explanation, reset control, privacy boundary |

## Agent Product Checklist

For agent-related papers, always consider:

- **planning visibility**: can the user see what the agent is trying to do?
- **execution state**: is the agent idle, thinking, using tools, waiting, blocked, or done?
- **intervention**: can the user pause, redirect, approve, reject, or undo?
- **memory boundary**: what does the agent remember, for how long, and why?
- **confidence and grounding**: what evidence supports the answer or action?
- **failure recovery**: how does the agent explain, repair, and continue?
- **relationship tone**: is the agent being useful, sycophantic, intrusive, or appropriately empathetic?

## Portfolio Judgment

A strong portfolio translation should not merely restyle a chatbot. It should show:

- a future-facing interaction problem grounded in a real research capability;
- a concrete scenario where the old interface pattern breaks;
- a new interface pattern that exposes system state and preserves user agency;
- a prototypeable flow, not just a concept poster;
- evaluation criteria that prove the design is better than a generic chat interface.
