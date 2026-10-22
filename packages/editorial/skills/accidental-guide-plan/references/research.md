# Research

Every fact in a guide comes from a public, official source that you fetched while writing
it. The notes go in `sources.md` in the guide's notes folder, and the writer may use no fact
that isn't there.

## What counts as a source

| Use | Don't use |
|---|---|
| The vendor's or project's own documentation, specification or changelog | Anything non-public: internal wikis, internal docs, chat, internal names |
| The project's own published posts, papers and repositories | Third-party summaries of the docs |
| Standards bodies and specifications | Your memory of how a product used to work |
| Published practitioner write-ups, for what people report doing (marked as such) | Vendor marketing, as a source of fact |

Hype goes in a separate file (`hype.md`) and never into `sources.md`. Claims from launch
posts, social media and conference talks are useful for knowing what readers have heard, but
reading them next to the primary material colours the notes. Keep them apart, and read the
primary material first.

## How to take notes

For each source, record:

- the title, the publisher and the URL;
- the date you fetched it (and the page's own date, if it has one);
- short verbatim excerpts, in quotes, for each fact you'll use: a sentence or two, not whole
  sections;
- anything the source doesn't say that a reader will ask about ("The docs don't say how
  long a session lasts.").

Group the notes by topic or by key concept, so the writer can find the facts for each page.
Use [../templates/sources.md](../templates/sources.md).

## Products that change

Harnesses and their settings change every few weeks. Where products differ or change often,
the guide says "as of <Month Year>", and the sources page says when the facts were checked.
When sources disagree, the guide says which source says what, then what to do.

## In the guide

- No direct quotes in the body, and no names of people. Keep the idea, drop the quote and the
  name.
- Sources are listed only on the last page: one line on when they were checked, then a table
  of source (publisher and title), date, and address without `https://`.
- List only sources the guide actually uses. A source nothing cites comes off the list.
