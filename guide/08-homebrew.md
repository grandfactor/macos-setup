<!--
number: 08
part: Part III — Developer environment
description: Homebrew 6 from scratch — installing correctly on Apple silicon, formulae vs casks, Brewfiles, tap trust, ask mode, services, maintenance, and the Intel deprecation.
-->
# Homebrew

Homebrew is the package manager for macOS. Nearly every command-line tool in this guide and most GUI apps install through it, and a `Brewfile` is how you make a new Mac look like your old one in twenty minutes. This chapter covers Homebrew **6.x** (6.0.0 shipped June 2026), which changed several defaults from what older tutorials show.

## Install

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

The installer asks for your password once (`sudo` to create `/opt/homebrew` and set ownership to your user), installs the Command Line Tools if missing, and finishes with two lines to add to your shell config. On Apple silicon the prefix is **`/opt/homebrew`**; the installer's suggested snippet is:

```sh
echo >> ~/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

`brew shellenv` sets `HOMEBREW_PREFIX`, `PATH`, `MANPATH`, `INFOPATH`. Put it in `~/.zprofile` (login shells) or `~/.zshrc` — Chapter 9 organises this properly. Then:

```sh
brew doctor      # "Your system is ready to brew." — fix anything it flags
brew --prefix    # /opt/homebrew
brew config      # look for "Rosetta 2: false" and "macOS: 27.x-arm64"
```

> [!WARNING]
> If `brew --prefix` prints `/usr/local`, you have an **Intel** Homebrew running under Rosetta (usually inherited via Migration Assistant or by running the installer from an x86 terminal). It will stop receiving binary packages this month and stop working in macOS 28. Record it (`brew bundle dump --file=~/old-brewfile`), uninstall it with the official script under `arch -x86_64`, delete `/usr/local/Homebrew` and `/usr/local/Cellar`, and reinstall natively.

Standard-account users (Chapter 3): run the installer while authenticating as the admin user, then `sudo chown -R $(whoami):admin /opt/homebrew` so your daily account owns it. Homebrew refuses to run as root; multi-user Homebrew is unsupported — one user owns it.

## Concepts

| Term | Meaning |
|---|---|
| **Formula** | A command-line package built from source or, almost always, installed from a prebuilt **bottle**. `brew install ripgrep`. Lives in `/opt/homebrew/Cellar/<name>/<version>` and is symlinked into `/opt/homebrew/bin`, `lib`, etc. |
| **Cask** | A GUI app or large binary (fonts, drivers) installed from the vendor's own download. `brew install --cask ghostty`. The `.app` goes to `/Applications`; metadata to `/opt/homebrew/Caskroom`. |
| **Tap** | A third-party repository of formulae/casks (`brew tap owner/repo`). `homebrew/core` and `homebrew/cask` are built in and served from a JSON API rather than a git clone. |
| **Keg-only** | A formula not symlinked into `bin` because it would shadow a system tool (e.g. `openssl@3`, `libpq`, `curl`). Use `$(brew --prefix libpq)/bin/psql` or add to `PATH` explicitly. |
| **Bottle** | Prebuilt binary for your macOS version/arch. If none exists, `brew` compiles — slow and a sign the formula is unusual or you're on an unsupported macOS. |
| **Brewfile** | A manifest of taps, formulae, casks, Mac App Store apps and extension packages, consumed by `brew bundle`. |
| **Service** | A formula with a launchd definition (Postgres, Redis, nginx): `brew services start postgresql@17`. |

## Everyday commands

```sh
brew search <text>            # formulae and casks; use "brew search --desc" to search descriptions
brew info <pkg>               # what it is, deps, caveats (read caveats!), install status; "brew info --cask"
brew install <pkg>            # formula
brew install --cask <app>     # GUI app
brew exec <formula> -- <cmd>  # run a tool from a formula's environment without installing globally (6.0, like npx)
brew list                     # installed formulae (+ --cask for apps); "brew leaves" = explicitly installed, not deps
brew deps --tree <pkg>        # why is this here?
brew uses --installed <pkg>   # what depends on it
brew update                   # refresh the package index (fast; internal JSON API)
brew outdated                 # what would upgrade
brew upgrade                  # upgrade everything (formulae + casks); "brew upgrade <pkg>" for one
brew pin <pkg> / brew unpin   # freeze a version (formulae and, since 6.0, casks)
brew uninstall <pkg>          # remove; "--zap" for casks deletes prefs/caches too
brew autoremove               # remove orphaned dependencies
brew cleanup [--prune=all]    # delete old versions and downloads (auto-runs periodically; run manually to reclaim GB)
brew doctor                   # health check
brew tap-info --installed     # your taps and their trust status
brew vulns                    # (tap) check installed packages against known CVEs
```

Homebrew 6 turned on **"ask" mode by default for developers** (and it's a one-line opt-in for everyone): `brew install`/`upgrade` print a plan — packages, dependencies, download size — and wait for `y`. Set `HOMEBREW_ASK=1` in your shell config to have it everywhere, or `--yes`/`-y` to skip a prompt in scripts. `brew upgrade` now prints a summary at the end, and cask upgrades can reopen apps that were running.

Casks with `auto_updates true` (apps that update themselves, like Chrome, VS Code, Slack) are skipped by `brew upgrade` unless you pass `--greedy`, so `brew upgrade --greedy` occasionally forces them to the version Homebrew knows.

## Tap trust (new in 6.0)

Third-party taps contain arbitrary Ruby that runs on your machine. Homebrew 6 requires you to **trust a tap explicitly** before its formulae or casks are evaluated:

```sh
brew tap --trust owner/repo          # add and trust in one step
brew tap owner/repo                  # add untrusted → install of its packages is refused until trusted
brew trust owner/repo                # trust later
brew untrust owner/repo
brew tap-info owner/repo             # shows "trusted: true/false"
```

Official taps are trusted by default. Homebrew also stopped auto-tapping (`brew install owner/repo/tool` no longer silently adds the tap). In a Brewfile, write `tap "owner/repo", trusted: true`. Before trusting a tap, look at its GitHub repo — how many stars, who maintains it, does it just wrap binaries from a vendor's releases page. Popular taps you'll likely trust: `hashicorp/tap`, `oven-sh/bun`, `xcodesorg/made`, `FelixKratz/formulae` (sketchybar/borders), `koekeishiya/formulae` (yabai/skhd), `nikitabobko/tap` (AeroSpace), `charmbracelet/tap`, `stripe/stripe-cli`, `supabase/tap`.

## The Brewfile: your machine as code

Create one from your current state:

```sh
brew bundle dump --describe --file=~/.config/homebrew/Brewfile   # --force to overwrite
```

Edit it by hand from then on. A realistic developer Brewfile (yours will differ — this is the shape):

```ruby
# ~/.config/homebrew/Brewfile
tap "oven-sh/bun", trusted: true
tap "nikitabobko/tap", trusted: true

# --- shell & core CLI ---
brew "git"                 # newer than Apple's
brew "gh"                  # GitHub CLI
brew "zsh"                 # optional: newer than /bin/zsh
brew "starship"            # prompt
brew "zoxide"              # smarter cd
brew "fzf"                 # fuzzy finder
brew "ripgrep"             # rg
brew "fd"                  # find
brew "bat"                 # cat with wings
brew "eza"                 # ls
brew "jq", "yq"            # JSON / YAML
brew "tmux"
brew "neovim"
brew "mise"                # runtime versions (node, python, go, java…)
brew "uv"                  # python packaging
brew "direnv"
brew "tldr"                # or tlrc
brew "htop", "btop"
brew "wget", "curl"        # curl is keg-only; Apple's is fine for most uses
brew "coreutils", "gnu-sed", "gawk"   # GNU tools (g-prefixed)
brew "tree", "ncdu", "dust", "duf"
brew "watch", "entr"
brew "hyperfine"           # benchmarking
brew "difftastic", "git-delta"
brew "shellcheck", "shfmt"
brew "pre-commit"
brew "gnupg", "pinentry-mac"
brew "mas"                 # Mac App Store CLI
brew "trash"               # move to Trash from the shell instead of rm
brew "colima", "docker", "docker-compose", "docker-buildx"   # or the OrbStack cask instead of these four
brew "postgresql@17", restart_service: :changed
brew "redis", restart_service: :changed
brew "sqlite"
brew "awscli"
brew "terraform"           # or tofu
brew "kubectl", "k9s", "helm"
brew "oven-sh/bun/bun"

# --- GUI apps ---
cask "ghostty"
cask "visual-studio-code"
cask "zed"
cask "raycast"
cask "rectangle"           # or: cask "nikitabobko/tap/aerospace"
cask "karabiner-elements"
cask "maccy"
cask "1password", "1password-cli"
cask "orbstack"
cask "tableplus"
cask "postman"             # or "bruno"
cask "obsidian"
cask "notion"
cask "slack", "discord", "zoom"
cask "google-chrome", "firefox", "zen"
cask "iina"                # video player
cask "the-unarchiver"
cask "appcleaner"
cask "stats"               # menu bar system monitor
cask "ice"                 # menu bar organiser
cask "font-jetbrains-mono-nerd-font"
cask "font-fira-code-nerd-font"
cask "qlmarkdown", "syntax-highlight", "quicklook-json", "qlstephen"

# --- Mac App Store (needs mas + signed in) ---
mas "Xcode", id: 497799835
mas "Amphetamine", id: 937984704
mas "Kagi for Safari", id: 1622835804

# --- VS Code extensions ---
vscode "ms-python.python"
vscode "esbenp.prettier-vscode"
vscode "eamodio.gitlens"
```

Apply it on a new machine (or after editing):

```sh
brew bundle install --file=~/.config/homebrew/Brewfile   # installs anything missing; parallel since 6.0
brew bundle check                                        # what's missing
brew bundle cleanup                                      # uninstall things NOT in the Brewfile (asks first)
brew bundle add ripgrep --describe                       # append to the Brewfile
brew bundle remove ripgrep
```

Set `HOMEBREW_BUNDLE_FILE=~/.config/homebrew/Brewfile` in your shell config so you can drop `--file`. Homebrew 6 also lets a Brewfile carry `npm`, `cargo`, `go`, `uv` (Python tools), `krew` and even `winget` (on Windows) entries, so global CLI tools from language ecosystems live in the same manifest:

```ruby
uv "ruff"
uv "pre-commit"
npm "typescript"
cargo "cargo-watch"
```

Commit the Brewfile to your dotfiles repo (Chapter 10). Appendix B is a complete annotated Brewfile you can start from.

## Services

Formulae with background daemons integrate with launchd:

```sh
brew services list
brew services start postgresql@17      # start now + at login
brew services run redis                # start now only
brew services stop postgresql@17
brew services restart --all
brew services info postgresql@17       # status, log paths, user
```

Logs go to `/opt/homebrew/var/log/`; data to `/opt/homebrew/var/<service>/`. For databases that should only run when you're actually developing, prefer starting them per project (Chapter 15) or in containers — a Postgres that autostarts at login is a battery cost you'll forget about.

## Fonts, drivers, and other casks

- **Fonts** are casks: `brew install --cask font-jetbrains-mono-nerd-font` (the *Nerd Font* variants include the icons that Starship, eza and Neovim status lines expect). Since Homebrew 4.x the fonts live in the main cask repo — no `homebrew/cask-fonts` tap needed.
- **Drivers/kernel extensions** (Logitech, Wacom, Elgato, VirtualBox) are casks too; on Apple silicon many need approval in `Privacy & Security` after install, and a kext requires *Reduced Security* in Recovery — avoid apps that still ship kexts in 2026.
- **Quarantine**: casks are downloaded with Gatekeeper's quarantine bit set, so the first launch shows the "downloaded from the internet" check. `brew install --cask --no-quarantine <app>` skips that for apps you trust (or `export HOMEBREW_CASK_OPTS="--no-quarantine"` for all). Casks whose signatures fail Gatekeeper are disabled in Homebrew as of September 2026, so anything installable is at least signed.
- `brew install --cask --appdir=~/Applications <app>` installs for your user only.
- **`brew uninstall --zap --cask <app>`** removes preferences, caches, and launch agents listed in the cask definition — the closest thing to a clean uninstall. AppCleaner does the same for non-Homebrew apps.

## Environment variables worth setting

```sh
# ~/.zshenv or ~/.zshrc
export HOMEBREW_NO_ENV_HINTS=1          # quieter
export HOMEBREW_BUNDLE_FILE="$HOME/.config/homebrew/Brewfile"
export HOMEBREW_CASK_OPTS="--no-quarantine"   # optional; see above
export HOMEBREW_NO_ANALYTICS=1          # opt out of anonymous analytics (or `brew analytics off`)
export HOMEBREW_ASK=1                   # always show the plan and confirm
# export HOMEBREW_AUTO_UPDATE_SECS=86400  # update the index at most daily instead of every 5 min
# export HOMEBREW_NO_AUTO_UPDATE=1        # never auto-update on install (then run `brew update` yourself)
```

Defaults that changed in 5.x/6.x and no longer need setting: concurrent downloads (on), the internal JSON API (on), `brew bundle` parallel installs (on), SBOM generation (now **opt-in** via `HOMEBREW_SBOM=1`).

## Maintenance routine

Weekly (or bind it to a Raycast/Shortcuts command):

```sh
brew update && brew upgrade && brew autoremove && brew cleanup --prune=all && brew doctor
```

Occasionally:

- `brew leaves` — anything you don't recognise, `brew uninstall` it.
- `brew bundle cleanup` — prunes to the Brewfile.
- `du -sh $(brew --cache)` — the download cache; `brew cleanup --prune=all` clears it.
- After a **major macOS upgrade**: `brew update`, `brew upgrade`, then `brew doctor`. If many bottles are missing for a brand-new macOS version (the first week or two of Golden Gate), Homebrew builds from source; be patient or wait a week. Reinstall the CLT if `brew doctor` says they're outdated.
- **Every September**: read the Homebrew blog post for the new major version. 6.0's changes (tap trust, ask mode) broke a few people's scripts.

## Homebrew and the Intel deprecation

Per Homebrew's support tiers: with macOS 27 dropping Intel Macs, **macOS x86_64 moved to Tier 3 in September 2026** — no CI, no new bottles, install-from-source only, `brew doctor` warns — and **in September 2027 all Intel macOS code is deleted**. If you still have an Intel Mac on Tahoe, expect increasingly frequent from-source builds; if you have an Intel Homebrew on an Apple silicon Mac, remove it now (above).

## Alternatives and complements

- **MacPorts** — older, uses `/opt/local`, builds more from source, runs as root. Excellent for scientific/legacy Unix software; fine to run *alongside* Homebrew if you keep PATHs straight. Most people don't need it.
- **Nix / nix-darwin / Home Manager** — declarative, reproducible, cross-platform. Powerful and a real rabbit hole; if you already use Nix on Linux, `nix-darwin` can manage Homebrew casks *and* system settings. Homebrew 6 warns when it detects a Nix-managed installation but works.
- **`mise`** (Chapter 11) for language runtimes and dev tools with per-project versions; **`uv tool`**, **`pipx`**, **`npm -g`**, **`cargo install`** for language-specific CLIs — increasingly all recorded in the Brewfile via the 6.0 extensions.
- **Mac App Store + `mas`** for sandboxed apps that update themselves and are tied to your Apple Account.
- **Setapp** ($10/month subscription to ~250 Mac apps) — worth it if you'd otherwise buy 3+ of its apps (CleanShot X, Bartender, TablePlus, Paste, iStat Menus…). Free 7-day trial; students get 50% off.
- **Workbrew** — Homebrew for managed fleets (the Homebrew lead's company). Relevant if your employer manages Macs.
- **BrewUI** — Homebrew's own upcoming official GUI; not ready for general use yet. **Cakebrew** is dead; **Applite** is a decent third-party cask GUI for beginners.
