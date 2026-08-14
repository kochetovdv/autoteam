# Orchestration and autonomy

The human opens **one** chat with an assignment. The orchestrator (`autoteam-orchestrator`) invokes subagents itself. No new chat per role. Any execution environment with subagents works — the method is not tied to an environment.

## Assignment

| Meaning of the first message | Cycle without waiting for "go ahead" |
|-------------------------|---------------------------|
| build / fix / investigate | brief → roles → acceptance → artifact |
| build and release | same + `autoteam-release` after acceptance |
| turn an idea into a working solution | "solution mode": full cycle non-stop, decision journal, critic board at the finish |
| an idea, no spec | `autoteam-product` → `autoteam-positioning`, not code |
| estimate the scope | `autoteam-scope` |
| how to promote / why aren't we growing | `autoteam-growth` + `autoteam-analytics` + `autoteam-content` |
| how to charge money | `autoteam-pricing` |
| how much are we spending / limits | `autoteam-budget` |
| learn the repository | `autoteam-onboarding` |

The brief is always written. Unknown repository — `autoteam-onboarding` right away. Stack: `docs/process/stack.md`.

## Two modes

**Interactive** (human in the loop): meaning-level forks (two readings of money, rights, a contract, security, no stack) — a question to the human, stop only dependent tasks.

**"Solution mode"** (autonomous, activated by an assignment like "build a solution / work autonomously"): questions turn into decisions recorded in the journal (the product's `docs/process/decisions.md`, canon template `templates/decisions.md`). **Ask and continue:** at the start of the cycle the human gets a digest — up to 3 questions where an early answer is cheapest, plus a queue of actions only the human can perform (accounts, payments, identification — from the resource registry `templates/resources.md`, each with the consequence "without X, package Y stalls after checkpoint Z"); work proceeds on ASSUMP without waiting; an answer or action at any moment = an amendment to the journal. ASSUMPs that change the market, the audience, or money are duplicated into the journal. A missing resource is not a cycle stop: `Blocked-by-resource` for that package, the rest keeps moving. Only hard stops halt work: external money; law and public commitments; irreversible destruction; production without "release it". The result is a working solution as a whole: it launches, is verified with evidence, is deployed in an available environment (if an external environment is forbidden — a local run reproducible from instructions; the interpretation goes into the journal), is documented; anything deferred — an explicit short list.

## Non-blocking approvals

Request the decision and **continue independent** tasks. Stop only work for which that decision is an input.

Stop dependents (interactive): two readings of money/law/security/contract; new product behavior; a new architecture boundary; release without an assignment; the irreversible (wipe, mass recomputation without confirmation); no stack when code cannot be written without one.

Not a stop: documentation of another module, another screen, tests, estimating another boundary, refactoring outside the boundary, a draft not headed to prod.

`Blocked`: blocker owner, next action, check date.

## How to launch subagents

1. One role, one deliverable. Adjacent roles in a chain may be merged into one subagent at L1–L2 (artifacts are sequential); at L3 (data, race conditions, security, money) — do not merge. Author ≠ acceptor, always.
2. Model per the **project's** `docs/process/model-routing.md` if the file exists; otherwise canon principles.
3. In the prompt: read the specified skill (+ reference if needed), the context package, the return format. Not the chat history.
4. Acceptance — see "Critic board". Different model families if the environment provides them; one family — a `same-family` note in the handoff.
5. `CHANGES_REQUIRED` → back to the implementer, at most **2** cycles, then the human (in "solution mode" — record in the journal and simplify the solution, don't hang).
6. Release — a third subagent, neither the code's author nor its acceptor.

Context package: role; spec/plan/task revisions; affected contracts and entry points; in/out; prohibitions; verification commands; return format; perimeter boundaries — what was left out and why (a conclusion of absence beyond the perimeter is a question to the orchestrator, not a finding).

Parallelism — only without a shared mutable boundary. **An unpinned shared numeric budget or NFR is also a shared boundary:** before a parallel launch the orchestrator writes out the shared numbers explicitly or appoints one branch as the number's owner. Many roles — in waves: independent ones in parallel, dependent ones in the next wave; while one stream waits for assembly, other waves keep working.

Resilience: end of a wave = checkpoint (a git commit in the product if git exists; otherwise a progress record) — an interrupted cycle recovers from the journal and checkpoints; at each checkpoint, open perimeter narrowings are re-checked (`templates/resources.md`). The active cycle marker `docs/process/.cycle-lock` (id, start time) guards against a double launch in one folder; a live foreign marker — a question to the human; a marker older than a day is stale. An amendment that changes an ASSUMP spawns a task to revise dependent artifacts.

## Critic board

Composition is not fixed: **lenses = ways the product can fail** — the board is assembled from the question "how can this product die"; composition and rationale go into the journal. Core: commercial, engineering, art (for UI; screenshots of both versions), user (an impatient user walking the demo scenario). By product nature: facts (claims → fact/ASSUMP/source), operations ("what breaks in a month"), DX instead of art for API/CLI, security/quality by risk.

Mechanics: each critic is a separate subagent with fresh context and a mandate to "look for reasons to reject"; critics don't see each other's verdicts until they submit their own; any `CHANGES_REQUIRED` sends the work back (up to 2 cycles); the implementer may contest a finding with evidence — the orchestrator arbitrates, the dispute goes into the journal; a conflict of lenses — tie-break by positioning (the lens closer to what the ICP pays for is senior); acceptance budget ≤5 critics by default, cut lenses go into the journal; the critic's model ≥ the implementer's model. Returns are the norm and are recorded in the handoff; a systematic zero returns is a retro trigger. Intermediate tasks — one specialized critic.

The acceptance checklist includes: the decision journal does not contradict the final artifacts (amendments in place); the artifact's recommendations do not contradict its own findings — a recommendation's object is not marked defective in another section, otherwise an explicit "fix X first" dependency; every conclusion of absence carries its search area, and conclusions resting on an open perimeter narrowing are marked incomplete.

## Gates (human)

Apply in interactive mode; in "solution mode" gates 1–3 are replaced by the critic board plus the decision journal.

1. Requirements approved — if behavior changes.
2. Architecture approved — if there's a new boundary, storage, protocol.
3. Merge / PR acceptance — if the project has PRs and the human asked for it.
4. Release to production — always the human, unless there's an explicit "release it" in the assignment for **this** cycle. Hard stop in both modes.

Release to staging (pre-prod) ≠ declaring production.

## Cadences

Architecture review: `docs/architecture/review.md` and `autoteam-architecture-review`. Method retro: by triggers (`autoteam-retro`), not after every run.
