<!--
number: 05
part: Part II — System & interface
description: Modifier remaps, Caps Lock as Control/Escape, Karabiner-Elements, text navigation shortcuts every Mac user should know, input sources, and coming from Windows/Linux keyboards.
-->
# Keyboard, shortcuts & input

macOS is a keyboard-first operating system wearing a mouse-first costume. Nearly everything has a shortcut, most text fields share the same Emacs-derived navigation keys, and modifier keys are remappable at the system level. Learn this chapter once and every app gets faster.

## The modifier keys and what they mean

| Key | Symbol | Role |
|---|---|---|
| Command | <kbd>⌘</kbd> | App-level actions: copy, paste, save, quit, switch apps. Equivalent to <kbd>Ctrl</kbd> on Windows/Linux for *shortcuts*. |
| Option (Alt) | <kbd>⌥</kbd> | Modifies: word-wise movement, special characters, alternate menu items (hold ⌥ while a menu is open to see them). |
| Control | <kbd>⌃</kbd> | Terminal/Emacs-style text editing (<kbd>⌃</kbd><kbd>A</kbd>, <kbd>⌃</kbd><kbd>E</kbd>, <kbd>⌃</kbd><kbd>K</kbd>), window/Space management, right-click (<kbd>⌃</kbd>-click). |
| Shift | <kbd>⇧</kbd> | Extend selection; reverse direction of many shortcuts. |
| Function / Globe | <kbd>fn</kbd> / <kbd>🌐</kbd> | Function-row behaviour; emoji picker; a fourth modifier in some apps. On Apple silicon it's also used by native window tiling (<kbd>fn</kbd><kbd>⌃</kbd><kbd>←</kbd>). |
| Caps Lock | | Wasted real estate — remap it (below). |

The key insight for switchers: **<kbd>⌘</kbd> is where your thumb is**, so <kbd>⌘</kbd><kbd>C</kbd>/<kbd>V</kbd>/<kbd>Z</kbd>/<kbd>S</kbd>/<kbd>W</kbd>/<kbd>Q</kbd>/<kbd>T</kbd> are one-hand chords, and <kbd>⌃</kbd> is free for the terminal — <kbd>⌃</kbd><kbd>C</kbd> interrupts a process while <kbd>⌘</kbd><kbd>C</kbd> copies, with no conflict. This is why the Mac terminal experience is nicer than Windows'.

## Remap Caps Lock (do this today)

`System Settings → Keyboard → Keyboard Shortcuts… → Modifier Keys`. Choose the keyboard in the dropdown (each keyboard is remapped separately) and set **Caps Lock → ⌃ Control**. Control is the most useful key with the worst factory position; on the home row it makes terminal editing, tmux prefixes, and IDE shortcuts effortless. Vim users often prefer **Caps Lock → ⎋ Escape**, or — with Karabiner — *Escape when tapped, Control when held* (the "dual-role" setup), which is what most heavy keyboard users end up with.

While you're there, on a **Windows-layout keyboard**, swap **⌥ Option ↔ ⌘ Command** so the key next to the space bar is Command like on a Mac keyboard. (Many mechanical keyboards have a hardware Mac/Win switch or DIP setting — use that instead if present.)

## Karabiner-Elements: the remapper

For anything beyond the five modifier keys, **Karabiner-Elements** (free, open source, `brew install --cask karabiner-elements`) is the standard. It runs as a system extension (approve it in `System Settings → General → Login Items & Extensions → Driver Extensions`, and grant *Input Monitoring*). Popular "complex modifications" you can import from its online rules gallery or write yourself:

- **Caps Lock → Escape if alone, Control if held** (the canonical one).
- **Hyper key**: Caps Lock → <kbd>⌘</kbd><kbd>⌥</kbd><kbd>⌃</kbd><kbd>⇧</kbd> when held — a fifth modifier no app uses, so <kbd>Hyper</kbd><kbd>T</kbd> can launch your terminal, <kbd>Hyper</kbd><kbd>H/J/K/L</kbd> can be arrows, etc. Pairs beautifully with Raycast hotkeys or a window manager.
- **Right ⌘ → Change input source**, **Right ⌥ → Fn** for keyboards that lack it.
- **Vim-style navigation layer** (hold a key → H/J/K/L become arrows everywhere).
- **Per-device profiles**: a different map for your external mechanical keyboard vs the built-in one.
- **Swap ⌥ and ⌘ only on external PC keyboards** (Karabiner does this per device, unlike System Settings' per-keyboard dropdown which sometimes forgets).

A minimal `~/.config/karabiner/karabiner.json` "Caps Lock dual role" rule:

```json
{
  "description": "Caps Lock → Escape (tap) / Control (hold)",
  "manipulators": [{
    "type": "basic",
    "from": { "key_code": "caps_lock", "modifiers": { "optional": ["any"] } },
    "to": [{ "key_code": "left_control" }],
    "to_if_alone": [{ "key_code": "escape" }]
  }]
}
```

Karabiner's config is JSON and lives in `~/.config/karabiner/`, so it belongs in your dotfiles (Chapter 10). Alternatives: **Hyperkey** (just the Hyper key, one click), **Keyboard Maestro** (paid; macros, not just remaps — Chapter 21), or a QMK/ZMK/VIA-programmable keyboard where the remap lives in the firmware and follows the keyboard.

## Text editing shortcuts that work everywhere

These work in every native text field — Safari, Mail, Notes, Slack's composer, the address bar, Xcode, even most Electron apps — because they're implemented by the Cocoa text system, not the app.

| Action | Shortcut |
|---|---|
| Move by word | <kbd>⌥</kbd><kbd>←</kbd> / <kbd>⌥</kbd><kbd>→</kbd> |
| Start / end of line | <kbd>⌘</kbd><kbd>←</kbd> / <kbd>⌘</kbd><kbd>→</kbd> (also <kbd>⌃</kbd><kbd>A</kbd> / <kbd>⌃</kbd><kbd>E</kbd>) |
| Start / end of document | <kbd>⌘</kbd><kbd>↑</kbd> / <kbd>⌘</kbd><kbd>↓</kbd> |
| Page up / down | <kbd>fn</kbd><kbd>↑</kbd> / <kbd>fn</kbd><kbd>↓</kbd> (<kbd>⌃</kbd><kbd>V</kbd> down) |
| Select (add <kbd>⇧</kbd> to any movement) | <kbd>⌥</kbd><kbd>⇧</kbd><kbd>→</kbd> selects a word; <kbd>⌘</kbd><kbd>⇧</kbd><kbd>←</kbd> to line start |
| Delete word back / forward | <kbd>⌥</kbd><kbd>⌫</kbd> / <kbd>⌥</kbd><kbd>fn</kbd><kbd>⌫</kbd> (<kbd>⌥</kbd><kbd>D</kbd> in terminals) |
| Delete to line start | <kbd>⌘</kbd><kbd>⌫</kbd> |
| Delete to line end | <kbd>⌃</kbd><kbd>K</kbd> (kills to *macOS* kill buffer; <kbd>⌃</kbd><kbd>Y</kbd> yanks it back) |
| Forward delete | <kbd>fn</kbd><kbd>⌫</kbd> or <kbd>⌃</kbd><kbd>D</kbd> |
| Transpose two characters | <kbd>⌃</kbd><kbd>T</kbd> |
| Move line (Notes/Pages/Xcode) | <kbd>⌃</kbd><kbd>⌘</kbd><kbd>↑</kbd>/<kbd>↓</kbd> |
| Emacs-style char/line movement | <kbd>⌃</kbd><kbd>F</kbd>/<kbd>B</kbd>/<kbd>N</kbd>/<kbd>P</kbd> |
| Paste and match style (plain text) | <kbd>⌘</kbd><kbd>⌥</kbd><kbd>⇧</kbd><kbd>V</kbd> |
| Look up / define selected word | <kbd>⌃</kbd><kbd>⌘</kbd><kbd>D</kbd> (or three-finger tap) |
| Emoji & symbols picker | <kbd>⌃</kbd><kbd>⌘</kbd><kbd>Space</kbd> (or <kbd>🌐</kbd> if you left it enabled) |
| Special characters | Hold <kbd>⌥</kbd>: <kbd>⌥</kbd><kbd>-</kbd> en dash –, <kbd>⌥</kbd><kbd>⇧</kbd><kbd>-</kbd> em dash —, <kbd>⌥</kbd><kbd>;</kbd> …, <kbd>⌥</kbd><kbd>8</kbd> •, <kbd>⌥</kbd><kbd>2</kbd> ™, <kbd>⌥</kbd><kbd>G</kbd> ©, <kbd>⌥</kbd><kbd>E</kbd> then vowel → é, <kbd>⌥</kbd><kbd>U</kbd> then vowel → ü, <kbd>⌥</kbd><kbd>N</kbd> then n → ñ |
| Accents on a held key | Hold <kbd>e</kbd> → picker (disable with `ApplePressAndHoldEnabled false` to get key repeat instead — Chapter 3) |

You can add or override these globally by editing `~/Library/KeyBindings/DefaultKeyBinding.dict` (create it). Windows switchers who want <kbd>Home</kbd>/<kbd>End</kbd> to mean line start/end rather than document start/end:

```
{
  "\UF729"  = moveToBeginningOfLine:;                       /* Home */
  "\UF72B"  = moveToEndOfLine:;                             /* End  */
  "$\UF729" = moveToBeginningOfLineAndModifySelection:;     /* Shift-Home */
  "$\UF72B" = moveToEndOfLineAndModifySelection:;           /* Shift-End  */
  "^\UF729" = moveToBeginningOfDocument:;                   /* Ctrl-Home */
  "^\UF72B" = moveToEndOfDocument:;                         /* Ctrl-End */
}
```

Log out and back in. (Electron apps and terminals have their own keymaps and ignore this file.)

## System shortcuts worth memorising

| Category | Shortcut | Does |
|---|---|---|
| **Apps** | <kbd>⌘</kbd><kbd>Tab</kbd> / <kbd>⌘</kbd><kbd>`</kbd> | Switch apps / windows of the current app |
| | <kbd>⌘</kbd><kbd>Q</kbd> / <kbd>⌘</kbd><kbd>W</kbd> / <kbd>⌘</kbd><kbd>⌥</kbd><kbd>W</kbd> | Quit app / close window or tab / close all windows |
| | <kbd>⌘</kbd><kbd>H</kbd> / <kbd>⌘</kbd><kbd>⌥</kbd><kbd>H</kbd> | Hide app / hide all others |
| | <kbd>⌘</kbd><kbd>M</kbd> | Minimise (prefer ⌘H — minimised windows vanish from ⌘Tab) |
| | <kbd>⌘</kbd><kbd>⌥</kbd><kbd>⎋</kbd> | Force Quit dialog |
| | <kbd>⌘</kbd><kbd>,</kbd> | App settings — universal |
| | <kbd>⌘</kbd><kbd>⇧</kbd><kbd>/</kbd> | Help menu search — finds *any* menu item by name, then arrow to it |
| **Window** | <kbd>fn</kbd><kbd>⌃</kbd><kbd>←</kbd>/<kbd>→</kbd>/<kbd>↑</kbd>/<kbd>↓</kbd> | Native tiling: left/right half, fill, centre (Chapter 6) |
| | <kbd>fn</kbd><kbd>⌃</kbd><kbd>⇧</kbd> + arrows | Quarters |
| | <kbd>fn</kbd><kbd>⌃</kbd><kbd>R</kbd> | Return to previous size |
| | <kbd>⌃</kbd><kbd>⌘</kbd><kbd>F</kbd> / <kbd>fn</kbd><kbd>F</kbd> | Full screen |
| | <kbd>⌘</kbd><kbd>N</kbd> / <kbd>⌘</kbd><kbd>T</kbd> | New window / tab |
| | <kbd>⌘</kbd><kbd>⇧</kbd><kbd>[</kbd> / <kbd>]</kbd>, <kbd>⌃</kbd><kbd>Tab</kbd> | Previous/next tab (works in Safari, Terminal, Finder, VS Code…) |
| **Spaces** | <kbd>⌃</kbd><kbd>←</kbd>/<kbd>→</kbd> | Previous/next Space |
| | <kbd>⌃</kbd><kbd>1</kbd>…<kbd>9</kbd> | Jump to Space N (enable in Keyboard Shortcuts → Mission Control) |
| | <kbd>⌃</kbd><kbd>↑</kbd> / <kbd>⌃</kbd><kbd>↓</kbd> | Mission Control / App Exposé |
| | <kbd>fn</kbd><kbd>H</kbd> or <kbd>F11</kbd> | Show desktop |
| **System** | <kbd>⌘</kbd><kbd>Space</kbd> | Spotlight (Search or Ask on GG) |
| | <kbd>⌘</kbd><kbd>⇧</kbd><kbd>Space</kbd> | Visual Intelligence (GG) |
| | <kbd>⌃</kbd><kbd>⌘</kbd><kbd>Q</kbd> | Lock screen |
| | <kbd>⌥</kbd><kbd>⌘</kbd><kbd>⏏</kbd> / <kbd>⌃</kbd><kbd>⇧</kbd><kbd>Power</kbd> | Sleep / display sleep |
| | <kbd>⌃</kbd><kbd>⌘</kbd><kbd>Power</kbd> | Force restart (hold) |
| | <kbd>⌥</kbd>-click menu bar items (Wi‑Fi, Sound, Bluetooth, Battery) | Debug/detail views: BSSID, channel, sample rate, condition |
| | <kbd>⌥</kbd><kbd>⇧</kbd> + volume/brightness keys | Quarter-step adjustments |
| **Screenshots** | <kbd>⌘</kbd><kbd>⇧</kbd><kbd>3</kbd> / <kbd>4</kbd> / <kbd>5</kbd> | Full screen / selection / the toolbar (record, timer, options). Add <kbd>⌃</kbd> to copy to clipboard instead of saving. In ⌘⇧4, press <kbd>Space</kbd> to capture a window, hold <kbd>⌥</kbd> to omit the shadow. |
| | <kbd>⌘</kbd><kbd>⇧</kbd><kbd>6</kbd> | Touch Bar (old) / Visual Intelligence region (GG) |
| **Finder / Save dialogs** | <kbd>⌘</kbd><kbd>⇧</kbd><kbd>G</kbd> or `/` or `~` | Go to path — works inside Open/Save dialogs too; drag a folder onto the dialog to jump there |
| | <kbd>⌘</kbd><kbd>D</kbd> in dialogs | "Don't Save" / Desktop |
| | <kbd>⌘</kbd><kbd>⌫</kbd> in dialogs | "Delete"/"Don't Save" (the destructive default) |
| | <kbd>⌘</kbd><kbd>.</kbd> / <kbd>⎋</kbd> | Cancel |

## Keyboard navigation of the UI

- `System Settings → Keyboard → Keyboard navigation`: **on**. Then <kbd>Tab</kbd> moves through *all* controls (buttons too), <kbd>Space</kbd> presses, <kbd>Return</kbd> is the default button, <kbd>⎋</kbd> cancels.
- <kbd>⌃</kbd><kbd>F2</kbd> (or <kbd>fn</kbd><kbd>⌃</kbd><kbd>F2</kbd>) focuses the **menu bar**; type to jump to a menu; arrows navigate. <kbd>⌃</kbd><kbd>F3</kbd> focuses the Dock. <kbd>⌃</kbd><kbd>F8</kbd> focuses menu bar extras (status items).
- <kbd>⌘</kbd><kbd>⇧</kbd><kbd>/</kbd> opens Help → Search: type any menu command; it highlights where it lives and pressing <kbd>Return</kbd> runs it. This is the fastest way to run an obscure command in any app.
- In dialogs, the first letter of a button often activates it when Full Keyboard Access is on.

## Custom app shortcuts

`System Settings → Keyboard → Keyboard Shortcuts… → App Shortcuts → +`. Pick an app (or *All Applications*), type the **exact menu item title** (including `…` typed as <kbd>⌥</kbd><kbd>;</kbd>), assign a key. Examples people set:

- *All Applications*: `Merge All Windows` → <kbd>⌘</kbd><kbd>⇧</kbd><kbd>M</kbd>; `Export as PDF…` → <kbd>⌘</kbd><kbd>⇧</kbd><kbd>E</kbd>; `Move Window to Left Side of Screen` → something ergonomic.
- *Safari*: `Show Web Inspector` if the default clashes; `Pin Tab`.
- *Finder*: `New Terminal at Folder` → <kbd>⌘</kbd><kbd>⌥</kbd><kbd>T</kbd>.
- *Mail*: `Archive` → <kbd>⌘</kbd><kbd>E</kbd>.

Menu items in the *Services* submenu are enabled here too (`Keyboard Shortcuts → Services`) — turn off the dozens you never use; they clutter every right-click menu.

## Function keys and the Touch Bar's legacy

- **Use F1, F2, etc. keys as standard function keys**: `Keyboard → Keyboard Shortcuts… → Function Keys`. Developers using IDE debuggers (<kbd>F5</kbd>–<kbd>F11</kbd>) usually turn this **on** and hit <kbd>fn</kbd> for brightness/volume. Alternatively keep media keys and let the IDE bindings use <kbd>fn</kbd>.
- Per-app exceptions: `Keyboard → Keyboard Shortcuts… → Function Keys` has none, but Karabiner can switch behaviour per app (e.g. standard F-keys only in Xcode/IntelliJ/VS Code).

## Input sources and typing in other languages

- `Keyboard → Text Input → Edit… → +` to add layouts/languages. **Show Input menu in menu bar**. Switch with <kbd>⌃</kbd><kbd>Space</kbd> (previous) / <kbd>⌃</kbd><kbd>⌥</kbd><kbd>Space</kbd> (next) — **and make sure this doesn't collide with <kbd>⌘</kbd><kbd>Space</kbd> for Spotlight** (check the *Input Sources* section of Keyboard Shortcuts).
- **Automatically switch to a document's input source**: on if you write in two scripts.
- **Unicode Hex Input** layout: hold <kbd>⌥</kbd> and type a code point (`2192` → →). Handy for maths symbols.
- **US International – PC** or **ABC – Extended** give dead keys for accents on a US keyboard; the standard **ABC** layout has them via <kbd>⌥</kbd> chords as shown above.
- **Dictation** (<kbd>🌐</kbd> twice by default, or set your own): on-device, offline, punctuation by voice ("comma", "new line"), works in any text field. Golden Gate's improved dictation (M3+, 12 GB+) is noticeably more accurate.

## Coming from Windows or Linux: the translation table

| You press on Windows/Linux | On Mac | Notes |
|---|---|---|
| <kbd>Ctrl</kbd><kbd>C</kbd>/<kbd>V</kbd>/<kbd>X</kbd>/<kbd>Z</kbd>/<kbd>S</kbd>/<kbd>A</kbd>/<kbd>F</kbd> | <kbd>⌘</kbd> + same letter | Universal |
| <kbd>Alt</kbd><kbd>Tab</kbd> | <kbd>⌘</kbd><kbd>Tab</kbd> (apps) + <kbd>⌘</kbd><kbd>`</kbd> (windows) | Or install AltTab |
| <kbd>Alt</kbd><kbd>F4</kbd> | <kbd>⌘</kbd><kbd>Q</kbd> (quit) / <kbd>⌘</kbd><kbd>W</kbd> (close window) | Closing the last window does *not* quit a Mac app |
| <kbd>Win</kbd> / <kbd>Super</kbd> | <kbd>⌘</kbd><kbd>Space</kbd> | Launch anything |
| <kbd>Win</kbd><kbd>D</kbd> | <kbd>fn</kbd><kbd>H</kbd> / <kbd>F11</kbd> | Show desktop |
| <kbd>Win</kbd><kbd>L</kbd> | <kbd>⌃</kbd><kbd>⌘</kbd><kbd>Q</kbd> | Lock |
| <kbd>Win</kbd><kbd>←</kbd>/<kbd>→</kbd> | <kbd>fn</kbd><kbd>⌃</kbd><kbd>←</kbd>/<kbd>→</kbd> | Snap halves (or Rectangle/Raycast) |
| <kbd>Win</kbd><kbd>Shift</kbd><kbd>S</kbd> | <kbd>⌘</kbd><kbd>⇧</kbd><kbd>4</kbd> (+<kbd>⌃</kbd> to clipboard) | Screenshot region |
| <kbd>PrtSc</kbd> | <kbd>⌘</kbd><kbd>⇧</kbd><kbd>3</kbd> | |
| <kbd>Home</kbd>/<kbd>End</kbd> | <kbd>⌘</kbd><kbd>←</kbd>/<kbd>→</kbd> | Line start/end (or remap Home/End as above) |
| <kbd>Ctrl</kbd><kbd>Home</kbd>/<kbd>End</kbd> | <kbd>⌘</kbd><kbd>↑</kbd>/<kbd>↓</kbd> | Document start/end |
| <kbd>Ctrl</kbd><kbd>←</kbd>/<kbd>→</kbd> | <kbd>⌥</kbd><kbd>←</kbd>/<kbd>→</kbd> | Word-wise |
| <kbd>Ctrl</kbd><kbd>Backspace</kbd> | <kbd>⌥</kbd><kbd>⌫</kbd> | Delete word |
| <kbd>Delete</kbd> | <kbd>fn</kbd><kbd>⌫</kbd> | Forward delete; <kbd>⌫</kbd> alone is Backspace |
| <kbd>F2</kbd> rename | <kbd>Return</kbd> on a Finder item | <kbd>Return</kbd> renames; <kbd>⌘</kbd><kbd>O</kbd> opens |
| <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>Esc</kbd> | <kbd>⌘</kbd><kbd>⌥</kbd><kbd>⎋</kbd> / Activity Monitor | Force Quit / task manager |
| Right-click | <kbd>⌃</kbd>-click, two-finger tap, or right side of Magic Mouse | |
| Middle-click | Three-finger tap (with MiddleClick app) or <kbd>⌘</kbd>-click for links | |
| <kbd>Ctrl</kbd><kbd>Alt</kbd><kbd>T</kbd> (terminal) | none by default | Bind in Ghostty/iTerm2 (global hotkey window) or Raycast |
| <kbd>Alt</kbd> + accelerator letters in menus | none | Use <kbd>⌘</kbd><kbd>⇧</kbd><kbd>/</kbd> and type the command name |

Two things trip up switchers for a week: (1) **<kbd>⌘</kbd><kbd>W</kbd> closes the window but the app stays open** with its menu bar — that's normal, and it relaunches instantly; quit with <kbd>⌘</kbd><kbd>Q</kbd> when you mean it. (2) **Menus live in the menu bar at the top of the screen**, not in each window; the *active app's* menus are shown. Both stop being weird by Friday.

## Hardware keyboard notes

- **Keyboard layout wizard** appears the first time you plug in an unknown keyboard (ISO vs ANSI detection). If <kbd>§</kbd> and <kbd>&#96;</kbd> (backtick) are swapped on a European keyboard, rerun it: `Keyboard → Change Keyboard Type…` (or Karabiner's *Devices* tab has a per-device §/backtick swap).
- **Mechanical keyboards with QMK/VIA**: set the Mac layout in firmware (swap GUI/Alt, map F-keys to media as you like). Then nothing in macOS needs remapping and the board works identically on your Linux box.
- **Bluetooth lag**: pair via USB-C once (Apple keyboards), keep the dongle in a USB-A port rather than a hub for Logitech Bolt receivers, and avoid 2.4 GHz Wi‑Fi congestion — Apple's N1 chip (M5 Pro/Max, M6) with Bluetooth 6 is markedly better here.
- **Two keyboards, two layouts**: `Keyboard → Text Input → Edit…` is global, but Karabiner can force a per-device input source.
