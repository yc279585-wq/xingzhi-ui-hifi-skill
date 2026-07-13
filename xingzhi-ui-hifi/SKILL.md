---
name: xingzhi-ui-hifi
description: Generate Xingzhi PC/Web high-fidelity UI screens from PRDs, low-fidelity screenshots, wireframes, rough page sketches, or feature descriptions. Use when the user asks to turn Xingzhi desktop web product requirements, PRD screenshots, low-fi UI images, database pages, chart/table pages, dashboards, or institutional web pages into polished high-fidelity PC/Web pages that follow the bundled domestic component specification and Xingzhi/HTSC web page templates.
---

# Xingzhi UI Hifi

## Purpose

Transform Xingzhi PC/Web product PRDs, low-fidelity screenshots, wireframes, and rough page drafts into high-fidelity desktop web UI screens that match the bundled domestic component specification and Xingzhi/HTSC web page templates.

## Required Reference Loading

Before designing or generating a Xingzhi high-fidelity page, read:

- `references/design-rules.md` for confirmed PC/Web brand tokens, layout rules, and UI construction guidance.
- `references/component-index.md` to map the user's target screen to relevant spec pages and sample images.
- `references/output-checklist.md` before final delivery or visual QA.
- `references/web-page-templates.md` for the HTSC-style global navigation, 1920 px page frame, 1200 px content container, side navigation rules, and level-1/level-2/level-3 page templates.

Use the source assets in `assets/` as visual ground truth:

- `assets/domestic-component-spec.pdf`
- `assets/pdf-samples/domestic-contact-sheet.png`
- `assets/pdf-samples/domestic-*.png` for PC/Web component visual samples.
- `assets/logos/htsc-xingzhi-logo-white-combined.webp` for the HTSC + Xingzhi combined white top-nav logo.
- `assets/logos/htsc-logo-white.webp` and `assets/logos/xingzhi-logo-seal.webp` when the Huatai Securities wordmark and Xingzhi seal need separate placement.

Use extracted text only as a search aid:

- `references/extracted/domestic-text.md`
- `references/extracted/domestic-headings.tsv`

If a newer or more complete Xingzhi spec is provided in the user request, prioritize that file, extract its visual rules, and update the design interpretation for the current task.

## Workflow

1. Parse the input.
   - Identify the target PC/Web screen size, page purpose, user role, primary action, and required content.
   - If the input is an image, inspect visual hierarchy, rough component positions, labels, and implied user flow.
   - If the input is a PRD, convert requirements into page sections, states, controls, and data examples.
   - Classify the page as a level-1, level-2, or level-3 PC/Web page using `references/web-page-templates.md` before designing.

2. Map low fidelity to high fidelity.
   - Preserve the product intent and information architecture.
   - Replace rough boxes with production-grade PC/Web components.
   - Add realistic but restrained data only where the PRD or wireframe leaves placeholders.
   - Do not add marketing sections unless the screen is explicitly a promotional or onboarding screen.
   - Do not add new content modules beyond the low-fidelity screenshot or PRD unless the user explicitly asks for them.
   - Keep the provided low-fidelity page content inside the correct content region; move its navigation into the shared top navigation or side navigation template instead of duplicating it inside the content area.

3. Apply Xingzhi visual language.
   - Use the confirmed Xingzhi cyan-blue as the primary action and selected-state color.
   - Use white cards/components on pale gray PC/Web backgrounds.
   - Use orange/gold only for warning, tag, highlight, or chart-support moments.
   - Keep typography, spacing, and component density suitable for a practical financial/institutional PC/Web product.
   - For HTSC/Xingzhi desktop web top navigation, use the bundled logo image assets from `assets/logos/`; do not redraw the Huatai Securities or Xingzhi logos with text boxes, geometric shapes, or approximate typography.

4. Produce the high-fidelity artifact.
   - For PC/Web implementation requests, build the actual usable screen, not a static description.
   - For image/mockup requests, generate a polished bitmap or Figma-ready visual specification.
   - If generating code, use the existing project stack and design system when present.
   - For PC/Web prototypes with no existing project, use a 1920 px page canvas and place the primary content in a centered 1200 px container unless the user specifies another width.
   - When the user needs to share the result outside the local machine, produce a standalone HTML artifact with required CSS, JS, fonts, images, and chart rendering embedded or otherwise reachable from the published URL.

5. Verify before final response.
   - Run or render the result when possible.
   - Check against `references/output-checklist.md`.
   - State any spec gaps clearly, especially when a design decision is inferred because the provided PDFs do not include detailed component tables.

## Output Expectations

Deliver a high-fidelity PC/Web page with clear hierarchy, realistic content, accessible contrast, polished spacing, and Xingzhi brand consistency. The result should feel like a production institutional web product screen, not a poster, landing page, or generic template.
