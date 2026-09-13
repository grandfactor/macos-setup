<!--
number: 06
part: Part II — System & interface
description: Spaces, Mission Control, native tiling, Stage Manager, and the third-party window managers (Rectangle, Raycast, AeroSpace, yabai) — which one fits how you work, and how to set up multiple displays.
-->
# Window management, Spaces & displays

macOS's window model confuses newcomers: there is no "maximise" in the Windows sense, apps can have many windows across many desktops, and full-screen is its own thing. Once you understand the three layers — **Spaces**, **tiling**, and **switching** — it's very fast. This chapter sets up the built-ins, then picks a third-party manager if you want more.

## Mental model

- A **Space** (virtual desktop) is a full-screen canvas. Each display has its own set of Spaces (`Displays have separate Spaces`: on). Full-screen apps become their own Space.
- **Windows** float in a Space. macOS remembers window positions per app and restores them on relaunch (Golden Gate also restores them across display connect/disconnect much better than before).
- **The green button** (or double-clicking the title bar) *zooms/fills* the window to the content's natural size or the full screen; **holding <kbd>⌥</kbd>** while clicking it fills the screen without entering full-screen mode; **hovering** it shows the tiling menu (Fill, Center, Left/Right/Top/Bottom halves, quarters, *Move to display*, *Enter Full Screen*).
- **Hiding** (<kbd>⌘</kbd><kbd>H</kbd>) an app removes its windows but keeps it in <kbd>⌘</kbd><kbd>Tab</kbd>; **minimising** (<kbd>⌘</kbd><kbd>M</kbd>) sends the window to the Dock and *out* of <kbd>⌘</kbd><kbd>Tab</kbd> — which is why most Mac users never minimise.

## Native window tiling (Sequoia+)

macOS finally does Windows-style snapping:

- **Drag a window to a screen edge** → it tiles to that half (top edge = fill; corners = quarters). A ghost outline previews the result. Hold <kbd>⌥</kbd> while dragging to get the outline immediately.
- **Keyboard**: <kbd>fn</kbd><kbd>⌃</kbd><kbd>←</kbd>/<kbd>→</kbd>/<kbd>↑</kbd>/<kbd>↓</kbd> = left half / right half / top half / bottom half; <kbd>fn</kbd><kbd>⌃</kbd><kbd>F</kbd> = fill; <kbd>fn</kbd><kbd>⌃</kbd><kbd>C</kbd> = centre; <kbd>fn</kbd><kbd>⌃</kbd><kbd>⇧</kbd> + arrows = quarters; <kbd>fn</kbd><kbd>⌃</kbd><kbd>R</kbd> = revert. On external keyboards without <kbd>fn</kbd>, use <kbd>🌐</kbd> or remap in `Keyboard Shortcuts → Windows`, where you can also **rebind these** to <kbd>⌃</kbd><kbd>⌥</kbd> + arrows (the Rectangle convention).
- **Menu**: `Window → Move & Resize` lists every arrangement, including *Left & Right*, *Top & Bottom*, *Quarters* which arrange **two or four windows at once**.
- Settings: `Desktop & Dock → Windows`: **Tiled windows have margins: off** (tight), *Drag windows to screen edges to tile*: on, *Drag windows to menu bar to fill screen*: on, *Hold ⌥ key while dragging windows to tile*: on.

For a lot of people — two windows side-by-side, one maximised, occasionally thirds — this is enough, and it needs no Accessibility permission. Its limits: no thirds/two-thirds by keyboard, no "move to next display" hotkey, no per-app rules, and the snapping zones are a bit coarse. That's where the third-party tools come in.

## Spaces and Mission Control

Set up once:

1. `System Settings → Desktop & Dock → Mission Control`: **Automatically rearrange Spaces based on most recent use: OFF**. This is the single most important setting — with it on, your Spaces shuffle constantly and <kbd>⌃</kbd><kbd>3</kbd> stops meaning anything.
2. `Keyboard → Keyboard Shortcuts… → Mission Control`: enable **Switch to Desktop 1…9** (<kbd>⌃</kbd><kbd>1</kbd>…<kbd>⌃</kbd><kbd>9</kbd>). They appear only after the Spaces exist — create them first.
3. Open Mission Control (<kbd>⌃</kbd><kbd>↑</kbd>, three/four-finger swipe up, or <kbd>F3</kbd>), hover top-right → **+** to add Spaces. Create 4–6 and give them roles — e.g. **1 Communication** (mail, Slack), **2 Browser/research**, **3 Code** (editor + terminal), **4 Second project / school**, **5 Media/notes**. Right-click a Space in Mission Control to rename? (Not possible — but Spaces auto-name from full-screen apps; wallpaper per Space is possible: set a wallpaper while on that Space.)
4. **Assign apps to Spaces**: right-click an app's Dock icon → *Options → Assign To → This Desktop*. Slack always opens on 1, your IDE on 3, etc. *All Desktops* is great for a music player or a floating notes window. `When switching to an application, switch to a Space with open windows for the application`: on — so <kbd>⌘</kbd><kbd>Tab</kbd> to Slack jumps to Space 1.
5. Move windows between Spaces by dragging them to the edge of the screen (hold briefly), dragging onto a Space thumbnail in Mission Control, or — fastest — **start dragging the window, then press <kbd>⌃</kbd><kbd>←</kbd>/<kbd>→</kbd>** with the other hand.

Trackpad: three- or four-finger horizontal swipe switches Spaces, up opens Mission Control, down shows the current app's windows (App Exposé). `Accessibility → Display → Reduce motion` makes the switch instant instead of sliding.

Full-screen (<kbd>⌃</kbd><kbd>⌘</kbd><kbd>F</kbd>) is a Space of its own that hides the menu bar and Dock. Great for a single-window focus session on a laptop screen; awkward on a big monitor. **Split View** (hover the green button → *Tile Window to Left of Screen*) puts two full-screen apps side by side with a draggable divider.

## Stage Manager

`Control Center → Stage Manager` (or Desktop & Dock). It groups windows into "stages" shown as thumbnails on the left; clicking one swaps the whole set in. It's a different metaphor from Spaces — like having your open windows as a deck of cards. Some people love it for a single laptop screen; most developers find Spaces + tiling more predictable and leave it off. If you try it, turn off *Show recent apps* to reclaim the left strip and use `Click wallpaper to reveal desktop: Only in Stage Manager`.

## Third-party window managers

Three tiers, from "just snapping" to "i3 on macOS". All need **Accessibility** permission (`Privacy & Security → Accessibility`); the tilers also want **Screen Recording** to read window titles in some cases.

### Tier 1 — snapping and hotkeys (most people)

| Tool | Price | Why pick it |
|---|---|---|
| **Rectangle** | Free, OSS | The classic. <kbd>⌃</kbd><kbd>⌥</kbd> + arrows/U/I/J/K/Enter/C for halves, quarters, thirds, maximise, centre, *next display* (<kbd>⌃</kbd><kbd>⌥</kbd><kbd>⌘</kbd><kbd>→</kbd>). Snap areas configurable. **Rectangle Pro** ($10) adds layouts, pinning, app-specific rules, stage-like "throw". |
| **Raycast window management** | Free (part of Raycast) | Same actions as Rectangle, assigned via Raycast hotkeys, plus *Reasonable Size*, *Almost Maximize*, custom sizes. If you already run Raycast, don't install a second tool. |
| **Loop** | Free, OSS | Hold a trigger key and move the mouse for a radial menu of positions. Pretty, fast, very configurable; the choice for people who don't want to memorise 15 chords. |
| **Swish** | $16 | Trackpad-gesture window management (swipe on a title bar to tile). Great with Magic Trackpad. |
| **BetterSnapTool / Magnet / Moom** | $3–$10 | Fine; older, still maintained. Moom's custom grid palette remains unique. |

**Recommendation**: Rectangle if you don't use Raycast; Raycast's built-in commands if you do. Bind: left/right halves, left/right two-thirds, maximise, centre, next display, and "reasonable size". That covers 95% of real use.

### Tier 2 — automatic tiling without disabling security

**AeroSpace** (free, OSS) is the most recommended tiler in 2026. It's an i3-like tree tiler: every new window is auto-placed in a split; you move focus with <kbd>⌥</kbd><kbd>H/J/K/L</kbd>, move windows with <kbd>⌥</kbd><kbd>⇧</kbd><kbd>H/J/K/L</kbd>, switch layout (tiles ↔ accordion) with <kbd>⌥</kbd><kbd>/</kbd>, and jump to *workspaces* with <kbd>⌥</kbd><kbd>1</kbd>…<kbd>9</kbd>. Crucially it **does not use macOS Spaces** (it emulates workspaces by hiding windows off-screen), so it needs **no SIP changes**, works on locked-down work machines, and switches workspaces with zero animation. Config is a single `~/.aerospace.toml` — dotfiles-friendly. Pair it with **JankyBorders** (active-window highlight) and **Sketchybar** if you want a Linux-rice look.

Minimal `~/.aerospace.toml` to get started:

```toml
start-at-login = true
after-startup-command = ['exec-and-forget borders active_color=0xff58a6ff width=5.0']
default-root-container-layout = 'tiles'
accordion-padding = 30
[gaps]
inner.horizontal = 8
inner.vertical = 8
outer.left = 8
outer.bottom = 8
outer.top = 8
outer.right = 8

[mode.main.binding]
alt-h = 'focus left'
alt-j = 'focus down'
alt-k = 'focus up'
alt-l = 'focus right'
alt-shift-h = 'move left'
alt-shift-j = 'move down'
alt-shift-k = 'move up'
alt-shift-l = 'move right'
alt-slash = 'layout tiles horizontal vertical'
alt-comma = 'layout accordion horizontal vertical'
alt-f = 'fullscreen'
alt-shift-f = 'layout floating tiling'
alt-minus = 'resize smart -50'
alt-equal = 'resize smart +50'
alt-1 = 'workspace 1'
alt-2 = 'workspace 2'
alt-3 = 'workspace 3'
alt-4 = 'workspace 4'
alt-shift-1 = 'move-node-to-workspace 1'
alt-shift-2 = 'move-node-to-workspace 2'
alt-shift-3 = 'move-node-to-workspace 3'
alt-shift-4 = 'move-node-to-workspace 4'
alt-tab = 'workspace-back-and-forth'
alt-shift-semicolon = 'mode service'

[mode.service.binding]
esc = ['reload-config', 'mode main']
r = ['flatten-workspace-tree', 'mode main']
f = ['layout floating tiling', 'mode main']

# Float apps that hate tiling
[[on-window-detected]]
if.app-id = 'com.apple.systempreferences'
run = 'layout floating'
[[on-window-detected]]
if.app-id = 'com.apple.finder'
run = 'layout floating'
```

**Amethyst** (free, OSS) is the simpler xmonad-style option: fewer concepts, works with real Spaces, good if AeroSpace feels like too much.

### Tier 3 — yabai (maximum control, some SIP cost)

**yabai** (free, OSS) + **skhd** (hotkey daemon) is the deepest tiler: BSP layouts, real Spaces integration, window opacity, borders, scripting via a Unix socket. Its full power (creating/destroying/moving Spaces, focusing across displays with animation off, window shadows/opacity) requires **partially disabling System Integrity Protection** and loading a scripting addition into Dock.app:

1. Boot to Recovery (hold power → Options → Terminal): `csrutil enable --without fs --without debug --without nvram` (Apple silicon).
2. Reboot, then `sudo nvram boot-args=-arm64e_preview_abi`, reboot again.
3. Add the sudoers line yabai's wiki gives so it can load the scripting addition without a password.

**This weakens your machine's security posture** (kernel/debug protections) and Apple sometimes breaks the addition on major macOS releases — check yabai's issue tracker before installing Golden Gate. Many yabai users run it *without* the scripting addition (SIP untouched) and accept losing Space manipulation; that is a reasonable middle path. On a work-managed Mac, don't touch SIP; use AeroSpace.

### Choosing

| You… | Use |
|---|---|
| Just want snap-to-half and maximise | Native tiling + Rectangle or Raycast |
| Use a big monitor and want thirds/two-thirds and quick centring | Rectangle / Raycast / Loop |
| Come from i3/sway/Hyprland and miss auto-tiling | **AeroSpace** |
| Want auto-tiling but keep real macOS Spaces and swipes | Amethyst, or yabai without SIP changes |
| Want everything scriptable and don't mind SIP tweaks | yabai + skhd (+ sketchybar) |
| Prefer gestures | Swish, or Loop |

## Multiple displays

- **Arrangement**: `Displays → Arrange…` (or drag the thumbnails). Put the display with the white bar as your **main display** — the Dock and new windows land there. With a laptop in clamshell, the external becomes main automatically.
- **Displays have separate Spaces** (Mission Control): **on**. Each display gets its own Spaces and menu bar. Off gives one giant Space spanning displays (useful for a single ultra-wide + laptop stretched layout, rarely otherwise).
- **Move a window to another display**: drag; or hover the green button → *Move to &lt;display&gt;*; or Rectangle's <kbd>⌃</kbd><kbd>⌥</kbd><kbd>⌘</kbd><kbd>←</kbd>/<kbd>→</kbd>; or AeroSpace's `move-node-to-monitor`.
- **Scaling**: for a 4K 27" pick the "looks like 2560×1440" (2×-ish) or 3008×1692 option; text stays sharp because macOS renders at 2× and downsamples. 5K 27" = perfect 2× at 2560×1440. A 1440p 27" monitor runs at 1× and text looks thin — that's the display, not a setting.
- **Refresh rate**: choose the max in `Displays`. Golden Gate exposes more high-res and high-refresh modes over Thunderbolt/HDMI and remembers window positions per display configuration much more reliably.
- **Clamshell**: closed lid + external display + power + external keyboard/mouse works out of the box. Keep the lid *open* an inch if the laptop gets hot under sustained load (the keyboard deck dissipates heat).
- **DisplayLink / USB-only docks**: avoid if you can. Thunderbolt/USB4 docks drive displays natively via DisplayPort Alt Mode; DisplayLink needs a driver (screen-recording permission, occasional flicker, no HDCP). If a cheap dock's second monitor doesn't appear, it's DisplayLink.
- **Two displays on base M-chips** (M5 Air/Pro): supported natively since M3 (Air needs the lid closed for two externals on M3; M4/M5 Air drives two with lid open). The Neo drives one.
- **Sidecar** turns an iPad into a display (wired or wireless, touch supported better in GG). **Universal Control** shares one keyboard/mouse across a Mac and iPad sitting next to each other — enable in `Displays → Advanced`.
- **iPhone Mirroring** (Sequoia+) puts your iPhone on the Mac desktop, resizable in GG; iPhone notifications arrive on the Mac. Useful for testing your own iOS app while coding.

## Focus-follows-mouse and other Linux habits

macOS has no system-wide focus-follows-mouse; AeroSpace/yabai offer it for their windows, and Ghostty/iTerm2 have it for their splits. Sloppy-focus fans generally adjust. Middle-click-to-paste doesn't exist outside X11 terminals (XQuartz). Workspaces-per-monitor behaviour is what `Displays have separate Spaces` gives you. Keyboard-driven everything: see the shortcuts in Chapter 5.

## Recommended setups

**Student on a 13"/15" laptop, no monitor**: native tiling for halves; 4 Spaces with roles; <kbd>⌃</kbd><kbd>1–4</kbd> bound; full-screen for the editor during deep work; Raycast or Rectangle for "maximise" and "centre". Reduce motion on.

**Engineer with a 27" 5K + laptop**: main display = the 27"; separate Spaces on; editor two-thirds left / terminal one-third right (Rectangle <kbd>⌃</kbd><kbd>⌥</kbd><kbd>E</kbd>/<kbd>T</kbd>) on Space 1 of the big screen; browser on Space 2; comms on the laptop screen. Assign Slack/Mail to the laptop display's Space.

**Tiling enthusiast**: AeroSpace + JankyBorders, 6 workspaces, apps assigned by `on-window-detected` rules, System Settings/Finder/dialog-heavy apps floated, Ghostty as the terminal with its own splits, `alt-tab` back-and-forth. Native Spaces unused; Mission Control gestures disabled to avoid confusion.
