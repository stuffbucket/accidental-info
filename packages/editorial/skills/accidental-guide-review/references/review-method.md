# Review method

Four reviews, each run by a separate reviewer (a subagent or a person) that starts cold: it
gets only what the review lists, never the plan, the briefs or the conversation that made the
guide. A reviewer that knows what the guide meant to say can't see what it actually says.

Every finding names the `guide.md` line (or PDF page), quotes the text, says what's wrong in
one or two sentences, and gives a rewrite that follows the voice rules. The rewrites become
the next edit list, so make them usable word for word.

## 1. Reader panel

**Gets:** the built PDF (page images and `pdftotext` output) and `guide.md` for exact text.
Not the sources.

**Readers.** Read every page three times, once as each:

- **Exec.** A senior leader who has heard the terms in slide decks. Decides funding and
  organisation. Has five minutes.
- **Lead.** Runs a team of about ten, has used coding agents, skeptical. Decides process.
- **IC.** A senior engineer who uses agents every day, knows the base guide's terms and has
  no patience for fluff or hand-waving.

**Looks for:** where each reader stops: an undefined term, a jump in depth, a sentence that
says two different things on two pages, a claim the reader doesn't believe, a page that
answers a question nobody asked yet. Then a voice pass against `checklist.md`.

**Report:** [../templates/readers.md](../templates/readers.md). Top ten fixes first, most
serious first, then page by page.

## 2. Fidelity

**Gets:** `guide.md` and `sources.md` (and the raw pages behind it, if kept). Not the hype
notes.

**Checks** every factual claim against the sources. Verdicts:

| Verdict | Means |
|---|---|
| Wrong | The source says something different |
| Overreach | The guide says more, or more certainly, than the source |
| Unsourced | No source in `sources.md` supports it |
| Naming | The guide's term differs from the source's or the series' without saying so |
| Non-public | Internal or confidential material, or a name from the deny list |
| Stale | The source is dated, or the product has changed since, and the guide doesn't say "as of" |

**Report:** [../templates/fidelity.md](../templates/fidelity.md). Each finding quotes the
guide, quotes the source with its URL, gives the verdict and the corrected text.

## 3. Format leakage

**Gets:** `guide.md` and the page images, and nothing about the series, the form model or the
author. The reviewer reads as someone who has never seen an Accidental Guide.

**Looks for** text that is about the guide, its making or its form, instead of the topic:

| Code | Kind |
|---|---|
| SN | Self-narration: the guide, its sources, its tables, columns, figures or pages |
| UV | Unnamed voices: "speakers mean", "people say" |
| PV | Presenter voice: hooks, teasers, set-up and reveal, "they say X, we say Y" |
| BF | Borrowed framing: the form model's vocabulary (birds, species, field guide, travel) |
| TR | Trivia or history asides: who coined a term, an old paper |
| JG | Jargon, or a name the reader can't know at that point |
| TT | A terms-table row that is commentary, or a term the guide never uses |
| MP | Mannered prose (see the write skill's `banned-patterns.md`) |

Run `lint_guide.py` first; it catches most SN, UV, BF and MP markers. A zero-shot text
classifier can be a further first pass, but in practice it fires on topic, not form, and
misses most plain "this guide says" sentences. Reading is the check.

Also compare the PDF text with `guide.md`: text the builders print on their own (diagram
labels, cover lines) needs the same scan.

**Report:** [../templates/format-leakage.md](../templates/format-leakage.md). If there was
an earlier scan, start with what's left of it.

## 4. Series consistency

**Gets:** this guide and every guide it names or borrows words from, the base guide, and the
output of the plan skill's `list_concepts.py`.

**Checks:**

| Type | Looks for |
|---|---|
| Names | One concept with two names, or one name with two meanings, across guides |
| Ownership | A concept that is a key here and in another guide; a tile key that means two things |
| Contradictions | Two guides that say different things about the same fact |
| Cross-references | The colon form in the body; the referenced guide exists and says what this one claims |
| Front matter and form | Kicker, subtitle pattern, running footer, semver version, entry rows and labels match the series |
| Voice | Drift from the voice rules that the other guides don't have |

**Report:** [../templates/series-consistency.md](../templates/series-consistency.md). Each
finding quotes the lines in each guide and says which guide changes.

## A final cold read (optional)

Before publishing, one more reader with the PDF only, reporting blockers only: anything that
would make an exec, lead or IC stop reading or misunderstand. Same finding format.

## From findings to edits

1. Drop findings that contradict the author's rules or the base guide.
2. Where two reviews disagree, the author's feedback decides, then the sources.
3. Turn the rest into one edit list per guide (the write skill's `templates/edit-list.md`),
   with line numbers from the current file, grouped by section, replacement text word for
   word where you have it.
4. Run the writer, lint, build, commit. Re-run only the reviews whose findings were serious.

## Reviewer prompt

Give each reviewer this, filled in:

> You are reviewing one Accidental Guide, a five-minute guide for someone new to the topic.
> Read only the files listed here: <files>. Don't read anything else in the repository.
> Do the <review name> review described in <path to review-method.md>, section <n>, and write
> the report to <notes>/<review>.md using the template at <path>. Cite `guide.md` line numbers
> and quote the text exactly. Give a rewrite for every finding. No mannered prose in the
> rewrites: the writing must not call attention to itself.
