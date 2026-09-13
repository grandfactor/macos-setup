<!--
number: 21
part: Part V — Daily driving & workflows
description: Making the Mac do things for you — Shortcuts (and running them from the shell), launchd for scheduled and event-driven jobs, Automator's remaining uses, AppleScript and JXA for controlling apps, Hammerspoon for Lua-powered hotkeys and window/system automation, Keyboard Maestro and BetterTouchTool, Folder Actions and Hazel, and a grab-bag of macOS-specific CLI tools every script should know about.
-->
# Automation & scripting

macOS has more automation layers than any other desktop OS, accumulated over 30 years: AppleScript (1993), Automator (2005), launchd (2005), JavaScript for Automation (2014), Shortcuts (2021), and a rich set of command-line tools that expose the GUI — `open`, `pbcopy`, `osascript`, `defaults`, `mdfind`, `say`, `shortcuts`. Third-party tools (Hammerspoon, Keyboard Maestro, BetterTouchTool, Hazel) fill the gaps. This chapter picks the right layer for each kind of job and gives working examples you can paste.

> [!TIP]
> **Which tool?** Scheduled or on-boot job → **launchd**. Reacting to a new file in a folder → **Folder Action / Hazel / launchd WatchPaths**. Global hotkey that does something → **Hammerspoon** (free) or **Keyboard Maestro** ($). Chaining GUI apps together, or anything you want on iPhone too → **Shortcuts**. Poking a specific app's data (Mail, Music, Finder, Notes) → **AppleScript/JXA** via `osascript`. Anything that's just files and text → a **shell/Python script**, wrapped in one of the above.

## The macOS-specific CLI toolbox

Before writing automation, know the commands that make shell scripts on a Mac different from Linux. All are preinstalled.

| Command | What | Example |
|---|---|---|
| `open` | Open files, URLs, apps; the glue for everything | `open .` (Finder here), `open -a Safari https://…`, `open -R file` (reveal), `open -e notes.txt` (TextEdit), `open -b com.apple.Terminal`, `open 'x-apple.systempreferences:com.apple.Battery-Settings.extension'` |
| `pbcopy` / `pbpaste` | Clipboard in/out | `cat file \| pbcopy`, `pbpaste \| jq .`, `pbpaste > out.txt` |
| `osascript` | Run AppleScript or JXA from the shell | `osascript -e 'display notification "Done" with title "Build"'` |
| `defaults` | Read/write preference plists | `defaults read com.apple.dock`, `defaults write -g ApplePressAndHoldEnabled -bool false` |
| `shortcuts` | Run/list Shortcuts | `shortcuts run "Resize Image" -i photo.png`, `shortcuts list` |
| `automator` | Run a workflow | `automator -i file.txt Workflow.workflow` |
| `mdfind` / `mdls` | Spotlight queries and metadata | `mdfind -name invoice.pdf`, `mdfind 'kMDItemContentType == "com.adobe.pdf" && kMDItemFSSize > 10000000'`, `mdls photo.heic` |
| `say` | Text-to-speech | `make && say "build done" \|\| say "build failed"` |
| `afplay` | Play a sound | `afplay /System/Library/Sounds/Glass.aiff` |
| `screencapture` | Screenshots | `screencapture -i -c` (interactive, to clipboard), `screencapture -T 3 shot.png` |
| `sips` | Image conversion/resizing | `sips -Z 1024 *.png`, `sips -s format jpeg in.heic --out out.jpg` |
| `textutil` | Convert rtf/doc/html/txt | `textutil -convert txt notes.rtf` |
| `qlmanage -p` | Quick Look from the terminal | `qlmanage -p file.pdf` |
| `caffeinate` | Prevent sleep | `caffeinate -dis ./long_job.sh` (display, idle, system) |
| `pmset` | Power management | `pmset -g batt`, `sudo pmset repeat wakeorpoweron MTWRF 08:00:00` |
| `networksetup` / `scutil` | Network config | `networksetup -setairportpower en0 off`, `scutil --dns` |
| `airport` (gone) → `wdutil` | Wi-Fi info | `sudo wdutil info` |
| `system_profiler` | Hardware/software inventory | `system_profiler SPHardwareDataType`, `SPDisplaysDataType` |
| `sw_vers` / `uname -m` | macOS version / arch | `sw_vers -productVersion` → `26.6`; `uname -m` → `arm64` |
| `diskutil` / `hdiutil` | Disks and disk images | `hdiutil create -size 1g -fs APFS -volname Scratch scratch.dmg`, `hdiutil attach scratch.dmg` |
| `security` | Keychain from the shell | `security find-generic-password -s "MyAPI" -w` (read a secret) |
| `codesign` / `spctl` / `xattr` | Signature, Gatekeeper, quarantine | `xattr -d com.apple.quarantine ./tool` (only if you trust it — see [chapter 16](16-security-and-privacy.html)) |
| `launchctl` | Manage launchd jobs | below |
| `log` | Unified log | `log show --last 10m --predicate 'process == "kernel"'`, `log stream --predicate 'eventMessage contains "USB"'` |
| `tmutil` | Time Machine | `tmutil startbackup`, `tmutil listlocalsnapshots /` |
| `softwareupdate` | OS updates | `softwareupdate -l`, `softwareupdate --install-rosetta` |
| `mas` (brew) | App Store from the shell | `mas install 1569813296` |
| `duti` (brew) | Set default apps | `duti -s com.microsoft.VSCode .md all` |
| `trash` (brew) | Move to Trash instead of `rm` | `trash old/` (or `mv … ~/.Trash`) |
| `terminal-notifier` (brew) | Richer notifications with icons/actions | `terminal-notifier -title Build -message Done -open http://localhost:3000` |

Two idioms worth memorizing:

```sh
# Notify when a long command finishes (add to .zshrc as a function)
notify() { "$@"; local s=$?; osascript -e "display notification \"exit $s\" with title \"$1 finished\""; return $s; }
notify make -j8

# Secrets from Keychain instead of plaintext in .zshrc
export OPENAI_API_KEY="$(security find-generic-password -s openai -w 2>/dev/null)"
# store once with:  security add-generic-password -s openai -a "$USER" -w 'sk-…' -U
```

## Shortcuts

Shortcuts is Apple's mainstream automation: a visual action editor with ~300 system actions plus actions donated by apps (via App Intents), synced through iCloud to iPhone/iPad/Watch, runnable from Spotlight, the menu bar, a hotkey, Finder's Quick Actions, the Services menu, and — critically for developers — the shell.

### When Shortcuts is the right tool

- The task touches **apps**: resize the images in the selection and AirDrop them; make a calendar event from selected text; toggle a Focus mode; run a Shortcut on an iPhone photo that ends up on the Mac.
- You want it **on every device**. A Shortcut that logs a study session to a Notes table works identically on Mac and iPhone.
- It should appear in **Finder's right-click menu** (Quick Action) or the **Share sheet**.
- **macOS 26 automations**: Shortcuts on Mac finally has *triggers* — time of day, when an app opens/closes, when connecting to a display or Wi-Fi network, when a file is added to a folder, when a Focus turns on, on battery level, on Bluetooth connect. That was previously iOS-only and the main reason to reach for Hazel or Keyboard Maestro.
- **Apple Intelligence actions** (macOS 26): "Use Model" lets a Shortcut call the on-device model, Private Cloud Compute, or ChatGPT with a prompt and structured output — summarize the clipboard, extract dates from an email, classify a screenshot — no API key.

### Developer-relevant tricks

- **Run a shell script** action (Mac only) — `zsh` by default, receives Shortcut input on stdin or as an argument. Pass results back as text. So any script becomes a Quick Action, a menu bar item, a hotkey, or a Siri phrase in about 30 seconds.
- **Run from the terminal**: `shortcuts run "Name" --input-path file.png --output-path out/`. Scripts can call Shortcuts, Shortcuts can call scripts.
- **Keyboard shortcut**: in the Shortcut's details (ⓘ) → "Add Keyboard Shortcut". Works system-wide. Also "Pin in Menu Bar" and "Use as Quick Action" checkboxes.
- **Run AppleScript / Run JavaScript for Automation** actions embed the older languages when you need app scripting inside a Shortcut.
- **SSH**: the "Run Script over SSH" action lets a Shortcut on your *iPhone* run a command on your Mac (or a server) — restart a dev server from the couch.
- **Web requests**: "Get Contents of URL" does GET/POST with headers and JSON — enough for webhook-driven automations without any code.
- **Shortcuts as a launcher backend**: Raycast and Alfred both list your Shortcuts as commands.

### Example: "Commit and push current repo" Quick Action

1. Receive **Folders** in Finder → Run Shell Script with input as arguments:

    ```sh
    cd "$1" && git add -A && git commit -qm "wip: $(date '+%F %R')" && git push -q && echo "pushed $(git rev-parse --short HEAD)"
    ```

2. **Show Notification** with the output.
3. Tick "Use as Quick Action → Finder". Right-click any repo folder → Quick Actions → the Shortcut.

### Example: a study-timer automation (macOS 26 triggers)

Trigger: **Focus "Study" turned on** → actions: Quit App (Slack, Discord, Messages), Set Appearance (Dark), Run Shell Script (`brew services stop --all`), Set Do Not Disturb until Focus ends. Trigger **Focus "Study" turned off** → the reverse. This used to need Keyboard Maestro.

### Limitations

Shortcuts is slow to start (~0.5–1 s), error messages are opaque, there's no version control (export as `.shortcut` files to your dotfiles for a backup), and complex logic in a drag-and-drop editor becomes painful past ~30 actions. Push logic into a script and keep the Shortcut as a thin wrapper.

## launchd: cron, but better

macOS has `cron`, but it's discouraged (no persistence across sleep, no Full Disk Access prompts, `crontab` needs Full Disk Access itself now). **launchd** is the native way to run something at login, on a schedule, when a path changes, or continuously as a service. Every Homebrew service (`brew services`) is a launchd agent.

Two kinds: **LaunchAgents** run as your user, when you're logged in (`~/Library/LaunchAgents/`). **LaunchDaemons** run as root at boot, no user session (`/Library/LaunchDaemons/`, needs `sudo`). You'll almost always want agents.

A job is a property list. Label it with reverse-DNS naming (`com.yourname.backup-notes`), which is also the filename.

### Scheduled job: back up an Obsidian vault to Git hourly

```xml
<!-- ~/Library/LaunchAgents/com.yourname.vault-backup.plist -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key>            <string>com.yourname.vault-backup</string>
  <key>ProgramArguments</key> <array>
    <string>/bin/zsh</string><string>-lc</string>
    <string>cd ~/Documents/vault && git add -A && git diff --cached --quiet || git commit -qm "auto $(date +%F-%R)" && git push -q</string>
  </array>
  <key>StartInterval</key>    <integer>3600</integer>
  <key>RunAtLoad</key>        <true/>
  <key>StandardOutPath</key>  <string>/tmp/vault-backup.log</string>
  <key>StandardErrorPath</key><string>/tmp/vault-backup.err</string>
  <key>EnvironmentVariables</key><dict>
    <key>PATH</key><string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
  </dict>
</dict></plist>
```

```sh
# Load (modern syntax; "launchctl load" is deprecated but still works)
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.yourname.vault-backup.plist
# Run it now to test
launchctl kickstart -k gui/$(id -u)/com.yourname.vault-backup
# Status / logs
launchctl print gui/$(id -u)/com.yourname.vault-backup | head -30
tail /tmp/vault-backup.err
# Unload
launchctl bootout gui/$(id -u)/com.yourname.vault-backup
```

Scheduling keys:

- `StartInterval` — every N seconds. If the Mac was asleep, the job runs once on wake (unlike cron, which just skips).
- `StartCalendarInterval` — cron-like: `<dict><key>Hour</key><integer>9</integer><key>Minute</key><integer>0</integer><key>Weekday</key><integer>1</integer></dict>` (Monday 09:00). An array of dicts for multiple times.
- `WatchPaths` — run when any listed path changes (file or directory). `QueueDirectories` — run when a directory is non-empty (a processing queue).
- `KeepAlive` — restart if it exits (a service). `<true/>` or `<dict><key>SuccessfulExit</key><false/></dict>` (restart only on failure). Pair with `ThrottleInterval` to avoid a crash loop.
- `RunAtLoad` — run once when loaded (i.e., at login).
- `StartOnMount` — when a volume mounts (start a backup when the drive is plugged in).

Gotchas: launchd jobs get a minimal environment — **no PATH from your shell**, no `~/.zshrc` — so set `EnvironmentVariables` or use `zsh -lc` (login shell, slower) as above. Jobs that touch protected folders (Desktop, Documents, Downloads, Photos, Mail) will fail silently unless the *executable* (e.g., `/bin/zsh` or your script's interpreter) has been granted **Full Disk Access** in Privacy & Security — prefer putting automated data under `~/code` or `~/.local` to avoid it. Use absolute paths everywhere. `~` is expanded in `ProgramArguments` strings only inside a shell.

Tools: **LaunchControl** ($) is a GUI for writing and debugging plists; **`plutil -lint file.plist`** validates syntax; **`launchd.info`** is the community reference. For one-liners, `brew install --cask launchcontrol` or just copy the template above.

### Homebrew services

`brew services start postgresql@18` writes and loads a launch agent for you. `brew services list` shows all; `brew services run X` starts without registering at login. It's the easiest way to daemonize anything Homebrew installs — including your own formulae.

## AppleScript and JXA

**AppleScript** is the 1990s English-like language for controlling scriptable apps through Apple Events. It looks silly and it is still the only way to reach deep into Finder, Mail, Music, Notes, Calendar, Reminders, Safari tabs, Terminal windows, Keynote, OmniFocus, Things, and most long-lived Mac apps. **JavaScript for Automation (JXA)** exposes the same Apple Events from JavaScript; less documentation, saner language. Both run via `osascript`; both are embeddable in Shortcuts, Hammerspoon, Keyboard Maestro, and Raycast.

Open **Script Editor** (built in) → **File → Open Dictionary** to browse what an app exposes. That's the API reference.

Useful one-liners you'll actually use:

```sh
# Notification
osascript -e 'display notification "Tests passed" with title "pytest" sound name "Glass"'

# Dialog with input, result to stdout
osascript -e 'text returned of (display dialog "Branch name:" default answer "feature/")'

# Frontmost app name
osascript -e 'tell application "System Events" to get name of first process whose frontmost is true'

# URL of the current Safari tab (Chrome: replace app name; "active tab of front window")
osascript -e 'tell application "Safari" to get URL of current tab of front window'

# Every Safari tab URL, for saving a research session
osascript -e 'tell application "Safari" to get URL of every tab of every window' | tr ',' '\n'

# Path of the frontmost Finder window (for a "cd here" alias)
cdf() { cd "$(osascript -e 'tell application "Finder" to POSIX path of (target of front window as alias)')"; }

# Toggle dark mode
osascript -e 'tell application "System Events" to tell appearance preferences to set dark mode to not dark mode'

# Set volume / mute
osascript -e 'set volume output volume 30' ; osascript -e 'set volume output muted true'

# Now-playing from Music
osascript -e 'tell application "Music" to get name of current track & " — " & artist of current track'

# Create a Reminder
osascript -e 'tell application "Reminders" to make new reminder with properties {name:"Submit lab 3", due date:(current date) + 2 * days}'

# Append to a note in Notes
osascript -e 'tell application "Notes" to tell folder "Work" to set body of note "Log" to (body of note "Log") & "<div>'"$(date)"': entry</div>"'

# Empty the Trash, quietly
osascript -e 'tell application "Finder" to empty trash'

# Open a new Terminal/Ghostty window at a path (Ghostty: use `open -na Ghostty --args --working-directory=…`)
osascript -e 'tell application "Terminal" to do script "cd ~/code && ls"'
```

JXA equivalent for the Safari tabs example, showing the syntax:

```js
// save as tabs.js; run with: osascript -l JavaScript tabs.js
const safari = Application("Safari");
const urls = safari.windows().flatMap(w => w.tabs().map(t => t.url()));
console.log(urls.join("\n"));   // goes to stderr; use `urls.join("\n")` as last expression for stdout
```

Where AppleScript beats everything else: **GUI scripting** via System Events — clicking menu items and buttons in apps that expose nothing else (`tell application "System Events" to tell process "Zoom" to click menu item "Mute Audio" of menu "Meeting" of menu bar 1`). It needs **Accessibility** permission for the calling app (Terminal, Script Editor, Hammerspoon) and it's brittle when apps update. Use it as a last resort.

> [!NOTE]
> Since macOS 10.14, the *first* time a script targets an app you'll get an "X wants access to control Y" prompt, recorded under **Privacy & Security → Automation**. Automated scripts (launchd) can't answer prompts — run them interactively once from the same host app so the permission is recorded.

## Automator

Automator (2005) is still installed and still does two things well: **Folder Actions** (run a workflow when files are added to a folder — though macOS 26 Shortcuts triggers now cover this) and **Quick Actions** for Finder/Services with the full list of Automator's file-processing actions (PDF manipulation, image scaling, rename with patterns, "Run Shell Script" with `$@` or stdin). Anything new should be a Shortcut; open Automator if you inherit `.workflow` files or need a PDF action Shortcuts lacks ("Combine PDF Pages", "Extract PDF Text" — actually both exist in Shortcuts now, so mostly: don't).

## Hammerspoon: Lua for everything

**Hammerspoon** (free, open source, `brew install --cask hammerspoon`) exposes macOS — windows, screens, hotkeys, Wi-Fi, USB, battery, audio devices, menu bar items, notifications, pasteboard, timers, app events, Spotlight, AppleScript — as Lua APIs. A single `~/.hammerspoon/init.lua` (put it in your dotfiles) replaces a window manager, a hotkey daemon, a clipboard tool, and half of Keyboard Maestro. It's the automation choice for people who'd rather write 20 lines than drag 20 boxes.

A starter config demonstrating the common patterns:

```lua
-- ~/.hammerspoon/init.lua
local hyper = {"cmd", "alt", "ctrl"}          -- with Karabiner: Caps Lock → hyper (see ch. 5)

-- Reload config on save
hs.pathwatcher.new(os.getenv("HOME") .. "/.hammerspoon/", hs.reload):start()
hs.alert.show("Hammerspoon loaded")

-- 1. App launch/focus hotkeys (the #1 productivity win)
local apps = { t = "Ghostty", e = "Visual Studio Code", b = "Safari", n = "Obsidian", s = "Slack", f = "Finder" }
for key, app in pairs(apps) do
  hs.hotkey.bind(hyper, key, function() hs.application.launchOrFocus(app) end)
end

-- 2. Window management (halves/maximize/center; AeroSpace or Rectangle if you want more)
hs.window.animationDuration = 0
local function move(fn)
  return function()
    local w = hs.window.focusedWindow(); if not w then return end
    local f = w:screen():frame(); w:setFrame(fn(f))
  end
end
hs.hotkey.bind(hyper, "left",  move(function(f) return hs.geometry.rect(f.x, f.y, f.w/2, f.h) end))
hs.hotkey.bind(hyper, "right", move(function(f) return hs.geometry.rect(f.x+f.w/2, f.y, f.w/2, f.h) end))
hs.hotkey.bind(hyper, "return", move(function(f) return f end))
hs.hotkey.bind(hyper, "c", move(function(f) return hs.geometry.rect(f.x+f.w*0.1, f.y+f.h*0.1, f.w*0.8, f.h*0.8) end))
hs.hotkey.bind(hyper, "tab", function() hs.window.focusedWindow():moveToScreen(hs.screen.mainScreen():next()) end)

-- 3. React to events: mute mic + quit Slack when leaving the home Wi-Fi
local homeSSID = "MyHomeWiFi"
hs.wifi.watcher.new(function()
  local ssid = hs.wifi.currentNetwork()
  if ssid ~= homeSSID then
    hs.audiodevice.defaultInputDevice():setInputMuted(true)
    hs.notify.new({title="Left home network", informativeText="Mic muted"}):send()
  end
end):start()

-- 4. Do something when a display is plugged in (rearrange windows, set audio output)
hs.screen.watcher.new(function()
  if #hs.screen.allScreens() > 1 then
    hs.audiodevice.findOutputByName("Studio Display Speakers"):setDefaultOutputDevice()
  end
end):start()

-- 5. Caffeine toggle in the menu bar
local caff = hs.menubar.new()
local function setCaff(state) hs.caffeinate.set("displayIdle", state); caff:setTitle(state and "☕" or "💤") end
caff:setClickCallback(function() setCaff(not hs.caffeinate.get("displayIdle")) end)
setCaff(false)

-- 6. Paste as plain text (⌘⇧V) — strips formatting everywhere
hs.hotkey.bind({"cmd","shift"}, "v", function()
  hs.eventtap.keyStrokes(hs.pasteboard.getContents())
end)

-- 7. Run a shell command and show the result
hs.hotkey.bind(hyper, "g", function()
  local out = hs.execute("cd ~/code/project && git status --short | wc -l", true)
  hs.alert.show("Changed files: " .. out:gsub("%s+", ""))
end)

-- 8. Vim-style arrow keys with hyper held, in every app
for key, arrow in pairs({h="left", j="down", k="up", l="right"}) do
  hs.hotkey.bind(hyper, key, function() hs.eventtap.keyStroke({}, arrow, 0) end, nil,
                            function() hs.eventtap.keyStroke({}, arrow, 0) end)
end
```

The API docs are at `hammerspoon.org/docs`; the **Spoons** repository has drop-in plugins (window grids, clipboard history, a Pomodoro timer, Spotify controls, `URLDispatcher` to route links to different browsers by domain — great for opening work links in Chrome and everything else in Safari). Hammerspoon needs **Accessibility** permission (prompted on first run). Combined with Karabiner mapping Caps Lock to hyper ([chapter 5](05-keyboard-and-input.html)), you get a whole layer of hotkeys that conflict with nothing.

## Keyboard Maestro, BetterTouchTool, and friends

If you'd rather not write Lua:

- **Keyboard Maestro** ($36 one-time) — macros triggered by hotkeys, typed strings, app launch/quit, USB/Wi-Fi/display changes, time, folder changes, MIDI, and more; actions for clicking, typing, menu selection, image-recognition clicks (the "find this button on screen" fallback for un-scriptable apps), AppleScript/shell/JXA/Swift, variables, loops, conditions. The most complete Mac automation tool, with a 20-year track record. The right choice for GUI-heavy automation and text expansion.
- **BetterTouchTool** ($12 / $24 lifetime) — started as trackpad gesture customization (three-finger swipe → action), grew into hotkeys, window snapping, a Touch Bar replacement, and a Stream Deck controller, with a Hammerspoon-ish scripting layer. Best if gestures are what you want to customize.
- **Hazel** ($42) — rule-based folder automation: "when a PDF whose contents match 'Invoice' appears in Downloads, rename it `YYYY-MM-invoice.pdf` and move to `~/Documents/Finance`", "move screenshots older than a week to an archive folder", "unzip and trash archives". Reliable, low-effort. macOS 26 Shortcuts folder triggers do the simple cases; Hazel does content matching and nested rules.
- **Raycast** ([chapter 19](19-daily-driver-apps.html)) — Script Commands (`#!/bin/bash` with metadata comments) become launcher commands; extensions in TypeScript for anything with a UI.
- **Espanso** (free, open source) — text expansion from a YAML file (`:sig` → your signature, `:date` → today, `:shrug` → ¯\\\_(ツ)\_/¯), with forms and shell-command output. Cross-platform. Keyboard Maestro and Raycast Snippets do this too.
- **Alfred Workflows** — the equivalent for Alfred users.
- **Shortcat** / **Homerow** — keyboard-click any UI element by label, for the un-scriptable.

## Folder-driven workflows

Three patterns for "something happens when a file appears":

1. **Shortcuts Automation** (macOS 26): Trigger "Folder" → run actions on the added files. Fine for simple moves/renames.
2. **launchd `WatchPaths`/`QueueDirectories`**: robust, runs without any app open, scriptable in anything. Best for inbox-style processing (`~/Inbox` → script sorts to destinations).
3. **Hazel**: when rules get complicated (content matching, dates, nested conditions) and you don't want to maintain a script.

A useful one: watch `~/Downloads` and unquarantine *nothing* automatically, but move `.dmg`/`.pkg` installers older than 7 days to Trash and screenshots to `~/Pictures/Screenshots`. In launchd form, `WatchPaths` on `~/Downloads` + a script with `find -mtime +7`.

## Scripting languages for glue

- **zsh/bash** for anything under 50 lines. macOS ships `bash` 3.2 (GPLv2 freeze) — write `#!/bin/zsh` or `#!/usr/bin/env bash` with `brew install bash` (5.x) and avoid bash-4 features in `/bin/bash` scripts. BSD `sed`/`awk`/`date`/`stat` differ from GNU (`brew install coreutils gnu-sed` adds `g`-prefixed GNU versions; see [chapter 9](09-terminal-and-shell.html)).
- **Python** for anything longer. `#!/usr/bin/env -S uv run --script` with inline dependencies (PEP 723) makes single-file scripts with packages trivial — see [chapter 11](11-languages-and-runtimes.html). `pyobjc` gives Python access to every macOS framework if you need it.
- **Swift scripts** — `#!/usr/bin/env swift` runs a `.swift` file directly. Slow start (compiles), but full access to AppKit/Foundation. Nice for tiny native utilities; `swift-sh` or a compiled binary for anything hot.
- **JXA** when you need Apple Events and hate AppleScript.
- **Node** — `zx` (Google) makes shell-scripting in JavaScript pleasant if that's your language.

Keep scripts in `~/.local/bin` (on PATH via your `.zshrc`) inside the dotfiles repo ([chapter 10](10-dotfiles-and-git.html)), so every automation you write survives a reinstall.

## Recipes

A few complete, copy-pasteable automations that pay for the chapter.

**Build-done notifier as a shell wrapper** (`~/.local/bin/nt`):

```sh
#!/bin/zsh
# usage: nt make test   — runs the command, notifies with status, plays a sound
start=$(date +%s); "$@"; s=$?; dur=$(( $(date +%s) - start ))
title="${1} $([ $s -eq 0 ] && echo ✅ || echo ❌) (${dur}s)"
osascript -e "display notification \"exit $s\" with title \"$title\""
afplay /System/Library/Sounds/$([ $s -eq 0 ] && echo Glass || echo Basso).aiff &
exit $s
```

**"Morning" Shortcut / script** — run at login via launchd `RunAtLoad`, or as a Shortcut with a Time trigger: open Calendar and Mail, start `brew services run postgresql@18`, pull your dotfiles and course repos (`for d in ~/code/uni/*/; do git -C "$d" pull -q --ff-only; done`), print today's agenda (`icalBuddy eventsToday` via `brew install ical-buddy`).

**Project launcher** (Hammerspoon or Raycast Script Command): `hyper+P` → chooser listing `~/code/*` → opens the pick in your editor, a terminal tab there, and the project's `localhost` URL if `package.json` has a dev script.

**Screenshot pipeline**: `defaults write com.apple.screencapture location ~/Pictures/Screenshots` + a Shortcut Quick Action "Optimize & copy" (Resize to max 1600px → Convert to PNG → Run Shell Script `pngquant` or `oxipng` → Copy to Clipboard) — for pasting into issues and docs at sane sizes.

**Toggle audio output** (Hammerspoon): `hs.audiodevice.allOutputDevices()` cycle on `hyper+A` — headphones ↔ speakers ↔ display without touching Control Center.

**Batch rename with metadata**: `exiftool '-FileName<CreateDate' -d '%Y-%m-%d_%H%M%S%%-c.%%e' ~/Pictures/import/` (`brew install exiftool`) — dated photo filenames; wrap in a Quick Action.

**Clipboard transforms** (Raycast Script Commands or Hammerspoon): JSON pretty-print (`pbpaste | jq . | pbcopy`), Markdown table from TSV, base64 encode/decode, URL-decode, "title case," strip tracking parameters from a URL (`sed -E 's/[?&](utm_[a-z]+|fbclid|gclid)=[^&]*//g'`).

> [!TIP]
> Whatever you automate, put the plist, the Lua, the script, and an exported `.shortcut` in your dotfiles repo with a one-line README entry. Six months from now you won't remember why the Mac beeps at 09:00 on Mondays, and `git log` will.
