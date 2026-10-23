#!/usr/bin/env python3
"""Check a guide.md for the patterns the Accidental Guides don't allow.

Usage:
  lint_guide.py GUIDE [--deny FILE ...] [--no-deny] [--strict] [--skip CODE,CODE] [--list]

GUIDE is a guide.md, a guide folder, or a slug (looked up in drafts/ and then guides/ at the
repository root).

Prints one line per finding, with its line number:

  guide.md:23: error SN "this guide": ...the text around it...

Errors are rule breaks. Warnings are things a person has to read and decide. The script
can't judge flow, tone or whether a sentence builds on the last one; read the pages too.

The deny list is a file of names that must never appear in a guide, one per line (#
starts a comment): non-public product, team and project names. It lives outside any
repository and is never committed. The lint reads, in this order:

  ACCIDENTAL_GUIDE_DENYLIST   if set, one or more paths separated by colons; set it to an
                              empty string to read none
  otherwise                   ~/.config/accidental-guides/denylist.txt, if it exists

--deny FILE   read this deny list too. Can be given more than once.
--no-deny     read no deny list, only the --deny files given.
--strict      exit 1 on warnings as well as errors.
--skip        leave out these codes, such as --skip PQ,QQ.
--list        print the codes and what each one checks, then exit.

Exit status: 0 clean, 1 findings that fail (errors, or any finding with --strict).
Standard library only.
"""
import argparse
import os
import re
import sys
from pathlib import Path

DEFAULT_DENYLIST = Path.home() / ".config" / "accidental-guides" / "denylist.txt"

CODES = {
    "FM": "front matter: required keys, kicker, semver version, title length",
    "MD": "Markdown the builders print literally: backticks, emphasis, list lines, & before letters, <",
    "PU": "punctuation: em dashes, spaced en dashes, semicolons, exclamation marks, straight quotes",
    "SN": "self-narration and stage direction: this guide, this page, below, let's, here's",
    "UV": "unnamed voices: speakers mean, people say, some say",
    "MP": "mannered prose markers: not X but Y, rather than, inflated words, stiff subjects, fragments",
    "EQ": "embedded question phrases: what a factory is, how a gate works",
    "RQ": "questions in body paragraphs (rhetorical questions are banned; plain ones in tables are fine)",
    "RS": "a row or table cell sentence that starts with It, Its, They, This or These",
    "BF": "borrowed framing: birds, species, field guide, travel, video",
    "XR": "cross-references: the colon form in the body, the ellipsis form only on the cover",
    "PQ": "people and quotes: name-checks, 'according to', long quoted passages (not in sources)",
    "CL": "claims about what most teams or people do",
    "IN": "internal names from the deny list, and words such as confidential",
}

ERROR, WARN = "error", "warning"
I = re.I

# (code, severity, pattern, flags, message). Patterns run on body text, one line at a time.
RULES = [
    ("MD", ERROR, r"`", 0, "backtick: the builders print it literally"),
    ("MD", ERROR, r"\*\*|(?<![\w*])\*(?=\w)", 0, "emphasis marker: bold and mono are applied by rule"),
    ("MD", ERROR, r"&(?=[A-Za-z])", 0, "& before a letter: ReportLab reads it as an entity; write 'and'"),
    ("PU", ERROR, r"—|\s--\s", 0, "em dash: use two sentences or a comma"),
    ("PU", ERROR, r"\s–\s", 0, "spaced en dash used as a dash: use two sentences or a comma"),
    ("PU", ERROR, r";", 0, "semicolon: use two sentences"),
    ("PU", ERROR, r"!(?!\[)", 0, "exclamation mark"),
    ("PU", WARN, r"(?<![\w=])\"|(?<=\s)'|^'", 0, "straight quote: use typographic quotes (’ “ ”)"),
    ("SN", ERROR, r"\bthis (guide|page|section|series|table|diagram|chapter|book)\b", I, "self-narration"),
    ("SN", ERROR, r"\b(the|our) series\b|\bthe guide (says|uses|covers|calls)\b", I, "self-narration"),
    ("SN", ERROR, r"\bas (noted|mentioned|shown|described|discussed) (above|below|earlier|before)\b", I, "stage direction"),
    ("SN", WARN, r"\b(below|above|later in|next page|previous page)\b", I, "stage direction? point to the thing by name"),
    ("SN", ERROR, r"\blet[’']s\b|\bhere[’']s\b|\bnow that\b|\bwe[’']ll\b|\bwe will\b", I, "stage direction"),
    ("SN", WARN, r"\bon page \d+|\bpage \d+\b", I, "page number typed by hand: check it against the built PDF"),
    ("UV", ERROR, r"\bspeakers\b|\bpeople say\b|\bsome say\b|\bthey say\b|\bit is said\b|\bmany argue\b", I, "unnamed voice"),
    ("MP", ERROR, r"\bnot (just|only|merely|simply)\b", I, "'not just X' flourish"),
    ("MP", WARN, r"\bnot\b[^.?!:]{1,40}?,? but\b", I, "'not X but Y'? say what it is"),
    ("MP", WARN, r"\brather than\b|\binstead of\b", I, "contrast: keep only if it corrects a real misreading, once"),
    ("MP", ERROR, r"\b(simply|easily|really|actually|powerful|crucial|leverage[sd]?|unlock(s|ed)?|seamless(ly)?|robust|game-changer|delve|testament|supercharge|cutting-edge|world-class)\b", I, "inflated or filler word"),
    ("MP", WARN, r"\b(just|important|key|landscape|journey)\b", I, "filler word? ('key' is fine in 'API key', 'journey' in 'user journey')"),
    ("MP", ERROR, r"\bnote that\b|\bit[’']s worth (noting|mentioning)\b|\bat its core\b|\bhere[’']s the thing\b|\blet that sink in\b|\bin a nutshell\b|\bthe bottom line\b|\bmake no mistake\b", I, "throat-clearing"),
    ("MP", ERROR, r"\ba person (can|may|should|must)\b|\bone (may|might|can|should|must)\b", I, "stiff generic subject: say 'you' or name who does it"),
    ("MP", WARN, r"\b(a|the) (team|user|developer|reader) (can|may|should|must)\b", I, "stiff generic subject? fine in an example, otherwise say 'you'"),
    ("MP", WARN, r"\bthe (result|answer|catch|twist|point|truth|secret|upshot)\b:", I, "colon reveal"),
    ("EQ", ERROR, r"\b(what|how|why|where|when) (a|an|the|your) [\w’' -]{1,40}? (is|are|works|means)\s*[.,?]", I, "embedded question: ask it plainly ('What is a software factory?')"),
    ("BF", ERROR, r"\b(birds?|birder|birding|species|field guide|sightings?|in the wild|habitat|plumage|lonely planet|youtube|episode|viewers|subscribe)\b", I, "borrowed framing: the form model is for structure and pacing only"),
    ("BF", WARN, r"\b(travel(s|ler|ers|ing)?|passport|itinerary|tourist|guidebook)\b", I, "borrowed framing?"),
    ("XR", ERROR, r"Accidental Guide to…|Accidental Guide to\.\.\.", 0, "the ellipsis form belongs on the cover; in the body write 'An Accidental Guide to: Title'"),
    ("XR", ERROR, r"Accidental Guide to (?!:)", 0, "cross-reference without the colon: 'An Accidental Guide to: Title'"),
    ("CL", WARN, r"\bmost (teams|people|companies|developers|engineers|organi[sz]ations)\b", I, "claim about what most do: say which group the guide is about"),
    ("IN", ERROR, r"\b(confidential|internal\s+(only|use)|do not share|not for distribution)\b", I, "marked non-public"),
]

# Only outside the sources section: sources may name authors and quote titles.
PEOPLE_RULES = [
    ("PQ", WARN, r"\b[A-Z][a-z]+ [A-Z][a-z]+(’s)? (says|said|calls|called|wrote|coined|argues|argued|told|tweeted|posted)\b", 0, "name-check of a person: keep the idea, drop the name"),
    ("PQ", WARN, r"\baccording to\b|\bin (his|her|their) words\b", I, "attribution in the body: sources go in the appendix"),
    ("PQ", WARN, r"“[^”]*(\s\S+){5,}[^”]*”", 0, "long quoted passage: no direct quotes in the body"),
]

ROW_START = re.compile(r"^(It|Its|It’s|They|Their|This|These)\b")
HEADING = re.compile(r"^# (.*?) \{#([\w-]+)[^}]*\}\s*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?(\+[0-9A-Za-z.-]+)?$")
REQUIRED = ("title", "kicker", "subtitle", "running_footer", "edition", "cover_footer", "collection",
            "collection_mark", "number", "version")


def load_deny(paths):
    terms = []
    for p in paths:
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.split("#", 1)[0].strip()
                if line:
                    terms.append(line)
    return [(t, re.compile(r"(?<![\w.])" + re.escape(t) + r"(?![\w])", re.I)) for t in terms]


def deny_list_paths(extra, use_default):
    paths = list(extra)
    if not use_default:
        return paths
    env = os.environ.get("ACCIDENTAL_GUIDE_DENYLIST")
    if env is not None:
        return paths + [p for p in env.split(":") if p]
    if DEFAULT_DENYLIST.is_file():
        paths.append(str(DEFAULT_DENYLIST))
    return paths


def guide_path(arg):
    p = Path(arg)
    if p.is_file():
        return str(p)
    if (p / "guide.md").is_file():
        return str(p / "guide.md")
    for start in (Path(__file__).resolve().parent, Path.cwd()):
        for d in (start, *start.parents):
            if (d / "packages" / "pipeline" / "guide.py").is_file():
                for kind in ("drafts", "guides"):
                    if (d / kind / arg / "guide.md").is_file():
                        return str(d / kind / arg / "guide.md")
    sys.exit(f"no guide.md for {arg!r}: give a guide.md, a guide folder or a slug")


def sentences(text):
    return [s for s in re.split(r"(?<=[.?!])\s+", text.strip()) if s]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("guide", nargs="?")
    ap.add_argument("--deny", action="append", default=[])
    ap.add_argument("--no-deny", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--skip", default="")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    if args.list:
        for code, what in CODES.items():
            print(f"{code}  {what}")
        return
    if not args.guide:
        ap.error("give the path to guide.md")

    args.guide = guide_path(args.guide)
    skip = {c.strip().upper() for c in args.skip.split(",") if c.strip()}
    deny = load_deny(deny_list_paths(args.deny, not args.no_deny))
    rules = [(c, s, re.compile(p, f), m) for c, s, p, f, m in RULES]
    people = [(c, s, re.compile(p, f), m) for c, s, p, f, m in PEOPLE_RULES]

    lines = open(args.guide, encoding="utf-8").read().split("\n")
    findings = []

    def add(n, code, sev, msg, text, span=None):
        if code in skip:
            return
        if span:
            a, b = max(0, span[0] - 30), min(len(text), span[1] + 30)
            excerpt = ("…" if a else "") + text[a:b].strip() + ("…" if b < len(text) else "")
        else:
            excerpt = text.strip()[:90]
        findings.append((n, sev, code, msg, excerpt))

    # Front matter.
    start = 0
    meta = {}
    if not lines or lines[0] != "---":
        add(1, "FM", ERROR, "guide.md must start with --- on line 1", lines[0] if lines else "")
    else:
        for i in range(1, len(lines)):
            if lines[i] == "---":
                start = i + 1
                break
            key, _, value = lines[i].partition(":")
            meta[key.strip()] = (value.strip(), i + 1)
        for key in REQUIRED:
            if key not in meta:
                add(1, "FM", ERROR, f"front matter has no {key}:", "")
        if "kicker" in meta and meta["kicker"][0] != "An Accidental Guide to…":
            add(meta["kicker"][1], "FM", ERROR, "kicker should be 'An Accidental Guide to…' (with the … character)", meta["kicker"][0])
        if "version" in meta and not SEMVER.match(meta["version"][0]):
            add(meta["version"][1], "FM", ERROR, "version must be semver, such as 0.1.0", meta["version"][0])
        if "title" in meta and len(meta["title"][0].split()) > 6:
            add(meta["title"][1], "FM", WARN, "title has more than six words: keep it short and balanced", meta["title"][0])
        for key, (value, n) in meta.items():
            if "—" in value or ";" in value:
                add(n, "PU", ERROR, "em dash or semicolon in front matter", value)
            for term, rx in deny:
                if rx.search(value):
                    add(n, "IN", ERROR, f"internal name {term!r}", value)

    # Split the body into units: a heading, a table row, a diagram line, or a paragraph
    # (text lines up to a blank line, joined with spaces, as the parser joins them). Each
    # unit keeps the line each piece came from, so findings point at the right line.
    units = []  # (kind, section, header_row, [(line_no, text)])
    section, in_fence, para = None, False, []

    def flush():
        nonlocal para
        if para:
            units.append(("p", section, False, para))
            para = []

    for idx in range(start, len(lines)):
        n, raw = idx + 1, lines[idx]
        if raw.startswith("```"):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            units.append(("diagram", section, False, [(n, raw)]))
            continue
        text = re.sub(r"^>\s?", "", raw) if raw.startswith(">") else raw
        if not text.strip() or re.match(r"^\[!(TIP|NOTE|WARNING)\]\s*$", text):
            flush()
            continue
        m = HEADING.match(text)
        if m or text.startswith("# ") or text.startswith("## "):
            flush()
            if m:
                section = m.group(2)
            elif text.startswith("# "):
                add(n, "MD", ERROR, "a # line without {#id} is printed as text, or breaks the parser", text)
            units.append(("heading", section, False, [(n, text)]))
            continue
        if text.lstrip().startswith("|"):
            flush()
            if re.fullmatch(r"\s*\|?[\s:|-]+\|?\s*", text):
                continue
            nxt = re.sub(r"^>\s?", "", lines[idx + 1]) if idx + 1 < len(lines) else ""
            header = bool(re.fullmatch(r"\s*\|[\s:|-]+\|?\s*", nxt))
            units.append(("row", section, header, [(n, text)]))
            continue
        if re.match(r"^\s*([-*+]|\d+\.)\s", text):
            add(n, "MD", ERROR, "list line: printed as part of a paragraph; use a table or sentences", text)
        para.append((n, text.strip()))
    flush()

    for kind, sec, header, parts in units:
        body = " ".join(t for _, t in parts)
        starts, pos = [], 0
        for ln, t in parts:
            starts.append((pos, ln))
            pos += len(t) + 1

        def line_at(i):
            return [ln for p, ln in starts if p <= i][-1]

        def hit(code, sev, msg, span, text=body):
            add(line_at(span[0]), code, sev, msg, text, span)

        for term, rx in deny:
            for h in rx.finditer(body):
                hit("IN", ERROR, f"internal name {term!r}", h.span())
        if kind == "diagram":
            # Diagram data: only the labels are prose, so check dashes and semicolons.
            for h in re.finditer(r"—|;", body):
                hit("PU", ERROR, "em dash or semicolon in a diagram label", h.span())
            continue

        for h in re.finditer(r"<(?!br/>)", body):
            hit("MD", ERROR, "'<' outside <br/>", h.span())
        if "<br/>" in body and kind != "heading":
            hit("MD", WARN, "<br/> outside a # title: the Word document prints it", (body.index("<br/>"), body.index("<br/>") + 5))

        for code, sev, rx, msg in rules:
            for h in rx.finditer(body):
                hit(code, sev, msg, h.span())
        if sec != "sources":
            for code, sev, rx, msg in people:
                for h in rx.finditer(body):
                    hit(code, sev, msg, h.span())

        if kind == "row" and not header:
            cells = [c.strip() for c in body.strip().strip("|").split("|")]
            for cell in cells[1:]:
                if any(ROW_START.match(s) for s in sentences(cell)):
                    add(parts[0][0], "RS", ERROR, "row sentence starts with a pronoun: name the subject", cell)
        if kind == "p" and sec != "sources":
            for s in sentences(body):
                at = body.find(s)
                if s.endswith("?"):
                    add(line_at(at), "RQ", WARN, "question in a paragraph: rhetorical questions are banned", s)
                if len(s.rstrip(".").split()) <= 2 and s.endswith("."):
                    add(line_at(at), "MP", WARN, "sentence fragment: drama fragments are banned", s)

    findings = sorted(set(findings))
    for n, sev, code, msg, excerpt in findings:
        print(f"{args.guide}:{n}: {sev} {code} {msg}: {excerpt}")
    errors = sum(1 for f in findings if f[1] == ERROR)
    warns = len(findings) - errors
    print(f"{errors} errors, {warns} warnings" + ("" if deny else " (no deny list found, so internal names weren't checked)"))
    if errors or (args.strict and warns):
        sys.exit(1)


if __name__ == "__main__":
    main()
