<!--
number: B
part: Part VI — Reference
description: The complete Brewfile behind this guide — 100+ CLI tools, runtimes, container/cloud tooling, fonts, and every GUI app recommended in chapters 9–19, with the optional ones commented out. Plus how Brewfile syntax works, how to keep yours in sync, and how to split it per machine.
-->
# Appendix B — Brewfile

`brew bundle` reads a Ruby-flavoured manifest and installs everything in it — formulae, casks, Mac App Store apps (via `mas`), and VS Code extensions. It is the single most useful file in a dotfiles repo: the whole software side of a Mac in 300 lines, reproducible with one command. [Chapter 8](08-homebrew.html) explains Homebrew itself; this appendix is the manifest.

```sh
brew bundle --file=scripts/Brewfile          # install what's listed (skips what's already there)
brew bundle check --file=scripts/Brewfile    # what's missing?
brew bundle cleanup --file=scripts/Brewfile  # what's installed but NOT listed? (add --force to uninstall)
brew bundle dump --force --describe          # regenerate from what's installed → ./Brewfile
```

## Conventions in this file

- Lines starting with `#cask`, `#brew`, `#mas`, `#vscode` (no space) are **opt-in alternatives** — remove the `#` to enable. Lines starting with `# ` are commentary.
- The **uncommented** set is the guide's default recommendation: a full developer CLI, `mise` + `uv`, container/cloud tooling, Nerd Fonts, Ghostty, VS Code, OrbStack, Firefox, and the Tier-1 daily-driver apps from [chapter 19](19-daily-driver-apps.html). On a fast connection it's ~15–25 minutes and ~8 GB (Xcode excluded).
- `restart_service: false` on `postgresql@18` and `redis` means they're installed but **not** started at login — `brew services run postgresql@18` when you need them ([chapter 15](15-databases-and-local-dev.html)).
- `mas` entries need you to be signed in to the App Store; the bootstrap script drops them otherwise. Find IDs with `mas search "name"`.
- `vscode` entries run `code --install-extension`; they're skipped if VS Code isn't installed.
- Third-party taps (`supabase/tap`, `nikitabobko/tap`) will prompt for trust on first use under Homebrew 6 — that's the new tap-trust feature working as intended.

## `scripts/Brewfile`

{{include:scripts/Brewfile|ruby}}

## Per-machine Brewfiles

One file rarely fits a laptop, a desktop, and a work machine. Two patterns:

**Includes** — a base file plus a per-host file, concatenated at install time:

```sh
# ~/.dotfiles/install.sh
cat Brewfile.base "Brewfile.$(scutil --get ComputerName | tr ' ' '-')" 2>/dev/null > /tmp/Brewfile
brew bundle --file=/tmp/Brewfile
```

**Ruby conditionals** — the Brewfile is Ruby, so this works:

```ruby
host = `scutil --get ComputerName`.strip
cask "docker-desktop"  if host == "work-mbp"       # company mandates Docker Desktop
cask "orbstack"        unless host == "work-mbp"
cask "steam"           if host == "studio"
brew "postgresql@18", restart_service: (host == "studio")
```

## Keeping it honest

Every month (the routine in [chapter 18](18-performance-and-maintenance.html)):

```sh
brew bundle cleanup --file=~/.dotfiles/Brewfile    # lists things you installed ad hoc
# → either add them to the Brewfile (you use them) or `brew uninstall --zap` them (you don't)
brew bundle dump --force --describe --file=/tmp/Brewfile.now && diff ~/.dotfiles/Brewfile /tmp/Brewfile.now
```

`brew bundle dump` sorts alphabetically and loses your comments, so don't overwrite a hand-curated file with it — diff and copy the new lines across. `--describe` adds each formula's description as a comment, which makes a dumped file readable enough to start from.

## Formula and cask name changes

Homebrew renames casks when upstream renames apps (`docker` → `docker-desktop`, `tailscale` → `tailscale-app`, `handbrake` → `handbrake-app`, `wireshark` → `wireshark-app` all happened in 2025–26). `brew bundle` prints a deprecation warning with the new name; update the file. `brew search --cask name` finds the current one.
