# Immutable review record

Use this structure inline in a P-record or as a linked artifact. Each submitted review, correction or re-review gets a new `RV-*` record; preserve earlier records. [Work item rules](../docs/process/work-items.md) govern independence, findings and current/stale applicability.

```markdown
# RV-<id> — P-<existing id>
Kind: first verdict | re-review | correction | carry-forward assessment
Recorded at:
Reviewer: <stable actor_id; run_id; role; exact model; family or unavailable with reason>
Independence: <not an author of this candidate; contribution history checked; same-family limitation if any>
Assignment/lens and boundaries:
Decision and finite critique scope/round bound: <when open-ended critique is assigned; shared across agents, see assurance>
Candidate: <immutable version/hash + location; authors actor/run>
Inputs: <requirements/plan/contracts/knowledge versions/hashes; dirty snapshot base/hash/location when relevant>
Evidence reviewed/produced: <candidate/input versions; environment/tool versions; procedure/command; result/exit; output links>
Coverage and limits: <criterion/REQ/NFR/findings checked; untested/unknown surfaces>
Independent meaning, where consequential: <primary source/observation and dates; checker independent of disputed interpretation; own expected observations recorded before author's derived expectations; reconciliation or explicit limitation>
Peer verdict exposure: none before this first verdict | <what was visible and why this is a re-review>
Earlier records: <links; original finding IDs; author responses>
Outcome progress on re-review: <starting observation → current evidence; remaining failure; consecutive returns without progress; reassessment/extra-round decision if triggered>

## Findings
<stable RV-id/F-id> | <impact/severity> | <claim and location> | <evidence/reproduction> | <required outcome>
Recheck/disposition: <original finding id; fixed/disproved/deferred/authorized exception; evidence, rationale and responsible owner>

## Verdict and reasons
ACCEPTED | CHANGES_REQUIRED | BLOCKED
<criterion coverage, material risks, outstanding findings; BLOCKED names the missing input and next owner/action>
Recommendation/next handoff:

## Carry-forward assessment, if applicable
Old reviewed candidate/inputs → new candidate/inputs: <versions/hashes>
Change and dependency impact analysis:
Still-covered criteria/findings and evidence checked:
Limits and justification:
Independent acceptor: <actor_id/run_id>
```

The P-record separately records whether this review applies to its current candidate. A new commit or changed input does not alter this immutable record. A reviewer who edits the judged artifact becomes an author and cannot supply that candidate's independent acceptance. Reveal first verdicts to peer reviewers only after they have each submitted their own.
