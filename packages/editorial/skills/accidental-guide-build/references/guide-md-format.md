# The Markdown in guide.md

`guide.md` holds every word and the data the diagrams are drawn from. It has no layout.
This is everything the parsers understand; anything else is printed literally or breaks the
build. Each guide's own README says which constructs its builder reads, so check it too.

## Front matter

Line 1 is `---`. Each line is `key: value`, split at the first colon, with no quoting.

```
---
title: Lights-Off Software Factories
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to software factories where nobody reads the code, as of October 2026.
running_footer: Lights-Off Software Factories
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: friend@accidental.info · October 2026
version: 0.3.0
---
```

| Key | Used for |
|---|---|
| `title` | Cover, PDF metadata, colophon, site heading. Short and balanced, six words or fewer. |
| `kicker` | Always `An Accidental Guide to…`, with the ellipsis character. |
| `subtitle` | Cover and site. "A pocket-sized guide to …, as of <Month Year>." |
| `running_footer` | Footer on every inner page. Usually the title. |
| `edition` | The end page footer and the site: `oops@accidental.info · CC BY 4.0 · <Month Year>`, the address for mistakes, the text's license and the month. |
| `cover_footer` | The cover's footer: `friend@accidental.info · <Month Year>`. |
| `version` | Semver. The build fails without a valid one. |

## Sections

Each `#` heading starts a section and ends with `{#id}`, with optional `key=value` attributes:

```
# What is a lights-off<br/>software factory? {#why}
# Scenario {#entry num=01 mono=Sn}
```

- A `#` line without `{#id}` isn't a heading. It becomes text, or crashes the parser.
- `<br/>` in a title forces a line break in both the PDF and the Word document. Use it only in
  `#` titles.
- `entry` repeats, one per key concept, in file order. `num` is the entry number and `mono`
  the two-letter tile key.
- The order of sections in the file doesn't set the order of pages. `build()` does.

## Paragraphs, subheads and tables

- Paragraphs are separated by blank lines and can wrap over several lines.
- `## Heading` is a subhead. In an entry, `## Field marks` comes before its table, and
  `## Confused with: Name` names the other thing, followed by one paragraph.
- Tables are pipe tables. The separator row is skipped and the first row is the header. Where
  the PDF prints no header, the header is a label for editors (`Term`, `Field`, `Question`,
  `Source`). A cell can't contain `|`.

| Where | Columns |
|---|---|
| `{#why}` terms table | Term, Meaning |
| Entry, first table | Field, Text; rows exactly Identify by, What, So what |
| Entry, field marks | Field, Short answer, Detail; the same labels on every entry |
| Table pages | One header row that is printed; then one closing paragraph after the table |
| `{#sources}` | Source, Date, Address (no `https://`) |

A Short answer cell doesn't end with a full stop. The builder adds one and bolds it.

## Grey blocks and callouts (builders that support them)

- Lines that start with `> ` are a grey block: paragraphs and tables on a light grey panel.
- A `> ` block whose first line is `> [!TIP]`, `> [!NOTE]` or `> [!WARNING]` is a callout: one
  paragraph in an outlined box, led by "Tip.", "Note." or "Watch out." At most one per page.
- In an entry, a field marks table inside a grey block prints as a three-column grid of
  label and short answer. The Detail column can be left out.

## The sequence diagram (builders that support it)

A fenced block; the word after the backticks is ignored.

````
```diagram
part Person doing it |  |
part Spec | Sp | the plan
part Work item | Wi
band Write it down
msg 0 -> 1: writes the spec
msg 1 --> 0: acceptance criteria
note 1: kept in the repo
```
````

- `part Label | Key | caption` adds a column, counted from 0. An empty key draws plain text
  with no tile, for things that aren't one of the guide's parts.
- `msg A -> B: label` is a request, drawn solid. `msg A --> B: label` is a result, dashed.
- `band Label` starts a labelled group. `note N: text` writes a note on part N's line.

## Literals and bold

Writers mark nothing. The builders apply style by rule:

- File names, paths and commands (`AGENTS.md`, `.claude/agents/`, `/compact`) are set in mono
  because `MONO_RE` matches them. Ordinary words with slashes ("and/or") come out in mono by
  mistake, so avoid them.
- Bold: titles, row labels, the first sentence of What and So what, each Short answer, the
  first column of tables.
- Part names that label a row, a step or a Confused with get their tile if they're in
  `NAME2MONO`.
