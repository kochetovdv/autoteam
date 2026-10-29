# autoteam 1.6 — Agent development canon

A portable method library for coordinating an agent team: understand the user's outcome, plan, implement, independently check, and retain verified project knowledge. The method applies to products, investigations, experiments, and documents. It does not include a running scheduler or connections to external providers.

English is canonical. [Русская версия](ru/README.md) is maintained with the same changes. The library contains **25 skills in each language**. Read the [v1.6.0 release notes](docs/releases/v1.6.0.md) for changes and upgrade instructions, or the [changelog](CHANGELOG.md) for the revision history.

## Start here

- A situation and its roles: [catalog](skills/autoteam-catalog/SKILL.md).
- One assignment through the team: [orchestration](docs/process/orchestration.md).
- Detailed authorities: [process map](docs/process/README.md).
- Reusable artifact shapes: [templates](templates/README.md).

## What's new in 1.6

- **Outcome checks and bounded critique.** Independently check critical meaning against primary sources. Two correction returns without outcome progress trigger reassessment; changing models does not reset the history. Open-ended critique defaults to one broad pass and one targeted recheck. [Assurance](docs/process/assurance.md).
- **Traceable work and review.** Keep one task record, pinned inputs, every contributing author, immutable verdicts, and current/stale applicability. Cancellation and replacement are explicit non-delivery outcomes. [Work items](docs/process/work-items.md).
- **Reusable project knowledge.** Separate project settings, verified memory, specifications, decisions, sources, and cycle state. Recheck present applicability against current facts and observation dates. [Project knowledge](docs/process/project-knowledge.md).
- **Audits and monitoring.** Review applicable risk areas and generate observation settings from context. Detect cumulative drift, retain unknown delivery, and verify actual scheduling before promising recurrence. [Audit skill](skills/autoteam-audit/SKILL.md) and [monitor skill](skills/autoteam-monitor/SKILL.md).
- **Team, limits, and resources.** Delegate useful work automatically, account for optional limits across all agents, preserve evidence, and clean up only owned resources. [Model routing](docs/process/model-routing.md) and [resource lifecycle](docs/process/resource-lifecycle.md).

## Quick start

1. Download the complete repository or clone it:

   ```text
   git clone https://github.com/kochetovdv/autoteam.git
   cd autoteam
   python scripts/check_canon.py
   ```

   The checker uses Python 3 and its standard library. A successful check prints `"ok": true` and the bundle fingerprint.

2. Select English or Russian, keep a verified snapshot for the cycle, and give the agent its absolute path. Use [kickoff](templates/kickoff.md) for the assignment and [project profile](templates/project-profile.md) for known project settings; the agent fills these from context rather than asking you to complete every field.
3. Point the agent at [the orchestrator](skills/autoteam-orchestrator/SKILL.md) for an assigned task, or [the catalog](skills/autoteam-catalog/SKILL.md) when choosing a role. Register skills using the facilities of your agent environment and keep their shared references bound to the same snapshot.

No provider-specific installer or integration is bundled. A single copied skill directory is not a full installation. See [installation and version pinning](#installation-and-version-pinning) before updating an existing project.

## Method, project, and cycle

The canon owns how work is organized. The project profile owns domain vocabulary, stack, commands, available models/integrations, authority, limits, and visual references. Verified memory preserves reusable facts and lessons with evidence. Specifications define desired behavior; decisions preserve the reasons; state summarizes the current cycle. [Knowledge rules](docs/process/project-knowledge.md) prevent these from replacing each other.

The orchestrator launches the useful agents and independent checks without repeated requests for their number. A user may set a whole-task limit; otherwise quality and completion take priority over token economy. [Model routing](docs/process/model-routing.md) covers actual dispatch, shared accounting, and preservation/acceptance reserves.

Critical meaning is independently checked against primary sources and observations. [Assurance](docs/process/assurance.md) bounds open-ended critique and interrupts patch loops that make no progress toward the original outcome. Changing models does not reset the history. Cancelled/replaced work stays distinct from accepted delivery; recovery and monitoring guarantees require verified environment capabilities.

Explain consequences for the user and product before implementation details. Product milestones distinguish a payment-ready system, observed revenue, and validated economics.

## Installation and version pinning

The full bundle is `canon.json`, this entry documentation, `skills/`, `docs/`, `templates/`, their maintained `ru/` counterparts, and `scripts/check_canon.py`. Keep a complete immutable snapshot and record its version, content fingerprint, path, and selected language in the project profile/brief. Expose skills from that snapshot where the environment supports it; bind discovery copies and shared references to it otherwise.

Required shared documents are dependencies. A copied skill folder alone gives focused guidance, not the complete process. Check a candidate bundle before exposing it; do not overwrite global user skills or update a shared checkout incidentally. An active cycle continues reading its snapshot even when another project updates the source. [Packaging details](skills/README.md).

```text
python scripts/check_canon.py
python scripts/check_canon.py --compare <full-bundle-root>
```

The checker reports structure, locale coverage, links, and content differences. It is read-only and does not install the method, prove translations equivalent, or establish agent behavior. Environment adapters must actually launch and verify models, scheduled observations, tracker transitions, and recovery.

## Validation

Run the checker and its regression suite from the repository root:

```text
python -X utf8 scripts/check_canon.py
python -X utf8 -m unittest discover -s tests -v
```

GitHub Actions runs both commands on Linux and Windows. Structural checks and instruction-level scenario reviews do not prove runtime recovery, delivery guarantees, agent compliance, or improved business results. See the [release validation scope](docs/releases/v1.6.0.md#validation).

## Boundaries

A review does not mutate its subject. Writing agents use isolated owned workspaces. External spending, commitments, destruction, and production follow the granted authority. Audits disclose incomplete coverage; monitors distinguish missing data from no change and generate their internal settings from context.

The library is maintained in `skills/`, `docs/`, and `templates/`; product-specific commands and findings stay in the product. [Deliberate gaps](docs/process/gaps.md).
