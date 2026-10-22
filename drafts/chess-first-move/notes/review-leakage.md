# The First Move in Chess: format leakage

A cold read of `drafts/chess-first-move/guide.md`, version 0.1.0, and the built PDF, by a
reader who has never seen an Accidental Guide. Every page was rendered and read. The PDF text
was compared with `guide.md` to find text that only the builders print.

Line numbers are `guide.md` lines. "PDF p. N" marks text only the build prints. Each finding
counts once, even when it covers several lines. "Low" marks a finding a reader would likely
get past.

First pass: `lint_guide.py` (0 errors, 0 warnings). No classifier pass was run. A grep for em
dashes, semicolons, exclamation marks, straight quotes and pronoun-led sentences found none.

Kinds: SN self-narration, UV unnamed voices, PV presenter voice, BF borrowed framing, TR
trivia, JG jargon, TT terms-table commentary, MP mannered prose.

## Status of the last scan

No earlier scan.

## Rows that start with It, Its, They or This

None. Every sentence in the terms table (lines 25 to 27), the entry rows (lines 48 to 50, 69
to 71, 90 to 92), the Field marks rows and the moves table (lines 115 to 120) starts with a
named subject or an imperative.

## Findings

| Line | Text | Kind | Rewrite |
|---|---|---|---|
| 18 | "Opening lines matter less when you’re learning than a few principles you can use against whatever the other player does." | JG | Lines 18 to 19, from "Opening lines": "When you’re learning, a few principles help more than memorized sequences of moves. You can use the principles against whatever the other player does." |
| 115 to 118 | "opens lines for the queen and a bishop" | JG | "frees the queen and a bishop to move" in all four rows |
| 124 | "4.Qxf7#" | JG | x and # are never explained. Line 42: "White’s pawn moves to e4, then Black’s pawn moves to e5. Black’s move alone is 1…e5. An x means a capture and # means checkmate." |
| 50 | "The center usually opens first as its pawns are exchanged." | JG | "The center usually opens first, because center pawns often capture each other." |
| 117 | "The e-pawn answers White in the middle" | MP | "> \| 1…e5 \| As Black, after 1.e4. The e-pawn moves two squares, blocks White’s e-pawn and frees the queen and a bishop to move. \|" |
| 118 | "The d-pawn answers White in the middle" | MP | "> \| 1…d5 \| As Black, after 1.d4. The d-pawn moves two squares, blocks White’s d-pawn and frees the queen and a bishop to move. \|" |
| 69 | "Knights and bishops leaving their starting row." | MP | Synonym for "rank", defined on page 3. "\| Identify by \| Knights and bishops leaving their starting squares. \|" |
| PDF p. 3 | "K king, Q queen, R rook, B bishop, N knight, small disc pawn. White’s pieces are light, Black’s are dark." | JG | "small disc pawn" reads as a kind of pawn. Key text in the build: "Letters mark the pieces: K king, Q queen, R rook, B bishop, N knight. A small disc is a pawn. White’s pieces are light and Black’s are dark." |
| 27 | "One move that moves your king and a rook." | MP, Low | "> \| Castling \| One move of your king and a rook together. \|" |
| 21 | "Three ideas cover most of what you need at the start." | PV, Low | Set-up line for the table. "Center, development and castling cover most of what you need at the start." |
| 52, 73, 94 | "Field marks" (heading, PDF pp. 4 to 6) | BF, Low | A bird-watching term with no meaning in chess. A cold reader gets past it, but a plain label reads better: "At a glance". This is a change to the form, so it applies to every guide. |
| PDF p. 8 | "Written and reviewed by a person. AI does the grunt work. Set in TeX Gyre Heros." | SN, Low | Colophon about how the guide was made. It sits on the back cover, where readers expect it. No change unless the series drops it. |

## Counts

| Kind | Count |
|---|---|
| SN | 1 |
| UV | 0 |
| PV | 1 |
| BF | 1 |
| TR | 0 |
| JG | 5 |
| TT | 0 |
| MP | 4 |
| Total | 12 |
