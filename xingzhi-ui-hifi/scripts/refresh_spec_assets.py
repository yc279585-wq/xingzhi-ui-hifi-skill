#!/usr/bin/env python3
"""Refresh Xingzhi spec text indexes and sample page renders."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw
from pypdf import PdfReader


DEFAULT_DESIGN_PAGES = [2, 3, 6, 8, 11, 12, 20, 21, 25, 29, 35, 39, 40, 41, 44, 45, 46, 50, 52, 56, 58]
DEFAULT_DOMESTIC_PAGES = [3, 4, 8, 10, 14, 18, 21, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55]


def extract_text(pdf_path: Path, out_md: Path, out_tsv: Path) -> None:
    reader = PdfReader(str(pdf_path))
    lines = [f"# Extracted text: {pdf_path.name}\n", f"Pages: {len(reader.pages)}\n"]
    headings: list[tuple[int, str]] = []
    for index, page in enumerate(reader.pages, 1):
        try:
            text = page.extract_text() or ""
        except Exception as exc:  # Keep the index useful even when one page is odd.
            text = f"[text extraction failed: {exc}]"
        text = "\n".join(line.strip() for line in text.splitlines() if line.strip())
        lines.extend([f"\n\n## Page {index}\n", text[:3000] if text else "[no extractable text]"])
        for line in text.splitlines()[:10]:
            if 2 <= len(line) <= 50:
                headings.append((index, line))
    out_md.write_text("\n".join(lines), encoding="utf-8")
    out_tsv.write_text("\n".join(f"{page}\t{text}" for page, text in headings), encoding="utf-8")


def render_pages(pdftoppm: str, pdf_path: Path, out_dir: Path, prefix: str, pages: list[int], width: int) -> None:
    for page in pages:
        output_prefix = out_dir / f"{prefix}-p{page:03d}"
        subprocess.run(
            [
                pdftoppm,
                "-f",
                str(page),
                "-l",
                str(page),
                "-scale-to-x",
                str(width),
                "-scale-to-y",
                "-1",
                "-png",
                "-singlefile",
                str(pdf_path),
                str(output_prefix),
            ],
            check=True,
        )


def contact_sheet(out_dir: Path, prefix: str, columns: int = 3) -> None:
    files = sorted(out_dir.glob(f"{prefix}-p*.png"))
    thumbs = []
    for path in files:
        image = Image.open(path).convert("RGB")
        image.thumbnail((320, 220), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (340, 260), "white")
        canvas.paste(image, ((340 - image.width) // 2, 24))
        ImageDraw.Draw(canvas).text((12, 6), path.stem, fill=(30, 30, 30))
        thumbs.append(canvas)
    rows = (len(thumbs) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * 340, rows * 260), (245, 247, 250))
    for index, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((index % columns) * 340, (index // columns) * 260))
    sheet.save(out_dir / f"{prefix}-contact-sheet.png", quality=90)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--pdftoppm", default="pdftoppm")
    args = parser.parse_args()

    skill_dir = args.skill_dir
    assets = skill_dir / "assets"
    refs = skill_dir / "references" / "extracted"
    samples = assets / "pdf-samples"
    refs.mkdir(parents=True, exist_ok=True)
    samples.mkdir(parents=True, exist_ok=True)

    design_pdf = assets / "xingzhi-app-2025-design-spec.pdf"
    domestic_pdf = assets / "domestic-component-spec.pdf"
    extract_text(design_pdf, refs / "design-text.md", refs / "design-headings.tsv")
    extract_text(domestic_pdf, refs / "domestic-text.md", refs / "domestic-headings.tsv")
    render_pages(args.pdftoppm, design_pdf, samples, "design", DEFAULT_DESIGN_PAGES, 960)
    render_pages(args.pdftoppm, domestic_pdf, samples, "domestic", DEFAULT_DOMESTIC_PAGES, 1200)
    contact_sheet(samples, "design")
    contact_sheet(samples, "domestic")


if __name__ == "__main__":
    main()
