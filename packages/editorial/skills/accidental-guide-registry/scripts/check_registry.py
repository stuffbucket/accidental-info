#!/usr/bin/env python3
"""Validate the canonical concept registry and its recorded guide appearances."""
import argparse
import json
import re
from pathlib import Path

CODE = re.compile(r"^[A-Z][a-z0-9]$")
ENTRY = re.compile(r"^# (.*?) \{#entry\s+([^}]*)\}$", re.M)


def repo_root(start: Path) -> Path:
    for path in (start, *start.parents):
        if (path / "packages/editorial/registry.json").is_file():
            return path
    raise SystemExit("cannot find the repository root")


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path)
    args = parser.parse_args()
    root = args.root.resolve() if args.root else repo_root(Path(__file__).resolve())
    path = root / "packages/editorial/registry.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    problems: list[str] = []

    families = {family.get("key"): family for family in data.get("families", [])}
    if len(families) != len(data.get("families", [])):
        problems.append("family keys are not unique")
    for key, family in families.items():
        if not CODE.fullmatch(key or ""):
            problems.append(f"invalid family code {key!r}")
        for field in ("name", "color", "token", "hex"):
            if not family.get(field):
                problems.append(f"family {key}: missing {field}")

    used: dict[str, str] = {code: f"reserved family code ({reason})" for code, reason in data.get("reserved_codes", {}).items()}
    names: dict[str, str] = {}
    appearances: dict[tuple[str, str], list[dict]] = {}
    registered_guides: set[str] = set()
    for concept in data.get("concepts", []):
        name, code, family_key = concept.get("concept", ""), concept.get("code", ""), concept.get("family", "")
        normalized = norm(name)
        if not normalized:
            problems.append("concept without a name")
        elif normalized in names:
            problems.append(f"concept names collide after normalization: {names[normalized]!r} and {name!r}")
        else:
            names[normalized] = name
        if not CODE.fullmatch(code):
            problems.append(f"{name}: invalid code {code!r}")
        elif code in used:
            problems.append(f"{name}: code {code} already belongs to {used[code]}")
        else:
            used[code] = name
        family = families.get(family_key)
        if not family:
            problems.append(f"{name}: unknown family {family_key!r}")
        else:
            for field, source in (("family_name", "name"), ("color", "color"), ("token", "token"), ("hex", "hex")):
                if concept.get(field) != family.get(source):
                    problems.append(f"{name}: {field} disagrees with family {family_key}")
        owner = concept.get("owner")
        owner_roles = 0
        seen_here: set[tuple[str, str]] = set()
        for appearance in concept.get("appears_in", []):
            guide, entry = appearance.get("guide", ""), appearance.get("entry", "")
            pair = (guide, entry)
            if not guide or not entry:
                problems.append(f"{name}: appearance needs guide and entry")
            if pair in seen_here:
                problems.append(f"{name}: duplicate appearance {guide}/{entry}")
            seen_here.add(pair)
            role = appearance.get("role")
            if role not in ("owner", "reference"):
                problems.append(f"{name}: {guide}/{entry} has invalid role {role!r}")
            if role == "owner":
                owner_roles += 1
                if owner != guide:
                    problems.append(f"{name}: owner appearance is in {guide}, not owner {owner}")
            code_now = appearance.get("code_now")
            if code_now is not None and not CODE.fullmatch(code_now):
                problems.append(f"{name}: {guide}/{entry} has invalid current code {code_now!r}")
            appearances.setdefault(pair, []).append({"concept": name, **appearance})
            registered_guides.add(guide)
        if owner_roles > 1:
            problems.append(f"{name}: more than one owner appearance")

    # Every tiled entry in a guide or draft must be recorded with its current code. Planned
    # appearances may remain in the registry before their guide folder exists.
    for state in ("guides", "drafts"):
        for guide in (root / state).iterdir():
            source = guide / "guide.md"
            if not source.is_file() or guide.name not in registered_guides:
                continue
            for match in ENTRY.finditer(source.read_text(encoding="utf-8")):
                entry, attrs = match.groups()
                values = dict(item.split("=", 1) for item in attrs.split() if "=" in item)
                code = values.get("mono")
                if not code:
                    continue
                candidates = appearances.get((guide.name, entry), [])
                if not any(item.get("code_now") == code for item in candidates):
                    problems.append(f"{guide.name}/{entry}: tile {code} is not recorded in registry.json")

    if problems:
        raise SystemExit("registry problems:\n- " + "\n- ".join(problems))
    print(f"registry ok: {len(data['concepts'])} concepts, {len(families)} families, {len(used)} reserved or assigned codes")


if __name__ == "__main__":
    main()
