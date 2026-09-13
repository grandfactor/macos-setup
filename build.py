#!/usr/bin/env python3
"""
build.py — turns guide/*.md into:
  * docs/            static HTML site (GitHub Pages: Settings → Pages → main /docs)
  * GUIDE.md         single-file Markdown adaptation of the whole site
  * docs/search.json client-side search index

Zero dependencies (stdlib only) so it survives sandbox resets.
Markdown subset supported: ATX headings, paragraphs, fenced code, GFM tables,
nested ordered/unordered/task lists, blockquotes + GitHub admonitions
(> [!NOTE] etc.), horizontal rules, inline code/bold/italic/strike/links/images,
raw inline HTML (e.g. <kbd>), and an {{include:path}} directive.
"""
from __future__ import annotations

import html
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GUIDE = ROOT / "guide"
DOCS = ROOT / "docs"
SITE_TITLE = "The macOS Setup Guide"
SITE_TAGLINE = "For CS students, software engineers and everyone who lives on a Mac — 2026 edition"
REPO_URL = "https://github.com/grandfactor/macos-setup"
LAST_UPDATED = "September 2026"

# --------------------------------------------------------------------------- #
# Inline markdown
# --------------------------------------------------------------------------- #

TAG_RE = re.compile(r"</?[a-zA-Z][a-zA-Z0-9-]*(\s[^<>]*)?/?>")


def escape_text(s: str) -> str:
    """Escape &, <, > but let real-looking HTML tags through."""
    out = []
    pos = 0
    for m in TAG_RE.finditer(s):
        out.append(html.escape(s[pos:m.start()], quote=False))
        out.append(m.group(0))
        pos = m.end()
    out.append(html.escape(s[pos:], quote=False))
    return "".join(out)


def inline(md: str) -> str:
    codes: list[str] = []

    def stash(m):
        c = m.group(2)
        if len(m.group(1)) > 1 and c.startswith(" ") and c.endswith(" ") and c.strip():
            c = c[1:-1]  # CommonMark: strip one space of padding in ``  `` spans
        codes.append(c)
        return f"\x00{len(codes) - 1}\x00"

    md = re.sub(r"(`+)(.+?)\1", stash, md)
    md = escape_text(md)
    md = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)",
                lambda m: f'<img src="{m.group(2)}" alt="{m.group(1)}"'
                          + (f' title="{m.group(3)}"' if m.group(3) else "") + ' loading="lazy">', md)

    def link(m):
        text, href = m.group(1), m.group(2)
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        return f'<a href="{href}"{ext}>{text}</a>'

    md = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, md)
    md = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", md)
    md = re.sub(r"__(.+?)__", r"<strong>\1</strong>", md)
    md = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", md)
    md = re.sub(r"(?<![\w_/])_(?!\s)([^_]+?)(?<!\s)_(?![\w_/])", r"<em>\1</em>", md)
    md = re.sub(r"~~(.+?)~~", r"<del>\1</del>", md)
    md = re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{html.escape(codes[int(m.group(1))], quote=False)}</code>", md)
    return md


def strip_tags(s: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def slugify(text: str) -> str:
    text = strip_tags(text)
    text = text.replace("`", "").lower().strip()
    # GitHub-compatible: drop punctuation, then map EACH whitespace char to a hyphen (no collapsing),
    # so anchors in GUIDE.md resolve identically on github.com and on the site.
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s", "-", text)
    return text.strip("-") or "section"


# --------------------------------------------------------------------------- #
# Block markdown
# --------------------------------------------------------------------------- #

@dataclass
class Heading:
    level: int
    text: str
    id: str


ADMONITIONS = {
    "NOTE": ("note", "Note"),
    "TIP": ("tip", "Tip"),
    "IMPORTANT": ("important", "Important"),
    "WARNING": ("warning", "Warning"),
    "CAUTION": ("caution", "Caution"),
}

LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")


class Renderer:
    def __init__(self):
        self.headings: list[Heading] = []
        self.used_ids: dict[str, int] = {}
        self.plain: list[str] = []

    def uid(self, text: str) -> str:
        s = slugify(text)
        n = self.used_ids.get(s, 0)
        self.used_ids[s] = n + 1
        return s if n == 0 else f"{s}-{n}"

    def render(self, md: str) -> str:
        md = expand_includes(md)
        return self.blocks(md.replace("\r\n", "\n").split("\n"))

    # -- block parser ---------------------------------------------------------
    def blocks(self, lines: list[str]) -> str:
        out: list[str] = []
        i, n = 0, len(lines)
        while i < n:
            line = lines[i]
            stripped = line.strip()
            if not stripped:
                i += 1
                continue

            m = re.match(r"^(\s*)(```+|~~~+)\s*([\w+\-.#]*)\s*$", line)
            if m:
                fence, lang = m.group(2), m.group(3)
                buf = []
                i += 1
                while i < n and not re.match(rf"^\s*{re.escape(fence)}\s*$", lines[i]):
                    buf.append(lines[i])
                    i += 1
                i += 1
                code = html.escape("\n".join(buf), quote=False)
                cls = f' class="language-{lang}"' if lang else ""
                label = f'<span class="code-lang">{html.escape(lang)}</span>' if lang else ""
                out.append(f'<div class="codeblock">{label}<button class="copy" type="button" aria-label="Copy code">Copy</button>'
                           f'<pre><code{cls}>{code}</code></pre></div>')
                self.plain.append("\n".join(buf))
                continue

            m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
            if m:
                level = len(m.group(1))
                text = inline(m.group(2))
                hid = self.uid(m.group(2))
                self.headings.append(Heading(level, text, hid))
                anchor = f'<a class="anchor" href="#{hid}" aria-label="Permalink">#</a>' if level > 1 else ""
                out.append(f'<h{level} id="{hid}">{text}{anchor}</h{level}>')
                self.plain.append(strip_tags(text))
                i += 1
                continue

            if re.match(r"^\s*([-*_])(\s*\1){2,}\s*$", line):
                out.append("<hr>")
                i += 1
                continue

            if i + 1 < n and "|" in line and re.match(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$", lines[i + 1]):
                header = split_row(line)
                aligns = [align(c) for c in split_row(lines[i + 1])]
                i += 2
                rows = []
                while i < n and lines[i].strip() and "|" in lines[i]:
                    rows.append(split_row(lines[i]))
                    i += 1
                out.append(self.table(header, aligns, rows))
                continue

            if stripped.startswith(">"):
                buf = []
                while i < n and lines[i].strip().startswith(">"):
                    buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                    i += 1
                kind = None
                if buf:
                    km = re.match(r"^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$", buf[0].strip())
                    if km:
                        kind = km.group(1)
                        buf = buf[1:]
                inner = self.blocks(buf)
                if kind:
                    cls, label = ADMONITIONS[kind]
                    out.append(f'<div class="admonition {cls}"><p class="admonition-title">{label}</p>{inner}</div>')
                else:
                    out.append(f"<blockquote>{inner}</blockquote>")
                continue

            if LIST_RE.match(line):
                block, i = self.collect_list(lines, i)
                out.append(block)
                continue

            if re.match(r"^<(div|details|summary|table|section|figure|iframe|ul|ol|video|img|hr|br|p)\b", stripped):
                buf = [line]
                i += 1
                while i < n and lines[i].strip():
                    buf.append(lines[i])
                    i += 1
                out.append("\n".join(buf))
                continue

            buf = [stripped]
            i += 1
            while i < n and lines[i].strip() and not self.starts_block(lines[i]):
                buf.append(lines[i].strip())
                i += 1
            text = inline(" ".join(buf))
            out.append(f"<p>{text}</p>")
            self.plain.append(strip_tags(text))
        return "\n".join(out)

    @staticmethod
    def starts_block(line: str) -> bool:
        s = line.strip()
        return bool(
            re.match(r"^#{1,6}\s", s)
            or re.match(r"^(```|~~~)", s)
            or s.startswith(">")
            or LIST_RE.match(line)
            or re.match(r"^\s*([-*_])(\s*\1){2,}\s*$", line)
            or s.startswith("|")
            or re.match(r"^<(div|details|table|section|figure)\b", s)
        )

    # -- lists ----------------------------------------------------------------
    def collect_list(self, lines: list[str], i: int) -> tuple[str, int]:
        n = len(lines)
        first = LIST_RE.match(lines[i])
        base = len(first.group(1))
        items: list[list[str]] = []
        markers: list[str] = []
        while i < n:
            line = lines[i]
            if not line.strip():
                j = i + 1
                while j < n and not lines[j].strip():
                    j += 1
                if j < n:
                    ind = len(lines[j]) - len(lines[j].lstrip())
                    is_item = LIST_RE.match(lines[j]) is not None
                    if ind > base or (is_item and ind == base):
                        if items:
                            items[-1].append("")
                        i = j
                        continue
                break
            ind = len(line) - len(line.lstrip())
            m = LIST_RE.match(line)
            if m and ind == base:
                items.append([m.group(3)])
                markers.append(m.group(2))
                i += 1
                continue
            if ind > base and items:
                items[-1].append(line[min(ind, base + 2):])
                i += 1
                continue
            break

        ordered = bool(re.match(r"\d", markers[0]))
        tag = "ol" if ordered else "ul"
        start = ""
        if ordered:
            f = int(re.match(r"\d+", markers[0]).group(0))
            if f != 1:
                start = f' start="{f}"'
        lis = []
        has_task = False
        for content in items:
            head, rest = content[0], content[1:]
            cls = ""
            task = re.match(r"^\[( |x|X)\]\s+(.*)$", head)
            if task:
                has_task = True
                checked = " checked" if task.group(1).lower() == "x" else ""
                body = f'<input type="checkbox" disabled{checked}> {inline(task.group(2))}'
                cls = ' class="task"'
            else:
                body = inline(head)
            # lazy paragraph continuation directly after the item head
            while rest and rest[0].strip() and not self.starts_block(rest[0]):
                body += " " + inline(rest.pop(0).strip())
            nested = self.blocks(rest) if any(r.strip() for r in rest) else ""
            self.plain.append(strip_tags(body))
            lis.append(f"<li{cls}>{body}{nested}</li>")
        lcls = ' class="task-list"' if has_task else ""
        return f"<{tag}{start}{lcls}>\n" + "\n".join(lis) + f"\n</{tag}>", i

    def table(self, header, aligns, rows) -> str:
        def cells(tag, cs):
            parts = []
            for idx, c in enumerate(cs):
                a = aligns[idx] if idx < len(aligns) else ""
                style = f' style="text-align:{a}"' if a else ""
                t = inline(c)
                self.plain.append(strip_tags(t))
                parts.append(f"<{tag}{style}>{t}</{tag}>")
            return "".join(parts)
        thead = f"<thead><tr>{cells('th', header)}</tr></thead>"
        tbody = "<tbody>" + "".join(f"<tr>{cells('td', r)}</tr>" for r in rows) + "</tbody>"
        return f'<div class="table-wrap"><table>{thead}{tbody}</table></div>'


def split_row(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s)]


def align(cell: str) -> str:
    c = cell.strip()
    if c.startswith(":") and c.endswith(":"):
        return "center"
    if c.endswith(":"):
        return "right"
    return ""


def expand_includes(md: str) -> str:
    def repl(m):
        rel = m.group(1).strip()
        lang = m.group(2) or Path(rel).suffix.lstrip(".") or "text"
        body = (ROOT / rel).read_text(encoding="utf-8").rstrip("\n")
        return f"```{lang}\n{body}\n```"
    return re.sub(r"^\{\{include:([^}|]+)(?:\|([a-z0-9]+))?\}\}\s*$", repl, md, flags=re.M)


# --------------------------------------------------------------------------- #
# Chapters
# --------------------------------------------------------------------------- #

@dataclass
class Chapter:
    src: Path
    slug: str
    number: str
    title: str
    description: str
    part: str
    md: str

    @property
    def href(self) -> str:
        return f"{self.slug}.html"

    @property
    def label(self) -> str:
        """'12. Editors & IDEs' for chapters; appendix titles already carry their letter."""
        if self.title.lower().startswith("appendix"):
            return self.title
        return f"{self.number}. {self.title}"


FRONT_RE = re.compile(r"^<!--\s*(.*?)\s*-->\s*", re.S)


def parse_front(md: str) -> tuple[dict, str]:
    """Front matter = leading HTML comment of key: value lines (invisible on GitHub)."""
    meta = {}
    m = FRONT_RE.match(md)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        md = md[m.end():]
    return meta, md


def load_chapters() -> list[Chapter]:
    chapters = []
    for p in sorted(GUIDE.glob("*.md")):
        if p.name.startswith("_"):
            continue
        meta, body = parse_front(p.read_text(encoding="utf-8"))
        tm = re.search(r"^#\s+(.+)$", body, re.M)
        title = meta.get("title") or (tm.group(1).strip() if tm else p.stem)
        chapters.append(Chapter(
            src=p, slug=p.stem, number=meta.get("number", p.stem.split("-")[0]),
            title=title, description=meta.get("description", ""), part=meta.get("part", ""), md=body,
        ))
    return chapters


# --------------------------------------------------------------------------- #
# HTML shell
# --------------------------------------------------------------------------- #

def nav_html(chapters: list[Chapter], current: Chapter | None) -> str:
    parts: list[str] = []
    last_part = None
    for ch in chapters:
        if ch.part != last_part:
            if last_part is not None:
                parts.append("</ul>")
            parts.append(f'<p class="nav-part">{html.escape(ch.part)}</p><ul>')
            last_part = ch.part
        cls = ' class="active"' if current and ch.slug == current.slug else ""
        num = f'<span class="nav-num">{html.escape(ch.number)}</span>' if ch.number else ""
        parts.append(f'<li{cls}><a href="{ch.href}">{num}{html.escape(ch.title)}</a></li>')
    if last_part is not None:
        parts.append("</ul>")
    return "\n".join(parts)


def toc_html(headings: list[Heading]) -> str:
    items = [h for h in headings if 2 <= h.level <= 3]
    if not items:
        return ""
    out = ['<nav class="toc" aria-label="On this page"><p class="toc-title">On this page</p><ul>']
    for h in items:
        out.append(f'<li class="lvl{h.level}"><a href="#{h.id}">{h.text}</a></li>')
    out.append("</ul></nav>")
    return "\n".join(out)


GH_ICON = ('<svg width="20" height="20" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 '
           '3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-'
           '.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-'
           '1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 '
           '1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38'
           'A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>')


def page(chapters: list[Chapter], ch: Chapter | None, body: str, *, title: str, description: str,
         headings: list[Heading] | None = None, prev: Chapter | None = None, nxt: Chapter | None = None,
         is_index: bool = False) -> str:
    full_title = SITE_TITLE if is_index else f"{title} — {SITE_TITLE}"
    toc = toc_html(headings or [])
    pager = ""
    if prev or nxt:
        p = (f'<a class="pager-link prev" href="{prev.href}"><span>Previous</span><strong>{html.escape(prev.title)}</strong></a>'
             if prev else "<span></span>")
        q = (f'<a class="pager-link next" href="{nxt.href}"><span>Next</span><strong>{html.escape(nxt.title)}</strong></a>'
             if nxt else "<span></span>")
        pager = f'<nav class="pager" aria-label="Chapter navigation">{p}{q}</nav>'
    if ch:
        links = (f'<a href="{REPO_URL}/blob/main/guide/{ch.src.name}" target="_blank" rel="noopener">View this chapter as Markdown</a>'
                 f' · <a href="{REPO_URL}/edit/main/guide/{ch.src.name}" target="_blank" rel="noopener">Edit on GitHub</a>')
    else:
        links = f'<a href="{REPO_URL}/blob/main/GUIDE.md" target="_blank" rel="noopener">Read the whole guide as one Markdown file</a>'
    desc = html.escape(description or SITE_TAGLINE, quote=True)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{html.escape(full_title, quote=True)}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/style.css">
<script>(function(){{try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();</script>
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<header class="topbar">
  <button class="menu-btn" id="menuBtn" aria-label="Toggle navigation" aria-expanded="false" aria-controls="sidebar"><span></span><span></span><span></span></button>
  <a class="brand" href="index.html"><img src="assets/favicon.svg" alt="" width="26" height="26"><span>{html.escape(SITE_TITLE)}</span></a>
  <div class="topbar-right">
    <button class="search-btn" id="searchBtn" aria-label="Search the guide (press slash)"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><span>Search</span><kbd>/</kbd></button>
    <button class="theme-btn" id="themeBtn" aria-label="Toggle dark mode" title="Toggle light / dark / auto">◐</button>
    <a class="gh" href="{REPO_URL}" target="_blank" rel="noopener" aria-label="GitHub repository">{GH_ICON}</a>
  </div>
</header>
<div class="layout">
  <aside class="sidebar" id="sidebar">
    <nav aria-label="Chapters">
      <a class="nav-home{' active' if is_index else ''}" href="index.html">Start here: overview &amp; how to use this guide</a>
      {nav_html(chapters, ch)}
    </nav>
  </aside>
  <main id="content" class="content">
    <article class="prose">
{body}
    </article>
    {pager}
    <footer class="page-footer">
      <p>{links}</p>
      <p>Last reviewed {LAST_UPDATED}. Written for macOS 26 Tahoe and macOS 27 Golden Gate on Apple silicon Macs. Prices are US list prices. Text is CC BY 4.0; code and configs are MIT.</p>
    </footer>
  </main>
  <aside class="rightbar">{toc}</aside>
</div>
<div class="search-modal" id="searchModal" hidden>
  <div class="search-panel" role="dialog" aria-modal="true" aria-label="Search the guide">
    <input type="search" id="searchInput" placeholder="Search the guide…" autocomplete="off" spellcheck="false" aria-label="Search">
    <ul id="searchResults" class="search-results" role="listbox"></ul>
    <p class="search-hint"><kbd>↑</kbd><kbd>↓</kbd> navigate · <kbd>Enter</kbd> open · <kbd>Esc</kbd> close</p>
  </div>
</div>
<script src="assets/app.js" defer></script>
</body>
</html>
"""


def index_body(chapters: list[Chapter], intro_html: str) -> str:
    cards = []
    last_part = None
    for ch in chapters:
        if ch.part != last_part:
            if last_part is not None:
                cards.append("</div>")
            cards.append(f'<h2 class="part-title" id="{slugify(ch.part)}">{html.escape(ch.part)}</h2><div class="cards">')
            last_part = ch.part
        cards.append(
            f'<a class="card" href="{ch.href}"><span class="card-num">{html.escape(ch.number)}</span>'
            f'<span class="card-title">{html.escape(ch.title)}</span>'
            f'<span class="card-desc">{html.escape(ch.description)}</span></a>'
        )
    if last_part is not None:
        cards.append("</div>")
    return intro_html + '\n<h2 id="chapters">All chapters</h2>\n' + "\n".join(cards)


# --------------------------------------------------------------------------- #
# GUIDE.md (single-file Markdown adaptation)
# --------------------------------------------------------------------------- #

def demote_headings(md: str, by: int = 1) -> str:
    """Shift headings so chapter H1s become H2 in the combined file; skip fenced code."""
    out, in_fence = [], False
    for line in md.split("\n"):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
        if not in_fence:
            m = re.match(r"^(#{1,6})(\s+.*)$", line)
            if m:
                line = "#" * min(6, len(m.group(1)) + by) + m.group(2)
        out.append(line)
    return "\n".join(out)


def build_guide_md(chapters: list[Chapter], intro_md: str) -> str:
    out = [f"# {SITE_TITLE}", "", f"_{SITE_TAGLINE}_", "",
           "> This is the single-document Markdown adaptation of the website. The same content is split "
           "chapter-by-chapter in [`guide/`](guide/), and rendered as a site in [`docs/`](docs/). "
           f"Last reviewed {LAST_UPDATED}.", "", "## Table of contents", ""]
    last_part = None
    for ch in chapters:
        if ch.part != last_part:
            out += [f"**{ch.part}**", ""]
            last_part = ch.part
        out.append(f"- [{ch.label}](#{slugify(ch.label)}) — {ch.description}")
    # cross-chapter links: "12-editors-and-ides.html#foo" -> "#foo" / "#12-editors--ides" so GUIDE.md is self-contained
    by_slug = {ch.slug: ch for ch in chapters}
    def relink(md: str) -> str:
        def repl(m):
            slug, frag = m.group(1), m.group(2)
            if slug == "index":
                return "](#table-of-contents)"
            ch = by_slug.get(slug)
            if not ch:
                return m.group(0)
            return f"](#{frag})" if frag else f"](#{slugify(ch.label)})"
        return re.sub(r"\]\(([0-9a-z][0-9a-z-]*)\.html(?:#([^)\s]+))?\)", repl, md)
    out += ["", "---", "", demote_headings(relink(intro_md.strip())), ""]
    for ch in chapters:
        body = relink(expand_includes(ch.md.strip()))
        # rename the chapter H1 to include its number, then demote everything one level
        body = re.sub(r"^#\s+.+$", f"# {ch.label}", body, count=1, flags=re.M)
        out += ["---", "", demote_headings(body), "", "[↑ Back to top](#table-of-contents)", ""]
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def main() -> int:
    chapters = load_chapters()
    if not chapters:
        print("no chapters in guide/", file=sys.stderr)
        return 1
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("")
    intro_path = GUIDE / "_intro.md"
    intro_md = intro_path.read_text(encoding="utf-8") if intro_path.exists() else f"# {SITE_TITLE}\n\n{SITE_TAGLINE}\n"
    search_index = []

    for idx, ch in enumerate(chapters):
        r = Renderer()
        body_html = r.render(ch.md)
        prev = chapters[idx - 1] if idx > 0 else None
        nxt = chapters[idx + 1] if idx + 1 < len(chapters) else None
        (DOCS / ch.href).write_text(
            page(chapters, ch, body_html, title=ch.title, description=ch.description,
                 headings=r.headings, prev=prev, nxt=nxt), encoding="utf-8")
        for sec in re.split(r'(?=<h[23] id=")', body_html):
            m = re.match(r'<h([23]) id="([^"]+)">(.*?)<a class="anchor"', sec)
            text = re.sub(r"\s+", " ", strip_tags(re.sub(r"<[^>]+>", " ", sec[m.end():] if m else sec))).strip()
            if not text and not m:
                continue
            search_index.append({
                "c": ch.title, "n": ch.number,
                "t": strip_tags(m.group(3)) if m else "",
                "u": f"{ch.href}#{m.group(2)}" if m else ch.href,
                "b": text[:700],
            })

    r = Renderer()
    intro_html = r.render(intro_md)
    (DOCS / "index.html").write_text(
        page(chapters, None, index_body(chapters, intro_html), title=SITE_TITLE, description=SITE_TAGLINE,
             headings=r.headings, is_index=True), encoding="utf-8")
    (DOCS / "search.json").write_text(json.dumps(search_index, ensure_ascii=False), encoding="utf-8")
    (ROOT / "GUIDE.md").write_text(build_guide_md(chapters, intro_md), encoding="utf-8")

    words = sum(len(c.md.split()) for c in chapters) + len(intro_md.split())
    print(f"built {len(chapters)} chapters, {words:,} words, {len(search_index)} search sections -> docs/ and GUIDE.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
