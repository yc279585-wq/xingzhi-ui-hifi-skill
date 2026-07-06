# Xingzhi High-Fidelity Output Checklist

Before final delivery, verify:

- The screen preserves the PRD or low-fidelity information architecture.
- Primary action, secondary actions, and navigation are obvious.
- APP blue `#00A6FA` is used as the primary action/selected-state anchor.
- Orange/gold is reserved for warning, highlight, hot tag, or chart-support usage.
- Text hierarchy is clear: page title, section title, body, metadata.
- Components are mobile-appropriate with stable heights, margins, and touch targets.
- For desktop/web pages, the page uses a 1920 px canvas by default and keeps primary content inside a centered 1200 px container.
- For desktop/web pages, the unified HTSC-style top navigation appears before page-specific content.
- For desktop/web pages, the global navigation is full-width while page content is constrained to the intended 1200 px container.
- For desktop/web level-2 or level-3 pages, low-fidelity navigation is mapped to side navigation or inner tabs according to `web-page-templates.md`.
- For desktop/web level-2 pages with side navigation, the right content region keeps a fixed width across sibling pages, typically 976 px when using a 200 px side nav and 24 px gutter.
- For desktop/web chart pages, do not add KPI cards, side summaries, feeds, or other business modules unless they are present in the source or requested.
- For desktop/web chart and table pages, source screenshots have been redrawn as real HTML/SVG/canvas text and graphics rather than pasted as blurred raster content.
- K-line/candlestick charts are crisp at desktop size, with readable axis labels, legends, candles, wicks, and moving averages.
- Page title/top content starts at a consistent height across sibling directory views.
- Overview card icons use one consistent visual system and do not mix emoji, screenshot fragments, and line icons.
- If the user requested a shareable result, the delivered HTML has no local `file://`, `/Users/...`, or unbundled asset references.
- Cards are not nested inside cards.
- Buttons, chips, tabs, and active states use consistent blue treatment unless the component is explicitly a warning/highlight.
- Empty, loading, disabled, and error states are included when naturally implied by the workflow.
- Chinese UI copy is concise and realistic.
- Text does not overflow or overlap at mobile viewport sizes.
- Contrast is readable on blue, white, gray, and pale surfaces.
- The component choice was checked against `references/component-index.md`.
- The final artifact has been rendered, screenshotted, or visually inspected when tooling allows.
- Any decisions inferred beyond the PDF samples are mentioned briefly in the final response.
