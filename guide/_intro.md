# The macOS Setup Guide

<div class="hero">
<p class="lede">A complete, opinionated, deeply researched guide to setting up a Mac for computer science students, software engineers, and anyone who uses a Mac as their daily machine. From which Mac to buy, through the first boot, to a fully tuned development environment, security posture, backup strategy and automation layer — with the reasoning behind every recommendation.</p>
<div class="badges">
<span class="badge">macOS 26 Tahoe &amp; 27 Golden Gate</span>
<span class="badge">Apple silicon (M1 → M6)</span>
<span class="badge">Homebrew 6</span>
<span class="badge">Reviewed September 2026</span>
<span class="badge">23 chapters + 5 appendices · ~70,000 words · fully scriptable</span>
</div>
</div>

## Who this is for

- **CS students** starting a degree (or a bootcamp) who just got a Mac and want to set it up *once, properly*, without cargo-culting a random dotfiles repo.
- **Software engineers** joining a new job or replacing a laptop who want a reproducible, secure, fast environment on day one.
- **Daily drivers** — people who live on their Mac for writing, research, media, school and life — who want the machine to get out of their way.

You don't need to read it front to back. Each chapter stands alone, and the [checklists](23-checklists-and-cheat-sheets.html) at the end compress the whole thing into a few printable pages.

## How to use this guide

1. **In a hurry?** Read [Chapter 2 (first boot)](02-first-boot-and-migration.html), run the [bootstrap script](appendix-a-bootstrap-script.html), then skim the [checklists](23-checklists-and-cheat-sheets.html).
2. **Buying a Mac?** Start with [Chapter 1](01-hardware-and-buying.html); it is written for September 2026 pricing and the M5/M6 lineup.
3. **Already set up but it feels messy?** Jump to [Homebrew](08-homebrew.html), [Terminal &amp; shell](09-terminal-and-shell.html), [Dotfiles](10-dotfiles-and-git.html) and [Security](16-security-and-privacy.html).
4. **Setting up for a specific stack?** [Languages &amp; runtimes](11-languages-and-runtimes.html), [Containers &amp; VMs](13-containers-and-vms.html) and [Databases &amp; local dev](15-databases-and-local-dev.html) are self-contained.

Conventions used throughout:

| Convention | Meaning |
|---|---|
| <kbd>⌘</kbd> <kbd>⌥</kbd> <kbd>⌃</kbd> <kbd>⇧</kbd> <kbd>fn</kbd>/<kbd>🌐</kbd> | Command, Option, Control, Shift, Function/Globe |
| `System Settings → General → Software Update` | Navigate the Settings app in that order |
| `$ command` | Run in a terminal; the `$` is a prompt, don't type it (the copy button strips it) |
| **Recommended** / *Alternative* / ~~Avoid~~ | Our default pick / a fine substitute / something we actively steer you away from |
| Note / Tip / Warning callouts | Read these; they save hours |

Every recommendation comes with a *why*. If you disagree with the *why*, you'll know exactly what to swap.

## What's new in 2026 (and why this guide exists)

The Mac platform changed more in 2025–2026 than in the previous five years combined, and most setup guides on the internet haven't caught up:

- **macOS 27 "Golden Gate" ships September 14, 2026** and is **Apple-silicon only**. Intel Macs stay on macOS 26 Tahoe (security updates until ~2029). Rosetta 2 is removed for general apps in macOS 28 (fall 2027) — so this guide is uncompromisingly *arm64-native first*.
- **The lineup is completely new**: MacBook Neo ($599, A18 Pro, 8 GB), MacBook Air M5, MacBook Pro M5 / M5 Pro / M5 Max, Mac mini M6 and M5 Pro, Mac Studio M5 Max / M5 Ultra, two new Studio Displays. Chapter 1 tells you which one to actually buy.
- **Apple shipped its own container runtime** (`container`, on the Containerization framework) and Docker Desktop is no longer the automatic answer.
- **Homebrew 6** introduced tap trust, an "ask before install" default, parallel `brew bundle`, `brew exec`, and is dropping Intel bottles this month.
- **Spotlight became a real launcher** (apps, files, actions, clipboard history, Quick Keys) and in Golden Gate hosts Siri AI. The Raycast/Alfred question has a different answer now.
- **Security defaults moved**: FileVault is on by default at setup, its recovery key lives in iCloud Keychain and the Passwords app, Stolen Device Protection came to MacBooks, Gatekeeper lost its right-click bypass, and encrypted HFS+ backup drives are deprecated.
- **Tooling consolidated**: `mise` and `uv` replaced a zoo of version managers; Ghostty matured into the default terminal recommendation; Zed, Cursor and VS Code split the editor market three ways; AI coding agents live in the terminal and in Xcode 27.

Everything below reflects that world. Where a fact is likely to age (a version number, a price), it is dated so you can judge it.

## A note on opinions

This guide is opinionated on purpose. Beginners are paralysed by "it depends"; experts already know when to deviate. So each section gives a **default**, one or two **alternatives**, and the **reason**. When a tool is *free for students* or *free for personal use*, we say so, because that matters when you're on a budget.

Nothing here is sponsored. Prices are US list prices at the time of review; education pricing is noted where Apple or a vendor offers it.

## Contributing and corrections

The source is plain Markdown in the [`guide/`](https://github.com/grandfactor/macos-setup/tree/main/guide) directory of the repository; the site and the single-file `GUIDE.md` are generated from it by a dependency-free Python script (`python3 build.py`). Found a mistake, a stale price or a better tool? Open an issue or a pull request.
