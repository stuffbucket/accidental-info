# Chess diagrams

`chessdiagram.py` draws chess boards for the guides into a ReportLab canvas: the board from a
FEN, from White's side or Black's, with the series' own piece illustrations, tinted squares,
move arrows and captions. It needs only ReportLab, and its output is deterministic, so a
guide's PDF keeps a stable hash.

The pieces are drawn in code, as a family: a simplified Staunton silhouette for each piece,
from a few rectangles, circles and curves, with one stroke weight. White's pieces are white
with an ink outline; Black's are solid ink with a thin light line where their parts meet.
They aren't copied from any piece set, font or SVG, and are under the repository's licences
(the code MIT, the drawings CC BY 4.0).

## Use it from a guide

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "packages" / "chess"))
import chessdiagram as cd

fen = cd.play("1.e4 e5 2.Nf3 Nc6")                      # placement after these moves
box = cd.draw_board(c, x, top - size, size, fen=fen, side="black",
                    tints={"d4": "Us", "e4": "Us"}, arrows=[("g1", "f3")])
y = cd.draw_caption(c, "After 2…Nc6.", box.x0, box.y0 - 2, box.x1 - box.x0)
```

`parents[2]` is the repository from `drafts/<slug>/build_guide.py` or `guides/<slug>/build_guide.py`.

## API

| Name | What it does |
|---|---|
| `draw_board(c, x, y, size, fen=START, side="white", tints=None, arrows=(), coords=True, font="Sans", coord_size=None, ...)` | Draws a board with its lower-left corner at `(x, y)`, `size` points wide. `side="black"` turns the board round, and the rank and file labels follow. `tints` is `{square: colour}`; a family code such as `"Us"` gives a pale tint of that family's colour, a `"#rrggbb"` is used as it is. `arrows` is `[(from, to), ...]`, drawn over the pieces in ink (or `arrow_color`). The labels are set in `font` (falls back to Helvetica if it isn't registered). Returns a `Box`: `x0, y0, x1, y1` is the extent with the labels, `board` is `(x, y, size)`. |
| `board_box(x, y, size, coords=True, coord_size=None)` | The extent `draw_board` would take, `(x0, y0, x1, y1)`, for layout before drawing. |
| `square_xy(square, x, y, size, side="white")` | The lower-left corner of a square, such as `"e4"`, on a board at `(x, y, size)`. |
| `draw_piece(c, ch, x, y, sq)` | One piece, FEN letter `ch` (upper case White), in the square at `(x, y)` with side `sq`. |
| `draw_caption(c, text, x, top, width, font="Sans", size=6.4, leading=None, color=COORD)` | Plain text wrapped to `width`, from `top` down. Returns the bottom y. For rich text, use a ReportLab `Paragraph` instead. |
| `play(moves, fen=START)` | The FEN placement after playing moves in algebraic notation, from a list or a string such as `"1.e4 e5 2.Nf3 Nc6"`. Raises `ValueError` on a move it can't find or that's ambiguous. |
| `Position(fen)` | The same, one `.play(san)` at a time; `.fen()` gives the placement. |
| `tint(colour, t)` | A colour or family code mixed with white; `t=1` is the colour. |
| `piece_svg(ch)`, `export_svg(folder)` | One piece as SVG, or all twelve as `wK.svg` … `bP.svg`. |
| `START`, `INK`, `LIGHT_SQ`, `DARK_SQ`, `COORD`, `FAMILY` | The starting placement and the colours: ink `#1d1d1b`, white and warm grey `#e3ded6` squares, grey labels, the six family colours. |

Squares are readable down to about 12 points (a 96-point board). Coordinates are set at
`size / 22` points, between 4.6 and 6.4.

## Files

| Path | What it is |
|---|---|
| `chessdiagram.py` | The module |
| `pieces/*.svg` | The twelve pieces as SVG, for the website, from the same geometry |
| `specimen.py` | Renders the specimen sheet (every piece, both colours, on both squares, at five sizes, and three boards) and rewrites `pieces/` |
| `test_chessdiagram.py` | Both sides of the starting position, a deterministic PDF, the moves, and that `pieces/` is current |

```sh
.venv/bin/python packages/chess/specimen.py /tmp/specimen.png   # from the repository root
pnpm --filter @accidentalguide/chess test
```

A guide's turbo build doesn't know about this package, so after changing a piece, rebuild
the guides that use it and update their `expected.sha256`.
