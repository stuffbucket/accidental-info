---
name: accidental-guide-manage
description: Manage the Accidental Guides portfolio: place proposals in the taxonomy, reserve stable slugs and map codes, move guides through planned, draft and published states, and verify workspace, site and release metadata. Use when adding, moving, publishing, retiring or inventorying guides, or when changing collections and groups.
metadata:
  series: Accidental Guides
  version: "1.0"
---

# Manage the guide portfolio

The portfolio has one public taxonomy and one lifecycle. Manage both before changing a guide folder.

Read [../../taxonomy.md](../../taxonomy.md) and [references/lifecycle.md](references/lifecycle.md) first.

## Add a proposal

1. Write the reader's one question and a title of six words or fewer.
2. Choose one collection and one group using the taxonomy, not the provider or tool used in the example.
3. Choose a stable lowercase slug. Search guides, drafts, `coming` entries and release tags before using it.
4. Add the proposal under `coming` in `site/src/data/collections.json`.
5. For a mapped collection, reserve a unique two-letter map code. Do not reuse a family or concept code.
6. Run `python3 scripts/check_portfolio.py` from this skill's folder, or pass `--root`.
7. Use `accidental-guide-plan` to choose concepts and create the draft.

## Change state

- **Planned to draft:** create `drafts/<slug>/`, then run `pnpm sync`. The built draft is promoted in place automatically.
- **Draft to published:** finish review, move the folder to `guides/<slug>/`, run `pnpm sync`, build and test. Keep the slug, map code and taxonomy placement.
- **Retired:** remove the public entry only after the release and links have a replacement. Never reuse its slug, map code or concept codes.

Do not move a published guide in the taxonomy as routine cleanup. Cover numbers currently follow taxonomy order. A move is a visible renumbering change across every later guide in that collection.

## Verify

Run in order:

```sh
python3 packages/editorial/skills/accidental-guide-manage/scripts/check_portfolio.py
python3 packages/editorial/skills/accidental-guide-manage/scripts/check_back_page.py
pnpm sync
pnpm test
pnpm build
```

The portfolio check covers taxonomy membership, IDs, map codes and built guide metadata. The back-page check keeps the contact, tagline, spacing and colophon order consistent in every builder. `pnpm sync` owns generated workspace files and cover metadata.
