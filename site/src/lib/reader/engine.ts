// The guide reader's engine: lays a PDF's pages in a row or a column, scrolls them natively, zooms them with pinch,
// keys and buttons, turns the row into a column and back, and paints each page from the PDF's vectors at the
// screen's resolution.
//
// How it stays smooth:
// - The pages sit in one native scroller. Trackpads and touch scroll it on the compositor; nothing is measured or
//   moved by script while they do.
// - Pages are absolutely positioned from numbers this file computes, so nothing is measured while scrolling.
// - In a row a vertical wheel scrolls sideways: trackpad deltas pass straight through (batched into one write per
//   frame), and coarse mouse-wheel notches ease over a few frames, adding up while one is still moving.
// - PDF.js paints only after scrolling stops, and pauses between its slices while the pages move, so painting never
//   competes with a scroll. Until then each page shows its placeholder image, and after a zoom the last canvas
//   stretches.
// - A pinch scales the whole track with a CSS transform and re-lays the pages once, after the gesture settles.
// - The overlay scrollbar's thumb follows the scroll with a CSS scroll-driven animation where the browser has one.
// - Turning the layout animates each page's transform with the Web Animations API, on the compositor.
//
// The chrome reads state from attributes on <html>: data-layout ("horizontal" | "vertical"), and data-zooming,
// data-scrolling and data-rotating while those are happening. data-reader is "ready" once a page is painted from
// the PDF, or "fallback" if the PDF can't be loaded (the placeholders stay, and everything else still works).

import type { PDFDocumentProxy, PDFPageProxy, RenderTask } from "pdfjs-dist";

export interface ReaderOptions {
  url: string; // the PDF
  pageCount: number;
  pageAspect: number; // width / height of a page
  placeholder?: (n: number) => string; // URL of page n's low-res image, shown until the vector render lands
}

export type Layout = "horizontal" | "vertical";

export interface Reader {
  readonly page: number; // 1-based page at the reading position
  readonly pageCount: number;
  readonly zoom: number; // 1 = fit
  readonly layout: Layout;
  goTo(page: number, opts?: { smooth?: boolean }): void;
  next(): void;
  prev(): void;
  zoomIn(): void;
  zoomOut(): void;
  fit(): void;
  setZoom(z: number, focus?: { x: number; y: number }): void;
  setLayout(mode: Layout, opts?: { animate?: boolean }): void;
  on(event: "page" | "zoom" | "layout" | "ready", cb: () => void): () => void;
  destroy(): void;
}

type Event = "page" | "zoom" | "layout" | "ready";
type Point = { x: number; y: number };

const MIN_ZOOM = 0.5;
const MAX_ZOOM = 4;
const STEPS = [0.5, 0.67, 0.75, 0.9, 1, 1.1, 1.25, 1.5, 1.75, 2, 2.5, 3, 4];
// A column's page is never wider than this at zoom 1.
const MAX_FIT_WIDTH = 960;
// Pixels in one page's full canvas. Past this the full canvas is painted coarser and a second canvas paints just
// the part of the page in view at full resolution.
const MAX_FULL_PIXELS = 8_000_000;
// Pixels in all canvases together; the ones farthest from view go first.
const MAX_TOTAL_PIXELS = 40_000_000;
// Pages this far either side of the visible ones keep their canvases.
const KEEP = 2;
const SETTLE_MS = 150;
const SCROLL_IDLE_MS = 120;
// The turn between a row and a column: each page's flight, and the delay from one page to the next.
const TURN_MS = 520;
const TURN_STAGGER_MS = 50;
// The overlay scrollbar: its hit target across the bar (WCAG 2.2's minimum) and how long it stays after a scroll.
const BAR = 24;
const BAR_IDLE_MS = 1200;
const LAYOUT_KEY = "ag-reader-layout";

const clamp = (v: number, lo: number, hi: number) => Math.min(hi, Math.max(lo, v));
const lerp = (a: number, b: number, t: number) => a + (b - a) * t;

// Structural styles. The look belongs to reader.css; everything here is wrapped in :where() so any rule there wins.
const STYLE = `
:where(.reader-scroller){position:absolute;inset:0;overflow:auto;overscroll-behavior:contain;outline:none;
  touch-action:pan-x pan-y;scrollbar-width:none;scroll-timeline:--reader-sx x,--reader-sy y}
:where(.reader-scroller)::-webkit-scrollbar{display:none}
:where(.reader-track){position:relative;transform-origin:0 0}
:where(.reader-page){position:absolute;left:0;top:0;background:#fff;overflow:hidden;contain:strict;
  --scale-round-x:1px;--scale-round-y:1px;box-shadow:0 0 0 1px rgb(0 0 0 / .08),0 2px 12px rgb(0 0 0 / .12)}
:where(.reader-page)>img,:where(.reader-page)>canvas{position:absolute;left:0;top:0;width:100%;height:100%;
  display:block;user-select:none;-webkit-user-select:none;pointer-events:none}
:where(.reader-page)>img[hidden]{display:none}
:where(.reader-page)>canvas.reader-detail{width:auto;height:auto}
:where(.reader-page) .textLayer{position:absolute;inset:0;overflow:clip;line-height:1;text-align:initial;
  -webkit-text-size-adjust:none;text-size-adjust:none;forced-color-adjust:none;transform-origin:0 0;z-index:1;
  caret-color:CanvasText;--min-font-size:1;--text-scale-factor:calc(var(--total-scale-factor) * var(--min-font-size));
  --min-font-size-inv:calc(1 / var(--min-font-size))}
:where(.reader-page) .textLayer :is(span,br){color:transparent;position:absolute;white-space:pre;cursor:text;
  transform-origin:0% 0%;user-select:text;-webkit-user-select:text}
:where(.reader-page) .textLayer>:not(.markedContent),:where(.reader-page) .textLayer .markedContent span:not(.markedContent){
  z-index:1;--font-height:0;font-size:calc(var(--text-scale-factor) * var(--font-height));--scale-x:1;--rotate:0deg;
  transform:rotate(var(--rotate)) scaleX(var(--scale-x)) scale(var(--min-font-size-inv))}
:where(.reader-page) .textLayer .markedContent{display:contents}
:where(.reader-page) .textLayer ::selection{background:rgb(0 100 255 / .25);color:transparent}
:where(.reader-page) .textLayer br::selection{background:transparent}
:where(.reader-page) .textLayer .endOfContent{display:block;position:absolute;inset:100% 0 0;z-index:0;cursor:default;user-select:none}
:where(.reader-page) .textLayer.selecting .endOfContent{top:0}
:where([data-rotating] .reader-page) :is(.textLayer,.reader-links){display:none}
:where(.reader-links){position:absolute;inset:0;z-index:2;pointer-events:none}
:where(.reader-links)>a{position:absolute;pointer-events:auto;border-radius:2px}
:where(.reader-links)>a:hover{background:rgb(0 100 255 / .1)}
:where(.reader-track)>.reader-back{position:absolute;left:0;top:0;margin:0}
:where(.reader-scrollbar){position:absolute;z-index:5;background:transparent;touch-action:none;
  transition:opacity .2s ease,transform .25s cubic-bezier(.2,.7,.2,1)}
:where(.reader-scrollbar[data-axis=x]){left:8px;right:8px;bottom:0;height:${BAR}px}
:where(.reader-scrollbar[data-axis=y]){top:8px;bottom:8px;right:0;width:${BAR}px}
:where(.reader-scrollbar[data-hidden]){opacity:0;pointer-events:none}
:where(.reader-scrollbar[data-axis=x][data-hidden]){transform:translateY(100%)}
:where(.reader-scrollbar[data-axis=y][data-hidden]){transform:translateX(100%)}
:where(.reader-scrollbar-thumb){position:absolute;left:0;top:0;display:grid;place-items:center;animation:none linear both}
:where(.reader-scrollbar[data-axis=x]) .reader-scrollbar-thumb{height:${BAR}px;width:var(--thumb-len,${BAR}px)}
:where(.reader-scrollbar[data-axis=y]) .reader-scrollbar-thumb{width:${BAR}px;height:var(--thumb-len,${BAR}px)}
:where(.reader-scrollbar-thumb)::before{content:"";border-radius:999px;background:var(--scroll-thumb,rgb(0 0 0 / .25))}
:where(.reader-scrollbar[data-axis=x]) .reader-scrollbar-thumb::before{width:100%;height:6px}
:where(.reader-scrollbar[data-axis=y]) .reader-scrollbar-thumb::before{width:6px;height:100%}
:where(.reader-scrollbar:hover,.reader-scrollbar[data-dragging]) .reader-scrollbar-thumb::before{background:var(--scroll-thumb-hover,rgb(0 0 0 / .45))}
:where(.reader-scrollbar[data-axis=x]:is(:hover,[data-dragging])) .reader-scrollbar-thumb::before{height:9px}
:where(.reader-scrollbar[data-axis=y]:is(:hover,[data-dragging])) .reader-scrollbar-thumb::before{width:9px}
@keyframes reader-thumb-x{from{transform:translateX(0)}to{transform:translateX(var(--thumb-travel,0px))}}
@keyframes reader-thumb-y{from{transform:translateY(0)}to{transform:translateY(var(--thumb-travel,0px))}}
@supports (animation-timeline: --a){
  :where(.reader-scrollbar[data-axis=x][data-driven]) .reader-scrollbar-thumb{animation-name:reader-thumb-x;animation-timeline:--reader-sx}
  :where(.reader-scrollbar[data-axis=y][data-driven]) .reader-scrollbar-thumb{animation-name:reader-thumb-y;animation-timeline:--reader-sy}
}
@media (prefers-reduced-motion: reduce){:where(.reader-scrollbar){transition:opacity .15s}:where(.reader-scrollbar[data-hidden]){transform:none}}
`;

interface PageState {
  n: number;
  el: HTMLDivElement;
  img: HTMLImageElement | null;
  x: number;
  y: number;
  full: HTMLCanvasElement | null;
  fullKey: string;
  // The detail canvas: a region of the page, in fractions of the page, painted at full resolution.
  detail: HTMLCanvasElement | null;
  detailKey: string;
  detailRegion: { u0: number; v0: number; u1: number; v1: number } | null;
  textDone: boolean;
  task: RenderTask | null;
}

// The layout the visitor chose, kept for the session so the next guide opens the same way. A reload starts over.
const readChoice = (): Layout | null => {
  try {
    const nav = performance.getEntriesByType("navigation")[0] as PerformanceNavigationTiming | undefined;
    if (nav?.type === "reload") sessionStorage.removeItem(LAYOUT_KEY);
    const v = sessionStorage.getItem(LAYOUT_KEY);
    return v === "horizontal" || v === "vertical" ? v : null;
  } catch {
    return null;
  }
};
const writeChoice = (v: Layout) => {
  try {
    sessionStorage.setItem(LAYOUT_KEY, v);
  } catch {}
};

export function mountReader(viewport: HTMLElement, opts: ReaderOptions): Reader {
  const { pageCount, pageAspect } = opts;
  const root = document.documentElement;
  const doc = viewport.ownerDocument;
  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)");

  if (!doc.getElementById("reader-engine-style")) {
    const style = doc.createElement("style");
    style.id = "reader-engine-style";
    style.textContent = STYLE;
    doc.head.prepend(style);
  }

  // ---- DOM ----------------------------------------------------------------------------------------------------
  const scroller = doc.createElement("div");
  scroller.className = "reader-scroller";
  scroller.tabIndex = 0;
  const track = doc.createElement("div");
  track.className = "reader-track";
  scroller.append(track);

  const pages: PageState[] = [];
  for (let n = 1; n <= pageCount; n++) {
    const el = doc.createElement("div");
    el.className = "reader-page";
    el.id = `reader-page-${n}`;
    el.dataset.page = String(n);
    el.setAttribute("role", "group");
    el.setAttribute("aria-label", `Page ${n} of ${pageCount}`);
    let img: HTMLImageElement | null = null;
    if (opts.placeholder) {
      img = doc.createElement("img");
      img.alt = "";
      img.decoding = "async";
      img.draggable = false;
      el.append(img);
    }
    track.append(el);
    pages.push({
      n, el, img, x: 0, y: 0,
      full: null, fullKey: "", detail: null, detailKey: "", detailRegion: null,
      textDone: false, task: null,
    });
  }

  // The back chevron before the first page of a row scrolls with the pages.
  const back = (viewport.querySelector(".reader-back") ?? doc.querySelector(".reader-back")) as HTMLElement | null;
  const backHome = back ? { parent: back.parentNode, next: back.nextSibling } : null;
  if (back) track.prepend(back);

  // The overlay scrollbar. Keys scroll the scroller itself, so the bar is hidden from assistive technology.
  const bar = doc.createElement("div");
  bar.className = "reader-scrollbar";
  bar.setAttribute("aria-hidden", "true");
  const thumb = doc.createElement("div");
  thumb.className = "reader-scrollbar-thumb";
  bar.dataset.hidden = "";
  bar.append(thumb);
  const driven = typeof CSS !== "undefined" && CSS.supports?.("animation-timeline: --a");
  if (driven) {
    bar.dataset.driven = "";
    viewport.style.setProperty("timeline-scope", "--reader-sx, --reader-sy");
  }

  // A probe that turns the pad and gap variables, whatever their units, into pixels.
  const probe = doc.createElement("div");
  probe.setAttribute("aria-hidden", "true");
  probe.style.cssText =
    "position:absolute;visibility:hidden;pointer-events:none;width:0;height:0;" +
    "padding:var(--reader-pad-block,var(--reader-pad,24px)) var(--reader-gap,40px) 0 var(--reader-pad,24px)";

  // Anything already in the viewport (the plain list of page images) stays until the engine is in place.
  const fallback = [...viewport.children] as HTMLElement[];
  viewport.append(scroller, bar, probe);
  for (const el of fallback) el.hidden = true;

  // ---- state --------------------------------------------------------------------------------------------------
  let choice: Layout | null = readChoice();
  let layout: Layout = "horizontal";
  let zoom = 1; // committed zoom: the one the pages are laid out at
  let vw = 0, vh = 0, pad = 24, padBlock = 24, gap = 40;
  let pageW = 0, pageH = 0;
  let trackW = 0, trackH = 0;
  let current = 1;
  let destroyed = false;
  let rotating = false;
  let pdf: PDFDocumentProxy | null = null;
  let pdfW = 0; // the page's width in PDF points
  // Scroll events that follow the engine's own instant scrolls (a zoom, a resize) don't count as scrolling.
  let quietUntil = 0;
  const listeners = new Map<Event, Set<() => void>>();
  const emit = (e: Event) => listeners.get(e)?.forEach((cb) => cb());

  // A pinch in progress: the track is scaled by `g.s` and moved by (g.tx, g.ty), in track pixels.
  let g: { s: number; tx: number; ty: number; focus: Point } | null = null;
  let settleTimer = 0;

  // ---- layout -------------------------------------------------------------------------------------------------
  const mainPos = (p: PageState) => (layout === "horizontal" ? p.x : p.y);
  const mainSize = () => (layout === "horizontal" ? pageW : pageH);
  const mainView = () => (layout === "horizontal" ? vw : vh);
  const scrollMain = () => (layout === "horizontal" ? scroller.scrollLeft : scroller.scrollTop);
  const maxScroll = () => Math.max(0, layout === "horizontal" ? trackW - vw : trackH - vh);
  const autoLayout = (): Layout => (vw > vh ? "horizontal" : "vertical");

  const computeLayout = (z: number) => {
    vw = scroller.clientWidth;
    vh = scroller.clientHeight;
    layout = choice ?? autoLayout();
    if (root.dataset.layout !== layout) root.dataset.layout = layout;
    const cs = getComputedStyle(probe);
    pad = parseFloat(cs.paddingLeft) || 0;
    gap = parseFloat(cs.paddingRight) || 0;
    padBlock = parseFloat(cs.paddingTop) || pad;
    if (layout === "horizontal") {
      pageH = Math.max(50, vh - 2 * pad) * z;
      pageW = pageH * pageAspect;
      const row = pageCount * pageW + (pageCount - 1) * gap;
      // Room before the first page for the back chevron.
      if (back) back.style.display = "";
      const backW = back ? back.offsetWidth : 0;
      const start = backW ? 2 * pad + backW : pad;
      const lead = Math.max(start, (vw - row) / 2);
      const top = Math.max(pad, (vh - pageH) / 2);
      pages.forEach((p, i) => ((p.x = lead + i * (pageW + gap)), (p.y = top)));
      trackW = Math.ceil(lead + row + Math.max(pad, (vw - row) / 2));
      trackH = Math.ceil(Math.max(vh, pageH + 2 * pad));
    } else {
      pageW = Math.min(Math.max(50, vw - 2 * pad), MAX_FIT_WIDTH) * z;
      pageH = pageW / pageAspect;
      const col = pageCount * pageH + (pageCount - 1) * gap;
      const lead = Math.max(padBlock, (vh - col) / 2);
      const left = Math.max(pad, (vw - pageW) / 2);
      pages.forEach((p, i) => ((p.x = left), (p.y = lead + i * (pageH + gap))));
      trackW = Math.ceil(Math.max(vw, pageW + 2 * pad));
      trackH = Math.ceil(col + 2 * lead);
    }
  };

  const applyLayout = () => {
    track.style.width = `${trackW}px`;
    track.style.height = `${trackH}px`;
    const w = `${pageW}px`, h = `${pageH}px`;
    for (const p of pages) {
      const s = p.el.style;
      s.width = w;
      s.height = h;
      s.transform = `translate(${p.x}px, ${p.y}px)`;
      if (pdfW) s.setProperty("--total-scale-factor", String(pageW / pdfW));
    }
    if (back) {
      if (layout === "horizontal") {
        back.style.display = "";
        const p = pages[0];
        const bx = p.x - pad - back.offsetWidth;
        const by = p.y + pageH / 2 - back.offsetHeight / 2;
        back.style.transform = `translate(${bx}px, ${by}px)`;
      } else back.style.display = "none";
    }
    layoutBar();
  };

  // A point in the viewport as a page and a position on it in fractions of the page (which can fall outside 0..1
  // in the gaps), so it can be found again after the pages move.
  const anchorAt = (pt: Point) => {
    const tx = scroller.scrollLeft + pt.x, ty = scroller.scrollTop + pt.y;
    let best = pages[0], dist = Infinity;
    for (const p of pages) {
      const dx = Math.max(p.x - tx, 0, tx - (p.x + pageW));
      const dy = Math.max(p.y - ty, 0, ty - (p.y + pageH));
      const d = dx + dy;
      if (d < dist) (best = p), (dist = d);
    }
    return { p: best, u: (tx - best.x) / pageW, v: (ty - best.y) / pageH };
  };
  const setScroll = (x: number, y: number) => {
    quietUntil = performance.now() + 100;
    scroller.scrollLeft = x;
    scroller.scrollTop = y;
  };
  const scrollToAnchor = (a: ReturnType<typeof anchorAt>, pt: Point) =>
    setScroll(a.p.x + a.u * pageW - pt.x, a.p.y + a.v * pageH - pt.y);

  // ---- the reading position -----------------------------------------------------------------------------------
  // The page under a point a little way into the view: the first page more than half in view when pages fit,
  // the page in the middle of the view when one doesn't. At the very end, the last page.
  const pageAtScroll = (s: number) => {
    const max = maxScroll();
    if (max > 1 && s >= max - 1) return pageCount;
    const size = mainSize();
    const r = s + Math.min(size / 2 + pad, mainView() / 2);
    for (const p of pages) if (r < mainPos(p) + size) return p.n;
    return pageCount;
  };
  const leadPad = () => (layout === "horizontal" ? pad : padBlock);
  const scrollForPage = (n: number) => {
    const p = pages[clamp(Math.round(n), 1, pageCount) - 1];
    return clamp(mainPos(p) - (n === 1 ? mainPos(p) : leadPad()), 0, maxScroll());
  };

  // Placeholder images load for the pages near the view only.
  const loadPlaceholders = () => {
    if (!opts.placeholder) return;
    const [first, last] = visibleRange();
    for (const p of pages)
      if (p.img && !p.img.getAttribute("src") && p.n >= first - 2 && p.n <= last + 2) p.img.src = opts.placeholder(p.n);
  };

  const updatePage = () => {
    loadPlaceholders();
    if (!driven) moveThumb();
    const n = pageAtScroll(scrollMain());
    if (n === current) return;
    current = n;
    hashWrite(n);
    emit("page");
  };

  // The pages in view, as a range.
  const visibleRange = () => {
    const s = scrollMain(), v = mainView(), size = mainSize();
    let first = pageCount, last = 1;
    for (const p of pages) {
      const a = mainPos(p);
      if (a + size > s && a < s + v) {
        first = Math.min(first, p.n);
        last = Math.max(last, p.n);
      }
    }
    if (first > last) first = last = current;
    return [first, last] as const;
  };

  // ---- hash ---------------------------------------------------------------------------------------------------
  let hashTimer = 0;
  const hashRead = () => {
    const m = /^#page-(\d+)$/.exec(location.hash);
    return m ? clamp(parseInt(m[1], 10), 1, pageCount) : 0;
  };
  const hashWrite = (n: number) => {
    clearTimeout(hashTimer);
    hashTimer = window.setTimeout(() => {
      if (hashRead() === n) return;
      try {
        history.replaceState(history.state, "", `#page-${n}`);
      } catch {}
    }, 200);
  };

  // ---- scrolling animation (keys, page buttons, mouse-wheel notches, the scrollbar's track) ---------------------
  // A critically damped spring pulls the scroll position toward a target. Each notch or key press moves the target
  // and the motion carries on from its current speed, so fast input becomes one continuous glide, never a jump.
  let anim: { x: number; y: number; px: number; py: number; vx: number; vy: number; last: number; raf: number; page: number } | null = null;
  const OMEGA = 22; // 1/s: settles in about 300 ms

  const animateTo = (x: number, y: number, page = 0) => {
    x = clamp(x, 0, Math.max(0, trackW - vw));
    y = clamp(y, 0, Math.max(0, trackH - vh));
    if (anim) {
      anim.x = x;
      anim.y = y;
      anim.page = page;
      return;
    }
    const a = (anim = {
      x, y, px: scroller.scrollLeft, py: scroller.scrollTop, vx: 0, vy: 0,
      last: performance.now(), page, raf: 0,
    });
    // The exact step of a critically damped spring over dt, for one axis.
    const spring = (p: number, v: number, target: number, dt: number) => {
      const e = p - target, k = Math.exp(-OMEGA * dt), w = v + OMEGA * e;
      return [target + (e + w * dt) * k, (v - OMEGA * w * dt) * k];
    };
    const tick = (now: number) => {
      if (anim !== a) return;
      const dt = Math.min(0.064, Math.max(0, now - a.last) / 1000);
      a.last = now;
      [a.px, a.vx] = spring(a.px, a.vx, a.x, dt);
      [a.py, a.vy] = spring(a.py, a.vy, a.y, dt);
      const done =
        Math.abs(a.x - a.px) < 0.5 && Math.abs(a.y - a.py) < 0.5 && Math.abs(a.vx) < 20 && Math.abs(a.vy) < 20;
      if (done) (a.px = a.x), (a.py = a.y);
      scroller.scrollLeft = a.px;
      scroller.scrollTop = a.py;
      if (done) anim = null;
      else a.raf = requestAnimationFrame(tick);
    };
    a.raf = requestAnimationFrame(tick);
  };
  const stopAnim = () => {
    if (anim) cancelAnimationFrame(anim.raf);
    anim = null;
  };

  const goTo = (n: number, o?: { smooth?: boolean }) => {
    n = clamp(Math.round(n) || 1, 1, pageCount);
    const s = scrollForPage(n);
    const x = layout === "horizontal" ? s : scroller.scrollLeft;
    const y = layout === "horizontal" ? scroller.scrollTop : s;
    if (o?.smooth && !reduceMotion.matches) animateTo(x, y, n);
    else {
      stopAnim();
      setScroll(x, y);
      updatePage();
    }
  };

  // The next page is the first whose place is past the scroll; the one before, the last whose place is short of
  // it. While an animation is under way its target counts, so quick presses go one page each.
  const step = (dir: 1 | -1) => {
    if (anim?.page) return goTo(anim.page + dir, { smooth: true });
    const s = scrollMain();
    const p =
      dir > 0
        ? pages.find((q) => scrollForPage(q.n) > s + 2)
        : [...pages].reverse().find((q) => scrollForPage(q.n) < s - 2);
    if (p) goTo(p.n, { smooth: true });
  };

  // ---- wheel --------------------------------------------------------------------------------------------------
  let pendingX = 0, flushRaf = 0;
  const flush = () => {
    flushRaf = 0;
    scroller.scrollLeft += pendingX;
    pendingX = 0;
  };
  // A trackpad (or another pixel-precise device) reports wheelDelta as exactly -3 × delta in Chromium and WebKit; a
  // mouse wheel reports whole ticks (±120 each), or lines (deltaMode 1) in Firefox. Without wheelDelta, small
  // pixel deltas are taken for a trackpad.
  const isTrackpad = (e: WheelEvent) => {
    if (e.deltaMode !== 0) return false;
    const wd = (e as any).wheelDeltaY as number | undefined;
    if (wd) return wd === -3 * e.deltaY;
    return Math.abs(e.deltaY) < 50 || !Number.isInteger(e.deltaY);
  };
  // One mouse-wheel tick moves at least a line, so a slow single notch always makes a visible glide.
  const LINE = 40;

  const onWheel = (e: WheelEvent) => {
    if (e.ctrlKey || e.metaKey) return pinchWheel(e);
    if (rotating) return e.preventDefault();
    if (layout !== "horizontal") return stopAnim(); // native
    // When the pages are taller than the view the vertical wheel pans them up and down, natively.
    if (trackH > vh + 1 && !e.shiftKey) return stopAnim();
    const unit = e.deltaMode === 1 ? LINE : e.deltaMode === 2 ? vw : 1;
    const dx = e.deltaX * unit, dy = e.deltaY * unit;
    // A sideways trackpad swipe or shift+wheel: native.
    if (Math.abs(dy) <= Math.abs(dx)) return stopAnim();
    e.preventDefault();
    if (!isTrackpad(e)) {
      const d = Math.sign(dy) * Math.max(Math.abs(dy), LINE);
      const from = anim && Math.sign(anim.x - scroller.scrollLeft) === Math.sign(d) ? anim.x : scroller.scrollLeft;
      animateTo(from + d, scroller.scrollTop);
      if (anim) anim.page = 0;
      return;
    }
    // Trackpad: one to one. A glide still running from a notch hands over to the fingers.
    stopAnim();
    pendingX += dy;
    if (!flushRaf) flushRaf = requestAnimationFrame(flush);
  };

  // ---- zoom ---------------------------------------------------------------------------------------------------
  const liveZoom = () => (g ? clamp(zoom * g.s, MIN_ZOOM, MAX_ZOOM) : zoom);
  const center = (): Point => ({ x: vw / 2, y: vh / 2 });

  // Lays the pages out at a new zoom, keeping the content at `focus` (a point in the viewport) where it is.
  const commitZoom = (z: number, focus: Point, anchor?: ReturnType<typeof anchorAt>) => {
    z = clamp(z, MIN_ZOOM, MAX_ZOOM);
    const a = anchor ?? anchorAt(focus);
    zoom = z;
    computeLayout(z);
    applyLayout();
    scrollToAnchor(a, focus);
    queueRender(true);
  };

  const beginGesture = (focus: Point) => {
    stopAnim();
    if (!g) {
      g = { s: 1, tx: 0, ty: 0, focus };
      track.style.willChange = "transform";
      root.dataset.zooming = "";
      cancelRenders();
    }
  };
  const applyGesture = () => {
    if (g) track.style.transform = `translate(${g.tx}px, ${g.ty}px) scale(${g.s})`;
  };
  // Scales the live transform by `f` about a point in the viewport.
  const gestureScale = (f: number, focus: Point) => {
    if (!g) return;
    const s = clamp(zoom * g.s * f, MIN_ZOOM, MAX_ZOOM) / zoom;
    f = s / g.s;
    const qx = scroller.scrollLeft + focus.x, qy = scroller.scrollTop + focus.y;
    g.tx = qx - f * (qx - g.tx);
    g.ty = qy - f * (qy - g.ty);
    g.s = s;
    g.focus = focus;
    applyGesture();
    emit("zoom");
  };
  const gesturePan = (dx: number, dy: number) => {
    if (!g) return;
    g.tx += dx;
    g.ty += dy;
    applyGesture();
  };
  const endGestureSoon = () => {
    clearTimeout(settleTimer);
    settleTimer = window.setTimeout(endGesture, SETTLE_MS);
  };
  const endGesture = () => {
    clearTimeout(settleTimer);
    if (!g) return;
    const { s, tx, ty, focus } = g;
    // The content at the focus now, in the untransformed track.
    const qx = scroller.scrollLeft + focus.x, qy = scroller.scrollTop + focus.y;
    const ux = (qx - tx) / s, uy = (qy - ty) / s;
    const a = anchorAt({ x: ux - scroller.scrollLeft, y: uy - scroller.scrollTop });
    g = null;
    track.style.transform = "";
    track.style.willChange = "";
    commitZoom(zoom * s, focus, a);
    delete root.dataset.zooming;
    emit("zoom");
  };

  // ctrl+wheel: a trackpad pinch in Chromium and Firefox, or ctrl and a mouse wheel.
  const pinchWheel = (e: WheelEvent) => {
    e.preventDefault();
    if (rotating) return;
    const unit = e.deltaMode === 1 ? 40 : e.deltaMode === 2 ? vh : 1;
    const d = clamp(e.deltaY * unit, -50, 50);
    const r = viewport.getBoundingClientRect();
    const focus = { x: e.clientX - r.left, y: e.clientY - r.top };
    beginGesture(focus);
    gestureScale(Math.exp(-d * 0.01), focus);
    endGestureSoon();
  };

  // Safari's trackpad pinch.
  let gestureLast = 1;
  const onGestureStart = (e: any) => {
    e.preventDefault();
    if (rotating) return;
    gestureLast = 1;
    const r = viewport.getBoundingClientRect();
    beginGesture({ x: e.clientX - r.left, y: e.clientY - r.top });
  };
  const onGestureChange = (e: any) => {
    e.preventDefault();
    if (!g) return;
    const r = viewport.getBoundingClientRect();
    gestureScale(e.scale / gestureLast, { x: e.clientX - r.left, y: e.clientY - r.top });
    gestureLast = e.scale;
    endGestureSoon();
  };
  const onGestureEnd = (e: any) => {
    e.preventDefault();
    if (g) endGestureSoon();
  };

  // Two-finger touch pinch. One finger scrolls natively.
  let touch: { d: number; mx: number; my: number } | null = null;
  const touchInfo = (e: TouchEvent) => {
    const [a, b] = [e.touches[0], e.touches[1]];
    const r = viewport.getBoundingClientRect();
    return {
      d: Math.hypot(a.clientX - b.clientX, a.clientY - b.clientY),
      mx: (a.clientX + b.clientX) / 2 - r.left,
      my: (a.clientY + b.clientY) / 2 - r.top,
    };
  };
  const onTouchStart = (e: TouchEvent) => {
    if (e.touches.length === 2 && !rotating) {
      touch = touchInfo(e);
      beginGesture({ x: touch.mx, y: touch.my });
      clearTimeout(settleTimer);
    }
  };
  const onTouchMove = (e: TouchEvent) => {
    if (!touch || e.touches.length !== 2) return;
    e.preventDefault();
    const t = touchInfo(e);
    gesturePan(t.mx - touch.mx, t.my - touch.my);
    gestureScale(t.d / touch.d, { x: t.mx, y: t.my });
    touch = t;
  };
  const onTouchEnd = (e: TouchEvent) => {
    if (touch && e.touches.length < 2) {
      touch = null;
      endGesture();
    }
  };

  // Buttons and keys: the same transform, eased over a few frames, then one re-layout.
  let zoomAnim = 0;
  let zoomTarget = 0; // while a button or key zoom eases
  const animateZoom = (target: number, focus = center()) => {
    if (rotating) return;
    target = clamp(target, MIN_ZOOM, MAX_ZOOM);
    if (reduceMotion.matches) {
      if (g) endGesture();
      commitZoom(target, focus);
      emit("zoom");
      return;
    }
    zoomTarget = target;
    beginGesture(focus);
    cancelAnimationFrame(zoomAnim);
    const from = liveZoom();
    const t0 = performance.now();
    const tick = (now: number) => {
      const t = Math.min(1, (now - t0) / 160);
      const e = 1 - (1 - t) ** 3;
      gestureScale((from * (target / from) ** e) / liveZoom(), focus);
      if (t < 1) zoomAnim = requestAnimationFrame(tick);
      else (zoomTarget = 0), endGesture();
    };
    zoomAnim = requestAnimationFrame(tick);
  };
  const stepZoom = (dir: 1 | -1) => {
    const z = zoomTarget || liveZoom();
    const next = dir > 0 ? STEPS.find((s) => s > z + 0.01) : [...STEPS].reverse().find((s) => s < z - 0.01);
    if (next) animateZoom(next);
  };

  // ---- turning between a row and a column ---------------------------------------------------------------------
  let turnAnims: Animation[] = [];
  const setLayout = (mode: Layout, o?: { animate?: boolean }) => {
    if (mode !== "horizontal" && mode !== "vertical") return;
    choice = mode;
    writeChoice(mode);
    if (mode === layout) return;
    if (g) endGesture();
    stopAnim();
    for (const a of turnAnims) a.cancel();
    const keep = current;
    const sx = scroller.scrollLeft, sy = scroller.scrollTop;
    const before = pages.map((p) => ({ x: p.x - sx, y: p.y - sy }));
    const oldW = pageW, oldH = pageH;
    const was = layout;

    computeLayout(zoom);
    applyLayout();
    goTo(keep);
    current = keep;
    emit("layout");
    emit("page");

    const animate = o?.animate !== false && typeof track.animate === "function";
    if (!animate) return queueRender(true);
    rotating = true;
    root.dataset.rotating = "";
    hideBar(true);
    cancelRenders();

    let anims: Animation[] = [];
    if (reduceMotion.matches) {
      anims = [track.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 160, easing: "ease-out" })];
    } else {
      const nx = scroller.scrollLeft, ny = scroller.scrollTop;
      // Centres in the viewport, before and after, and the pivot: the page being read.
      const c0 = (i: number) => ({ x: before[i].x + oldW / 2, y: before[i].y + oldH / 2 });
      const c1 = (i: number) => ({ x: pages[i].x - nx + pageW / 2, y: pages[i].y - ny + pageH / 2 });
      const k = keep - 1;
      const P0 = c0(k), P1 = c1(k);
      const turn = was === "horizontal" ? Math.PI / 2 : -Math.PI / 2;
      const inView = (c: Point, w: number, h: number) =>
        c.x + w / 2 > -w && c.x - w / 2 < vw + w && c.y + h / 2 > -h && c.y - h / 2 < vh + h;
      const order = pages
        .map((_, i) => i)
        .filter((i) => inView(c0(i), oldW, oldH) || inView(c1(i), pageW, pageH))
        .sort((a, b) => Math.abs(a - k) - Math.abs(b - k));
      const s0 = oldW / pageW;
      const STEPS_N = 12;
      order.forEach((i, rank) => {
        const o0 = { x: c0(i).x - P0.x, y: c0(i).y - P0.y };
        const o1 = { x: c1(i).x - P1.x, y: c1(i).y - P1.y };
        const r0 = Math.hypot(o0.x, o0.y), r1 = Math.hypot(o1.x, o1.y);
        const a0 = r0 ? Math.atan2(o0.y, o0.x) : r1 ? Math.atan2(o1.y, o1.x) - turn : 0;
        // The end angle, unwrapped to the turn's direction.
        let a1 = r1 ? Math.atan2(o1.y, o1.x) : a0 + turn;
        while (a1 - a0 > Math.PI) a1 -= 2 * Math.PI;
        while (a1 - a0 < -Math.PI) a1 += 2 * Math.PI;
        const tilt = (turn * 180) / Math.PI / 8;
        const frames: Keyframe[] = [];
        for (let j = 0; j <= STEPS_N; j++) {
          const t = j / STEPS_N;
          const a = lerp(a0, a1, t), r = lerp(r0, r1, t);
          // The centre in track pixels, for the page's own translate.
          const cx = lerp(P0.x, P1.x, t) + r * Math.cos(a) + nx;
          const cy = lerp(P0.y, P1.y, t) + r * Math.sin(a) + ny;
          const s = lerp(s0, 1, t);
          frames.push({
            offset: t,
            transform: `translate(${cx - pageW / 2}px, ${cy - pageH / 2}px) rotate(${tilt * Math.sin(Math.PI * t)}deg) scale(${s})`,
          });
        }
        pages[i].el.style.zIndex = String(pageCount - rank);
        anims.push(
          pages[i].el.animate(frames, {
            duration: TURN_MS,
            delay: rank * TURN_STAGGER_MS,
            easing: "cubic-bezier(.65,0,.35,1)",
            fill: "backwards",
          }),
        );
      });
      if (back && layout === "horizontal")
        anims.push(back.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 200, delay: TURN_MS, fill: "backwards" }));
    }
    turnAnims = anims;
    Promise.all(anims.map((a) => a.finished.catch(() => {}))).then(() => {
      if (turnAnims !== anims || destroyed) return;
      turnAnims = [];
      for (const p of pages) p.el.style.zIndex = "";
      rotating = false;
      delete root.dataset.rotating;
      queueRender(true);
      flashBar();
    });
  };

  // ---- the overlay scrollbar ----------------------------------------------------------------------------------
  let barLen = 0, thumbLen = 0, travel = 0;
  let barTimer = 0, barHover = false, dragging: { p: number; s: number } | null = null;
  const barAxis = () => (layout === "horizontal" ? "x" : "y");
  const layoutBar = () => {
    if (bar.dataset.axis !== barAxis()) bar.dataset.axis = barAxis();
    barLen = Math.max(0, mainView() - 16);
    const total = layout === "horizontal" ? trackW : trackH;
    thumbLen = total > mainView() ? Math.max(BAR, (barLen * mainView()) / total) : barLen;
    travel = Math.max(0, barLen - thumbLen);
    bar.style.setProperty("--thumb-len", `${thumbLen}px`);
    bar.style.setProperty("--thumb-travel", `${travel}px`);
    if (!driven) moveThumb();
  };
  const moveThumb = () => {
    const max = maxScroll();
    const t = max > 0 ? (scrollMain() / max) * travel : 0;
    thumb.style.transform = layout === "horizontal" ? `translateX(${t}px)` : `translateY(${t}px)`;
  };
  const hasOverflow = () => maxScroll() > 1;
  const showBar = () => {
    if (rotating || !hasOverflow()) return;
    if (bar.hasAttribute("data-hidden")) delete bar.dataset.hidden;
    clearTimeout(barTimer);
    if (!barHover && !dragging) barTimer = window.setTimeout(() => hideBar(), BAR_IDLE_MS);
  };
  const hideBar = (now = false) => {
    clearTimeout(barTimer);
    if (!now && (barHover || dragging)) return;
    if (!bar.hasAttribute("data-hidden")) bar.dataset.hidden = "";
  };
  const flashBar = () => showBar();
  const onBarEnter = () => ((barHover = true), showBar());
  const onBarLeave = () => ((barHover = false), showBar());
  const onBarDown = (e: PointerEvent) => {
    if (e.button !== 0) return;
    e.preventDefault();
    stopAnim();
    const along = layout === "horizontal" ? e.clientX : e.clientY;
    if (e.target === thumb) {
      dragging = { p: along, s: scrollMain() };
      bar.dataset.dragging = "";
      bar.setPointerCapture(e.pointerId);
      showBar();
    } else {
      // A click on the track moves one view toward it.
      const r = thumb.getBoundingClientRect();
      const start = layout === "horizontal" ? r.left : r.top;
      const dir = along < start ? -1 : 1;
      const d = dir * mainView() * 0.9;
      if (layout === "horizontal") animateTo(scroller.scrollLeft + d, scroller.scrollTop);
      else animateTo(scroller.scrollLeft, scroller.scrollTop + d);
    }
  };
  const onBarMove = (e: PointerEvent) => {
    if (!dragging) return;
    const along = layout === "horizontal" ? e.clientX : e.clientY;
    const s = dragging.s + ((along - dragging.p) * maxScroll()) / Math.max(1, travel);
    if (layout === "horizontal") scroller.scrollLeft = s;
    else scroller.scrollTop = s;
  };
  const onBarUp = (e: PointerEvent) => {
    if (!dragging) return;
    dragging = null;
    delete bar.dataset.dragging;
    if (bar.hasPointerCapture(e.pointerId)) bar.releasePointerCapture(e.pointerId);
    showBar();
  };
  // A pointer near the bar's edge brings it back.
  const onViewportMove = (e: PointerEvent) => {
    if (e.pointerType === "touch") return;
    const r = viewport.getBoundingClientRect();
    const near = layout === "horizontal" ? r.bottom - e.clientY < 40 : r.right - e.clientX < 40;
    if (near) showBar();
  };

  // ---- keys ---------------------------------------------------------------------------------------------------
  const onKey = (e: KeyboardEvent) => {
    if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey) return;
    const t = e.target as HTMLElement | null;
    if (t?.closest?.("input, textarea, select, [contenteditable=''], [contenteditable='true']")) return;
    const onControl = !!t?.closest?.("button, a, summary, [role='button']");
    switch (e.key) {
      case "ArrowRight": case "ArrowDown": case "PageDown":
        step(1); break;
      case "ArrowLeft": case "ArrowUp": case "PageUp":
        step(-1); break;
      case " ":
        if (onControl) return;
        step(e.shiftKey ? -1 : 1); break;
      case "Home":
        goTo(1, { smooth: true }); break;
      case "End":
        goTo(pageCount, { smooth: true }); break;
      case "+": case "=":
        stepZoom(1); break;
      case "-": case "_":
        stepZoom(-1); break;
      case "0":
        animateZoom(1); break;
      default:
        return;
    }
    e.preventDefault();
  };

  // ---- scroll events ------------------------------------------------------------------------------------------
  let scrollRaf = 0, idleTimer = 0;
  const onScroll = () => {
    if (!scrollRaf) scrollRaf = requestAnimationFrame(() => ((scrollRaf = 0), updatePage()));
    if (performance.now() < quietUntil) return;
    if (!root.hasAttribute("data-scrolling")) root.dataset.scrolling = "";
    showBar();
    clearTimeout(idleTimer);
    idleTimer = window.setTimeout(() => {
      delete root.dataset.scrolling;
      queueRender(false);
    }, SCROLL_IDLE_MS);
  };

  // ---- resize -------------------------------------------------------------------------------------------------
  let resizeRaf = 0;
  const relayout = () => {
    resizeRaf = 0;
    if (g) endGesture();
    const keep = current;
    const before = layout;
    const a = anchorAt(center());
    computeLayout(zoom);
    applyLayout();
    if (layout !== before || zoom <= 1) goTo(keep);
    else scrollToAnchor(a, center());
    if (layout !== before) emit("layout");
    queueRender(true);
  };
  const ro = new ResizeObserver(() => {
    if (!resizeRaf) resizeRaf = requestAnimationFrame(relayout);
  });

  // ---- rendering ----------------------------------------------------------------------------------------------
  let readyFired = false;
  const pdfPages = new Map<number, Promise<PDFPageProxy>>();
  const getPage = (n: number) => {
    let p = pdfPages.get(n);
    if (!p) pdfPages.set(n, (p = pdf!.getPage(n)));
    return p;
  };

  const freeCanvas = (c: HTMLCanvasElement | null) => {
    if (!c) return;
    c.remove();
    // Releases the backing store at once (Safari holds it otherwise).
    c.width = c.height = 0;
  };
  const dropCanvases = (p: PageState, detailOnly = false) => {
    freeCanvas(p.detail);
    p.detail = null;
    p.detailKey = "";
    p.detailRegion = null;
    if (detailOnly) return;
    freeCanvas(p.full);
    p.full = null;
    p.fullKey = "";
    if (p.img) p.img.hidden = false;
  };
  const canvasPixels = (p: PageState) =>
    (p.full ? p.full.width * p.full.height : 0) + (p.detail ? p.detail.width * p.detail.height : 0);
  const distance = (p: PageState, first: number, last: number) =>
    p.n < first ? first - p.n : p.n > last ? p.n - last : 0;

  let queue: (() => Promise<void>)[] = [];
  let running = false;
  let renderTimer = 0;
  const cancelRenders = () => {
    queue = [];
    for (const p of pages) p.task?.cancel();
  };
  const queueRender = (soon: boolean) => {
    clearTimeout(renderTimer);
    if (soon) renderTimer = window.setTimeout(planRenders, 0);
    else planRenders();
  };
  const busy = () => !!g || rotating || root.hasAttribute("data-scrolling");

  const planRenders = () => {
    if (!pdf || destroyed || busy()) return; // the end of the scroll, pinch or turn comes back here
    const [first, last] = visibleRange();
    const dpr = window.devicePixelRatio || 1;
    const wantFull = pageW * dpr * pageH * dpr;
    const fullScale = wantFull > MAX_FULL_PIXELS ? dpr * Math.sqrt(MAX_FULL_PIXELS / wantFull) : dpr;
    const needDetail = fullScale < dpr * 0.99;
    const fullKey = `${Math.round(pageW)}x${fullScale.toFixed(3)}`;
    const detailKey = `${Math.round(pageW)}x${dpr}`;

    for (const p of pages) {
      const d = distance(p, first, last);
      if (d > KEEP) dropCanvases(p);
      else if (!needDetail || d > 0) dropCanvases(p, true);
    }

    const near = pages.filter((p) => distance(p, first, last) <= 1);
    near.sort((a, b) => distance(a, first, last) - distance(b, first, last));
    queue = [];
    for (const p of near) {
      if (p.fullKey !== fullKey) queue.push(() => renderFull(p, fullScale, fullKey));
      if (!p.textDone) queue.push(() => renderText(p));
    }
    if (needDetail) {
      for (const p of near) {
        if (distance(p, first, last) > 0) continue;
        const region = detailRegion(p);
        if (!region) continue;
        const have = p.detailRegion;
        const covered =
          p.detailKey === detailKey && have &&
          have.u0 <= region.view.u0 && have.v0 <= region.view.v0 &&
          have.u1 >= region.view.u1 && have.v1 >= region.view.v1;
        if (!covered) queue.push(() => renderDetail(p, region.want, dpr, detailKey));
      }
    }

    // Drop the farthest canvases until the total fits.
    let total = pages.reduce((t, p) => t + canvasPixels(p), 0);
    const far = [...pages].sort((a, b) => distance(b, first, last) - distance(a, first, last));
    for (const p of far) {
      if (total <= MAX_TOTAL_PIXELS || distance(p, first, last) === 0) break;
      total -= canvasPixels(p);
      dropCanvases(p);
    }
    void pump();
  };

  // The part of page p in view, and a slightly larger region to paint, in fractions of the page.
  const detailRegion = (p: PageState) => {
    const sx = scroller.scrollLeft, sy = scroller.scrollTop;
    const x0 = Math.max(sx, p.x), x1 = Math.min(sx + vw, p.x + pageW);
    const y0 = Math.max(sy, p.y), y1 = Math.min(sy + vh, p.y + pageH);
    if (x1 <= x0 || y1 <= y0) return null;
    const mx = vw * 0.1, my = vh * 0.1;
    const f = (a: number, b: number, c: number, d: number) => ({
      u0: clamp((a - p.x) / pageW, 0, 1), v0: clamp((c - p.y) / pageH, 0, 1),
      u1: clamp((b - p.x) / pageW, 0, 1), v1: clamp((d - p.y) / pageH, 0, 1),
    });
    return { view: f(x0, x1, y0, y1), want: f(x0 - mx, x1 + mx, y0 - my, y1 + my) };
  };

  const pump = async () => {
    if (running) return;
    running = true;
    try {
      while (queue.length && !destroyed) {
        const job = queue.shift()!;
        try {
          await job();
        } catch (err: any) {
          if (err?.name !== "RenderingCancelledException") console.warn("reader: render failed", err);
        }
        // Yield so input and frames go first.
        await new Promise((r) => setTimeout(r, 0));
      }
    } finally {
      running = false;
    }
  };

  // PDF.js paints in slices of a few milliseconds; between slices it waits while the pages are moving.
  const politely = (cont: () => void) => {
    const go = () => (busy() ? setTimeout(go, 50) : cont());
    requestAnimationFrame(go);
  };

  const paint = async (
    p: PageState,
    make: (page: PDFPageProxy) => { canvas: HTMLCanvasElement; viewport: any; transform?: number[] },
  ) => {
    const page = await getPage(p.n);
    if (busy() || destroyed) return null;
    const job = make(page);
    p.task = page.render({ canvas: job.canvas, viewport: job.viewport, transform: job.transform });
    p.task.onContinue = politely;
    try {
      await p.task.promise;
    } catch (e) {
      freeCanvas(job.canvas);
      throw e;
    } finally {
      p.task = null;
    }
    if (destroyed) return freeCanvas(job.canvas), null;
    return job;
  };

  const renderFull = async (p: PageState, scale: number, key: string) => {
    const job = await paint(p, (page) => {
      const base = page.getViewport({ scale: 1 });
      const vp = page.getViewport({ scale: (pageW / base.width) * scale });
      const canvas = doc.createElement("canvas");
      canvas.width = Math.max(1, Math.round(vp.width));
      canvas.height = Math.max(1, Math.round(vp.height));
      canvas.className = "reader-full";
      canvas.setAttribute("aria-hidden", "true");
      return { canvas, viewport: vp };
    });
    if (!job) return;
    const { canvas } = job;
    if (p.full) p.full.replaceWith(canvas), freeCanvas(p.full);
    else if (p.img) p.img.after(canvas);
    else p.el.prepend(canvas);
    p.full = canvas;
    p.fullKey = key;
    if (p.img) p.img.hidden = true;
    if (!readyFired) {
      readyFired = true;
      performance.mark?.("reader:first-render");
      root.dataset.reader = "ready";
      emit("ready");
    }
  };

  const renderDetail = async (p: PageState, r: { u0: number; v0: number; u1: number; v1: number }, dpr: number, key: string) => {
    let box = { x0: 0, y0: 0, x1: 0, y1: 0, w: 1, h: 1 };
    const job = await paint(p, (page) => {
      const base = page.getViewport({ scale: 1 });
      const vp = page.getViewport({ scale: (pageW / base.width) * dpr });
      box = {
        x0: Math.floor(r.u0 * vp.width), y0: Math.floor(r.v0 * vp.height),
        x1: Math.ceil(r.u1 * vp.width), y1: Math.ceil(r.v1 * vp.height),
        w: vp.width, h: vp.height,
      };
      const canvas = doc.createElement("canvas");
      canvas.width = Math.max(1, box.x1 - box.x0);
      canvas.height = Math.max(1, box.y1 - box.y0);
      canvas.className = "reader-detail";
      canvas.setAttribute("aria-hidden", "true");
      return { canvas, viewport: vp, transform: [1, 0, 0, 1, -box.x0, -box.y0] };
    });
    if (!job) return;
    const { canvas } = job;
    const s = canvas.style;
    s.left = `${(box.x0 / box.w) * 100}%`;
    s.top = `${(box.y0 / box.h) * 100}%`;
    s.width = `${((box.x1 - box.x0) / box.w) * 100}%`;
    s.height = `${((box.y1 - box.y0) / box.h) * 100}%`;
    const before = p.full ?? p.img;
    if (p.detail) p.detail.replaceWith(canvas), freeCanvas(p.detail);
    else if (before) before.after(canvas);
    else p.el.prepend(canvas);
    p.detail = canvas;
    p.detailKey = key;
    p.detailRegion = { u0: box.x0 / box.w, v0: box.y0 / box.h, u1: box.x1 / box.w, v1: box.y1 / box.h };
  };

  let TextLayerClass: typeof import("pdfjs-dist").TextLayer | null = null;
  const renderText = async (p: PageState) => {
    if (p.textDone || !TextLayerClass) return;
    p.textDone = true;
    const page = await getPage(p.n);
    const vp = page.getViewport({ scale: 1 });
    const div = doc.createElement("div");
    div.className = "textLayer";
    const layer = new TextLayerClass({ textContentSource: page.streamTextContent(), container: div, viewport: vp });
    await layer.render();
    // TextLayer sizes its box from the page's points; the page box is the size that counts.
    div.style.width = div.style.height = "";
    p.el.append(div);
    await renderLinks(p, page);
  };

  // Links: web and mail links open as usual; links inside the PDF move the reader.
  const renderLinks = async (p: PageState, page: PDFPageProxy) => {
    const annots = await page.getAnnotations({ intent: "display" });
    const links = annots.filter((a: any) => a.subtype === "Link");
    if (!links.length) return;
    const box = doc.createElement("div");
    box.className = "reader-links";
    const [vx0, vy0, vx1, vy1] = page.view;
    const W = vx1 - vx0, H = vy1 - vy0;
    for (const a of links as any[]) {
      const [x1, y1, x2, y2] = a.rect;
      const el = doc.createElement("a");
      const s = el.style;
      s.left = `${((Math.min(x1, x2) - vx0) / W) * 100}%`;
      s.top = `${((vy1 - Math.max(y1, y2)) / H) * 100}%`;
      s.width = `${(Math.abs(x2 - x1) / W) * 100}%`;
      s.height = `${(Math.abs(y2 - y1) / H) * 100}%`;
      const url: string | undefined = a.url || a.unsafeUrl;
      if (url) {
        el.href = url;
        if (!/^mailto:/i.test(url)) (el.target = "_blank"), (el.rel = "noopener");
        el.title = url.replace(/^mailto:/i, "");
      } else if (a.dest) {
        const target = await destPage(a.dest);
        if (!target) continue;
        el.href = `#page-${target}`;
        el.title = `Page ${target}`;
        el.addEventListener("click", (e) => {
          e.preventDefault();
          goTo(target, { smooth: true });
        });
      } else continue;
      box.append(el);
    }
    if (box.childElementCount) p.el.append(box);
  };
  const destPage = async (dest: unknown) => {
    try {
      const explicit = typeof dest === "string" ? await pdf!.getDestination(dest) : (dest as any[]);
      const ref = explicit?.[0];
      if (ref == null) return 0;
      const idx = typeof ref === "number" ? ref : await pdf!.getPageIndex(ref);
      return idx + 1;
    } catch {
      return 0;
    }
  };

  const loadPdf = async () => {
    try {
      const [lib, worker] = await Promise.all([import("pdfjs-dist"), import("pdfjs-dist/build/pdf.worker.min.mjs?url")]);
      if (destroyed) return;
      lib.GlobalWorkerOptions.workerSrc = worker.default;
      TextLayerClass = lib.TextLayer;
      const loaded = await lib.getDocument({ url: opts.url, isEvalSupported: false, enableXfa: false }).promise;
      if (destroyed) return void loaded.destroy();
      pdf = loaded;
      const first = await getPage(1);
      pdfW = first.getViewport({ scale: 1 }).width;
      for (const p of pages) p.el.style.setProperty("--total-scale-factor", String(pageW / pdfW));
      planRenders();
    } catch (err) {
      // The placeholders stay, and the reader keeps working with them.
      console.warn("reader: the PDF could not be loaded", err);
      root.dataset.reader = "fallback";
    }
  };

  // ---- hash changes from outside (a link, the address bar) ----------------------------------------------------
  const onHash = () => {
    const n = hashRead();
    if (n && n !== current) goTo(n, { smooth: true });
  };

  // ---- mount --------------------------------------------------------------------------------------------------
  computeLayout(zoom);
  applyLayout();
  current = hashRead() || 1;
  goTo(current);

  scroller.addEventListener("scroll", onScroll, { passive: true });
  scroller.addEventListener("wheel", onWheel, { passive: false });
  scroller.addEventListener("touchstart", onTouchStart, { passive: true });
  scroller.addEventListener("touchmove", onTouchMove, { passive: false });
  scroller.addEventListener("touchend", onTouchEnd, { passive: true });
  scroller.addEventListener("touchcancel", onTouchEnd, { passive: true });
  scroller.addEventListener("pointerdown", stopAnim, { passive: true });
  viewport.addEventListener("pointermove", onViewportMove, { passive: true });
  viewport.addEventListener("gesturestart", onGestureStart);
  viewport.addEventListener("gesturechange", onGestureChange);
  viewport.addEventListener("gestureend", onGestureEnd);
  bar.addEventListener("pointerenter", onBarEnter);
  bar.addEventListener("pointerleave", onBarLeave);
  bar.addEventListener("pointerdown", onBarDown);
  bar.addEventListener("pointermove", onBarMove);
  bar.addEventListener("pointerup", onBarUp);
  bar.addEventListener("pointercancel", onBarUp);
  window.addEventListener("keydown", onKey);
  window.addEventListener("hashchange", onHash);
  ro.observe(viewport);
  // A change of screen (or of the browser's zoom) changes the pixel ratio: paint again.
  let dprQuery: MediaQueryList | null = null;
  const onDpr = () => {
    dprQuery?.removeEventListener("change", onDpr);
    dprQuery = matchMedia(`(resolution: ${window.devicePixelRatio}dppx)`);
    dprQuery.addEventListener("change", onDpr);
    queueRender(true);
  };
  onDpr();
  scroller.focus({ preventScroll: true });
  void loadPdf();

  return {
    get page() { return current; },
    get pageCount() { return pageCount; },
    get zoom() { return liveZoom(); },
    get layout() { return layout; },
    goTo,
    next: () => step(1),
    prev: () => step(-1),
    zoomIn: () => stepZoom(1),
    zoomOut: () => stepZoom(-1),
    fit: () => animateZoom(1),
    setZoom(z, focus) {
      if (rotating) return;
      if (g) endGesture();
      commitZoom(z, focus ?? center());
      emit("zoom");
    },
    setLayout,
    on(event, cb) {
      let set = listeners.get(event);
      if (!set) listeners.set(event, (set = new Set()));
      set.add(cb);
      return () => set!.delete(cb);
    },
    destroy() {
      destroyed = true;
      stopAnim();
      cancelRenders();
      for (const a of turnAnims) a.cancel();
      cancelAnimationFrame(zoomAnim);
      cancelAnimationFrame(flushRaf);
      cancelAnimationFrame(scrollRaf);
      cancelAnimationFrame(resizeRaf);
      for (const t of [settleTimer, idleTimer, renderTimer, hashTimer, barTimer]) clearTimeout(t);
      ro.disconnect();
      dprQuery?.removeEventListener("change", onDpr);
      window.removeEventListener("keydown", onKey);
      window.removeEventListener("hashchange", onHash);
      viewport.removeEventListener("pointermove", onViewportMove);
      viewport.removeEventListener("gesturestart", onGestureStart);
      viewport.removeEventListener("gesturechange", onGestureChange);
      viewport.removeEventListener("gestureend", onGestureEnd);
      for (const p of pages) dropCanvases(p);
      if (back && backHome?.parent) {
        back.style.transform = back.style.display = "";
        backHome.parent.insertBefore(back, backHome.next);
      }
      scroller.remove();
      bar.remove();
      probe.remove();
      viewport.style.removeProperty("timeline-scope");
      for (const el of fallback) el.hidden = false;
      void pdf?.destroy();
      listeners.clear();
      for (const k of ["layout", "zooming", "scrolling", "rotating", "reader"]) delete root.dataset[k];
    },
  };
}
