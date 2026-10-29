---
name: autoteam-ui
description: Design and implement product-specific interfaces with visual direction, working interaction samples, states, and independent visual acceptance. Use for UI/UX, landing pages, and redesigns.
---

# Interfaces

Start from the user scenario, product positioning, profile, and existing design system. The stack follows [the mode-aware rule](../../docs/process/stack.md). Explain design choices through user outcomes. Public reference sites are source material, not authority over the project.

## Direction before scale

For a new product or unresolved major redesign, inspect relevant current references and create a small set of materially different working samples of the key screen/flow. They differ in composition, typography, density, graphic language, and interaction, not just palette. Reuse an approved direction for ordinary screens rather than redesigning every task.

The agent proposes and, within the granted mode, selects a direction with reasons and continues. Reuse the human's known preferences; do not force a repeated style questionnaire. Store references and the chosen direction in the project profile, not in the method. A year, a fashionable effect, a forbidden font list, or a replacement default palette does not define quality. [Visual direction rules](../../docs/design/anti-slop.md).

## Working behavior

Define the essential empty/loading/error/success/partial states. For an expressive public product, demonstrate the intended hero, navigation, scroll behavior, and motion in the sample before multiplying it across the site. Motion should communicate feedback, relationships, or progression. Use appropriate timing, reduced-motion behavior, and a fallback; content and the primary action remain usable without special effects.

A sticky action, transition, canvas, or 3D effect needs a scenario-level reason and an explicit performance/accessibility budget. A business tool may prioritize task density and clarity. Select the visual and interaction level deliberately from the product's purpose; do not assume every genre needs the same effects.

## Acceptance

An independent reviewer examines the actual rendered result against the scenario, chosen references, and declared direction. Require desktop/mobile observations and critical-state evidence where applicable. Motion/scroll claims need a recording or equivalent observed interaction; a static screenshot cannot prove them. Check focus, keyboard use, contrast, touch usability, responsiveness, readable content, and primary actions.

Report what was actually viewed, at which version, and what remains unverified. Source inspection and "the build passed" do not establish visual quality. A failed screenshot or browser tool is missing evidence, not a reason to declare the result visually accepted. Record author/reviewer and applicable version under [work items](../../docs/process/work-items.md).

Delivery → `autoteam-delivery`; public discoverability → `autoteam-growth`. Do not silently add a client platform or replace an existing stack.
