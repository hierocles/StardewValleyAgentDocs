#!/usr/bin/env python3
"""Organize mediawiki-to-gfm output into agent-friendly docs/ tree."""

from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "output" / "raw"
DOCS_DIR = ROOT / "docs"
MANIFEST_PATH = Path(__file__).resolve().parent / "page_manifest.yaml"
WIKI_BASE = "https://stardewvalleywiki.com/"


def load_manifest() -> dict:
    with MANIFEST_PATH.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def wiki_title_to_flat_filename(title: str) -> str:
    """Match mediawiki-to-gfm --flatten naming from Convert.php retrieveFileInfo."""
    url = title.replace(" ", "_").replace(":", "_")
    if "/" in url:
        dirname, basename = url.rsplit("/", 1)
        flat = dirname.replace("/", "_") + "_" + basename
    else:
        flat = url
    return flat + ".md"


def flat_to_wiki_title(flat_stem: str, known_titles: dict[str, str]) -> str | None:
    if flat_stem in known_titles:
        return known_titles[flat_stem]
    return None


def build_flat_index(raw_dir: Path) -> dict[str, Path]:
    index: dict[str, Path] = {}
    for path in raw_dir.glob("*.md"):
        index[path.stem] = path
    return index


def build_title_map(manifest: dict) -> tuple[dict[str, str], dict[str, str]]:
    """wiki_title -> output slug; flat_stem -> wiki_title."""
    pages = manifest.get("pages", {})
    title_to_output: dict[str, str] = {}
    flat_to_title: dict[str, str] = {}

    for wiki_title in pages:
        flat = wiki_title_to_flat_filename(wiki_title)[:-3]
        flat_to_title[flat] = wiki_title
        cfg = pages[wiki_title]
        if cfg.get("emit") == "readme_source":
            continue
        if "output" in cfg:
            title_to_output[wiki_title] = cfg["output"]
        elif "splits" in cfg:
            title_to_output[wiki_title] = cfg["splits"][0]["output"]

    return title_to_output, flat_to_title


def build_slug_map(manifest: dict) -> dict[str, str]:
    slug_map: dict[str, str] = {}
    for wiki_title, cfg in manifest.get("pages", {}).items():
        if cfg.get("emit") == "readme_source":
            continue
        if "output" in cfg:
            slug_map[wiki_title] = cfg["output"]
        if "splits" in cfg:
            for split in cfg["splits"]:
                slug_map[wiki_title] = split["output"]
    return slug_map


def extract_section(text: str, start: str, end: str) -> str:
    if start == "start":
        start_idx = 0
    else:
        match = re.search(re.escape(start), text, re.IGNORECASE)
        if not match:
            return ""
        start_idx = match.start()

    if end == "end":
        return text[start_idx:].strip()

    end_match = re.search(re.escape(end), text[start_idx + 1 :], re.IGNORECASE)
    if not end_match:
        return text[start_idx:].strip()
    end_idx = start_idx + 1 + end_match.start()
    return text[start_idx:end_idx].strip()


def strip_existing_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta = yaml.safe_load(parts[1]) or {}
    return meta, parts[2].lstrip("\n")


def derive_tags(wiki_title: str, body: str) -> list[str]:
    short = wiki_title.replace("Modding:", "").replace("Modder Guide/", "").replace("APIs/", "")
    tags = [re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-") for t in short.split("/") if t]
    for match in re.finditer(r"^#{1,3}\s+(.+)$", body, re.MULTILINE):
        word = re.sub(r"[^a-z0-9]+", "-", match.group(1).strip().lower()).strip("-")
        if word and word not in tags and len(tags) < 8:
            tags.append(word)
    return tags[:8]


def rewrite_links(text: str, flat_to_slug: dict[str, str]) -> str:
    """Rewrite flattened wiki links and .md filenames to docs/ relative paths."""

    def flat_for_target(target: str) -> str:
        target = target.strip()
        if target.startswith("http"):
            return target
        target = target.split("#", 1)[0]
        return target.replace(" ", "_").replace(":", "_")

    def repl_md_link(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2)
        anchor = ""
        if "#" in target:
            target, anchor_part = target.split("#", 1)
            anchor = "#" + re.sub(r"[^a-z0-9]+", "-", anchor_part.lower()).strip("-")
        flat = flat_for_target(target)
        slug = flat_to_slug.get(flat)
        if slug:
            return f"[{label}]({slug}{anchor})"
        if flat.startswith("Modding"):
            return f"[{label}]({WIKI_BASE}{flat.replace('_', ' ')}{anchor})"
        return match.group(0)

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl_md_link, text)

    for flat, slug in flat_to_slug.items():
        text = text.replace(f"]({flat}.md", f"]({slug}")
        text = text.replace(f"]({flat})", f"]({slug})")

    return text


def make_frontmatter(
    title: str,
    wiki_source: str,
    category: str,
    tags: list[str],
    permalink: str | None,
    agent_priority: str | None = None,
) -> str:
    lines = ["---", f'title: "{title.replace(chr(34), "")}"', f'wiki_source: "{wiki_source}"']
    if permalink:
        lines.append(f"permalink: {permalink}")
    lines.append(f"category: {category}")
    if tags:
        lines.append("tags: [" + ", ".join(tags) + "]")
    if agent_priority:
        lines.append(f"agent_priority: {agent_priority}")
    lines.append("---\n")
    return "\n".join(lines)


def generate_readme(manifest: dict, entries: list[dict]) -> None:
    missing = manifest.get("missing_from_export", [])
    sections = {
        "Using mods (player guide)": [
            "player-guide/getting-started.md",
            "player-guide/troubleshooting.md",
            "player-guide/key-bindings.md",
            "player-guide/mod-compatibility.md",
        ],
        "SMAPI C# modding": [
            "smapi/get-started.md",
            "smapi/game-fundamentals.md",
            "smapi/common-tasks.md",
            "smapi/apis/overview.md",
        ],
        "Content packs": [
            "content-packs/overview.md",
            "content-packs/frameworks.md",
            "content-packs/content-patcher.md",
        ],
        "Reference": [
            "reference/game-state-queries.md",
            "reference/item-queries.md",
            "reference/context-tags.md",
        ],
        "NPCs": ["npcs/overview.md", "npcs/dialogue.md", "npcs/schedules.md"],
        "Items": ["items/overview.md", "items/objects.md", "items/crops.md"],
        "Locations": ["locations/locations.md", "locations/maps/intro-and-getting-started.md"],
    }
    by_slug = {e["slug"]: e for e in entries}
    lines = [
        "# Stardew Valley Modding Documentation",
        "",
        "Agent-friendly markdown converted with [mediawiki-to-gfm](https://github.com/outofcontrol/mediawiki-to-gfm) (Pandoc) and organized by concept.",
        "",
        f"- **Documents:** {len(entries)}",
        f"- **Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
        "",
        "See [`manifest.json`](manifest.json) for machine-readable metadata.",
        "",
        "## Concept map",
        "",
    ]
    for section, slugs in sections.items():
        lines.append(f"### {section}\n")
        for slug in slugs:
            entry = by_slug.get(slug)
            if entry:
                lines.append(f"- [{entry['title']}]({slug})")
        lines.append("")
    lines.append("## Not included in export\n")
    for page in missing:
        url = WIKI_BASE + page.replace(" ", "_")
        lines.append(f"- [{page}]({url})")
    lines.append("")
    (DOCS_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def organize(raw_dir: Path = RAW_DIR, docs_dir: Path = DOCS_DIR) -> int:
    manifest = load_manifest()
    merge_only = set(manifest.get("merge_only", []))
    pages_cfg = manifest.get("pages", {})
    flat_index = build_flat_index(raw_dir)
    _, flat_to_title = build_title_map(manifest)

    flat_to_slug: dict[str, str] = {}
    for wiki_title, cfg in pages_cfg.items():
        flat = wiki_title_to_flat_filename(wiki_title)[:-3]
        if "output" in cfg:
            flat_to_slug[flat] = cfg["output"]
        elif "splits" in cfg:
            flat_to_slug[flat] = cfg["splits"][0]["output"]

    if docs_dir.exists():
        shutil.rmtree(docs_dir)
    docs_dir.mkdir(parents=True)

    entries: list[dict] = []

    for wiki_title, cfg in pages_cfg.items():
        if wiki_title in merge_only or cfg.get("emit") == "readme_source":
            continue
        flat_name = wiki_title_to_flat_filename(wiki_title)
        raw_path = flat_index.get(flat_name[:-3])
        if not raw_path or not raw_path.exists():
            print(f"Warning: missing raw file for {wiki_title} ({flat_name})", file=sys.stderr)
            continue

        raw_text = raw_path.read_text(encoding="utf-8")
        meta, body = strip_existing_frontmatter(raw_text)
        body = rewrite_links(body, flat_to_slug)

        outputs: list[tuple[dict, str]] = []
        if "splits" in cfg:
            for split in cfg["splits"]:
                section = extract_section(body, split.get("from", "start"), split.get("until", "end"))
                if section:
                    outputs.append((split, section))
        elif "output" in cfg:
            outputs.append((cfg, body))

        for split_cfg, content in outputs:
            out_path = docs_dir / split_cfg["output"]
            out_path.parent.mkdir(parents=True, exist_ok=True)
            category = split_cfg.get("category", "general")
            display = out_path.stem.replace("-", " ").title()
            tags = derive_tags(wiki_title, content)
            fm = make_frontmatter(
                display,
                wiki_title,
                category,
                tags,
                meta.get("permalink"),
                split_cfg.get("agent_priority"),
            )
            out_path.write_text(fm + content + "\n", encoding="utf-8")
            slug = split_cfg["output"].replace("\\", "/")
            entries.append(
                {
                    "slug": slug,
                    "title": display,
                    "category": category,
                    "tags": tags,
                    "wiki_source": wiki_title,
                }
            )

    (docs_dir / "manifest.json").write_text(json.dumps(sorted(entries, key=lambda e: e["slug"]), indent=2), encoding="utf-8")
    generate_readme(manifest, entries)
    print(f"Organized {len(entries)} documents into {docs_dir}")
    return 0


if __name__ == "__main__":
    raw = Path(sys.argv[1]) if len(sys.argv) > 1 else RAW_DIR
    docs = Path(sys.argv[2]) if len(sys.argv) > 2 else DOCS_DIR
    raise SystemExit(organize(raw, docs))
