"""Make a GitHub release for each guide version that doesn't have one yet.

Usage: python3 release.py <folder> [--dry-run]

<folder> holds guides.json and guides/<id>.pdf and guides/<id>.docx, laid out as
guide_pages.py writes them under site/public/. For each guide whose tag <id>-v<version> is
not in the repository yet, this runs `gh release create`: the release is named
"<Title> <version>", a draft guide's release is marked as a prerelease, the PDF and the Word
document are attached, and the notes are the guide's subtitle and blurb with a link to read
it online. A guide whose tag exists is skipped, so running it again changes nothing.

gh reads the repository from GH_REPO and the token from GH_TOKEN. TARGET, if set, is the
commit the new tags point at. Uses the standard library only, so it runs on a CI runner's
own Python.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

# Where the site is served; the Pages workflow sets these from actions/configure-pages.
SITE = (os.environ.get("SITE_ORIGIN", "https://stuffbucket.github.io").rstrip("/")
        + os.environ.get("SITE_BASE", "/accidentalguide").rstrip("/"))


def tag(guide):
    return f"{guide['id']}-v{guide['version']}"


def page_url(guide):
    folder = "drafts" if guide.get("status") == "draft" else "guides"
    return f"{SITE}/{folder}/{guide['id']}/"


def notes(guide):
    """The release notes: the guide's card, subtitle and blurb, and where to read it."""
    parts = [f"![{guide['title']}]({SITE}/guides/{guide['id']}/card.png)", guide["subtitle"]]
    if guide.get("blurb"):
        parts.append(guide["blurb"])
    if guide.get("status") == "draft":
        parts.append("Still being written. Its words and parts may change.")
    parts.append(f"Read it online: {page_url(guide)}")
    return "\n\n".join(parts) + "\n"


def command(guide, folder, target=None):
    files = [folder / "guides" / name for name in (guide["pdf"], guide.get("docx")) if name]
    missing = [str(f) for f in files if not f.exists()]
    if missing:
        sys.exit(f"{guide['id']}: missing {', '.join(missing)}")
    args = ["gh", "release", "create", tag(guide), *map(str, files),
            "--title", f"{guide['title']} {guide['version']}", "--notes", notes(guide)]
    if target:
        args += ["--target", target]
    if guide.get("status") == "draft":
        args.append("--prerelease")
    return args


def existing_tags():
    out = subprocess.run(["gh", "api", "--paginate", "repos/{owner}/{repo}/tags", "--jq", ".[].name"],
                         check=True, capture_output=True, text=True).stdout
    return set(out.split())


def main(folder, dry_run=False):
    guides = json.loads((folder / "guides.json").read_text(encoding="utf-8"))
    tags = existing_tags()
    for guide in guides:
        if tag(guide) in tags:
            print(f"{tag(guide)}: tag exists, skipped")
            continue
        args = command(guide, folder, os.environ.get("TARGET"))
        if dry_run:
            print(f"{tag(guide)}: would run {args}")
            continue
        subprocess.run(args, check=True)
        print(f"{tag(guide)}: released")


if __name__ == "__main__":
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(paths) != 1 or set(flags) - {"--dry-run"}:
        sys.exit(__doc__)
    main(Path(paths[0]), dry_run="--dry-run" in flags)
