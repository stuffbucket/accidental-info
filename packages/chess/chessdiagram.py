"""Chess diagrams for the Accidental Guides, drawn into a ReportLab canvas.

Pure Python: it needs only ReportLab, which every guide's build already uses. A guide's
build_guide.py imports it with

    ROOT = Path(__file__).resolve().parents[2]          # the repository, from drafts/<slug>/
    sys.path.insert(0, str(ROOT / "packages" / "chess"))
    import chessdiagram as cd

The piece illustrations are drawn here, in code, as a family: a simplified Staunton
silhouette for each piece, built from a few rectangles, circles and Bezier curves on a
100-unit square, with one stroke weight. Nothing is copied from a piece set, a font or an
SVG. The same geometry is written out as SVG files by export_svg() (see pieces/).

Everything is deterministic: no randomness, no dates, fixed float formatting, so a PDF that
uses it keeps a stable hash under ReportLab's invariant mode.

See README.md for the API.
"""
from __future__ import annotations

import math
import re
from dataclasses import dataclass

__all__ = [
    "START", "INK", "LIGHT_SQ", "DARK_SQ", "COORD", "FAMILY", "tint",
    "draw_board", "board_box", "draw_piece", "draw_caption", "wrap_lines",
    "play", "Position", "square_xy", "piece_svg", "export_svg",
]

# ---------------------------------------------------------------- colours
INK = "#1d1d1b"          # outlines and Black's pieces: an ink, not pure black
PAPER = "#ffffff"        # White's pieces and the light squares
LIGHT_SQ = "#ffffff"
DARK_SQ = "#e3ded6"      # a light warm grey
COORD = "#6b6b6b"        # rank and file labels
INNER = "#f3efe8"        # the thin light line inside Black's pieces
EDGE = "#b9b2a7"         # the board's hairline edge

# The six family colours of the series (packages/editorial/registry.md).
FAMILY = {"Ru": "#FFCD29", "Wr": "#9747FF", "Ck": "#14AE5C", "Us": "#F24822",
          "Dm": "#E83FBF", "Nu": "#0D99FF"}

START = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
FILES = "abcdefgh"


def _rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def tint(color, t):
    """color mixed with white: t=1 is the colour, t=0 is white. color is '#rrggbb' or a family
    code such as 'Us'. Returns '#rrggbb'."""
    color = FAMILY.get(color, color)
    return "#%02x%02x%02x" % tuple(round(255 - (255 - v) * t) for v in _rgb(color))


def _color(h):
    from reportlab.lib.colors import HexColor
    return HexColor(FAMILY.get(h, h)) if isinstance(h, str) else h


# ---------------------------------------------------------------- piece geometry
# A shape is a list of path operations on a 100 x 100 square, y up:
#   ("M", x, y)  ("L", x, y)  ("C", x1, y1, x2, y2, x, y)  ("Z",)
# A piece is a list of layers, drawn in order, each ("fill", ops), ("line", ops) or
# ("dot", ops). Fills carry the outline; lines are inner details; dots are small solid marks
# such as the knight's eye. White: fills white, outlines and details in ink. Black: fills and
# outlines in ink, details in a thin light line.
K_ = 0.5523


def circle(cx, cy, r):
    k = r * K_
    return [("M", cx + r, cy), ("C", cx + r, cy + k, cx + k, cy + r, cx, cy + r),
            ("C", cx - k, cy + r, cx - r, cy + k, cx - r, cy),
            ("C", cx - r, cy - k, cx - k, cy - r, cx, cy - r),
            ("C", cx + k, cy - r, cx + r, cy - k, cx + r, cy), ("Z",)]


def rrect(x0, y0, x1, y1, r):
    k = r * (1 - K_)
    return [("M", x0 + r, y0), ("L", x1 - r, y0), ("C", x1 - k, y0, x1, y0 + k, x1, y0 + r),
            ("L", x1, y1 - r), ("C", x1, y1 - k, x1 - k, y1, x1 - r, y1),
            ("L", x0 + r, y1), ("C", x0 + k, y1, x0, y1 - k, x0, y1 - r),
            ("L", x0, y0 + r), ("C", x0, y0 + k, x0 + k, y0, x0 + r, y0), ("Z",)]


def poly(*pts, close=True):
    ops = [("M", *pts[0])] + [("L", *p) for p in pts[1:]]
    return ops + [("Z",)] if close else ops


def _base(w=30, y0=11, h=9):
    """The plinth every piece stands on, centred, w either side of the middle."""
    return ("fill", rrect(50 - w, y0, 50 + w, y0 + h, 3.2))


def _flare(top_y, top_w, bot_w=20, bot_y=20, bow=0.55):
    """A body that narrows from the plinth to a waist: concave sides."""
    l0, r0, l1, r1 = 50 - bot_w, 50 + bot_w, 50 - top_w, 50 + top_w
    dy = top_y - bot_y
    return ("fill", [("M", l0, bot_y),
                     ("C", l0 + (l1 - l0) * bow, bot_y + dy * 0.25, l1, bot_y + dy * (1 - bow) , l1, top_y),
                     ("L", r1, top_y),
                     ("C", r1, bot_y + dy * (1 - bow), r0 - (r0 - r1) * bow, bot_y + dy * 0.25, r0, bot_y),
                     ("Z",)])


def _collar(y, w=15, h=5.5):
    return ("fill", rrect(50 - w, y, 50 + w, y + h, 2.4))


def pawn():
    return [
        _base(25, 12, 8.5),
        _flare(46, 7.5, 18, 20.5, 0.62),
        _collar(43, 13.5, 5.5),
        ("fill", circle(50, 60, 12)),
    ]


def rook():
    crown = poly((27.5, 63), (72.5, 63), (72.5, 84), (64.5, 84), (64.5, 77.5), (55.5, 77.5),
                 (55.5, 84), (44.5, 84), (44.5, 77.5), (35.5, 77.5), (35.5, 84), (27.5, 84))
    return [
        _base(30, 11, 9),
        ("fill", poly((31, 20), (69, 20), (66, 57), (34, 57))),
        ("fill", rrect(29, 55, 71, 63.5, 1.5)),
        ("fill", crown),
    ]


def bishop():
    mitre = [("M", 39, 49), ("C", 30.5, 59, 36, 73, 50, 84.5), ("C", 64, 73, 69.5, 59, 61, 49), ("Z",)]
    return [
        _base(27, 11, 9),
        _flare(46, 7.5, 19, 20, 0.6),
        _collar(43, 14.5, 6),
        ("fill", mitre),
        ("fill", circle(50, 87.5, 4.6)),
        # the mitre's slit
        ("line", poly((56.5, 71), (47, 60.5), close=False)),
    ]


def queen():
    # a coronet of five points fanning out from the collar, each tipped with a ball
    tips = [(25.5, 79), (37, 85.5), (50, 88.5), (63, 85.5), (74.5, 79)]
    cup = poly((37.5, 61), tips[0], (38, 70.5), tips[1], (45, 72), tips[2], (55, 72), tips[3],
               (62, 70.5), tips[4], (62.5, 61))
    return [
        _base(30, 11, 9),
        _flare(56, 9, 21, 20, 0.6),
        _collar(54, 15.5, 6.5),
        ("fill", cup),
    ] + [("fill", circle(x, y, 4.1)) for x, y in tips] + [
        ("line", poly((38.5, 66), (61.5, 66), close=False)),
    ]


def king():
    cup = [("M", 35.5, 60.5), ("C", 29, 66, 31, 77, 39, 77.5), ("L", 61, 77.5),
           ("C", 69, 77, 71, 66, 64.5, 60.5), ("Z",)]
    cross = poly((46.8, 76), (53.2, 76), (53.2, 83.5), (59.5, 83.5), (59.5, 89.5), (53.2, 89.5),
                 (53.2, 96), (46.8, 96), (46.8, 89.5), (40.5, 89.5), (40.5, 83.5), (46.8, 83.5))
    return [
        _base(30, 11, 9),
        _flare(56, 9, 21, 20, 0.6),
        _collar(54, 15.5, 6.5),
        ("fill", cross),
        ("fill", cup),
        ("line", poly((37, 68.5), (63, 68.5), close=False)),
    ]


def knight():
    # A horse's head facing left: mane down the back of the neck, two ears, a long face down
    # to a squared muzzle, an open mouth, the jaw, and the chest down to the plinth.
    head = [
        ("M", 71, 20),
        ("C", 75, 38, 76, 58, 66, 74),          # back of the neck, bulging out
        ("C", 64.5, 77, 62.5, 80, 61, 83),      # up to the ear
        ("L", 59.5, 92),                        # ear tip
        ("L", 54.5, 84.5),                      # between the ears
        ("L", 51, 90.5),                        # front ear tip
        ("L", 48.5, 83),                        # forelock
        ("C", 40, 80.5, 33, 73.5, 27.5, 64),    # forehead and face, sloping down
        ("C", 25, 60, 22.5, 56.5, 22.5, 53.5),  # nose
        ("C", 22.5, 50, 25, 48.5, 28, 49),      # muzzle tip
        ("L", 34, 51.5),                        # mouth corner
        ("L", 30.5, 47.5),                      # lower lip
        ("C", 33.5, 44, 38.5, 44.5, 42, 47.5),  # chin and jaw
        ("C", 44, 49, 46, 51.5, 48.5, 52),      # under the jaw
        ("C", 40, 45, 32, 34, 31, 20),          # throat and chest down to the plinth
        ("Z",),
    ]
    mane = [("M", 64.5, 71.5), ("C", 70.5, 58, 70, 40, 66.5, 25)]
    return [
        _base(29, 11, 9),
        ("fill", head),
        ("line", mane),
        ("dot", circle(45.5, 70, 3.1)),
        ("dot", circle(28.2, 54.8, 1.6)),
    ]


PIECES = {"k": king, "q": queen, "r": rook, "b": bishop, "n": knight, "p": pawn}
NAMES = {"k": "king", "q": "queen", "r": "rook", "b": "bishop", "n": "knight", "p": "pawn"}

# One stroke weight for the family, in piece units (a square is 100). A floor keeps the line
# from vanishing on small boards.
STROKE = 3.4
MIN_STROKE_PT = 0.42


def _stroke_units(scale):
    return max(STROKE, MIN_STROKE_PT / scale)


# ---------------------------------------------------------------- drawing pieces
def _path(c, ops, ox, oy, s):
    p = c.beginPath()
    for op in ops:
        if op[0] == "M":
            p.moveTo(ox + op[1] * s, oy + op[2] * s)
        elif op[0] == "L":
            p.lineTo(ox + op[1] * s, oy + op[2] * s)
        elif op[0] == "C":
            p.curveTo(*(ox + v * s if i % 2 == 0 else oy + v * s for i, v in enumerate(op[1:])))
        else:
            p.close()
    return p


def draw_piece(c, ch, x, y, sq):
    """Draw one piece, FEN letter ch (upper case White, lower case Black), in the square
    whose lower-left corner is (x, y) and whose side is sq points."""
    white = ch.isupper()
    layers = PIECES[ch.lower()]()
    s = sq / 100.0
    sw = _stroke_units(s) * s
    c.saveState()
    c.setLineJoin(1); c.setLineCap(1)
    for kind, ops in layers:
        p = _path(c, ops, x, y, s)
        if kind == "fill":
            c.setLineWidth(sw)
            c.setStrokeColor(_color(INK))
            c.setFillColor(_color(PAPER if white else INK))
            c.drawPath(p, stroke=1, fill=1)
        elif kind == "line":
            c.setLineWidth(sw * (0.9 if white else 0.55))
            c.setStrokeColor(_color(INK if white else INNER))
            c.drawPath(p, stroke=1, fill=0)
        else:  # dot
            c.setFillColor(_color(INK if white else INNER))
            c.drawPath(p, stroke=0, fill=1)
    if not white:
        # the parts' joins, which the ink fill hides, in the thin light line
        for kind, ops in _joins(ch.lower()):
            p = _path(c, ops, x, y, s)
            c.setLineWidth(sw * 0.55); c.setStrokeColor(_color(INNER))
            c.drawPath(p, stroke=1, fill=0)
    c.restoreState()


def _joins(kind):
    """Light lines on a Black piece where its parts meet: the top of the plinth and the
    collar, which a White piece shows by its outlines."""
    j = {
        "p": [(29, 21.8, 71), (39, 44.8, 61), (39.5, 48.6, 60.5)],
        "r": [(23, 21, 77), (31, 56.8, 69), (31, 62, 69)],
        "b": [(26, 21, 74), (38, 44.8, 62), (39, 49.2, 61)],
        "q": [(22, 21, 78), (37, 55.8, 63), (37.5, 60.6, 62.5)],
        "k": [(22, 21, 78), (37, 55.8, 63), (37.5, 60.6, 62.5)],
        "n": [(24, 21, 76)],
    }[kind]
    return [("line", poly((x0, yy), (x1, yy), close=False)) for x0, yy, x1 in j]


# ---------------------------------------------------------------- boards
@dataclass(frozen=True)
class Box:
    """Where a board landed. x0, y0, x1, y1: the extent including the rank and file labels and
    any caption. board: (x, y, size) of the squares themselves."""
    x0: float
    y0: float
    x1: float
    y1: float
    board: tuple


def _coord_size(size):
    return max(4.6, min(6.4, size / 22.0))


def board_box(x, y, size, coords=True, coord_size=None):
    """The extent a board drawn at (x, y, size) takes, with its labels: (x0, y0, x1, y1)."""
    if not coords:
        return (x, y, x + size, y + size)
    fs = coord_size or _coord_size(size)
    return (x - fs * 1.35, y - fs * 1.75, x + size, y + size)


def square_xy(square, x, y, size, side="white"):
    """Lower-left corner of a square such as 'e4' on a board at (x, y, size)."""
    f, r = FILES.index(square[0]), int(square[1]) - 1
    if side == "black":
        f, r = 7 - f, 7 - r
    sq = size / 8.0
    return x + f * sq, y + r * sq


def _placement(fen):
    rows = fen.split()[0].split("/")
    if len(rows) != 8:
        raise ValueError(f"not a FEN placement: {fen!r}")
    out = {}
    for i, row in enumerate(rows):
        f = 0
        for ch in row:
            if ch.isdigit():
                f += int(ch)
            else:
                out[FILES[f] + str(8 - i)] = ch
                f += 1
        if f != 8:
            raise ValueError(f"rank {8 - i} of {fen!r} has {f} files")
    return out


def draw_board(c, x, y, size, fen=START, side="white", tints=None, arrows=(), coords=True,
               font="Sans", light=LIGHT_SQ, dark=DARK_SQ, edge=EDGE, arrow_color=None,
               coord_color=COORD, coord_size=None):
    """Draw a board with its lower-left corner at (x, y), size points wide, into canvas c.

    fen     a FEN placement ('rnbqkbnr/pppppppp/8/...'); a full FEN is fine too.
    side    'white' puts White at the bottom; 'black' turns the board round, with the labels.
    tints   {square: colour} fills those squares; colour is '#rrggbb' or a family code such
            as 'Us', taken as a pale tint (tint(code, 0.3)).
    arrows  [(from_square, to_square), ...] drawn over the pieces.
    coords  draw the rank numbers left of the board and the file letters under it, in
            coord_size points (default: from the board's size, 4.6 to 6.4).
    font    the font for the labels: a registered name ('Sans' in the guides); falls back to
            Helvetica when it isn't registered.

    Returns a Box with the drawn extent.
    """
    from reportlab.pdfbase import pdfmetrics
    sq = size / 8.0
    tints = tints or {}
    c.saveState()
    for r in range(8):
        for f in range(8):
            name = FILES[f] + str(r + 1)
            fx, fy = square_xy(name, x, y, size, side)
            if name in tints:
                t = tints[name]
                fill = tint(t, 0.3) if t in FAMILY else t
            else:
                fill = dark if (f + r) % 2 == 0 else light
            c.setFillColor(_color(fill))
            c.rect(fx, fy, sq, sq, stroke=0, fill=1)
    if edge:
        c.setStrokeColor(_color(edge)); c.setLineWidth(0.5)
        c.rect(x, y, size, size, stroke=1, fill=0)
    for name, ch in sorted(_placement(fen).items()):
        fx, fy = square_xy(name, x, y, size, side)
        draw_piece(c, ch, fx, fy, sq)
    for a, b in arrows:
        _arrow(c, a, b, x, y, size, side, arrow_color or INK)
    if coords:
        try:
            pdfmetrics.getFont(font)
        except KeyError:
            font = "Helvetica"
        fs = coord_size or _coord_size(size)
        c.setFillColor(_color(coord_color)); c.setFont(font, fs)
        files = FILES if side == "white" else FILES[::-1]
        ranks = "12345678" if side == "white" else "87654321"
        for i in range(8):
            c.drawCentredString(x - fs * 0.75, y + (i + 0.5) * sq - fs * 0.35, ranks[i])
            c.drawCentredString(x + (i + 0.5) * sq, y - fs * 1.45, files[i])
    c.restoreState()
    return Box(*board_box(x, y, size, coords, coord_size), board=(x, y, size))


def _arrow(c, a, b, x, y, size, side, color):
    sq = size / 8.0
    ax, ay = square_xy(a, x, y, size, side); bx, by = square_xy(b, x, y, size, side)
    ax += sq / 2; ay += sq / 2; bx += sq / 2; by += sq / 2
    d = math.hypot(bx - ax, by - ay)
    ux, uy = (bx - ax) / d, (by - ay) / d
    w = max(0.9, sq * 0.11)
    head, hw = sq * 0.36, sq * 0.24
    ax, ay = ax + ux * sq * 0.18, ay + uy * sq * 0.18
    tx, ty = bx - ux * sq * 0.12, by - uy * sq * 0.12
    nx, ny = -uy, ux
    c.saveState()
    c.setStrokeColor(_color(color)); c.setFillColor(_color(color))
    c.setLineWidth(w); c.setLineCap(0)
    c.line(ax, ay, tx - ux * head * 0.9, ty - uy * head * 0.9)
    p = c.beginPath()
    p.moveTo(tx, ty)
    p.lineTo(tx - ux * head + nx * hw, ty - uy * head + ny * hw)
    p.lineTo(tx - ux * head - nx * hw, ty - uy * head - ny * hw)
    p.close()
    c.drawPath(p, stroke=0, fill=1)
    c.restoreState()


def wrap_lines(text, font, size, width):
    """Split text into lines no wider than width, at spaces."""
    from reportlab.pdfbase import pdfmetrics
    out, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if line and pdfmetrics.stringWidth(trial, font, size) > width:
            out.append(line); line = word
        else:
            line = trial
    if line:
        out.append(line)
    return out


def draw_caption(c, text, x, top, width, font="Sans", size=6.4, leading=None, color=COORD):
    """A caption set ragged right from top down, wrapped to width. Returns the bottom y."""
    from reportlab.pdfbase import pdfmetrics
    try:
        pdfmetrics.getFont(font)
    except KeyError:
        font = "Helvetica"
    leading = leading or size * 1.28
    c.saveState(); c.setFillColor(_color(color)); c.setFont(font, size)
    y = top
    for line in wrap_lines(text, font, size, width):
        y -= leading
        c.drawString(x, y + (leading - size) * 0.5, line)
    c.restoreState()
    return y


# ---------------------------------------------------------------- moves
class Position:
    """A position that can play moves in standard algebraic notation (SAN), enough to set up
    opening diagrams: every piece move, captures, castling, en passant and promotion, with
    moves that leave the king in check ruled out when the SAN is ambiguous."""

    def __init__(self, fen=START):
        parts = fen.split()
        self.board = _placement(parts[0])
        self.turn = parts[1] if len(parts) > 1 else "w"
        self.ep = parts[3] if len(parts) > 3 and parts[3] != "-" else None
        self.castle = parts[2] if len(parts) > 2 else "KQkq"

    def fen(self):
        """The FEN placement."""
        rows = []
        for r in range(8, 0, -1):
            row, n = "", 0
            for f in FILES:
                ch = self.board.get(f + str(r))
                if ch:
                    row += (str(n) if n else "") + ch; n = 0
                else:
                    n += 1
            rows.append(row + (str(n) if n else ""))
        return "/".join(rows)

    # -- geometry
    @staticmethod
    def _sq(f, r):
        return FILES[f] + str(r + 1) if 0 <= f < 8 and 0 <= r < 8 else None

    def _reaches(self, frm, to, kind, white):
        """Can a piece of this kind on frm move (or capture) to `to`, ignoring checks?"""
        f0, r0 = FILES.index(frm[0]), int(frm[1]) - 1
        f1, r1 = FILES.index(to[0]), int(to[1]) - 1
        df, dr = f1 - f0, r1 - r0
        if kind == "n":
            return (abs(df), abs(dr)) in ((1, 2), (2, 1))
        if kind == "k":
            return max(abs(df), abs(dr)) == 1
        dirs = {"r": abs(df) * abs(dr) == 0, "b": abs(df) == abs(dr),
                "q": abs(df) * abs(dr) == 0 or abs(df) == abs(dr)}
        if kind in dirs:
            if not dirs[kind] or (df, dr) == (0, 0):
                return False
            sf, sr = (df > 0) - (df < 0), (dr > 0) - (dr < 0)
            f, r = f0 + sf, r0 + sr
            while (f, r) != (f1, r1):
                if self._sq(f, r) in self.board:
                    return False
                f, r = f + sf, r + sr
            return True
        raise ValueError(kind)

    def _attacked(self, square, by_white):
        for frm, ch in list(self.board.items()):
            if ch.isupper() != by_white:
                continue
            kind = ch.lower()
            if kind == "p":
                d = 1 if by_white else -1
                f0, r0 = FILES.index(frm[0]), int(frm[1]) - 1
                if square in (self._sq(f0 - 1, r0 + d), self._sq(f0 + 1, r0 + d)):
                    return True
            elif self._reaches(frm, square, kind, by_white):
                return True
        return False

    def _king_safe_after(self, frm, to, white, extra=None):
        saved = dict(self.board)
        ch = self.board.pop(frm)
        self.board[to] = ch
        if extra:
            self.board.pop(extra, None)
        king = next(s for s, p in self.board.items() if p == ("K" if white else "k"))
        ok = not self._attacked(king, not white)
        self.board = saved
        return ok

    def play(self, san):
        """Play one move in SAN ('e4', 'Nf3', 'exd5', 'O-O', 'e8=Q', 'Bxf7+'). Returns self."""
        white = self.turn == "w"
        m = san.strip().rstrip("+#!?")
        if m in ("O-O", "0-0", "O-O-O", "0-0-0"):
            rank = "1" if white else "8"
            long = m.count("-") == 2
            k_from, k_to = "e" + rank, ("c" if long else "g") + rank
            r_from, r_to = ("a" if long else "h") + rank, ("d" if long else "f") + rank
            self.board[k_to] = self.board.pop(k_from)
            self.board[r_to] = self.board.pop(r_from)
            self.ep = None
            self.turn = "b" if white else "w"
            return self
        g = re.fullmatch(r"([KQRBN])?([a-h])?([1-8])?(x)?([a-h][1-8])(?:=?([QRBN]))?", m)
        if not g:
            raise ValueError(f"can't read the move {san!r}")
        piece, dfile, drank, capture, to, promo = g.groups()
        kind = (piece or "P").lower()
        mine = (lambda ch: ch.isupper()) if white else (lambda ch: ch.islower())
        cands = []
        for frm, ch in sorted(self.board.items()):
            if not mine(ch) or ch.lower() != kind:
                continue
            if dfile and frm[0] != dfile or drank and frm[1] != drank:
                continue
            target = self.board.get(to)
            if target and mine(target):
                continue
            extra = None
            if kind == "p":
                d = 1 if white else -1
                f0, r0 = FILES.index(frm[0]), int(frm[1]) - 1
                f1, r1 = FILES.index(to[0]), int(to[1]) - 1
                if capture:
                    if abs(f1 - f0) != 1 or r1 - r0 != d:
                        continue
                    if not target:
                        if to != self.ep:
                            continue
                        extra = to[0] + frm[1]
                else:
                    if f1 != f0 or target:
                        continue
                    if r1 - r0 == d:
                        pass
                    elif r1 - r0 == 2 * d and r0 == (1 if white else 6) and self._sq(f0, r0 + d) not in self.board:
                        pass
                    else:
                        continue
            else:
                if not self._reaches(frm, to, kind, white):
                    continue
            if self._king_safe_after(frm, to, white, extra):
                cands.append((frm, extra))
        if len(cands) != 1:
            raise ValueError(f"{san!r} matches {len(cands)} pieces in {self.fen()}")
        frm, extra = cands[0]
        ch = self.board.pop(frm)
        if extra:
            self.board.pop(extra)
        if promo:
            ch = promo if white else promo.lower()
        self.board[to] = ch
        self.ep = None
        if kind == "p" and abs(int(to[1]) - int(frm[1])) == 2:
            self.ep = frm[0] + str((int(frm[1]) + int(to[1])) // 2)
        self.turn = "b" if white else "w"
        return self


def play(moves, fen=START):
    """The FEN placement after playing moves from fen. moves is a list of SAN strings or one
    string such as '1.e4 e5 2.Nf3 Nc6' (move numbers and '...' are skipped)."""
    if isinstance(moves, str):
        moves = [t for t in re.split(r"\s+", moves) if t]
    p = Position(fen)
    for mv in moves:
        mv = re.sub(r"^\d+\.(\.\.)?|^\.\.\.|^\d+…|^…", "", mv)
        if mv:
            p.play(mv)
    return p.fen()


# ---------------------------------------------------------------- SVG
def _svg_d(ops):
    def n(v):
        return f"{v:.2f}".rstrip("0").rstrip(".")
    out = []
    for op in ops:
        if op[0] == "Z":
            out.append("Z")
        else:
            vals = [n(v if i % 2 == 0 else 100 - v) for i, v in enumerate(op[1:])]
            out.append(op[0] + " ".join(vals))
    return " ".join(out)


def piece_svg(ch):
    """One piece as a standalone SVG on a 100 x 100 view box."""
    white = ch.isupper()
    sw = STROKE
    fill = PAPER if white else INK
    detail = INK if white else INNER
    lw = sw * (0.9 if white else 0.55)
    body = []
    for kind, ops in PIECES[ch.lower()]():
        d = _svg_d(ops)
        if kind == "fill":
            body.append(f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{sw}"/>')
        elif kind == "line":
            body.append(f'<path d="{d}" fill="none" stroke="{detail}" stroke-width="{lw:.2f}"/>')
        else:
            body.append(f'<path d="{d}" fill="{detail}"/>')
    if not white:
        for _, ops in _joins(ch.lower()):
            body.append(f'<path d="{_svg_d(ops)}" fill="none" stroke="{INNER}" stroke-width="{lw:.2f}"/>')
    color = "White" if white else "Black"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">\n'
            f'<title>{color} {NAMES[ch.lower()]}</title>\n'
            f'<g stroke-linejoin="round" stroke-linecap="round">\n' + "\n".join(body) + "\n</g>\n</svg>\n")


def export_svg(folder):
    """Write the twelve pieces as wK.svg ... bP.svg into folder. Returns the paths."""
    import os
    os.makedirs(folder, exist_ok=True)
    paths = []
    for ch in "KQRBNPkqrbnp":
        name = ("w" if ch.isupper() else "b") + ch.upper() + ".svg"
        path = os.path.join(folder, name)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(piece_svg(ch))
        paths.append(path)
    return paths
