<!--
number: 18
part: Part IV — Security, backup & maintenance
description: Keeping a Mac fast for years — reading Activity Monitor and memory pressure correctly, reclaiming storage (System Data, caches, Docker, Xcode, Homebrew), auditing login items and launch agents, battery health and the 80% charge limit, thermals, Spotlight reindexing, and a low-effort maintenance routine.
-->
# Performance & maintenance

Apple-silicon Macs don't slow down the way Intel machines did — there's no spinning disk to fragment, no registry to rot, and macOS manages memory aggressively. What *does* go wrong is predictable: the disk fills up with build artifacts and container images, something you installed once runs at login forever, a runaway process eats a core in the background, and the battery gets cooked by living at 100% on a desk. This chapter covers how to *read* what the machine is doing, then how to fix the handful of things that actually matter.

> [!TIP]
> **The 80/20 of Mac maintenance:** (1) keep ≥15% of the disk free, (2) audit login items twice a year, (3) turn on the charge limit if the Mac lives plugged in, (4) reboot when the uptime passes a couple of weeks. Everything else in this chapter is diagnosis for when something feels wrong.

## Reading Activity Monitor correctly

Open Activity Monitor (`⌘Space` → "Activity"), or pin it to the Dock during setup week. Five tabs, each with one thing that matters:

| Tab | Look at | Ignore |
|---|---|---|
| **CPU** | `% CPU` sorted descending; anything sustained >100% that isn't a build or a video call. The **Idle** number at the bottom (>80% at rest is normal). | Short spikes; `kernel_task` high *while the Mac is hot* is the OS throttling on purpose. |
| **Memory** | The **Memory Pressure** graph. Green = fine, yellow = fine but compressing, red = you're swapping hard. | "Memory Used" — macOS uses all RAM it can as cache; a "full" number is not a problem. |
| **Energy** | **Energy Impact** and **12 hr Power**; the culprits when battery life suddenly drops. Also **Preventing Sleep**. | Absolute numbers — only relative ranking matters. |
| **Disk** | **Bytes Written** over time for processes you don't expect (Spotlight `mds_stores` after a big copy is normal for an hour). | Reads. |
| **Network** | Sent/received bytes by process; find the cloud-sync app re-uploading 40 GB. | — |

Useful, non-obvious features:

- **View → All Processes, Hierarchically** shows which parent spawned that mystery `node` process.
- **View → Dock Icon → Show CPU History** turns the Dock icon into a live graph.
- Select a process → **ⓘ** → **Sample Process** gives you a stack dump you can paste into a bug report (or feed to an AI assistant) to figure out what a hung app is doing.
- `⌥⌘⎋` (Force Quit dialog) is the fast path when a GUI app is stuck; Activity Monitor's ✕ button does the same with more information.

### Memory pressure, unified memory, and "do I need more RAM?"

On Apple silicon the CPU and GPU share one pool of memory. macOS will happily *use* all of it — file cache, compressed pages, GPU buffers — so the raw "used" number is meaningless. Three signals actually indicate a RAM shortage:

1. **Memory Pressure is yellow or red for minutes at a time**, not just during a build.
2. **Swap Used** grows into multiple gigabytes and stays there. A little swap is normal; 8–10 GB of swap on a 16 GB machine means the working set doesn't fit.
3. Apps visibly stall for a second when you switch to them (pages being decompressed or read back from SSD).

From the terminal:

```sh
# Pressure and swap in one line each
memory_pressure | tail -1
sysctl vm.swapusage

# Top 10 processes by resident memory
ps -axm -o rss,comm | head -11 | awk 'NR>1{printf "%6.0f MB  %s\n",$1/1024,$2}'

# Live view (q to quit)
top -o mem -stats pid,command,mem,cpu
```

Rules of thumb for 2026 workloads (see [chapter 1](01-hardware-and-buying.html) for the buying angle):

- **8 GB (MacBook Neo):** fine for editors, browsers, and one language runtime. Docker/OrbStack with a database plus a JVM plus Chrome will swap constantly.
- **16 GB:** the comfortable floor for a CS student or web developer. Watch pressure when running containers *and* an Android/iOS simulator.
- **24–36 GB:** local LLMs up to ~20B parameters at 4-bit, Kubernetes-in-Docker, multiple VMs, big monorepos indexed by an IDE.
- **48 GB+:** ML work, 70B-class models, video.

You can't upgrade RAM later. If you're swapping every day, the fix is to reduce the working set (quit Docker when not using it, use one browser, close the IDE you're not using), not to "clean memory" with a utility — those apps just purge the cache macOS would have dropped anyway.

## Storage: where the space went

APFS reports free space in a confusing way because snapshots, purgeable files, and clones make "used" fuzzy. Start with the two views macOS gives you, then go to the terminal.

**System Settings → General → Storage** gives category totals. The category that confuses everyone is **System Data** (formerly "Other"): it's caches, logs, Time Machine local snapshots, container disk images, Xcode simulators, and anything macOS can't classify. It legitimately reaches 30–100 GB on a developer machine.

From the terminal, find the real culprits:

```sh
# Top-level usage of your home folder, largest first (takes a minute)
du -xhd1 ~ 2>/dev/null | sort -rh | head -20

# Same for Library, where most "System Data" lives
du -xhd1 ~/Library 2>/dev/null | sort -rh | head -20

# Interactive drill-down (install once: brew install dust  or  brew install ncdu)
dust -d 2 ~
ncdu ~
```

Or use a GUI: **GrandPerspective** (free, treemap), **DaisyDisk** ($10, prettier, can scan hidden system volumes), or **OmniDiskSweeper** (free, plain list). All three are in the [Brewfile](appendix-b-brewfile.html).

### The usual suspects on a developer Mac

| Location | What | Safe cleanup |
|---|---|---|
| `~/Library/Developer/Xcode/DerivedData` | Xcode build intermediates | Delete the whole folder anytime; Xcode rebuilds. Often 10–50 GB. |
| `~/Library/Developer/Xcode/iOS DeviceSupport`, `.../Archives` | Symbols for every iOS version you ever plugged in; app archives | Delete old versions; keep archives you've shipped. |
| `~/Library/Developer/CoreSimulator` | Simulator runtimes and device images | `xcrun simctl delete unavailable`; Xcode → Settings → Components to remove old runtimes (5–8 GB each). |
| `~/.orbstack` / `~/Library/Containers/com.docker.docker` | Container images, volumes, build cache | `docker system prune -a --volumes` (destroys stopped containers and unused volumes — read the prompt). OrbStack: Settings → Storage. |
| `~/Library/Caches` | App caches | `brew cleanup --prune=all`; otherwise let apps manage it. Deleting the folder is safe but they regrow. |
| `~/Library/Caches/Homebrew`, `$(brew --cache)` | Downloaded bottles | `brew cleanup -s` |
| `~/.cache`, `~/.npm/_cacache`, `~/.cache/uv`, `~/.cargo/registry`, `~/.m2`, `~/.gradle/caches`, `~/go/pkg/mod` | Package manager caches | `npm cache clean --force`, `uv cache clean`, `cargo cache -a` (via `cargo install cargo-cache`), `go clean -modcache`, delete Gradle caches. |
| `node_modules` folders everywhere | Dependencies for projects you finished in 2024 | `npx npkill` walks your projects and lets you delete them interactively. |
| `~/.local/share/mise`, `~/.pyenv`, `~/.nvm` | Old runtime versions | `mise prune` / `mise uninstall`. |
| `~/Library/Application Support/Code/User/workspaceStorage` | VS Code per-workspace caches | Safe to delete when VS Code is closed. |
| `~/Library/Application Support/Slack/Cache`, Teams, Discord, Spotify | Electron media caches, often 2–5 GB each | Delete from inside the app (Spotify → Settings → Storage) or trash the Cache folder while quit. |
| `~/Library/Mail` | Offline copies of every attachment | Mail → Settings → Accounts → Download Attachments: Recent. |
| `~/Library/Messages/Attachments` | Every photo anyone ever texted you | System Settings → Storage → Messages → review large attachments. |
| `~/Downloads` | You know | Sort by size. A Hazel or Shortcuts rule to archive files older than 30 days helps. |
| Local Time Machine snapshots | Hourly snapshots when the backup drive is unplugged | `tmutil listlocalsnapshots /` then `tmutil deletelocalsnapshots <date>`; macOS purges them itself when space gets low. |

A one-shot cleanup you can run monthly (also in [Appendix A](appendix-a-bootstrap-script.html) as `scripts/cleanup.sh`):

```sh
#!/bin/sh
set -eu
echo "→ Homebrew";      brew cleanup --prune=all -s; brew autoremove
echo "→ Xcode";         rm -rf ~/Library/Developer/Xcode/DerivedData/*; xcrun simctl delete unavailable 2>/dev/null || true
echo "→ Docker";        command -v docker >/dev/null && docker system prune -f 2>/dev/null || true
echo "→ npm/uv/go";     npm cache clean --force 2>/dev/null; uv cache clean 2>/dev/null; go clean -modcache 2>/dev/null || true
echo "→ mise";          command -v mise >/dev/null && mise prune -y || true
echo "→ Trash";         rm -rf ~/.Trash/* 2>/dev/null || true
echo "→ Snapshots";     tmutil listlocalsnapshots / | sed 's/.*\.//' | xargs -I{} tmutil deletelocalsnapshots {} >/dev/null 2>&1 || true
df -h / | tail -1
```

> [!WARNING]
> Never `rm -rf` inside `/System`, `/Library` (root-level), or `/private/var/db`. On a sealed system volume you mostly can't, but the parts you *can* touch (`/Library/Caches`, `/private/var/folders`) are managed by the OS and deleting them by hand causes odd breakage until the next reboot. Use `sudo periodic daily weekly monthly` if you want the OS to run its own cleanups, though on modern macOS it's largely a no-op.

### Purgeable space and why `df` disagrees with Finder

Finder shows *available* space including **purgeable** items — local snapshots, iCloud-evicted files, caches macOS knows it can drop. `df -h` shows what's actually free right now. When you're installing something big and get "not enough space" despite Finder saying otherwise, the OS hasn't purged yet. Force it by trying the copy anyway (macOS purges on demand), or delete snapshots as above.

Check the state of your APFS container:

```sh
diskutil apfs list | grep -E "Capacity (In Use|Not Allocated)|Name"
```

### Keep 15% free

APFS and SSD wear-leveling both want headroom. Below ~10% free, writes slow down, Time Machine local snapshots get purged constantly, and Xcode/Docker start failing in confusing ways. If you're routinely below that, the fix is an external SSD for media and project archives (see [chapter 17](17-backup-and-recovery.html)) or an honest look at whether you need three container runtimes.

## Login items and background processes

Every app you install wants to run at login. Six months in, a fresh Mac has 25 things starting before you type a password. This is the single biggest cause of "my Mac got slow."

**System Settings → General → Login Items & Extensions.** Two lists:

- **Open at Login** — full apps. Remove anything you don't need running the moment you sit down. Keep: password manager, clipboard manager, window manager, your launcher. Question: Slack, Discord, Spotify, cloud-sync clients you use weekly, every "helper" from a printer or webcam vendor.
- **Allow in the Background** — launch agents and daemons registered by apps. Toggling one off disables the agent without deleting it. Turn off anything from an app you uninstalled (macOS shows the developer name; if it's unfamiliar, search for it).

The terminal view is more complete. Agents live in five places:

```sh
# Per-user agents (apps you installed)
ls -la ~/Library/LaunchAgents
# System-wide agents/daemons installed by third-party apps (needs the app's installer or sudo)
ls -la /Library/LaunchAgents /Library/LaunchDaemons
# Apple's own — leave alone
# /System/Library/LaunchAgents /System/Library/LaunchDaemons

# What's currently loaded for your user, with PID and last exit status
launchctl list | sort -k3

# Everything with a non-zero exit code (crashing agents that relaunch forever)
launchctl list | awk '$2 != 0 && $2 != "-"'
```

To remove one properly:

```sh
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.example.helper.plist
rm ~/Library/LaunchAgents/com.example.helper.plist
```

Also check **Login Items → Extensions** for Finder Sync, Quick Look, Share, and Spotlight extensions from uninstalled apps; each one is a process that gets loaded on demand.

> [!NOTE]
> Homebrew services (`brew services list`) are launch agents too — `postgresql`, `redis`, `mysql` running at login are exactly the kind of thing you forget about. `brew services stop --all` before travel, or don't autostart databases at all and run `brew services run postgresql@18` when you need them (see [chapter 15](15-databases-and-local-dev.html)).

## Uninstalling properly

Dragging an app to the Trash leaves preferences, caches, launch agents, and sometimes a privileged helper behind. For most apps the leftovers are a few KB of plists and harmless. For anything that installed a kernel/system extension, a VPN, an agent, or a helper (Docker Desktop, antivirus, Adobe, Logitech/Razer software, old Zoom versions), use the vendor's uninstaller or a cleaner:

- `brew uninstall --zap <cask>` — Homebrew's zap stanza deletes the app *and* its known support files. This is the strongest argument for installing GUI apps via casks.
- **AppCleaner** (free) or **Pearcleaner** (free, open source) — drop an app in, see the associated files, delete them together.
- Check **System Settings → General → Login Items & Extensions → Extensions** and **Privacy & Security** for orphaned system extensions; `systemextensionsctl list` in the terminal.

## Battery health

Lithium-ion batteries age by **cycle count** and by **time spent at high charge and high temperature**. A Mac that lives on a desk at 100% and 35 °C degrades faster than one that's cycled daily.

Check the state: **System Settings → Battery → Battery Health (ⓘ)** shows Maximum Capacity and cycle count. `system_profiler SPPowerDataType | grep -E "Cycle Count|Condition|Maximum Capacity"` from the terminal. Apple rates batteries for 1,000 cycles to 80% capacity; "Service Recommended" appears below 80%.

Settings that matter:

- **Optimized Battery Charging** (on by default) learns your schedule and holds at 80% until shortly before you usually unplug. Leave it on.
- **Charge limit (80%)** — new in macOS 26.4 for Apple-silicon laptops: **System Settings → Battery → Charge Limit**. If the Mac is docked most of the week, set this. It's the biggest single thing you can do for long-term health. Toggle it off for a travel day (the menu bar battery item has a "Charge to Full Now" shortcut).
- **Low Power Mode** — Battery → Low Power Mode → "Only on Battery" caps performance modestly and can add 1–2 hours. Fine for note-taking days; turn off for builds.
- **Energy Mode** (M-series Pro/Max only) — "High Power" pins the fans up for sustained loads; "Low Power" the opposite. Automatic is right almost always.

Third-party options: **AlDente** ($) gives finer control (arbitrary limits, heat protection, sailing mode) and was the only way to do this before 26.4; **coconutBattery** (free) shows detailed history. Both are in the Brewfile as optional.

Battery *life* problems (not health) are almost always software: check Activity Monitor → Energy sorted by 12 hr Power, and look for **Preventing Sleep: Yes** on something like a browser tab with a video call it thinks is still open. `pmset -g assertions` lists what's holding the Mac awake right now.

```sh
# Who's keeping the Mac awake?
pmset -g assertions | grep -iE "PreventUserIdleSystemSleep|PreventUserIdleDisplaySleep" -A2

# Battery/charging log with wake reasons (find the 3 AM wakeups)
pmset -g log | grep -E "Wake Requests|DarkWake|Sleep  " | tail -30
```

## Thermals and fan noise

Apple-silicon Macs throttle gracefully: when they get hot, `kernel_task` appears to use a lot of CPU — that's the scheduler stealing cycles to cool down, not a bug. MacBook Air has no fan and will throttle under sustained load (long compiles, ML training); that's the trade-off you accepted for silence.

To reduce heat:

- Keep the intake vents (hinge area on MacBooks) unobstructed. A stand helps more than any software.
- Sustained 100% CPU from something that *shouldn't* be busy (Spotlight after a migration, a cloud sync client, a runaway Electron app) is the usual cause of a hot idle Mac — Activity Monitor → CPU.
- **Stats** or **iStat Menus** ($) in the menu bar show temperature and fan speed. `sudo powermetrics --samplers smc -i 1000 -n 1` prints die temperatures and fan RPM from the terminal.
- Don't install fan-control software unless you know why. Macs Fan Control can force fans on early, which is fine, but the defaults are already tuned.

## Spotlight and indexing

Spotlight (`mds`, `mds_stores`, `mdworker`) indexes every file change. It runs hot for an hour after a migration, big `git clone`, or Xcode install — that's normal. If Spotlight is *constantly* busy, or search results are wrong or missing, rebuild the index:

```sh
# Check indexing status
mdutil -s /

# Rebuild (takes 10–60 minutes; search is degraded meanwhile)
sudo mdutil -E /

# Stop indexing an external drive entirely
sudo mdutil -i off /Volumes/Backup
```

Exclude build output from indexing to reduce churn: **System Settings → Spotlight → Search Privacy** (or Spotlight → Privacy on older versions) and add `~/code` (or specifically `node_modules`, `target`, `.build` — Spotlight doesn't do globs, so add the folders or accept indexing them). Many developers exclude their entire code directory and rely on the editor's search and `fd`/`rg` instead. Time Machine has a separate exclusion list (see [chapter 17](17-backup-and-recovery.html)).

> [!TIP]
> Alternative launchers (Raycast, Alfred) use Spotlight's metadata index for file search. If you turned indexing off to save CPU, file search in those breaks too.

## Updates

- **macOS updates**: System Settings → General → Software Update. Turn on **Install Security Responses and system files** (background security patches). For feature updates, waiting a week or two after release is reasonable on a machine you depend on; security updates (26.6 fixed 155 CVEs) should not wait. See the [security chapter](16-security-and-privacy.html).
- **App Store apps**: automatic updates on.
- **Homebrew**: `brew update && brew upgrade && brew cleanup` weekly, or `brew upgrade --greedy` to include casks with their own auto-updaters. Pin anything you can't afford to have change: `brew pin postgresql@18`.
- **Casks with auto-updaters** (Chrome, VS Code, Slack, Zoom) update themselves; `brew upgrade` skips them unless `--greedy`.
- **Runtimes**: `mise upgrade` for tool versions, `mise self-update` for mise itself (or via brew).
- **Global npm/pip/cargo installs**: the fewer the better. `npm outdated -g`, `uv tool upgrade --all`, `cargo install-update -a` (via `cargo-update`).

Reboot after macOS updates, obviously, but also reboot every couple of weeks regardless. `uptime` shows how long it's been; leaked memory in WindowServer and a dozen helper processes recovers nothing else.

## A maintenance routine that fits in five minutes

**Weekly (Friday, before closing the lid):**

```sh
brew update && brew upgrade && brew cleanup
mise upgrade
uptime   # >14 days? reboot
df -h /  # <15% free? run cleanup.sh
```

**Monthly:**

- Run `scripts/cleanup.sh` (above).
- Glance at **Login Items & Extensions**; remove anything new you don't recognize.
- Check Time Machine ran in the last 24 hours (menu bar icon or `tmutil latestbackup`).
- **Battery Health**: note cycle count; if the Mac was docked all month and the limit is off, turn it on.

**Every semester / quarter:**

- `brew bundle cleanup` to see what's installed that's not in your Brewfile — decide whether to add it or remove it (see [chapter 8](08-homebrew.html)).
- `npx npkill` and `docker system prune -a` for abandoned projects.
- Review **Privacy & Security** permissions (Full Disk Access, Screen Recording, Accessibility) and revoke stale ones.
- Check macOS version against Apple's currently-supported list; if you're on an N-2 release, plan the upgrade.
- Test a restore from backup — open a file from Time Machine you haven't touched in months.

**Things you don't need to do:**

- "Repair permissions" — hasn't existed since El Capitan.
- Reset SMC/NVRAM — Apple silicon manages this itself; the old key combos don't exist. If someone tells you to, they're reading a 2015 article.
- Run a "cleaner" or "optimizer" app. CleanMyMac and its clones do the same things as the commands above with a subscription attached, and their background agents are themselves a login-item problem. The one useful thing they do — finding large old files — GrandPerspective does for free.
- Defragment. APFS on SSD; no.
- Reinstall macOS annually. If the machine feels slow, it's one of: disk space, login items, a runaway process, or a battery that needs the charge limit. Find which.

## When it's actually slow: a diagnostic order

1. `uptime` — over two weeks? Reboot first, then re-evaluate.
2. `df -h /` — under 10% free? Fix that.
3. Activity Monitor → **CPU**, sort by % CPU. Anything sustained above 100% that isn't yours? Sample it, quit it, find why it's running (login items).
4. Activity Monitor → **Memory**, look at pressure. Red? Quit Docker/IDE/browser you aren't using; consider whether you bought enough RAM.
5. Activity Monitor → **Disk**, sort by Bytes Written. Spotlight or a sync client thrashing?
6. `pmset -g thermlog` (or `sudo powermetrics`) — throttled from heat? Clear the vents, close the tab with the WebGL demo.
7. Boot into **Safe Mode** (hold power → Options → hold ⇧ while choosing the volume) — if it's fast there, a third-party login item or extension is the cause. Binary-search the Login Items list.
8. Still slow? [Chapter 22](22-troubleshooting.html) covers logs, Recovery, and when to reinstall.
