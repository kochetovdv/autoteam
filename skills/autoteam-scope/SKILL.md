---
name: autoteam-scope
description: Scope and risks before the start — gaps, decomposition, MVP delivery order, Firm/Assumed/Excluded traceability. Use when planning scope, deciding what to build first, checking input completeness.
---

# Scope (method)

The truth about scope before the swarm starts building. Not about hours and not a quote: an agent team doesn't bill time — it is obliged to know what exactly it is building, what the input is missing, and what it is deliberately deferring.

**Input.** Brief, idea, spec, or repository. **Output.** Gaps, decomposition, delivery order (MVP → onward), risks, traceability. **Forbidden.** Silently turning "not estimated" into "not doing"; closing a gap with an invention; assigning a stack that isn't in the input. **Evidence.** Input line → work package; ASSUMPs marked. **Stop.** Only packages with no input (Blocker question). Everything else — ASSUMP and move on. **Next.** Delivery → `autoteam-architecture` / `autoteam-delivery`. Economics → `autoteam-pricing`.

## Order

1. Input once: what is given (Firm), what is inferred (Assumed).
2. Gaps by category — walk through all of them: evidence, acceptance criteria, load, variability, R&D, boundaries of external systems, permissions and personal data (regime per the jurisdiction map), maintenance, resources (accounts, access, infrastructure, data, human actions — `templates/resources.md`).
3. Blocker questions — only where a package cannot be formulated without the answer.
4. Decomposition: stage → module → package; one package — one result.
5. Order: what carries value in the first delivery (MVP), what comes after, what is deliberately absent.
6. R&D — separate packages with a threshold (`autoteam-research`).
7. Traceability: every input item → Firm | Assumed | Excluded | Blocked | Optional.

Template: `templates/scope.md`. Money/hours estimates for an external client are outside the method.
