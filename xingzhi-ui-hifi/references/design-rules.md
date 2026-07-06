# Xingzhi Design Rules

## Source Assets

These rules are derived from the bundled full PDFs:

- `assets/xingzhi-app-2025-design-spec.pdf`: APP design system, 320 pages.
- `assets/domestic-component-spec.pdf`: domestic/web component system, 55 pages.

Use APP rules first for mobile high-fidelity screens. Use the domestic component PDF as a secondary source for general enterprise colors, typography, icon discipline, and web-specific components.

## Core Visual Language

- Primary APP color: `#00A6FA` (APP Blue). Use for primary buttons, active tabs, selected states, links, progress, and major interactive highlights.
- Supporting cyan: `#00D2F0`. Use sparingly for gradients, secondary emphasis, charts, or operational accents.
- Supporting gold/orange: `#D9AF6C`, `#FEAF40`, and domestic warning yellow `#F6A316`. Use for warning, hot tags, highlights, chart accents, or status badges, not as the default primary CTA.
- Page surfaces are pale gray (`#F5F7FA` / `#F7F9FA`) with white cards and component blocks.
- The design is compact, financial/institutional, and utility-driven. Avoid marketing-style hero layouts for normal product screens.

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

APP type scale:

- H1 / 特大标题: 20 px, line-height 28 px, weight 500.
- H2 / 一级标题: 16 px, line-height 24 px, weight 500.
- H3 / 二级标题: 14 px, line-height 22 px, weight 500.
- B1 / 一级文字: 14 px, line-height 22 px, weight 400.
- B2 / 二级文字: 12 px, line-height 18 px, weight 400.
- B4 / 三级文字: 10 px, line-height 14 px, weight 400, letter-spacing 0.5 px only when the spec calls for tiny auxiliary text.

Domestic/web type scale, useful for larger panels:

- 12/16, 14/18, 16/22, 18/24, 24/32, 32/38, 36/44, 40/48.

Keep letter spacing at `0`. Do not use oversized hero typography inside normal app screens.

## Layout And Spacing

- Design primarily for iPhone-sized mobile screens unless the user specifies another target.
- Use light gray page backgrounds with white cards or list blocks.
- Use 12 px card/content padding when matching APP card examples; use 16 px page margins for normal mobile screens.
- Use the spec spacing rhythm: 4 px for tight title-to-meta gaps, then 8, 12, 16, 24, 32 for larger relationships.
- Radius: tags use 3 pt; drawers/popups use 16 pt; cards and buttons generally use small-to-medium radii from the visual spec. Prefer 8 px for cards/buttons unless matching a page sample with a stronger radius.
- Keep dense product pages scannable: title, metadata, value/status, action. Do not stack decorative cards inside cards.
- Use shadows only to separate floating layers. Domestic shadow reference: `#9198A7` at 25% opacity, x 0, y 0, blur 30.

## Component Guidance

Use these component patterns when converting low fidelity to high fidelity:

- Navigation bar: compact top bar with clear title and minimal actions; use blue/cyan for active accents and white/light surfaces for dense pages.
- Primary button: blue fill, white text. Bottom primary actions are common for task workflows.
- Secondary button: white surface with blue border/text.
- Text button: pure text, optionally paired with an icon, for lower-emphasis actions.
- Button combinations: use primary + secondary. Do not use primary + primary or secondary + secondary pairs for main decision buttons.
- Cards: white surface, compact padding, clear title/value hierarchy, no nested cards.
- Lists and information flows: dense readable rows with title, source/type, time, optional tag, and trailing action/status.
- Tabs/segmented controls: blue active state, neutral inactive state, clear underline or pill background depending on the sample page.
- Tab bar: bottom navigation with 2-4 items is explicitly covered in the APP spec.
- Tags/chips: small radius, blue for selected/brand, orange/gold for warning/hot/highlight, gray for neutral metadata.
- Forms: support horizontal and vertical layouts; include label, placeholder/value, validation/error, and optional trailing button/switch when the PRD implies it.
- Empty states: concise Chinese copy, optional illustration, and a single blue primary action when recovery is possible.
- Popup/drawer: bottom sheet with 16 pt radius, title/subtitle/close control, selection or confirmation content, and a clear confirmation button when required.
- Data/status screens: prioritize scanability, status color, and next action over decoration.

## Content Tone

- Use concise Chinese product copy.
- Prefer task-oriented labels: "提交", "确认", "查看详情", "立即处理", "保存".
- Avoid explanatory paragraphs inside the UI unless the PRD requires guidance text.
- Use realistic sample data, but keep it obviously replaceable when source data is missing.

## Spec Handling

When exact component values are needed, consult `references/component-index.md`, then open the relevant sample PNG or PDF page. If the user's requested screen maps to multiple patterns, prefer APP samples over domestic/web samples.
