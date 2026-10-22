"""Tests for chessdiagram: run with the repository's virtualenv.

    ../../.venv/bin/python test_chessdiagram.py
"""
import hashlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import chessdiagram as cd  # noqa: E402

from reportlab.pdfgen import canvas  # noqa: E402


def render():
    """The starting position from White's side and from Black's side, on one page."""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(324, 200), invariant=1)
    center = {s: "Us" for s in ("d4", "d5", "e4", "e5")}
    a = cd.draw_board(c, 24, 30, 128, side="white", tints=center)
    b = cd.draw_board(c, 176, 30, 128, side="black", tints=center, arrows=[("e7", "e5")])
    c.showPage(); c.save()
    return buf.getvalue(), a, b


def test_both_sides():
    data, a, b = render()
    assert data.startswith(b"%PDF"), "not a PDF"
    assert a.board == (24, 30, 128) and b.board == (176, 30, 128)
    assert a.x0 < 24 and a.y0 < 30, "the labels sit left of and under the board"


def test_deterministic():
    one, two = render()[0], render()[0]
    assert hashlib.sha256(one).hexdigest() == hashlib.sha256(two).hexdigest(), "PDF differs between runs"


def test_flip():
    # a1 is lower-left from White's side and upper-right from Black's
    assert cd.square_xy("a1", 0, 0, 80, "white") == (0, 0)
    assert cd.square_xy("a1", 0, 0, 80, "black") == (70, 70)
    assert cd.square_xy("h8", 0, 0, 80, "black") == (0, 0)


def test_moves():
    assert cd.play([]) == cd.START
    assert cd.play("1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6") == \
        "r1bqkb1r/1ppp1ppp/p1n2n2/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R"
    assert cd.play("1.d4 d5 2.c4 dxc4 3.e4 b5 4.a4 c6") == \
        "rnbqkbnr/p3pppp/2p5/1p6/P1pPP3/8/1P3PPP/RNBQKBNR"
    # en passant, then castling
    fen = cd.play("1.e4 Nf6 2.e5 d5 3.exd6")
    assert fen == "rnbqkb1r/ppp1pppp/3P1n2/8/8/8/PPPP1PPP/RNBQKBNR", fen
    fen = cd.play("1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.O-O Be7 5.d3 O-O")
    assert fen == "r1bq1rk1/ppppbppp/2n2n2/4p3/2B1P3/3P1N2/PPP2PPP/RNBQ1RK1", fen


def test_svgs_current():
    """pieces/*.svg match the geometry: run specimen.py after changing a piece."""
    for ch in "KQRBNPkqrbnp":
        name = ("w" if ch.isupper() else "b") + ch.upper() + ".svg"
        with open(os.path.join(HERE, "pieces", name), encoding="utf-8") as fh:
            assert fh.read() == cd.piece_svg(ch), f"pieces/{name} is out of date; run specimen.py"


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"ok {t.__name__}")
    print(f"{len(tests)} tests passed")
