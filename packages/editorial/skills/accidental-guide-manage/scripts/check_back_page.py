#!/usr/bin/env python3
"""Check every guide builder against the shared back-page contract.

Usage: check_back_page.py [--root REPOSITORY]
"""
import argparse
from pathlib import Path


CONTACT = "friend@accidental.info"
TAGLINE = "My friend has some questions."


def repo_root(start: Path) -> Path:
    for path in (start, *start.parents):
        if (path / "packages/pipeline/guide.py").is_file():
            return path
    raise SystemExit("cannot find the repository root")


def ordered(text: str, needles: tuple[str, ...]) -> bool:
    position = -1
    for needle in needles:
        position = text.find(needle, position + 1)
        if position < 0:
            return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path)
    args = parser.parse_args()
    root = args.root.resolve() if args.root else repo_root(Path(__file__).resolve())
    folders = [
        folder
        for base in (root / "guides", root / "drafts")
        for folder in sorted(base.iterdir())
        if (folder / "guide.md").is_file()
    ]
    folders.append(root / "packages/template")
    problems: list[str] = []

    for folder in folders:
        label = folder.relative_to(root)
        pdf_path = folder / "build_guide.py"
        docx_path = folder / "build_docx.py"
        for path in (pdf_path, docx_path):
            if not path.is_file():
                problems.append(f"{label}: missing {path.name}")

        if pdf_path.is_file():
            pdf = pdf_path.read_text(encoding="utf-8")
            required = (
                f'CONTACT_EMAIL = "{CONTACT}"',
                f'TAGLINE = "{TAGLINE}"',
                "yb = MB + 93",
                'f"mailto:{CONTACT_EMAIL}"',
            )
            for needle in required:
                if needle not in pdf:
                    problems.append(f"{label}/build_guide.py: missing {needle!r}")
            if not ordered(pdf, (
                'wrap_words(C.SUBTITLE, "Sans", 6.4, W)',
                '"Written and reviewed by a person. AI does the grunt work."',
                '"Set in TeX Gyre Heros and Newsreader."',
                "STAR_LABEL",
            )):
                problems.append(f"{label}/build_guide.py: colophon lines are absent or out of order")

        if docx_path.is_file():
            docx = docx_path.read_text(encoding="utf-8")
            required = (
                "_run(line, G.TAGLINE, 9, INK, False, True, SERIF)",
                'f"mailto:{address}"',
                "ruled_footer(end, G.END_FOOTER, mail=True)",
            )
            for needle in required:
                if needle not in docx:
                    problems.append(f"{label}/build_docx.py: missing {needle!r}")
            if not ordered(docx, (
                'para(doc, "Written and reviewed by a person. AI does the grunt work."',
                'para(doc, "Set in TeX Gyre Heros and Newsreader."',
            )):
                problems.append(f"{label}/build_docx.py: colophon paragraphs are absent or out of order")

        guide_path = folder / "guide.md"
        if guide_path.is_file():
            edition = next(
                (line.removeprefix("edition: ") for line in guide_path.read_text(encoding="utf-8").splitlines()
                 if line.startswith("edition: ")),
                "",
            )
            if edition.split(" · ", 1)[0] != CONTACT:
                problems.append(f"{label}/guide.md: end-page contact is not {CONTACT}")

    if problems:
        raise SystemExit("back-page problems:\n- " + "\n- ".join(problems))
    print(f"back page ok: {len(folders) - 1} guides and the template")


if __name__ == "__main__":
    main()
