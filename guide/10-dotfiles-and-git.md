<!--
number: 10
part: Part III — Developer environment
description: Version-controlling your configuration with a bare repo, chezmoi or stow; a complete Git setup for macOS (identity, signing with SSH keys, delta, aliases, global ignore); GitHub CLI; direnv; and secrets hygiene.
-->
# Dotfiles & Git

Everything you configured in the last three chapters lives in text files. Put them in a Git repository and a new Mac — or a reset one — goes from Setup Assistant to *your* environment in twenty minutes. This chapter also sets up Git itself the way a working engineer has it, because the defaults are from 2005.

## What counts as dotfiles

Anything under `~` that starts with a `.`, plus the modern `~/.config/*` tree:

| Config | Path |
|---|---|
| zsh | `~/.zshenv`, `~/.zprofile`, `~/.zshrc` |
| Git | `~/.config/git/config`, `~/.config/git/ignore` (XDG paths — no more `~/.gitconfig`) |
| Ghostty | `~/.config/ghostty/config` |
| Starship | `~/.config/starship.toml` |
| mise | `~/.config/mise/config.toml` |
| tmux | `~/.config/tmux/tmux.conf` |
| Neovim | `~/.config/nvim/` |
| Karabiner | `~/.config/karabiner/karabiner.json` |
| AeroSpace | `~/.aerospace.toml` (or `~/.config/aerospace/aerospace.toml`) |
| Homebrew | `~/.config/homebrew/Brewfile` |
| SSH | `~/.ssh/config` (**not** the keys) |
| VS Code | `~/Library/Application Support/Code/User/settings.json`, `keybindings.json` (or use Settings Sync) |
| Zed | `~/.config/zed/settings.json`, `keymap.json` |
| macOS defaults | your `macos-defaults.sh` script (Chapter 3 / Appendix A) |

**Never commit**: `~/.ssh/id_*`, `~/.gnupg/`, `~/.aws/credentials`, `~/.npmrc` with tokens, `~/.netrc`, `.env` files, anything from `~/Library/Keychains`. Chapter 16 covers where secrets go instead.

## Three ways to manage them

### 1. The bare-repo trick (zero tools)

Your home directory *is* the working tree; the `.git` directory lives elsewhere so `~` doesn't look like a repo.

```sh
git init --bare "$HOME/.dotfiles"
alias dot='git --git-dir="$HOME/.dotfiles" --work-tree="$HOME"'   # put this in .zshrc
dot config status.showUntrackedFiles no
dot add ~/.zshrc ~/.config/ghostty/config ~/.config/starship.toml ~/.config/git/config
dot commit -m "initial dotfiles"
dot remote add origin git@github.com:you/dotfiles.git
dot push -u origin main
```

On a new machine:

```sh
git clone --bare git@github.com:you/dotfiles.git "$HOME/.dotfiles"
alias dot='git --git-dir="$HOME/.dotfiles" --work-tree="$HOME"'
dot checkout            # fails if files exist — move them aside, retry
dot config status.showUntrackedFiles no
```

Pros: no dependencies, files live in place, `dot diff` works. Cons: no templating (same file on every machine), no secrets handling, easy to accidentally `dot add` something large.

### 2. chezmoi (recommended for more than one machine)

**chezmoi** (`brew install chezmoi`) is a single Go binary that keeps the source of truth in `~/.local/share/chezmoi` and *applies* it to `~`. Its strengths: **templates** (one `.gitconfig` with `{{ if eq .chezmoi.hostname "work-mbp" }}` blocks), **secrets** pulled from 1Password/Bitwarden/Keychain at apply time (never stored in the repo), `run_once_` scripts (install Homebrew, run `brew bundle`, apply `defaults`), and first-class support for macOS/Linux differences.

```sh
chezmoi init                                  # creates the source repo
chezmoi add ~/.zshrc ~/.config/ghostty/config # copies into the source dir (as dot_zshrc, dot_config/ghostty/config)
chezmoi edit ~/.zshrc                         # edit the source version
chezmoi diff                                  # what would change
chezmoi apply                                 # write to ~
chezmoi cd && git add -A && git commit -m "…" && git push
# new machine — one line, including running your install scripts:
sh -c "$(curl -fsLS get.chezmoi.io)" -- init --apply you
```

A secrets template line: `token = {{ onepasswordRead "op://Private/GitHub/token" }}` — chezmoi calls the 1Password CLI at apply time. Machine-specific data lives in `~/.config/chezmoi/chezmoi.toml` (`[data] email = "…"`, `work = true`).

### 3. GNU Stow / yadm / Nix Home Manager

- **Stow** (`brew install stow`): keep `~/dotfiles/zsh/.zshrc`, `~/dotfiles/ghostty/.config/ghostty/config`, run `stow zsh ghostty` to symlink them into `~`. Simple, transparent, no templating. Very popular.
- **yadm**: the bare-repo trick with templating and encryption bolted on.
- **Home Manager (Nix)**: declarative, reproducible, manages packages *and* config, steep learning curve; the right answer if you're already Nix-curious and wrong for a first-year student.

Pick chezmoi if you have (or will have) a work Mac and a personal Mac; the bare repo or Stow if you have one machine and like simplicity.

## Repository layout and bootstrap

Whatever the tool, include an `install.sh` (idempotent) at the repo root so the sequence on a fresh Mac is:

```sh
xcode-select --install
git clone git@github.com:you/dotfiles.git ~/.dotfiles   # or the chezmoi one-liner
~/.dotfiles/install.sh
```

The script (Appendix A is a complete one) should: install Homebrew if missing → `brew bundle` → link/apply dotfiles → run `macos-defaults.sh` → `mise install` → set up Touch ID sudo → remind you of the manual steps (sign in to 1Password, add SSH key to GitHub, grant Accessibility to Raycast/Karabiner). Keep a `README.md` with those manual steps; you'll thank yourself in two years.

Structure that scales:

```
dotfiles/
├── install.sh
├── Brewfile
├── macos-defaults.sh
├── zsh/            .zshenv .zprofile .zshrc
├── git/            config ignore
├── ghostty/        config
├── starship.toml
├── mise/           config.toml
├── nvim/           …
├── karabiner/      karabiner.json
├── aerospace/      aerospace.toml
├── vscode/         settings.json keybindings.json extensions.txt
└── README.md       manual steps, hardware notes
```

Include `.zshrc.local` in `.gitignore` and source it from `.zshrc` for machine-specific bits (work proxies, secrets, aliases you'd rather not publish).

## Git, configured properly

Homebrew's `git` (`brew install git`) is newer than Apple's. Use the XDG location so `~` stays clean:

```sh
mkdir -p ~/.config/git
```

`~/.config/git/config`:

```ini
[user]
    name = Alex Kowalski
    email = alex@example.com
    signingkey = ~/.ssh/id_ed25519.pub        # sign commits with your SSH key (no GPG needed)
[gpg]
    format = ssh
[gpg "ssh"]
    allowedSignersFile = ~/.config/git/allowed_signers
    # 1Password users: program = /Applications/1Password.app/Contents/MacOS/op-ssh-sign
[commit]
    gpgsign = true
    verbose = true                            # show the diff in the commit message editor
[tag]
    gpgsign = true
[init]
    defaultBranch = main
[core]
    editor = nvim                             # or: code --wait / zed --wait
    pager = delta
    autocrlf = input
    excludesfile = ~/.config/git/ignore
    fsmonitor = true                          # faster status in big repos (uses FSEvents)
    untrackedCache = true
[color]
    ui = auto
[column]
    ui = auto
[branch]
    sort = -committerdate
[tag]
    sort = version:refname
[fetch]
    prune = true
    pruneTags = true
    all = true
[pull]
    rebase = true
[push]
    default = simple
    autoSetupRemote = true                    # first `git push` just works
    followTags = true
[rebase]
    autoSquash = true
    autoStash = true
    updateRefs = true
[merge]
    conflictstyle = zdiff3
[diff]
    algorithm = histogram
    colorMoved = plain
    mnemonicPrefix = true
    renames = true
[rerere]
    enabled = true
    autoupdate = true
[help]
    autocorrect = prompt
[interactive]
    diffFilter = delta --color-only
[delta]
    navigate = true
    side-by-side = false
    line-numbers = true
    hyperlinks = true
[credential]
    helper = osxkeychain                      # HTTPS tokens in the Keychain; `gh auth login` sets this up too
[url "git@github.com:"]
    insteadOf = https://github.com/           # always push over SSH even if you cloned via HTTPS
[alias]
    st = status -sb
    co = checkout
    sw = switch
    br = branch
    ci = commit
    ca = commit --amend --no-edit
    cm = commit -m
    lg = log --oneline --graph --decorate --all -30
    last = log -1 HEAD --stat
    unstage = reset HEAD --
    undo = reset --soft HEAD~1
    wip = !git add -A && git commit -m "wip"
    fixup = commit --fixup
    please = push --force-with-lease
    aliases = config --get-regexp ^alias\\.
    ignored = ls-files --others --ignored --exclude-standard
    root = rev-parse --show-toplevel
    cleanup = "!git branch --merged | grep -vE '(^\\*|main|master|develop)' | xargs -r git branch -d"
[includeIf "gitdir:~/Developer/work/"]
    path = ~/.config/git/config-work          # different email/signing key for work repos
```

Notes on the choices:

- **SSH commit signing** (Git ≥ 2.34) reuses your SSH key — no GPG keyring to manage. Add the same public key to GitHub as a *Signing key* (`gh ssh-key add ~/.ssh/id_ed25519.pub --type signing`), and put `alex@example.com ssh-ed25519 AAAA…` in `~/.config/git/allowed_signers` so `git log --show-signature` verifies locally. With **1Password** as SSH agent, set `gpg.ssh.program` to `op-ssh-sign` and Touch ID approves each signature.
- `fsmonitor` + `untrackedCache` make `git status` instant in monorepos on macOS.
- `pull.rebase = true` and `rebase.autoStash` keep history linear for the solo-dev workflow; teams that merge can flip it.
- `includeIf` lets your work identity kick in automatically for anything under `~/Developer/work/`.
- `delta` (`brew install git-delta`) gives syntax-highlighted, line-numbered diffs; `difftastic` (`git difftool -t difftastic` after `[difftool "difftastic"] cmd = difft "$LOCAL" "$REMOTE"`) understands syntax trees.

Global ignore, `~/.config/git/ignore`:

```
# macOS
.DS_Store
.AppleDouble
.LSOverride
._*
.Spotlight-V100
.Trashes
Icon?
# editors
.idea/
.vscode/*
!.vscode/settings.json
!.vscode/extensions.json
*.swp
*~
.zed/
# envs & secrets (belt and braces — repos should ignore these too)
.env
.env.*
!.env.example
.envrc
.direnv/
# tooling
.mise.local.toml
.tool-versions.local
node_modules/
__pycache__/
.venv/
.pytest_cache/
.ruff_cache/
.mypy_cache/
target/
dist/
build/
```

## GitHub CLI

`brew install gh`, then `gh auth login` (choose SSH, upload your key, authenticate in the browser). It configures the Keychain credential helper too. Daily use:

```sh
gh repo create my-project --private --clone     # new repo + clone
gh repo clone owner/repo
gh pr create --fill                             # PR from the current branch
gh pr checkout 123                              # review someone's PR locally
gh pr view --web
gh pr checks --watch
gh issue list --assignee @me
gh run watch                                    # tail a GitHub Actions run
gh api repos/{owner}/{repo}/releases            # any REST call
gh extension install dlvhdr/gh-dash             # a TUI dashboard of PRs/issues
gh copilot suggest "undo last commit but keep changes"   # gh-copilot extension
```

GitLab has `glab`; Bitbucket has nothing good. **Git GUI clients** if you want one: **Fork** ($50, fast, best interactive rebase UI), **Tower** ($69/yr), **GitKraken**, **Sublime Merge**, **GitHub Desktop** (free, basic), or the Git panels in VS Code/Zed/JetBrains — plus `lazygit` in the terminal, which many people end up preferring to all of them.

## direnv: per-directory environment

`brew install direnv`, hook it in `.zshrc` (`eval "$(direnv hook zsh)"`). Drop a `.envrc` in a project:

```sh
# .envrc
dotenv_if_exists .env          # load KEY=value pairs from .env (which is gitignored)
export DATABASE_URL=postgres://localhost/myapp_dev
PATH_add ./bin ./node_modules/.bin
layout python                  # or `use mise` / `use flake` (nix) — activates a venv automatically
```

`direnv allow` once; from then on, `cd` into the directory loads the environment and leaving it unloads it. `mise` (Chapter 11) can do the env part too (`[env]` in `.mise.toml`), so many people use only mise; direnv remains the standard for teams with mixed tooling and for Nix flakes.

## Secrets hygiene for repos

- Commit `.env.example` with placeholder keys; never `.env`. Add `.env*` to the global ignore (above) *and* each repo's `.gitignore`.
- Install **gitleaks** or **trufflehog** (`brew install gitleaks`) and run it as a pre-commit hook: `pre-commit` (`brew install pre-commit`) with a `.pre-commit-config.yaml` including `gitleaks`. GitHub's push protection also blocks known token formats on push for public repos and for orgs with Advanced Security.
- If you *do* commit a secret: rotate it immediately (assume it's compromised the moment it hits a remote), then rewrite history with `git filter-repo` and force-push. Rotating is the important part; the rewrite is hygiene.
- Store personal API keys in the **macOS Keychain** (`security add-generic-password -a "$USER" -s openai_api_key -w`) and read them in `.zshrc` lazily, or in **1Password** and inject with `op run --env-file=.env.tpl -- npm start`. Both beat a plaintext `export OPENAI_API_KEY=` in your dotfiles.
- SSH keys: one per machine, passphrase-protected, in the Keychain or a hardware token. Revoke a machine's key on GitHub when you sell it.
