---
name: autoteam-ui
description: First-class interfaces — landing pages, SaaS, B2B, admin panels; design tokens, typography, motion, WebGL where it belongs. Use for UI, UX, a landing page, a mockup, a redesign.
---

# Interfaces

The bar is the industry's best products, not "no worse than a generator". The UI stack comes from the product / ADR; no stack — a question for the human.

**Input.** Screen/flow, product character, references if any, UI stack. **Output.** A working interface: tokens, states, motion. **Forbidden.** AI defaults (`docs/design/anti-slop.md`); copying someone else's brand; heavy effects that block content; animation for animation's sake. **Evidence.** All screen states (empty/loading/error/success); a11y minimum; speed does not degrade. **Stop.** No UI stack — ask. No reference — don't wait: direction from character, code right away, alternative in text. **Next.** Delivery → `autoteam-delivery`. Public page → `autoteam-growth`. Stack-specific UI craft — product overlay.

## The bar by genre

Landing page: one offer; composition, typography, and speed sell on their own. **Flagship tech-company site / showcase**: the bar is today's best industry sites, not "a tidy brochure"; scroll choreography, an expressive hero, meaningful motion are the price of entry to the genre, not an option; WebGL/canvas — where it raises the level. Stack asceticism is no excuse: pick the stack as "the minimum that delivers the genre bar"; weight budget and build come from the genre. SaaS product: flow clarity, empty states lead to value, density per task. B2B/admin panel: density, tables as a tool, filters in the URL, bulk operations. Internal tool: operator speed over marketing.

Mobile checklist (mandatory for public UI): navigation collapses meaningfully (hamburger/drawer on overflow), touch targets ≥44px, the first screen sells without scrolling, no horizontal scroll; at acceptance — a mobile screenshot through the art lens, not just a formal width check.

## Craft

1. Character: 3–5 words, industry over fashion. From positioning, if it exists.
2. References are a habit, not a one-off step: before every significant screen, look at how the best in class solve this task today. Copy the level (grid, type, density, rhythm), not the brand.
3. Tokens: color, type scale, spacing, radii, shadows — a system, not ad hoc. A UI kit is fine, but on top of the project's tokens.
4. Typography: scale, rhythm, size contrast — half of the "expensive" look. A typeface with character, not the first system font.
5. States: empty / loading / error / success / partial — designed, not "later".
6. Motion: micro-interactions with a purpose (feedback, connection, entrance). 150–300ms, easing, `prefers-reduced-motion`. An expensive impression comes from appropriateness, not quantity.
7. Special effects (WebGL, canvas, 3D, shaders) — where they raise the genre bar (flagship landing, data viz). Always: fallback, performance budget, content doesn't wait for the effect.
8. Build → check: is it recognizable as "made by a generator"? Change type **and** grid, not just color.

a11y minimum: visible focus, `type=button`, contrast, not color alone, keyboard on the critical path.

## Clients

Web / responsive / PWA / native — a project decision, explicit and with its cost. Don't silently add a new platform.
