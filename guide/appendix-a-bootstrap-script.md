<!--
number: A
part: Part VI — Reference
description: The complete, idempotent bootstrap script that turns a fresh Apple-silicon Mac into the setup this guide describes — Command Line Tools, Homebrew, Brewfile, mise/uv, Git and SSH, shell, Touch ID sudo, dotfiles — plus the macOS defaults script, the monthly cleanup script, and the security audit script. Read before running.
-->
# Appendix A — Bootstrap script

Everything in [Part II](03-system-settings.html) and [Part III](07-command-line-tools-and-xcode.html) that can be automated, in four scripts that live in the repo's `scripts/` directory. They're written for **zsh on macOS 26/27, Apple silicon**, and every step is idempotent — run them again after a partial failure or on a Mac you set up by hand and they'll only do what's missing.

> [!WARNING]
> **Read scripts before you run them.** Piping `curl` into a shell from a stranger's repo is exactly the habit [chapter 16](16-security-and-privacy.html) warns about. Clone the repo, open the files, delete the lines you disagree with (there will be some — these are opinions), then run. The scripts never touch `/System`, never disable Gatekeeper/SIP/FileVault, and ask before installing Rosetta or logging in to GitHub.

## Quick start

```sh
# Option 1: clone first (recommended — you can read and edit)
git clone https://github.com/grandfactor/macos-setup.git ~/code/macos-setup
cd ~/code/macos-setup
less scripts/bootstrap.sh            # read it
zsh scripts/bootstrap.sh             # full setup, ~20–40 min depending on the Brewfile

# Option 2: one line on a brand-new Mac (Terminal.app → paste)
/bin/zsh -c "$(curl -fsSL https://raw.githubusercontent.com/grandfactor/macos-setup/main/scripts/bootstrap.sh)"
```

Flags:

| Flag | Effect |
|---|---|
| `--minimal` | Core CLI tools + mise/uv + a dozen Tier-1 apps (Ghostty, VS Code, Raycast, Rectangle, Firefox, OrbStack…). ~10 minutes. |
| `--no-defaults` | Skip `macos-defaults.sh` (keep Apple's UI defaults). |
| `--no-apps` | Skip the Brewfile entirely; install only `git gh mise uv starship fzf zoxide eza bat fd ripgrep jq`. |
| `--dotfiles <git-url>` | Clone your dotfiles to `~/.dotfiles` and run its `install.sh` (or `install`, `bootstrap.sh`, `setup.sh`) at the end. |
| `GIT_NAME=… GIT_EMAIL=…` (env) | Skip the Git identity prompts. |

What it deliberately leaves to you: **FileVault** (needs your password and a recovery-key decision in the GUI), **Find My / Stolen Device Protection**, **Time Machine** destination, **Xcode.app** (12 GB; `mas install 497799835`), granting **Accessibility/Full Disk Access** prompts, and signing in to apps. The script ends with a checklist of those.

## `scripts/bootstrap.sh`

{{include:scripts/bootstrap.sh|sh}}

### Notes on specific steps

- **Command Line Tools headless install** uses the `softwareupdate` trick (touch the `.installondemand.in-progress` file so the CLT package shows up in `softwareupdate -l`). If Apple's catalog doesn't list it — happens for a few days around a new macOS release — the script falls back to the GUI prompt and waits for Enter.
- **Homebrew** is installed with `NONINTERACTIVE=1`; analytics are turned off. The `shellenv` line goes in `~/.zprofile` (login shells) so GUI apps launched from the Dock also see `/opt/homebrew/bin` — see [chapter 8](08-homebrew.html) and [chapter 22](22-troubleshooting.html) on PATH.
- **Rosetta** is opt-in because macOS 27 removes it by default and macOS 28 removes it entirely; installing it hides the Intel-only apps you should be replacing ([chapter 2](02-first-boot-and-migration.html)).
- **Brewfile filtering**: `mas` lines are dropped if you're not signed in to the App Store (the install would fail); `vscode` extension lines are dropped if VS Code isn't in the selected set. `--no-upgrade` keeps an already-installed formula at its version rather than upgrading mid-bootstrap.
- **SSH signing** for Git commits is configured instead of GPG: no agent to babysit, the same key you use for GitHub auth, verified badge on GitHub once uploaded as a *signing* key (the script does this via `gh ssh-key add --type signing` if you log in) — [chapter 10](10-dotfiles-and-git.html).
- **Touch ID for sudo** is written to `/etc/pam.d/sudo_local`, which macOS 14+ preserves across updates (`/etc/pam.d/sudo` is reset by every update) — [chapter 9](09-terminal-and-shell.html).
- **The `.zshrc` starter** is appended only if there's no `starship init` line already; it's meant to be replaced by your dotfiles. Order matters: `zsh-syntax-highlighting` must be sourced last.
- **`sudo` keep-alive + `caffeinate`** prevent the two classic bootstrap failures: the sudo timestamp expiring during a long `brew bundle`, and the Mac sleeping halfway through.

## `scripts/macos-defaults.sh`

The `defaults write` collection from [chapter 3](03-system-settings.html), expanded. Every line is a preference you could set by clicking; nothing here needs a reboot except keyboard repeat rate, trackpad settings, and Stage Manager (log out/in). Run it standalone with `zsh scripts/macos-defaults.sh`; re-running is harmless.

{{include:scripts/macos-defaults.sh|sh}}

Things to reconsider before running: `KeyRepeat 1` is *very* fast (use `2` if characters double up); `hibernatemode 25` + `destroyfvkeyonstandby 1` is the paranoid sleep setting (slower wake, but RAM is wiped) — comment it out on a desktop or if wake-from-sleep feels slow; `com.apple.swipescrolldirection` is "natural" scrolling — set `false` if you're coming from Windows/Linux and hate it; the hot corners (lock screen bottom-right, desktop top-right) are one person's habit.

To find the key for any setting not covered: `defaults read > /tmp/a; (change it in System Settings); defaults read > /tmp/b; diff /tmp/a /tmp/b`.

## `scripts/cleanup.sh`

The monthly disk cleanup from [chapter 18](18-performance-and-maintenance.html). Removes only things that regenerate: Homebrew caches and orphaned dependencies, Xcode DerivedData and unavailable simulators, stopped containers and dangling images, package-manager caches, old logs, Trash, and Time Machine local snapshots. Prints how much it freed.

{{include:scripts/cleanup.sh|sh}}

Schedule it with launchd (monthly on the 1st at 12:00) — see [chapter 21](21-automation-and-scripting.html) for the plist pattern:

```sh
mkdir -p ~/Library/LaunchAgents
cat > ~/Library/LaunchAgents/com.macos-setup.cleanup.plist <<EOT
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>com.macos-setup.cleanup</string>
  <key>ProgramArguments</key><array><string>/bin/sh</string><string>$HOME/code/macos-setup/scripts/cleanup.sh</string></array>
  <key>StartCalendarInterval</key><dict><key>Day</key><integer>1</integer><key>Hour</key><integer>12</integer></dict>
  <key>EnvironmentVariables</key><dict><key>PATH</key><string>/opt/homebrew/bin:/usr/bin:/bin</string></dict>
  <key>StandardOutPath</key><string>/tmp/cleanup.log</string>
</dict></plist>
EOT
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.macos-setup.cleanup.plist
```

## `scripts/audit.sh`

A read-only security and health check from [chapter 16](16-security-and-privacy.html): FileVault, firewall, Gatekeeper, SIP, screensaver password, guest account, automatic updates, sharing services, SSH server, launch agents and system extensions counts, disk space, last Time Machine backup, uptime, Rosetta presence, SSH key, Touch ID sudo. Run it after bootstrap and each semester.

{{include:scripts/audit.sh|sh}}

## Adapting these for your own dotfiles

The intended end state is that **your dotfiles repo** owns the configuration and these scripts are just the bootstrap that gets you to `git clone`. A common layout:

```
~/.dotfiles/
├── install.sh          # stow/symlink + brew bundle + mise install; idempotent
├── Brewfile            # brew bundle dump --describe, pruned
├── macos-defaults.sh   # your fork of the script above
├── zsh/ .zshrc .zprofile .zshenv
├── git/ .gitconfig .gitignore_global
├── ghostty/ config
├── starship.toml
├── mise/ config.toml
├── vscode/ settings.json keybindings.json extensions.txt
├── hammerspoon/ init.lua
├── karabiner/ karabiner.json
└── ssh/ config           # no keys!
```

Then bootstrap becomes: `zsh bootstrap.sh --no-apps --no-defaults --dotfiles git@github.com:you/dotfiles.git` and your `install.sh` does the rest. [Chapter 10](10-dotfiles-and-git.html) covers stow vs chezmoi vs a bare repo, secrets handling, and per-machine branches.
