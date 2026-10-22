# Ordering Wine for the Table: reader panel

Reviewed: `drafts/ordering-wine/guide.md`, version 0.2.0, and its 7-page PDF (page images
and `pdftotext` output). Each page was read as three readers with no access to the sources:

- **Diner.** Rarely drinks wine, has just been handed the list at a restaurant dinner and
  has to order. Decides what to say to the server in the next five minutes.
- **Expert.** Knows wine well. Has no patience for errors, overstatement or snobbery.
  Decides whether to trust the guide.
- **Host.** Paying for a large table and watching the bill. Decides how many bottles, at
  what price.

The voice pass checks the guide against the review skill’s `checklist.md`.

All rewrites together cut the body by about 26 words (about 2 words if lines 17 to 18 are
kept). The ledger is at the end.

## Top ten fixes

Most serious first.

**1. The diner has nothing to say when asked what they like.**
Page 3, line 36: “Say what you’re eating, what you like and don’t like, and your price band.”
The Diner doesn’t know what they like. The words that would help (light, full, dry) only
arrive on pages 4 and 5, after the order has been placed.
Rewrite line 36: “Say what you’re eating, your price band, and whether you like light or full,
dry or a little sweet.”

**2. There is no step for placing the order.**
Page 3, lines 36 to 37. The steps go from “Ask the server” straight to “Check the label”. The
Diner’s worst moment, naming a wine they can’t pronounce, is skipped. The added row makes no
factual claim, so it needs no source.
Rewrite: insert after line 36: “> | Order | Name the wine, or point to it on the list. |”

**3. The second-cheapest finding is overstated and has no date.**
Page 5, lines 122 to 123: “One study of 235 London wine lists found its markup was lower
than the next four bottles’ markups.” The Expert knows a study gives averages, not a rule for
every list, and wonders when it was done. The Host can’t tell whether “the next four bottles”
means the next four printed or the next four up in price.
Rewrite line 123: “In a study of 235 London lists from 2015, its markup was on average below
the next four wines up in price.”

**4. The Host isn’t told where markups are highest.**
Page 6, line 151: “Look for less familiar regions and grapes. Those wines are often on the
list for their quality and value.” The Host’s question is which part of the list is the
better deal. The second sentence doesn’t say, and the Expert doubts its claim. The study has
the answer.
Rewrite line 151: “Look for less familiar regions and grapes. In the London study, percentage
markups were highest on mid-range wines.”

**5. “Sound” is never defined.**
Page 3, line 39: “Nod when the wine is sound”. Page 6, line 142: “whether the wine is sound”.
The Diner reads “sound” as a noise. Everywhere else the guide says faulty.
Rewrite line 39: “Nod when the wine isn’t faulty, and the server will pour it.” For line 142,
see fix 7.

**6. “Price” means two different things.**
Page 2, line 25: “The price band you set before reading any names.” Page 5, line 110: “Price
is what the restaurant charges for a bottle or glass.” The Host notices the term change
between pages. The page 2 row is an instruction, not a definition.
Rewrite line 25: “| Price | What the restaurant charges for a bottle or glass. |”

**7. Sending back a bottle you just don’t like.**
Page 6, lines 142 to 143: “If it’s sound and you don’t like it, you can still ask kindly about
another bottle.” The Expert disbelieves this as general advice and winces on the restaurant’s
behalf. The Host wonders whether they pay for both bottles. The guide gives no limit.
Rewrite lines 142 to 143: “The taste is for faults. If a bottle under $100 has no fault but
you don’t like it, one wine site says it’s reasonable to ask for another.”

**8. Saying the budget aloud in front of guests.**
Page 5, line 111: “Say it plainly when you ask for help.” The Host at a large table, perhaps
with clients, won’t say a number out loud and skips the advice. The rewrite is a method with
no factual claim.
Rewrite line 111, second sentence: “Say it, or point to a price on the list.”

**9. The Grape page has claims the Expert rejects.**
Page 4, lines 69 to 71. “A name such as Pinot Noir before the producer or place” is often
false, because many lists put the producer first. “Grapes differ in body” makes the grape the
only cause, when alcohol counts too. “Pinot Noir is a light red” has many exceptions.
Rewrite line 69: “A name such as Pinot Noir or Chardonnay.”
Rewrite line 70, second sentence: “Body is how heavy and rich a wine tastes. Grape and
alcohol both affect it.”
Rewrite line 71: “Ask for light or full. Pinot Noir is usually a light red and Cabernet
Sauvignon a full one, while Chardonnay is often a full white.”

**10. “Corked” reads as “has a cork”.**
Page 6, line 130: “Corked wine smells musty, like wet cardboard.” The Diner doesn’t know that
corked names a fault. A few lines later the cork question makes the confusion worse.
Rewrite line 130: “A taste is a small pour used to check for faults. One fault, corked wine,
smells musty, like wet cardboard.”

## Page by page

### Page 1: Cover

| Reader | Stops at | Why |
|---|---|---|
| Diner | nothing | The title and five tiles tell them what’s inside. |
| Expert | nothing | |
| Host | nothing | |

Rewrite: none.

### Page 2: How do you order wine for the table?

| Reader | Stops at | Why |
|---|---|---|
| Diner | “Five terms cover most of the job.” (line 17) | The sentence counts the guide’s own table and gives no new information. The first paragraph already reassures them. |
| Expert | “Dry \| A wine with no sugar you can taste.” (line 24) | Accepts it. Notes rosé is missing from “white, red or sparkling” (line 13) but doesn’t stop. |
| Host | “Price \| The price band you set before reading any names.” (line 25) | An instruction, not a definition. Page 5 defines Price differently (fix 6). |

Rewrite: delete lines 17 to 18. Line 25 as in fix 6.

### Page 3: How does ordering go?

| Reader | Stops at | Why |
|---|---|---|
| Diner | “what you like and don’t like” (line 36) | Has no answer (fix 1). Then finds no step for saying the order (fix 2). “Sound” on line 39 is new (fix 5). |
| Expert | “Find that price, then look at whites, reds or sparkling wines.” (line 35) | Most lists are arranged by style or region, with prices beside each wine. You can’t “find that price” first. |
| Host | “Make sure the producer, wine and year match what you ordered.” (line 37) | Doesn’t say why the year matters. A different year can change the price, which is the Host’s concern. |

The tip on line 42 works for the Host. The Expert accepts it.

Rewrite line 35: “Note the whites, reds or sparkling wines within your price band.”
Rewrite line 37: “Make sure the producer, wine and year match what you ordered. Years can
differ in price.”
Lines 36 and 39 as in fixes 1, 2 and 5.

### Page 4: Wine list, Grape

| Reader | Stops at | Why |
|---|---|---|
| Diner | “Wines by the glass are sold one glass at a time.” (line 62) | Says nothing they didn’t know. Wines by the glass are part of the wine list (line 50), so “Confused with” has nothing to separate. |
| Diner | “Place names instead of grapes” (line 78) and “Region” (line 80) | The same idea gets two names on one page. |
| Expert | lines 69 to 71 | See fix 9. |
| Host | nothing | |

Rewrite lines 62 to 63: “Wines by the glass suit a table whose dishes need different
wines.”
Rewrite line 78: “Regions instead of grapes”.
Rewrite lines 82 to 83: “Some wines are listed by region instead of grape. Ask the server
which grape and style the region means.”
Lines 69 to 71 as in fix 9.

### Page 5: Dry, Price

| Reader | Stops at | Why |
|---|---|---|
| Diner | “A drying feel is tannin” (line 98) | Tannin is never explained. The point they need is only that the drying feel isn’t about sugar. |
| Diner | “Second-cheapest bottle” (line 120) | Never heard the belief, so the box answers a question they didn’t have. The Host does care, so keep it and fix the wording (fix 3). |
| Expert | “as in many Rieslings” (line 91) | Many Rieslings are fully dry. “Some” is safer. |
| Expert | “rule out most of the list” (line 111) | Overstated. |
| Host | “Keeping your budget secret” (line 118) and “Pick your range first” (line 51) | Budget, range and price band all name one thing. |

Rewrite line 91: “Say dry if you want no sweetness. Ask for off-dry if you’d like a little, as
in some Rieslings.”
Rewrite line 98: “A drying feel in the mouth”.
Rewrite lines 102 to 103: “A dry wine isn’t sweet. A wine can also feel drying in your mouth,
which has nothing to do with sugar.”
Rewrite line 111, first sentence: “A price band helps the server narrow the list.”
Rewrite line 118: “Keeping your price band secret”.
Rewrite line 51: “Pick your price band first, then look at the names.”
Line 123 as in fix 3.

### Page 6: Taste, Common questions

| Reader | Stops at | Why |
|---|---|---|
| Diner | “Corked wine” (line 130) | See fix 10. |
| Diner | “Do I smell the cork? \| No.” (line 152) | The server has just put the cork in front of them. “No” reads like a rule they might break. |
| Diner | “musty, mouldy or flat” (line 131) | Could read “flat” as “no bubbles”. Low. Keep the source’s word. |
| Expert | lines 142 to 143 | See fix 7. |
| Expert | “The taste checks the bottle, not your choice.” (line 131) | Repeats line 130 and line 142. |
| Host | “A glass of something sparkling to start gives you a few minutes.” (line 149) | At a large table this is an extra round on the bill, offered only to buy time. |
| Host | “For a large table, order a few bottles.” (line 150) | Reads as a quantity rule. The reason, that guests can match their dishes, is missing. By the glass also repeats page 4. |

Rewrite line 131: “If the wine smells musty, mouldy or flat, ask for another bottle.”
Rewrite line 149: “No. Take your time with the list.”
Rewrite line 150: “By the glass suits very different dishes. At a large table, a few bottles
let guests match their dishes.”
Rewrite line 152: “You don’t need to. Little can be learned from smelling it, and presenting
the cork is mostly for show.”
Lines 130, 142 to 143 and 151 as in fixes 4, 7 and 10.

### Page 7: Sources, back cover

| Reader | Stops at | Why |
|---|---|---|
| Diner | nothing | |
| Expert | “Wine Folly, How to Order Wine at a Restaurant · October 2026” (line 166) | That page has no date. October 2026 is the date it was read, unlike every other row. The NIAAA row on line 168 has the same problem. |
| Host | nothing | |

In the PDF, the NIAAA address breaks mid-word (“how-many-drink / s-are-common-containers”)
and “August 2024 ·” sits alone on a line.

Rewrite lines 166 and 168: replace “October 2026” with “No date”. Builder: break addresses
at a slash or hyphen.

## Voice pass

| Line | Text | Rule | Rewrite |
|---|---|---|---|
| 17 | “Five terms cover most of the job.” | No slogans; nothing about the guide itself | Delete lines 17 to 18. |
| 51, 118 | “Pick your range first”, “Keeping your budget secret” | Each part has one name | “Pick your price band first, then look at the names.” “Keeping your price band secret” |
| 62 | “Wines by the glass are sold one glass at a time.” | Each paragraph answers the reader’s next question | Delete. Line 63: “Wines by the glass suit a table whose dishes need different wines.” |
| 71 | “A few names cover a lot.” | No slogans | “Ask for light or full.” |
| 78, 82, 83 | “Place names”, “by place”, “a place name” | Each part has one name (the heading says Region) | As on page 4. |
| 130 | “the small pour that checks the wine isn’t faulty” | No personification | “A taste is a small pour used to check for faults.” |
| 131 | “The taste checks the bottle, not your choice.” | No “not X but Y” flourishes; no personification | Delete. |
| 142 | “The taste tells you whether the wine is sound.” | No personification | “The taste is for faults.” |
| 14, 131, 138 | “recognize” and “mouldy” | One spelling system | “recognise” (to match “mouldy”, the source’s word), or “moldy” throughout. |

No row sentence starts with “It”, “Its”, “They” or “This”. There are no em dashes,
semicolons or exclamation marks.

## Verdict

The Diner would finish and get through the order if fixes 1, 2, 5 and 10 are made. As it
stands, they reach the server with no words for what they like and no step for naming the
wine. The Expert would finish but stop trusting the guide at the Grape page and the
send-back advice. Both problems are small and fixable from the sources. The Host would take
away the bottle count and the price-band habit, but would miss the most useful price fact,
mid-range markups, unless fix 4 is made.

## Word ledger

| Lines | Change |
|---|---|
| 17 to 18 | −24 |
| 36, plus new Order row | +5, +11 |
| 37 | +5 |
| 49 (fidelity, optional) | −3 |
| 51, 118 | +1, +1 |
| 62 to 63 | −10 |
| 69, 70, 71 | −4, +2, 0 |
| 78, 82 to 83 | −1, −3 |
| 91 | −2 |
| 98, 102 to 103 | +1, +1 |
| 110 (fidelity S2) | +4 |
| 111 | −2, +2 |
| 123 | +4 |
| 130, 131 | +1, −8 |
| 142 to 143 | +3 |
| 149, 150, 151, 152 | −12, 0, −1, +3 |
| Net | about −26 |
