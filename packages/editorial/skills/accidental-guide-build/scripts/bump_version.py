#!/usr/bin/env python3
"""Bump the semver version: line in a guide's front matter.

Usage:
  bump_version.py GUIDE patch|minor|major
  bump_version.py GUIDE --show

GUIDE is a guide.md, a guide folder, or a slug (looked up in drafts/ and then guides/ at
the repository root).

patch: wording fixes and small edits (0.3.0 -> 0.3.1).
minor: a new round of edits, cuts or a changed page (0.3.1 -> 0.4.0).
major: the guide is published as reviewed, or its key concepts change after that (0.4.0 -> 1.0.0).

Prints the old and new version. Standard library only.
"""
import re
import sys
from pathlib import Path

SEMVER = re.compile(r"^version:\s*(\d+)\.(\d+)\.(\d+)\s*$")


def repo_root():
    for start in (Path(__file__).resolve().parent, Path.cwd()):
        for d in (start, *start.parents):
            if (d / "packages" / "pipeline" / "guide.py").is_file():
                return d
    return None


def guide_md(arg):
    p = Path(arg)
    if p.is_file():
        return p
    if (p / "guide.md").is_file():
        return p / "guide.md"
    root = repo_root()
    for kind in ("drafts", "guides"):
        if root and (root / kind / arg / "guide.md").is_file():
            return root / kind / arg / "guide.md"
    sys.exit(f"no guide.md for {arg!r}: give a guide.md, a guide folder or a slug")


def main():
    if len(sys.argv) != 3 or sys.argv[2] not in ("patch", "minor", "major", "--show"):
        sys.exit(__doc__.strip())
    path, part = guide_md(sys.argv[1]), sys.argv[2]
    lines = path.read_text(encoding="utf-8").split("\n")
    if lines[0] != "---":
        sys.exit(f"{path}: no front matter (line 1 must be ---)")
    for i in range(1, len(lines)):
        if lines[i] == "---":
            sys.exit(f"{path}: front matter has no version: line; add version: 0.1.0")
        m = SEMVER.match(lines[i])
        if m:
            break
    major, minor, patch = map(int, m.groups())
    old = f"{major}.{minor}.{patch}"
    if part == "--show":
        print(old)
        return
    if part == "major":
        major, minor, patch = major + 1, 0, 0
    elif part == "minor":
        minor, patch = minor + 1, 0
    else:
        patch += 1
    new = f"{major}.{minor}.{patch}"
    lines[i] = f"version: {new}"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"{path}: {old} -> {new}")


if __name__ == "__main__":
    main()
