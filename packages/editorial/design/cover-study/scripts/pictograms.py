"""Pictograms for the Accidental Guides, drawn on a 12 x 12 unit grid.

Rules, the same for every sign:
- one stroke weight, 1 unit, square caps and mitred joins;
- straight lines at 0, 45 and 90 degrees only;
- circles and arcs centred on grid points, radii in half units;
- solid fills allowed; one ink, no colour (colour stays with the part tiles);
- a white knock-out of 0.75 unit where two shapes overlap.
"""
import math
from reportlab.lib.colors import white


class Grid:
    def __init__(self, c, ox, oy, u, ink, paper=white):
        self.c, self.ox, self.oy, self.u, self.ink, self.paper = c, ox, oy, u, ink, paper
        c.setLineCap(2); c.setLineJoin(0); c.setLineWidth(u)

    def P(self, x, y):
        return self.ox + x * self.u, self.oy + y * self.u

    def _style(self, fill, stroke, color):
        col = color or self.ink
        self.c.setFillColor(col); self.c.setStrokeColor(col); self.c.setLineWidth(self.u)
        return dict(stroke=1 if stroke else 0, fill=1 if fill else 0)

    def poly(self, pts, fill=True, stroke=False, color=None, closed=True):
        st = self._style(fill, stroke, color)
        p = self.c.beginPath(); p.moveTo(*self.P(*pts[0]))
        for q in pts[1:]:
            p.lineTo(*self.P(*q))
        if closed:
            p.close()
        self.c.drawPath(p, **st)

    def rect(self, x0, y0, x1, y1, fill=True, stroke=False, color=None):
        self.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill, stroke, color)

    def line(self, *pts, color=None):
        self.poly(list(pts), fill=False, stroke=True, color=color, closed=False)

    def disc(self, x, y, r, fill=True, stroke=False, color=None):
        st = self._style(fill, stroke, color)
        cx, cy = self.P(x, y); self.c.circle(cx, cy, r * self.u, **st)

    def arc(self, x, y, r, a0, a1, color=None):
        self._style(False, True, color)
        cx, cy = self.P(x, y); R = r * self.u
        p = self.c.beginPath()
        p.arc(cx - R, cy - R, cx + R, cy + R, startAng=a0, extent=a1 - a0)
        self.c.drawPath(p, stroke=1, fill=0)

    def sector(self, x, y, r, a0, a1, color=None):
        """Filled pie slice."""
        self._style(True, False, color)
        cx, cy = self.P(x, y); R = r * self.u
        p = self.c.beginPath(); p.moveTo(cx, cy)
        p.arcTo(cx - R, cy - R, cx + R, cy + R, startAng=a0, extent=a1 - a0); p.close()
        self.c.drawPath(p, stroke=0, fill=1)


# Each sign draws inside 0..12 x 0..12. Comments give the idea, not the coordinates.

def specs(g):
    # A page with a folded corner, two lines of text, and a review mark over its foot.
    g.poly([(1.5, 1.5), (7.5, 1.5), (7.5, 8.5), (4.5, 11.5), (1.5, 11.5)], fill=False, stroke=True)
    g.poly([(4.5, 11.5), (4.5, 8.5), (7.5, 8.5)], fill=True)
    g.line((3.5, 6.5), (5.5, 6.5))
    g.line((3.5, 4.5), (5.5, 4.5))
    g.disc(8.5, 3.5, 3.75, color=g.paper)
    g.disc(8.5, 3.5, 3)
    g.line((7, 3.5), (8, 2.5), (10, 4.5), color=g.paper)


def smoke(g):
    # The ceiling, the alarm under it, its little light, and the chirp.
    g.line((0.5, 11.5), (11.5, 11.5))
    g.sector(6, 11, 3.5, 180, 360)
    g.disc(6, 9.25, 0.6, color=g.paper)
    for r in (5.5, 7.5, 9.5):
        g.arc(6, 11, r, 240, 300)


def chess_first(g):
    # A pawn (base, flared body, collar, head) and the arrow of its first move.
    g.rect(1, 1, 8, 2)
    g.poly([(2, 2), (7, 2), (5, 4), (5, 5), (4, 5), (4, 4)])
    g.rect(2.5, 5, 6.5, 6)
    g.disc(4.5, 7.75, 1.75)
    g.line((10.5, 1), (10.5, 10))
    g.poly([(8.5, 9), (10.5, 11), (12.5, 9)], fill=False, stroke=True, closed=False)


def grilled_cheese(g):
    # Side view: a pan with a long handle, a sandwich in it, the cheese running over the
    # edge, and a little heat coming off it.
    g.poly([(0.5, 2.5), (2, 1), (8, 1), (9.5, 2.5)])
    g.line((9.5, 2), (12, 2))
    g.rect(1.5, 3.25, 8.5, 5.25)
    g.rect(1, 6, 9, 6.75)
    g.disc(8.5, 5.75, 1)
    g.rect(1.5, 7.5, 8.5, 9.5)
    for x in (3, 5, 7):
        g.line((x, 10.5), (x, 12))


def catalog(g):
    # A counting frame: the oldest calculating machine, for the series about the newest.
    g.rect(0.5, 0.5, 11.5, 11.5, fill=False, stroke=True)
    for y, beads in ((9, (2.5, 5, 9.5)), (6, (2.5, 7, 9.5)), (3, (2.5, 5, 7.5))):
        g.line((1, y), (11, y))
        for x in beads:
            g.disc(x, y, 1.25)


def agents(g):
    # A model (the disc) held in its harness (the frame), reaching out to two tools.
    g.rect(0.5, 2.5, 7.5, 9.5, fill=False, stroke=True)
    g.disc(4, 6, 2)
    g.line((7.5, 8), (10, 8))
    g.line((7.5, 4), (10, 4))
    g.rect(10, 7, 12, 9)
    g.disc(11, 4, 1)


def context(g):
    # A window filling from the bottom up. The panes still clear at the top are the room left.
    g.rect(1.5, 0.5, 10.5, 11.5, fill=False, stroke=True)
    g.rect(2.5, 1.5, 9.5, 6.5)
    g.line((6, 6.5), (6, 11))


def claude_code(g):
    # A terminal: a window with a prompt and a cursor.
    g.rect(0.5, 1.5, 11.5, 10.5, fill=False, stroke=True)
    g.rect(0.5, 9, 11.5, 10.5)
    g.line((2.5, 7), (4.5, 5), (2.5, 3))
    g.line((6, 3), (9, 3))


def dnd(g):
    # A twenty-sided die, seen face on.
    s = math.sqrt(3) / 2
    pts = [(6 + 5.5 * math.cos(math.radians(a)), 6 + 5.5 * math.sin(math.radians(a)))
           for a in (90, 150, 210, 270, 330, 30)]
    g.poly(pts, fill=False, stroke=True)
    g.poly([(6, 9), (6 - 3 * s * 1.0, 4.5), (6 + 3 * s * 1.0, 4.5)])


SIGNS = {
    "specs-and-reviews": specs,
    "chirping-smoke-detector": smoke,
    "chess-first-move": chess_first,
    "grilled-cheese": grilled_cheese,
    "accidental-intelligence": catalog,
    "agents-harnesses-skills-tools": agents,
    "context-windows": context,
    "claude-code": claude_code,
}


def draw(c, slug, x, y, size, ink, paper=white, pad=2):
    """Draw slug's sign centred in a size x size box at lower-left (x, y)."""
    u = size / (12 + 2 * pad)
    g = Grid(c, x + pad * u, y + pad * u, u, ink, paper)
    SIGNS[slug](g)
    c.setLineCap(0); c.setLineJoin(0)
