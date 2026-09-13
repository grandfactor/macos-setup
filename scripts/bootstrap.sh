#!/bin/zsh
# bootstrap.sh — set up a fresh Apple-silicon Mac (macOS 26/27) for development in one go.
#
#   Fresh Mac:   /bin/zsh -c "$(curl -fsSL https://raw.githubusercontent.com/grandfactor/macos-setup/main/scripts/bootstrap.sh)"
#   From clone:  zsh scripts/bootstrap.sh [--minimal] [--no-defaults] [--no-apps] [--dotfiles <git-url>]
#
# What it does (each step is idempotent and skipped if already done):
#   1. Xcode Command Line Tools        5. Brewfile (full or --minimal)      9. Touch ID for sudo
#   2. Homebrew (+ shellenv)           6. mise + uv, default runtimes      10. Dotfiles (optional)
#   3. Rosetta (only if you say yes)   7. Git identity + SSH key           11. Summary & next steps
#   4. macOS defaults (optional)       8. Shell plugins / starship
#
# It does NOT: turn on FileVault (do it in System Settings — needs your password and a recovery-key choice),
# install Xcode.app (12 GB; `mas install 497799835` or the App Store), or touch anything under /System.
# Read the whole file before running it on your machine. Every step is a function; comment out what you don't want.
#
# Companion to The macOS Setup Guide — https://grandfactor.github.io/macos-setup/appendix-a-bootstrap-script.html

set -euo pipefail

# ─── Options ──────────────────────────────────────────────────────────────────
MINIMAL=0; DO_DEFAULTS=1; DO_APPS=1; DOTFILES_URL="${DOTFILES_URL:-}"
GIT_NAME="${GIT_NAME:-}"; GIT_EMAIL="${GIT_EMAIL:-}"
REPO_RAW="https://raw.githubusercontent.com/grandfactor/macos-setup/main"
while (( $# )); do
  case "$1" in
    --minimal)      MINIMAL=1 ;;
    --no-defaults)  DO_DEFAULTS=0 ;;
    --no-apps)      DO_APPS=0 ;;
    --dotfiles)     DOTFILES_URL="$2"; shift ;;
    -h|--help)      sed -n '2,20p' "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac; shift
done

# ─── Helpers ──────────────────────────────────────────────────────────────────
autoload -Uz colors && colors
step() { print -P "\n%F{blue}%B▶ $1%b%f"; }
ok()   { print -P "%F{green}  ✔ $1%f"; }
skip() { print -P "%F{yellow}  ↷ $1 (already done)%f"; }
die()  { print -P "%F{red}  ✖ $1%f" >&2; exit 1; }
ask()  { local a; read -q "a?$1 [y/N] "; echo; [[ $a == [yY] ]]; }
have() { command -v "$1" >/dev/null 2>&1; }
SCRIPT_DIR="${0:A:h}"
fetch() { # fetch <relative-path> → stdout, from local clone if present else from GitHub
  if [[ -f "$SCRIPT_DIR/$1" ]]; then cat "$SCRIPT_DIR/$1"; else curl -fsSL "$REPO_RAW/scripts/$1"; fi
}

# ─── Preflight ────────────────────────────────────────────────────────────────
step "Preflight"
[[ "$(uname -s)" == Darwin ]] || die "This is for macOS."
[[ "$(uname -m)" == arm64 ]]  || die "Apple silicon only (Intel Macs can't run macOS 27; see chapter 1)."
osver=$(sw_vers -productVersion); (( ${osver%%.*} >= 26 )) || echo "  ⚠ macOS $osver — this guide targets 26+; most steps still work."
[[ $EUID -ne 0 ]] || die "Don't run as root; it will ask for sudo when needed."
ok "macOS $osver on $(sysctl -n machdep.cpu.brand_string)"
# Keep sudo alive for the duration (needed for CLT, defaults, pam)
sudo -v; ( while true; do sudo -n true; sleep 50; kill -0 "$$" 2>/dev/null || exit; done ) 2>/dev/null &
caffeinate -dimsu -w $$ &   # don't sleep mid-install

# ─── 1. Command Line Tools ────────────────────────────────────────────────────
step "Xcode Command Line Tools"
if xcode-select -p >/dev/null 2>&1 && [[ -e "$(xcode-select -p)/usr/bin/git" ]]; then
  skip "CLT at $(xcode-select -p)"
else
  # Headless install: create the trigger file, find the label, install via softwareupdate
  touch /tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress
  label=$(softwareupdate -l 2>/dev/null | grep -o 'Label: Command Line Tools.*' | sed 's/^Label: //' | tail -1)
  if [[ -n "$label" ]]; then
    softwareupdate -i "$label" --verbose
  else
    xcode-select --install 2>/dev/null || true
    echo "  A dialog opened — install the Command Line Tools, then press Enter."; read -r
  fi
  rm -f /tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress
  xcode-select -p >/dev/null 2>&1 || die "CLT still missing"
  ok "installed"
fi
sudo xcodebuild -license accept 2>/dev/null || true

# ─── 2. Homebrew ──────────────────────────────────────────────────────────────
step "Homebrew"
if [[ -x /opt/homebrew/bin/brew ]]; then
  skip "/opt/homebrew"
else
  NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ok "installed"
fi
eval "$(/opt/homebrew/bin/brew shellenv)"
if ! grep -qs 'brew shellenv' ~/.zprofile; then
  printf '\n# Homebrew\neval "$(/opt/homebrew/bin/brew shellenv)"\n' >> ~/.zprofile
  ok "added shellenv to ~/.zprofile"
fi
brew analytics off >/dev/null 2>&1 || true
brew update --quiet
[[ -d /usr/local/Homebrew ]] && echo "  ⚠ Intel Homebrew found in /usr/local — you probably want to remove it (chapter 8)."

# ─── 3. Rosetta (opt-in) ──────────────────────────────────────────────────────
step "Rosetta 2"
if [[ -f /Library/Apple/usr/share/rosetta/rosetta ]]; then
  skip "installed"
elif ask "  Install Rosetta 2? (needed only for Intel-only apps / x86 containers; removed in macOS 28)"; then
  softwareupdate --install-rosetta --agree-to-license && ok "installed"
else
  ok "skipped"
fi

# ─── 4. macOS defaults ────────────────────────────────────────────────────────
step "macOS defaults"
if (( DO_DEFAULTS )); then
  fetch macos-defaults.sh > /tmp/macos-defaults.sh && zsh /tmp/macos-defaults.sh && ok "applied (scripts/macos-defaults.sh)"
else
  ok "skipped (--no-defaults)"
fi

# ─── 5. Brewfile ──────────────────────────────────────────────────────────────
step "Brewfile"
if (( DO_APPS )); then
  fetch Brewfile > /tmp/Brewfile
  if (( MINIMAL )); then
    # Minimal: core CLI + mise/uv + terminal/editor/launcher only (everything up to the "Fonts" section, plus Tier 1 casks)
    awk '/^# ─── Fonts/{exit} {print}' /tmp/Brewfile > /tmp/Brewfile.min
    grep -E '^cask "(ghostty|visual-studio-code|raycast|rectangle|maccy|jordanbaird-ice|stats|itsycal|shottr|appcleaner|the-unarchiver|bitwarden|karabiner-elements|font-jetbrains-mono-nerd-font|orbstack|firefox)"' /tmp/Brewfile >> /tmp/Brewfile.min
    mv /tmp/Brewfile.min /tmp/Brewfile
    ok "minimal set"
  fi
  # mas needs an App Store login; skip mas lines if not signed in
  if ! mas account >/dev/null 2>&1; then sed -i '' '/^mas /d' /tmp/Brewfile; echo "  ℹ not signed into the App Store — skipping mas entries"; fi
  # vscode lines need `code` on PATH; brew bundle handles the ordering, but skip if VS Code isn't in this Brewfile
  grep -q '^cask "visual-studio-code"' /tmp/Brewfile || sed -i '' '/^vscode /d' /tmp/Brewfile
  HOMEBREW_BUNDLE_NO_LOCK=1 brew bundle --file=/tmp/Brewfile --no-upgrade || echo "  ⚠ some formulae failed; run 'brew bundle --file=/tmp/Brewfile' again later"
  ok "brew bundle done"
else
  ok "skipped (--no-apps)"
  brew install --quiet git gh mise uv starship fzf zoxide eza bat fd ripgrep jq
fi

# ─── 6. Runtimes ──────────────────────────────────────────────────────────────
step "Runtimes (mise + uv)"
have mise || brew install --quiet mise
have uv   || brew install --quiet uv
eval "$(mise activate zsh)"
mise settings set experimental true >/dev/null 2>&1 || true
mise use -g -y node@lts python@3.13 >/dev/null && ok "node@lts, python@3.13 via mise"
if ask "  Also install java@21 and go@latest?"; then mise use -g -y java@21 go@latest && ok "java, go"; fi
uv python install 3.13 >/dev/null 2>&1 || true
ok "uv $(uv --version | awk '{print $2}')"

# ─── 7. Git + SSH ─────────────────────────────────────────────────────────────
step "Git identity and SSH key"
if [[ -z "$(git config --global user.name 2>/dev/null)" ]]; then
  [[ -n "$GIT_NAME" ]]  || read -r "GIT_NAME?  Git user.name: "
  [[ -n "$GIT_EMAIL" ]] || read -r "GIT_EMAIL?  Git user.email: "
  git config --global user.name "$GIT_NAME"; git config --global user.email "$GIT_EMAIL"
fi
git config --global init.defaultBranch main
git config --global pull.rebase true
git config --global push.autoSetupRemote true
git config --global rerere.enabled true
git config --global core.excludesfile ~/.gitignore_global
grep -qs '^\.DS_Store$' ~/.gitignore_global 2>/dev/null || printf '.DS_Store\n._*\n.Spotlight-V100\n.Trashes\n.env\n.venv/\nnode_modules/\n.idea/\n.vscode/*\n!.vscode/settings.json\n!.vscode/extensions.json\n' >> ~/.gitignore_global
have delta && git config --global core.pager "delta" && git config --global interactive.diffFilter "delta --color-only"
ok "git configured for $(git config --global user.name)"

if [[ ! -f ~/.ssh/id_ed25519 ]]; then
  mkdir -p ~/.ssh && chmod 700 ~/.ssh
  ssh-keygen -t ed25519 -C "$(git config --global user.email)" -f ~/.ssh/id_ed25519
  ssh-add --apple-use-keychain ~/.ssh/id_ed25519
  ok "ed25519 key created"
else
  skip "~/.ssh/id_ed25519"
fi
if ! grep -qs 'UseKeychain' ~/.ssh/config; then
  cat >> ~/.ssh/config <<'CFG'
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
  ServerAliveInterval 60
CFG
  chmod 600 ~/.ssh/config; ok "~/.ssh/config"
fi
# SSH commit signing (no GPG needed)
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
if have gh && ! gh auth status >/dev/null 2>&1; then
  if ask "  Log in to GitHub now (uploads the SSH key as auth + signing key)?"; then
    gh auth login -p ssh -h github.com -w
    gh ssh-key add ~/.ssh/id_ed25519.pub --type signing --title "$(scutil --get ComputerName) signing" 2>/dev/null || true
  fi
fi

# ─── 8. Shell ─────────────────────────────────────────────────────────────────
step "Shell"
[[ "$SHELL" == */zsh ]] || chsh -s /bin/zsh
if [[ ! -f ~/.zshrc ]] || ! grep -qs 'starship init' ~/.zshrc; then
  cat >> ~/.zshrc <<'ZRC'

# ── added by macos-setup bootstrap (replace with your dotfiles) ──
export EDITOR="code --wait"; export VISUAL="$EDITOR"
export PATH="$HOME/.local/bin:$PATH"
HISTSIZE=100000; SAVEHIST=100000; setopt SHARE_HISTORY HIST_IGNORE_ALL_DUPS HIST_IGNORE_SPACE
setopt AUTO_CD CORRECT INTERACTIVE_COMMENTS
autoload -Uz compinit && compinit -C
zstyle ':completion:*' menu select
eval "$(mise activate zsh)"
eval "$(zoxide init zsh)"
eval "$(fzf --zsh)"
eval "$(starship init zsh)"
source "$(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh"
source "$(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"   # must be last
alias ls='eza --icons --group-directories-first' ll='eza -la --icons --git' cat='bat -p' g=git
alias brewup='brew update && brew upgrade && brew cleanup'
ZRC
  ok "~/.zshrc starter written"
else
  skip "~/.zshrc"
fi
mkdir -p ~/.local/bin ~/code
if [[ ! -f ~/.config/starship.toml ]]; then
  mkdir -p ~/.config; starship preset nerd-font-symbols -o ~/.config/starship.toml 2>/dev/null || true
fi

# ─── 9. Touch ID for sudo ─────────────────────────────────────────────────────
step "Touch ID for sudo"
if grep -qs pam_tid /etc/pam.d/sudo_local; then
  skip "/etc/pam.d/sudo_local"
elif [[ -f /etc/pam.d/sudo_local.template ]]; then
  sed 's/^#auth/auth/' /etc/pam.d/sudo_local.template | sudo tee /etc/pam.d/sudo_local >/dev/null && ok "enabled"
else
  echo "auth       sufficient     pam_tid.so" | sudo tee /etc/pam.d/sudo_local >/dev/null && ok "enabled"
fi

# ─── 10. Dotfiles ─────────────────────────────────────────────────────────────
step "Dotfiles"
if [[ -n "$DOTFILES_URL" ]]; then
  if [[ -d ~/.dotfiles ]]; then skip "~/.dotfiles"; else git clone "$DOTFILES_URL" ~/.dotfiles && ok "cloned"; fi
  for inst in install.sh install bootstrap.sh setup.sh; do
    [[ -x ~/.dotfiles/$inst ]] && { (cd ~/.dotfiles && ./$inst); ok "ran $inst"; break; }
  done
else
  ok "none given (--dotfiles <url> to clone and run its install.sh)"
fi

# ─── 11. Summary ──────────────────────────────────────────────────────────────
step "Done"
cat <<SUMMARY

  Next, by hand (chapter 2, 16, 17):
    • System Settings → Privacy & Security → FileVault → ON  (store the recovery key in Passwords)
    • System Settings → Privacy & Security → Stolen Device Protection → ON;  Find My → ON
    • Grant Accessibility to Rectangle/Raycast/Hammerspoon/Karabiner when they ask
    • Plug in a drive → Time Machine → encrypt → start the first backup
    • Open a NEW terminal window (Ghostty is installed) — the prompt, mise, fzf, etc. activate there
    • Sign into: password manager, browser sync, Raycast, VS Code Settings Sync, App Store (then: mas install 497799835 for Xcode)
    • Run  zsh scripts/audit.sh  to check the security posture; add scripts/cleanup.sh to your monthly routine

  Log: brew list --formula | wc -l  formulae, $(brew list --cask 2>/dev/null | wc -l | tr -d ' ') casks. Enjoy the Mac.
SUMMARY
