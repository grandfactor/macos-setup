<!--
number: E
part: Part VI — Reference
description: Where the facts in this guide come from and where to check them when they drift — Apple's own documentation and release notes, project changelogs, the community references worth trusting, release calendars for every runtime, and a note on how the guide was researched and how to report an error.
-->
# Appendix E — Sources & further reading

This guide was researched in September 2026 against primary sources wherever one existed: Apple's documentation and release notes, project changelogs and docs, vendor pricing pages, and official release schedules. Community sources are listed where they add practical knowledge Apple doesn't publish. Prices, version numbers, and dates *will* drift; the point of this appendix is to give you the places to re-check rather than to trust the guide forever.

Working notes from the research pass live in the repo's [`research/`](https://github.com/grandfactor/macos-setup/tree/main/research) directory, dated, if you want to see what was checked and when.

## Apple — primary documentation

| Topic | Where |
|---|---|
| macOS release notes (developer) | developer.apple.com/documentation/macos-release-notes — every 26.x / 27 build, with known issues |
| macOS user guide | support.apple.com/guide/mac-help — System Settings panes, Spotlight, Finder, Time Machine, Shortcuts |
| Security releases and CVE lists | support.apple.com/100100 (Apple security releases) — what each update fixed; the 26.6 entry lists 155 CVEs |
| Apple Platform Security Guide | support.apple.com/guide/security — FileVault, Secure Enclave, Gatekeeper, SIP, sealed system volume, Activation Lock; the authoritative reference behind [ch. 16](16-security-and-privacy.html) |
| Apple Platform Deployment | support.apple.com/guide/deployment — MDM-era detail on `defaults`, profiles, startup security, DFU revive |
| Rosetta 2 | support.apple.com/102527 — install instructions and the macOS 27/28 removal notice |
| Spotlight keyboard shortcuts | support.apple.com/guide/mac-help/mh26783 — the `⌘1`–`⌘4` views and quick keys |
| Mac keyboard shortcuts | support.apple.com/102650 — the canonical list behind [Appendix C](appendix-c-keyboard-shortcuts.html) |
| Startup key combinations (Apple silicon) | support.apple.com/102603 — hold-power options, Safe Mode, Diagnostics |
| Revive or restore with Apple Configurator | support.apple.com/108900 — DFU procedure per model |
| Apple Diagnostics reference codes | support.apple.com/102550 |
| Battery health and charge limit | support.apple.com/102888 (Optimized Battery Charging), 26.4 release notes for the 80% limit |
| Time Machine | support.apple.com/guide/mac-help/mh35860; `man tmutil` |
| Shortcuts user guide (Mac) | support.apple.com/guide/shortcuts-mac — actions, automations/triggers, Run Shell Script |
| Mac Automation Scripting Guide (AppleScript/JXA) | developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide — archived but still the reference |
| launchd | developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup; `man launchd.plist`; launchd.info (community reference) |
| Xcode, Command Line Tools, SDKs | developer.apple.com/xcode/resources; developer.apple.com/download/all (older Xcode/CLT builds) |
| Apple `container` | github.com/apple/container — README, docs, release notes (1.0: no Compose) |
| MLX | github.com/ml-explore/mlx; ml-explore.github.io/mlx |
| Virtualization framework | developer.apple.com/documentation/virtualization |
| Hardware tech specs and pricing | apple.com/mac/compare; apple.com/us-edu/store (education pricing); apple.com/newsroom (launch dates: Mar 3 2026 MacBook Air M5 / MBP M5 Pro–Max / Studio Displays; Aug 25 2026 Mac mini M6 & M5 Pro, Mac Studio M5 Max/Ultra) |
| macOS 27 Golden Gate | apple.com/newsroom (WWDC June 8 2026 announcement; September 14 2026 release); developer.apple.com/macos |
| Apple Intelligence availability | apple.com/apple-intelligence — supported devices and languages |
| Feedback Assistant | feedbackassistant.apple.com — where real bug reports go |

## Developer tooling — official docs and changelogs

| Tool | Where |
|---|---|
| Homebrew | docs.brew.sh (Installation, FAQ, Homebrew on Apple silicon, Brew Bundle, Services); brew.sh/blog — 6.0 release post (tap trust, `brew exec`, parallel bundle, Intel Tier 3); github.com/Homebrew/brew/releases |
| Ghostty | ghostty.org/docs (config reference, keybinds, macOS specifics); github.com/ghostty-org/ghostty/releases — 1.3.0 (Mar 2026) notes |
| iTerm2 / WezTerm / Kitty / Warp | iterm2.com/documentation; wezterm.org; sw.kovidgoyal.net/kitty; docs.warp.dev |
| zsh | zsh.sourceforge.io/Doc; the Arch wiki zsh page (excellent, distro-agnostic) |
| Starship | starship.rs/config |
| fzf / zoxide / eza / bat / fd / ripgrep / delta | each project's GitHub README (junegunn/fzf, ajeetdsouza/zoxide, eza-community/eza, sharkdp/bat, sharkdp/fd, BurntSushi/ripgrep, dandavison/delta) |
| tmux | github.com/tmux/tmux/wiki |
| Git | git-scm.com/docs; GitHub Docs — SSH keys, SSH commit signing (docs.github.com/authentication) |
| GitHub CLI | cli.github.com/manual |
| chezmoi / GNU Stow | chezmoi.io; gnu.org/software/stow |
| mise | mise.jdx.dev — getting started, configuration, idiomatic version files, tasks |
| uv | docs.astral.sh/uv — projects, scripts (PEP 723), tools, Python versions |
| Node.js | nodejs.org/en/about/previous-releases and the release blog — Node 26 LTS (Oct 2026) and the new yearly release model |
| Python | peps.python.org/pep-0790 (3.15 schedule, Oct 2026); devguide.python.org/versions |
| Java | openjdk.org/projects/jdk (25 LTS; 27 LTS Sept 2027); adoptium.net |
| Go / Rust | go.dev/doc/devel/release; releases.rs / forge.rust-lang.org |
| PostgreSQL | postgresql.org/support/versioning (18 current; 19 due autumn 2026) |
| VS Code | code.visualstudio.com/docs; code.visualstudio.com/updates (monthly); keyboard reference PDF (macOS) |
| Cursor / Zed / JetBrains | docs.cursor.com; zed.dev/docs; jetbrains.com/help; jetbrains.com/community/education (free student licenses) |
| GitHub Copilot | docs.github.com/copilot; education.github.com/pack (Student Developer Pack terms) |
| Stack Overflow Developer Survey | survey.stackoverflow.co — the 2026 edition is the source for editor share figures quoted in [ch. 12](12-editors-and-ides.html) |
| OrbStack | docs.orbstack.dev — Docker, Linux machines, Rosetta, pricing/licensing |
| Docker Desktop | docs.docker.com/desktop/setup/install/mac-install; docker.com/pricing (subscription tiers) |
| Podman / Colima / Lima | podman.io/docs; github.com/abiosoft/colima; lima-vm.io |
| UTM / VMware Fusion / Parallels | docs.getutm.app; vmware.com (Fusion free for all since Nov 2024); parallels.com |
| Kubernetes tooling | kubernetes.io/docs/tasks/tools; kind.sigs.k8s.io; k9scli.io |
| Cloud CLIs | docs.aws.amazon.com/cli; cloud.google.com/sdk/docs; learn.microsoft.com/cli/azure |
| Tailscale | tailscale.com/kb |
| Hammerspoon | hammerspoon.org/docs; hammerspoon.org/Spoons |
| Karabiner-Elements | karabiner-elements.pqrs.org/docs; ke-complex-modifications.pqrs.org |
| AeroSpace / Rectangle / yabai | nikitabobko.github.io/AeroSpace/guide; rectangleapp.com; github.com/koekeishiya/yabai/wiki |
| Raycast / Alfred | manual.raycast.com; alfredapp.com/help |
| Keyboard Maestro / BetterTouchTool / Hazel | wiki.keyboardmaestro.com; docs.folivora.ai; noodlesoft.com/manual |
| Objective-See tools (LuLu, KnockKnock, BlockBlock) | objective-see.org/tools.html |
| Little Snitch | obdev.at/products/littlesnitch |
| 1Password / Bitwarden | developer.1password.com (CLI, SSH agent); bitwarden.com/help |
| Zotero / Obsidian / Anki | zotero.org/support; help.obsidian.md; docs.ankiweb.net |
| LaTeX / Typst | tug.org/mactex; typst.app/docs |

## Community references worth trusting

- **Mr. Macintosh** (mrmacintosh.com) — meticulous tracking of every macOS build, installer download links, and update quirks; the first place to look when an update misbehaves.
- **Howard Oakley, The Eclectic Light Company** (eclecticlight.co) — deep, tested explanations of APFS, Time Machine, XProtect, the unified log, Apple silicon boot and security; Oakley's free utilities (Mints, Silent Knight, T2M2) are referenced in [ch. 17](17-backup-and-recovery.html) and [ch. 22](22-troubleshooting.html).
- **Six Colors** (sixcolors.com) and **Daring Fireball** (daringfireball.net) — informed commentary on Apple releases; the Six Colors FileVault/recovery-key write-up informed [ch. 16](16-security-and-privacy.html).
- **MacRumors** (macrumors.com) and **9to5Mac** (9to5mac.com) — release roundups and hardware buyer's guides (macrumors.com/roundup); good for "what changed in 26.x" summaries and the MacBook Neo/M5/M6 launch coverage.
- **Michael Tsai's blog** (mjtsai.com) — link roundups on macOS developer and security issues, with the discussion that follows each change (Gatekeeper's right-click removal, TCC changes, Rosetta's retirement).
- **ERNW macOS hardening guide** (github.com/ernw/hardening) and the **macOS Security and Privacy Guide** (github.com/drduh/macOS-Security-and-Privacy-Guide) — the two community hardening references [ch. 16](16-security-and-privacy.html) draws from and deliberately trims for a daily-driver machine.
- **Apple Stack Exchange** (apple.stackexchange.com) and **Ask Different** — the searchable Q&A corpus for "why does macOS do X"; look for answers with `man` page citations.
- **awesome-mac** (github.com/jaywcjlove/awesome-mac) and **Awesome macOS Command Line** (github.com/herrbischoff/awesome-macos-command-line) — exhaustive app and `defaults` lists; the latter is the best index of `defaults write` keys.
- **macos-defaults.com** — visual, per-key documentation of `defaults write` settings with screenshots of the effect.
- **Mathias Bynens's `.macos`** (github.com/mathiasbynens/dotfiles) — the ancestor of every macOS defaults script, including [Appendix A](appendix-a-bootstrap-script.html)'s; many keys are now obsolete, so treat it as history.
- **launchd.info** — the friendliest reference for `launchd.plist` keys.
- **The Arch Wiki** (wiki.archlinux.org) — for anything that's really about zsh, tmux, Git, SSH, or Neovim, it's the clearest documentation on the internet regardless of OS.
- **Julia Evans's zines** (wizardzines.com) — Git, the shell, DNS, and networking explained better than anywhere else; recommended reading in [ch. 20](20-cs-student-specific.html).
- **The Missing Semester of Your CS Education** (missing.csail.mit.edu) — MIT's course on the shell, editors, Git, debugging, and metaprogramming; the natural companion to Part III of this guide.
- **r/macapps**, **r/MacOS**, **r/macsysadmin**, **MacAdmins Slack** (macadmins.org) — where practical fixes surface first, especially for enterprise/university-managed Macs.

## Release calendars to bookmark

Check these each September (macOS/Xcode/Java), October (Node LTS, Python), and when a course pins a version.

| What | Calendar |
|---|---|
| macOS point releases and security updates | support.apple.com/100100 |
| macOS major releases | WWDC in June (announce), mid-September (ship) — every year since 2020 |
| Xcode | with each macOS/iOS release; betas from June |
| Homebrew | github.com/Homebrew/brew/releases (monthly-ish minor, yearly major) |
| Ghostty | ~6-month cadence (1.4 expected ~September 2026) |
| Node.js | April (even major, becomes LTS in October); the 2026 policy moves to one release per year |
| Python | October annually (3.15 in 2026); peps.python.org release PEPs |
| Java | March and September; LTS every two years (25 → 27 in Sept 2027) |
| Go | February and August |
| Rust | every 6 weeks |
| PostgreSQL | September/October annually |
| VS Code | monthly, first week |
| Docker Desktop / OrbStack | monthly-ish |
| Ubuntu (for containers/VMs) | April (LTS in even years: 26.04 is current LTS) and October |

## How this guide was researched

Each chapter started from Apple's documentation for the feature in question, then the tool's own docs, then release notes for the current version, then community sources for practical behaviour Apple doesn't document (e.g., which `defaults` keys still work, how Gatekeeper's "Open Anyway" flow behaves in 26.x, real-world OrbStack vs Docker Desktop performance). Prices were taken from vendor pages in September 2026 in USD, with education pricing from Apple's US education store. Where a claim couldn't be verified against a primary source it was either dropped or marked with hedging language ("check current terms").

Things that were *not* done: no synthetic benchmarks were run; no affiliate links exist anywhere in the guide; no vendor was consulted or paid. Recommendations reflect the author's judgment of the best default for a CS student or working engineer in 2026, and are explicitly opinions where the guide says so.

## Reporting errors

If something is wrong, out of date, or missing: open an issue or pull request at [github.com/grandfactor/macos-setup](https://github.com/grandfactor/macos-setup). Every page on the site has an **Edit on GitHub** link in its footer. Corrections that cite a primary source get merged fastest. The single-file [`GUIDE.md`](https://github.com/grandfactor/macos-setup/blob/main/GUIDE.md) is generated from the per-chapter sources in `guide/` by `build.py`; edit the chapter file, not the generated output.
