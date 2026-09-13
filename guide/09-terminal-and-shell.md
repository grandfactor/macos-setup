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
