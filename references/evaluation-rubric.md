# Thesis Reader Evaluation Rubric

Use this rubric for the verifier pass. Score each dimension from 0 to 2.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Source integrity | Primary source absent or misrepresented | Source present but provenance or coverage is unclear | Primary source preferred, provenance clear, secondary material labeled |
| Claim fidelity | Important claims are wrong or unsupported | Core thesis is mostly right with some compression or ambiguity | Thesis, contribution, and claim boundaries match the source |
| Method and evidence | Method or evidence is missing/misread | Main method and results appear but important details are weak | Method, datasets or samples, baselines, metrics, results, and evidence strength are correctly handled |
| Conclusions and limits | Inference is presented as fact or limits are hidden | Some distinction exists but critique is incomplete | Author conclusions, stated limits, independent critique, and open questions are clearly separated |
| Explanation quality | Technical explanation is misleading or opaque | Understandable but imprecise in places | Plain-language explanation preserves the actual mechanism and necessary terminology |
| AI/UX/HCI translation | Generic claims such as "improves UX" | Some concrete implications but weak connection to evidence | Capabilities, interface states, controls, risks, and evaluation signals follow from the research |
| Output fitness | Requested structure or audience is missed | Structure is mostly complete | Output mode, audience, length, and deliverable requirements are satisfied |

## Decision

- `pass`: at least 12/14, no dimension scored 0, and no critical failure.
- `revise`: 8-11, or any dimension scored 0 that can be corrected from available evidence.
- `blocked`: below 8, inaccessible central evidence, irreconcilable source conflict, or required human judgment.

## Critical Failures

Any one of these prevents a pass:

- invented authors, dates, institutions, datasets, sample sizes, metrics, results, quotations, or limitations;
- treating a secondary summary as if it were the paper;
- asserting causality, generalization, or product readiness beyond the evidence;
- hiding that the full source could not be inspected;
- mixing author claims and reviewer inference without labels;
- producing a final public deck before the requested discussion or human gate;
- using citations that do not support the attached claim.

## Mode-Specific Checks

### Structured Deep Read

- Cover basic information, motivation, method, evidence, conclusion, limitations, plain-language understanding, AI/UX/HCI implications, and actionable directions.
- Map major conclusions to evidence rather than listing results without interpretation.
- State what remains unproven.

### Quick Brief

- Explain whether the source deserves a deeper read and why.
- Include the most important evidence and the largest limitation.
- Avoid implying that a quick brief has the confidence of a full deep read.

### Portfolio Translation

- Define a user, scenario, trigger, system capability, interaction flow, failure recovery, and evaluation signal.
- Show how the research changes an interaction pattern rather than merely restyling chat.

### Xiaohongshu Visual Deck

- Use 4-6 pages and one central idea per page.
- Include at least one insight produced or clarified during the discussion.
- Preserve research caveats despite concise copy.
- Keep the final page concrete about product, UX/HCI, AI PM, or portfolio consequences.
- Treat visual polish as necessary but never as evidence of factual quality.

## Verifier Output

Return:

```md
Decision: pass | revise | blocked
Score: X/14
Critical failures: none | list

Blocking findings:
- [claim or section] finding and source-grounded reason

Non-blocking improvements:
- improvement

Required next action:
- revise | request source | request human decision | complete
```

