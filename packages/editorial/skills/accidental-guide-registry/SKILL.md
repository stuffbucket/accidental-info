---
name: accidental-guide-registry
description: Allocate and maintain Accidental Guides concept ownership, two-letter tile codes and colour families. Use before naming a guide's key concepts, when adding or reusing a tile, when resolving a terminology collision, or when registry.md and registry.json may disagree.
metadata:
  series: Accidental Guides
  version: "1.0"
---

# Manage the concept registry

`packages/editorial/registry.json` is the canonical structured registry. `registry.md` is its reviewable human view plus the history behind earlier decisions.

Read [references/registry-policy.md](references/registry-policy.md) before allocating a concept.

## Allocate a concept

1. Search normalized concept names, aliases and current guide entries.
2. Reuse an existing concept only when the thing and meaning are the same.
3. If the meaning is new, choose one owning guide and one of the six families.
4. Choose an unused two-letter code. Family codes and retired codes stay reserved.
5. Add the owner appearance and any reference appearances to `registry.json`.
6. Run `python3 scripts/check_registry.py`.
7. Run `python3 scripts/render_registry.py` to refresh the generated table in `registry.md`.
8. Change the guide builders and hashes only after the registry diff is accepted.

## Rules

- One concept has one owner, code and family.
- A guide may use an owned concept as a plain word without a tile.
- A repeated tile keeps the registry code and family and points to the owner.
- A provider's name for an existing thing is an alias, not automatically a new concept.
- A code is never recycled.
- A broad term is split only when readers meet two different things that need different explanations.

## Verify

```sh
python3 packages/editorial/skills/accidental-guide-registry/scripts/check_registry.py
python3 packages/editorial/skills/accidental-guide-registry/scripts/render_registry.py --check
```
