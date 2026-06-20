#!/usr/bin/env python3
"""Preprocess MediaWiki XML export before Pandoc conversion."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from wiki_templates import preprocess_wikitext

NS = {"mw": "http://www.mediawiki.org/xml/export-0.11/"}
ET.register_namespace("", NS["mw"])


def load_fragment_pages(root: ET.Element) -> dict[str, str]:
    pages: dict[str, str] = {}
    for page in root.findall("mw:page", NS):
        title_el = page.find("mw:title", NS)
        text_el = page.find("mw:revision/mw:text", NS)
        if title_el is None or text_el is None or text_el.text is None:
            continue
        pages[title_el.text] = text_el.text
    return pages


def preprocess_xml(input_path: Path, output_path: Path) -> None:
    tree = ET.parse(input_path)
    root = tree.getroot()
    fragments = load_fragment_pages(root)

    for page in root.findall("mw:page", NS):
        text_el = page.find("mw:revision/mw:text", NS)
        if text_el is None or text_el.text is None:
            continue
        text_el.text = preprocess_wikitext(text_el.text, fragments)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "Stardew+Valley+Wiki-20260620185839.xml"
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else root / "output" / "preprocessed.xml"

    if not input_path.exists():
        print(f"Error: input not found: {input_path}", file=sys.stderr)
        return 1

    preprocess_xml(input_path, output_path)
    print(f"Preprocessed {input_path.name} -> {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
