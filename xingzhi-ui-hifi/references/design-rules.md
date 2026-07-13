# Xingzhi PC/Web Design Rules

## Source Assets

These rules are derived from the bundled full PDFs:

- `assets/domestic-component-spec.pdf`: domestic/web component system.

Use these rules for PC/Web high-fidelity screens only. Do not apply phone-screen navigation, safe-area, touch-specific, or narrow-device layout rules.

## Core Visual Language

- Primary Xingzhi color: `#00A6FA`. Use for primary buttons, active tabs, selected states, links, progress, and major interactive highlights.
- Supporting cyan: `#00D2F0`. Use sparingly for gradients, secondary emphasis, charts, or operational accents.
- Supporting gold/orange: `#D9AF6C`, `#FEAF40`, and domestic warning yellow `#F6A316`. Use for warning, hot tags, highlights, chart accents, or status badges, not as the default primary CTA.
- Page surfaces are pale gray (`#F5F7FA` / `#F7F9FA`) with white cards and component blocks.
- The design is compact, financial/institutional, and utility-driven. Avoid marketing-style hero layouts for normal PC/Web product screens.

## Color Tokens

Use these tokens unless a newer spec or existing codebase overrides them:

- `brand.primary`: `#00A6FA`
- `brand.primarySoft`: `#EAF8FF`
- `brand.primaryCyan`: `#00D2F0`
- `brand.gold`: `#D9AF6C`
- `brand.orange`: `#FEAF40`
- `state.error`: `#F24949`
- `state.warning`: `#F2BA49`
- `state.success`: `#3B990F`
- `border.default`: `#E6EBF0`
- `surface.page`: `#F5F7FA`
- `surface.card`: `#FFFFFF`
- `text.primary`: `#222222`
- `text.secondary`: `#555555`
- `text.tertiary`: `#999999`
- `text.disabled`: `#BBBBBB`
- `neutral.light`: `#DDDDDD`

Domestic/web secondary palette, when needed:

- Deep blue `#0D59C4`, light blue `#00C9E5`, dark nav `#0E172D`.
- Chart colors: `#D86C39`, `#4E9A9B`, `#377A58`, `#BB318F`, `#D1A63C`, `#67A138`, `#BB0000`, `#478FC1`, `#A374E9`.

## Typography

Use the system Chinese UI font stack unless the project already defines a font:

```css
font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif;
```

PC/Web type scale:

- 12/16, 14/18, 16/22, 18/24, 24/32, 32/38, 36/44, 40/48.
- Keep data, table, chart, and form text mostly in the 12/16, 14/18, 16/22, and 18/24 range.
- Use 24px and above only for page-level titles or overview screens that truly need display hierarchy.

Keep letter spacing at `0`. Do not use oversized hero typography inside normal PC/Web product screens.

## Layout And Spacing

- Design primarily for a 1920px desktop canvas unless the user specifies another PC/Web target.
- Use light gray page backgrounds with white cards or list blocks.
- Use 16px to 24px card/content padding for normal PC/Web product pages; use denser spacing only for data tables, chart dashboards, or tool panels.
- Use the spec spacing rhythm: 4 px for tight title-to-meta gaps, then 8, 12, 16, 24, 32 for larger relationships.
- Radius: tags use small radii around 3px to 4px; cards and buttons generally use 6px to 8px unless matching an existing PC/Web component.
- Keep dense product pages scannable: title, metadata, value/status, action. Do not stack decorative cards inside cards.
- Use shadows only to separate floating layers. Domestic shadow reference: `#9198A7` at 25% opacity, x 0, y 0, blur 30.

## Component Guidance

Use these component patterns when converting low fidelity to high fidelity:

- Navigation: use the HTSC-style full-width dark global top navigation for institutional web pages. Use left side navigation for level-2 modules and tabs/segmented controls for level-3 views.
- Primary button: blue fill, white text. Bottom primary actions are common for task workflows.
- Secondary button: white surface with blue border/text.
- Text button: pure text, optionally paired with an icon, for lower-emphasis actions.
- Button combinations: use primary + secondary. Do not use primary + primary or secondary + secondary pairs for main decision buttons.
- Cards: white surface, compact padding, clear title/value hierarchy, no nested cards.
- Lists and information flows: dense readable rows with title, source/type, time, optional tag, and trailing action/status.
- Tabs/segmented controls: blue active state, neutral inactive state, clear underline or pill background depending on the sample page.
- Tags/chips: small radius, blue for selected/brand, orange/gold for warning/hot/highlight, gray for neutral metadata.
- Forms: support horizontal and vertical layouts; include label, placeholder/value, validation/error, and optional trailing button/switch when the PRD implies it.
- Empty states: concise Chinese copy, optional illustration, and a single blue primary action when recovery is possible.
- Modal/dialog/popup: use compact PC/Web modal or dropdown patterns. Avoid narrow-device bottom-sheet behavior unless the user explicitly asks for a responsive adaptation.
- Data/status screens: prioritize scanability, status color, and next action over decoration.

## Content Tone

- Use concise Chinese product copy.
- Prefer task-oriented labels: "提交", "确认", "查看详情", "立即处理", "保存".
- Avoid explanatory paragraphs inside the UI unless the PRD requires guidance text.
- Use realistic sample data, but keep it obviously replaceable when source data is missing.

## Spec Handling

When exact component values are needed, consult `references/component-index.md`, then open the relevant domestic/web sample PNG or PDF page.
