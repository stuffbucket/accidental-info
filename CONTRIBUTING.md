# Contributing

Most changes start as an issue. Corrections and topic suggestions are the main way to help,
and the quickest to act on.

## Suggest a guide

Open a [Suggest a guide](https://github.com/stuffbucket/accidentalguide/issues/new?template=suggest-a-guide.yml)
issue. Name the question the guide would answer, and who asks it.

## Report a mistake

- **A wrong fact:** open a [Something is wrong](https://github.com/stuffbucket/accidentalguide/issues/new?template=something-is-wrong.yml)
  issue. Name the guide, quote the sentence, and say what's true. Link a source if you have
  one.
- **A word used two ways:** every guide uses one name for each thing, and a word keeps one
  meaning in every guide. When a word means two things, open an
  [A word is used two ways](https://github.com/stuffbucket/accidentalguide/issues/new?template=word-used-two-ways.yml)
  issue and quote both places.

A small fix can also come as a pull request that changes the guide's `guide.md`.

## Write your own

The [Word template](https://accidental.info/accidental-guide-template.docx) is the guides'
layout as a Word document. Each place in it says what goes there: the reader's question, up
to six parts with their field marks, and the sources. Use it for your own team or class. The
template's text is under CC BY 4.0, like the guides.

## Sending us a guide

We publish a few guides from other writers. Not many, because each one takes a long time to
check.

1. Write it in the [Word template](https://accidental.info/accidental-guide-template.docx):
   one question, six parts at most, about a page each.
2. Open a [Send a guide](https://github.com/stuffbucket/accidentalguide/issues/new?template=send-a-guide.yml)
   issue and drag the `.docx` into the description field.

What we check:

- **A named person stands behind every sentence.** You wrote it or checked it, and you'll
  answer questions about it.
- **Every fact has a source you've read.** List them all. A link you haven't opened doesn't
  count, and neither does a source that doesn't say what the guide says.
- **It reads like the series.** Plain words, one name for each thing, and the rules under
  [Voice](#voice).

**AI.** A person writes and reviews every one of our guides, and AI does the grunt work:
finding sources, rough drafts and the builds. Every line is checked by that person before
it's published. You can work the same way. Say how you used AI in the form. What we won't take is text that
nobody has checked: made-up facts, sources that don't exist, or answers to our questions
that come straight from a chatbot.

**We may close a submission without comment,** when it's hard to check, skips the template,
or looks generated and unread. We don't debate closures. Accounts that keep sending that kind
of thing get blocked.

There's no payment, prize or ranking for submissions. By sending a guide you license it under
CC BY 4.0, so we can edit, publish and translate it.

## Start a draft

This is for people already writing with us. A guide from anyone else starts as a
[Send a guide](https://github.com/stuffbucket/accidentalguide/issues/new?template=send-a-guide.yml)
issue.


Install the tools once:

```sh
mise install
pnpm install
```

Copy a guide folder into `drafts/<slug>/`, without its built files. The slug is the guide's
name in lowercase words joined by hyphens. It names the files and the page's address.

```sh
rsync -a --exclude dist --exclude node_modules --exclude expected.sha256 \
  guides/software-factories/ drafts/<slug>/
```

Change `guide.md`: the front matter (title, subtitle, `version: 0.1.0`) and the text. The
guide's `README.md` describes the Markdown. Then add the draft to the workspace and build it:

```sh
pnpm sync
pnpm build
pnpm preview    # http://localhost:4321/accidentalguide/drafts/<slug>/
```

Open a pull request with the folder. A draft moves to `guides/` when it's finished.

## The build checks

`pnpm build` builds every guide and fails when:

- **Content runs past a page's bottom margin.** The build names the page. Shorten the text
  on that page or split it.
- **The PDF differs from `expected.sha256`.** The PDF build is deterministic, so the same
  text always gives the same bytes. When you change the text on purpose, copy the new hash
  from the build's `sha256 <hash>` line into the guide's `expected.sha256`, as
  `<hash>  <slug>.pdf`. A new draft has no `expected.sha256` until you write its first one.

Also bump the `version:` in the front matter (semver) when the text changes. Each new
version gets a GitHub release with its PDF and Word files.

`pnpm test` runs the tests. CI runs `pnpm turbo run build test` on every pull request.

## Voice

The guides' text follows these rules:

- Plain-spoken and direct, the way a colleague explains something over coffee.
- Contractions are fine.
- State the point, then the reason.
- No taglines, slogans, rhetorical questions, "not X but Y", em-dash asides, rhythm
  triplets or stage direction ("this page", "below").
- Rows must read on their own: no sentence starts with "it", "its", "they" or "this".
- Each field row leads with a short bold answer.
- Each term keeps one meaning.
- No quotes and no names of people in the body. Public sources go on the sources page only.
- No text about the guide itself: no "this guide", page numbers or descriptions of the
  layout.
