<!--
number: 09
part: Part III — Developer environment
description: Choosing a terminal (Ghostty, iTerm2, WezTerm, Kitty, Warp), zsh configured properly without a framework, Starship, fzf, zoxide, the modern Rust CLI toolkit, tmux, SSH keys, and Touch ID for sudo.
-->
# Terminal & shell

You'll spend more hours in the terminal than in any other window. The 2026 recipe: a **GPU-accelerated terminal** (Ghostty), **zsh** with a small hand-written config instead of a heavyweight framework, **Starship** for the prompt, **fzf** and **zoxide** for navigation, and a set of modern Rust replacements for the classic Unix tools. Everything here is in the Brewfile from Chapter 8.

## Choosing a terminal emulator

Terminal.app got 24-bit colour, Powerline glyph support and a new default theme in Tahoe; it's genuinely fine now. Most developers still switch for splits, better keybindings, and speed.

| Terminal | Best for | Config | Notes |
|---|---|---|---|
| **Ghostty** (free, OSS, Zig) | **Default recommendation.** Native macOS UI (real tabs, windows, Liquid Glass), fastest renderer, sensible defaults | `~/.config/ghostty/config` — plain `key = value` | 1.3 (Mar 2026) added scrollback search (<kbd>⌘</kbd><kbd>F</kbd>), native scrollbars, click-to-move-cursor, command-finished notifications, key tables, drag-to-reorder splits, "Set as default terminal". 6-month release cadence. |
| **iTerm2** (free, OSS) | Deepest feature set: shell integration, triggers, tmux `-CC` native integration, per-profile everything, password manager | GUI prefs (exportable JSON) | 15 years of polish; slower rendering than the GPU terminals; still the choice for tmux-CC users. |
| **WezTerm** (free, OSS, Rust) | Cross-platform (identical on Linux/Windows), Lua config, built-in multiplexer, SSH domains | `~/.wezterm.lua` | The pick if you live on more than one OS and want one config. |
| **Kitty** (free, OSS) | Speed, keyboard-driven, kittens (icat, diff, ssh), graphics protocol | `~/.config/kitty/kitty.conf` | Opinionated maintainer, non-native window chrome. Great with Neovim. |
| **Warp** (freemium, closed) | AI-native: blocks, command palette, natural-language → command, agent mode | GUI | Account optional since 2025; a different paradigm; polarising. Try it if you're new to the CLI. |
| **Alacritty** (free, OSS) | Minimal, fast, no tabs/splits (use tmux) | TOML | Purists only. |
| **Terminal.app** | Zero install | GUI | Fine for occasional use; no splits. |

Install Ghostty and make it default (Ghostty → *Set Ghostty as Default Terminal App*):

```sh
brew install --cask ghostty
```

A starter `~/.config/ghostty/config`:

```
# Font (install a Nerd Font via Homebrew cask; icons in prompts need it)
font-family = JetBrainsMono Nerd Font
font-size = 13
font-thicken = true
adjust-cell-height = 10%

# Theme: light/dark follows the system
theme = light:GitHub-Light-Default,dark:GitHub-Dark-Default
background-opacity = 0.97
background-blur = 20
macos-titlebar-style = tabs
macos-option-as-alt = true            # so ⌥ works as Meta in the shell (Emacs bindings, ⌥← word jumps)
cursor-style = bar
cursor-style-blink = false
mouse-hide-while-typing = true
copy-on-select = clipboard
window-save-state = always
window-inherit-working-directory = true
split-inherit-working-directory = true
scrollback-limit = 100000000
shell-integration-features = cursor,sudo,title
notify-on-command-finish = unfocused
notify-on-command-finish-after = 30s

# Keybinds (defaults are good; a few additions)
keybind = super+d=new_split:right
keybind = super+shift+d=new_split:down
keybind = super+alt+left=goto_split:left
keybind = super+alt+right=goto_split:right
keybind = super+alt+up=goto_split:up
keybind = super+alt+down=goto_split:down
keybind = super+shift+enter=toggle_split_zoom
keybind = global:super+grave=toggle_quick_terminal    # drop-down terminal from anywhere
```

Ghostty ships shell integration for zsh/bash/fish that enables: jump between prompts (<kbd>⌘</kbd><kbd>↑</kbd>/<kbd>↓</kbd>), copy last command's output, click to move the cursor in the prompt, `sudo` with Touch ID passthrough, and the working directory in new tabs. `ghostty +list-themes` previews 400+ themes; `ghostty +show-config --default --docs` lists every option.

**iTerm2 users**: turn on *Shell Integration* (iTerm2 → Install Shell Integration), set *Option key = Esc+* in the profile's Keys tab, enable *GPU rendering*, and consider *Triggers* (highlight or notify on regex in output). **tmux -CC** turns tmux windows into native tabs — unique to iTerm2.

## Shell: zsh, configured by hand

macOS's default shell has been **zsh** since Catalina. Keep it. (Fish is lovely but not POSIX; Bash 3.2 is ancient; Nushell is interesting but niche.) If you want the newest zsh, `brew install zsh`, add `/opt/homebrew/bin/zsh` to `/etc/shells`, then `chsh -s /opt/homebrew/bin/zsh` — but Apple's `/bin/zsh` is fine.

### Skip Oh My Zsh (or use it knowingly)

Oh My Zsh, Prezto and Zim add hundreds of aliases and a plugin manager with a measurable startup cost, and hide *how* things work — exactly what a CS student should be learning. The modern approach is ~60 lines of your own `.zshrc` plus three plugins loaded directly. If you already love OMZ, keep it, trim to 3–5 plugins, and use a fast prompt. Either way, measure: `time zsh -i -c exit` should be under 100 ms.

### Where zsh reads config

| File | Read when | Put here |
|---|---|---|
| `~/.zshenv` | Every zsh (including scripts) | `PATH`-independent environment variables, `XDG_*`, `EDITOR`. Keep tiny. |
| `~/.zprofile` | Login shells (each new terminal tab on macOS is a login shell) | `eval "$(brew shellenv)"`, `PATH` additions. |
| `~/.zshrc` | Interactive shells | Aliases, functions, completion, prompt, plugins, key bindings. |
| `~/.zlogout` | On exit | Rarely used. |
| `/etc/zshrc`, `/etc/zprofile` | System-wide, before yours | Apple's; `/etc/zprofile` runs `path_helper`, which rebuilds `PATH` from `/etc/paths` and `/etc/paths.d/*` and **reorders** it — which is why `PATH` set in `.zshenv` gets clobbered. Set PATH in `.zprofile` or `.zshrc`. |

### A complete, fast `.zshrc`

```sh
# ~/.zshrc — no framework, ~50ms startup
# --- Homebrew (also in .zprofile for login shells; harmless twice) ---
eval "$(/opt/homebrew/bin/brew shellenv)"

# --- history: big, shared, deduplicated ---
HISTFILE="$HOME/.zsh_history"
HISTSIZE=200000
SAVEHIST=200000
setopt SHARE_HISTORY INC_APPEND_HISTORY HIST_IGNORE_ALL_DUPS HIST_IGNORE_SPACE HIST_REDUCE_BLANKS HIST_VERIFY EXTENDED_HISTORY

# --- behaviour ---
setopt AUTO_CD            # `..` and `dirname` without cd
setopt AUTO_PUSHD PUSHD_IGNORE_DUPS PUSHD_SILENT
setopt EXTENDED_GLOB GLOB_DOTS NO_CASE_GLOB
setopt INTERACTIVE_COMMENTS
setopt CORRECT            # suggest corrections for mistyped commands
unsetopt BEEP
bindkey -e                # emacs keybindings (⌃A ⌃E ⌃K ⌃R …); `bindkey -v` for vi mode
WORDCHARS='*?_-.[]~=&;!#$%^(){}<>'   # ⌥⌫ stops at / and .

# --- completion ---
autoload -Uz compinit
# cache compdump; rebuild at most once a day
if [[ -n ~/.zcompdump(#qN.mh+24) ]]; then compinit; else compinit -C; fi
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*:descriptions' format '%F{yellow}-- %d --%f'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path "$HOME/.cache/zsh/zcompcache"
# Homebrew site-functions are on fpath via brew shellenv (gh, docker, kubectl completions land there)

# --- plugins (installed via brew; sourced directly, no plugin manager) ---
source "$(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh"
source "$(brew --prefix)/share/zsh-history-substring-search/zsh-history-substring-search.zsh"
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down
ZSH_AUTOSUGGEST_STRATEGY=(history completion)
ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE=40
source "$(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"   # must be last plugin

# --- tools ---
eval "$(starship init zsh)"                # prompt
eval "$(zoxide init zsh --cmd cd)"         # `cd` learns your dirs; `cdi` interactive
eval "$(fzf --zsh)"                        # ⌃R history, ⌃T files, ⌥C cd
eval "$(mise activate zsh)"                # per-project runtimes (Chapter 11)
eval "$(direnv hook zsh)"                  # per-directory env (Chapter 10)
export FZF_DEFAULT_COMMAND='fd --type f --hidden --exclude .git'
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
export FZF_ALT_C_COMMAND='fd --type d --hidden --exclude .git'
export FZF_DEFAULT_OPTS='--height 40% --layout=reverse --border --info=inline'
export FZF_CTRL_T_OPTS="--preview 'bat --color=always --style=numbers --line-range=:200 {}'"

# --- environment ---
export EDITOR="nvim"         # or "code --wait" / "zed --wait"
export VISUAL="$EDITOR"
export PAGER="less -RFX"
export MANPAGER="sh -c 'col -bx | bat -l man -p'"   # coloured man pages
export BAT_THEME="ansi"
export HOMEBREW_NO_ENV_HINTS=1
export HOMEBREW_BUNDLE_FILE="$HOME/.config/homebrew/Brewfile"
export GPG_TTY=$(tty)

# --- aliases ---
alias ls='eza --group-directories-first --icons=auto'
alias ll='eza -lah --git --group-directories-first --icons=auto'
alias lt='eza --tree --level=2 --icons=auto'
alias cat='bat --paging=never'
alias du='dust'
alias df='duf'
alias top='btop'
alias vim='nvim'
alias g='git'
alias gs='git status -sb'
alias gl='git log --oneline --graph --decorate -20'
alias gd='git diff'
alias gp='git push'
alias gc='git commit'
alias gco='git switch'
alias ..='cd ..'
alias ...='cd ../..'
alias rm='trash'                     # brew install trash; `command rm` for the real thing
alias mkd='mkdir -p'
alias path='echo -e ${PATH//:/\\n}'
alias reload='exec zsh'
alias brewup='brew update && brew upgrade && brew autoremove && brew cleanup --prune=all'
alias ip='curl -s https://ifconfig.me && echo'
alias localip="ipconfig getifaddr en0"
alias flushdns='sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder'

# --- functions ---
mkcd() { mkdir -p "$1" && cd "$1"; }
# fuzzy kill
fkill() { ps -ef | sed 1d | fzf -m --header='[kill:process]' | awk '{print $2}' | xargs -r kill -${1:-9}; }
# fuzzy git branch switch
gb() { git branch --all | grep -v HEAD | fzf --preview 'git log --oneline --graph -20 {1}' | sed 's/.* //' | sed 's#remotes/origin/##' | xargs -r git switch; }
# extract anything
extract() {
  case "$1" in
    *.tar.bz2|*.tbz2) tar xjf "$1" ;;  *.tar.gz|*.tgz) tar xzf "$1" ;;  *.tar.xz) tar xJf "$1" ;;
    *.tar) tar xf "$1" ;;  *.bz2) bunzip2 "$1" ;;  *.gz) gunzip "$1" ;;  *.zip) unzip "$1" ;;
    *.7z) 7z x "$1" ;;  *.rar) unrar x "$1" ;;  *) echo "don't know how to extract '$1'" ;;
  esac
}
cheat() { curl -s "cheat.sh/$1"; }

# --- local overrides (not in dotfiles repo) ---
[[ -f ~/.zshrc.local ]] && source ~/.zshrc.local
```

Install the pieces:

```sh
brew install starship zoxide fzf zsh-autosuggestions zsh-syntax-highlighting zsh-history-substring-search \
             eza bat ripgrep fd dust duf btop trash tlrc
```

Don't alias `grep` to `rg` or `find` to `fd` — scripts and tutorials that call `grep` expect BSD grep flags; use the new names directly and let muscle memory follow.

### Starship prompt

A single binary, fast, works in every shell, configured in `~/.config/starship.toml`. The default shows directory, git branch/status, language versions when relevant, command duration, and exit status. A compact two-line variant:

```toml
# ~/.config/starship.toml
add_newline = true
format = """
$directory$git_branch$git_status$git_state$python$nodejs$rust$golang$java$cmd_duration
$character"""
[character]
success_symbol = "[❯](bold green)"
error_symbol = "[❯](bold red)"
vimcmd_symbol = "[❮](bold yellow)"
[directory]
truncation_length = 4
truncate_to_repo = true
style = "bold cyan"
[git_branch]
symbol = " "
style = "bold purple"
[git_status]
style = "yellow"
ahead = "⇡${count}"
behind = "⇣${count}"
diverged = "⇕⇡${ahead_count}⇣${behind_count}"
[cmd_duration]
min_time = 2000
format = "took [$duration]($style) "
[python]
symbol = " "
format = '[${symbol}(${version} )(\($virtualenv\) )]($style)'
[nodejs]
symbol = " "
```

Presets: `starship preset nerd-font-symbols -o ~/.config/starship.toml` (needs a Nerd Font); `starship preset plain-text-symbols` if you don't want icons. Alternatives: **Powerlevel10k** (zsh-only, extremely fast with its instant prompt, more ornate), **Pure** (minimal), **Oh My Posh** (cross-shell, Windows heritage).

## The modern CLI toolkit

Rust/Go rewrites of the classics: faster, saner defaults, colour, and — importantly — identical on macOS and Linux, so your muscle memory ports to servers.

| Instead of | Use | Why |
|---|---|---|
| `ls` | **eza** | Colours, icons, git status column, tree mode |
| `cat` | **bat** | Syntax highlighting, line numbers, git diff gutter; `bat -p` for plain |
| `grep -r` | **ripgrep (rg)** | 10× faster, respects `.gitignore`, sane defaults |
| `find` | **fd** | Intuitive syntax (`fd pattern`), ignores `.git`, parallel |
| `cd` | **zoxide** | `cd proj` jumps to the most-used matching directory from anywhere |
| `history` / <kbd>⌃</kbd><kbd>R</kbd> | **fzf** (+ **atuin** optional) | Fuzzy everything; atuin syncs shell history across machines with a SQLite DB |
| `du` | **dust** | Visual tree of what's big |
| `df` | **duf** | Readable table |
| `top` | **btop** (or `htop`) | Pretty, mouse-driven, shows per-core and GPU on Apple silicon |
| `sed` (simple substitutions) | **sd** | `sd 'foo' 'bar' file` — no regex-escaping hell |
| `diff` | **difftastic** / **delta** | Syntax-aware diffs (`git difftool`) / beautiful `git diff` pager |
| `man` | **tlrc (tldr)** | Practical examples first: `tldr tar` |
| `curl` for APIs | **xh** or **httpie** | `xh :8080/api name=alex` |
| `jq` | **jq** (still) + **yq** for YAML, **fx** interactive | |
| `time` | **hyperfine** | Statistical benchmarking with warmup |
| `watch` | **watchexec** / `entr` | Re-run on file change: `watchexec -e py pytest` |
| `ps aux \| grep` | **procs** | Coloured, searchable process list |
| `nano`/`vim` for quick edits | **micro** or **helix** | Modern modal (helix) or non-modal (micro) editors |
| File manager | **yazi** | Blazing TUI file manager with previews; `y` shell wrapper cds on exit |
| Git TUI | **lazygit** | Stage hunks, rebase interactively, without memorising flags |
| Docker TUI | **lazydocker** | |
| Kubernetes TUI | **k9s** | |
| Markdown in terminal | **glow** | `glow README.md` |
| JSON/CSV data | **miller (mlr)**, **qsv**, **visidata** | Spreadsheets in the terminal |
| Misc | **ncdu**, **tokei** (LOC counter), **gping**, **dog** (DNS), **bandwhich**, **ouch** (archives), **presenterm** | |

Don't install all of these on day one. Start with `eza bat rg fd zoxide fzf`, add the rest as you notice the need.

## tmux (or not)

With Ghostty/iTerm2/WezTerm splits, **you don't need tmux locally**. You need it for **remote work** (sessions survive SSH disconnects) and if you want one layout that works identically over SSH. `brew install tmux`, then:

```
# ~/.config/tmux/tmux.conf
set -g prefix C-a            # ⌃A instead of ⌃B (Caps Lock → ⌃ makes this trivial)
unbind C-b
bind C-a send-prefix
set -g mouse on
set -g base-index 1
setw -g pane-base-index 1
set -g renumber-windows on
set -g history-limit 100000
set -g default-terminal "tmux-256color"
set -as terminal-features ",xterm-ghostty:RGB"
set -g escape-time 0
set -g focus-events on
bind | split-window -h -c "#{pane_current_path}"
bind - split-window -v -c "#{pane_current_path}"
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R
bind r source-file ~/.config/tmux/tmux.conf \; display "reloaded"
set -g status-position top
# plugins via tpm: `git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm`
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-yank'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'catppuccin/tmux'
run '~/.tmux/plugins/tpm/tpm'
```

**Zellij** is the modern alternative (Rust, discoverable keybindings shown on screen, layouts in KDL, floating panes). Good for beginners who find tmux's prefix-key model opaque.

## SSH

Generate a modern key (one per machine, never copied between machines):

```sh
ssh-keygen -t ed25519 -C "alex@mbp-2026"
# passphrase: yes. Store it in the keychain so you type it once per login:
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

`~/.ssh/config`:

```
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
  ServerAliveInterval 60
  ServerAliveCountMax 3
  IdentitiesOnly yes

Host github.com
  User git

Host uni
  HostName login.cs.university.edu
  User alex42
  ForwardAgent no
  # ProxyJump bastion.university.edu

Host homelab
  HostName 100.101.102.103      # Tailscale IP
  User alex
  LocalForward 5432 localhost:5432
```

Notes:

- `UseKeychain yes` is a macOS-only option: the passphrase is stored in the login keychain and the key auto-loads.
- Upload the public key with `gh ssh-key add ~/.ssh/id_ed25519.pub --title mbp-2026` (GitHub CLI), or `cat ~/.ssh/id_ed25519.pub | pbcopy` and paste it into the web UI.
- Prefer a **hardware key** (YubiKey, `ssh-keygen -t ed25519-sk`) or **1Password's SSH agent** (keys never sit unencrypted on disk; Touch ID approves each use) for your main identity. 1Password: enable *Developer → SSH Agent* and add `IdentityAgent "~/Library/Group Containers/2BUA8C4S2C.com.1password/t/agent.sock"` to the `Host *` block.
- Turn **on** *Remote Login* in Sharing only if you SSH *into* this Mac. If you do, disable password auth (`PasswordAuthentication no` in a file under `/etc/ssh/sshd_config.d/`) and keep the firewall on.
- **mosh** (`brew install mosh`) for flaky Wi‑Fi; **Tailscale** (Chapter 14) to reach your Mac from anywhere without port forwarding.
- Copy files with `rsync -avz --progress src/ user@host:dst/` — install Homebrew's `rsync`; Apple replaced it with the less capable `openrsync` in Sequoia.

## Touch ID for sudo

Apple made this survive OS updates by adding `/etc/pam.d/sudo_local`. Enable it once:

```sh
sudo sh -c 'sed "s/^#auth/auth/" /etc/pam.d/sudo_local.template > /etc/pam.d/sudo_local'
cat /etc/pam.d/sudo_local   # → auth sufficient pam_tid.so
```

Now `sudo` prompts with Touch ID (or your Apple Watch). Inside **tmux**, Touch ID needs `pam_reattach`: `brew install pam-reattach` and add `auth optional /opt/homebrew/lib/pam/pam_reattach.so` as the *first* line of `sudo_local`. Ghostty's `sudo` shell-integration feature forwards the terminal correctly so it works in splits.

## Fonts and rendering

Install a **Nerd Font** (a programming font patched with 3,000+ icons) — `brew install --cask font-jetbrains-mono-nerd-font` (or Fira Code, Iosevka, Monaspace, Cascadia Code, Geist Mono; Berkeley Mono if you pay for fonts). Use it in the terminal *and* your editor so icons in prompts, `eza`, Neovim and Starship render. Apple's **SF Mono** is excellent but has no icon glyphs; Ghostty falls back to a symbols font if installed (`brew install --cask font-symbols-only-nerd-font`).

Ligatures (`->` becoming an arrow) are a taste thing; JetBrains Mono and Fira Code have them, and Ghostty and most editors let you toggle them.

## Common terminal problems

- **`⌥←` inserts weird characters instead of jumping words**: set Option as Meta/Esc+ (Ghostty `macos-option-as-alt = true`; iTerm2 Profiles → Keys → Left Option = Esc+).
- **Slow new tab**: `time zsh -i -c exit`. Culprits: nvm (use mise), `compinit` without cache, Oh My Zsh with many plugins, Conda's init block. Use `zmodload zsh/zprof` at the top of `.zshrc` and `zprof` at the bottom to find it.
- **`PATH` order wrong / Homebrew tools shadowed by system ones**: `/etc/zprofile`'s `path_helper` reorders PATH; make sure `brew shellenv` runs *after* it (in `.zprofile` or `.zshrc`), and check with `which -a git`.
- **Colours look wrong over SSH**: the remote lacks `xterm-ghostty` terminfo — `infocmp -x xterm-ghostty | ssh host tic -x -` installs it, or set `SetEnv TERM=xterm-256color` for that host in `~/.ssh/config`.
- **Locale warnings on servers**: add `export LANG=en_US.UTF-8` to `.zshenv`.
- **Terminal asks for Full Disk Access / Files & Folders**: normal the first time you touch `~/Desktop`, `~/Documents`, `~/Downloads` or `~/Library/Mail`; grant it in Privacy & Security.
- **"Operation not permitted" writing to `/usr/bin`**: that's SIP; use Homebrew's prefix.
