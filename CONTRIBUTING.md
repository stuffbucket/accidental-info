# Contributing

Most changes start as an issue.

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

## Start a draft

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
