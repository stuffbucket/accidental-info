"""Render the piece specimen sheet, and write the pieces as SVG.

    python specimen.py [out.png]     (default: specimen.png next to this file)

The sheet shows every piece, both colours, on light and dark squares, at several square
sizes, then two small boards of the starting position (White's side and Black's side). It
also writes pieces/*.svg from the same geometry.
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import chessdiagram as cd  # noqa: E402

from reportlab.pdfgen import canvas  # noqa: E402
from reportlab.pdfbase import pdfmetrics  # noqa: E402
from reportlab.pdfbase.ttfonts import TTFont  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
FONT = os.path.join(ROOT, "drafts", "chess-first-move", "fonts", "heros-regular.ttf")
FONTB = os.path.join(ROOT, "drafts", "chess-first-move", "fonts", "heros-bold.ttf")


def fonts():
    if os.path.exists(FONT):
        pdfmetrics.registerFont(TTFont("Sans", FONT))
        pdfmetrics.registerFont(TTFont("Sans-Bold", FONTB))
        return "Sans", "Sans-Bold"
    return "Helvetica", "Helvetica-Bold"


def sheet(c, W, H):
    reg, bold = fonts()
    c.setFillColor(cd._color("#ffffff")); c.rect(0, 0, W, H, stroke=0, fill=1)
    x0, y = 28, H - 30
    c.setFillColor(cd._color(cd.INK)); c.setFont(bold, 13)
    c.drawString(x0, y, "Accidental Guides chess pieces")
    y -= 14
    c.setFont(reg, 7); c.setFillColor(cd._color(cd.COORD))
    c.drawString(x0, y, "King, queen, rook, bishop, knight, pawn. White and Black, on light and dark squares, "
                        "at each square size.")
    y -= 14
    order = "KQRBNP"
    for sq in (64, 36, 22, 14, 12):
        c.setFillColor(cd._color(cd.INK)); c.setFont(bold, 7)
        c.drawString(x0, y - 8, f"{sq} pt square")
        y -= 14
        for white in (True, False):
            x = x0
            for light in (True, False):
                for ch in order:
                    c.setFillColor(cd._color(cd.LIGHT_SQ if light else cd.DARK_SQ))
                    c.rect(x, y - sq, sq, sq, stroke=0, fill=1)
                    cd.draw_piece(c, ch if white else ch.lower(), x, y - sq, sq)
                    x += sq
                x += max(8, sq * 0.3)
            y -= sq + 4
        y -= 14
    # boards
    size = 12 * 8
    b1 = cd.draw_board(c, x0 + 10, y - size, size, side="white", tints={s: "Us" for s in ("d4", "d5", "e4", "e5")})
    cd.draw_board(c, x0 + 10 + size + 40, y - size, size, side="black", tints={s: "Us" for s in ("d4", "d5", "e4", "e5")})
    size2 = 14 * 8
    fen = cd.play("1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6")
    cd.draw_board(c, x0 + 10 + 2 * (size + 40), y - size2, size2, fen=fen, arrows=[("f3", "g5")])
    return b1


def main(out):
    W, H = 860, 700
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(W, H), invariant=1)
    sheet(c, W, H)
    c.showPage(); c.save()
    pdf_path = os.path.splitext(out)[0] + ".pdf"
    with open(pdf_path, "wb") as fh:
        fh.write(buf.getvalue())
    import pypdfium2 as pdfium
    doc = pdfium.PdfDocument(pdf_path)
    doc[0].render(scale=3).to_pil().save(out)
    doc.close()
    cd.export_svg(os.path.join(HERE, "pieces"))
    print(f"wrote {out} and {pdf_path}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "specimen.png"))
