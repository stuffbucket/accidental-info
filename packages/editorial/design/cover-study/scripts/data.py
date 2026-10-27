"""Read guide data from the repo (read-only) into data.json for the mockups."""
import json, os, re, glob
REPO = os.path.expanduser("~/github/stuffbucket/accidental-info")
HERE = os.path.dirname(os.path.abspath(__file__))

def guide_dir(slug):
    for base in ("guides", "drafts"):
        d = f"{REPO}/{base}/{slug}"
        if os.path.isdir(d):
            return d

def load(slug):
    d = guide_dir(slug)
    meta = json.load(open(f"{d}/dist/guide.json"))
    src = open(f"{d}/build_guide.py").read()
    fam = {}
    m = re.search(r"PART_FAMILY = (\{.*?\})", src, re.S)
    if m:
        fam = eval(m.group(1))
    lines = re.search(r"COVER_LINES = (\(.*?\))", src, re.S)
    # Older builders have no COVER_LINES; these are the lines their covers print.
    cover_lines = list(eval(lines.group(1))) if lines else {
        "agents-harnesses-skills-tools": ["Agents", "Harnesses", "Skills and Tools"],
        "software-factories": ["Software", "Factories"],
        "claude-code": ["Claude Code"], "claude-desktop": ["Claude", "Desktop"],
    }.get(slug, [meta["title"]])
    parts = []
    for num, mono, name in [(m.group(2), m.group(3), m.group(1)) for m in
                            re.finditer(r"^# (.+?) \{#entry num=(\d+) mono=(\w+)\}", open(f"{d}/guide.md").read(), re.M)]:
        parts.append(dict(num=num, key=mono, name=name, family=fam.get(mono)))
    import pypdfium2 as pdfium
    pdf = pdfium.PdfDocument(f"{d}/dist/{slug}.pdf")
    txt = pdf[0].get_textpage().get_text_range()
    pages = re.findall(r"^page (\d+)", txt, re.M)
    for part, pg in zip(parts, pages):
        part["page"] = int(pg)
    return dict(slug=slug, title=meta["title"], lines=cover_lines, subtitle=meta["subtitle"],
                version=meta["version"], status=meta.get("status", "published"), parts=parts)

def main():
    coll = json.load(open(f"{REPO}/site/src/data/collections.json"))["collections"]
    reg = json.load(open(f"{REPO}/packages/editorial/registry.json"))
    global CODE_FAMILY
    CODE_FAMILY = {x["code"]: x["family"] for x in reg["concepts"]}
    out = dict(families=reg["families"], collections=[], guides={})
    for c in coll:
        slugs = [(c["catalog"], None)] if c.get("catalog") else []
        for g in c.get("groups", []):
            for s in g["guides"]:
                slugs.append((s, g["name"]))
        for s in c.get("guides", []):
            slugs.append((s, None))
        for s in c.get("coming", []):
            slugs.append((s["id"], None))
        out["collections"].append(dict(id=c["id"], name=c["name"], line=c["line"], code=c["code"],
                                       guides=[s for s, _ in slugs]))
        for i, (s, grp) in enumerate(slugs):
            if guide_dir(s):
                g = load(s); g.update(collection=c["id"], group=grp, number=i if c.get("catalog") else i + 1)
                for part in g["parts"]:
                    part["family"] = part["family"] or CODE_FAMILY.get(part["key"])
                out["guides"][s] = g
    cat = out["guides"]["accidental-intelligence"]
    counts = {"Ru": 7, "Wr": 6, "Ck": 7, "Us": 4, "Dm": 5, "Nu": 7}  # as printed on the catalog cover
    cat["parts"] = [dict(num=f"{i+1:02d}", key=f["key"], name=f["name"], family=f["key"], count=counts[f["key"]])
                    for i, f in enumerate(reg["families"])]
    cat["number"] = 0
    json.dump(out, open(f"{HERE}/data.json", "w"), indent=1, ensure_ascii=False)
    for s, g in out["guides"].items():
        print(g["collection"], g["number"], s, [(p["key"], p["family"]) for p in g["parts"]])

main()
