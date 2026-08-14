# Cycle-start assignment (template)

Copy the block below as the first message of a new task. Connect two folders: the project working folder and the autoteam canon. Fill in the task and constraints, replacing `<...>`. The task can be anything: a product from an idea, a redesign, analysis of someone else's code, an experiment — the orchestrator picks the route.

```
The autoteam folder holds the team's skill canon (library, read-only).
Read autoteam-orchestrator and work by the canon.
Mode: solution (autonomous, decision journal) | interactive.

Cycle start:
1. Copy the canon into the project: skills → .claude/skills/, docs and templates → autoteam/.
   Copy already exists — overwrite it entirely: the copy is a cache.
2. Onboarding: repository map (if it's not empty), resource inventory
   → registry docs/process/resources.md.
3. git: exists — work in it; doesn't — initialize. Checkpoint commit at the end
   of every wave. Cycle marker docs/process/.cycle-lock.
4. Decision journal docs/process/decisions.md (append-only, amendments).
5. First message to me — brief and digest: up to 3 questions where an early
   answer is cheapest, plus actions only I can take (accounts, payments,
   access). Don't wait for answers — work on ASSUMP.

Task:
<what to do — in your own words, with known facts and links>

Constraints:
- Working folder: <name>
- Production: do not release | "release it" — allowed this cycle
- Final acceptance: critic board across product-failure lenses
- Facts and resources absent from the input are not to be invented: ASSUMP with
  a marker, resource registry, human action queue
- At the end: demo script and handoff (board verdicts, returns, journal);
  retro — only on canon triggers
```

Notes (not copied into the assignment):

- For analyzing someone else's repository, phrase the task as questions ("what is this system, where are the risks, what to fix first") — the orchestrator will route through onboarding → architecture-review + quality/security; "solution mode" works here too: the result is a report with evidence, not edits to someone else's code without an assignment.
- "Release it" in the task = permission for production this cycle. No such word — production is hard-closed.
- The more facts in the input (links, data, accounts into the registry), the fewer ASSUMP entries and reworks.
