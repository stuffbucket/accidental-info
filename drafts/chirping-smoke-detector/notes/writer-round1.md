# Writing instructions, round 1: An Accidental Guide to… Smoke Detectors That Chirp

You are writing one file: `drafts/chirping-smoke-detector/guide.md` (from your working directory it is `./guide.md`). It holds PLACEHOLDER text that shows the shape the builders expect. Replace every PLACEHOLDER with finished text. Don't touch any other file.

## Who it's for

Someone at home, quite possibly at 2 a.m., with a single high chirp coming from somewhere in the house every half minute or so. They don't know which alarm it is, whether it's an emergency, or how to make it stop without breaking anything. They want to get back to bed, safely. Safety facts must be exactly what the sources say.

## The question, and the answer in order

Which smoke alarm is chirping, and how do I make it stop?

1. A single short chirp every 30 to 60 seconds is the alarm asking for attention, not a fire. The loud repeating pattern is the alarm sound, and that means get out.
2. The usual cause is a low battery. The other common cause is the alarm reaching its end of life, about 10 years after it was made.
3. Chirps often start in the small hours because a battery gives less power when the house cools at night.
4. Finding it: wait for the next chirp, look for the alarm whose light is blinking differently, narrow it down room by room. Interconnected alarms all sound for smoke, but only the one with the problem chirps.
5. The fix: a new battery, or a new alarm when it's past its date or has a sealed battery. Then press test. The hush button buys time and fixes nothing.
6. Never take an alarm down and leave it down.

Use "smoke alarm" in the body, every time (the word fire services and makers use). In the first paragraph you may say once that most people call it a smoke detector.

## Section notes

- `{#why}` first paragraph: about 50 words, the site's summary; it must stand alone. Second paragraph: about 45 words, the night-time cold effect and that the fix takes minutes once you know which one. Terms table: one sentence per part.
- `{#fit}` "Which one is it?": one paragraph (about 35 words), then the four steps (Wait, Look, Narrow it down, Check the date), one or two sentences each, then the warning callout (one or two sentences: never leave an alarm down; for a hardwired alarm, turn off its breaker before you take it off the ceiling, only if `sources.md` supports it).
- Entries: about 100 to 120 words each. Field marks are three short answers (Found on, Fixed by, Cannot), a few words each.
- `{#apart}` "What does the sound mean?": four rows. Sound, Means, Do this. Suggested rows, only if sourced: one chirp every 30 to 60 seconds; chirps that continue after a new battery or a chirp pattern the manual calls end of life; three long beeps repeating (smoke, get out); four beeps repeating on a combination alarm (carbon monoxide, get out to fresh air and call for help). Then one closing sentence.

## Read first, in this order

1. `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`: the author's feedback. Binding.
2. `packages/editorial/skills/accidental-guide-write/references/voice.md`: his voice. Binding.
3. `packages/editorial/skills/accidental-guide-write/references/banned-patterns.md`: what never goes in, and the Markdown rules the builders need.
4. `guides/specs-and-reviews/guide.md`: a finished guide in the same layout. Copy its length, rhythm and row style, not its topic.
5. `drafts/chirping-smoke-detector/notes/plan.md`: the page plan. Follow it.
6. `drafts/chirping-smoke-detector/notes/sources.md`: every fact you may use. Use no fact that isn't there. Where makers or models differ, say so plainly and tell the reader to check their own label or manual.

(Paths are relative to the repository root, which is two folders up from your working directory.)

## The series, and the tone

The series is "An Accidental Guide to…": a five-minute read for a reluctant or anxious reader who has just had this land on them. The spirit is warm and lightly self-deprecating, with dry understatement now and then, the way a kind friend who has been there would explain it. But the author's voice rules win every time: plain, short sentences, normal word order, nothing that calls attention to the writing. At most one light, dry line per page, and only where it helps the reader relax. No jokes that need setting up, no puns, no wordplay, no mannered prose. Assume no expertise.

No mannered prose: the writing must not call attention to itself. Make no assumption that the reader is an expert.

## Length

Five minutes front to back: about 950 words in guide.md, tables and sources included, which prints as about 1,050. Stay under the word budget for each page in the plan. Cut detail, not clarity. Short is good; staccato isn't.

## How to write it

- Regular English, "you" for the reader. Point first, then the reason ("X, so Y"; "When X, do Y").
- Build one idea at a time. No paragraph by list: a list goes in a table.
- Each part has one name, used every time (the names in the plan and the headings).
- Rows must read on their own: no sentence in a table cell starts with "It", "Its", "They" or "This".
- No quotes, no names of people, no brand praise or blame. Makers may be named only where the plan or sources need it to say who advises what (for example "Bosch and Miele say…"), and only plainly.
- No self-narration ("this guide", "this page", "below", "here's", "let's"), no rhetorical questions, no "not X but Y" flourishes, no em dashes, no semicolons, no exclamation marks, no rhythm triplets, no slogans, no kicker endings.
- Avoid: simply, just, really, actually, key, important, crucial, note that.

## Markdown rules the builders need

- Typographic apostrophes and quotes (’ “ ”). No backticks, no emphasis, no list lines, no "&", no "<" except the `<br/>` already in `#` titles, no slashes in ordinary words (write "and" or "or").
- No "e.g." or "i.e.".
- The first sentence of What and So what prints in bold up to the first ". ", so make it a complete short sentence that defines or answers on its own.
- A field marks Short answer cell is a few words with no full stop (the builder adds one and bolds it).
- A cell can't contain "|".
- The Confused with paragraph is two flat sentences.

## Keep the shape

Replace every PLACEHOLDER with finished text. Keep the front matter keys, every heading and its `{#id ...}`, the number of paragraphs in each section, table header rows, first-column labels (where given) and the field mark labels. Lines that start with "> " must keep their "> ". Don't add or remove sections, rows or paragraphs except where this brief says so. Don't touch any file except `./guide.md`.

## Sources page

Replace the single PLACEHOLDER row of the Sources table with one row per source in the "For the sources page" table at the end of `drafts/chirping-smoke-detector/notes/sources.md`, in that order, with only sources the guide actually uses. Keep the intro sentence "These public sources were checked in October 2026."

When you're done, reply with one line: done.

## Facts to watch (all from sources.md)

- Chirp timing varies by model: say "about every 30 to 60 seconds" and that the pattern for low battery, end of life and faults varies by model, so check the label or manual. Don't quote a single model's pattern as universal.
- Chirping that continues after a new battery means the alarm is at the end of its life (NFPA). Some alarms remember the weak battery: Kidde's reset is battery out, hold the test button for at least 15 seconds, battery back in. For a hardwired alarm, turn off the breaker first.
- Night chirps: a battery near the end of its life struggles more as the room cools, and most homes are coolest between 2 a.m. and 6 a.m. (Kidde, First Alert).
- Finding it: some alarms blink their light in a special pattern when the battery is low, to show which alarm needs it (First Alert); after a smoke alarm, only the alarm that sensed smoke flashes its red light (Kidde, First Alert). Interconnected alarms all sound together for smoke (NFPA, USFA). Don't state as a universal rule that only the faulty one chirps; say "usually".
- Sealed 10-year alarms: the battery can’t be replaced, so replace the whole alarm. Hardwired alarms usually have a backup battery to replace once a year. Replace any alarm 10 years from the manufacture date printed on the back, or if there is no date (NFPA, USFA).
- Hush: quiets a nuisance alarm for a few minutes (about 7 to 9, by model). On many models a press also quiets a low-battery chirp for some hours (8 to 24 in the manuals checked); then the chirp comes back. A hush button never fixes the cause.
- Never take the battery out or disconnect an alarm to stop the noise (USFA: a dead or missing battery is the same as no alarm). NFPA research: nearly three in five home fire deaths happen in homes with no smoke alarms or alarms that didn’t work, and missing, disconnected or dead batteries are the most common reason alarms fail. Use the research numbers only as the sources give them.
- Test at least once a month (NFPA, USFA); manuals ask for weekly. Say "at least once a month".
- Three long beeps repeating: smoke or fire, get out, call 9-1-1 (or your emergency number) and stay out. Four beeps repeating on a CO or combination alarm: carbon monoxide, go outside and call for help (NFPA).
- Keep the Sources table to the sources you use, at most ten.
