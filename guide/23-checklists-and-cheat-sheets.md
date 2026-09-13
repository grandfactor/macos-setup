<!--
number: 23
part: Part VI — Reference
description: The whole guide compressed into printable checklists — the day-one setup order, the 30-minute security pass, the developer-environment checklist, weekly/monthly maintenance, a new-project checklist, a pre-travel checklist, and one-page cheat sheets for the terminal, Homebrew, mise/uv, Git, containers, and macOS CLI tools.
-->
# Checklists & cheat sheets

Everything in the previous 22 chapters, boiled down to lists you can tick. Each item links back to where it's explained. Print this page (`⌘P` — the site has a print stylesheet) or keep it open on a second screen during setup day.

## Day one: the setup order

Doing these in order avoids redoing work (e.g., install Homebrew *before* restoring dotfiles that assume it; turn on FileVault *before* copying data so it's encrypted from the start).

**Before unboxing** — [ch. 1](01-hardware-and-buying.html), [ch. 2](02-first-boot-and-migration.html)

- [ ] Old Mac: Time Machine backup complete; dotfiles repo pushed; `brew bundle dump` committed; export browser data; note license keys; sign out of iMessage/Music if selling it.
- [ ] Have your Apple Account password and a second trusted device for 2FA.
- [ ] Decide: migrate (Migration Assistant, convenient) or fresh install (clean, this guide's default).

**Setup Assistant** — [ch. 2](02-first-boot-and-migration.html)

- [ ] Language/region; connect Wi-Fi; skip Migration Assistant if going fresh.
- [ ] Sign in with Apple Account (enables Find My/Activation Lock, iCloud Keychain).
- [ ] Account name short and lowercase (`alex`, not `Alex Smith`) — it becomes your home folder.
- [ ] **Turn on FileVault** when offered; choose iCloud/Passwords app for the recovery key.
- [ ] Touch ID; Apple Pay optional; Siri optional; Screen Time skip; Analytics off.
- [ ] Appearance: Auto.

**First 15 minutes** — [ch. 3](03-system-settings.html), [ch. 16](16-security-and-privacy.html)

- [ ] Software Update → install everything; enable automatic security responses.
- [ ] Privacy & Security: FileVault on (verify), Firewall on, Lockdown Mode no (unless needed), Stolen Device Protection on.
- [ ] Lock Screen: require password immediately after sleep; screen saver 5 min.
- [ ] Trackpad: Tap to click, tracking speed, three-finger drag (Accessibility).
- [ ] Keyboard: key repeat fast, delay short; Caps Lock → Escape/Control; `fn` key → "Do Nothing" or Dictation off; disable press-and-hold accents.
- [ ] Dock: auto-hide, smaller, remove default apps, "Show recent apps" off.
- [ ] Finder: show path bar, status bar, extensions, `~/Library`; new window opens Home; search current folder.
- [ ] Desktop & Dock: hot corners; Stage Manager off (or on, your call); click wallpaper to reveal desktop → "Only in Stage Manager".
- [ ] Spotlight/Siri: pick your launcher shortcut plan (`⌘Space` for Spotlight or Raycast).
- [ ] Run the `defaults write` script from [ch. 3](03-system-settings.html) (or `scripts/macos-defaults.sh` in [Appendix A](appendix-a-bootstrap-script.html)).

**Developer bootstrap (30–60 min, mostly waiting)** — [ch. 7](07-command-line-tools-and-xcode.html)–[10](10-dotfiles-and-git.html)

- [ ] `xcode-select --install` (Command Line Tools).
- [ ] Install Homebrew; add `shellenv` to `~/.zprofile`; `brew doctor`.
- [ ] `brew bundle --file=Brewfile` ([Appendix B](appendix-b-brewfile.html)) — terminal, editor, CLI tools, fonts, apps.
- [ ] Ghostty (or chosen terminal) + Nerd Font; open it, close Terminal.app forever.
- [ ] Clone dotfiles; run the installer/stow; new shell — prompt, aliases, plugins working.
- [ ] `git config` user/email; generate `ssh-keygen -t ed25519`; add to GitHub (`gh auth login`); enable commit signing (SSH).
- [ ] Touch ID for `sudo` (`/etc/pam.d/sudo_local`).
- [ ] `mise` installed and activated; `mise use -g node@lts python@3.13 …`; `uv` for Python.
- [ ] Editor: sign in to Settings Sync; extensions restored; `code`/`cursor`/`zed` CLI on PATH.
- [ ] Containers: OrbStack (or Docker Desktop/`container`); `docker run hello-world`.
- [ ] Full Xcode only if you need iOS/macOS dev (12 GB, App Store or `xcodes`).

**Apps and accounts** — [ch. 19](19-daily-driver-apps.html)

- [ ] Password manager first; sign in; browser extension.
- [ ] Browsers: default browser set; sync signed in; content blocker; profiles for work/personal.
- [ ] Launcher (Raycast/Alfred) hotkey; clipboard manager; window manager (Rectangle/AeroSpace) — grant Accessibility.
- [ ] Menu bar: Ice, Stats, Itsycal.
- [ ] Communication apps installed and set **not** to open at login.
- [ ] Cloud storage clients; iCloud Drive Desktop & Documents sync decided (default: off for developers).

**Before the end of day one** — [ch. 17](17-backup-and-recovery.html)

- [ ] Time Machine to an external drive (encrypted) — first backup running.
- [ ] Cloud backup (Backblaze/Arq/iCloud) configured, or at least documents in iCloud Drive.
- [ ] Verify Find My shows the Mac; note the serial number in your password manager.
- [ ] `brew bundle dump --force --describe` — commit the actual Brewfile to dotfiles.
- [ ] Reboot once. Everything should come back exactly as you left it.

## The 30-minute security pass

From [ch. 16](16-security-and-privacy.html). Do it on day one and again each semester.

- [ ] `fdesetup status` → FileVault On. Recovery key stored somewhere you can reach without the Mac.
- [ ] Firewall on; "Block all incoming connections" off (breaks AirDrop/Handoff); stealth mode on.
- [ ] Gatekeeper at default ("App Store & Known Developers"). Understand the Privacy & Security → Open Anyway flow; never `xattr -d` random downloads.
- [ ] Automatic updates on (macOS, App Store, security responses). Homebrew upgraded weekly.
- [ ] Password manager with unique passwords; passkeys where offered; 2FA on Apple Account, GitHub, email, bank; hardware key (YubiKey) for Apple Account and GitHub if you can.
- [ ] Lock screen: immediately; hot corner or `⌃⌘Q` habit; require password after screen saver.
- [ ] Stolen Device Protection on; Find My on; Activation Lock verified.
- [ ] Privacy → review Full Disk Access, Accessibility, Screen Recording, Input Monitoring, Automation, Location; revoke anything you don't recognize.
- [ ] Sharing: everything off unless used (Screen Sharing, Remote Login/SSH, File Sharing, Remote Management).
- [ ] Safari/browser: block cross-site tracking; Private Relay if iCloud+; DNS over HTTPS profile or router-level.
- [ ] Optional: LuLu outbound firewall; Little Snitch; Objective-See tools (BlockBlock, KnockKnock).
- [ ] Guest user off; auto-login off; login window shows name and password fields (not user list) on shared machines.
- [ ] Secrets: none in dotfiles repo; API keys in Keychain or 1Password CLI; `.env` files gitignored.
- [ ] SSH: ed25519 keys with passphrase in Keychain; `PasswordAuthentication no` on any server you own.
- [ ] Run the audit script from [ch. 16](16-security-and-privacy.html); all green.

## Developer environment checklist

From [ch. 7](07-command-line-tools-and-xcode.html)–[15](15-databases-and-local-dev.html). Green means `which` finds it, it runs, and it's the version you expect.

- [ ] `xcode-select -p` → `/Library/Developer/CommandLineTools` (or Xcode.app).
- [ ] `brew doctor` → "ready to brew"; `brew --prefix` → `/opt/homebrew`; no `/usr/local` Homebrew unless intentional.
- [ ] Shell: `echo $SHELL` → `/bin/zsh`; `time zsh -i -c exit` < 300 ms; prompt shows git branch; `fzf` `⌃R` history; `zoxide`; `eza`/`bat`/`fd`/`rg`/`jq` installed.
- [ ] Terminal: Nerd Font renders icons; true color (`curl -s https://gist.githubusercontent.com/lifepillar/09a44b8cf0f9397465614e622979107f/raw/24-bit-color.sh | bash`); `⌥` as Meta; copy-on-select decided.
- [ ] `git --version` (Homebrew's, not Apple's, if you want latest); `git config --global -l` shows name, email, `init.defaultBranch main`, `pull.rebase`, signing, `core.excludesfile` with `.DS_Store`.
- [ ] `ssh -T git@github.com` → authenticated; `gh auth status` ok.
- [ ] `mise doctor` clean; `mise ls` shows global tools; `node -v`, `python3 -V`, `java -version`, `go version`, `rustc -V` as needed.
- [ ] `uv --version`; `uv python list` shows installed interpreters; no global `pip install`s.
- [ ] Editor opens from the CLI (`code .`); formatting on save; language servers; Copilot/agent configured (or deliberately off).
- [ ] `docker version` client + server; `docker context ls` points at the intended runtime; `docker compose version`.
- [ ] Databases: `psql --version`; `brew services list` shows what autostarts (ideally nothing); TablePlus/DBeaver connects.
- [ ] Cloud CLIs authed as needed (`aws sts get-caller-identity`, `gcloud auth list`, `az account show`); `kubectl config get-contexts`.
- [ ] `~/code` (or your layout) exists; excluded from Spotlight and Time Machine as decided; not inside iCloud Drive.
- [ ] Dotfiles repo: `git status` clean; `install.sh` idempotent; Brewfile current.
- [ ] `~/.local/bin` on PATH; personal scripts there.

## New project checklist

- [ ] `mkdir ~/code/<org>/<project> && cd` there; `git init` (or `gh repo create --private --clone`).
- [ ] `.tool-versions` / `mise.toml` pins runtime versions; `mise install`.
- [ ] Python: `uv init` → `pyproject.toml`; `uv add …`; `.venv` gitignored (uv does it). Node: `npm init`/`pnpm init`; `engines` field; lockfile committed.
- [ ] `.gitignore` for the stack + `.DS_Store` (global) + `.env`.
- [ ] `.editorconfig`; formatter/linter config (`ruff`, `biome`/`prettier`, `gofmt`…); pre-commit hooks (`pre-commit` or `lefthook`).
- [ ] `README.md` with one-command setup and run instructions; `LICENSE` if public.
- [ ] `compose.yaml` for databases/services; `.env.example` committed, `.env` not.
- [ ] CI: GitHub Actions workflow running tests on push (`actions/setup-node`/`setup-python` with the same pinned version).
- [ ] Editor workspace settings (`.vscode/settings.json`, recommended extensions) if the team shares them; Copilot disabled per-workspace if the course forbids it.
- [ ] First commit, push, branch protection on `main` for group work.

## Weekly / monthly / semester maintenance

From [ch. 18](18-performance-and-maintenance.html), [ch. 17](17-backup-and-recovery.html).

**Weekly (5 min)**

- [ ] `brew update && brew upgrade && brew cleanup`; `mise upgrade`.
- [ ] `uptime` > 14 days → reboot.
- [ ] `df -h /` < 15% free → cleanup script.
- [ ] Time Machine ran in the last 24 h (`tmutil latestbackup`).

**Monthly (15 min)**

- [ ] Run `scripts/cleanup.sh` (brew, Xcode DerivedData, Docker prune, package caches, Trash, local snapshots).
- [ ] Login Items & Extensions: remove anything unfamiliar or unused.
- [ ] Battery: cycle count noted; charge limit on if docked; `pmset -g batt`.
- [ ] `brew bundle cleanup` → decide add-to-Brewfile vs uninstall; commit the Brewfile.
- [ ] Password manager: security report / breached-password check.
- [ ] macOS point update installed.

**Each semester / quarter (1 h)**

- [ ] Restore test: open a random old file from Time Machine; `git clone` your dotfiles onto a fresh user account and run the installer.
- [ ] Re-verify student offers (GitHub Education, JetBrains) — [ch. 20](20-cs-student-specific.html).
- [ ] Privacy permissions audit; SSH keys audit on GitHub/servers (remove old machines); rotate API tokens older than a year.
- [ ] `npx npkill`; `docker system prune -a`; `mise prune`; delete simulators you don't use.
- [ ] Check macOS support status; plan the major upgrade ~2–4 weeks after release once your critical tools confirm compatibility.
- [ ] Re-read the "What's new" section on the guide's [landing page](index.html); update Brewfile and dotfiles for tool changes.

## Before travel / a conference / an exam

- [ ] Backup completed *today*; laptop bag also has the charger (65 W GaN) and a USB-C cable; power bank if flying.
- [ ] Find My verified; Stolen Device Protection on; auto-lock immediate.
- [ ] Charge limit off the night before (charge to 100%); Low Power Mode on when on battery.
- [ ] `brew services stop --all`; quit Docker; close Electron apps not needed → hours more battery.
- [ ] Offline: docs downloaded (Dash/DevDocs), papers in Zotero synced, repos pulled, `uv sync`/`npm ci` run, lecture slides saved locally, Apple Maps offline area.
- [ ] Border crossing: consider logging out of sensitive accounts; FileVault means a powered-off Mac is safe; know your jurisdiction's rules.
- [ ] Presenting: Do Not Disturb Focus scheduled; notifications off on the projector display; screen mirroring resolution tested; HDMI/USB-C adapter packed; `caffeinate -d` or Amphetamine.
- [ ] Exam with lockdown browser: install and test days before; disable Karabiner/Hammerspoon/clipboard managers that proctoring software flags; know the Wi-Fi.

## Cheat sheet: macOS keyboard essentials

The full table is [Appendix C](appendix-c-keyboard-shortcuts.html). The 20 that matter most:

| Shortcut | Does |
|---|---|
| `⌘Space` | Spotlight (or your launcher) |
| `⌘Tab` / `⌘\`` | Switch apps / switch windows of the current app |
| `⌘Q` / `⌘W` / `⌘H` / `⌘M` | Quit / close window / hide / minimize |
| `⌥⌘⎋` | Force Quit dialog |
| `⌘,` | Preferences of any app |
| `⌘⇧3` / `⌘⇧4` / `⌘⇧5` | Screenshot full / selection / toolbar & recording (add `⌃` → clipboard) |
| `⌃⌘Q` | Lock screen |
| `⌃↑` / `⌃←→` | Mission Control / switch Spaces |
| `fn` (Globe) + `E` / `Q` / `C` / `N` / `D` | Emoji / Quick Note / Control Center / Notifications / Dictation |
| `⌘⇧.` | Toggle hidden files (Finder/open dialogs) |
| `⌘⇧G` | Go to folder (Finder/open dialogs — type or paste a path) |
| `Space` | Quick Look selected file |
| `⌘⌫` / `⌘⇧⌫` | Move to Trash / empty Trash |
| `⌘↑` / `⌘↓` / `⌘O` | Parent folder / open (Finder) |
| `⌃A` / `⌃E` / `⌃K` / `⌥←→` | Emacs-style line editing in every text field |
| `⌘⇧V` | Paste and match style (most apps) |
| `⌃⌘Space` | Character viewer (emoji/symbols) — or `fn E` |
| `⌘⌥D` | Toggle Dock |
| `⌘⌥⌃8` (via Accessibility shortcut) | Invert colors — set up in Accessibility → Shortcut |
| Hold `⌥` while clicking menu bar icons | Extra info (Wi-Fi diagnostics, Bluetooth details, Sound devices) |

## Cheat sheet: terminal on macOS

```sh
# Files
open .                     # Finder here          open -a "Visual Studio Code" file
open -R file               # reveal in Finder     qlmanage -p file 2>/dev/null  # Quick Look
pbcopy < file ; pbpaste    # clipboard            trash file    # brew install trash
mdfind -onlyin ~ "query"   # Spotlight search     mdls file     # metadata
ls -la@                    # extended attrs       xattr -d com.apple.quarantine file
du -shx * | sort -rh | head  # what's big         dust / ncdu   # interactive

# System
sw_vers ; uname -m ; uptime ; system_profiler SPHardwareDataType
memory_pressure | tail -1 ; sysctl vm.swapusage ; df -h /
top -o cpu -stats pid,command,cpu,mem ; sudo powermetrics --samplers smc -n1 -i1000
pmset -g batt ; pmset -g assertions ; caffeinate -dis cmd
softwareupdate -l ; softwareupdate --install-rosetta --agree-to-license
launchctl list | grep -v com.apple ; launchctl bootout gui/$(id -u)/label
log show --last 10m --predicate 'messageType == error' --style compact
diskutil list ; diskutil apfs list ; tmutil listlocalsnapshots /
defaults read com.apple.dock ; defaults write -g KeyRepeat -int 2 ; killall Dock

# Network
lsof -nP -iTCP -sTCP:LISTEN            # who's listening
kill $(lsof -t -iTCP:3000)             # free a port
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder   # flush DNS
scutil --dns | grep nameserver | sort -u ; sudo wdutil info
networksetup -listallhardwareports ; ipconfig getifaddr en0

# Security
fdesetup status ; spctl --status ; csrutil status ; sudo pfctl -s info
security find-generic-password -s name -w      # read a Keychain secret
codesign -dv --verbose=2 /Applications/App.app ; codesign -s - -f ./bin

# Automation
osascript -e 'display notification "done" with title "build"'
shortcuts run "Name" ; say "done" ; afplay /System/Library/Sounds/Glass.aiff
```

## Cheat sheet: Homebrew 6

```sh
brew install pkg          brew install --cask app      brew uninstall --zap app
brew search x             brew info x                  brew home x
brew update               brew upgrade [--greedy]      brew cleanup --prune=all -s
brew outdated             brew pin x / brew unpin x    brew autoremove
brew list --formula       brew list --cask             brew leaves   # top-level only
brew deps --tree x        brew uses --installed x      brew doctor
brew services list        brew services run x          brew services start/stop x
brew bundle dump --force --describe       brew bundle [--file=~/Brewfile]     brew bundle cleanup
brew tap user/repo        brew untap user/repo         # Homebrew 6: taps prompt for trust
brew exec cmd             # run with Homebrew's env (6.0)
brew --prefix [x]         brew --cache                 brew shellenv
HOMEBREW_NO_AUTO_UPDATE=1 brew install x               # skip update this once
```

## Cheat sheet: mise + uv

```sh
# mise — runtimes
mise use -g node@lts python@3.13 java@21 go@latest    # global
mise use node@24                                       # per-project → mise.toml
mise install ; mise ls ; mise ls-remote node ; mise outdated ; mise upgrade
mise exec node@22 -- node script.js ; mise run task    # tasks from mise.toml
mise doctor ; mise prune ; mise self-update
mise settings set idiomatic_version_file_enable_tools node,python   # .nvmrc/.python-version

# uv — Python
uv python install 3.13 ; uv python list ; uv python pin 3.13
uv init ; uv add requests ; uv add --dev pytest ruff ; uv remove x
uv sync ; uv lock ; uv run pytest ; uv run script.py
uv tool install ruff ; uvx black .        # global tools, isolated (pipx replacement)
uv pip install -r requirements.txt        # pip-compatible mode inside .venv
uv venv ; source .venv/bin/activate       # if you want a classic venv
uv cache clean
# inline script deps (PEP 723):  # /// script \n # dependencies = ["httpx"] \n # ///
```

## Cheat sheet: Git

```sh
git init -b main ; gh repo create --private --source=. --push
git status -sb ; git add -p ; git commit -m "type(scope): msg" ; git push -u origin HEAD
git switch -c feature ; git switch - ; git branch -d feature
git fetch --prune ; git pull --rebase ; git rebase -i origin/main
git stash push -m "wip" ; git stash pop ; git stash list
git log --oneline --graph --all -20 ; git log -p --follow file ; git blame -w -C file
git diff --staged ; git diff main...HEAD ; git difftool
git restore file ; git restore --staged file ; git reset --soft HEAD~1 ; git revert sha
git reflog                                    # undo almost anything
git worktree add ../proj-fix fix-branch       # parallel checkouts
git bisect start ; git bisect bad ; git bisect good sha ; git bisect run ./test.sh
git config --global rerere.enabled true       # remember conflict resolutions
gh pr create --fill ; gh pr checkout 42 ; gh pr view --web ; gh run watch
# signing (SSH):  git config --global gpg.format ssh ; user.signingkey ~/.ssh/id_ed25519.pub ; commit.gpgsign true
```

## Cheat sheet: containers

```sh
docker context ls ; docker context use orbstack
docker run --rm -it -v "$PWD":/w -w /w -p 8080:80 image cmd
docker run -d --name pg -e POSTGRES_PASSWORD=pw -p 5432:5432 -v pgdata:/var/lib/postgresql/data postgres:18
docker ps -a ; docker logs -f name ; docker exec -it name sh ; docker stop name ; docker rm -f name
docker build -t app . ; docker buildx build --platform linux/arm64,linux/amd64 -t app --push .
docker run --platform linux/amd64 image          # x86 image via Rosetta (until macOS 28)
docker compose up -d ; docker compose logs -f svc ; docker compose down -v
docker system df ; docker system prune -a --volumes ; docker image prune
orb create ubuntu:24.04 dev ; orb -m dev bash ; orb list ; orb stop dev    # OrbStack Linux machines
container run --rm -it alpine sh                  # Apple's container CLI
```

## Cheat sheet: where things live

| What | Path |
|---|---|
| Homebrew | `/opt/homebrew` (`bin/`, `Cellar/`, `Caskroom/`, `etc/`, `var/`) |
| Command Line Tools | `/Library/Developer/CommandLineTools` |
| Xcode | `/Applications/Xcode.app`; `~/Library/Developer/Xcode/DerivedData` |
| Shell config | `~/.zshenv` → `~/.zprofile` (login) → `~/.zshrc` (interactive); system: `/etc/zshrc`, `/etc/paths.d/` |
| User launch agents | `~/Library/LaunchAgents` (3rd-party system: `/Library/LaunchAgents`, `/Library/LaunchDaemons`) |
| App preferences | `~/Library/Preferences/*.plist`; sandboxed: `~/Library/Containers/<bundle>/Data/Library/Preferences` |
| App support/data | `~/Library/Application Support/<App>` |
| Caches / logs | `~/Library/Caches`, `~/Library/Logs`, `/Library/Logs/DiagnosticReports` |
| Mise / uv / cargo / go | `~/.local/share/mise`, `~/.cache/uv` + `~/.local/share/uv`, `~/.cargo`, `~/go` |
| SSH / GPG | `~/.ssh` (`config`, keys, `known_hosts`), `~/.gnupg` |
| Keychains | `~/Library/Keychains`; system `/Library/Keychains` |
| Fonts | `~/Library/Fonts` (user), `/Library/Fonts` (all users) |
| iCloud Drive | `~/Library/Mobile Documents/com~apple~CloudDocs` |
| Screenshots default | `~/Desktop` (change: `defaults write com.apple.screencapture location …`) |
| Time Machine local snapshots | hidden; `tmutil listlocalsnapshots /` |
| Hosts file | `/etc/hosts` (then flush DNS) |
| Sudo Touch ID | `/etc/pam.d/sudo_local` |
| System (read-only, sealed) | `/System`, `/usr/bin`, `/bin`; writable: `/usr/local`, `/opt`, `/Library`, `~` |

## Cheat sheet: version and support timeline (September 2026)

| Thing | Current | Next | Notes |
|---|---|---|---|
| macOS | 26.6 Tahoe | **27 Golden Gate — 14 Sept 2026** | Apple-silicon only; Rosetta removed on 27 (reinstallable), gone in 28 |
| Security updates | 26.x, 25.x (Sequoia), 24.x (Sonoma) | 24 drops when 27 ships | Stay within N-1 |
| Xcode | 26.x | 27 with macOS 27 | ~12 GB |
| Homebrew | 6.x | — | tap trust prompts, `brew exec`, Intel Tier 3 |
| Node | 24 LTS (active) | **26 LTS — Oct 2026** | New yearly release model |
| Python | 3.14 | **3.15 — Oct 2026** | Use `uv` |
| Java | 25 LTS | 27 LTS Sept 2027 | 21 still common in courses |
| Go / Rust | 1.27 / 1.9x | 6-month / 6-week cadence | `mise use go@latest` |
| PostgreSQL | 18 | 19 — Sept/Oct 2026 | `postgresql@18` |
| Ghostty | 1.3 | — | — |
| VS Code | monthly | — | — |

Exact numbers will drift — [Appendix E](appendix-e-sources.html) lists where to check.
