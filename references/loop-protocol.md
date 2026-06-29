# Thesis Reading Loop Protocol

Use this protocol for full deep reads, multi-source synthesis, long-running discussion, portfolio translation, and discussion-to-deck work. Do not invoke the full loop for a narrow definition or quick factual answer.

## Loop Contract

Define these fields before execution:

| Field | Required decision |
|---|---|
| Goal | What understanding or artifact must exist at the end? |
| Source boundary | Which primary and secondary sources may be used? |
| Output mode | Deep read, synthesis, translation, post, or visual deck |
| Evidence | What proves the output is grounded and complete? |
| State | Where progress, decisions, and open questions persist |
| Revision budget | Default: two reviewer-driven revisions |
| Stop rule | Pass threshold, blocked source, exhausted budget, or human decision |
| Human gate | Interpretation choice, final narrative, publication, or external action |

## State Machine

Use these statuses in the per-paper state file:

1. `intake`: identify source and goal.
2. `source_ready`: confirm that the evidence can be inspected.
3. `drafting`: build the argument map and requested output.
4. `verifying`: run a separate review against the source and rubric.
5. `revising`: address blocking findings.
6. `discussion`: preserve durable insights from follow-up dialogue.
7. `deck_ready`: enough paper and discussion context exists for visual synthesis.
8. `awaiting_human`: wait for a judgment or publication decision.
9. `complete`: acceptance criteria passed and required human gates closed.
10. `blocked`: source, evidence, tool, or decision prevents valid continuation.

Do not move directly from `drafting` to `complete` for a verified-loop task.

## Worker Pass

Produce an argument map before polished prose:

- research question and prior limitation;
- central claim and claimed novelty;
- method or conceptual mechanism;
- evidence mapped to each important claim;
- conclusion supported by that evidence;
- author-stated limitations;
- independent critique and open questions;
- relevance to the user's AI/UX/HCI or product goal.

When evidence is not reported, write `not reported` rather than inferring a plausible value.

## Verifier Pass

Keep maker and checker logically separate.

- Prefer a fresh verifier agent or clean context.
- Provide the source, user request, selected output template, rubric, and draft.
- Ask for findings before suggestions.
- Require locations or claim references for blocking findings.
- Do not ask the verifier to reward style or agree with the worker.
- Return `pass`, `revise`, or `blocked`, plus scores and concrete findings.

When no separate agent is available, run a distinct second pass that reopens the source and checks each claim without relying on the draft's explanations.

## Revision Policy

1. Fix unsupported claims, factual errors, missing evidence, and source/inference confusion first.
2. Fix structural omissions and unclear technical explanations second.
3. Improve style only after correctness and completeness pass.
4. Re-run the complete rubric after each revision.
5. Stop after two failed revisions and request human direction. Do not quietly broaden the task or alter the threshold.

## Acceptance And Stop Rules

Complete a deep read only when:

- the rubric score meets its threshold;
- no critical failure remains;
- source limitations and uncertainty are visible;
- the requested output mode is structurally complete;
- the state file records the final status and open questions.

Stop as `blocked` when the central evidence is inaccessible, contradictory, corrupted, or too incomplete for the requested confidence level.

## Human Gates

Require explicit user judgment before:

- choosing a controversial interpretation when evidence supports multiple readings;
- converting tentative research into a strong product recommendation;
- deciding the final editorial angle after multi-turn discussion;
- generating or publishing the final public-facing deck when the user has not requested it;
- posting, emailing, submitting, or otherwise publishing content.

## Budget Defaults

- Maximum revision rounds: 2.
- Maximum repeated attempts on an inaccessible source: 2 methods, then ask.
- Default reviewer count: 1 independent verifier.
- Use additional sources only when they resolve a material gap, current-state question, or conflict.

