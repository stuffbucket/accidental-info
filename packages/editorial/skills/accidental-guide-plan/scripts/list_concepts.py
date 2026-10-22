#!/usr/bin/env python3
"""List the key concepts (filled tiles) of every guide, and flag any concept that is a key
in more than one guide.

Usage:
  list_concepts.py [GUIDES_DIR ...]

GUIDES_DIR is a folder of guide folders, such as guides/ or drafts/. With none given, it
reads guides/ and drafts/ at the repository root. A guide folder is one with a guide.md.
Keys are the "# Name {#entry ...}" headings; the two-letter tile key comes from mono=.
Standard library only.

Use it when planning a guide: each concept is a key in exactly one guide, and a tile key
(such as Sp) shouldn't mean two different things in the series. The per-harness guides
show other guides' tiles on purpose; packages/editorial/registry.md says which guide owns
each concept.
"""
import re
import sys
from pathlib import Path

ENTRY = re.compile(r"^# (.*?) \{#entry\b([^}]*)\}\s*$")


def repo_root():
    for start in (Path(__file__).resolve().parent, Path.cwd()):
        for d in (start, *start.parents):
            if (d / "packages" / "pipeline" / "guide.py").is_file():
                return d
    sys.exit("can't find the repository root (the folder with packages/pipeline/guide.py)")


def norm(name):
    """Compare names without case or a plural s, so Skill and Skills count as one."""
    return re.sub(r"s$", "", name.lower())


def front(text):
    meta = {}
    lines = text.splitlines()
    if lines and lines[0] == "---":
        for line in lines[1:]:
            if line == "---":
                break
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
    return meta


def main():
    if any(a in ("-h", "--help") for a in sys.argv[1:]):
        sys.exit(__doc__.strip())
    if sys.argv[1:]:
        dirs = [Path(d) for d in sys.argv[1:]]
    else:
        root = repo_root()
        dirs = [root / "guides", root / "drafts"]
    by_name, by_key = {}, {}
    for d in dirs:
        if not d.is_dir():
            continue
        for g in sorted(d.iterdir()):
            md = g / "guide.md"
            if not md.is_file():
                continue
            text = md.read_text(encoding="utf-8")
            meta = front(text)
            keys = []
            for line in text.splitlines():
                m = ENTRY.match(line)
                if m:
                    attrs = dict(a.split("=", 1) for a in m.group(2).split() if "=" in a)
                    name, key = m.group(1).replace("<br/>", " "), attrs.get("mono", "?")
                    keys.append(f"{attrs.get('num', '?')} {name} ({key})")
                    by_name.setdefault(norm(name), []).append(g.name)
                    by_key.setdefault(key, set()).add((name, g.name))
            print(f"{d.name}/{g.name}  {meta.get('title', '?')}  v{meta.get('version', '?')}")
            print("    " + ("; ".join(keys) if keys else "no entries"))
    clashes = {n: gs for n, gs in by_name.items() if len(gs) > 1}
    keyclash = {k: v for k, v in by_key.items() if len({norm(n) for n, _ in v}) > 1}
    print()
    if clashes:
        print("concepts that are a key in more than one guide:")
        for n, gs in sorted(clashes.items()):
            print(f"    {n}: {', '.join(gs)}")
    else:
        print("no concept is a key in more than one guide")
    if keyclash:
        print("tile keys that mean different things in different guides:")
        for k, v in sorted(keyclash.items()):
            print(f"    {k}: " + ", ".join(f"{n} in {g}" for n, g in sorted(v)))


if __name__ == "__main__":
    main()
