"""Build the GitHub Pages site from dist/ into _site/.

Run build.py first. This reads dist/guides.json and writes _site/index.html, which lists
each guide with its title, subtitle, version, blurb and links to its PDF and Word
document. It copies those files next to the page, renders each PDF's cover to a PNG and
copies the guides' fonts so the page is set in the same faces as the guides.
"""
import html
import json
import shutil
from pathlib import Path

import pypdfium2 as pdfium

HERE = Path(__file__).resolve().parent
DIST = HERE / "dist"
SITE = HERE / "_site"
REPO = "https://github.com/stuffbucket/accidentalguide"
FONTS = ["texgyreheros-regular.otf", "texgyreheros-bold.otf", "texgyreheros-italic.otf",
         "LiberationMono-Regular.ttf"]

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Accidental Guides</title>
<meta name="description" content="Short guides to how the AI systems we work with are put together.">
<style>
@font-face {{ font-family: "Heros"; src: url("fonts/texgyreheros-regular.otf"); }}
@font-face {{ font-family: "Heros"; src: url("fonts/texgyreheros-bold.otf"); font-weight: bold; }}
@font-face {{ font-family: "Heros"; src: url("fonts/texgyreheros-italic.otf"); font-style: italic; }}
@font-face {{ font-family: "Mono"; src: url("fonts/LiberationMono-Regular.ttf"); }}
:root {{ --ink: #111111; --grey: #5f5f5f; --hair: #bdbdbd; --paper: #ffffff; }}
@media (prefers-color-scheme: dark) {{
  :root {{ --ink: #ececec; --grey: #a3a3a3; --hair: #4a4a4a; --paper: #161616; }}
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--paper); color: var(--ink);
  font: 16px/1.5 "Heros", "Helvetica Neue", Helvetica, Arial, sans-serif; }}
main {{ max-width: 46rem; margin: 0 auto; padding: 3rem 1rem 4rem; }}
.kicker {{ font-weight: bold; font-size: .85rem; margin: 0; }}
h1 {{ font-size: 2.4rem; line-height: 1.1; margin: .3rem 0 .8rem; }}
.lead {{ color: var(--grey); margin: 0 0 2.5rem; max-width: 34rem; }}
article {{ display: grid; grid-template-columns: 9rem minmax(0, 1fr); gap: 1.5rem;
  border-top: 1px solid var(--ink); padding: 1.5rem 0 2rem; }}
article img {{ width: 100%; height: auto; border: 1px solid var(--hair); display: block; }}
h2 {{ font-size: 1.35rem; line-height: 1.2; margin: .15rem 0 .35rem; }}
.subtitle {{ color: var(--grey); margin: 0 0 .75rem; }}
.blurb {{ margin: 0 0 .9rem; }}
.meta {{ font-family: "Mono", ui-monospace, Menlo, monospace; font-size: .78rem;
  color: var(--grey); margin: 0 0 .9rem; }}
.links a {{ display: inline-block; margin-right: 1rem; color: var(--ink); font-weight: bold;
  text-decoration: none; border-bottom: 1px solid var(--hair); }}
.links a:hover {{ border-color: var(--ink); }}
footer {{ border-top: 1px solid var(--ink); padding-top: .8rem; font-size: .8rem; color: var(--grey); }}
footer a {{ color: var(--grey); }}
@media (max-width: 34rem) {{
  h1 {{ font-size: 1.9rem; }}
  article {{ grid-template-columns: 5.5rem minmax(0, 1fr); gap: 1rem; }}
}}
</style>
</head>
<body>
<main>
<p class="kicker">An Accidental Guide to…</p>
<h1>Accidental Guides</h1>
<p class="lead">Short guides to how the AI systems we work with are put together. Each one
comes as a PDF and as a Word document.</p>
{guides}
<footer>Built from <a href="{repo}">{repo_short}</a>.</footer>
</main>
</body>
</html>
"""

GUIDE = """<article id="{id}">
<a href="{pdf}"><img src="{cover}" alt="Cover of {title}" width="{w}" height="{h}" loading="lazy"></a>
<div>
<h2>{title}</h2>
<p class="subtitle">{subtitle}</p>
<p class="blurb">{blurb}</p>
<p class="meta">Version {version} · {pages} pages</p>
<p class="links"><a href="{pdf}">PDF</a>{word}</p>
</div>
</article>"""


def cover(pdf, png):
    """Render the PDF's first page to png and return its size."""
    doc = pdfium.PdfDocument(pdf)
    image = doc[0].render(scale=2).to_pil()
    image.save(png, optimize=True)
    doc.close()
    return image.size


def main():
    guides = json.loads((DIST / "guides.json").read_text())
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "fonts").mkdir(parents=True)
    fonts = HERE / "guides" / guides[0]["id"] / "fonts"
    for name in FONTS:
        shutil.copy(fonts / name, SITE / "fonts" / name)
    shutil.copytree(fonts / "licenses", SITE / "fonts" / "licenses")
    shutil.copy(DIST / "guides.json", SITE / "guides.json")
    items = []
    for g in guides:
        shutil.copy(DIST / g["pdf"], SITE / g["pdf"])
        if g["docx"]:
            shutil.copy(DIST / g["docx"], SITE / g["docx"])
        png = f"{g['id']}.png"
        w, h = cover(DIST / g["pdf"], SITE / png)
        e = {k: html.escape(str(v)) for k, v in g.items()}
        items.append(GUIDE.format(
            **e, cover=png, w=w // 2, h=h // 2,
            word=f'<a href="{e["docx"]}">Word</a>' if g["docx"] else ""))
    (SITE / "index.html").write_text(PAGE.format(
        guides="\n".join(items), repo=REPO, repo_short=REPO.removeprefix("https://")))
    (SITE / ".nojekyll").write_text("")
    print(f"wrote {SITE / 'index.html'}: {len(guides)} guides")


if __name__ == "__main__":
    main()
