// The map at the top of the landing page: a 3 x 3 grid with the catalog guide in the middle and the eight series
// groups around it. src/data/groups.json lists them:
//
//   center   the id of the guide in the middle (the catalog of the series)
//   groups   eight groups in reading order, left to right and top to bottom, skipping the middle:
//            id      a stable slug (the cell's data-group, and later the name of its illustration)
//            name    the group's name as shown
//            guides  the ids of its guides in public/guides.json, in the order shown
//            coming  (optional) titles of guides not yet published, shown after the guides
//            image   (optional, for later) the group's small black-and-white illustration, a path under public/
//
// Every guide in guides.json has to be in exactly one place on the map, so a new guide can't drop off it unseen.
// checkGroups throws, and so fails the build, when one isn't.

const CELLS = 8;

/**
 * Checks the groups against the guides and returns the cells to draw: the center guide, then each group with its
 * guides looked up and its place in the grid (row and column, 1 to 3).
 *
 * @template {{ id: string }} G
 * @param {{ center: string, groups: { id: string, name: string, guides: string[], coming?: string[], image?: string }[] }} data
 * @param {G[]} guides
 */
export function checkGroups(data, guides) {
  const problems = [];
  const byId = new Map(guides.map((guide) => [guide.id, guide]));
  const groups = data.groups ?? [];

  if (!byId.has(data.center)) problems.push(`the center guide "${data.center}" is not in guides.json`);
  if (groups.length !== CELLS) problems.push(`there are ${groups.length} groups; the map has room for ${CELLS}`);

  const slugs = new Set();
  // Where each guide is placed, as the names of the places.
  const places = new Map([[data.center, ["the center"]]]);
  for (const group of groups) {
    if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(group.id ?? "")) {
      problems.push(`group "${group.name}" needs an id in lowercase-with-hyphens, not "${group.id}"`);
    }
    if (slugs.has(group.id)) problems.push(`two groups have the id "${group.id}"`);
    slugs.add(group.id);
    if (!group.name) problems.push(`group "${group.id}" has no name`);
    for (const id of group.guides ?? []) {
      if (!byId.has(id)) problems.push(`group "${group.name}" lists "${id}", which is not in guides.json`);
      places.set(id, [...(places.get(id) ?? []), `"${group.name}"`]);
    }
  }
  for (const guide of guides) {
    const where = places.get(guide.id) ?? [];
    if (!where.length) problems.push(`guide "${guide.id}" is in no group`);
    if (where.length > 1) problems.push(`guide "${guide.id}" is in ${where.join(" and ")}`);
  }

  if (problems.length) {
    throw new Error(
      `src/data/groups.json doesn't match public/guides.json:\n  - ${problems.join("\n  - ")}\n` +
        "Put every guide in exactly one group (or the center), and list only guides that are in guides.json.",
    );
  }

  return {
    center: byId.get(data.center),
    groups: groups.map((group, index) => {
      // Cells 0 to 8 in reading order; the middle one (4) is the center's.
      const cell = index < 4 ? index : index + 1;
      return {
        ...group,
        row: Math.floor(cell / 3) + 1,
        column: (cell % 3) + 1,
        guides: (group.guides ?? []).map((id) => byId.get(id)),
        coming: group.coming ?? [],
      };
    }),
  };
}
