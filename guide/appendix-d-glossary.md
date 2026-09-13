<!--
number: D
part: Part VI — Reference
description: Plain-English definitions of the macOS, Apple-silicon, and developer-tooling terms used throughout the guide — from APFS and Activation Lock to XProtect and zsh — with pointers to the chapter that goes deeper.
-->
# Appendix D — Glossary

Alphabetical. Bold terms are defined elsewhere in this list. Chapter references point to where the concept matters in practice.

**Activation Lock** — Anti-theft tie between a Mac and the Apple Account that enabled Find My. A locked Mac can't be erased and reactivated without that account's credentials. Automatic when Find My is on. → [ch. 16](16-security-and-privacy.html)

**ad-hoc signing** — A code signature with no developer identity (`codesign -s -`). Apple silicon requires *every* executable to be signed at least ad-hoc; compilers do it automatically. Ad-hoc-signed apps trip **Gatekeeper** when downloaded. → [ch. 22](22-troubleshooting.html)

**AeroSpace** — Open-source i3-style tiling window manager for macOS that doesn't need Accessibility hacks or SIP changes. → [ch. 6](06-window-management.html)

**agent (launch agent)** — A **launchd** job that runs as your user when you're logged in (`~/Library/LaunchAgents`). Compare **daemon**. → [ch. 21](21-automation-and-scripting.html)

**AirPlay Receiver** — macOS feature that listens on ports 5000 and 7000 and collides with dev servers. Turn off in AirDrop & Handoff settings. → [ch. 22](22-troubleshooting.html)

**APFS** — Apple File System (2017). Copy-on-write, snapshots, clones, native encryption, space-sharing volumes inside a **container**. Case-insensitive by default. → [ch. 17](17-backup-and-recovery.html), [ch. 18](18-performance-and-maintenance.html)

**Apple Account** — Formerly Apple ID. Your identity for iCloud, App Store, Find My, Activation Lock, and the FileVault recovery-key escrow option.

**Apple Intelligence** — Apple's on-device + **Private Cloud Compute** AI features: Writing Tools, Siri answers in Spotlight, Shortcuts "Use Model" action, Visual Intelligence. Requires M1+ and 8 GB.

**Apple silicon** — Apple's ARM64 system-on-chip family (M1–M6, A18 Pro in the MacBook Neo). **Unified memory**, integrated GPU/Neural Engine, no upgradeable RAM. macOS 27 runs *only* on Apple silicon. → [ch. 1](01-hardware-and-buying.html)

**arm64 / aarch64** — The 64-bit ARM instruction set Apple silicon executes natively. Contrast **x86_64**. Also the Docker platform string `linux/arm64`.

**Automator** — 2005-era visual automation app; mostly superseded by **Shortcuts**, still useful for Quick Actions and legacy `.workflow` files. → [ch. 21](21-automation-and-scripting.html)

**Brewfile** — A `brew bundle` manifest listing formulae, casks, `mas` apps, and VS Code extensions. → [ch. 8](08-homebrew.html), [Appendix B](appendix-b-brewfile.html)

**cask** — A Homebrew package that installs a GUI app (or font, or driver) rather than a CLI tool: `brew install --cask ghostty`. → [ch. 8](08-homebrew.html)

**Cellar** — Where Homebrew keeps installed formula versions (`/opt/homebrew/Cellar/<name>/<version>`), symlinked into `/opt/homebrew/bin`.

**chezmoi / stow** — Dotfile managers. GNU Stow symlinks a repo's tree into `~`; chezmoi templates and encrypts per-machine. → [ch. 10](10-dotfiles-and-git.html)

**CLT (Command Line Tools)** — Apple's ~1 GB package with `clang`, `git`, `make`, `lldb`, SDK headers; installed by `xcode-select --install`. Enough for most development without the 12 GB Xcode. → [ch. 7](07-command-line-tools-and-xcode.html)

**Compose** — Docker's multi-container spec (`compose.yaml`). Apple's `container` tool doesn't support it; OrbStack and Docker Desktop do. → [ch. 13](13-containers-and-vms.html)

**container (Apple)** — Apple's open-source `container` CLI (1.0 in 2025) that runs each Linux container in its own lightweight VM using the **Virtualization framework**. Fast and secure; no Compose, smaller ecosystem than Docker. → [ch. 13](13-containers-and-vms.html)

**container (APFS)** — The partition-level object inside which APFS volumes share space. `diskutil apfs list`.

**Continuity / Handoff / Universal Control / Sidecar** — Apple's cross-device features: pick up tasks across devices, use one keyboard/mouse across a Mac and iPad, use an iPad as a display.

**daemon (launch daemon)** — A **launchd** job that runs as root at boot, before any login (`/Library/LaunchDaemons`). → [ch. 21](21-automation-and-scripting.html)

**`defaults`** — CLI for reading/writing preference **plists**: `defaults write com.apple.dock autohide -bool true`. → [ch. 3](03-system-settings.html), [Appendix A](appendix-a-bootstrap-script.html)

**DFU mode** — Device Firmware Update mode; lets a second Mac revive or restore an Apple-silicon Mac's firmware and recoveryOS over USB-C via Apple Configurator/Finder. → [ch. 22](22-troubleshooting.html)

**Dock** — The app launcher/switcher strip. Auto-hide it. → [ch. 4](04-finder-dock-spotlight.html)

**dotfiles** — Your configuration files (`.zshrc`, `.gitconfig`, editor settings…), ideally in a Git repo with an idempotent installer. → [ch. 10](10-dotfiles-and-git.html)

**Electron** — Framework for building desktop apps from web tech; Slack, Discord, VS Code, Spotify, Notion. Memory-hungry (300–800 MB each). → [ch. 18](18-performance-and-maintenance.html)

**Erase All Content and Settings** — One-click factory reset (System Settings → General → Transfer or Reset) that keeps macOS installed; much faster than reinstalling. → [ch. 22](22-troubleshooting.html)

**FileVault** — Full-disk encryption for the startup volume, keyed to your login password plus a recovery key (which macOS 26 can store in iCloud Keychain/Passwords). On Apple silicon it's nearly free in performance. Turn it on. → [ch. 16](16-security-and-privacy.html)

**File Provider** — The API cloud-storage apps (iCloud Drive, Dropbox, OneDrive, Google Drive) use for files-on-demand. Files can be "evicted" (cloud-only placeholders) — dangerous for Git repos. → [ch. 19](19-daily-driver-apps.html)

**Finder** — The file manager. → [ch. 4](04-finder-dock-spotlight.html)

**Focus** — Per-context notification filtering modes (Do Not Disturb, Work, Study…), syncable across devices and usable as Shortcuts triggers. → [ch. 21](21-automation-and-scripting.html)

**formula** — A Homebrew package definition for a CLI tool or library, built from source or installed as a prebuilt **bottle**. → [ch. 8](08-homebrew.html)

**Full Disk Access** — The **TCC** permission that lets an app (e.g., your terminal) read protected folders (Mail, Messages, Time Machine backups, other users). Granted per app in Privacy & Security. → [ch. 16](16-security-and-privacy.html)

**Gatekeeper** — The launch-time check that downloaded apps are signed by a known developer and **notarized**. macOS 26 removed the right-click-Open bypass; use Privacy & Security → Open Anyway. → [ch. 16](16-security-and-privacy.html)

**Ghostty** — Fast, native (Swift/Zig) GPU terminal emulator with a plain-text config; this guide's default terminal. 1.3 as of September 2026. → [ch. 9](09-terminal-and-shell.html)

**Golden Gate** — macOS 27 (ships 14 September 2026). Apple-silicon only; Liquid Glass intensity slider; Siri/AI in Spotlight; Rosetta removed from the default install. → [ch. 2](02-first-boot-and-migration.html)

**Hammerspoon** — Lua scripting bridge to macOS APIs for hotkeys, windows, and system events. → [ch. 21](21-automation-and-scripting.html)

**Homebrew** — The de facto macOS package manager (`brew`), installed under `/opt/homebrew` on Apple silicon. Version 6.0 (2026) added tap trust prompts, `brew exec`, parallel bundle installs; Intel support is Tier 3. → [ch. 8](08-homebrew.html)

**hyper key** — A single key (usually Caps Lock via Karabiner) that sends `⌃⌥⇧⌘` together, giving you a conflict-free modifier layer for your own shortcuts. → [ch. 5](05-keyboard-and-input.html)

**iCloud Drive** — Apple's file sync. "Desktop & Documents Folders" sync is convenient and risky for developers. → [ch. 2](02-first-boot-and-migration.html)

**iCloud Keychain** — Encrypted sync of passwords, passkeys, Wi-Fi passwords, and (since macOS 26) the FileVault recovery key; surfaced in the **Passwords** app.

**idempotent** — A script you can run repeatedly with the same end result — the property every bootstrap and dotfiles installer should have. → [Appendix A](appendix-a-bootstrap-script.html)

**JXA** — JavaScript for Automation; the JavaScript face of Apple Events, alternative to AppleScript. Run via `osascript -l JavaScript`. → [ch. 21](21-automation-and-scripting.html)

**Karabiner-Elements** — Low-level keyboard remapper (driver extension). Caps Lock → Escape/Control, hyper key, per-device profiles. → [ch. 5](05-keyboard-and-input.html)

**kernel extension (kext)** — Legacy third-party kernel code. Effectively dead on Apple silicon (needs Reduced Security); modern software uses **system extensions**. A kext requirement is a red flag. → [ch. 16](16-security-and-privacy.html)

**Keychain** — macOS's encrypted credential store (`security` CLI, Keychain Access app). Where SSH passphrases, Git tokens, and API keys should live. → [ch. 21](21-automation-and-scripting.html)

**launchd** — macOS's init system and job scheduler; replaces cron/systemd. Jobs are **plists** in LaunchAgents/LaunchDaemons folders, managed with `launchctl`. → [ch. 21](21-automation-and-scripting.html)

**Liquid Glass** — The translucent design language introduced in macOS 26 Tahoe; macOS 27 adds an intensity slider. Reduce Transparency in Accessibility if it hurts readability. → [ch. 3](03-system-settings.html)

**LLDB** — Apple's debugger (LLVM). Use it instead of GDB on macOS. → [ch. 20](20-cs-student-specific.html)

**Lockdown Mode** — Extreme security mode for people at risk of targeted attack; disables many features. Not for general use. → [ch. 16](16-security-and-privacy.html)

**Login Items & Extensions** — System Settings pane listing apps that open at login and background agents you can toggle. Audit it. → [ch. 18](18-performance-and-maintenance.html)

**`mas`** — CLI for the Mac App Store; used in Brewfiles for App Store apps. → [Appendix B](appendix-b-brewfile.html)

**Memory Pressure** — Activity Monitor's graph of how hard macOS is working to keep memory available. Green fine; sustained yellow/red = you need more RAM or fewer apps. More meaningful than "Memory Used". → [ch. 18](18-performance-and-maintenance.html)

**Migration Assistant** — Apple's tool for moving accounts, apps, and data from an old Mac/backup/PC. Convenient, brings cruft. → [ch. 2](02-first-boot-and-migration.html)

**mise** — Polyglot runtime version manager (Node, Python, Java, Go, Rust, Ruby…) replacing nvm/pyenv/rbenv/asdf; also tasks and env vars. → [ch. 11](11-languages-and-runtimes.html)

**Mission Control** — Overview of all windows and **Spaces**. `⌃↑`. → [ch. 6](06-window-management.html)

**MLX** — Apple's array/ML framework optimized for Apple silicon's unified memory; the fastest way to run LLMs locally on a Mac. → [ch. 20](20-cs-student-specific.html)

**MPS** — Metal Performance Shaders; PyTorch's GPU backend on Apple silicon (`device="mps"`). Not CUDA. → [ch. 20](20-cs-student-specific.html)

**Nerd Font** — A monospace font patched with thousands of icons (Powerline, devicons) that prompts like Starship and tools like eza use. → [ch. 9](09-terminal-and-shell.html)

**notarization** — Apple's automated malware scan of developer-signed apps; required for **Gatekeeper** to allow a download without warnings. → [ch. 16](16-security-and-privacy.html)

**OrbStack** — Fast, light Docker-compatible container runtime and Linux VM manager for macOS; this guide's default. Free for personal use. → [ch. 13](13-containers-and-vms.html)

**Optimized Battery Charging / Charge Limit** — Battery-health features: the first learns your schedule and holds at 80%; the second (macOS 26.4+) caps at 80% always. → [ch. 18](18-performance-and-maintenance.html)

**passkey** — Phishing-resistant public-key login credential synced via iCloud Keychain (or a password manager), replacing passwords on supporting sites. → [ch. 16](16-security-and-privacy.html)

**Passwords app** — Apple's built-in password manager (macOS 15+) with passkeys, TOTP, shared groups, and a Windows/Chrome extension. → [ch. 19](19-daily-driver-apps.html)

**PATH** — The ordered list of directories the shell searches for commands. `/opt/homebrew/bin` must come before `/usr/bin`. Set in `~/.zprofile`. → [ch. 9](09-terminal-and-shell.html), [ch. 22](22-troubleshooting.html)

**plist** — Property list; XML or binary key–value file used for preferences and launchd jobs. Inspect with `plutil -p`, edit with `defaults`. → [ch. 3](03-system-settings.html)

**Private Cloud Compute** — Apple's server-side AI processing with verifiable privacy guarantees, used when a request is too large for on-device models.

**Private Relay** — iCloud+ feature that proxies Safari traffic through two hops to hide IP and DNS from sites and your ISP.

**purgeable space** — Storage macOS can reclaim on demand (caches, local snapshots, evicted cloud files); counted as "available" by Finder but not by `df`. → [ch. 18](18-performance-and-maintenance.html)

**Quick Action** — A Shortcut or Automator workflow exposed in Finder's right-click menu and the Touch Bar/Services menu. → [ch. 21](21-automation-and-scripting.html)

**Quick Look** — Space-bar file preview in Finder; extensible with plugins (Markdown, source code, JSON). → [ch. 4](04-finder-dock-spotlight.html)

**Raycast** — Extensible launcher with clipboard history, window management, snippets, and an extension store; the common Spotlight replacement. → [ch. 19](19-daily-driver-apps.html)

**Recovery (macOS Recovery / recoveryOS)** — The hidden boot environment (hold power → Options) with Disk Utility, Reinstall macOS, Time Machine restore, Terminal, Startup Security Utility. → [ch. 22](22-troubleshooting.html)

**Rosetta 2** — Apple's translation layer that runs **x86_64** Mac binaries (and, via OrbStack/Docker, x86 Linux containers) on Apple silicon. Not installed by default on macOS 27 (`softwareupdate --install-rosetta`); removed entirely in macOS 28. → [ch. 2](02-first-boot-and-migration.html)

**Safe Mode** — Boot with only Apple extensions and no login items (hold ⇧ when choosing the startup disk). The fastest "is it my software or the OS?" test. → [ch. 22](22-troubleshooting.html)

**sealed system volume (SSV)** — The read-only, cryptographically signed volume holding macOS itself (`/System`, `/usr/bin`). You can't modify it; install into `/opt`, `/usr/local`, or `~`. → [ch. 16](16-security-and-privacy.html)

**Shortcuts** — Apple's cross-device visual automation app; on macOS 26 gained triggers (time, app, folder, Wi-Fi, Focus) and an AI "Use Model" action. Runnable from the shell with `shortcuts run`. → [ch. 21](21-automation-and-scripting.html)

**SIP (System Integrity Protection)** — Kernel-enforced protection of system files and processes even from root. Leave it enabled. `csrutil status`. → [ch. 16](16-security-and-privacy.html)

**Spaces** — Virtual desktops; swipe or `⌃←→`. Assign apps per Space; turn off automatic reordering. → [ch. 6](06-window-management.html)

**Spotlight** — System search and launcher (`⌘Space`). macOS 26 added `⌘1–4` filtered views, clipboard history, Actions, and AI answers. Index managed by `mds`; rebuild with `mdutil -E /`. → [ch. 4](04-finder-dock-spotlight.html)

**Stage Manager** — Optional window-grouping mode with recent apps in a side strip. Off by default in this guide. → [ch. 6](06-window-management.html)

**Starship** — Fast, cross-shell prompt configured in `starship.toml`. → [ch. 9](09-terminal-and-shell.html)

**Stolen Device Protection** — macOS 26.4+ feature requiring biometrics (no password fallback) and a security delay for sensitive changes when the Mac is away from familiar locations. → [ch. 16](16-security-and-privacy.html)

**system extension** — Modern, user-space replacement for **kexts**: network extensions (VPNs, LuLu), endpoint security (antivirus), driver extensions (Karabiner). Listed by `systemextensionsctl list`. → [ch. 16](16-security-and-privacy.html)

**System Data** — The Storage pane's catch-all category (caches, snapshots, container images, simulators). Legitimately 30–100 GB on a dev Mac. → [ch. 18](18-performance-and-maintenance.html)

**Tahoe** — macOS 26 (2025–26). Liquid Glass, new Spotlight, Shortcuts triggers, the last release supporting a few Intel Macs. 26.6 is current as of September 2026. → [ch. 2](02-first-boot-and-migration.html)

**tap** — A third-party Homebrew repository (`brew tap owner/repo`). Homebrew 6 asks you to trust a tap before installing from it. → [ch. 8](08-homebrew.html)

**TCC (Transparency, Consent, and Control)** — The permissions system behind Privacy & Security prompts (Camera, Full Disk Access, Accessibility, Automation, Screen Recording…). `tccutil reset` clears grants. → [ch. 16](16-security-and-privacy.html), [ch. 22](22-troubleshooting.html)

**Thunderbolt / USB4 / USB-C** — The Mac's ports. Same connector, different capabilities: TB4/5 = 40–80 Gbps, displays, PCIe; USB-C cables may be USB 2.0 only with no video. → [ch. 1](01-hardware-and-buying.html), [ch. 22](22-troubleshooting.html)

**Time Machine** — Apple's versioned backup to an external disk or network share; hourly local **snapshots** when the disk is away. → [ch. 17](17-backup-and-recovery.html)

**Touch ID for sudo** — Configured via `/etc/pam.d/sudo_local` so terminal `sudo` accepts a fingerprint. → [ch. 9](09-terminal-and-shell.html)

**unified log** — The system-wide structured log (`log show`, `log stream`, Console app) replacing text log files. → [ch. 22](22-troubleshooting.html)

**unified memory** — Apple silicon's single memory pool shared by CPU, GPU, and Neural Engine. Why "Memory Used" looks high and why RAM size matters for local ML. → [ch. 1](01-hardware-and-buying.html), [ch. 18](18-performance-and-maintenance.html)

**uv** — Astral's fast Python package/project/interpreter manager replacing pip, venv, pipx, pyenv, and poetry for most uses. → [ch. 11](11-languages-and-runtimes.html)

**Virtualization framework** — Apple's built-in hypervisor API used by OrbStack, UTM (Apple mode), Docker Desktop, `container`, Parallels, and VMware Fusion for fast arm64 VMs. → [ch. 13](13-containers-and-vms.html)

**Visual Intelligence** — macOS 27 screen-understanding feature (`⌘⇧Space`) that identifies and acts on what's on screen.

**x86_64 / amd64** — The Intel/AMD 64-bit instruction set. Needs **Rosetta 2** on a Mac; `linux/amd64` containers are translated. Gone entirely with macOS 28. → [ch. 2](02-first-boot-and-migration.html), [ch. 13](13-containers-and-vms.html)

**Xcode** — Apple's IDE and SDKs (12+ GB); required for iOS/macOS app development, optional otherwise. Manage versions with `xcodes`. → [ch. 7](07-command-line-tools-and-xcode.html)

**XProtect** — Apple's built-in, silently updated malware scanner and remediation (XProtect Remediator). One reason third-party antivirus is unnecessary for most people. → [ch. 16](16-security-and-privacy.html)

**zsh** — The default shell since Catalina. Config order: `.zshenv` → `.zprofile` (login) → `.zshrc` (interactive). → [ch. 9](09-terminal-and-shell.html)
