// Starlight gives every Markdown table `display: block; overflow: auto`, so a table wider than the column
// scrolls sideways. A keyboard user can only scroll it if it can take focus (axe: scrollable-region-focusable).
// This Sätteri hast plugin gives each table tabindex="0" and a name: the heading above it, or the page title.
//
// In a table of three or more columns it also copies each column's heading onto that column's cells as
// data-label. On a narrow screen site/src/styles/tables.css shows such a table as one card per row, with the
// label in front of each value, so the table does not have to scroll. And it marks long code in a cell, such as a
// SHA-256, with data-break, so that only those values break across lines and short names stay whole.

const HEADINGS = ["h1", "h2", "h3", "h4", "h5", "h6"];
const CELLS = new Set(["td", "th"]);

/** Tables with fewer columns stay tables on a narrow screen; their text wraps. */
export const STACK_COLUMNS = 3;

/** Code this long with no spaces may break anywhere in a table cell. A shorter name stays whole. */
export const LONG_CODE = 20;

/** A plugin factory: Sätteri calls it once per document, so `heading` starts empty on each page. */
export function tableFocus() {
  let heading = null;
  // The column headings of the table being visited, and the column of the next cell in the current row.
  let labels = [];
  let column = 0;
  return {
    name: "table-focus",
    element: {
      // Sätteri visits the matched elements in document order, so a table comes before its rows and cells.
      filter: [...HEADINGS, "table", "tr", "th", "td", "code"],
      visit(node, ctx) {
        switch (node.tagName) {
          case "table": {
            const title = ctx.data?.astro?.frontmatter?.title;
            ctx.setProperty(node, "tabIndex", 0);
            ctx.setProperty(node, "ariaLabel", heading ?? title ?? "Table");
            labels = [];
            return;
          }
          case "tr":
            column = 0;
            return;
          case "th":
            labels[column++] = ctx.textContent(node).trim();
            return;
          case "td": {
            const label = labels[column++];
            if (label && labels.length >= STACK_COLUMNS) ctx.setProperty(node, "dataLabel", label);
            return;
          }
          case "code": {
            // In a cell, or in a link in a cell.
            const parent = ctx.parent(node);
            const cell = CELLS.has(parent?.tagName) ? parent : parent && ctx.parent(parent);
            if (!CELLS.has(cell?.tagName)) return;
            const text = ctx.textContent(node);
            if (text.length >= LONG_CODE && !/\s/.test(text)) ctx.setProperty(node, "dataBreak", "");
            return;
          }
          default:
            heading = ctx.textContent(node).trim() || heading;
        }
      },
    },
  };
}

/** An Astro integration that adds the plugin to the Markdown and MDX pipeline, next to Starlight's. */
export default function tableFocusIntegration() {
  return {
    name: "table-focus",
    hooks: {
      "astro:config:setup": ({ config, logger }) => {
        const plugins = config.markdown.processor?.options?.hastPlugins;
        if (!Array.isArray(plugins)) {
          logger.warn("the Markdown processor takes no hast plugins; tables will not be focusable");
          return;
        }
        plugins.push(tableFocus);
      },
    },
  };
}
