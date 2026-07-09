# Thesis Reading Loop Protocol

Use this protocol for full deep reads, multi-source synthesis, long-running discussion, portfolio translation, discussion-to-deck work, and research-knowledge-base handoff work. Do not invoke the full loop for a narrow definition or quick factual answer.

For newly supplied papers, reports, technical blogs, PDFs, URLs, abstracts, screenshots, or paper notes, start with the pre-loop triage gate unless the user explicitly asks to skip it.

## Loop Contract

Define these fields before execution:

| Field | Required decision |
|---|---|
| Goal | What understanding or artifact must exist at the end? |
| Source boundary | Which primary and secondary sources may be used? |
| Output mode | Triage brief, deep read, synthesis, translation, post, visual deck, or paper knowledge package |
| Evidence | What proves the output is grounded and complete? |
| State | Where progress, decisions, and open questions persist |
| Revision budget | Default: two reviewer-driven revisions after the deep-read loop starts |
| Stop rule | Triage decision, pass threshold, blocked source, exhausted budget, or human decision |
| Human gate | Continue after triage, interpretation choice, final narrative, publication, knowledge-base handoff, or external action |

## State Machine

Use these statuses in the per-paper state file:

1. `intake`: identify source and goal.
2. `triage`: produce the 500-character reading-value brief from limited but inspected source information.
3. `awaiting_human`: wait for the user to decide whether to continue into the full verified loop or downstream handoff.
4. `source_ready`: confirm that the evidence can be inspected for full analysis.
5. `drafting`: build the argument map and requested output.
6. `verifying`: run a separate review against the source and rubric.
7. `revising`: address blocking findings.
8. `discussion`: preserve durable insights from follow-up dialogue.
9. `package_ready`: a Paper Knowledge Package exists and can be handed to a downstream knowledge loop.
10. `deck_ready`: enough paper and discussion context exists for visual synthesis.
11. `complete`: acceptance criteria passed and required human gates closed.
12. `blocked`: source, evidence, tool, or decision prevents valid continuation.

Do not move directly from `triage` to `drafting` unless the user confirms continuation or explicitly requested full analysis from the start. Do not move directly from `drafting` to `complete` for a verified-loop task. Do not move from `package_ready` into `research-knowledge-base` without explicit user approval.

## Triage Pass

The triage pass is a low-cost screening step, not a full paper analysis.

Use only enough evidence to judge reading value:

- title, abstract, introduction, conclusion, official project page, source metadata, screenshots, pasted excerpts, or user-provided notes;
- clearly label when the source is partial or secondary;
- do not invent datasets, metrics, results, authors, venues, or limitations;
- do not spend the full deep-read budget or generate the full structured deep read.

Return a Triage Brief with:

- core idea;
- significance for future AI development;
- value rating: high / medium / low;
- decision: worth deep reading yes / maybe / no;
- confidence and visible limitations;
- the question asking whether to continue into the full verified loop.

If the source is too incomplete even for triage, set status to `blocked` and request the missing source or excerpt.

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

## Knowledge Base Handoff Pass

After the verified reading loop has passed and follow-up discussion has produced durable insights, generate a Paper Knowledge Package.

The package must include:

- source metadata and source confidence;
- verified core thesis and research problem;
- method or mechanism;
- key evidence and evidence strength;
- limitations and independent critique;
- discussion synthesis;
- AI / UX / HCI translation;
- portfolio relevance;
- open questions;
- suggested knowledge-base links and belief update type.

Then ask the user whether to enter the Research Knowledge Base Loop:

1. Add to knowledge base
2. Generate Knowledge Card draft only
3. Skip for now

If the user chooses `Add to knowledge base`, pass the package to `research-knowledge-base`. If the user chooses draft only, generate a draft card but do not update indexes or beliefs. If the user skips, record the package location and stop.

## Acceptance And Stop Rules

Complete a triage step only when:

- it fits the 500-character limit;
- source confidence and limitations are visible;
- value rating and deep-read decision are explicit;
- the state file records the triage result and next action.

Complete a deep read only when:

- the rubric score meets its threshold;
- no critical failure remains;
- source limitations and uncertainty are visible;
- the requested output mode is structurally complete;
- the state file records the final status and open questions.

Complete a handoff package only when:

- it is clearly labeled as a handoff object;
- source-grounded facts, user discussion insights, and model recommendations are separated;
- confidence and limitations are visible;
- the user has been asked whether to enter the downstream Knowledge Base Loop.

Stop as `blocked` when the central evidence is inaccessible, contradictory, corrupted, or too incomplete for the requested confidence level.

## Human Gates

Require explicit user judgment before:

- entering the full verified reading loop after the triage brief;
- choosing a controversial interpretation when evidence supports multiple readings;
- converting tentative research into a strong product recommendation;
- deciding the final editorial angle after multi-turn discussion;
- passing a Paper Knowledge Package into `research-knowledge-base`;
- generating or publishing the final public-facing deck when the user has not requested it;
- posting, emailing, submitting, modifying an external knowledge base, or otherwise publishing content.

## Budget Defaults

- Triage pass: one concise pass, no revision loop unless the source was misunderstood.
- Maximum revision rounds for full deep read: 2.
- Knowledge-base handoff: one package draft, then human decision.
- Maximum repeated attempts on an inaccessible source: 2 methods, then ask.
- Default reviewer count: 1 independent verifier.
- Use additional sources only when they resolve a material gap, current-state question, or conflict.
