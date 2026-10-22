"""Keep the workspace's package.json files in step with the guide folders.

Usage: python workspace.py [--check]

Every folder under guides/ and drafts/ is a workspace package named
@accidentalguide/<slug> whose build runs guide.py on it. The site depends on every guide,
so turbo builds the guides before the site. This writes each guide's package.json and the
site's list of guides, and the lists of guides and drafts in README.md, from each guide.md's
front matter. With --check it changes nothing and fails if anything is out of step.
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
    stale = [p for p, text in wanted.items() if not p.exists() or p.read_text() != text]
    if check:
        if stale:
            sys.exit("out of step, run `pnpm sync`: " + ", ".join(str(p.relative_to(ROOT)) for p in stale))
        return
    for p in stale:
        p.write_text(wanted[p])
        print(f"wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main("--check" in sys.argv[1:])
