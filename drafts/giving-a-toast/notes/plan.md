# Plan: An Accidental Guide to… Giving a Toast

Slug `giving-a-toast`. Builder copied with `new_guide.py` from `drafts/hosting-thanksgiving/`
(itself `guides/specs-and-reviews/` with a blocks-only overview page and no mono
literals). Target about 900 to 1,000 printed words, 7 pages. Facts only from `sources.md`.

## The reader

Someone who has just been asked to "say a few words": at a wedding, a birthday dinner, a
leaving do or a family meal. They aren't a speaker and are dreading it. They want to know
how long to talk, what to say first, which story to tell and what will make the room wince.

## The question

How do I give a toast?

## The answer, in order

1. A toast is short: who you are, one story, a wish, and a raised glass. Two to three
   minutes.
2. How it goes, step by step: get attention, stand and lift your glass, the opening, the
   story, the last line, everyone drinks.
3. Opening: your name and how you know the person you're toasting.
4. Story: one short story or one quality, positive, that everyone in the room can follow.
5. Last line: raise your glass and invite everyone to join: "To Sam."
6. Length: two to three minutes. Write it down and practise out loud.
7. What to leave out: inside jokes, embarrassing stories, anything too personal, a roast,
   rambling.
8. Common questions: who goes first, do I stand, do I need a drink, what does the person
   being toasted do.

## Key concepts

Four, each with a page and a filled tile. Colours follow the registry's families.

| No. | Part | Key | Colour | Meaning (draft) |
|---|---|---|---|---|
| 01 | Opening | Op | purple (Wr, things you write down) | Your name and how you know the person. |
| 02 | Story | Sy | purple (Wr) | One short, kind story or quality. |
| 03 | Last line | Lt | purple (Wr) | The line that raises the glasses. |
| 04 | Length | Ln | blue (Nu, numbers and claims) | Two to three minutes. |

The three spoken parts are all words you prepare and write on a card, so they share a
colour. Codes checked against `registry.md` and `list_concepts.py`: `Op`, `Sy`, `Lt`, `Ln`
are unused (`St` is Startup context, `Cl` Closed loop. Last line was `Ll` in the first draft, changed to `Lt` because `Ll` reads as "LI" in the typeface).

Plain words, no tile: host, the person you're toasting, glass, roast, notecard.

## Pages

| Page | Section | What it does | Words |
|---|---|---|---|
| 1 | front matter | Cover | 45 |
| 2 | `{#why}` What goes in a toast? | Two paragraphs, terms in a grey block | 130 |
| 3 | `{#fit}` How does a toast go? | One sentence, grey Step / What to do table, callout | 130 |
| 4–5 | `{#entry}` × 4 | Two to a page | 4 × 90 |
| 6 | `{#apart}` What do I leave out? and `{#other}` Common questions | Two grey tables, packed on one page if they fit | 180 |
| 7 | `{#sources}` Sources | Four sources | 60 |
| | | Total | about 905 |

No diagram: the steps table is the visual.

## Entries

Field mark labels, the same on every entry: Rule of thumb, Watch for.

| Entry | Identify by | Confused with |
|---|---|---|
| Opening | The first sentence after the room goes quiet | Getting attention (comes first, no words needed) |
| Story | The one memory or quality you tell | Roast |
| Last line | "To Sam" with your glass raised | Reply (the person toasted smiles, nods or says thank you) |
| Length | The time from first word to raised glass | Casual toast (a few heartfelt sentences, "To our hosts"; changed from One-line toast in EDITS-3) |

The pairs were checked against `sources.md`: each difference is stated there.

## Tone

Reassuring and dry. One light line at most. The reader is nervous; the guide should make a
toast sound small and doable, which the sources support ("Even a few heartfelt sentences
will make an impact").

## Builder changes

- `build_guide.py`: `PART_FAMILY`, `NAME2MONO`, `COVER_LINES` ("Giving a", "Toast"),
  `SEQ_TILE` (unused).
- `content.py`: the voice comment. `{#other}` is already supported (packed after `{#apart}`).

## The writer

`gpt-5.6-sol-fast` through `run_writer.sh`: `writer-round1.md`, then `EDITS-2.md` and on.
