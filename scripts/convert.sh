#!/usr/bin/env bash
# Convert Stardew Valley Wiki XML export to agent-friendly docs using mediawiki-to-gfm.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if [[ -n "${1:-}" ]]; then
  XML="$1"
elif [[ -f "$ROOT/Stardew+Valley+Wiki-20260620185839.xml" ]]; then
  XML="$ROOT/Stardew+Valley+Wiki-20260620185839.xml"
else
  XML="$ROOT/Stardew+Valley+Wiki-20260620182032.xml"
fi
MW2GFM="$ROOT/tools/mediawiki-to-gfm"
RAW="$ROOT/output/raw"
PHP="${PHP_BIN:-php}"

if [[ ! -f "$XML" ]]; then
  echo "Error: XML export not found at: $XML" >&2
  echo "Place your MediaWiki export at the repo root or pass the path as the first argument." >&2
  exit 1
fi

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc is required (3.9+). See https://pandoc.org/installing.html" >&2
  exit 1
fi

if ! command -v "$PHP" >/dev/null 2>&1; then
  # Common Windows winget install path
  if [[ -x "/c/Users/dylan/AppData/Local/Microsoft/WinGet/Packages/PHP.PHP.8.4_Microsoft.Winget.Source_8wekyb3d8bbwe/php.exe" ]]; then
    PHP="/c/Users/dylan/AppData/Local/Microsoft/WinGet/Packages/PHP.PHP.8.4_Microsoft.Winget.Source_8wekyb3d8bbwe/php.exe"
  else
    echo "Error: PHP 8.4+ is required. Set PHP_BIN or install PHP." >&2
    exit 1
  fi
fi

export PATH="/c/Program Files/Pandoc:$PATH"
mkdir -p "$RAW"
rm -rf "$RAW"/*

PREPROCESSED="$ROOT/output/preprocessed.xml"
echo "==> Preprocessing wiki templates..."
python "$ROOT/scripts/preprocess_export.py" "$XML" "$PREPROCESSED"

echo "==> Converting with mediawiki-to-gfm (Pandoc)..."
"$PHP" "$MW2GFM/convert.php" \
  --filename="$PREPROCESSED" \
  --output="$RAW" \
  --format=gfm \
  --addmeta \
  --flatten \
  --skiperrors

echo "==> Organizing into docs/ by concept..."
python "$ROOT/scripts/organize_docs.py" "$RAW" "$ROOT/docs"

echo "Done. See docs/README.md"
