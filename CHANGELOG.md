# Canon revisions

## 1.6.0 — 2026-10-29

This revision extends the agent-development method. [Release notes and upgrade instructions](docs/releases/v1.6.0.md). It changes the canon, not a deployed product or a global skill installation.

- One work-item authority with pinned input/output versions, author/reviewer runs, review scope, immutable review history, and justified re-review/carry-forward.
- Automatic useful team scaling and evidence-based convergence; optional shared whole-task limits, including review, preservation, and cleanup.
- Business-readable consequences and evidence-based process/tool initiatives.
- Separation of profile, verified memory, specification, decisions, source derivations, and cycle state; immutable canon snapshots and explicit continuation.
- Regular risk-based audits and the shared critical claim/counterexample/probe protocol, including the checks themselves.
- Monitoring that generates its settings from context or an explicit instruction, with meaningful notifications, source freshness, and verified runtime scheduling.
- Owned resources, liveness-based lock recovery, checkpoint preservation, and cleanup after completion and failure.
- Visual direction through distinct working samples and observed interaction; no universal palette, named reference, or fashionable year.
- Stronger links between requirements, design, work, checks, and evidence, with proportionate paths and investigation before substantial changes.
- Corrected channel ROI direction/zero cases, mode-aware stack selection, isolated QA data mutation, and release workspace protection without automatic untracked stash.
- Honest full-bundle dependencies, version metadata, read-only consistency/fingerprint checks, and incomplete-copy detection.
- Independent checks of critical meaning against primary sources, with the original outcome and measured progress preserved across model handoffs.
- Bounded other-angle critique: default broad pass plus targeted recheck; two correction returns without outcome progress trigger a bounded reassessment, not another blind patch or automatic acceptance.
- Explicit cancelled/superseded non-delivery outcomes; durable handoffs, assignment generations and independently triggered recovery, or a disclosed manual-resume limit.
- Monitoring compares cumulative change with a reviewed reference state and preserves unknown notification delivery instead of assuming success or blindly retrying.
- Memory distinguishes observation/verification/recording dates and checks present applicability against current facts before consequential reuse.
- English/Russian release notes, a README quick start, and GitHub Actions checks for the complete bundle and checker regression tests on Linux and Windows. Local review transcripts and machine-specific evidence stay outside the public repository.

### Scope boundaries

The library defines process and adapter contracts. It does not supply a scheduler, provider bridge, tracker service, production monitor, or proof of customer demand. Those capabilities must be implemented and verified in a product environment.

Runtime verification that the deployed artifact is the intended release revision is deferred; this edition does not change the existing post-deploy smoke procedure for that purpose. No specific vendor, stack, site's design, or universal monitoring cadence becomes a canon dependency.

### Migration from 1.5

Keep product records and identifiers; do not create duplicate task registries. Add missing provenance and source links as work is touched. Initialize profile/memory only from known settings and checked evidence. Keep historical review verdicts, marking current applicability separately. Pin a complete verified bundle for the next cycle; do not replace instructions mid-cycle or overwrite a dirty/shared checkout. Existing global copies require a separate explicit installation/update operation.

Validate the bundle with `python scripts/check_canon.py`; compare a full copy with `--compare <bundle-root>`. Structural checks are not behavioral validation. Use independent scenario checks for consequential process changes.
