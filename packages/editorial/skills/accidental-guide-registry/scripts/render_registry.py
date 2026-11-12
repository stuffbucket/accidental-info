#!/usr/bin/env python3
"""Render the concept table in registry.md from registry.json."""
import argparse
import json
from pathlib import Path

START = "<!-- registry:concepts:start -->"
END = "<!-- registry:concepts:end -->"


def repo_root(start: Path) -> Path:
    for path in (start, *start.parents):
        if (path / "packages/editorial/registry.json").is_file():
            return path
    raise SystemExit("cannot find the repository root")


def appearance_text(concept: dict) -> str:
    out = []
    owner = concept.get("owner")
    for item in concept.get("appears_in", []):
        if item.get("guide") == owner and item.get("role") == "owner":
            continue
        text = item["guide"]
        if item.get("entry") and item["entry"] != concept["concept"]:
            text += f' ("{item["entry"]}")'
        if item.get("tile") == "outlined":
            text += " (outlined)"
        out.append(text)
    return ", ".join(out) if out else "—"


def render(data: dict) -> str:
    rows = [
        START,
        "| Concept | Code | Family | Color | Hex | Owner | Appears in |",
        "|---|---|---|---|---|---|---|",
    ]
    for concept in data["concepts"]:
        owner = concept.get("owner") or "none yet"
        rows.append(
            f'| {concept["concept"]} | `{concept["code"]}` | {concept["family"]} | '
            f'{concept["color"]} | `{concept["hex"]}` | {owner} | {appearance_text(concept)} |'
        )
    rows.append(END)
    return "\n".join(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve() if args.root else repo_root(Path(__file__).resolve())
    json_path = root / "packages/editorial/registry.json"
    md_path = root / "packages/editorial/registry.md"
    data = json.loads(json_path.read_text(encoding="utf-8"))
    text = md_path.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit("registry.md has no generated concept-table markers")
    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    wanted = before + render(data) + after
    if args.check:
        if text != wanted:
            raise SystemExit("registry.md is stale; run render_registry.py")
        print("registry.md matches registry.json")
        return
    md_path.write_text(wanted, encoding="utf-8")
    print("wrote packages/editorial/registry.md")


if __name__ == "__main__":
    main()
