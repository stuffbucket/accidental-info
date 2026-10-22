"""Tests for guide_pages.py. Run from the repo root:

    .venv/bin/python -m unittest discover -s site/scripts
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import guide_pages as gp  # noqa: E402

# Every guide's content.py has the same parse(); use one of them, so the tests read
# guide.md the way the builders do.
parse = gp.load_content("software-factories").parse

SAMPLE = """---
title: Sample
---

# One work item<br/>through a factory {#seq}

Factories where nobody reads the code have their own guide,
An Accidental Guide to: Lights-Off Software Factories.

```diagram
part Work item | Wi | tracker task
msg 1 -> 0: find ready work items
```

A closing note.

# Spec {#entry num=01 mono=Sp}

| Field | Text |
|---|---|
| Identify by | A requirements file. |

## Field marks

|  | Owned by | Lasts |
|---|---|---|
| Spec | People |  |

## Confused with: Work item

See An Accidental Guide to: Harness Engineering and An Accidental Guide to: Software Factories.

# Sources {#sources}

| Source | Date | Address |
|---|---|---|
| Someone, A page | 2026 | example.com/a |
| Team wiki | 2026 | Team wiki, Specs |
"""

PUBLISHED = {"Software Factories": "software-factories",
             "Lights-Off Software Factories": "lights-off-software-factories"}


def render(self_id="specs-and-reviews"):
    _meta, sections = parse(SAMPLE)
    return gp.render_body(sections, self_id, PUBLISHED, {(0, 0): 9})


class Headings(unittest.TestCase):
    def test_section_heading_strips_attributes_and_br(self):
        md = render()
        self.assertIn("\n## One work item through a factory\n", "\n" + md)
        self.assertNotIn("{#", md)
        self.assertNotIn("<br", md)

    def test_entry_heading_has_number(self):
        self.assertIn("\n## 01 Spec\n", render())

    def test_subheads_drop_one_level(self):
        md = render()
        self.assertIn("\n### Field marks\n", md)
        self.assertIn("\n### Confused with: Work item\n", md)


class Tables(unittest.TestCase):
    def test_table_passthrough(self):
        md = render()
        self.assertIn("| Field | Text |\n|---|---|\n| Identify by | A requirements file. |", md)

    def test_empty_cells_keep_columns(self):
        md = render()
        self.assertIn("|   | Owned by | Lasts |\n|---|---|---|\n| Spec | People |   |", md)

    def test_sources_link_web_addresses_only(self):
        md = render()
        self.assertIn("| [example.com/a](https://example.com/a) |", md)
        self.assertIn("| Team wiki, Specs |", md)


class Diagrams(unittest.TestCase):
    def test_diagram_becomes_page_image(self):
        md = render("software-factories")
        self.assertIn("![One work item through a factory]"
                      "(/accidentalguide/guides/software-factories/diagram-9.png)", md)
        self.assertNotIn("```", md)
        self.assertNotIn("msg ", md)
        # The image sits where the block was, between the two paragraphs.
        self.assertLess(md.index("have their own guide"), md.index("diagram-9.png"))
        self.assertLess(md.index("diagram-9.png"), md.index("A closing note."))

    def test_find_page_checks_title_and_labels(self):
        texts = ["cover One work item", "Wi One work item through a factory find ready work items",
                 "Other page"]
        self.assertEqual(gp.find_page(texts, "One work item<br/>through a factory",
                                      ["find ready work items"]), 2)
        with self.assertRaises(SystemExit):
            gp.find_page(texts, "One work item<br/>through a factory", ["not on the page"])
        with self.assertRaises(SystemExit):
            gp.find_page(texts, "Missing title")

    def test_diagram_labels(self):
        labels = gp.diagram_labels(["part Work item | Wi | tracker task", "band Pick up",
                                    "msg 1 -> 0: find ready work items", "note 1: stops here"])
        self.assertEqual(labels, ["Work item", "Pick up", "find ready work items", "stops here"])


QUOTED = """---
title: Sample
---

# Terms {#why}

An intro paragraph.

> | Term | Meaning |
> |---|---|
> | Spec | What you want built and why. |
>
> A grey paragraph.

# Fit {#fit}

> [!TIP]
> Check the acceptance criteria
> before the work itself.

> [!NOTE]
> A note.

> [!WARNING]
> A warning.

# Example {#example}

```skill
---
name: release-notes
---
1. Run scripts/list_changes.sh.
```
"""


def render_quoted(fences=None):
    _meta, sections = quoted_parse(QUOTED)
    return gp.render_body(sections, "specs-and-reviews", PUBLISHED, {}, None, fences)


# The '>' syntax is read by the newer content.py (Specs and Reviews and later).
quoted_parse = gp.load_content("specs-and-reviews").parse


class QuoteBlocks(unittest.TestCase):
    def test_grey_block_is_plain_markdown_in_place(self):
        md = render_quoted({(2, 0): "skill"})
        self.assertIn("An intro paragraph.\n\n| Term | Meaning |\n|---|---|\n"
                      "| Spec | What you want built and why. |\n\nA grey paragraph.\n\n## Fit", md)
        self.assertNotIn(">", md.replace("->", ""))

    def test_callouts_become_asides(self):
        md = render_quoted({(2, 0): "skill"})
        self.assertIn(":::tip\nCheck the acceptance criteria before the work itself.\n:::", md)
        self.assertIn(":::note\nA note.\n:::", md)
        self.assertIn(":::caution\nA warning.\n:::", md)
        self.assertNotIn("[!", md)

    def test_other_fenced_blocks_stay_code(self):
        md = render_quoted({(2, 0): "skill"})
        self.assertIn("```md\n---\nname: release-notes\n---\n1. Run scripts/list_changes.sh.\n```", md)
        self.assertEqual(gp.fence_langs(QUOTED), ["skill"])


class RealGuides(unittest.TestCase):
    """Every word of every guide's guide.md reaches its page, including '>' blocks."""

    def test_no_words_lost(self):
        import collections
        import json
        import re
        found = gp.built_guides()
        published = {g["title"]: g["id"] for g, _ in found if g.get("status") != "draft"}
        for g, folder in found:
            with self.subTest(guide=g["id"]):
                src = (folder / "guide.md").read_text(encoding="utf-8")
                content = gp.load_content(g["id"], folder)
                langs = iter(gp.fence_langs(src))
                pages, fences = {}, {}
                for si, s in enumerate(content.SECTIONS):
                    for di, _b in enumerate(b for b in s.blocks if b[0] == "diagram"):
                        lang = next(langs)
                        (pages.__setitem__((si, di), 1) if lang == "diagram"
                         else fences.__setitem__((si, di), lang))
                md = gp.render_body(content.SECTIONS, g["id"], published, pages, None, fences)
                md = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)
                body = src.split("\n---\n", 1)[1]
                body = re.sub(r"```diagram\n.*?```", "", body, flags=re.S)
                body = re.sub(r"^```\w+$", "```", body, flags=re.M)  # a fence's label isn't text
                body = re.sub(r"\{#[^}]*\}|<br/>|\[!(TIP|NOTE|WARNING)\]", " ", body)
                words = lambda t: collections.Counter(re.findall(r"[\w’'.,:;?()/-]+", t.replace("|", " ")))
                want, got = words(body), words(md)
                lost = {w: n - got[w] for w, n in want.items() if got[w] < n and not re.fullmatch(r"[-:]+", w)}
                self.assertEqual(lost, {})


class CrossReferences(unittest.TestCase):
    def test_published_guide_is_linked_across_a_line_break(self):
        md = render()
        self.assertIn("[An Accidental Guide to: Lights-Off Software Factories]"
                      "(/accidentalguide/guides/lights-off-software-factories/)", md)
        self.assertIn("[An Accidental Guide to: Software Factories]"
                      "(/accidentalguide/guides/software-factories/)", md)

    def test_unpublished_guide_is_left_alone(self):
        md = render()
        self.assertIn("See An Accidental Guide to: Harness Engineering and", md)

    def test_no_link_to_own_page(self):
        md = render("software-factories")
        self.assertIn("and An Accidental Guide to: Software Factories.", md)

    def test_longer_title_wins(self):
        text = gp.link_xrefs("An Accidental Guide to: Lights-Off Software Factories.", PUBLISHED)
        self.assertEqual(text, "[An Accidental Guide to: Lights-Off Software Factories]"
                               "(/accidentalguide/guides/lights-off-software-factories/).")


class Page(unittest.TestCase):
    def test_front_matter_and_download_line(self):
        _meta, sections = parse(SAMPLE)
        guide = dict(id="software-factories", title="Software Factories", subtitle="A subtitle.",
                     version="0.1.0", pages=12, pdf="software-factories.pdf",
                     docx="software-factories.docx", blurb="Another paragraph.")
        page = gp.render_page(guide, sections, 4, PUBLISHED, {(0, 0): 9})
        self.assertTrue(page.startswith('---\ntitle: "Software Factories"\n'
                                        'description: "A subtitle."\nsidebar:\n  order: 4\n---\n'))
        self.assertIn("Version 0.1.0 · 12 pages · [PDF](/accidentalguide/guides/software-factories.pdf)"
                      " · [Word](/accidentalguide/guides/software-factories.docx)", page)
        self.assertIn("\n\nAnother paragraph.\n\n## One work item", page)

    def test_sidebar_order(self):
        ids = [{"id": i} for i in ("zeta", "software-factories", "alpha", "accidental-intelligence")]
        self.assertEqual(gp.sidebar_order(ids), {"accidental-intelligence": 1, "software-factories": 2,
                                                 "alpha": 3, "zeta": 4})


if __name__ == "__main__":
    unittest.main()
