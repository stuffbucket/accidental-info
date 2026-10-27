#!/usr/bin/env python3
"""Build the print PDF of the design study.

  ~/github/stuffbucket/accidental-info/.venv/bin/python print/build.py [check-dir]

1. Makes print/print.html from ../index.html (read only): paths re-rooted to ../,
   lazy loading removed, the masthead/hero/answer wrapped as a title page,
   print/print.css linked after the page's own styles.
2. Serves design-study/ over http and prints with chrome-headless-shell.
3. Optionally rasterises every page to PNG in print/<check-dir>/.
"""
import http.server
import functools
import pathlib
import subprocess
import sys
import threading

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "accidental-guides-design-study.pdf"
CHROME = pathlib.Path.home() / "Library/Caches/ms-playwright/chromium_headless_shell-1246/chrome-headless-shell-mac-arm64/chrome-headless-shell"


def make_html():
    src = (ROOT / "index.html").read_text(encoding="utf-8")
    edits = [
        ('src="img/', 'src="../img/'),
        ('url("fonts/', 'url("../fonts/'),
        (' loading="lazy"', ''),
        ('</head>', '<link rel="stylesheet" href="print.css">\n</head>'),
        ('<header class="mast">', '<div class="title-page">\n<header class="mast">'),
        ('<!-- ============================================================ 1 -->',
         '<div class="title-foot"><span>A critique, four Swiss and Bauhaus alternatives with real sample covers, and a recommendation</span><span>01 Critique · 02 Directions · 03 Shelves · 04 Trade-offs · 05 Recommendation</span></div>\n</div>\n'
         '<!-- ============================================================ 1 -->'),
        ('<h3 style="margin-top: 56px;">At site size', '<h3 class="site-size" style="margin-top: 56px;">At site size'),
    ]
    for old, new in edits:
        if old not in src:
            sys.exit(f"build.py: pattern not found in index.html: {old!r}")
        src = src.replace(old, new)
    (HERE / "print.html").write_text(src, encoding="utf-8")


def serve():
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    http.server.SimpleHTTPRequestHandler.log_message = lambda *a, **k: None
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def render(port):
    url = f"http://127.0.0.1:{port}/print/print.html"
    cmd = [str(CHROME), "--headless", "--disable-gpu", "--hide-scrollbars",
           "--run-all-compositor-stages-before-draw", "--window-size=1440,1000", "--virtual-time-budget=15000",
           "--no-pdf-header-footer", f"--print-to-pdf={OUT}", url]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)


def rasterise(check):
    import pypdfium2 as pdfium
    d = HERE / check
    d.mkdir(exist_ok=True)
    for p in d.glob("page-*.png"):
        p.unlink()
    pdf = pdfium.PdfDocument(str(OUT))
    w, h = pdf[0].get_size()
    print(f"{len(pdf)} pages, {w / 72 * 25.4:.0f} x {h / 72 * 25.4:.0f} mm")
    for i, page in enumerate(pdf, 1):
        page.render(scale=1.1).to_pil().save(d / f"page-{i:02d}.png")


if __name__ == "__main__":
    make_html()
    httpd = serve()
    try:
        render(httpd.server_address[1])
    finally:
        httpd.shutdown()
    print("wrote", OUT)
    if len(sys.argv) > 1:
        rasterise(sys.argv[1])
