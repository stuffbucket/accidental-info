#!/usr/bin/env python3
"""Check guide folders against the public taxonomy.

Usage: check_portfolio.py [--root REPOSITORY]
"""
import argparse
import json
import re
from pathlib import Path

SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CODE = re.compile(r"^[A-Z][a-z0-9]$")


def repo_root(start: Path) -> Path:
    for path in (start, *start.parents):
        if (path / "site/src/data/collections.json").is_file():
            return path
    raise SystemExit("cannot find the repository root")


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    head = text.split("\n---\n", 1)[0]
    return dict(re.findall(r"^(\w+): (.*)$", head, re.M))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path)
    args = parser.parse_args()
    root = args.root.resolve() if args.root else repo_root(Path(__file__).resolve())
    data = json.loads((root / "site/src/data/collections.json").read_text(encoding="utf-8"))
    problems: list[str] = []
    listed: dict[str, str] = {}
    codes: dict[str, str] = {}
    coded_slugs: set[str] = set()

    def add(slug: str, where: str) -> None:
        if not SLUG.fullmatch(slug or ""):
            problems.append(f"{where}: invalid slug {slug!r}")
        if slug in listed:
            problems.append(f"{slug}: listed by {listed[slug]} and {where}")
        else:
            listed[slug] = where

    collection_ids: set[str] = set()
    for collection in data.get("collections", []):
        cid = collection.get("id", "")
        if cid in collection_ids:
            problems.append(f"duplicate collection id {cid!r}")
        collection_ids.add(cid)
        if not SLUG.fullmatch(cid):
            problems.append(f"invalid collection id {cid!r}")
        if collection.get("groups"):
            catalog = collection.get("catalog")
            if not catalog:
                problems.append(f"{cid}: grouped collection needs a catalog")
            else:
                add(catalog, f"collection {cid} catalog")
            group_ids: set[str] = set()
            for group in collection["groups"]:
                gid = group.get("id", "")
                if gid in group_ids:
                    problems.append(f"{cid}: duplicate group id {gid!r}")
                group_ids.add(gid)
                if not SLUG.fullmatch(gid) or not group.get("name"):
                    problems.append(f"{cid}: malformed group {gid!r}")
                where = f"{cid}/{gid}"
                for slug in group.get("guides", []):
                    add(slug, where)
                for entry in group.get("coming", []):
                    if not entry.get("title"):
                        problems.append(f"{where}: {entry.get('id')!r} has no title")
                    add(entry.get("id", ""), where)
        else:
            for slug in collection.get("guides", []):
                add(slug, f"collection {cid}")
            for entry in collection.get("coming", []):
                if not entry.get("title"):
                    problems.append(f"collection {cid}: {entry.get('id')!r} has no title")
                add(entry.get("id", ""), f"collection {cid}")

        for slug, code in collection.get("codes", {}).items():
            coded_slugs.add(slug)
            if not CODE.fullmatch(code or ""):
                problems.append(f"{cid}: {slug} has invalid map code {code!r}")
            if code in codes:
                problems.append(f"map code {code!r} is used by {codes[code]} and {slug}")
            else:
                codes[code] = slug

    folders: dict[str, Path] = {}
    for state in ("guides", "drafts"):
        base = root / state
        for folder in base.iterdir() if base.is_dir() else []:
            source = folder / "guide.md"
            if not source.is_file():
                continue
            if folder.name in folders:
                problems.append(f"{folder.name}: exists in both guides and drafts")
            folders[folder.name] = folder
            if folder.name not in listed:
                problems.append(f"{folder.name}: built guide is absent from collections.json")
            meta = front_matter(source)
            if not meta.get("title"):
                problems.append(f"{folder.name}: guide.md has no title")
            if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", meta.get("version", "")):
                problems.append(f"{folder.name}: guide.md has invalid version")
            if meta.get("edition", "").split(" · ", 1)[0] != "friend@accidental.info":
                problems.append(f"{folder.name}: end-page contact is not friend@accidental.info")

    for slug in listed:
        on_map = any(
            collection.get("groups") and (
                slug == collection.get("catalog")
                or any(
                    slug in group.get("guides", [])
                    or slug in [entry.get("id") for entry in group.get("coming", [])]
                    for group in collection.get("groups", [])
                )
            )
            for collection in data["collections"]
        )
        if on_map and slug not in coded_slugs:
            problems.append(f"{slug}: mapped guide has no map code")

    if problems:
        raise SystemExit("portfolio problems:\n- " + "\n- ".join(problems))
    print(f"portfolio ok: {len(folders)} built guides, {len(listed) - len(folders)} planned guides, {len(data['collections'])} collections")


if __name__ == "__main__":
    main()
