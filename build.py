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
        codes.append(m.group(2))
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
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
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
