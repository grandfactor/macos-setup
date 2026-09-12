# PROGRESS.md — agent memory for macos-setup

Goal: the most comprehensive, well-researched guide to setting up macOS for CS students /
software engineers / daily driving. Deliverables:
1. `docs/` — static site, GitHub Pages hostable (plain HTML/CSS/JS, no build step).
2. `GUIDE.md` — full Markdown adaptation of the site (single file, plus per-chapter `guide/*.md`).

Structure plan (chapters, each = one HTML page + one MD file):
00 intro / how to use     08 Homebrew                 16 Security & privacy
01 hardware & buying      09 Terminal & shell         17 Backup & recovery
02 first boot & migration 10 Dotfiles & git           18 Performance & maintenance
03 system settings        11 Languages & runtimes     19 Daily driver apps
04 Finder / Dock / UI     12 Editors & IDEs           20 CS-student specific
05 keyboard & input       13 Containers & VMs         21 Automation & scripting
06 window management      14 Cloud/DevOps tooling     22 Troubleshooting
07 CLI foundations (Xcode) 15 Databases & local dev   23 Checklists / cheat sheets
Appendices: A bootstrap script, B Brewfile, C keyboard shortcuts, D glossary, E sources.

Branch policy (from CLAUDE.md): push straight to main.

## Log
- 2026-09-12: repo empty except CLAUDE.md. Created PROGRESS.md. Next: research/ notes, then scaffold docs/ site.
