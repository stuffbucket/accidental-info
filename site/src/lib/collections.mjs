// The collections: the site's top level. src/data/collections.json lists them, in the order the landing page shows
// them. Each collection has:
//
//   id       a stable slug (the section's anchor on the landing page)
//   name     the collection's name as shown
//   line     (optional) one short line shown under the name
//   code     the two letters on its tile, like a part tile on a guide's cover ("Ai")
//   colour   its tile's colour, one of the guides' six: blue, purple, green, red, pink, yellow
//   image    (optional) an illustration, a path under public/; nothing is drawn until it is set
//   imageAlt (optional) its alt text; without it the illustration is treated as decoration
//
// and its guides, one of two ways:
//
//   guides   the ids of its guides in public/guides.json, in the order shown
//   coming   (optional) guides not built yet, as { "id", "title" }, shown after the guides. When a guide with
//            that id turns up in guides.json it is shown as a real guide in that place, and the title here is
//            no longer used, so a guide can be listed before it is written.
//
// or, for a collection with its own map page (Accidental Intelligence):
//
//   page     the map page, a path under the base ("intelligence/")
//   catalog  the id of the guide in the middle of the map (the catalog of the collection)
//   codes    the two letters on each guide's tile on the map, by id, coming guides included ("skills": "Sk")
//   groups   the groups around the catalog, in reading order, each with an id, a name, a colour (as above; its
//            guides' tiles take it) and guides and coming as above. On a wide screen the first ones go down the
//            left of the catalog and the rest down the right, split where the two sides balance.
//
// Every guide in guides.json has to be in exactly one collection, so a new guide can't drop off the site unseen,
// and an id under guides has to be in guides.json. checkCollections throws, and so fails the build, when not.

export const COLOURS = {
  blue: { base: "#0D99FF", band: "#0a7acc", ink: "#ffffff" },
  purple: { base: "#9747FF", band: "#7938cc", ink: "#ffffff" },
  green: { base: "#14AE5C", band: "#108b49", ink: "#ffffff" },
  red: { base: "#F24822", band: "#c1391b", ink: "#ffffff" },
  pink: { base: "#E83FBF", band: "#b93298", ink: "#ffffff" },
  yellow: { base: "#FFCD29", band: "#dbb023", ink: "#111111" },
};

const CODE = /^[A-Z][a-z0-9]$/;
const SLUG = /^[a-z0-9]+(-[a-z0-9]+)*$/;

/**
 * Checks the collections against the guides and returns them ready to draw. Each collection gets:
 *   guides  its guides from guides.json, in order (a "coming" guide that now exists is in its place here)
 *   coming  the { id, title } of its guides that don't exist yet
 *   entries both in the order listed, each { guide } or { coming }, a built coming guide in its place
 *   count   how many of its guides exist, drafts included
 *   map     for a collection with groups: { center, groups, codes }, each group with its colour and its own
 *           guides and coming
 *
 * @template {{ id: string }} G
 * @param {{ collections: any[] }} data
 * @param {G[]} guides
 */
export function checkCollections(data, guides) {
  const problems = [];
  const byId = new Map(guides.map((guide) => [guide.id, guide]));
  const collections = data.collections ?? [];
  // Where each id is listed, as the names of the places.
  const places = new Map();
  const place = (id, where) => places.set(id, [...(places.get(id) ?? []), where]);
  const slugs = new Set();

  // Resolves one list of guides and coming titles. A coming id that exists is promoted into the guides.
  const resolve = (owner, list, coming) => {
    const found = [];
    const later = [];
    // Both in the order listed: the guides, then the coming ones, each built one in its place.
    const entries = [];
    for (const id of list ?? []) {
      if (!byId.has(id)) {
        problems.push(`${owner} lists "${id}", which is not in guides.json (put it under "coming" until it is built)`);
      } else {
        found.push(byId.get(id));
        entries.push({ guide: byId.get(id) });
      }
      place(id, owner);
    }
    for (const entry of coming ?? []) {
      if (!SLUG.test(entry?.id ?? "") || !entry?.title) {
        problems.push(`${owner} has a coming guide without an id in lowercase-with-hyphens and a title`);
        continue;
      }
      if (byId.has(entry.id)) {
        found.push(byId.get(entry.id));
        entries.push({ guide: byId.get(entry.id) });
      } else {
        later.push({ id: entry.id, title: entry.title });
        entries.push({ coming: { id: entry.id, title: entry.title } });
      }
      place(entry.id, owner);
    }
    return { guides: found, coming: later, entries };
  };

  const out = collections.map((collection) => {
    const owner = `collection "${collection.name ?? collection.id}"`;
    if (!SLUG.test(collection.id ?? "")) {
      problems.push(`${owner} needs an id in lowercase-with-hyphens, not "${collection.id}"`);
    }
    if (slugs.has(collection.id)) problems.push(`two collections have the id "${collection.id}"`);
    slugs.add(collection.id);
    if (!collection.name) problems.push(`collection "${collection.id}" has no name`);
    if (!CODE.test(collection.code ?? "")) {
      problems.push(`${owner} needs a two-letter code like "Ai", not "${collection.code}"`);
    }
    if (!(collection.colour in COLOURS)) {
      problems.push(`${owner} needs a colour, one of ${Object.keys(COLOURS).join(", ")}`);
    }

    const shared = {
      id: collection.id,
      name: collection.name,
      line: collection.line ?? "",
      code: collection.code,
      colour: COLOURS[collection.colour] ?? COLOURS.blue,
      image: collection.image ?? null,
      imageAlt: collection.imageAlt ?? "",
      page: collection.page ?? null,
    };

    if (!collection.groups) {
      if (collection.catalog || collection.page) {
        problems.push(`${owner} has a catalog or a page but no groups for its map`);
      }
      const { guides: found, coming, entries } = resolve(owner, collection.guides, collection.coming);
      return { ...shared, guides: found, coming, entries, count: found.length, map: null };
    }

    // A collection with a map.
    if (collection.guides || collection.coming) {
      problems.push(`${owner} has groups, so its guides go in the groups, not in "guides" or "coming"`);
    }
    if (!collection.page) problems.push(`${owner} has groups but no page for its map`);
    if (!collection.groups.length) problems.push(`${owner} has no groups`);
    if (!byId.has(collection.catalog)) {
      problems.push(`${owner}'s catalog guide "${collection.catalog}" is not in guides.json`);
    }
    place(collection.catalog, `${owner} (its catalog)`);
    const center = byId.get(collection.catalog);
    const groupSlugs = new Set();
    const groups = collection.groups.map((group) => {
      const where = `group "${group.name ?? group.id}" in ${owner}`;
      if (!SLUG.test(group.id ?? "")) problems.push(`${where} needs an id in lowercase-with-hyphens`);
      if (groupSlugs.has(group.id)) problems.push(`two groups in ${owner} have the id "${group.id}"`);
      groupSlugs.add(group.id);
      if (!group.name) problems.push(`${where} has no name`);
      if (!(group.colour in COLOURS)) {
        problems.push(`${where} needs a colour, one of ${Object.keys(COLOURS).join(", ")}`);
      }
      return {
        id: group.id,
        name: group.name,
        colour: COLOURS[group.colour] ?? COLOURS.blue,
        image: group.image ?? null,
        ...resolve(where, group.guides, group.coming),
      };
    });
    // Every guide on the map, coming ones too, has its own two letters.
    const codes = collection.codes ?? {};
    const onMap = [
      collection.catalog,
      ...collection.groups.flatMap((group) => [...(group.guides ?? []), ...(group.coming ?? []).map((c) => c?.id)]),
    ];
    const seen = new Map();
    for (const id of onMap) {
      if (!CODE.test(codes[id] ?? "")) problems.push(`${owner} needs a two-letter code for "${id}" under "codes"`);
      else if (seen.has(codes[id])) problems.push(`${owner} gives "${seen.get(codes[id])}" and "${id}" the same code`);
      else seen.set(codes[id], id);
    }
    const found = [center, ...groups.flatMap((group) => group.guides)].filter(Boolean);
    return {
      ...shared,
      guides: found,
      coming: groups.flatMap((group) => group.coming),
      entries: [...(center ? [{ guide: center }] : []), ...groups.flatMap((group) => group.entries)],
      count: found.length,
      map: { center, groups, codes },
    };
  });

  for (const [id, where] of places) {
    if (where.length > 1) problems.push(`"${id}" is listed by ${where.join(" and ")}`);
  }
  for (const guide of guides) {
    if (!places.has(guide.id)) problems.push(`guide "${guide.id}" is in no collection`);
  }

  if (problems.length) {
    throw new Error(
      `src/data/collections.json doesn't match public/guides.json:\n  - ${problems.join("\n  - ")}\n` +
        "Put every guide in exactly one collection, and list a guide under guides only once it is built.",
    );
  }
  return out;
}
