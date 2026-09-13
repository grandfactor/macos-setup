<!--
number: 12
part: Part III — Developer environment
description: VS Code, Cursor, Zed, JetBrains, Neovim, Xcode and the AI coding agents — what each is for in 2026, recommended settings, and how to keep the configs in sync across machines.
-->
# Editors, IDEs & AI coding tools

The editor market split three ways in 2025–2026: **VS Code** remains the free universal default (~76% share in the Stack Overflow survey), **Cursor** is the AI-native fork that a fifth of developers now use, and **Zed** is the fast native newcomer. JetBrains stays the choice for Java/Kotlin and heavy refactoring; Neovim for the terminal-native; Xcode for Apple platforms. You don't have to pick one — most engineers run two.

## The recommendation

| You are… | Install | Why |
|---|---|---|
| A **CS student** | **VS Code** (free) + Copilot Student (free) — and **JetBrains** IDEs for Java/Kotlin courses (free with a student licence) | Every course's instructions assume VS Code; JetBrains for the JVM is what industry uses |
| A **working engineer**, general | **VS Code** or **Cursor** as primary, **Zed** for speed on big repos, terminal agent (Claude Code / Codex) alongside | The AI layer is now the differentiator; VS Code+Copilot vs Cursor is a taste/budget call |
| Deep in one ecosystem | **JetBrains** (IntelliJ/PyCharm/GoLand/RustRover/CLion/WebStorm) | Nothing beats their refactoring, debugger and framework awareness |
| Apple platforms | **Xcode 27** (+ VS Code/Zed for Swift packages) | Required for signing, simulators, Instruments |
| Terminal-native | **Neovim** (LazyVim or kickstart.nvim) or **Helix** | Everything over SSH, zero latency, infinitely configurable |

## Visual Studio Code

```sh
brew install --cask visual-studio-code
```

Launch once, then in the Command Palette (<kbd>⌘</kbd><kbd>⇧</kbd><kbd>P</kbd>) run *Shell Command: Install 'code' command in PATH* so `code .` works (Homebrew's cask usually does this for you). Turn on **Settings Sync** (sign in with GitHub) so extensions, settings, keybindings and snippets follow you to the next machine — or keep `settings.json`/`keybindings.json` in your dotfiles.

### Settings that matter

`⌘,` → open *settings.json* (the `{}` icon top right). A developer baseline:

```jsonc
{
  // --- editor ---
  "editor.fontFamily": "JetBrainsMono Nerd Font, Menlo, monospace",
  "editor.fontSize": 13,
  "editor.fontLigatures": true,
  "editor.lineHeight": 1.6,
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": { "source.fixAll": "explicit", "source.organizeImports": "explicit" },
  "editor.rulers": [88, 120],
  "editor.minimap.enabled": false,
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active",
  "editor.cursorSmoothCaretAnimation": "on",
  "editor.smoothScrolling": true,
  "editor.linkedEditing": true,
  "editor.stickyScroll.enabled": true,
  "editor.inlineSuggest.enabled": true,
  "editor.accessibilitySupport": "off",
  // --- files ---
  "files.autoSave": "onFocusChange",
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.exclude": { "**/.git": true, "**/node_modules": true, "**/.venv": true, "**/__pycache__": true },
  "files.watcherExclude": { "**/node_modules/**": true, "**/.venv/**": true, "**/target/**": true },
  "search.exclude": { "**/node_modules": true, "**/dist": true, "**/.venv": true },
  // --- workbench ---
  "workbench.startupEditor": "none",
  "workbench.colorTheme": "GitHub Dark Default",
  "workbench.iconTheme": "material-icon-theme",
  "workbench.editor.enablePreview": false,
  "workbench.tree.indent": 16,
  "window.autoDetectColorScheme": true,
  "window.newWindowDimensions": "inherit",
  "window.titleBarStyle": "custom",
  // --- terminal (runs your zsh, inherits mise) ---
  "terminal.integrated.fontFamily": "JetBrainsMono Nerd Font",
  "terminal.integrated.fontSize": 13,
  "terminal.integrated.defaultProfile.osx": "zsh",
  "terminal.integrated.scrollback": 20000,
  "terminal.integrated.macOptionIsMeta": true,
  "terminal.integrated.enableMultiLinePasteWarning": "never",
  // --- git ---
  "git.autofetch": true,
  "git.confirmSync": false,
  "git.enableSmartCommit": true,
  "git.openRepositoryInParentFolders": "always",
  "diffEditor.ignoreTrimWhitespace": false,
  // --- languages ---
  "[python]": { "editor.defaultFormatter": "charliermarsh.ruff", "editor.tabSize": 4 },
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true,
  "[go]": { "editor.defaultFormatter": "golang.go", "editor.tabSize": 4, "editor.insertSpaces": false },
  "[rust]": { "editor.defaultFormatter": "rust-lang.rust-analyzer" },
  "[markdown]": { "editor.wordWrap": "on", "editor.formatOnSave": false },
  "typescript.updateImportsOnFileMove.enabled": "always",
  "javascript.updateImportsOnFileMove.enabled": "always",
  "typescript.preferences.importModuleSpecifier": "relative",
  // --- telemetry / noise ---
  "telemetry.telemetryLevel": "off",
  "update.showReleaseNotes": false,
  "extensions.ignoreRecommendations": false,
  "security.workspace.trust.untrustedFiles": "open"
}
```

### Extensions (a curated, not exhaustive, list)

```sh
# generic
code --install-extension eamodio.gitlens              # or the lighter mhutchie.git-graph
code --install-extension usernamehw.errorlens          # inline diagnostics
code --install-extension editorconfig.editorconfig
code --install-extension esbenp.prettier-vscode
code --install-extension biomejs.biome
code --install-extension streetsidesoftware.code-spell-checker
code --install-extension pkief.material-icon-theme
code --install-extension github.github-vscode-theme
code --install-extension ms-vscode-remote.remote-ssh     # edit on servers
code --install-extension ms-vscode-remote.remote-containers
code --install-extension ms-azuretools.vscode-containers
code --install-extension redhat.vscode-yaml
code --install-extension tamasfe.even-better-toml
code --install-extension mikestead.dotenv
code --install-extension yzhang.markdown-all-in-one
# languages
code --install-extension ms-python.python charliermarsh.ruff ms-python.debugpy ms-toolsai.jupyter
code --install-extension golang.go
code --install-extension rust-lang.rust-analyzer vadimcn.vscode-lldb
code --install-extension llvm-vs-code-extensions.vscode-clangd
code --install-extension sswg.swift-lang
code --install-extension vscjava.vscode-java-pack
code --install-extension dbaeumer.vscode-eslint
code --install-extension bradlc.vscode-tailwindcss
# AI (pick one)
code --install-extension github.copilot github.copilot-chat
```

Record them in your dotfiles with `code --list-extensions > vscode/extensions.txt` — or as `vscode "…"` lines in the Brewfile (Chapter 8), which `brew bundle` installs.

### Keyboard essentials (macOS)

<kbd>⌘</kbd><kbd>P</kbd> file, <kbd>⌘</kbd><kbd>⇧</kbd><kbd>P</kbd> command, <kbd>⌘</kbd><kbd>⇧</kbd><kbd>O</kbd> symbol, <kbd>⌘</kbd><kbd>T</kbd> workspace symbol, <kbd>⌘</kbd><kbd>B</kbd> sidebar, <kbd>⌘</kbd><kbd>J</kbd> panel/terminal, <kbd>⌃</kbd><kbd>`</kbd> terminal, <kbd>⌘</kbd><kbd>\</kbd> split, <kbd>⌘</kbd><kbd>1/2/3</kbd> editor group, <kbd>⌥</kbd><kbd>↑/↓</kbd> move line, <kbd>⌥</kbd><kbd>⇧</kbd><kbd>↑/↓</kbd> copy line, <kbd>⌘</kbd><kbd>D</kbd> add selection to next match, <kbd>⌘</kbd><kbd>⇧</kbd><kbd>L</kbd> select all matches, <kbd>F2</kbd> rename, <kbd>F12</kbd> definition, <kbd>⌥</kbd><kbd>F12</kbd> peek, <kbd>⇧</kbd><kbd>F12</kbd> references, <kbd>⌘</kbd><kbd>.</kbd> quick fix, <kbd>⌘</kbd><kbd>K</kbd> <kbd>⌘</kbd><kbd>S</kbd> keybindings editor. Install the **Vim** or **VSCode Neovim** extension if you're modal.

### VS Code vs VSCodium

VS Code's binary is MIT-licensed source plus Microsoft telemetry, branding and the proprietary Marketplace. **VSCodium** (`brew install --cask vscodium`) is the telemetry-free build using the Open VSX registry; a few extensions (Copilot, Remote SSH, Pylance, C# Dev Kit) are Microsoft-only and don't work there. For students who need Copilot, plain VS Code with `telemetry.telemetryLevel: off` is the pragmatic answer.

## Cursor

**Cursor** (`brew install --cask cursor`) is a fork of VS Code with the AI layer rebuilt as first-class: **Tab** (multi-line predictive edits), **Agent/Composer** (plan and execute multi-file changes, run commands, fix from terminal errors), inline <kbd>⌘</kbd><kbd>K</kbd> edits, codebase indexing, and bundled frontier models (Anthropic, OpenAI, Google, its own). It imports your VS Code settings, keybindings and extensions on first launch; nearly all extensions work.

Pricing (Sept 2026): **Hobby** free (limited), **Pro $20/mo** (~$20 of model credits), **Pro+ $60**, **Ultra $200**, Teams $40/user + base fee. Students have periodically been offered a free year of Pro — check cursor.com/students. The credits model means heavy agent use runs out mid-month; set a spend alert.

Use Cursor if AI assistance is the reason you'd switch editors; stay on VS Code + Copilot if you want a flat price and Microsoft's ecosystem (Remote SSH, Dev Containers, Pylance) without fork lag — Cursor tracks VS Code releases with a delay of weeks. Windsurf (Codeium, now under Cognition) and Google's **Antigravity** (agent-manager IDE) are the other AI-first forks worth a look; Antigravity's multi-agent orchestration is the most different idea in the space.

## Zed

**Zed** (`brew install --cask zed`) is a native Rust editor with a GPU renderer from the creators of Atom: ~180 ms cold start vs 2+ s for Electron editors, ~140 MB idle memory, 8 ms keystroke latency, built-in real-time collaboration (multiplayer editing and voice), Vim mode that's actually good, and an **Agent Panel** that speaks the open **Agent Client Protocol** so you can plug in Claude Code, Gemini CLI, OpenCode or Zed's own hosted models. Language servers install automatically per file type. The editor is free and open source; **Zed Pro** (~$10/mo) is only for hosted AI usage.

Zed is the right choice for large monorepos and for people who find VS Code sluggish, and for pair programming. Its gaps in 2026: a smaller extension ecosystem (no VS Code extension compatibility), a debugger that's newer and less complete than VS Code's, Windows support still maturing. Many people run Zed for editing and VS Code for debugging. Config: `~/.config/zed/settings.json` and `keymap.json` (`⌘,`) — it imports VS Code keybindings and themes.

## JetBrains

IntelliJ IDEA, PyCharm, WebStorm, GoLand, RustRover, CLion, Rider, DataGrip, PhpStorm, RubyMine, Android Studio (Google's fork). Install via **JetBrains Toolbox** (`brew install --cask jetbrains-toolbox`), which manages versions, updates and the `idea`/`pycharm` shell launchers. **Free for students and teachers** (jetbrains.com/academy/student-pack, or via the GitHub Student Developer Pack) — the full Ultimate/Professional editions, renewable yearly while enrolled. WebStorm, RustRover, Rider, CLion and Aqua also have **free non-commercial licences** for everyone since 2024–2025. IntelliJ Community and PyCharm Community are free for any use.

Why JetBrains despite VS Code: language-aware refactoring that's actually safe across a whole project, the best debugger UX, deep framework understanding (Spring, Django, Rails, Next.js), database tools built in (Ultimate), and *everything* working out of the box without assembling extensions. Cost: memory (2–4 GB per IDE), indexing time on first open, and a heavier UI. The **AI Assistant** and **Junie** agent are JetBrains' AI layer (subscription; a free tier exists); Copilot and Claude Code also plug in.

macOS notes: the *IdeaVim* plugin is excellent; enable *Settings → Keymap → macOS* (default) and bind <kbd>⌘</kbd><kbd>⇧</kbd><kbd>A</kbd> (Find Action) into your fingers; increase the heap for big projects (*Help → Change Memory Settings*, 4096 MB); exclude `~/Library/Caches/JetBrains` from Time Machine.

## Neovim

`brew install neovim`. Start from a distribution rather than an empty config:

- **LazyVim** — batteries-included, lazy.nvim plugin manager, LSP/Treesitter/Telescope/Snacks preconfigured, Mason installs language servers. `git clone https://github.com/LazyVim/starter ~/.config/nvim && nvim`.
- **kickstart.nvim** — a single, heavily commented `init.lua` meant to be *read* and owned. Best for learning what each piece does (recommended for students).
- **AstroNvim**, **NvChad**, **LunarVim** — other full distros.

Pair with Ghostty (true colour, Kitty keyboard protocol for extra keybindings, Nerd Font for icons), `ripgrep` and `fd` (Telescope uses them), `lazygit` (Neovim plugin exists), and a clipboard bridge — Neovim on macOS uses `pbcopy`/`pbpaste` automatically for `"+`. AI in Neovim: **codecompanion.nvim**, **avante.nvim**, **copilot.lua**, or just run Claude Code in a split. **Helix** (`brew install helix`) is the modern alternative: Kakoune-style selection-first editing, LSP and Treesitter built in, zero-plugin philosophy — a great choice if you want modal editing without the configuration hobby.

## Xcode (for Apple platforms)

Chapter 7 covers installing it. Settings worth changing: *Text Editing → Display*: line numbers, code folding ribbon, page guide at 120; *Text Editing → Editing*: while editing, automatically trim trailing whitespace including whitespace-only lines; *Themes*: pick a dark one or install one; *Navigation → Command-click*: Jumps to Definition; *Key Bindings*: bind *Refactor → Rename* and *Jump to Definition* if you come from VS Code. Xcode 27's coding agents live in the *Conversation* panel — connect your Claude/ChatGPT account or use Apple's models. Simulators, SwiftUI previews and Instruments are why you tolerate the 15 GB.

## AI coding agents in the terminal

The biggest workflow change of 2025–2026: agents that read your repo, plan, edit files, run tests and iterate, driven from a terminal or an editor panel. They're complementary to whatever editor you use.

| Tool | Vendor / model | Install | Notes |
|---|---|---|---|
| **Claude Code** | Anthropic | `brew install --cask claude-code` or `npm i -g @anthropic-ai/claude-code` | Usage via Claude Pro/Max subscription or API. Skills, hooks, MCP servers, `CLAUDE.md` project memory. Integrates with VS Code/Zed/JetBrains panels. |
| **Codex CLI** | OpenAI | `brew install codex` / `npm i -g @openai/codex` | Included in ChatGPT Plus/Pro; sandboxed execution. |
| **Gemini CLI** | Google | `brew install gemini-cli` | Generous free tier with a Google account. |
| **OpenCode** | open source | `brew install opencode` | Bring any model (local via Ollama, or any API key). |
| **Aider** | open source | `uv tool install aider-chat` | The original; git-native, any model. |
| **Amp** | Sourcegraph | `npm i -g @sourcegraph/amp` | Team-oriented. |
| **GitHub Copilot CLI / coding agent** | GitHub | `gh extension install github/gh-copilot` | Free for students via Copilot Student; the coding agent works on issues → PRs in the cloud. |

Practical habits: give agents a `CLAUDE.md`/`AGENTS.md` at the repo root describing the stack, commands and conventions; run them in a **git worktree** or branch so you can review diffs; keep tests fast so the agent's loop is fast; never paste secrets into a prompt; and for university coursework, **read your integrity policy** — many courses now distinguish "AI for understanding" from "AI for writing the submitted code".

**Model Context Protocol (MCP)** servers give agents tools (GitHub, Postgres, browser, filesystem). Configure them once in `~/.claude.json` / Cursor / Zed settings and every agent can use them.

## Keeping editor configs in sync

- **VS Code / Cursor**: Settings Sync (built in), or commit `settings.json`, `keybindings.json`, `snippets/`, and an `extensions.txt` to dotfiles. Cursor stores its own copies under `~/Library/Application Support/Cursor/User/`.
- **Zed**: `~/.config/zed/` is already a dotfiles-friendly directory; it also has settings sync via a Zed account.
- **JetBrains**: *Settings Sync* (account-based) or export settings to a zip; Toolbox remembers your installed IDEs.
- **Neovim/Helix**: `~/.config/nvim` and `~/.config/helix` — pure text, commit them.
- **Xcode**: themes in `~/Library/Developer/Xcode/UserData/FontAndColorThemes`, key bindings in `…/KeyBindings`, snippets in `…/CodeSnippets` — symlink these into your dotfiles.

## Fonts for code

Same as the terminal (Chapter 9) so glyphs match: **JetBrains Mono**, **Fira Code**, **Monaspace** (GitHub; five variable families that mix), **Cascadia Code**, **Iosevka**, **Geist Mono**, **Commit Mono**, **Berkeley Mono** ($75, the enthusiast favourite), Apple's **SF Mono** (in `/System/Applications/Utilities/Terminal.app/Contents/Resources/Fonts` — copy them to Font Book to use elsewhere). 13 px at 1.6 line height on a Retina display is a comfortable default; 12 px on a 5K 27".
