<!--
number: 22
part: Part V — Daily driving & workflows
description: A diagnostic playbook for when the Mac misbehaves — the escalation ladder, reading the unified log and crash reports, fixing the classic developer breakages (Homebrew after an OS update, PATH problems, Xcode license, code-signing and Gatekeeper, permissions prompts, DNS, ports in use, Docker), Wi-Fi/Bluetooth/display/audio problems, Recovery mode, Safe Mode, DFU revive, and when a reinstall is actually the answer.
-->
# Troubleshooting

Most Mac problems fall into a dozen buckets, and each bucket has a fast fix. This chapter is organized by *symptom*, with the diagnostic tools first so you can figure out which bucket you're in. It assumes Apple silicon and macOS 26; Intel-specific advice (SMC reset, NVRAM reset, `csrutil` fights) is omitted deliberately because it either doesn't apply or does more harm than good.

> [!TIP]
> **The escalation ladder** — try these in order, stop when fixed: (1) quit and reopen the app, (2) log out and back in, (3) restart, (4) restart in Safe Mode, (5) check for and install updates, (6) create a fresh user account and test there, (7) reinstall macOS *over* the existing installation (keeps data), (8) erase and restore from backup. Steps 1–3 fix 80% of everything; steps 6–7 tell you whether it's your account/config or the OS.

## Diagnostic tools

### Force-quitting and hung apps

- `⌥⌘⎋` — Force Quit dialog. The Finder can be relaunched from here too.
- **Activity Monitor** → select the process → ✕ → Force Quit. Red text = "Not Responding." See [chapter 18](18-performance-and-maintenance.html).
- From the terminal: `pkill -x Slack`, `killall Dock` (restarts the Dock, harmless), `killall Finder`, `killall SystemUIServer`/`ControlCenter` (menu bar glitches), `sudo killall coreaudiod` (audio dropouts), `sudo killall bluetoothd` (Bluetooth), `killall WindowServer` (**logs you out**; fixes graphical corruption).

### The unified log

Everything macOS and most apps do is logged. The **Console** app shows it live (filter by process in the search field, or "Errors and Faults" in the sidebar), but the terminal is faster:

```sh
# Last 5 minutes, errors only
log show --last 5m --predicate 'messageType == error' --style compact

# Everything a specific process said recently
log show --last 30m --predicate 'process == "Finder"' --style compact

# Watch live while you reproduce the problem
log stream --predicate 'process == "Safari" || process CONTAINS "Wi-Fi"' --level info

# Why did the Mac wake / sleep / reboot?
log show --last 24h --predicate 'eventMessage CONTAINS "Wake reason" || eventMessage CONTAINS "Previous shutdown cause"' --style compact
pmset -g log | grep -E "Wake from|Sleep  " | tail -20
```

Shutdown cause codes (in the log after an unexpected restart): `-60` bad filesystem, `-62` watchdog timeout (kernel hang), `-128` unknown, `3` hard power-button shutdown, `5` normal, `-20`/`-30`/`-40` power/thermal. A recurring `-62` or a panic points at a driver/system extension or hardware.

### Crash reports and panics

Crash logs live in `~/Library/Logs/DiagnosticReports/` (your apps) and `/Library/Logs/DiagnosticReports/` (system, panics). Console → **Crash Reports** lists them. Open the newest `.ips`; the first ~40 lines give the process, the exception type, and the thread that crashed — enough to search on or paste into a bug report.

A **kernel panic** ("your computer restarted because of a problem") writes a `Kernel-*.panic` file. The `panicString` names the faulting kext or "watchdog". On Apple silicon, panics are almost always: a third-party system extension (VPN, antivirus, virtualization, audio drivers — check `systemextensionsctl list`), a bad USB/Thunderbolt device or hub, or failing hardware. Unplug everything, uninstall the extension, test.

**Apple Diagnostics** (hardware test): shut down, press and hold the power button until "Loading startup options," then hold `⌘D`. Reference codes: `ADP000` = no issues; `PPT` codes = battery; `VDH` = storage; `NDR`/`NDK` = sensors; `PFR` = firmware. Run this before any Apple Store visit.

### System Information and quick checks

```sh
sw_vers                                   # macOS version/build
system_profiler SPHardwareDataType        # model, chip, memory, serial
system_profiler SPSoftwareDataType        # uptime, boot mode (Safe?), SIP
csrutil status                            # System Integrity Protection: should be enabled
spctl --status                            # Gatekeeper: assessments enabled
fdesetup status                           # FileVault: On
sudo diskutil verifyVolume /              # quick APFS check (full repair from Recovery)
df -h / ; memory_pressure | tail -1      # space, memory
```

## Startup problems

Apple-silicon Macs have one entry point to everything: **shut down, then press and hold the power button** until "Loading startup options" appears. From there:

- **Options → Continue** — **macOS Recovery**: Disk Utility, Reinstall macOS, Restore from Time Machine, Safari, Terminal (Utilities menu), Startup Security Utility, and `resetpassword` from the Terminal. Recovery on Apple silicon is a separate hidden volume; if it's damaged, holding power still gets you to **Fallback Recovery** (`recoveryOS` on a second partition). If *that* fails, the Mac needs DFU revive (below).
- **Your startup disk → hold ⇧ → Continue in Safe Mode** — boots with only Apple kexts/extensions, no login items, caches cleared. If the problem disappears, a third-party login item, extension, or font is the cause. Safe Mode is also the fix for "stuck on the progress bar after an update" (boot Safe once, then restart normally).
- **Startup Security Utility** (in Recovery → Utilities) — Full Security is the default; **Reduced Security** is only needed for legacy kexts or unsigned kernel extensions; leave it at Full unless something you rely on explicitly asks.
- **Boot from an external installer** — create with `sudo /Applications/Install\ macOS\ Tahoe.app/Contents/Resources/createinstallmedia --volume /Volumes/USB` (macOS 26 or 27 as appropriate) and choose it in startup options. Rarely needed on Apple silicon; internet Recovery downloads the current installer.

**Stuck at the Apple logo/progress bar** for more than ~30 minutes: hold power to shut down; boot Safe Mode; if that fails, Recovery → Disk Utility → First Aid on the container and volume; then Reinstall macOS (keeps your data). **Flashing question mark/globe with a prohibition sign**: startup disk not found — Recovery → Disk Utility to check whether the volume exists, then set it via Startup Disk or reinstall.

**Password/login issues**: wrong password on FileVault boot screen after a change — use the *old* password once (the pre-boot cache updates after a successful login). Forgot it: click "?" → reset with Apple Account or the FileVault recovery key (which macOS 26 can now store in iCloud Keychain / the Passwords app — [chapter 16](16-security-and-privacy.html)). Or Recovery → Terminal → `resetpassword`. **Activation Lock** asks for the Apple Account that enabled Find My; there's no bypass — if you bought a used Mac locked to someone else, that's a return.

### DFU revive and restore

If the Mac shows nothing, is stuck in a boot loop, or an update failed at the firmware stage, **Apple Configurator** (Mac App Store) or the **Finder** on macOS 26 can **revive** (reinstall firmware + recoveryOS, keeps data) or **restore** (erases everything) it over a USB-C cable from a second Mac. Cable goes into a specific port (on MacBooks, the port nearest the hinge on the left; on desktops, the Thunderbolt port marked in Apple's support article). Put the Mac in DFU mode with the documented key sequence, connect, and choose Revive first. This replaces the Intel-era Boot Camp/SMC/Internet Recovery rituals; it's the last resort before Apple.

## Developer-environment breakages

### Homebrew after a macOS update

Symptoms: `brew doctor` warnings, "Xcode alert: The Xcode license must be accepted," `Error: Your Command Line Tools are too outdated`, formulae failing to compile with `clang` errors, `git` prompting for CLT installation.

```sh
xcode-select --install                       # reinstall CLT for the new OS (or:)
sudo rm -rf /Library/Developer/CommandLineTools && xcode-select --install
sudo xcodebuild -license accept              # if full Xcode is installed
brew update-reset && brew update && brew doctor
brew upgrade && brew reinstall $(brew list --formula | tr '\n' ' ')   # nuclear, if native libs broke
```

`brew doctor` will complain about "unbrewed" files in `/opt/homebrew`; that's usually harmless. **"Warning: Your Xcode is outdated"** after a major OS update: install the Xcode that matches from the App Store (or `xcodes`). If `brew` itself is missing after an upgrade to macOS 27: the Homebrew prefix `/opt/homebrew` is intact; your shell just lost `eval "$(/opt/homebrew/bin/brew shellenv)"` from a reset `.zprofile` — re-add it ([chapter 8](08-homebrew.html)).

**Rosetta gone after upgrading to macOS 27**: Intel-only apps crash on launch with "You need to install Rosetta" or nothing. `softwareupdate --install-rosetta --agree-to-license`. Then audit: `find /Applications -name "*.app" -maxdepth 2 -exec sh -c 'file "$1/Contents/MacOS/"* 2>/dev/null | grep -q arm64 || echo "$1"' _ {} \;` lists apps with no arm64 slice — replace them before macOS 28, which drops Rosetta for good ([chapter 2](02-first-boot-and-migration.html)).

### "command not found" and PATH

```sh
echo $PATH | tr ':' '\n'      # is /opt/homebrew/bin there, and before /usr/bin?
which -a python3 node git     # every match, in PATH order
type ls                       # alias/function/builtin/file?
```

Common causes: a fresh Terminal profile that runs `bash` instead of `zsh` (`chsh -s /bin/zsh`); `.zshrc` vs `.zprofile` confusion (Homebrew's `shellenv` belongs in `.zprofile`; interactive config in `.zshrc` — [chapter 9](09-terminal-and-shell.html)); `mise` not activated (`eval "$(mise activate zsh)"`); a GUI app (VS Code, Cursor) launched from the Dock inherits the *login* environment, not your shell's — launch from the terminal (`code .`) or set PATH in `.zprofile`/`.zshenv`. `path_helper` (`/etc/zprofile`) reorders PATH on login shells; if your order keeps getting scrambled, prepend in `.zshrc` instead.

### Xcode, simulators, and CLT

- **"xcrun: error: invalid active developer path"** after an update: `xcode-select --install`, or point at Xcode: `sudo xcode-select -s /Applications/Xcode.app`.
- Xcode won't launch/"damaged" after a download: `xattr -dr com.apple.quarantine /Applications/Xcode.app` and let it "verify" (5–10 min on first launch).
- Simulator won't boot: `xcrun simctl shutdown all && xcrun simctl erase all` (wipes simulators), or delete `~/Library/Developer/CoreSimulator/Caches`.
- Disk full: `~/Library/Developer/Xcode/DerivedData` and old runtimes — [chapter 18](18-performance-and-maintenance.html).
- `git` suddenly asks to install CLT even though Xcode exists: `xcode-select -p` shows the path; if it's wrong, `-s` as above.

### Gatekeeper, code signing, and "damaged" apps

- **"App is damaged and can't be opened. You should move it to the Trash"** — nearly always a *quarantine flag on an unsigned/ad-hoc-signed app*, not damage. If you trust the source: `xattr -d com.apple.quarantine /Applications/App.app` (or `-dr` for a folder). Homebrew casks do this automatically when the cask declares it.
- **"Apple could not verify X is free of malware"** — Gatekeeper blocked an unnotarized app. There is no right-click-Open bypass anymore on macOS 26; open **System Settings → Privacy & Security**, scroll to the "was blocked" message, click **Open Anyway** within the hour, authenticate. Or `spctl` doesn't help — the `--add`/`--master-disable` options were removed. See [chapter 16](16-security-and-privacy.html) before doing this for random downloads.
- **Your own compiled binaries are "killed"/"Killed: 9"** — on Apple silicon, all executables must be signed, at least ad-hoc. Compilers do this automatically; if you copy a binary, or `strip`/`lipo`/patch it, re-sign: `codesign -s - -f ./binary`. Same fix for "code signature invalid" on downloaded CLI tools: `codesign -s - -f`, then `xattr -d com.apple.quarantine`.
- **`dyld: Library not loaded`** — a Homebrew dependency was upgraded and the binary links to an old version: `brew reinstall <formula>` (or the tool that broke). For Python packages with native extensions, rebuild the venv.
- **Tools compiled for the wrong architecture**: `file $(which tool)` shows `x86_64` vs `arm64`. An `x86_64` binary needs Rosetta; a Homebrew installed under Rosetta lives in `/usr/local` — you may have two Homebrews. Keep `/opt/homebrew` (arm64) and delete `/usr/local`'s unless you specifically need x86 packages ([chapter 8](08-homebrew.html)).

### Permissions and privacy prompts

- **A CLI tool can't read `~/Documents`, `~/Desktop`, `~/Downloads` and gives `Operation not permitted`** even as root — TCC. Grant the *terminal app* (Ghostty/iTerm/Terminal) **Full Disk Access** in Privacy & Security, or move the data out of protected folders. Scripts run by launchd or cron inherit nothing; the interpreter needs the grant ([chapter 21](21-automation-and-scripting.html)).
- **An app keeps asking for Accessibility/Screen Recording after every update** — apps with changed signatures reset their TCC grant. Remove the app from the list and re-add it. Nuclear: `tccutil reset Accessibility com.example.app` (or `tccutil reset All` for everything — you'll re-approve each prompt).
- **Camera/microphone not working in a browser or Zoom** — Privacy & Security → Camera/Microphone; toggle the app off and on. If the camera is "in use" with no app open: `sudo killall VDCAssistant` (and `AppleCameraAssistant`).
- **"Operation not permitted" writing to `/usr/bin`, `/System`, `/bin`** — SIP + the sealed system volume. You don't. Install to `/usr/local/bin`, `/opt/homebrew/bin`, or `~/.local/bin`.

### Ports, networking, DNS

```sh
# What's listening on port 3000 / who owns it?
lsof -nP -iTCP:3000 -sTCP:LISTEN
sudo lsof -nP -iTCP -sTCP:LISTEN | sort -k9    # everything listening

# Kill whatever holds a port
kill $(lsof -t -iTCP:3000 -sTCP:LISTEN)

# Port 5000 / 7000 taken by "ControlCenter"? That's AirPlay Receiver.
#   System Settings → General → AirDrop & Handoff → AirPlay Receiver → off

# DNS cache flush after editing /etc/hosts or changing resolvers
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder

# Which DNS servers am I actually using?
scutil --dns | grep nameserver | sort -u
# Test resolution the way apps do (not just dig)
dscacheutil -q host -a name example.com

# Network interfaces/routes
ifconfig en0 ; netstat -rn | head ; networksetup -listallhardwareports
```

Notes: `localhost` resolves to both `127.0.0.1` and `::1` — a server bound to IPv4 only will fail from tools that try IPv6 first; bind to `::` or `0.0.0.0` or use `127.0.0.1` explicitly. **`.local` hostnames are mDNS** on macOS; resolving `myserver.local` over unicast DNS won't work (rename the domain or add `/etc/hosts` entries). `*.localhost` subdomains resolve to loopback automatically. **VPN clients** frequently break local DNS and Docker networks; disconnect to test. **Little Snitch/LuLu** silently blocking a new tool looks exactly like "the network is down" for that one process.

### Docker / OrbStack / containers

- **`Cannot connect to the Docker daemon`** — the runtime isn't running (open OrbStack/Docker Desktop) or `docker context ls` points at the wrong one: `docker context use orbstack` (or `desktop-linux`).
- **Images run painfully slowly / "exec format error"** — you pulled an `amd64` image on arm64. Look for an arm64 tag or run with `--platform linux/amd64` (Rosetta-translated; works until macOS 28). Build multi-arch with `docker buildx`.
- **Bind-mounted `node_modules`/file watching slow** — put dependencies in a named volume; OrbStack's VirtioFS is fast, Docker Desktop's is improved but still slower than native. Use `CHOKIDAR_USEPOLLING` only as a last resort.
- **Ports "already allocated"** — an old container: `docker ps -a`, `docker rm -f`. Or AirPlay Receiver (above).
- **Disk full** — `docker system df`, then `docker system prune -a --volumes` ([chapter 18](18-performance-and-maintenance.html)). Docker Desktop's `Docker.raw` doesn't shrink automatically; OrbStack's does.
- Full guidance in [chapter 13](13-containers-and-vms.html).

### Git and SSH

- **`Permission denied (publickey)`** — `ssh -T git@github.com -v` shows which keys were offered. `ssh-add -l` (agent empty after reboot? `AddKeysToAgent yes` + `UseKeychain yes` in `~/.ssh/config`). Wrong key for a second account? `Host github-work` alias with `IdentityFile` + `IdentitiesOnly yes`.
- **Git keeps asking for a password over HTTPS** — `git config --global credential.helper osxkeychain`, or `gh auth login`. A *stale* token: delete the `github.com` entry in **Keychain Access** and retry.
- **`fatal: detected dubious ownership`** — repo on an external drive or copied from another user: `git config --global --add safe.directory /path`.
- **Case-insensitive filesystem surprises** (`Readme.md` vs `README.md` both "exist") — APFS is case-insensitive by default; `git config core.ignorecase false` and fix the names. Or make a case-sensitive APFS volume for code (Disk Utility → + Volume → APFS (Case-sensitive)) — useful for Android/Linux kernel work, otherwise unnecessary.
- **`.DS_Store` committed** — global gitignore ([chapter 10](10-dotfiles-and-git.html)).
- **Commit signing fails after reboot** — `gpg-agent` needs `pinentry-mac` (`brew install pinentry-mac` and `pinentry-program /opt/homebrew/bin/pinentry-mac` in `~/.gnupg/gpg-agent.conf`); or switch to SSH signing (`gpg.format ssh`), which just works with the Keychain.

### Python, Node, and friends

- **`python` not found** — macOS ships `python3` only; make `python` via `mise` or an alias. Never symlink system `python3`.
- **Homebrew Python "externally-managed-environment"** — you tried `pip install` into Homebrew's Python. Use `uv` / venvs ([chapter 11](11-languages-and-runtimes.html)); don't `--break-system-packages`.
- **`EACCES` on `npm install -g`** — Node installed via mise/nvm doesn't need `sudo`; if you see this, your Node is from a system installer. Remove it and use mise.
- **Native module fails to build (`node-gyp`, `psycopg2`, `cryptography`)** — CLT missing or outdated (`xcode-select --install`), or a missing brew library (`brew install postgresql@18 openssl@3` and set `LDFLAGS`/`CPPFLAGS` as `brew info` prints). After an OS update, `rm -rf node_modules && npm ci` / rebuild the venv.
- **Slow shell startup** — `time zsh -i -c exit`; anything over ~300 ms is a plugin manager or `nvm`/`conda` init. Replace `nvm` with `mise`, lazy-load conda, use `zsh-defer` or `zinit`'s turbo mode ([chapter 9](09-terminal-and-shell.html)).

## Hardware and peripherals

### Wi-Fi

1. Toggle Wi-Fi off/on; forget and rejoin the network (System Settings → Wi-Fi → ⓘ → Forget). 
2. `sudo wdutil info` — check RSSI (below −70 dBm is poor), channel, and PHY mode; `wdutil` replaced the removed `airport` tool. Hold ⌥ and click the Wi-Fi menu bar icon for the same info.
3. **Wireless Diagnostics** (⌥-click Wi-Fi icon → Open Wireless Diagnostics → Window → Scan) shows channel congestion; move your router to a clear 5 GHz/6 GHz channel.
4. Change DNS to something not your ISP's (`1.1.1.1`, `9.9.9.9`) in Wi-Fi → Details → DNS; slow page loads with fine speed tests are usually DNS.
5. New Location: System Settings → Network → ⋯ → Locations → Edit → + "Clean" — a fresh network config without deleting anything.
6. Nuclear: with Wi-Fi off, move `/Library/Preferences/SystemConfiguration/{com.apple.airport.preferences.plist,com.apple.network.identification.plist,NetworkInterfaces.plist,preferences.plist}` to the Desktop and reboot. All network settings reset.
7. **Private Wi-Fi Address** ("Rotating") can break MAC-filtered or captive networks (universities) — set to Fixed or Off per network in Wi-Fi → ⓘ.
8. Captive portal not appearing: open `http://captive.apple.com` in a browser.

### Bluetooth

Turn off/on; remove and re-pair the device; `sudo pkill bluetoothd`. Keyboard/mouse lag in a crowded 2.4 GHz area: use a 5 GHz Wi-Fi network (Bluetooth shares the 2.4 GHz band), unplug USB 3 hubs near the Mac (they emit 2.4 GHz interference — a documented Apple issue), or use the vendor's dongle. If Bluetooth is entirely missing from Settings after an update: shut down fully (not restart), wait 30 seconds, boot.

### External displays

- **Blurry text on a 1080p/1440p monitor** — macOS drops sub-pixel AA; low-DPI panels look soft. Use a "Retina-class" (≥ 4K at 27") monitor for a crisp experience, or **BetterDisplay** to enable HiDPI scaled resolutions on lower-res panels ([chapter 19](19-daily-driver-apps.html)).
- **Not detected** — check the cable (HDMI 2.1 or DP 1.4 capable; many cheap USB-C cables are USB 2.0 only with no video), the port (base M-series Macs support a limited number of external displays — check your model's spec), and try **System Settings → Displays → Detect Displays** (hold ⌥ to reveal). DisplayLink docks need their driver (Screen Recording permission) and have lag; prefer Thunderbolt docks with native DP alt-mode.
- **Wrong refresh rate / HDR / color** — Displays → Advanced; set 60 Hz+ explicitly; disable HDR on monitors with poor HDR (most). "Flashing"/black-outs on a hub usually mean bandwidth — plug the display directly.
- **Windows rearrange every time you dock** — macOS remembers arrangements by display identity; use a window manager restore (Rectangle "restore," AeroSpace, or a Hammerspoon `hs.screen.watcher` — [chapter 21](21-automation-and-scripting.html)).
- **Brightness keys don't work on external** — `MonitorControl` (DDC/CI). Not possible over some DisplayLink docks.

### Audio

No sound / wrong device after unplugging headphones: **Control Center → Sound** to pick the output; `sudo killall coreaudiod` to restart the audio daemon. Crackling on USB DACs/interfaces: **Audio MIDI Setup** → set the sample rate to match (48 kHz), disable "Hog mode" apps. Bluetooth headphones' mic drops quality to phone-call codec — that's the Bluetooth standard, not a bug; use the Mac's mic for calls and headphones for output (pick separately in Sound settings, or via **Audio MIDI Setup → Create Aggregate Device**).

### Keyboard, trackpad, Touch ID

Repeated keys or missed keys: **Keyboard → Key repeat / Delay**; `defaults write -g ApplePressAndHoldEnabled -bool false` if holding a key shows accents instead of repeating ([chapter 5](05-keyboard-and-input.html)). Karabiner stopped working after an update: re-approve its driver extension in Privacy & Security → Login Items & Extensions → Driver Extensions, and Input Monitoring. Touch ID not offered for `sudo`: the PAM line was reset by the update — use `/etc/pam.d/sudo_local` which survives updates ([chapter 9](09-terminal-and-shell.html)). Trackpad erratic: dirt/moisture; or a swelling battery underneath (a hardware issue — stop and get it checked if the trackpad clicks poorly or the case bulges).

### USB, Thunderbolt, and storage

Drives not mounting: `diskutil list` (is it there?), `diskutil mount diskNsM`, Disk Utility → First Aid. NTFS drives are read-only on macOS by default — copy off, or reformat as exFAT for cross-platform. "Disk not ejected properly" on sleep: turn off "Put hard disks to sleep" in Battery/Energy settings, or use a powered hub. A device that kernel-panics the Mac when plugged in is a bad device or cable — replace it, don't debug it.

### Battery and charging

Not charging on a USB-C hub: the hub passes less wattage than the Mac wants; plug the charger directly. "Not charging" at 80% with the charge limit or Optimized Charging on is by design ([chapter 18](18-performance-and-maintenance.html)). Sudden battery drain: Activity Monitor → Energy → 12 hr Power; Wi-Fi/Bluetooth scanning in sleep (turn off "Wake for network access"); a stuck `mds` index; a browser tab with a video. `pmset -g assertions` while it should be asleep.

## macOS itself

- **Settings won't stick / apps reset preferences** — `cfprefsd` cache: `killall cfprefsd`, or the app's plist is corrupt: `defaults delete com.vendor.app` (loses prefs) after backing up with `defaults export`.
- **Finder slow / "The application Finder is not open"** — `killall Finder`; if persistent, delete `~/Library/Preferences/com.apple.finder.plist` and relaunch. Slow opening of a folder with thousands of items: switch to List view, disable icon previews and "Calculate all sizes."
- **Spotlight not finding things** — `sudo mdutil -E /` ([chapter 18](18-performance-and-maintenance.html)).
- **Notification Center/Dock/menu bar glitching** — `killall Dock`, `killall NotificationCenter`, `killall ControlCenter`.
- **Font problems, garbled text in one app** — Font Book → File → Validate Fonts; remove duplicates. Safe Mode clears font caches.
- **Time Machine "preparing backup" forever** — [chapter 17](17-backup-and-recovery.html): `tmutil stopbackup`, remove the `.inProgress` bundle on the destination, restart.
- **"Your system has run out of application memory"** — a leaking app; Activity Monitor → Memory sorted by Memory; Force Quit the top one. Chronic → more RAM or fewer Electron apps ([chapter 18](18-performance-and-maintenance.html)).
- **Liquid Glass makes text hard to read** — Accessibility → Display → Reduce Transparency, or the Liquid Glass intensity slider in Appearance on macOS 27 ([chapter 3](03-system-settings.html)).
- **Software Update fails / "unable to check for updates"** — free space ≥ 20 GB? `sudo softwareupdate -l --verbose`; try from Recovery (Reinstall macOS keeps data and applies the update); check `/var/log/install.log`.
- **iCloud sync stuck** — `brctl log --wait --shorten` shows the sync daemon live; often a single file with an illegal name or a huge one. `killall bird` (iCloud Drive daemon) restarts sync.

## When to reinstall, when to go to Apple

**Reinstall macOS (keep data)** — Recovery → Reinstall macOS. It replaces the system volume only; apps, files, and settings stay. Do this when: Safe Mode fixes things but you can't find the culprit, system daemons crash-loop, updates fail repeatedly. Takes 30–60 minutes. It's not the ritual it was on Intel; it's a reasonable step 7.

**Erase and set up fresh** — Recovery → Disk Utility → erase the container (or System Settings → General → Transfer or Reset → **Erase All Content and Settings**, which is much faster and keeps the OS). Restore *selectively* from Time Machine or your dotfiles/Brewfile rather than Migration Assistant if you're doing this to escape accumulated cruft ([chapter 2](02-first-boot-and-migration.html), [Appendix A](appendix-a-bootstrap-script.html)).

**Apple / authorized service** — Apple Diagnostics reports a code; the Mac panics with all peripherals unplugged and no third-party extensions; battery "Service Recommended"; liquid damage; the trackpad bulges; the display flickers in Recovery too (which rules out software). Book a Genius Bar or mail-in via the **Apple Support** app. Have a current backup and your Apple Account password; they will ask you to disable Find My / Activation Lock. AppleCare+ covers accidental damage with a deductible; the standard warranty is one year (two in the EU, plus consumer law).

## Getting help

When you ask a question, include: `sw_vers -productVersion`, the Mac model and chip (`system_profiler SPHardwareDataType | grep -E "Model Name|Chip|Memory"`), the exact error text (copy from the terminal or Console, not a photo), what changed recently (updates, new apps, new hardware), and whether Safe Mode / a fresh user account reproduces it. Good places: the app's own GitHub issues, `discussions.apple.com` for OS bugs, `apple.stackexchange.com`, r/MacOS and r/macsysadmin, the Homebrew discussions for anything brew-related, and Apple's Feedback Assistant (`applefeedback://`) for genuine OS bugs — they do read it, and it's the only channel that reaches engineering.
