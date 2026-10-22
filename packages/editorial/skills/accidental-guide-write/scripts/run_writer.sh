#!/usr/bin/env bash
# Optional. Run an outside writer model on a guide with a written set of instructions (a
# round-1 brief or an edit list), then show what changed in guide.md.
#
# Usage:
#   run_writer.sh GUIDE INSTRUCTIONS.md [--model NAME] [--add-dir DIR]... [--timeout SECS] [--dry-run]
#
# GUIDE           the guide folder (drafts/<slug> or guides/<slug>), or its slug. The writer
#                 runs from here.
# INSTRUCTIONS.md the brief or edit list. The writer is told to read it and do what it says.
# --model         the writer model (default gpt-5.6-sol-fast, or $WRITER_MODEL).
# --add-dir       more folders the writer may read, such as the repository root for the
#                 base guide. Repeat for each. The guide folder, the instructions' folder
#                 and packages/editorial/skills are always added.
# --timeout       stop the writer after this many seconds (default 900).
# --dry-run       print the command and exit.
#
# You don't need this script, or any model, to contribute: you can write and edit guide.md
# yourself. If an AI model drafts or edits text you contribute, follow the disclosure rule
# in CONTRIBUTING.md.
#
# Uses the GitHub Copilot CLI (`copilot`, or the path in $COPILOT). Commit before you run it,
# so the change is easy to see and to undo. The writer edits guide.md in place; never ask it
# to regenerate a whole guide.
set -euo pipefail

usage() { sed -n '2,24p' "$0" | sed 's/^# \{0,1\}//'; exit 2; }
[ $# -ge 2 ] || usage

HERE=$(cd "$(dirname "$0")" && pwd -P)
ROOT=$HERE
while [ "$ROOT" != / ] && [ ! -f "$ROOT/packages/pipeline/guide.py" ]; do ROOT=$(dirname "$ROOT"); done
if [ -f "$1/guide.md" ]; then
  GUIDE=$(cd "$1" && pwd)
elif [ -f "$ROOT/drafts/$1/guide.md" ]; then
  GUIDE=$ROOT/drafts/$1
elif [ -f "$ROOT/guides/$1/guide.md" ]; then
  GUIDE=$ROOT/guides/$1
else
  echo "no guide folder $1, and no $1 in drafts/ or guides/" >&2; exit 1
fi
INSTR=$(cd "$(dirname "$2")" && pwd)/$(basename "$2")
shift 2
MODEL=${WRITER_MODEL:-gpt-5.6-sol-fast}
TIMEOUT=900
DRY=0
DIRS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --model) MODEL=$2; shift 2 ;;
    --add-dir) DIRS+=("--add-dir" "$(cd "$2" && pwd)"); shift 2 ;;
    --timeout) TIMEOUT=$2; shift 2 ;;
    --dry-run) DRY=1; shift ;;
    *) usage ;;
  esac
done

[ -f "$GUIDE/guide.md" ] || { echo "$GUIDE has no guide.md" >&2; exit 1; }
[ -f "$INSTR" ] || { echo "no instructions at $INSTR" >&2; exit 1; }
COPILOT=${COPILOT:-copilot}

PROMPT="Read $INSTR and do exactly what it says. Edit files in place. Don't regenerate the guide and don't touch any file the instructions don't name. No mannered prose: the writing must not call attention to itself. Make no assumption that the reader is an expert. When you're done, reply with one line: done."

CMD=("$COPILOT" --model "$MODEL" -s --allow-all-tools --add-dir "$GUIDE" --add-dir "$(dirname "$INSTR")" --add-dir "$(dirname "$(dirname "$HERE")")")
[ ${#DIRS[@]} -gt 0 ] && CMD+=("${DIRS[@]}")
CMD+=(-p "$PROMPT")

if [ "$DRY" = 1 ]; then
  echo "cd $GUIDE"
  printf '%q ' perl -e 'alarm shift; exec @ARGV' "$TIMEOUT" "${CMD[@]}"; echo
  exit 0
fi

command -v "$COPILOT" >/dev/null || { echo "$COPILOT not found; install the GitHub Copilot CLI or set COPILOT" >&2; exit 1; }

if git -C "$GUIDE" rev-parse --git-dir >/dev/null 2>&1 && ! git -C "$GUIDE" diff --quiet -- . 2>/dev/null; then
  echo "warning: $GUIDE has uncommitted changes. Commit them first so the writer's change stands alone." >&2
fi

BEFORE=$(mktemp "${TMPDIR:-/tmp}/guide-before.XXXXXX")
cp "$GUIDE/guide.md" "$BEFORE"
STAMP=$(mktemp "${TMPDIR:-/tmp}/writer-stamp.XXXXXX")

echo "== writer: $MODEL, instructions $INSTR"
set +e
(cd "$GUIDE" && perl -e 'alarm shift; exec @ARGV' "$TIMEOUT" "${CMD[@]}")
STATUS=$?
set -e
[ $STATUS -eq 0 ] || echo "writer exited with status $STATUS (142 means it hit the timeout)" >&2

echo "== changes to guide.md"
diff -u "$BEFORE" "$GUIDE/guide.md" | sed "1,2s|$BEFORE|guide.md (before)|" || true
OTHER=$(find "$GUIDE" -type f -newer "$STAMP" ! -name guide.md ! -path "*/__pycache__/*" 2>/dev/null || true)
if [ -n "$OTHER" ]; then
  echo "== the writer also changed these files; check them or restore them:"
  echo "$OTHER"
fi
rm -f "$BEFORE" "$STAMP"
exit $STATUS
