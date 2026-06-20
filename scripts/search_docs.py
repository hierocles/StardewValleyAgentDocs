#!/usr/bin/env python3
"""Search Stardew Valley modding docs by keyword, category, or tag."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "docs" / "manifest.json"


def load_manifest() -> list[dict]:
    with MANIFEST.open(encoding="utf-8") as f:
        return json.load(f)


def score_entry(entry: dict, terms: list[str]) -> int:
    haystack = " ".join(
        [
            entry.get("slug", ""),
            entry.get("title", ""),
            entry.get("category", ""),
            entry.get("wiki_source", ""),
            " ".join(entry.get("tags", [])),
        ]
    ).lower()
    score = 0
    for term in terms:
        if term in haystack:
            score += 3 if term in entry.get("slug", "").lower() else 1
        if any(term in tag.lower() for tag in entry.get("tags", [])):
            score += 2
        if term == entry.get("category", "").lower():
            score += 4
    return score


def search(query: str | None = None, category: str | None = None, limit: int = 15) -> list[dict]:
    entries = load_manifest()
    if category:
        entries = [e for e in entries if e.get("category") == category]
    if not query:
        return entries[:limit]
    terms = [t for t in re.split(r"\s+", query.lower()) if t]
    scored = [(score_entry(e, terms), e) for e in entries]
    scored = [(s, e) for s, e in scored if s > 0]
    scored.sort(key=lambda x: (-x[0], x[1]["slug"]))
    return [e for _, e in scored[:limit]]


def list_categories() -> list[str]:
    return sorted({e.get("category", "") for e in load_manifest() if e.get("category")})


def main() -> int:
    parser = argparse.ArgumentParser(description="Search Stardew modding documentation")
    parser.add_argument("query", nargs="?", help="Search terms")
    parser.add_argument("--category", "-c", help="Filter by category")
    parser.add_argument("--limit", "-n", type=int, default=15)
    parser.add_argument("--list-categories", action="store_true")
    args = parser.parse_args()

    if args.list_categories:
        for cat in list_categories():
            print(cat)
        return 0

    results = search(args.query, args.category, args.limit)
    if not results:
        print("No matches.", file=sys.stderr)
        return 1

    for entry in results:
        tags = ", ".join(entry.get("tags", [])[:5])
        print(f"{entry['slug']}\t{entry['title']}\t[{entry.get('category', '')}] {tags}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
