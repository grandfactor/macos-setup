# The macOS Setup Guide

**The comprehensive, opinionated guide to setting up a Mac for CS students, software engineers, and daily driving — macOS 26 Tahoe / 27 Golden Gate, Apple silicon, September 2026.**

- **Website:** https://grandfactor.github.io/macos-setup/
- **Single-file Markdown:** [`GUIDE.md`](GUIDE.md) (~70,000 words — the whole site in one document, readable on GitHub)
- **Scripts:** [`scripts/`](scripts/) — `bootstrap.sh`, `macos-defaults.sh`, `cleanup.sh`, `audit.sh`, `Brewfile`

## What's in it

23 chapters and 5 appendices, organised in six parts:

| Part | Chapters |
|---|---|
| **I — Before you start** | 1 Hardware & buying · 2 First boot & migration |
| **II — System & interface** | 3 System Settings · 4 Finder, Dock, Spotlight · 5 Keyboard & input · 6 Window management |
| **III — Developer environment** | 7 Command Line Tools & Xcode · 8 Homebrew · 9 Terminal & shell · 10 Dotfiles & Git · 11 Languages & runtimes · 12 Editors & IDEs · 13 Containers & VMs · 14 Cloud & DevOps tooling · 15 Databases & local dev |
| **IV — Security, backup & maintenance** | 16 Security & privacy · 17 Backup & recovery · 18 Performance & maintenance |
| **V — Daily driving & workflows** | 19 Daily-driver apps · 20 CS-student specific · 21 Automation & scripting · 22 Troubleshooting |
| **VI — Reference** | 23 Checklists & cheat sheets · A Bootstrap script · B Brewfile · C Keyboard shortcuts · D Glossary · E Sources |

Every recommendation names the alternative and says why. Prices, versions, and dates are as of September 2026 and will drift; [Appendix E](guide/appendix-e-sources.md) lists where to re-check.

## Quick start on a new Mac

```sh
# Read it first: scripts/bootstrap.sh
/bin/zsh -c "$(curl -fsSL https://raw.githubusercontent.com/grandfactor/macos-setup/main/scripts/bootstrap.sh)"
```

Installs Command Line Tools, Homebrew, the Brewfile, `mise` + `uv`, Git/SSH with signing, a shell starter, Touch ID for `sudo`, and applies the macOS defaults. Flags: `--minimal`, `--no-defaults`, `--no-apps`, `--dotfiles <url>`. Details in [Appendix A](guide/appendix-a-bootstrap-script.md).

## Repository layout

```
guide/          chapter sources — NN-slug.md and appendix-X-slug.md, HTML-comment front matter
guide/_intro.md landing page content
scripts/        bootstrap.sh · macos-defaults.sh · cleanup.sh · audit.sh · Brewfile
build.py        stdlib-only static site generator (Markdown → docs/*.html, docs/search.json, GUIDE.md)
docs/           generated site (GitHub Pages serves this directory)
docs/assets/    style.css · app.js · favicon.svg (hand-written, not generated)
research/       dated research notes behind the chapters
GUIDE.md        generated single-file edition
```

## Building locally

Requires Python 3.11+ and nothing else.

```sh
python3 build.py                      # → docs/ and GUIDE.md
cd docs && python3 -m http.server 8000   # preview at http://localhost:8000
```

`build.py` renders GitHub-flavoured Markdown (tables, task lists, fenced code with copy buttons, `> [!NOTE]`-style admonitions), supports `{{include:path|lang}}` to embed a file from the repo as a code block, builds per-section search data, and writes the single-file `GUIDE.md` with a table of contents and demoted headings. Chapters are ordered by filename; appendices sort after numbered chapters.

## Hosting on GitHub Pages

The site is plain static HTML — no Jekyll, no Actions required.

1. **Settings → Pages → Build and deployment → Source: Deploy from a branch**
2. **Branch: `main`, folder: `/docs`** → Save
3. Site appears at `https://<user>.github.io/<repo>/` within a minute. `docs/.nojekyll` is written by the build so underscored assets are served as-is.

To publish with a custom domain, add `docs/CNAME` and set the domain in the Pages settings. If you'd rather build on push, a workflow is provided at `scripts/ci-example/pages.yml` — copy it to `.github/workflows/pages.yml` (it runs `build.py` and deploys `docs/` with the official Pages actions); switch the Pages source to **GitHub Actions** to use it.

## Contributing

Edit the chapter in `guide/`, run `python3 build.py`, commit both the source and the regenerated `docs/` + `GUIDE.md`. Corrections that cite a primary source are merged fastest. Every page has an **Edit on GitHub** link in the footer.

## License

Text and scripts © 2026 the contributors. Prose is licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); code in `scripts/` and `build.py` is [MIT](https://opensource.org/license/mit). Product names are trademarks of their owners; nothing here is affiliated with or endorsed by Apple.
