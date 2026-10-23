"""Keep the workspace's package.json files in step with the guide folders.

Usage: python workspace.py [--check]

Every folder under guides/ and drafts/ is a workspace package named
@accidentalguide/<slug> whose build runs guide.py on it. The site depends on every guide,
so turbo builds the guides before the site. This writes each guide's package.json and the
site's list of guides, and the lists of guides and drafts in README.md, from each guide.md's
front matter. It also writes the front matter the cover's band reads (collection,
collection_mark and number) from site/src/data/collections.json. With --check it changes
nothing and fails if anything is out of step.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1].parent
SCOPE = "@accidentalguide"


def guide_package(slug):
    return {
        "name": f"{SCOPE}/{slug}",
        "private": True,
        "scripts": {"build": "../../.venv/bin/python ../../packages/pipeline/guide.py ."},
        "devDependencies": {f"{SCOPE}/pipeline": "workspace:*"},
    }


SITE = "https://stuffbucket.github.io/accidentalguide"


def front_matter(folder):
    text = (folder / "guide.md").read_text(encoding="utf-8")
    block = text.split("\n---\n", 1)[0]
    return dict(re.findall(r"^(\w+): (.*)$", block, re.M))


COLLECTIONS = ROOT / "site" / "src" / "data" / "collections.json"
# Each collection's mark on its guides' covers, by collection id, as the cover study drew them
# (packages/editorial/design/cover-study/scripts/kit.py).
MARKS = {"intelligence": "square", "around-the-house": "triangle", "at-the-table": "circle",
         "games": "diamond"}


def cover_keys():
    """The front matter each listed guide's cover reads, by guide id: its collection's name and
    mark, and its two-digit number in the collection. A collection's catalog is 00. The other
    guides are numbered from 01 in the order the collection lists them: each group's guides and
    then its coming guides, then the collection's own guides and coming guides."""
    keys = {}
    for coll in json.loads(COLLECTIONS.read_text(encoding="utf-8"))["collections"]:
        if coll["id"] not in MARKS:
            sys.exit(f"collection {coll['id']!r} has no mark; add one to MARKS in "
                     "packages/pipeline/workspace.py")
        order = []
        for group in coll.get("groups", []):
            order += group.get("guides", []) + [g["id"] for g in group.get("coming", [])]
        order += coll.get("guides", []) + [g["id"] for g in coll.get("coming", [])]
        numbered = [(coll["catalog"], 0)] if coll.get("catalog") else []
        numbered += [(gid, n) for n, gid in enumerate(order, 1)]
        for gid, n in numbered:
            keys[gid] = {"collection": coll["name"], "collection_mark": MARKS[coll["id"]],
                         "number": f"{n:02d}"}
    return keys


def with_keys(text, values):
    """guide.md with these front matter keys set; a missing one goes after cover_footer, or
    after the key before it."""
    head, sep, body = text.partition("\n---\n")
    lines = head.split("\n")
    after = [i for i, l in enumerate(lines) if l.startswith("cover_footer:")]
    at = after[0] if after else len(lines) - 1
    for key, value in values.items():
        found = [i for i, l in enumerate(lines) if l.startswith(f"{key}:")]
        if found:
            at = found[0]
            lines[at] = f"{key}: {value}"
        else:
            at += 1
            lines.insert(at, f"{key}: {value}")
    return "\n".join(lines) + sep + body


def readme_table(folders, kind):
    rows = ["| Guide | What it covers | Version | Download |", "| --- | --- | --- | --- |"]
    for f in folders:
        fm = front_matter(f)
        page = f"{SITE}/{kind}/{f.name}/"
        files = f"[PDF]({SITE}/guides/{f.name}.pdf) · [Word]({SITE}/guides/{f.name}.docx)"
        rows.append(f"| [{fm['title']}]({page}) | {fm['subtitle']} | {fm['version']} | {files} |")
    return "\n".join(rows)


def readme(text, published, drafts):
    for kind, folders in (("guides", published), ("drafts", drafts)):
        start, end = f"<!-- {kind}:start -->", f"<!-- {kind}:end -->"
        before, rest = text.split(start, 1)
        after = rest.split(end, 1)[1]
        text = f"{before}{start}\n{readme_table(folders, kind)}\n{end}{after}"
    return text


ORDER = ["accidental-intelligence", "agents-harnesses-skills-tools", "specs-and-reviews",
         "software-factories", "lights-off-software-factories"]


def ordered(folders):
    return sorted(folders, key=lambda f: (ORDER.index(f.name) if f.name in ORDER else len(ORDER), f.name))


def dump(data):
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def main(check):
    folders = sorted(f for d in ("guides", "drafts") if (ROOT / d).is_dir()
                     for f in (ROOT / d).iterdir() if (f / "guide.md").exists())
    wanted = {f / "package.json": dump(guide_package(f.name)) for f in folders}
    keys = cover_keys()
    unlisted = [f.name for f in folders if f.name not in keys]
    for f in folders:
        if f.name in keys:
            wanted[f / "guide.md"] = with_keys((f / "guide.md").read_text(encoding="utf-8"), keys[f.name])
    site_path = ROOT / "site" / "package.json"
    site = json.loads(site_path.read_text())
    deps = {k: v for k, v in site.get("devDependencies", {}).items()
            if not k.startswith(f"{SCOPE}/") or k == f"{SCOPE}/pipeline"}
    deps.update({f"{SCOPE}/{f.name}": "workspace:*" for f in folders})
    site["devDependencies"] = dict(sorted(deps.items()))
    wanted[site_path] = dump(site)
    readme_path = ROOT / "README.md"
    wanted[readme_path] = readme(readme_path.read_text(encoding="utf-8"),
                                 ordered(f for f in folders if f.parent.name == "guides"),
                                 ordered(f for f in folders if f.parent.name == "drafts"))
    stale = [p for p, text in wanted.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
    note = (f"not in {COLLECTIONS.relative_to(ROOT)}, so the cover has no collection or number: "
            + ", ".join(unlisted))
    if check:
        if stale:
            sys.exit("out of step, run `pnpm sync`: " + ", ".join(str(p.relative_to(ROOT)) for p in stale))
        if unlisted:
            sys.exit(note)
        return
    for p in stale:
        p.write_text(wanted[p], encoding="utf-8")
        print(f"wrote {p.relative_to(ROOT)}")
    if unlisted:
        print(f"note: {note}; list them there and run `pnpm sync` again")


if __name__ == "__main__":
    main("--check" in sys.argv[1:])
