<!--
number: 19
part: Part V — Daily driving & workflows
description: The non-developer half of the Mac — browsers, password managers, launchers, clipboard managers, notes, email, calendar, PDF, media, communication, and the utilities that make macOS feel finished. Free/open-source first, with the paid upgrade named where it's worth it.
-->
# Daily-driver apps

A developer setup guide that stops at the terminal misses half the day. You'll spend as many hours in a browser, a notes app, a calendar, and Slack as in an editor, and the small utilities — a clipboard manager, a launcher, a window manager — are what make macOS feel *finished*. This chapter is the opinionated app list. Every item is available as a Homebrew cask (or App Store via `mas`) so the whole list installs from the [Brewfile](appendix-b-brewfile.html); the "Install" column gives the cask name.

The bias throughout: **free and open source first**, paid where it's genuinely better, and nothing that needs a subscription to do a job a one-time purchase did in 2019. Prices are current as of September 2026 and will drift.

> [!TIP]
> Don't install all of this on day one. Install the **Tier 1** items (bold in each section), live with the Mac for a week, and add things when you notice a specific friction. A Mac with 15 well-chosen apps beats one with 60 half-configured ones — see [chapter 18](18-performance-and-maintenance.html) on login items.

## Browsers

Your browser is the app you use most. Have two: a primary for daily life and a secondary for testing, isolated logins, and "the site that only works in Chrome."

| Browser | Engine | Why | Install |
|---|---|---|---|
| **Safari** | WebKit | Best battery life by a wide margin (often 1–2 hours more than Chrome), tightest OS integration (Passwords, Handoff, Tab Groups, Apple Pay), strong tracker blocking. Extensions are fewer but the essentials exist. Included with macOS. | built-in |
| **Firefox** | Gecko | The only major non-Chromium engine, excellent privacy defaults, container tabs (Multi-Account Containers) for isolating logins, uBlock Origin works fully. | `firefox` |
| **Zen** | Gecko | Firefox-based with an Arc-like vertical sidebar, workspaces, split view. The usual recommendation for people who liked Arc (which has been frozen since 2025). | `zen` |
| **Chrome** | Chromium | The compatibility baseline; DevTools are the reference; Google account integration. Heavier on battery and memory. Since Manifest V3, uBlock Origin is Lite-only. | `google-chrome` |
| **Brave** | Chromium | Chrome compatibility with built-in ad/tracker blocking; turn off the crypto/rewards features on first run. | `brave-browser` |
| **Vivaldi**, **Orion** | Chromium / WebKit | Vivaldi for power-user tab management; Orion (Kagi) for WebKit with Chrome *and* Firefox extension support — still occasionally rough. | `vivaldi`, `orion` |

Recommendation for a student/engineer: **Safari as the daily driver** (battery, integration) plus **Firefox or Chrome for development** with DevTools and extensions. Set the default in **System Settings → Desktop & Dock → Default web browser**.

Extensions worth having regardless of browser: a content blocker (uBlock Origin on Firefox; AdGuard or Wipr 2 on Safari; uBlock Origin Lite on Chrome), your password manager's extension, and **Refined GitHub**. Safari extensions are installed from the App Store (many are free).

Browser profiles: Chrome and Firefox both support multiple profiles — one for university/work accounts, one personal — which is cleaner than juggling logins. Safari has profiles since macOS 14 (**Safari → Settings → Profiles**).

## Password manager

Non-negotiable. See [chapter 16](16-security-and-privacy.html) for the reasoning; here's the choice:

| Option | Cost | Notes |
|---|---|---|
| **Apple Passwords** | Free | The built-in app (since macOS 15) with passkeys, TOTP codes, shared groups, Wi-Fi passwords, and a Windows/Chrome extension. Enough for most people who live in Apple's ecosystem. Now also stores your FileVault recovery key. |
| **Bitwarden** | Free / $10 yr | Open source, cross-platform, self-hostable (Vaultwarden). Free tier has everything one person needs; Premium adds TOTP and file attachments. The default recommendation if you use Android/Windows/Linux too. |
| **1Password** | $36 yr / $60 family | The most polished UI, best browser integration, SSH agent, developer CLI (`op`) for secrets in scripts and env vars. Worth it if your team uses it or you want the SSH/CLI features. Free for GitHub Student Developer Pack holders (one year). |
| **KeePassXC** | Free | Local-only database file; sync it yourself. For people who don't want a cloud in the loop. |

Install: `bitwarden`, `1password` + `1password-cli`, `keepassxc`. Whatever you pick, turn off Safari/Chrome's own password saving so you don't end up with three overlapping vaults.

## Launcher

Spotlight in macOS 26 is good — app launching, calculator, clipboard history (8 hours), file search, Shortcuts actions, Siri/AI answers, and `⌘1`–`⌘4` filtered views (see [chapter 4](04-finder-dock-spotlight.html)). Try living with it for a week before installing a replacement.

If you want more:

| Launcher | Cost | Why |
|---|---|---|
| **Raycast** | Free core; Pro $8 mo for AI/cloud sync | The current default among developers. Extension store (GitHub, Jira, Linear, Homebrew, color pickers, snippets, window management), scriptable in TypeScript, unlimited clipboard history, floating notes, quick AI chat. The free tier is genuinely complete. |
| **Alfred** | Free; Powerpack £34 one-time | The veteran. Workflows are extremely capable; one-time purchase; lighter than Raycast. If you dislike subscriptions and Electron-adjacent UIs, Alfred. |
| **LaunchBar** | $29 | Mature, fast, keyboard-centric; smaller community. |

Bind the launcher to `⌘Space` and move Spotlight to `⌥Space` (or vice versa) in **System Settings → Keyboard → Keyboard Shortcuts → Spotlight**. Install: `raycast`, `alfred`, `launchbar`.

## Clipboard manager

The single highest-value utility most people don't know they need. Copy several things, paste any of them later, with search.

- **Spotlight's built-in history** (macOS 26): `⌘Space` then `⌘4`. Eight hours only, no pinning. Fine to start.
- **Raycast Clipboard History** — if you already run Raycast, it's there (`⌥⌘C` by default, configurable), searchable, with images and pinning.
- **Maccy** (free, open source) — a menu bar clipboard history with fuzzy search. The lightweight standalone pick. `maccy`
- **Paste** ($15 yr) — the pretty one, with iCloud sync to iPhone and pinboards. Subscription.
- **CopyQ** (free) — cross-platform, scriptable, uglier. For people who also use Linux.

Whatever you use, exclude your password manager from history (all of the above support ignoring apps — set it).

## Window management

Covered in depth in [chapter 6](06-window-management.html). Summary for the app list: macOS 26 tiling (drag to edge, `fn+ctrl` shortcuts) handles the basics; **Rectangle** (free) for keyboard-driven halves/thirds; **AeroSpace** (free) for i3-style tiling; **Raycast** has window commands built in. Install: `rectangle`, `aerospace`.

## Notes and knowledge

The genre where opinions run hottest. Pick by *where your notes need to be* rather than features.

| App | Cost | Sync | Why |
|---|---|---|---|
| **Apple Notes** | Free | iCloud | Fast, reliable, searchable, handles PDFs and handwriting from iPad, shared folders, Quick Note (`fn+Q`). Underrated for lecture notes and general life. Not Markdown; export is awkward. |
| **Obsidian** | Free (Sync $4–8 mo; or sync via iCloud/Git) | Files on disk | Markdown files in a folder you own, linked notes, graph view, thousands of community plugins, Canvas, vim mode. The default for CS students who want notes to outlive any company. Sync with iCloud Drive for free, or Obsidian Git plugin. |
| **Notion** | Free personal; Plus $10 mo | Cloud | Databases, kanban, shared team wikis, templates. Great for project/course tracking; slow, online-only-ish, and your data is in their format. Free for students with a `.edu` email. |
| **Bear** | $30 yr | iCloud | Beautiful Markdown-flavored notes with tags; Apple-only. |
| **Logseq** / **Anytype** | Free | Files / P2P | Outliner-style (Logseq) and Notion-like but local-first (Anytype) alternatives. |
| **Zotero** | Free | Cloud (300 MB free) | Reference manager for papers; Safari/Chrome connector saves PDFs and metadata in one click. Essential from the first research-heavy course onward. |

Recommendation: **Obsidian for coursework and long-term knowledge, Apple Notes for everything ephemeral**, Zotero the moment you have to cite anything. Install: `obsidian`, `notion`, `bear` (App Store), `logseq`, `anytype`, `zotero`.

## Tasks, calendar, and time

- **Reminders + Calendar** (built-in) are more than enough for most students. Reminders has smart lists, tags, subtasks, and natural language ("Submit lab Friday 5pm"). Calendar supports Google/Outlook/CalDAV accounts and shows in the menu bar via **Itsycal** (free) or **Dato**.
- **Things 3** ($50 one-time for Mac, separate iPhone/iPad) — the most pleasant task manager on the platform; no subscription. **Todoist** (free / $4 mo) for cross-platform and natural-language entry. **OmniFocus** if you're deep into GTD.
- **Fantastical** ($57 yr) is the calendar power tool (natural-language entry, multiple calendar sets, Zoom integration); the free tier is fine as a menu bar calendar. **BusyCal** ($50 one-time) is the no-subscription alternative.
- **Toggl Track** (free) or **Timing** ($) if you bill hours or want to know where the day went.
- **Itsycal** (`itsycal`, free) — a tiny menu bar calendar. Nearly everyone should install this.

## Email

- **Apple Mail** — free, private, handles Gmail/Exchange/IMAP, Hide My Email, mail categorization since macOS 15. Rules and smart mailboxes are underused. The right default for most people.
- **Thunderbird** — free, open source, cross-platform, extension ecosystem, good for multiple accounts and heavy filtering.
- **Mimestream** ($50 yr) — native Gmail client that speaks the Gmail API (labels, categories, snooze) properly. If you live in Gmail and dislike the web UI, this is the one.
- **Spark**, **Superhuman** ($30 mo) — AI-assisted triage; Superhuman is very fast and very expensive.
- **Proton Mail / Fastmail apps** if that's your provider.

Set your default mail client in **Mail → Settings → General** (yes, the setting lives inside Mail.app even for choosing another app).

## Communication

Almost all of these are Electron apps that want to run at login and eat 400 MB each. Install the ones you actually need and set them to *not* open at login; open them when you sit down to work.

`slack`, `discord`, `zoom`, `microsoft-teams`, `signal`, `telegram`, `whatsapp`. **Messages** and **FaceTime** are built in and, in 2026, do RCS with Android users. For Slack and Discord specifically, the browser version is usually fine and saves memory.

## Files, cloud, and sync

- **iCloud Drive** — already there; Desktop & Documents sync is convenient and dangerous (see [chapter 2](02-first-boot-and-migration.html)). Good for documents; keep code out of it (Git repos + iCloud eviction = corruption risk).
- **Google Drive**, **Dropbox**, **OneDrive** — all use the File Provider API now, so they behave like iCloud (files on demand, no kernel extension). Install the one your school/work uses. Storage tiers are cheaper via a Google One / Microsoft 365 student plan.
- **Syncthing** (free, open source, `syncthing`) — peer-to-peer folder sync without a cloud. Excellent for syncing an Obsidian vault or a projects folder between a laptop and a desktop.
- **Maestral** (free, `maestral`) — open-source Dropbox client that's lighter than the official one.
- **Transmit** ($45) or **Cyberduck** (free) for SFTP/S3 with a GUI; **Mountain Duck** to mount remote storage as a disk. For most engineers, `rsync`/`scp`/`rclone` in the terminal is enough.

Finder quality-of-life (see [chapter 4](04-finder-dock-spotlight.html) for settings): **QuickLook plugins** — `qlmarkdown`, `syntax-highlight`, `quicklook-json`, `qlvideo` let space-bar preview handle Markdown, source code, JSON, and more video formats. Since macOS 15 these need explicit enabling in **System Settings → Login Items & Extensions → Quick Look**.

## PDFs and documents

- **Preview** — built-in, does annotation, form filling, signatures, page reorder, merge (drag thumbnails between windows), and image conversion. Most people never need more.
- **Skim** (free, `skim`) — PDF reader for academics: notes, highlights with export, SyncTeX for LaTeX, presentation mode.
- **PDF Expert** ($80 yr or one-time tier) — if you edit PDFs heavily.
- **Zotero** handles paper PDFs (see above).
- **Pages / Numbers / Keynote** (free, App Store) — perfectly good, and Keynote is the best presentation app on any platform.
- **Microsoft 365** — free for most students through their university; install via `microsoft-office` or the Mac App Store. Word compatibility matters when a professor requires `.docx`.
- **LibreOffice** (free, `libreoffice`) — for when you need an office suite with no account.
- **Typora** ($15) / **MacDown** (free) / **iA Writer** ($50) — Markdown editors when you want to write prose rather than code. Or just VS Code with a Markdown preview.
- **LaTeX**: `mactex-no-gui` (cask, ~2 GB) plus **TeXShop** or VS Code with LaTeX Workshop; or **Overleaf** in the browser for collaborative writing. **Typst** (`typst`) is the modern alternative that compiles instantly and has a much saner syntax; most students writing solo papers should try it first.

## Media

- **IINA** (free, open source, `iina`) — the video player. Plays everything (mpv underneath), native macOS UI, picture-in-picture, Touch Bar/Trackpad gestures. Uninstall VLC.
- **Music / TV** — built-in; Apple Music student plan is $6 mo with Apple TV+ included.
- **Spotify** (`spotify`) — set it not to open at login; it's 500 MB of Electron.
- **Photos** — built-in and good; iCloud Photos is the sync you already pay for.
- **Pixelmator Pro** (now Apple's, free since 2025) / **Affinity** (now free from Canva since 2025 — Photo, Designer, Publisher in one app) — the serious image editing choices; both one-time or free, no Adobe subscription.
- **Shottr** (free, `shottr`) — screenshot tool with pixel measurement, OCR, scrolling capture, annotations. The built-in `⌘⇧5` is fine; Shottr is better. **CleanShot X** ($29) is the polished paid option.
- **Kap** (free, `kap`) / **Screen Studio** ($89) — screen recording as GIF/MP4; Screen Studio adds the auto-zoom effects you see in every product demo.
- **HandBrake** (`handbrake`), **ffmpeg** (`brew install ffmpeg`) — transcoding.
- **Audacity** (`audacity`) / **Ocenaudio** — audio editing.
- **OBS** (`obs`) — streaming and recording.
- **ImageOptim** (free, `imageoptim`) — drag-and-drop lossless image compression before committing assets to a repo.

## Menu bar and system utilities

| App | Cost | What | Install |
|---|---|---|---|
| **Ice** | Free | Hides menu bar icons behind a divider (Bartender alternative after its ownership change). Essential on a notch MacBook where icons vanish. | `jordanbaird-ice` |
| **Stats** | Free | CPU/GPU/memory/network/battery/temps in the menu bar. iStat Menus ($12) is the polished version. | `stats` |
| **AlDente** | Free / $ | Charge limiter with more control than the built-in 26.4 limit. | `aldente` |
| **KeyboardCleanTool** | Free | Locks the keyboard so you can wipe it. | `keyboardcleantool` |
| **Karabiner-Elements** | Free | Key remapping; Caps Lock → Escape/Control, hyper key. See [chapter 5](05-keyboard-and-input.html). | `karabiner-elements` |
| **BetterDisplay** | Free / $ | Fix scaling on non-Retina external monitors, virtual displays, brightness control for external monitors. | `betterdisplay` |
| **MonitorControl** | Free | Brightness/volume keys control external displays over DDC. | `monitorcontrol` |
| **Amphetamine** | Free | Keep the Mac awake for a presentation or a long download. Built-in `caffeinate -d` does the same from the terminal. | App Store |
| **AppCleaner** / **Pearcleaner** | Free | Thorough uninstalls (see [chapter 18](18-performance-and-maintenance.html)). | `appcleaner`, `pearcleaner` |
| **The Unarchiver** | Free | Opens every archive format macOS's built-in tool doesn't (rar, 7z). Or `brew install sevenzip` and use the terminal. | `the-unarchiver` |
| **Keka** | Free / $ | Archive creation with encryption and format choice. | `keka` |
| **LuLu** | Free | Outbound firewall — see [chapter 16](16-security-and-privacy.html). | `lulu` |
| **Hidden Bar** / **Dozer** | Free | Simpler Ice alternatives. | `hiddenbar` |
| **Latest** | Free | Checks all installed apps for updates (including non-Store, non-brew). | `latest` |
| **Mos** / **LinearMouse** | Free | Smooth scrolling and per-device scroll direction for a mouse (so the mouse scrolls "normally" while the trackpad stays "natural"). | `mos`, `linearmouse` |
| **Hammerspoon** | Free | Lua automation for windows, hotkeys, and system events — see [chapter 21](21-automation-and-scripting.html). | `hammerspoon` |
| **Numi** / **Soulver** | Free / $ | Natural-language calculator ("$1200 / 4 people in EUR"). Raycast and Spotlight do the simple cases. | `numi` |
| **TextSniper** / built-in Live Text | $ / Free | OCR from any screen region. macOS Live Text does this in Preview and screenshots already; Shottr does it free. | — |
| **Rocket** | Free | Slack-style `:emoji:` autocomplete everywhere. | `rocket` |
| **Klack** / **Keyclick** | $ | Mechanical keyboard sounds. No reason, just fun. | `klack` |

## Reading and reference

- **Dash** ($30) — offline API documentation for 200+ languages/frameworks with instant search; integrates with Raycast/Alfred and every editor. Paid, one-time, worth it for anyone who reads docs daily. `dash`
- **DevDocs** (free, web / `devdocs` desktop wrapper) — the free equivalent; works offline as a PWA.
- **NetNewsWire** (free, open source, `netnewswire`) — RSS reader, iCloud sync. RSS is still the best way to follow release notes and blogs. **Reeder** ($) is the pretty one.
- **Kindle**, **Apple Books** — built-in / App Store.
- **Anki** (free, `anki`) — spaced repetition. See [chapter 20](20-cs-student-specific.html).

## Terminal-adjacent GUI tools

Covered in their own chapters, but for completeness in the app list: **Ghostty** or **iTerm2** ([chapter 9](09-terminal-and-shell.html)); **VS Code**, **Cursor**, **Zed**, **JetBrains Toolbox** ([chapter 12](12-editors-and-ides.html)); **OrbStack** ([chapter 13](13-containers-and-vms.html)); **TablePlus**, **Postico**, **DBeaver** ([chapter 15](15-databases-and-local-dev.html)); **Fork**, **Tower**, **GitHub Desktop**, **Sublime Merge** for Git GUIs ([chapter 10](10-dotfiles-and-git.html)); **Proxyman** or **Charles** for HTTP debugging; **Bruno**/**Postman**/**Insomnia** for API clients ([chapter 14](14-cloud-and-devops-tooling.html)); **Kaleidoscope** ($) or **Meld** (free) for visual diffs.

## Games and fun (yes, really)

Mac gaming in 2026 is real: **Steam** (`steam`), **CrossOver** ($74 yr; runs Windows games via Wine + Apple's Game Porting Toolkit), **Whisky** (free, `whisky` — the free Wine/GPTK wrapper), and Apple's own Games app (macOS 26) for Arcade and Store titles. **Heroic** for Epic/GOG. **OpenEmu** for retro. Set Steam to *not* launch at login.

## What to skip

- **Antivirus** — see [chapter 16](16-security-and-privacy.html). XProtect + Gatekeeper + common sense; Malwarebytes free for an occasional scan if paranoid.
- **CleanMyMac, MacKeeper, "memory cleaners", "battery optimizers"** — see [chapter 18](18-performance-and-maintenance.html).
- **Adobe Creative Cloud** unless a course requires it; Affinity and Pixelmator are free now.
- **Java runtimes from java.com** — install via mise or `brew install openjdk` ([chapter 11](11-languages-and-runtimes.html)).
- **Flash, Silverlight, Java browser plugins** — if a university system requires one, complain to IT; it's 2026.
- **Anything that asks to install a kernel extension** on Apple silicon — legitimate software uses system extensions now; a kext is a red flag or abandonware.

## The Tier 1 list

If you install nothing else from this chapter: **a password manager**, **Raycast or Alfred**, **a clipboard manager** (or Raycast's), **Rectangle or AeroSpace**, **Obsidian or Apple Notes**, **Itsycal**, **IINA**, **Shottr**, **Ice**, **Stats**, **AppCleaner**, **The Unarchiver**, **Karabiner-Elements** (if remapping), and **Zotero** (if writing). All are free. Everything is in [Appendix B](appendix-b-brewfile.html) with the optional items commented out.
