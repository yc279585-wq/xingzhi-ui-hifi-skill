# Xingzhi UI Hifi Skill

This repository archives the `xingzhi-ui-hifi` Codex skill for generating high-fidelity Xingzhi / HTSC PC/Web UI screens from PRDs, low-fidelity screenshots, wireframes, dashboards, chart/table pages, and desktop web product page drafts.

## Install

1. Download or clone this repository.
2. Copy the `xingzhi-ui-hifi` folder into your local Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R xingzhi-ui-hifi ~/.codex/skills/
```

3. Restart Codex if it is already open.
4. Use the skill in a prompt:

```text
$xingzhi-ui-hifi 帮我把这张页面做一张高保真出来
```

## Notes

- The skill includes domestic PC/Web component references, HTSC/Xingzhi web page templates, output checklists, logo assets, and supporting visual samples.
- No Git LFS setup is required for the current PC/Web-only archive.
- For shareable web prototypes, the skill now prefers standalone HTML with embedded assets and crisp redrawn chart/table content.
