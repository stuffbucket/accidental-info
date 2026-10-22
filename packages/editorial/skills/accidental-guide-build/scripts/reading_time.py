#!/usr/bin/env python3
"""Count the printed words in a built guide and say how long it takes to read.

Usage:
  reading_time.py GUIDE [--wpm 220] [--target 1100] [--max 1250] [--quiet]

GUIDE is a built PDF, a guide folder or a slug. For a folder or a slug it reads the PDF the
build wrote, <folder>/dist/<slug>.pdf, looking the slug up in drafts/ and then guides/ at the
repository root. Build the guide first.

Counts words the way `pdftotext GUIDE.pdf - | wc -w` does, for the whole guide and for each
page, so you can see which pages to cut. The target for an Accidental Guide is five minutes
front to back, about 1,100 printed words, tables, diagram labels and sources included.

Exits 1 if the guide has more than --max words. Needs pdftotext (poppler). Standard library
otherwise.
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


def words(pdf, first=None, last=None):
    cmd = ["pdftotext"]
    if first:
        cmd += ["-f", str(first), "-l", str(last or first)]
    cmd += [pdf, "-"]
    text = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    return len(text.split())


def pages(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"^Pages:\s+(\d+)", out, re.M).group(1))


def repo_root():
    for start in (Path(__file__).resolve().parent, Path.cwd()):
        for d in (start, *start.parents):
            if (d / "packages" / "pipeline" / "guide.py").is_file():
                return d
    return None


def find_pdf(arg):
    p = Path(arg)
    if p.is_file():
        return str(p)
    folders = [p]
    root = repo_root()
    if root:
        folders += [root / "drafts" / arg, root / "guides" / arg]
    for f in folders:
        if (f / "guide.md").is_file():
            pdf = f / "dist" / f"{f.name}.pdf"
            if not pdf.is_file():
                sys.exit(f"{pdf} doesn't exist yet: build the guide first")
            return str(pdf)
    sys.exit(f"no PDF or guide for {arg!r}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", metavar="GUIDE")
    ap.add_argument("--wpm", type=int, default=220, help="reading speed in words a minute (default 220)")
    ap.add_argument("--target", type=int, default=1100, help="target printed words (default 1100)")
    ap.add_argument("--max", type=int, default=1250, help="fail above this many words (default 1250)")
    ap.add_argument("--quiet", action="store_true", help="print only the total line")
    args = ap.parse_args()

    if not shutil.which("pdftotext"):
        sys.exit("pdftotext not found; install poppler")
    args.pdf = find_pdf(args.pdf)
    total = words(args.pdf)
    minutes = total / args.wpm
    if not args.quiet and shutil.which("pdfinfo"):
        print("page  words")
        for n in range(1, pages(args.pdf) + 1):
            print(f"{n:>4}  {words(args.pdf, n):>5}")
    over = total - args.target
    verdict = "on target" if over <= 0 else f"{over} over the {args.target}-word target"
    print(f"{total} printed words, {minutes:.1f} minutes at {args.wpm} words a minute, {verdict}")
    if total > args.max:
        print(f"too long: more than {args.max} words. Cut detail, not clarity.")
        sys.exit(1)


if __name__ == "__main__":
    main()
