# Xingzhi / HTSC Web Page Templates

Use this reference for desktop/web product pages, especially pages based on `https://inst.htsc.com/incos/` or screenshots with the HTSC institutional website top navigation.

## Core Web Frame

- Page canvas: design and render desktop web pages at `1920px` wide by default.
- Main content width: constrain the primary content to a centered `1200px` container.
- Global navigation: every web page starts with the same full-width dark top navigation before the page-specific content.
- Page background: use the Xingzhi/HTSC light website style by default: `#F5F7FA` page background with white content cards.
- Treat low-fidelity colors as draft styling, not a binding theme. Preserve the source information architecture and content, but apply Xingzhi/HTSC website styling unless the user explicitly asks to keep the source visual theme.
- Do not add business modules that are not present in the low-fidelity screenshot or PRD. Improve fidelity, hierarchy, spacing, and component styling while preserving the original information architecture.
- Do not use the supplied low-fidelity screenshot as a background image with decorations placed on top. Rebuild the interface as real layout, text, tables, icons, and charts.
- Keep page-specific content widths stable across directory switches. For a 1200px container with a 200px side nav and 24px gutter, the right content region is `976px`; make landing grids, charts, tables, and detail views fill that region so switching pages does not cause horizontal jumps.

## Global Top Navigation

Match the HTSC institutional navigation pattern from the product site:

- Height: match the current HTSC official site header, about `60px` on a 1920px desktop canvas.
- Full width: spans the entire `1920px` page canvas.
- Inner content: centered `1200px`.
- Background: deep navy `#0E172D`.
- Bottom active indicator: cyan/blue bar, `3px` high, under the active primary nav item.
- Left brand zone: HTSC logo/wordmark area, fixed visual weight, separated from nav by subtle divider when space allows.
- Primary nav labels: `首页`, `研究服务`, `投资服务`, `交易服务`, `托管外包`, `运营工作台`, `企业服务`, `期货专区`.
- Right utility zone: search icon, site selector such as `中国站`, and login/account entry such as `去登录`.
- Active primary item: use white text and cyan underline; inactive items use light gray-blue text.
- Do not place page-specific charts, filters, or low-fidelity navigation inside the global top bar.
- The global navigation is full-width and is not constrained to the page's 1200px content card. Only its inner nav content is centered/aligned according to the HTSC site pattern.
- Use sharp official or high-resolution logo assets when available. If a logo must be embedded in a standalone file, use a high-resolution data URI or vector recreation; avoid scaling up blurred screenshots.

## Navigation Hierarchy

Use three levels consistently:

- Level 1 navigation: the global top navigation. It identifies the major product area.
- Level 2 navigation: a left side navigation for the current product section. Use this when the low-fidelity screenshot has many sibling pages or database/report categories.
- Level 3 navigation: tabs, segmented controls, or compact submenus inside the page content. Use this for views within a selected level-2 item, such as `日K / 周K / 月K`, chart/data/table modes, or filters.

## Level-1 Page Template

Use for product-area landing pages or overview pages reached from the top navigation.

- Structure: global top navigation, then a centered `1200px` content container.
- Content: page title/header, optional short summary, and the low-fidelity modules exactly as provided.
- Navigation: no side navigation unless the page needs persistent section switching.
- Visual treatment: restrained enterprise page; avoid marketing hero treatment unless the source is clearly a public marketing page.

## Level-2 Page Template

Use for functional modules inside a product area, such as databases, reports, workbenches, lists, dashboards, and management pages.

- Structure: global top navigation, then a centered `1200px` two-column layout.
- Side navigation: left vertical navigation inside the 1200px container.
- Recommended side nav width: `180px` to `220px`.
- Content region: remaining width after side nav and gutter.
- Gutter: `24px` between side nav and content.
- Active side nav item: blue/cyan indicator or soft blue background; inactive items are neutral.
- The low-fidelity page's own navigation should usually become this side navigation. Do not keep it as a second top nav inside the content unless it is truly a level-3 control.
- The side nav and right content should stay mounted and dimensionally stable across views. Do not let the homepage card grid shrink narrower than later chart/table pages.
- Overview cards should use consistent line-style or product-system icons. Do not mix emoji, low-fidelity screenshot fragments, and line icons in the same card set.

## Level-3 Page Template

Use for detail, data, chart, form, and analysis pages inside a selected level-2 module.

- Structure: global top navigation, centered `1200px` container, optional left side navigation, then the page body.
- Page body starts with a compact title row: title, unit/source metadata, and optional right-side controls only when present in the source or PRD.
- View switching uses level-3 tabs or segmented controls inside the content area.
- Dense data views should use cards, tables, charts, or forms according to the source information architecture.
- For chart pages, keep the chart in the content area and preserve the provided legends, axes, units, and date ranges. Do not add KPI cards, event feeds, or summaries unless present in the source or requested.
- Keep the first content/title baseline consistent across all sibling pages. A user switching directories should not see the first row jump up or down unless the source requires a distinct filter/header.
- Section titles should be clean text rows, not heavy colored backplates, unless the original product component explicitly uses a section bar.

## Web Layout Defaults

- Top nav height: `60px` for HTSC official-site-style desktop pages.
- Container width: `1200px`.
- Page top spacing after nav: `24px` to `32px`.
- Side nav width: `200px` default.
- Side/content gutter: `24px`.
- Card radius: `6px` to `8px`.
- Card border: `#E6EBF0` on light pages; subtle blue border on dark analytical pages.
- Font stack: `-apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif`.
- Web text sizes: 12/16, 14/18, 16/22, 18/24. Keep chart labels at 11-12px.

## Chart/Data Page Rules

- Preserve the source chart as the primary object; do not crowd it with unrelated panels.
- If the low-fidelity page is a chart-only page, keep the high-fidelity page chart-first.
- Keep legends near the chart, usually above the plot area.
- Keep units/source metadata next to the page title.
- If a source screenshot uses dark analytical styling, do not inherit the dark theme by default. Convert the chart into the light Xingzhi/HTSC website style unless the user explicitly asks to keep a dark analytical page.
- Render and screenshot the final page when possible; check that the 1200px content area is visually centered inside the 1920px canvas.
- Recreate charts as crisp rendered graphics instead of pasting raster screenshots. Prefer SVG or high-DPI canvas (`devicePixelRatio` aware) with real text, axes, legends, and lines.
- K-line/candlestick pages are especially sensitive to blur: draw candles, wicks, moving averages, grid lines, labels, and legends natively, and verify at 1920px that small text remains readable.
- For dense multi-chart analytical pages, keep chart card dimensions, title positions, legends, axis label size, and gutters consistent across cards. The visual priority is clean comparative scanning, not decorative effects.
- For dense financial tables, rebuild the table with HTML/CSS text and grid lines. Preserve grouped headers, units, year columns, highlight rows, and numeric alignment; avoid using the screenshot image as table content.
- Use chart colors purposefully: blue/cyan for primary Xingzhi anchors, orange/gold for current-year or highlighted series, red/green only where financial meaning or source emphasis requires it, and muted blue-gray for historical comparison series.

## Standalone Sharing Rules

Use these when the user asks for a file or URL that others can open reliably:

- A `file://` URL only works on the creator's machine. For sharing, create either a hosted page or a standalone HTML file that can be uploaded anywhere.
- For a single-file deliverable, inline CSS and JS, embed small images/logos as data URIs, and avoid local paths such as `/Users/...`, `file://`, relative asset folders, or machine-specific references.
- If the prototype uses charts, include the chart drawing code in the same HTML or use a CDN only when internet access is acceptable for the audience.
- Before delivery, search the standalone file for local references and open it directly in a browser to verify navigation, chart rendering, and logo sharpness.
