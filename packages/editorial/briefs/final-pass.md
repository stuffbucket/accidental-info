# Final pass on a guide

Work from the repository root. The process skills are in `packages/editorial/skills/` (read
each SKILL.md you use, and use their scripts).

For each guide you're given, edit it in place. Don't regenerate it.

## Steps

1. **Registry.** Apply `packages/editorial/registry.md` (and `registry.json`) for this
   guide:
   - tile codes
   - color families and hex values
   - tiles that become "see the owning guide"

   A non-owner guide shows the tile and points to the owning guide by title in colon form ("An
   Accidental Guide to: Agent Skills"). It covers only what is specific to this guide.

   Settings has no owning guide. Each harness guide defines it in one plain line.

2. **Layout.** Bring the guide onto the newer layout of `guides/specs-and-reviews` (see the
   build skill's `references/design.md` and the plan skill's `references/page-kinds.md`):
   - grey blocks
   - one callout at most per page
   - fewer rules
   - packed pages

   Port the builder change into this guide's own `build_guide.py` and `build_docx.py` as the
   smallest diff in the existing idiom, then mark up `guide.md` to use it.

3. **Five minutes.** The body, excluding the sources appendix, reads in five minutes or less: about
   1,100 words. Measure with the build skill's `reading_time.py <slug>`, and leave out the
   sources pages. Cut detail and repetition, not clarity.

   Make text changes from a written edit list that has line numbers, by hand or with the
   write skill's optional `run_writer.sh`. Every edit list includes: "No mannered prose: the
   writing must not call attention to itself. Make no assumption that the reader is an
   expert." If an AI model edits the text, follow the disclosure rule in CONTRIBUTING.md.

4. **Lint.** Run the write skill's `lint_guide.py <slug>`, which reads the deny list it
   documents, and fix every hit.

5. **Version and build.**
   - Bump the minor version (`bump_version.py <slug> minor`).
   - Build with the build skill's `build_one.sh <slug>`. It must print "no overflow" and
     build the Word document.
   - Render every page and read it as a newcomer.
   - Update `expected.sha256` (`build_one.sh <slug> --update-hash`) and confirm it matches.

6. **Commit** only that guide's folder:
   - `git add <guide folder> && git commit -m "<plain message>"`
   - Retry if git reports `index.lock`. Never use `git stash`.
   - Commit the layout port and the text cut separately.

## Don't touch

- `agents-harnesses-skills-tools`
- `software-factories`
- any guide folder you weren't given

Reply in under 100 words per guide with:
- the version
- the page count
- the body word count
- the commits
