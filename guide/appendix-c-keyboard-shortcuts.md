<!--
number: C
part: Part VI — Reference
description: Every keyboard shortcut worth knowing on macOS 26/27, grouped by context — system, windows and Spaces, Finder, text editing (including the Emacs bindings that work in every Cocoa text field), screenshots, Spotlight, Safari, Terminal/Ghostty, VS Code, and the modifier symbols decoded.
-->
# Appendix C — Keyboard shortcuts

Modifier symbols, as printed on Apple keyboards and used throughout this guide: **⌘** Command · **⌥** Option (Alt) · **⌃** Control · **⇧** Shift · **fn** / 🌐 Globe · **⇪** Caps Lock · **⎋** Escape · **⌫** Delete (Backspace) · **⌦** Forward Delete (`fn ⌫`) · **↩** Return · **⇥** Tab · **⇞⇟** Page Up/Down (`fn ↑↓`) · **↖↘** Home/End (`fn ←→`).

Everything below is a default unless marked *(set up in ch. N)*. Change any system shortcut in **System Settings → Keyboard → Keyboard Shortcuts**; add app-menu shortcuts under **App Shortcuts** (type the exact menu item name).

## System

| Shortcut | Action |
|---|---|
| `⌘Space` | Spotlight (or Raycast/Alfred if you swapped them — [ch. 4](04-finder-dock-spotlight.html)) |
| `⌘⇧Space` | Visual Intelligence (macOS 27) / Siri type-to |
| `⌘Tab`, `⌘⇧Tab` | Next / previous app (hold ⌘, tap Tab, `Q` to quit the highlighted app, `H` to hide, `↑`/`↓` to see its windows) |
| `` ⌘` ``, `` ⌘⇧` `` | Next / previous window of the current app |
| `⌘Q` / `⌘W` / `⌘⇧W` | Quit / close window or tab / close all windows |
| `⌘H` / `⌘⌥H` | Hide app / hide all others |
| `⌘M` / `⌘⌥M` | Minimize / minimize all |
| `⌘N` / `⌘T` / `⌘O` / `⌘S` / `⌘P` | New window / new tab / open / save / print |
| `⌘,` | App settings |
| `⌘?` (`⌘⇧/`) | Help menu with search — finds any menu item by name and points at it |
| `⌥⌘⎋` | Force Quit dialog |
| `⌃⌘Q` | Lock screen |
| `⌥⌘⏏` / `⌃⇧⏻` | Sleep / put displays to sleep (no eject key: `⌃⇧` + power) |
| `⌃⌘⏻` | Force restart (hold) |
| `⌘⌥⌃⏻` | Quit all apps and shut down (hold) |
| `fn` / 🌐 | Tap: emoji picker or Dictation or nothing (configurable). Hold + letter: `fn E` emoji · `fn Q` Quick Note · `fn C` Control Center · `fn N` Notification Center · `fn D` Dictation · `fn F` fullscreen · `fn A` Dock · `fn M` menu bar · `fn H` desktop |
| `⌃⌘Space` | Character viewer (emoji & symbols) |
| `⌘⌥D` | Toggle Dock hiding |
| `⌃F2` / `⌃F3` / `⌃F8` | Focus menu bar / Dock / status menus (then arrows + Return) |
| `⌘⌥⌃T` | *(App Shortcut you can add)* — e.g. new Ghostty window |
| `⌥` + volume/brightness key | Open Sound / Displays settings |
| `⇧⌥` + volume/brightness key | Quarter-step adjustments |
| `⌥` + click Wi-Fi/Bluetooth/Sound menu icon | Diagnostic details |
| `⌘⌥⌃8` | Invert colors *(enable in Accessibility → Keyboard → Shortcut)* |
| `⌥⌘F5` | Accessibility shortcuts panel |
| `⌃⌥⌘⇧` (hyper) + key | Your Hammerspoon/Karabiner layer *(set up in [ch. 5](05-keyboard-and-input.html), [ch. 21](21-automation-and-scripting.html))* |

## Windows, Spaces, tiling

| Shortcut | Action |
|---|---|
| `⌃↑` / `⌃↓` | Mission Control / App Exposé (current app's windows) |
| `⌃←` / `⌃→` | Previous / next Space |
| `⌃1`…`⌃9` | Jump to Space N *(enable in Keyboard Shortcuts → Mission Control)* |
| `F11` (or `fn F11`) | Show desktop |
| `⌃⌘F` / `fn F` | Full screen toggle |
| Green button hover / `fn ⌃F` | Tiling menu / fill |
| `fn ⌃←` / `fn ⌃→` | Tile left / right half (macOS 15+ built-in) |
| `fn ⌃↑` / `fn ⌃↓` | Tile top / bottom |
| `fn ⌃⇧←` / `fn ⌃⇧→` | Arrange left & right (two windows) |
| `fn ⌃R` | Return to previous size |
| `fn ⌃C` | Center |
| `⌥` + green button | Zoom (maximize without full screen) |
| `⌘` + drag | Move a background window without focusing it |
| `⌃⌘` + drag anywhere in a window | Move window *(with `NSWindowShouldDragOnGesture` from the defaults script)* |
| Double-click title bar | Zoom or minimize (Desktop & Dock setting) |
| `⌥⌘W` on a window edge | *(Rectangle)* — defaults are `⌃⌥←` `⌃⌥→` halves, `⌃⌥↩` maximize, `⌃⌥C` center, `⌃⌥⌘←/→` next display |
| `⌥H/J/K/L` | *(AeroSpace default)* focus left/down/up/right; `⌥⇧` + same to move; `⌥1–9` workspaces; `⌥/` toggle tiles/accordion — [ch. 6](06-window-management.html) |

## Finder

| Shortcut | Action |
|---|---|
| `⌘N` / `⌘T` / `⌘⇧N` | New window / new tab / new folder |
| `⌘↑` / `⌘↓` / `⌘O` | Enclosing folder / open selection |
| `⌘[` / `⌘]` | Back / forward |
| `⌘⇧G` | Go to Folder — type or paste a path; `~`, `/`, and Tab-completion work |
| `⌘⇧.` | Toggle hidden files |
| `⌘⇧H` / `⌘⇧D` / `⌘⇧O` / `⌘⌥L` / `⌘⇧A` / `⌘⇧U` / `⌘⇧C` / `⌘⇧K` / `⌘⇧I` / `⌘⇧R` | Home / Desktop / Documents / Downloads / Applications / Utilities / Computer / Network / iCloud Drive / AirDrop |
| `⌘1` / `⌘2` / `⌘3` / `⌘4` | Icon / List / Column / Gallery view |
| `⌘J` | View options for this folder (set as default here) |
| `⌘⌥P` / `⌘/` / `⌘⌥S` / `⌘⌥T` | Toggle path bar / status bar / sidebar / toolbar |
| `Space` / `⌥Space` | Quick Look / full-screen Quick Look |
| `⌘Y` | Quick Look (alternate) |
| `⌘I` / `⌘⌥I` | Get Info / Inspector (updates with selection) |
| `⌘D` | Duplicate |
| `⌘L` | Make alias |
| `⌘⌫` / `⌘⇧⌫` / `⌘⌥⇧⌫` | Move to Trash / empty Trash / empty without confirmation |
| `⌘⌥V` | Move (after `⌘C`) — cut-and-paste files |
| `⌘⌥C` | Copy pathname of selection |
| `↩` | Rename selection |
| `⌘E` | Eject |
| `⌘F` | Search (current folder first — set in Finder settings) |
| `⌘⌃N` (with selection) | New Folder with Selection |
| `⌘⇧P` | Preview pane |
| `⌥` + double-click | Open in new window and close current |
| `⌘` + double-click folder | Open in new tab |
| `⌥⌘` + drag | Make alias; `⌥` + drag = copy; `⌘` + drag = move (across volumes) |
| Drag file onto the title-bar icon of an Open dialog | Jump the dialog to that file's folder |
| Drag any file into a Terminal window | Inserts its quoted path |

## Text editing (works in every Cocoa text field)

These come from the Cocoa text system (Emacs bindings via `~/Library/KeyBindings/DefaultKeyBinding.dict`, [ch. 5](05-keyboard-and-input.html)). They work in Safari's address bar, Mail, Notes, Xcode, Slack, VS Code (mostly), and the Terminal.

| Shortcut | Action |
|---|---|
| `⌘←` / `⌘→` | Start / end of line |
| `⌥←` / `⌥→` | Word left / right |
| `⌘↑` / `⌘↓` | Start / end of document |
| `⌥↑` / `⌥↓` | Start of paragraph / end of paragraph |
| `⌥⌫` / `⌥⌦` | Delete word backward / forward |
| `⌘⌫` | Delete to start of line |
| `⌃A` / `⌃E` | Start / end of line (Emacs) |
| `⌃F` / `⌃B` / `⌃N` / `⌃P` | Forward / back / next line / previous line |
| `⌃D` / `⌃H` | Forward delete / backspace |
| `⌃K` | Kill to end of line (into the *Emacs* kill buffer, separate from the clipboard); `⌃Y` yank |
| `⌃O` | Insert newline after cursor |
| `⌃T` | Transpose characters |
| `⌃L` | Center cursor line in view |
| `⇧` + any motion | Extend selection |
| `⌘⇧V` | Paste and match style |
| `⌘⌥⇧V` | Paste plain text (some apps) |
| `⌘Z` / `⌘⇧Z` | Undo / redo |
| `⌘;` | Next misspelling; `⌘:` spelling panel |
| `⌃⌘D` | Look up word under cursor (dictionary/Wikipedia popover); also force-click |
| `fn fn` (or `fn D`) | Dictation |
| `⌥E` + vowel, `⌥N` + n, `⌥U` + vowel, `⌥\`` + vowel, `⌥C`, `⌥I` + letter | Accents: é ñ ü è ç î — or hold the key (unless `ApplePressAndHoldEnabled` is off) |
| `⌥8` / `⌥-` / `⌥⇧-` / `⌥;` / `⌥[` `⌥⇧[` / `⌥]` `⌥⇧]` / `⌥⇧K` / `⌥G` / `⌥R` / `⌥2` / `⌥⇧8` / `⌥=` / `⌥<` `⌥>` / `⌥/` | • – — … " " ' '  ©® ™ ° ≠ ≤ ≥ ÷ |

## Screenshots and recording

| Shortcut | Action |
|---|---|
| `⌘⇧3` | Full screen → file |
| `⌘⇧4` | Selection → file. Then: `Space` window mode (click a window; hold `⌥` for no shadow); hold `Space` while dragging to move selection; `⇧` locks an edge; `⌥` resizes from center; `⎋` cancels |
| `⌘⇧5` | Screenshot/recording toolbar: options for timer, save location, mic, show cursor |
| `⌘⇧6` | Touch Bar (legacy) |
| `⌃` + any of the above | To clipboard instead of file |
| `⌘⇧4` then `Space` then `⌘` + click menu | Capture a menu with its title |
| Click the floating thumbnail | Markup; drag it into any app |
| `⌘⇧C` in Shottr *(if installed)* | Capture area with pixel measurement/OCR — [ch. 19](19-daily-driver-apps.html) |

## Spotlight (macOS 26/27)

| Shortcut | Action |
|---|---|
| `⌘Space` | Open. Type to search; results are mixed |
| `⌘1` / `⌘2` / `⌘3` / `⌘4` | Applications / Files / Actions / Clipboard views |
| `⌘↩` | Reveal in Finder |
| `⌘I` | Info about result |
| `⌘C` | Copy result (file or answer) |
| `⌘L` | Jump to the definition/first result |
| `⇥` | Preview pane / expand |
| `⌘B` | Search the web instead |
| `⌥⌘Space` | Finder search window |
| Type a quick key, e.g. `sm` → Send Message | Quick keys for actions (assign in Spotlight → Actions) |
| `=` or just type math | Calculator; unit/currency conversion (`100 usd in eur`) |

Raycast defaults *(if installed)*: `⌥Space` (or swapped with Spotlight) open · `⌘K` actions on a result · `⌥⌘C` clipboard history · `⌥⌘N` notes · `⌃⌥←/→` window halves · `⌘,` settings.

## Safari

| Shortcut | Action |
|---|---|
| `⌘L` | Address bar |
| `⌘T` / `⌘W` / `⌘⇧T` | New / close / reopen closed tab |
| `⌃Tab` / `⌃⇧Tab` or `⌘⇧]` / `⌘⇧[` | Next / previous tab |
| `⌘1`–`⌘9` | Jump to tab N (or bookmarks if that setting is on) |
| `⌘⇧N` | New private window |
| `⌘⇧\` | Tab overview |
| `⌘⇧L` | Sidebar (Tab Groups, bookmarks, reading list) |
| `⌘⇧R` | Reader view |
| `⌘⌥R` | Reload ignoring cache |
| `⌘⌥I` | Web Inspector *(Develop menu on — defaults script)* |
| `⌘⌥C` | Console |
| `⌘⌥U` | View source |
| `⌘⌥E` | Empty caches |
| `⌘⇧D` | Add bookmark |
| `⌘D` | Add to Reading List (varies) |
| `⌘⇧F` | Full screen |
| `⌘F` / `⌘G` | Find / find next |
| `Space` / `⇧Space` | Page down / up |
| `⌘↑` / `⌘↓` | Top / bottom |
| `⌘+` / `⌘-` / `⌘0` | Zoom |
| `⌘⌥F` | Search Google from anywhere |
| `⌘⇧I` | Email link |
| `⌥` + click link | Download |
| `⌘` + click | Open in background tab |
| `⌘⇧` + click | Open in foreground tab |

Chrome/Firefox share most; Firefox uses `⌘⌥I` for DevTools too, Chrome `⌘⌥J` for console.

## Terminal.app / Ghostty / iTerm2

| Shortcut | Action |
|---|---|
| `⌘T` / `⌘W` / `⌘N` | Tab / close / window |
| `⌘D` / `⌘⇧D` | Split right / down (Ghostty: `⌘D` `⌘⇧D`; iTerm2: `⌘D` `⌘⇧D`; Terminal.app: `⌘D` only splits the same session) |
| `⌘⌥←→↑↓` | Focus split (Ghostty) |
| `⌘K` | Clear scrollback |
| `⌘F` | Search scrollback |
| `⌘+` / `⌘-` / `⌘0` | Font size |
| `⌘1`–`⌘9` | Tab N |
| `⌘⇧↩` | Zoom split (Ghostty) |
| `⌘⇧,` | Reload config (Ghostty) |
| `⌘⌃F` | Fullscreen |
| `⌘⇧Q` (Ghostty) | Toggle quick terminal *(set up in [ch. 9](09-terminal-and-shell.html))* |
| `⌥←` / `⌥→` | Word jump *(Option as Meta / `macos-option-as-alt = true`)* |
| `⌥` + click | Move cursor in the shell line |
| `⌘` + double-click URL / `⌘` + click | Open link |
| `⌘⇧P` | Command palette (Ghostty 1.2+) |
| Shell (zsh): `⌃R` | fzf history search *(ch. 9)* |
| `⌃T` / `⌥C` | fzf file / directory picker |
| `⌃A` `⌃E` `⌃U` `⌃K` `⌃W` `⌃Y` `⌃L` `⌃C` `⌃D` `⌃Z` | Line start/end · kill to start/end · kill word · yank · clear · interrupt · EOF · suspend (`fg` to resume) |
| `⌃X ⌃E` | Edit the current command line in `$EDITOR` |
| `⌃_` | Undo (zsh line editor) |
| `⎋ .` (or `⌥.`) | Insert last argument of previous command |
| `!!`, `!$`, `!*`, `^old^new` | History expansion: last command / its last arg / all args / substitute |
| tmux (prefix `⌃B` or `⌃A`): `c` `n` `p` `%` `"` `o` `z` `d` `[` `s` | new window · next · prev · split v · split h · next pane · zoom · detach · copy mode · session list |

## VS Code (macOS keymap)

| Shortcut | Action |
|---|---|
| `⌘⇧P` / `F1` | Command Palette |
| `⌘P` | Quick Open file; type `:` for line, `@` for symbol, `>` for command, `#` for workspace symbol |
| `⌘⇧O` | Go to symbol |
| `⌘T` | Go to symbol in workspace |
| `⌘B` / `⌘J` / `⌘⇧E` / `⌘⇧F` / `⌘⇧G` / `⌘⇧D` / `⌘⇧X` | Sidebar / panel / Explorer / Search / Source Control / Debug / Extensions |
| `` ⌃` `` / `` ⌃⇧` `` | Terminal / new terminal |
| `⌘\` / `⌘1` `⌘2` | Split editor / focus group |
| `⌘K ⌘W` / `⌘W` | Close all / close |
| `⌘⇧T` | Reopen closed editor |
| `⌃-` / `⌃⇧-` | Navigate back / forward |
| `F12` / `⌥F12` / `⇧F12` / `⌘F12` | Definition / peek / references / implementation |
| `F2` | Rename symbol |
| `⌘.` | Quick fix / code actions |
| `⌘⇧K` / `⌥↑↓` / `⇧⌥↑↓` | Delete line / move line / copy line |
| `⌘D` / `⌘⇧L` / `⌘U` | Add selection to next match / select all matches / undo last cursor |
| `⌥` + click / `⌥⌘↑↓` | Multiple cursors |
| `⌘⇧\` | Jump to matching bracket |
| `⌘K ⌘F` / `⇧⌥F` | Format selection / document |
| `⌘/` / `⇧⌥A` | Toggle line / block comment |
| `⌘K ⌘0` / `⌘K ⌘J` | Fold all / unfold all |
| `⌘K Z` | Zen mode |
| `⌘⇧V` / `⌘K V` | Markdown preview / to the side |
| `⌘K ⌘S` | Keyboard shortcuts editor |
| `⌘K ⌘T` | Color theme |
| `⌘I` / `⌘⇧I` / `⌃⌘I` | Inline chat / agent panel / chat *(Copilot/Cursor vary — [ch. 12](12-editors-and-ides.html))* |
| `F5` / `F9` / `F10` / `F11` | Debug start / breakpoint / step over / step into |
| `⌘⇧M` | Problems panel |
| `⌘K M` | Change language mode |

Cursor: same base, plus `⌘K` inline edit, `⌘L` chat, `⌘I` composer/agent. Zed: `⌘⇧P` palette, `⌘T` project symbols, `⌘P` files, `⌘⇧R` inline assist, `⌘?` AI panel. JetBrains: `⇧⇧` search everywhere, `⌘O` class, `⌘⇧O` file, `⌥↩` intention, `⌘⌥L` reformat, `⇧F6` rename, `⌘E` recent.

## Startup (Apple silicon)

| Do | Result |
|---|---|
| Press and hold power until "Loading startup options" | Recovery / startup disk chooser |
| From options: select disk → hold `⇧` → Continue in Safe Mode | Safe Mode |
| From options: `⌘D` | Apple Diagnostics |
| Options → Continue → Utilities → Terminal | Recovery Terminal (`resetpassword`, `diskutil`) |
| `⌘R`, `⌘⌥R`, `⌘⌥P R`, `⇧⌃⌥`+power | **Do nothing on Apple silicon** (Intel-era key combos) — see [ch. 22](22-troubleshooting.html) |

## Making your own

- **System Settings → Keyboard → Keyboard Shortcuts → App Shortcuts → +**: pick an app (or All Applications), type the *exact* menu item text (including `…` via `⌥;`), press keys. This is how you give any menu command a shortcut without a third-party tool.
- **Shortcuts app** → any Shortcut → ⓘ → Add Keyboard Shortcut: global hotkeys for automations ([ch. 21](21-automation-and-scripting.html)).
- **Karabiner-Elements**: Caps Lock → Escape when tapped / Hyper when held; swap `⌥`/`⌘` for PC keyboards; per-device rules ([ch. 5](05-keyboard-and-input.html)).
- **Hammerspoon**: `hs.hotkey.bind(hyper, "t", …)` for anything Lua can do ([ch. 21](21-automation-and-scripting.html)).
- **Conflict check**: `⌘Space` (Spotlight vs Raycast vs input source switch), `⌃Space` (input source vs editor completion), `⌘⇧Space` (Visual Intelligence vs Raycast defaults), `⌃←→` (Spaces vs terminal word jump — use `⌥←→` in the terminal instead), `F11` (Show Desktop vs debugger step) — disable the system side in Keyboard Shortcuts if an app needs the key.
