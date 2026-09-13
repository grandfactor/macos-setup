<!--
number: 04
part: Part II — System & interface
description: Finder as a power tool, Quick Look, the Dock, and the new Spotlight (apps, files, actions, clipboard, Quick Keys) — plus when Raycast or Alfred still earn their place.
-->
# Finder, Dock & Spotlight

Three built-in tools you'll touch hundreds of times a day. Finder is more capable than its reputation; the Dock is best minimised; and Spotlight, since macOS 26, is a genuine launcher that changes the calculus on Raycast and Alfred.

## Finder

### Views and navigation

- **List view** (<kbd>⌘</kbd><kbd>2</kbd>) is the developer default: sortable columns, expandable folders (<kbd>→</kbd>/<kbd>←</kbd> expand/collapse; <kbd>⌥</kbd><kbd>→</kbd> expands recursively). Set it as the default in `View → Show View Options → Use as Defaults` after enabling *Calculate all sizes* and adding the *Date Modified* and *Kind* columns.
- **Column view** (<kbd>⌘</kbd><kbd>3</kbd>) is fastest for drilling into deep trees; the resize bug from 26.0 was fixed in 26.3.
- **Gallery view** (<kbd>⌘</kbd><kbd>4</kbd>) for photos/PDFs with the Preview pane (<kbd>⌘</kbd><kbd>⇧</kbd><kbd>P</kbd>) showing metadata.
- **Go to folder**: <kbd>⌘</kbd><kbd>⇧</kbd><kbd>G</kbd>, type a path (`~/Library/Application Support`, `/opt/homebrew/etc`). Tab completes. It accepts `~` and `..`.
- **Go menu** shortcuts: <kbd>⌘</kbd><kbd>⇧</kbd><kbd>H</kbd> Home, <kbd>⌘</kbd><kbd>⇧</kbd><kbd>D</kbd> Desktop, <kbd>⌘</kbd><kbd>⇧</kbd><kbd>O</kbd> Documents, <kbd>⌘</kbd><kbd>⌥</kbd><kbd>L</kbd> Downloads, <kbd>⌘</kbd><kbd>⇧</kbd><kbd>A</kbd> Applications, <kbd>⌘</kbd><kbd>⇧</kbd><kbd>U</kbd> Utilities, <kbd>⌘</kbd><kbd>↑</kbd> enclosing folder, <kbd>⌘</kbd><kbd>↓</kbd> or <kbd>⌘</kbd><kbd>O</kbd> open.
- **Path bar** (`View → Show Path Bar`): right-click any segment → *Copy "…" as Pathname* or drag a folder from it into a Terminal window to paste its path. <kbd>⌘</kbd>-click the window title for the same hierarchy.
- **Copy a path**: select an item, <kbd>⌘</kbd><kbd>⌥</kbd><kbd>C</kbd>. Or right-click while holding <kbd>⌥</kbd> → *Copy … as Pathname*.
- **Hidden files**: <kbd>⌘</kbd><kbd>⇧</kbd><kbd>.</kbd> toggles.
- **Rename**: select, press <kbd>Return</kbd>. **Batch rename**: select several → right-click → *Rename…* (replace text, add sequence, add date).
- **Tabs**: <kbd>⌘</kbd><kbd>T</kbd>; merge windows with `Window → Merge All Windows`. Drag files onto a tab to move them there.
- **Move instead of copy** between volumes: <kbd>⌘</kbd>-drag. **Duplicate**: <kbd>⌘</kbd><kbd>D</kbd>. **Make alias**: <kbd>⌘</kbd><kbd>⌃</kbd><kbd>A</kbd>. **Cut and paste** files: copy with <kbd>⌘</kbd><kbd>C</kbd>, then **<kbd>⌘</kbd><kbd>⌥</kbd><kbd>V</kbd>** to move.
- **Delete immediately** (skip Trash): <kbd>⌘</kbd><kbd>⌥</kbd><kbd>⌫</kbd>. **Empty Trash without confirmation**: <kbd>⌘</kbd><kbd>⌥</kbd><kbd>⇧</kbd><kbd>⌫</kbd>.
- **New folder with selection**: select files → right-click → *New Folder with Selection (N items)*.
- **Open in Terminal**: right-click a folder → *Services → New Terminal at Folder* (enable in `System Settings → Keyboard → Keyboard Shortcuts → Services → Files and Folders`). Ghostty/iTerm2 install their own equivalents. Reverse direction: `open .` in a terminal opens Finder there.
- **Get Info** (<kbd>⌘</kbd><kbd>I</kbd>) for permissions, *Open with* default app (click *Change All…*), lock, and the hidden **Comments** field that Spotlight indexes. <kbd>⌘</kbd><kbd>⌥</kbd><kbd>I</kbd> is the *Inspector* that updates as you change selection.
- **Tags**: right-click → Tags. Useful for `urgent`/`todo`/`course-xyz`. Search `tag:urgent` in Spotlight.
- **Folder customisation** (Tahoe+): right-click → *Customize Folder…* — colour, emoji, or SF Symbol. Cheap visual structure for `~/Developer/school/*`.

### Sidebar, toolbar and favourites

- Drag your project folders, `~/Developer`, and `~/Library` (after `chflags nohidden ~/Library`) into the sidebar's *Favorites*. Remove *Recents* and *AirDrop*.
- Right-click the toolbar → *Customize Toolbar…*: add *Path*, *New Folder*, *Get Info*, *Delete*, *Connect*, and a **Quick Actions** button. Drag any app or script onto the toolbar while holding <kbd>⌘</kbd> to get a one-click launcher (e.g. your terminal or editor: drop VS Code there and drag folders onto it).
- **Connect to Server** (<kbd>⌘</kbd><kbd>K</kbd>): `smb://nas.local/share`, `nfs://`, `ftp://`, `vnc://`. Tick *Remember* and add to Favorites. Golden Gate speeds up SMB browsing noticeably.

### Quick Look

Select a file and press <kbd>Space</kbd>. It previews images, PDFs, video, Office docs, and — with plugins — code, Markdown, JSON, archives and more. <kbd>⌘</kbd><kbd>Y</kbd> also works. Arrow keys move through the selection; <kbd>⌥</kbd><kbd>Space</kbd> opens full screen. Quick Look supports *Markup* (annotate PDFs/images) and *Trim* (video) directly.

Essential Quick Look extensions for developers (all via Homebrew, all free):

```sh
brew install --cask qlmarkdown syntax-highlight   # Markdown preview; syntax-highlighted source for 100+ languages
brew install --cask quicklook-json qlstephen      # pretty JSON; plain-text files without extensions (README, Makefile, LICENSE)
brew install --cask quicklook-csv qlvideo         # CSV as table; thumbnails for more video codecs
brew install --cask betterzip                     # peek inside zip/tar without extracting (paid, but the QL plugin works in trial)
```

After installing, run `qlmanage -r` to reload, and approve each extension in `System Settings → General → Login Items & Extensions → Quick Look`.

### Smart Folders and Spotlight queries

`File → New Smart Folder` builds a saved search. Examples worth saving to the sidebar:

- *Kind is Source Code, Modified within last 7 days* → "This week's code".
- *Name contains `.env`* in `~/Developer` → occasional audit of secrets on disk.
- *Size > 500 MB* → what's eating the disk (also see `ncdu`, Chapter 18).

Raw query syntax works in the Finder search field and Spotlight: `kind:pdf date:this week`, `name:report kind:document`, `tag:urgent`, `modified:>2026-09-01`. In the search field, click the **+** to add criteria and *Other…* to pick from hundreds of metadata attributes (e.g. *Pixel width*, *Codec*).

### Archive and disk images

- Right-click → *Compress* makes a `.zip` (Archive Utility handles zip, tar.gz, bz2, xz; **not** rar or 7z — use `brew install --cask keka` or `brew install sevenzip`).
- Disk images: double-click a `.dmg` to mount; drag the app to `/Applications`; **eject** the image from the sidebar afterwards. Since Tahoe, new images default to **ASIF** (Apple Sparse Image Format), which is dramatically faster and near-native SSD speed — the right format for VM disks and encrypted vaults: `Disk Utility → File → New Image → Blank Image → Format: APFS, Encryption: 256-bit AES, Image Format: sparse` gives you an encrypted folder that mounts with a password.

### Things Finder still doesn't do well (and fixes)

| Gap | Fix |
|---|---|
| Two-pane file management (Norton Commander style) | **Marta** (free), **ForkLift 4**, **Commander One**; or `yazi` in the terminal (Chapter 9) |
| Bulk operations on thousands of files | Terminal: `fd`, `rg`, `rsync` — Chapter 9 |
| Show folder sizes instantly | `View → Show View Options → Calculate all sizes` (List view), or **OmniDiskSweeper** / `ncdu` |
| Cut (⌘X) files | Use <kbd>⌘</kbd><kbd>C</kbd> then <kbd>⌘</kbd><kbd>⌥</kbd><kbd>V</kbd> — Finder's "Move here" |
| Open a folder as a *project* | Drag it onto your editor's Dock icon, or `code .`, `zed .`, `cursor .` from Terminal |
| Automatic Downloads cleanup | **Hazel** (paid) rules, or a Shortcuts folder automation — Chapter 21 |
| `.DS_Store` files on network shares / repos | `defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true; defaults write com.apple.desktopservices DSDontWriteUSBStores -bool true` and add `.DS_Store` to your global gitignore (Chapter 10) |

## The Dock

The Dock is a launcher and a window switcher; with Spotlight and <kbd>⌘</kbd><kbd>Tab</kbd> doing both jobs, most developers shrink it and hide it (Chapter 3 has the settings). What's left to know:

- **Keep only the apps you run daily.** Drag everything else out (drop it on the desktop until it says *Remove*). A tidy Dock is a faster <kbd>⌘</kbd><kbd>Tab</kbd>.
- **Stacks**: drag `~/Downloads`, `~/Pictures/Screenshots` and your current project folder to the right side (next to Trash). Right-click → *Display as Folder*, *View content as Grid* or *Fan*. `Sort by Date Added` makes Downloads a reverse-chronological list.
- **Option-click** the Dock icon of an app for *Force Quit*. **Option-⌘-drag** a file onto a Dock icon that refuses it to force that app to open it.
- **Spacers**: `defaults write com.apple.dock persistent-apps -array-add '{tile-type="spacer-tile";}'; killall Dock` adds a blank separator; drag it where you want it. Use `small-spacer-tile` for a half-width one.
- **Show only running apps** (turn the Dock into a pure task switcher): `defaults write com.apple.dock static-only -bool true; killall Dock`.
- **Scroll on a Dock icon to show its windows**: `defaults write com.apple.dock scroll-to-open -bool true; killall Dock`.
- **Hidden apps translucent**: `defaults write com.apple.dock showhidden -bool true; killall Dock`.
- **Reset the Dock**: `defaults delete com.apple.dock; killall Dock`.

And the switcher: <kbd>⌘</kbd><kbd>Tab</kbd> cycles apps (hold <kbd>⌘</kbd>, tap <kbd>Tab</kbd> repeatedly; <kbd>⌘</kbd><kbd>`</kbd> cycles windows *within* an app; while the switcher is up, press <kbd>Q</kbd> to quit or <kbd>H</kbd> to hide the highlighted app, <kbd>↓</kbd> to see its windows). If you want windows rather than apps in the switcher (Windows-style <kbd>Alt</kbd><kbd>Tab</kbd>), install **AltTab** (free, open source).

## Spotlight (macOS 26+)

Spotlight was rebuilt in Tahoe and became a real launcher, then got Siri AI inside it in Golden Gate. If you last used it in Sonoma, relearn it.

### The four views

Press <kbd>⌘</kbd><kbd>Space</kbd>, then:

| Key | View | What it does |
|---|---|---|
| <kbd>⌘</kbd><kbd>1</kbd> | **Apps** | A grid of every installed app (this replaced Launchpad, which is gone), including iPhone apps via iPhone Mirroring. Type to filter. |
| <kbd>⌘</kbd><kbd>2</kbd> | **Files** | Recent files with type filters at the top; supports **slash filters** `/pdf`, `/word`, `/image`, `/text` then <kbd>Return</kbd>. |
| <kbd>⌘</kbd><kbd>3</kbd> | **Actions** | Hundreds of system and app commands: *Send Message*, *Create Event*, *Set Timer*, *Convert to PDF*, *Resize Image*, run any **Shortcut**. Apps expose their own via App Intents (e.g. Ghostty can focus a terminal). |
| <kbd>⌘</kbd><kbd>4</kbd> | **Clipboard** | Clipboard history (see below). |

Other shortcuts inside Spotlight: <kbd>↑</kbd> recalls previous *searches* (like shell history); <kbd>⌘</kbd><kbd>Return</kbd> reveals the selected file in Finder; <kbd>⌘</kbd><kbd>C</kbd> copies the result's path; <kbd>Tab</kbd> or <kbd>⌘</kbd><kbd>I</kbd> shows a preview/info pane; <kbd>⌘</kbd><kbd>L</kbd> jumps to the dictionary definition; <kbd>⌘</kbd><kbd>B</kbd> searches the web. Type maths (`2^32-1`, `15% of 84`, `120 usd in eur`, `3pm PST in London`) and get answers inline.

### Quick Keys

Spotlight assigns short abbreviations to your most-used *actions*: type `sm` → *Send Message*, `cr` → *Create Reminder*, `nn` → *New Note*, then <kbd>Return</kbd> and fill in the parameters inline without opening the app. They're auto-assigned by usage; see and reset them in `System Settings → Spotlight`. Any Shortcut you build (Chapter 21) becomes an action and can get a Quick Key — this is how you run "Start Deep Work Focus + open project + start timer" from four keystrokes.

### Clipboard history

Enable it once (Spotlight → <kbd>⌘</kbd><kbd>4</kbd> → *Turn On*, or `System Settings → Spotlight → Clipboard History`). It records text, images, files and URLs with source app and timestamp. <kbd>Return</kbd> pastes as **plain text** at the cursor (so it also replaces the old <kbd>⌘</kbd><kbd>⌥</kbd><kbd>⇧</kbd><kbd>V</kbd> paste-and-match-style habit); the small button to the right of an item makes it the *current* clipboard instead.

Limits you should know: **items expire after 8 hours**, nothing can be pinned, and there's no single-key shortcut to open the clipboard view — it's <kbd>⌘</kbd><kbd>Space</kbd> then <kbd>⌘</kbd><kbd>4</kbd>. Passwords copied from Apple's Passwords app are excluded, but third-party managers' copies may appear — copy something else right after pasting a secret. For persistent, pinnable history, add **Maccy** (free, open source, `brew install --cask maccy`) or use Raycast's clipboard manager.

### Search settings

`System Settings → Spotlight`: turn off categories you never want in results (*Siri Suggestions*, *Websites*, *Movies*, *Fonts*), and **Search Privacy…** to exclude folders — add your `node_modules`-heavy monorepo, VM disk folders, and Time Machine drives if indexing them slows things. Golden Gate rebuilt the search index (26.6 pre-optimised it); if search is wrong or slow, rebuild with `sudo mdutil -E /` and give it an hour.

For developers, note that Spotlight indexes file *contents* for text, code, PDFs and Office docs; `mdfind "kind:source 'TODO'"` uses the same index from the CLI, and `mdls file` shows the metadata it extracted.

### Siri AI in Spotlight (Golden Gate)

In macOS 27, <kbd>⌘</kbd><kbd>Space</kbd> is labelled **Search or Ask**. Plain queries search as before; questions ("what's the door code Sarah texted me", "summarise this PDF", "convert this table to CSV") are routed to Siri AI, which can read your local index (Mail, Messages, Notes, Files) and take actions in apps. Attach files with the **+**. **Visual Intelligence** is <kbd>⌘</kbd><kbd>⇧</kbd><kbd>Space</kbd>: drag a rectangle on screen and ask about it (great for "what does this compiler error mean" without copying text). Siri AI is opt-in (`System Settings → Apple Intelligence & Siri`) and English-only at launch; requests that leave the device go to Private Cloud Compute. If you'd rather Spotlight *only* searched, turn Siri AI off there.

## Raycast, Alfred, LaunchBar: do you still need one?

Honest 2026 answer: **Spotlight is enough for launching, files, actions and light clipboard use.** A third-party launcher is worth it if you want any of:

| Want | Spotlight (26/27) | **Raycast** | **Alfred 5** (Powerpack) |
|---|---|---|---|
| Launch apps, open files | ✅ | ✅ | ✅ (fastest raw search) |
| Persistent, pinned, searchable clipboard | ❌ (8 h, no pins) | ✅ free | ✅ |
| Snippets / text expansion | ❌ (Text Replacements only) | ✅ free | ✅ |
| Window management (halves, thirds, move to display) | ❌ (only native tiling) | ✅ free, excellent | via workflows |
| Calculator, unit/currency conversion | ✅ basic | ✅ rich | ✅ |
| Extensions store (GitHub, Jira, Linear, Homebrew, Docker, 1Password, VS Code projects…) | ❌ | ✅ ~2,000+ free | ✅ workflows (community) |
| Emoji picker, colour picker, system commands (sleep, empty trash, toggle dark mode) | partial | ✅ | ✅ |
| Scripting your own commands | Shortcuts | TypeScript/React extensions or script commands | Bash/Python/AppleScript workflows |
| Built-in AI chat / model routing | Siri AI (GG) | Pro ($8–10/mo) | via workflows |
| Price | free | **free** core; Pro for AI, sync, custom themes | ~£34 one-time Powerpack |
| Notes | Keeps improving each release | Cloud account optional; closed source; owns the "everything app" niche | Fast, local-first, one-time price; the automation nerd's pick |

**Recommendation**: install **Raycast** (`brew install --cask raycast`), bind it to <kbd>⌥</kbd><kbd>Space</kbd> (leave <kbd>⌘</kbd><kbd>Space</kbd> for Spotlight — the two coexist well), and use it for clipboard history, snippets, window management and the extensions you actually adopt (Homebrew search, GitHub, "Open project in editor"). Skip Raycast Pro unless the AI features replace a subscription you'd otherwise pay for. Choose **Alfred** if you dislike accounts and Electron-ish apps, or already own the Powerpack. Choose **LaunchBar** if you've used it for 15 years. Skip all three if Spotlight plus Maccy covers you — many people are surprised that it does now.
