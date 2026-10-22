# Writing instructions, round 1: An Accidental Guide to… Is My Houseplant Dying?

You are writing one file: `drafts/is-my-houseplant-dying/guide.md` (from your working directory it is `./guide.md`). It holds PLACEHOLDER text that shows the shape the builders expect. Replace every PLACEHOLDER with finished text. Don't touch any other file.

## Who it's for

Someone with one houseplant that looks unwell: drooping, yellowing or dropping leaves. Maybe a gift, maybe one they've had for years and feel slightly guilty about. They have no gardening background, and their first instinct is to water it. Plant names in Latin, fertilizer schedules and pest lists are out of scope.

## The question, and the answer in order

Is my houseplant dying?

1. Probably not yet. Most houseplant trouble comes from light and water, and both can be fixed.
2. A drooping plant can be thirsty or drowning. The signs overlap, so check the soil before you water.
3. Thirsty or drowning: the sign-by-sign table.
4. The parts that decide it: light, watering, the pot and its drainage, the roots.
5. Is it actually dead? Checks on stems and roots, and what to do if part of it is still alive.

Use "thirsty" for underwatered and "drowning" for overwatered, every time, after saying once what each means.

## Section notes

- `{#why}` first paragraph: about 50 words, the site's summary; it must stand alone. Second paragraph: about 45 words. Terms table: one sentence per part.
- `{#fit}` "Thirsty or drowning?": one paragraph (about 35 words), then the three-column table (Sign, Thirsty, Drowning) with rows Soil, Leaves, Stems, Roots; each cell a few words, 3 to 8. Then the tip callout: one or two sentences (for example the finger test, if sourced).
- Entries: about 100 to 120 words each. Field marks are three short answers (Check by, Healthy, Trouble), a few words each.
- `{#apart}` "Is it actually dead?": one intro sentence, then three rows of checks (Check, Still alive, Dead), each cell a few words, then one closing sentence on what to do with a plant that is partly alive (cut back to healthy tissue, repot, or take a cutting, only as sourced).

## Read first, in this order

1. `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`: the author's feedback. Binding.
2. `packages/editorial/skills/accidental-guide-write/references/voice.md`: his voice. Binding.
3. `packages/editorial/skills/accidental-guide-write/references/banned-patterns.md`: what never goes in, and the Markdown rules the builders need.
4. `guides/specs-and-reviews/guide.md`: a finished guide in the same layout. Copy its length, rhythm and row style, not its topic.
5. `drafts/is-my-houseplant-dying/notes/plan.md`: the page plan. Follow it.
6. `drafts/is-my-houseplant-dying/notes/sources.md`: every fact you may use. Use no fact that isn't there. Where makers or models differ, say so plainly and tell the reader to check their own label or manual.

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

Replace the single PLACEHOLDER row of the Sources table with one row per source in the "For the sources page" table at the end of `drafts/is-my-houseplant-dying/notes/sources.md`, in that order, with only sources the guide actually uses. Keep the intro sentence "These public sources were checked in October 2026."

When you're done, reply with one line: done.

## Facts to watch (all from sources.md)

- Watering problems are the most common houseplant trouble: overwatering is called the main cause of death of potted plants (Clemson) and the number one way people kill houseplants (UF). Light is the factor that most often limits growth (Iowa State, Missouri). Don't say most problems are light problems.
- The finger test: feel the soil about an inch, or a few centimetres, down (first knuckle). Dry there means water. Pot weight helps: a dry pot feels lighter.
- Water thoroughly until it runs out of the bottom, then empty the saucer or outer pot. Never leave a pot standing in water. Pots need a drainage hole; gravel in the bottom doesn't replace one. A decorative outer pot can hide standing water.
- Wilting can mean either thirsty or drowning, and watering a drowning plant makes it worse.
- Thirsty: dry soil, possibly pulled away from the pot sides; wilting; crisp brown leaf edges; older lower leaves yellow and fall first.
- Drowning: wet soil; wilting or yellowing of lower and inner leaves; old and new leaves yellowing and dropping at the same time; stem rot; dark, soft roots with a sour smell; tiny black flies (fungus gnats).
- Healthy roots are white or light-coloured and firm. Rotten roots are brown or black and soft.
- Light: too little gives long, weak, leaning growth, pale or smaller leaves and lower leaves yellowing and falling. Too much gives brown scorched or bleached patches. Light drops quickly with distance from a window. In the northern hemisphere, south windows are usually brightest and north windows darkest (sources are northern-hemisphere; say so if you name a direction). Winter light is weaker, so many plants do better closer to a bright window in winter.
- A plant moved to a darker spot can drop and yellow leaves while it adjusts; it takes time.
- Is it dead: cut out rotten parts and replant the healthy sections, take cuttings and root them, and throw away severely damaged plants (Maryland). The scratch test (green or cream and moist under the bark means alive; brown and brittle means that part is dead) comes from an outdoor-shrub source, so present it for woody stems only. A firm crown with pale tissue may be alive; a soft, hollow, black or foul-smelling one is unlikely to recover.
- Many houseplants recover quickly once their conditions improve (RHS).
- Water less often in a cool room and in winter when growth slows, but check the soil rather than going by a schedule (RHS).
- Keep the Sources table to the sources you use, at most ten.
