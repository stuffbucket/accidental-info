# The Last Move in Chess: format leakage

A cold read of `drafts/chess-last-move/guide.md`, version 0.1.0, and the built 9-page PDF,
by a reader who has never seen an Accidental Guide. Every page was rendered and read. The PDF
text (`pdftotext -layout`) was compared with `guide.md` to find text that only the builders
print.

Line numbers are `guide.md` lines. “PDF p. N” marks text only the build prints. Each finding
counts once, even when it covers several lines. “Low” marks a finding a reader would likely
get past.

First pass: `lint_guide.py` was not run, because this review was limited to the listed
files. No classifier pass. Every finding below comes from reading.

Kinds: SN self-narration, UV unnamed voices, PV presenter voice, BF borrowed framing, TR
trivia, JG jargon, TT terms-table commentary, MP mannered prose.

## Status of the last scan

No earlier scan was provided.

## Row sentences

No sentence in any table row starts with “It”, “Its”, “They” or “This”. That covers the
terms table (lines 26 to 30), the five entries (lines 50 to 52, 70 to 72, 90 to 92, 109 to
111 and 129 to 131), the Field marks rows and the habits table (lines 151 to 156). Every row
names its subject, such as “A king”, “Check means”, “A draw gives”, “The offer stands” and
“A handshake shows”.

## Findings

Most serious first.

| Line | Text | Kind | Rewrite |
|---|---|---|---|
| 22 | “These five terms tell you whether the game continues and how it ends.” | SN | “Check is the only one of these that doesn’t end the game.” |
| 28, 83, 90 | “but the king is safe”, “the king is safe but its player has no legal move”, “your king safe” | MP (synonym for variety: “safe” for “not in check”, which lines 37, 42 and 91 use) | Line 28: “The player to move has no legal move, but that player’s king isn’t in check.” Line 83: “In stalemate, the king isn’t in check, but its player has no legal move.” Line 90: “Your turn, your king not in check and no legal move available.” |
| 158 | “agree before you start if you won’t use touch-move.” | JG (named once, never defined, and the row on line 151 doesn’t use it) | “In a casual game, agree before you start whether a touched piece must move.” |
| 79 | “The mating move” | JG | “The checkmating move” |
| Diagram key, PDF p. 3 | “K king, Q queen, R rook, B bishop, N knight, small disc pawn. White’s pieces are light, Black’s are dark.” | SN, low (the key explains pieces the figure doesn’t show) | “K king, Q queen. White’s pieces are light, Black’s are dark.” |
| 15 to 16 | “Check is a warning, not the end.” | MP, low (“not X” contrast, and “warning” is a label used nowhere else) | Delete. The line 22 rewrite says it plainly. |
| 122 to 123 | “so say what you mean.” | MP, low (the page ends on a phrase rather than the action) | “so say the result in words.” |
| 130 | “Resigning means ending the game by conceding it.” | MP, low (defined with a synonym) | “Resigning means giving up the game.” |
| 54, 74, 94, 113, 133, and PDF pp. 4 to 7 | “Field marks” | BF, low (a birding term printed as a heading on every entry) | “At a glance”. The label is shared with the series, so the change belongs in the series template. |
| PDF p. 3 | Blue square on h8 on both boards, from “mark Mt h8” and “mark Sm h8” (lines 36 and 38) | JG, low (the mark is drawn with no key) | Add to the key: “The blue square is the king to move.” Or drop lines 36 and 38. |
| PDF p. 9 | “Written and reviewed by a person. AI does the grunt work. Set in TeX Gyre Heros.” | SN, low (colophon about how the booklet was made) | Leave it if it is the series colophon. Otherwise: “Set in TeX Gyre Heros.” |

Checked and clean: the three section titles are plain questions (lines 11, 32 and 145), with
no hooks or teasers. There are no unnamed voices, trivia, history asides, em dashes,
semicolons or straight apostrophes. The sentences on lines 41 to 42 (“On the left”, “On the
right”) only say how to read the figure. The sources line (162) dates the facts and is fine
where it is.

## Counts

| Kind | Count |
|---|---|
| SN | 3 |
| UV | 0 |
| PV | 0 |
| BF | 1 |
| TR | 0 |
| JG | 3 |
| TT | 0 |
| MP | 4 |
| Total | 11 |
