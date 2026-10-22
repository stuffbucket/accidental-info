#!/usr/bin/env bash
# Build one guide: the PDF, the Word document, the hash check, page images and reading time.
#
# Usage:
#   build_one.sh GUIDE [--out DIR] [--update-hash] [--pages-dir DIR] [--dpi N]
#
# GUIDE          the guide folder (drafts/<slug> or guides/<slug>), or just the slug, which is
#                looked up in drafts/ and then guides/ at the repository root.
# --out          where the PDF and .docx go (default GUIDE/dist, where the pipeline puts them).
# --update-hash  write the new PDF hash to GUIDE/expected.sha256, rebuild, and confirm it
#                matches. Use it when the text changed on purpose.
# --pages-dir    where the page images go (default: a new temporary folder).
# --dpi          resolution of the page images (default 60).
#
# The repository root is found from this script's own location. The Python interpreter is
# the root's .venv/bin/python unless PYTHON is set. Needs pdftoppm and pdftotext (poppler)
# for the page images and the word count. Exits non-zero if a build fails or a page
# overflows. The workspace build (pnpm turbo run build --filter=@accidentalguide/<slug>)
# runs the same checks and also writes dist/guide.json for the site.
set -euo pipefail

usage() { sed -n '2,19p' "$0" | sed 's/^# \{0,1\}//'; exit 2; }
[ $# -ge 1 ] || usage

HERE=$(cd "$(dirname "$0")" && pwd -P)
ROOT=$HERE
while [ "$ROOT" != / ] && [ ! -f "$ROOT/packages/pipeline/guide.py" ]; do ROOT=$(dirname "$ROOT"); done
[ -f "$ROOT/packages/pipeline/guide.py" ] || { echo "can't find the repository root (the folder with packages/pipeline/guide.py)" >&2; exit 1; }

if [ -f "$1/guide.md" ]; then
  GUIDE=$(cd "$1" && pwd)
elif [ -d "$ROOT/drafts/$1" ]; then
  GUIDE=$ROOT/drafts/$1
elif [ -d "$ROOT/guides/$1" ]; then
  GUIDE=$ROOT/guides/$1
else
  echo "no guide folder $1, and no $1 in drafts/ or guides/" >&2; exit 1
fi
shift
OUT="$GUIDE/dist"
UPDATE=0
PAGES=""
DPI=60
while [ $# -gt 0 ]; do
  case "$1" in
    --out) OUT=$2; shift 2 ;;
    --update-hash) UPDATE=1; shift ;;
    --pages-dir) PAGES=$2; shift 2 ;;
    --dpi) DPI=$2; shift 2 ;;
    *) usage ;;
  esac
done

SLUG=$(basename "$GUIDE")
PY=${PYTHON:-$ROOT/.venv/bin/python}

if [ ! -x "$PY" ]; then
  echo "no Python at $PY. Make the environment first, from $ROOT:" >&2
  echo "  pnpm turbo run build --filter=@accidentalguide/pipeline" >&2
  exit 1
fi
for f in guide.md content.py build_guide.py; do
  [ -f "$GUIDE/$f" ] || { echo "$GUIDE has no $f" >&2; exit 1; }
done
mkdir -p "$OUT"
OUT=$(cd "$OUT" && pwd)
PDF="$OUT/$SLUG.pdf"
DOCX="$OUT/$SLUG.docx"

build_pdf() {
  local log
  log=$(cd "$GUIDE" && "$PY" build_guide.py "$PDF") || { echo "$log"; echo "build_guide.py failed" >&2; exit 1; }
  echo "$log"
  if ! grep -q "^no overflow$" <<<"$log"; then
    echo "OVERFLOW: content runs past the bottom margin. Cut words; don't squeeze." >&2
    exit 1
  fi
  PDF_PAGES=$(sed -n 's/^wrote .*: \([0-9]*\) pages$/\1/p' <<<"$log")
  HASH=$(sed -n 's/^sha256 //p' <<<"$log")
  HASH_LINE=$(grep -E "^(matches|DIFFERS)" <<<"$log" || echo "no expected.sha256 yet")
}

echo "== PDF"
build_pdf

if [ "$UPDATE" = 1 ]; then
  echo "$HASH  $SLUG.pdf" > "$GUIDE/expected.sha256"
  echo "== wrote $GUIDE/expected.sha256; rebuilding to confirm"
  build_pdf
fi

if [ -f "$GUIDE/build_docx.py" ]; then
  echo "== Word"
  DLOG=$(cd "$GUIDE" && "$PY" build_docx.py "$PDF" "$DOCX") || { echo "$DLOG"; echo "build_docx.py failed" >&2; exit 1; }
  echo "$DLOG"
  DOCX_PAGES=$(sed -n 's/^wrote .*: \([0-9]*\) pages$/\1/p' <<<"$DLOG")
  if [ "$DOCX_PAGES" != "$PDF_PAGES" ]; then
    echo "WARNING: the PDF has $PDF_PAGES pages and the .docx has $DOCX_PAGES. Check the page order in build_docx.py." >&2
  fi
fi

if command -v pdftoppm >/dev/null; then
  echo "== Pages"
  [ -n "$PAGES" ] || PAGES=$(mktemp -d "${TMPDIR:-/tmp}/$SLUG-pages.XXXXXX")
  mkdir -p "$PAGES"
  rm -f "$PAGES/$SLUG"-*.png
  pdftoppm -r "$DPI" -png "$PDF" "$PAGES/$SLUG"
  echo "page images in $PAGES ($(ls "$PAGES" | grep -c "^$SLUG-.*png$") files). Look at every one."
else
  echo "pdftoppm not found; install poppler to render the pages" >&2
fi

if [ -f "$HERE/reading_time.py" ] && command -v pdftotext >/dev/null; then
  echo "== Reading time"
  "${PYTHON3:-python3}" "$HERE/reading_time.py" "$PDF" || true
fi

echo "== Summary"
echo "pdf   $PDF ($PDF_PAGES pages)"
[ -f "$DOCX" ] && echo "docx  $DOCX"
echo "hash  $HASH_LINE"
