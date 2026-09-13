# The macOS Setup Guide

_For CS students, software engineers and everyone who lives on a Mac — 2026 edition_

> This is the single-document Markdown adaptation of the website. The same content is split chapter-by-chapter in [`guide/`](guide/), and rendered as a site in [`docs/`](docs/). Last reviewed September 2026.

## Table of contents

**Part I — Before you start**

- [01. Hardware & buying guide](#01-hardware-buying-guide) — Which Mac to buy in late 2026, how much RAM and storage you actually need, education pricing, refurbs, and the accessories that matter.
- [02. First boot, Setup Assistant & migration](#02-first-boot-setup-assistant-migration) — Setup Assistant choices that are hard to undo, clean install vs Migration Assistant, the first 30 minutes, and getting to a known-good baseline.
**Part II — System & interface**

- [03. System Settings, pane by pane](#03-system-settings-pane-by-pane) — A pane-by-pane tour of System Settings in macOS 26/27 with the developer-relevant toggles, the Liquid Glass controls, and the defaults-write equivalents for scripting.
- [04. Finder, Dock & Spotlight](#04-finder-dock-spotlight) — Finder as a power tool, Quick Look, the Dock, and the new Spotlight (apps, files, actions, clipboard, Quick Keys) — plus when Raycast or Alfred still earn their place.
- [05. Keyboard, shortcuts & input](#05-keyboard-shortcuts-input) — Modifier remaps, Caps Lock as Control/Escape, Karabiner-Elements, text navigation shortcuts every Mac user should know, input sources, and coming from Windows/Linux keyboards.
- [06. Window management, Spaces & displays](#06-window-management-spaces-displays) — Spaces, Mission Control, native tiling, Stage Manager, and the third-party window managers (Rectangle, Raycast, AeroSpace, yabai) — which one fits how you work, and how to set up multiple displays.
**Part III — Developer environment**

- [07. Command Line Tools, Xcode & the toolchain](#07-command-line-tools-xcode-the-toolchain) — Command Line Tools vs full Xcode, xcode-select, SDKs and simulators, Rosetta 2 and the arm64-only future, and keeping Xcode from eating your disk.
- [08. Homebrew](#08-homebrew) — Homebrew 6 from scratch — installing correctly on Apple silicon, formulae vs casks, Brewfiles, tap trust, ask mode, services, maintenance, and the Intel deprecation.
- [09. Terminal & shell](#09-terminal-shell) — Choosing a terminal (Ghostty, iTerm2, WezTerm, Kitty, Warp), zsh configured properly without a framework, Starship, fzf, zoxide, the modern Rust CLI toolkit, tmux, SSH keys, and Touch ID for sudo.
- [10. Dotfiles & Git](#10-dotfiles-git) — Version-controlling your configuration with a bare repo, chezmoi or stow; a complete Git setup for macOS (identity, signing with SSH keys, delta, aliases, global ignore); GitHub CLI; direnv; and secrets hygiene.
- [11. Languages & runtimes](#11-languages-runtimes) — One version manager (mise) for everything, uv for Python, Node/Bun/Deno, Java, Go, Rust, C/C++, Swift, Ruby, .NET, and the ML stack (PyTorch MPS, MLX, Ollama) — with the 2026 release calendar.
- [12. Editors, IDEs & AI coding tools](#12-editors-ides-ai-coding-tools) — VS Code, Cursor, Zed, JetBrains, Neovim, Xcode and the AI coding agents — what each is for in 2026, recommended settings, and how to keep the configs in sync across machines.
- [13. Containers & virtual machines](#13-containers-virtual-machines) — Containers on macOS in 2026 — OrbStack, Docker Desktop, Colima, Podman and Apple's own `container` compared; multi-arch images; Kubernetes locally; Linux and Windows VMs with UTM, Parallels, VMware Fusion and Apple's Virtualization framework.
- [14. Cloud, network & DevOps tooling](#14-cloud-network-devops-tooling) — Cloud CLIs and credentials done safely, Terraform/OpenTofu, Kubernetes tooling, API clients, HTTP debugging, Tailscale for reaching your machines, and GitHub Actions locally.
- [15. Databases & local development services](#15-databases-local-development-services) — Postgres, MySQL, SQLite, Redis, MongoDB and friends on a Mac — Homebrew services vs containers vs Postgres.app, GUI clients, local HTTPS and custom domains, and a sane local-dev workflow.
**Part IV — Security, backup & maintenance**

- [16. Security & privacy](#16-security-privacy) — A realistic threat model, FileVault and its new recovery-key rules, Gatekeeper and notarisation, the firewall, passwords and passkeys, secrets on disk, permissions hygiene, browser privacy, Lockdown Mode, and what to do when a laptop is lost.
- [17. Backup & recovery](#17-backup-recovery) — The 3-2-1 strategy on a Mac — Time Machine done right (encrypted APFS, exclusions), a second local copy, cloud backup, what iCloud is and isn't, testing restores, and recovering a Mac that won't boot.
- [18. Performance & maintenance](#18-performance-maintenance) — Keeping a Mac fast for years — reading Activity Monitor and memory pressure correctly, reclaiming storage (System Data, caches, Docker, Xcode, Homebrew), auditing login items and launch agents, battery health and the 80% charge limit, thermals, Spotlight reindexing, and a low-effort maintenance routine.
**Part V — Daily driving & workflows**

- [19. Daily-driver apps](#19-daily-driver-apps) — The non-developer half of the Mac — browsers, password managers, launchers, clipboard managers, notes, email, calendar, PDF, media, communication, and the utilities that make macOS feel finished. Free/open-source first, with the paid upgrade named where it's worth it.
- [20. CS-student specific](#20-cs-student-specific) — What's different when the Mac is for a CS degree — free software through student programs, the course-by-course toolchain (C/C++, Java, Python, systems, ML, mobile, databases, theory), running x86 Linux and Windows when a class requires it, remote lab machines, LaTeX/Typst, note-taking, and surviving four years on one battery.

---

## The macOS Setup Guide

<div class="hero">
<p class="lede">A complete, opinionated, deeply researched guide to setting up a Mac for computer science students, software engineers, and anyone who uses a Mac as their daily machine. From which Mac to buy, through the first boot, to a fully tuned development environment, security posture, backup strategy and automation layer — with the reasoning behind every recommendation.</p>
<div class="badges">
<span class="badge">macOS 26 Tahoe &amp; 27 Golden Gate</span>
<span class="badge">Apple silicon (M1 → M6)</span>
<span class="badge">Homebrew 6</span>
<span class="badge">Reviewed September 2026</span>
<span class="badge">~30 chapters · fully scriptable</span>
</div>
</div>

### Who this is for

- **CS students** starting a degree (or a bootcamp) who just got a Mac and want to set it up *once, properly*, without cargo-culting a random dotfiles repo.
- **Software engineers** joining a new job or replacing a laptop who want a reproducible, secure, fast environment on day one.
- **Daily drivers** — people who live on their Mac for writing, research, media, school and life — who want the machine to get out of their way.

You don't need to read it front to back. Each chapter stands alone, and the [checklists](23-checklists-and-cheat-sheets.html) at the end compress the whole thing into a few printable pages.

### How to use this guide

1. **In a hurry?** Read [Chapter 2 (first boot)](02-first-boot-and-migration.html), run the [bootstrap script](appendix-a-bootstrap-script.html), then skim the [checklists](23-checklists-and-cheat-sheets.html).
2. **Buying a Mac?** Start with [Chapter 1](01-hardware-and-buying.html); it is written for September 2026 pricing and the M5/M6 lineup.
3. **Already set up but it feels messy?** Jump to [Homebrew](08-homebrew.html), [Terminal &amp; shell](09-terminal-and-shell.html), [Dotfiles](10-dotfiles-and-git.html) and [Security](16-security-and-privacy.html).
4. **Setting up for a specific stack?** [Languages &amp; runtimes](11-languages-and-runtimes.html), [Containers &amp; VMs](13-containers-and-vms.html) and [Databases &amp; local dev](15-databases-and-local-dev.html) are self-contained.

Conventions used throughout:

| Convention | Meaning |
|---|---|
| <kbd>⌘</kbd> <kbd>⌥</kbd> <kbd>⌃</kbd> <kbd>⇧</kbd> <kbd>fn</kbd>/<kbd>🌐</kbd> | Command, Option, Control, Shift, Function/Globe |
| `System Settings → General → Software Update` | Navigate the Settings app in that order |
| `$ command` | Run in a terminal; the `$` is a prompt, don't type it (the copy button strips it) |
| **Recommended** / *Alternative* / ~~Avoid~~ | Our default pick / a fine substitute / something we actively steer you away from |
| Note / Tip / Warning callouts | Read these; they save hours |

Every recommendation comes with a *why*. If you disagree with the *why*, you'll know exactly what to swap.

### What's new in 2026 (and why this guide exists)

The Mac platform changed more in 2025–2026 than in the previous five years combined, and most setup guides on the internet haven't caught up:

- **macOS 27 "Golden Gate" ships September 14, 2026** and is **Apple-silicon only**. Intel Macs stay on macOS 26 Tahoe (security updates until ~2029). Rosetta 2 is removed for general apps in macOS 28 (fall 2027) — so this guide is uncompromisingly *arm64-native first*.
- **The lineup is completely new**: MacBook Neo ($599, A18 Pro, 8 GB), MacBook Air M5, MacBook Pro M5 / M5 Pro / M5 Max, Mac mini M6 and M5 Pro, Mac Studio M5 Max / M5 Ultra, two new Studio Displays. Chapter 1 tells you which one to actually buy.
- **Apple shipped its own container runtime** (`container`, on the Containerization framework) and Docker Desktop is no longer the automatic answer.
- **Homebrew 6** introduced tap trust, an "ask before install" default, parallel `brew bundle`, `brew exec`, and is dropping Intel bottles this month.
- **Spotlight became a real launcher** (apps, files, actions, clipboard history, Quick Keys) and in Golden Gate hosts Siri AI. The Raycast/Alfred question has a different answer now.
- **Security defaults moved**: FileVault is on by default at setup, its recovery key lives in iCloud Keychain and the Passwords app, Stolen Device Protection came to MacBooks, Gatekeeper lost its right-click bypass, and encrypted HFS+ backup drives are deprecated.
- **Tooling consolidated**: `mise` and `uv` replaced a zoo of version managers; Ghostty matured into the default terminal recommendation; Zed, Cursor and VS Code split the editor market three ways; AI coding agents live in the terminal and in Xcode 27.

Everything below reflects that world. Where a fact is likely to age (a version number, a price), it is dated so you can judge it.

### A note on opinions

This guide is opinionated on purpose. Beginners are paralysed by "it depends"; experts already know when to deviate. So each section gives a **default**, one or two **alternatives**, and the **reason**. When a tool is *free for students* or *free for personal use*, we say so, because that matters when you're on a budget.

Nothing here is sponsored. Prices are US list prices at the time of review; education pricing is noted where Apple or a vendor offers it.

### Contributing and corrections

The source is plain Markdown in the [`guide/`](https://github.com/grandfactor/macos-setup/tree/main/guide) directory of the repository; the site and the single-file `GUIDE.md` are generated from it by a dependency-free Python script (`python3 build.py`). Found a mistake, a stale price or a better tool? Open an issue or a pull request.

---

## 01. Hardware & buying guide

> [!IMPORTANT]
> **The one-paragraph answer.** For a CS student or a working software engineer in September 2026 the sweet spot is a **MacBook Air M5 (13" or 15") with 24 GB of memory and 512 GB–1 TB of storage**, bought through the Apple Education Store. If you compile large native codebases, run several containers plus an IDE plus a browser all day, or do ML work, step up to a **14" MacBook Pro with M5 Pro (24–48 GB)**. Do **not** buy 8 GB of RAM for development work in 2026, and do **not** buy an Intel Mac at any price.

### The 2026 Mac lineup at a glance

Everything Apple currently sells is Apple silicon. The table shows US list price and *education* price (see [Education pricing](#education-pricing-and-back-to-school)) for the base configuration.

| Mac | Chip | Base memory / storage | Max memory | Displays (external) | Price (edu) | Released |
|---|---|---|---|---|---|---|
| **MacBook Neo 13"** | A18 Pro (6-core CPU, 5-core GPU) | 8 GB / 256 GB | 8 GB | 1 × 4K60 | $599 ($499) | Mar 2026 |
| **MacBook Air 13" / 15"** | M5 (10-core CPU, 8- or 10-core GPU) | 16 GB / 512 GB | 32 GB | 2 | from $1,099 / $1,299 | Mar 2026 |
| **MacBook Pro 14"** | M5 | 16 GB / 1 TB | 32 GB | 2 | $1,699 ($1,599) | Oct 2025 / Mar 2026 |
| **MacBook Pro 14" / 16"** | M5 Pro (15- or 18-core CPU) | 24 GB / 1 TB | 64 GB | 2 | $2,199 / $2,699 ($2,049 / $2,499) | Mar 2026 |
| **MacBook Pro 14" / 16"** | M5 Max (18-core CPU, up to 40-core GPU) | 36 GB / 2 TB | 128 GB | 4 | $3,599 / $3,899 ($3,299 / $3,599) | Mar 2026 |
| **iMac 24"** | M4 | 16 GB / 256 GB | 32 GB | 1–2 | $1,299 | Oct 2024 |
| **Mac mini** | **M6** (12-core CPU, 12-core GPU) | 16 GB / 256 GB | 32 GB | 3 | $899 ($799) | Sep 22 2026 |
| **Mac mini** | M5 Pro | 24 GB / 512 GB | 64 GB | 3 | $1,699 ($1,599) | Sep 22 2026 |
| **Mac Studio** | M5 Max | 36 GB / 512 GB | 128 GB | 5+ | $2,499 ($2,299) | Sep 22 2026 |
| **Mac Studio** | M5 Ultra (up to 36-core CPU, 80-core GPU) | 96 GB / 1 TB | 512 GB | 8 | $5,499 ($5,099) | Sep 22 2026 (512 GB late Oct) |
| **Mac Pro** | M2 Ultra | 64 GB / 1 TB | 192 GB | 8 | $6,999 | 2023 (stale) |

Notes on the generation you're buying into:

- **M5 family (late 2025–2026)** introduced *Neural Accelerators in every GPU core* (Apple claims ~4× AI throughput vs M4-class), a new "super core + performance core" CPU layout on Pro/Max, 2× faster SSDs, and the Apple **N1** wireless chip (Wi‑Fi 7, Bluetooth 6). All MacBook Pros have Thunderbolt 5.
- **M6** debuted in the Mac mini (announced Aug 25, 2026) — 12 CPU cores, "world's fastest single-thread," 170 GB/s memory bandwidth. Expect M6 MacBook Pros (widely rumoured to bring OLED displays) in late 2026 or 2027. If you can wait and you want a Pro, that's the one thing worth waiting for. Nobody should wait for anything to buy an Air.
- The **MacBook Neo** is Apple's $599 Mac. It uses the iPhone-class A18 Pro, has **8 GB of RAM soldered with no upgrade**, one USB 3 port and one USB 2 port, no Touch ID on the base model, Wi‑Fi 6E, and a 500-nit sRGB display. It runs macOS 26.3+ and 27 fine.

### How to choose

#### Laptop or desktop?

Students: laptop, always. You will carry it to lectures, labs, group projects, and interviews. Engineers with a fixed desk: a **Mac mini M6 ($899) plus a good monitor** is the best price/performance in the lineup by a wide margin, and a second-hand M1/M2 Air for travel costs less than the upgrade from Air to Pro. Many people end up with exactly that pair.

#### Air vs Pro

The Air is fanless. In sustained all-core loads (long compiles, video export, training a model locally) it throttles after several minutes; in bursty developer work (edit, build, test, browse) you will not notice. The Pro gets you:

- active cooling → sustained performance,
- the Liquid Retina **XDR** display (mini-LED, 1600 nits HDR, 120 Hz ProMotion, optional nano-texture) vs the Air's 500-nit 60 Hz IPS,
- 3 Thunderbolt ports + HDMI + SDXC vs 2 Thunderbolt ports,
- with M5 Pro/Max: more memory, more bandwidth, more external displays,
- better speakers/mics (matters more than you think for remote interviews and calls),
- up to 24 hours battery (16" M5 Pro) — the Air is ~15–18 hours in practice.

If your budget stretches to a 14" Pro with plain **M5**, compare it against a 15" Air with **more memory** at the same price: for most students the Air with 24–32 GB is the better machine, because memory is what runs out first.

#### 13" vs 14" vs 15" vs 16"

- **13" Air (1.24 kg)**: best for commuting and cramped lecture desks; you'll use an external monitor at home.
- **15" Air (1.51 kg)**: the "one machine" size for most people — the extra screen matters when you're not docked.
- **14" Pro (1.55–1.60 kg)**: the professional default; same footprint as the 13" Air with a vastly better screen.
- **16" Pro (2.14 kg)**: desktop-replacement. Heavy in a backpack every day; superb if you rarely move it.

#### The MacBook Neo: should a CS student buy one?

**Honestly: only if $599/$499 is the ceiling.** It will run VS Code, a browser, Python, Java, Node, Git, and a lecture's worth of tabs. The 8 GB limit becomes painful the moment you add Docker/OrbStack (which reserves memory for a Linux VM), an Android emulator, IntelliJ on a big project, or a local LLM. macOS will swap to the fast SSD and keep working, but you'll feel it, and constant heavy swapping shortens SSD life. If you choose a Neo, take the 512 GB model, keep containers off the machine (use a cloud VM or the university's servers), and plan to replace it after 2–3 years. The M5 Air at $999 (edu) with 16 GB is a far better four-year investment.

### Memory: the decision that actually matters

Apple silicon uses **unified memory**: CPU, GPU and Neural Engine share one pool, and *it cannot be upgraded later*. Buy for the last year you'll own the machine, not the first.

| Your workload | Minimum | Comfortable | Notes |
|---|---|---|---|
| Notes, browser, Office, light Python/Java coursework | 16 GB | 16 GB | 8 GB works but swaps heavily with many tabs. |
| Typical CS degree: IDE + browser + Docker/OrbStack + Slack/Discord + music | 16 GB | **24 GB** | 24 GB is the 2026 sweet spot; the upgrade is ~$200 (edu). |
| Full-stack dev: several services in containers, Postgres, Node, an Electron IDE, Figma | 24 GB | **32 GB** | Docker Desktop alone likes 4–8 GB; OrbStack is lighter. |
| Mobile dev: Xcode + iOS Simulator + Android Studio + emulator | 24 GB | 32–48 GB | Two emulators plus Xcode indexing is brutal on 16 GB. |
| Systems / big native builds (LLVM, Chromium, game engines), VMs | 32 GB | 48–64 GB | Also want M5 Pro/Max for the core count. |
| Local LLMs & ML: 7B–14B models quantised | 24–32 GB | 48 GB+ | Model size in GB ≈ memory needed; 128 GB M5 Max runs 70B-class models; 512 GB M5 Ultra runs ~400B. |

Rules of thumb:

- macOS itself is happy at 16 GB; the *browser* and *Electron apps* are what eat memory (every Chrome/Slack/VS Code/Discord window is a small Chromium).
- Memory pressure (Activity Monitor → Memory → the graph at the bottom) should stay **green**. Yellow occasionally is fine. Red means you bought too little.
- Do not "save" on memory to afford storage. Storage can be extended externally; memory cannot.

### Storage

- macOS + Xcode + a normal set of apps ≈ 60–90 GB. Xcode alone is ~15 GB installed and its iOS Simulator runtimes add 8–10 GB *each* (Chapter 7 shows how to prune them). Docker/OrbStack images balloon to tens of GB if you never `prune`. Node projects have `node_modules` folders of 500 MB+. A local LLM is 4–40 GB per model.
- **512 GB** is the realistic floor for a developer in 2026. **1 TB** if you do mobile, ML, video, or games. The MacBook Pro now *starts* at 1 TB (M5 Pro) / 2 TB (M5 Max), which is why it looks expensive next to the Air.
- Apple's SSDs are fast (the M5 Pro/Max models and the new Mac Studio have ~2× the throughput of M4) and integrated; an external Thunderbolt 5 NVMe enclosure (~$80 + a 2 TB drive ~$130) is a fine place for VMs, media, and cold projects.
- 256 GB is only acceptable on a Mac mini used as a desktop with an external drive, or a Neo used as a Chromebook.

### CPU & GPU: how much do cores matter?

- **Compiles and test suites scale with performance cores.** Base M5 (10 cores: 4P+6E) is already faster than an M1 Pro. M5 Pro (15/18 cores) is ~40–60% faster on parallel builds. M5 Max adds GPU, memory bandwidth (up to 614 GB/s on Mac Studio) and memory capacity more than CPU.
- **GPU** matters for ML (Metal/MLX/PyTorch MPS), game development, and video. It does not matter for web/backend/algorithms coursework.
- **External displays**: base M5 drives **two** external displays (Air/Pro), M5 Pro two, M5 Max four, Mac mini three, Mac Studio up to eight. The Neo drives **one**. If you want two monitors on a base chip, you can — this was a real limitation on M1/M2 base chips and is not any more.

### Education pricing and Back to School

- Apple's **Education Store** (apple.com/us-edu/store) is open year-round to current and newly accepted college students, their parents buying on their behalf, and educators at any level. Typical savings: **$100 on Air/mini, $100–$300 on Pro/Studio**, up to **10% off AppleCare+**. Verification is via UNiDAYS in some countries; in the US it's effectively honour-based at checkout for online orders (Apple may ask for proof).
- The **Back to School promotion** (usually early July → late September) stacks on top: in 2026 it's an Apple Gift Card of **up to $150** with a qualifying Mac. It's live at time of writing but ends soon; if you're reading this in October, it's gone until next summer.
- **Refurbished** (apple.com/shop/refurbished): ~15% off, new battery and outer shell, full one-year warranty, AppleCare-eligible. A refurbished M4 Pro 14" is frequently the best value in the store. Stock changes daily; the M5 Air appears there from ~6 months after launch.
- Most universities have a campus store or a Dell/Apple portal with equivalent pricing; check before you buy — some bundle AppleCare or a discount code.
- **Trade-in** values from Apple are conservative; selling a working M1/M2 Mac privately (Swappa, eBay, local) returns 20–40% more.
- US only: Apple Card Monthly Installments (0% APR, 12–24 months) and the new **Apple Upgrade** leasing program (Klarna, from ~$49/month for a Mac Studio) exist. Leasing a laptop you'll keep for four years is rarely the right call.

### Warranty: AppleCare+ or not?

- Every Mac has a one-year limited warranty and 90 days of phone support. In the EU/UK/Australia, consumer law extends coverage of defects to 2–6 years regardless.
- **AppleCare+ for Mac** covers accidental damage (unlimited incidents, $99 screen / $299 other), battery replacement below 80%, and extends the warranty to 3 years (or annual/monthly rolling). For a laptop you carry to class every day, the screen-crack maths usually favours buying it: an out-of-warranty MacBook Pro display is $600–$900. For a Mac mini on a desk, skip it.
- **AppleCare One** (US, $19.99/month) covers three devices with theft & loss on eligible iPhones/iPads; if you already have it, adding your Mac is $5.99/month.
- Students: buy it at the edu discount at purchase time, or within 60 days.

### Accessories that are actually worth it

**Buy on day one**

- A **second charger** for your desk or bag: any USB‑C PD charger ≥ 70 W (Anker, Ugreen, Apple's 70 W). The 16" Pro fast-charges from a 96 W+ brick; the Air ships with a 35 W dual-port or 70 W depending on config — the 70 W is worth the +$20.
- A **USB‑C hub or Thunderbolt dock** if you use an external monitor and wired Ethernet. A Thunderbolt 4/5 dock ($150–$300, CalDigit, OWC, Anker) gives you one-cable docking with charging; a $40 USB‑C hub covers HDMI + 2 USB-A + card reader.
- A **sleeve** for the backpack (tomtoc, Bellroy, Incase).

**External display**

- Coding is where **pixel density** matters most. Look for **"Retina-class"**: 4K at 27" (163 ppi) or 5K at 27" (218 ppi) — text is crisp at 2× scaling. A 1440p 27" monitor (109 ppi) looks blurry next to your MacBook; a 4K 32" (138 ppi) is a good compromise for people who want *space*.
- Value: LG/Dell/BenQ 27" 4K IPS with USB‑C ($300–$500). Premium: **Apple Studio Display (2026)** — 27" 5K 60 Hz, 600 nits, 12 MP camera, Thunderbolt 5, $1,599 — or the **Studio Display XDR** — 5K mini-LED 120 Hz, 2000 nits, $3,299. The Samsung ViewFinity S9 and ASUS ProArt 5K are the 5K alternatives around $1,000–$1,300.
- Avoid ultra-wides *for code* unless you're sure: macOS's window management is happier with two 16:9 panels.

**Input**

- Any keyboard works. Popular with developers: Apple Magic Keyboard with Touch ID (Touch ID unlock for `sudo` and 1Password is genuinely nice), Keychron K-series/Q-series (Mac layout, hot-swap), HHKB, NuPhy Air. Chapter 5 covers key remapping, so Windows layouts are fine too.
- Trackpad vs mouse is personal. The Magic Trackpad enables all the gestures Chapter 6 relies on; Logitech MX Master 3S is the developer-mouse default (Logi Options+ maps its gesture button to Mission Control).
- A **webcam** is unnecessary: the 12 MP Center Stage camera on Air/Pro (and Continuity Camera from an iPhone) is better than most external cameras.

**Audio**: AirPods Pro 3 or any Bluetooth headset works; for many calls a wired USB headset removes Bluetooth latency and drop-outs.

**Storage**: a 2 TB external SSD ($130–$180) for Time Machine (Chapter 17). Get one at least equal in size to your internal drive.

### Second-hand and older Apple silicon

If you're buying used, the ladder of value in 2026 is:

1. **M4 / M4 Pro MacBook Pro (2024)** — still current-feeling, supports everything, 16 GB base.
2. **M3 Pro/Max (2023)** — excellent; the M3 *base* MacBook Air/Pro 8 GB models are the ones to skip.
3. **M2 Air 16 GB (2022)** — the best cheap developer Mac; fanless but fast enough.
4. **M1 Pro/Max 14"/16" (2021)** — legendary battery, still faster than a Neo, 16–64 GB. A 32 GB M1 Max for $900 is a steal.
5. **M1 Air 16 GB (2020)** — fine for coursework, starting to feel its age with Electron apps.

All of these run macOS 27 Golden Gate and will get updates for years (Apple typically supports Macs for 6–8 years). Check battery cycle count (**System Settings → General → About → System Report → Power**; under 500 cycles is good), that Find My is off (Activation Lock!), and that it's not MDM-enrolled (a corporate/school device will re-enrol on erase).

> [!CAUTION]
> **Do not buy an Intel Mac in 2026, even for free-ish money.** macOS 26 Tahoe is the last version they run; security updates end around 2029; Homebrew moves Intel macOS to unsupported this month (no new binary packages) and deletes support in September 2027; Rosetta is going away; battery and thermals are far worse. A $599 MacBook Neo is a better computer than any Intel MacBook ever made.

### What about a Windows or Linux laptop instead?

A fair question for a CS student. Reasons people choose Mac for CS: a Unix userland with a polished GUI, the only platform for iOS/macOS development, best-in-class laptop hardware (battery, display, trackpad, speakers, silence), excellent local-AI performance per watt thanks to unified memory, and the fact that most of your future colleagues' dotfiles and tutorials assume it. Reasons to choose otherwise: you need CUDA (NVIDIA) for ML research, you target Windows-only software (some CAD/EE tooling), you want to dual-boot or run bare-metal Linux (Asahi Linux runs on M1/M2 only, not M3+), or budget — a $600 Neo has real limits and a $600 ThinkPad may have 16 GB and be upgradeable.

You can of course run Linux inside macOS trivially (Chapter 13), and Windows via Parallels or VMware Fusion (free for personal use) — both run Windows 11 ARM, which now runs x86 apps well.

### Checklist before you click Buy

- [ ] Apple silicon, not Intel.
- [ ] ≥ 16 GB memory (24 GB if you'll ever run containers or an emulator; 32 GB+ for mobile/ML).
- [ ] ≥ 512 GB storage (1 TB if mobile/ML/video).
- [ ] Bought through the Education Store (or refurb), with the Back to School gift card if in season.
- [ ] AppleCare+ decided (yes for a daily-carried laptop).
- [ ] Charger ≥ 70 W, sleeve, a Time Machine SSD.
- [ ] If used: Activation Lock off, no MDM, battery < 500 cycles.

[↑ Back to top](#table-of-contents)

---

## 02. First boot, Setup Assistant & migration

The first fifteen minutes with a new Mac contain three or four decisions that are annoying to reverse later: the account name, whether FileVault is on, how much you hand to iCloud, and whether you migrate an old mess onto a clean machine. This chapter walks through them in order, then gets you to a known-good baseline before you install anything.

### Before you unbox: decide these three things

1. **Clean install or migrate?** See [below](#migrate-or-start-clean). Short version: *migrate documents and settings, not applications*, unless the old Mac was set up recently and carefully.
2. **Which Apple Account?** Use your **personal** Apple Account, not a university or employer one — those get deleted when you leave, taking purchases, iCloud data and Find My with you. If the Mac is company-owned and MDM-enrolled, follow IT's instructions; the rest of this guide still applies inside the constraints they set.
3. **Short username.** Setup Assistant derives your home folder name (`/Users/<short name>`) from your full name. Pick something short, lowercase, no spaces — `alex`, not `Alexandra Kowalski`. Renaming it later is possible but fiddly, and it appears in every path you'll ever paste into a chat.

### Setup Assistant, step by step

The order below is macOS 26/27 on a new Mac; a wiped Mac is the same.

| Screen | Recommendation | Why |
|---|---|---|
| Language / Country | Your real region. | Affects date formats, keyboard, App Store country. Changeable later. |
| Accessibility | Skip unless needed. | All of it lives in System Settings → Accessibility. |
| Wi‑Fi | Join your network. | Needed for activation on Apple silicon. |
| Migration Assistant | **"Not now"** if you want a clean setup; see below. | You can run it later from `/Applications/Utilities`. |
| Sign in with your Apple Account | **Sign in.** | Enables Find My (anti-theft), iCloud Keychain (passwords, FileVault recovery key), Passwords app, Continuity. Use 2FA. |
| Create a computer account | Full name; **short username lowercase**; strong password; **"Allow my Apple Account to reset this password" — yes** unless you have a strict threat model. | The reset option is your safety net if you forget the login password; the Recovery Key covers the FileVault side. |
| Location Services | Yes. | Find My, time zone, Weather; per-app control later. |
| Analytics | Off (both toggles) unless you want to help Apple. | |
| Screen Time | Skip. | |
| Siri & Apple Intelligence | Enable if you want; Apple Intelligence downloads ~7 GB of models — fine to enable, configurable later. | On Golden Gate, Siri AI is turned on in Settings afterwards anyway. |
| **FileVault** | **On.** Since Tahoe it's on by default when signed into an Apple Account. Let it store the key in iCloud Keychain. | Full-disk encryption; Chapter 16 explains the recovery-key change. |
| Touch ID | Enrol at least two fingers. | Unlock, `sudo` (Chapter 9), password managers, App Store. |
| Apple Pay | Optional. | |
| Appearance | Auto. | Chapter 3 tunes Liquid Glass. |

When you land on the desktop: **do not start installing apps yet.** Do the baseline below first — ten minutes that save reinstalling.

### Migrate or start clean?

**Migration Assistant** (from a Time Machine backup, another Mac over Wi‑Fi/Thunderbolt, or a Windows PC) copies user accounts, applications, settings and files. It works remarkably well and is the right choice for *non-technical* users. For developers it has a downside: it faithfully copies the accumulated cruft of years — three Python installs, a `/usr/local` Homebrew from Intel days, launch agents from apps deleted in 2022, and 40 GB of `node_modules`.

| Coming from | Do this |
|---|---|
| **Brand new to Mac** (Windows/Linux/Chromebook) | Clean start. Copy documents via cloud drive or external SSD. Windows Migration Assistant is fine for photos/mail/contacts. |
| **Old Mac set up carelessly (most people)** | Clean start + selective migration: sign in to iCloud, copy `~/Documents`, `~/Pictures`, `~/Developer` from a Time Machine or external drive, reinstall apps via a Brewfile (Chapter 8). Keep the old Mac (or its backup) for a month. |
| **Old Mac with dotfiles + Brewfile** | Clean start, then `git clone` your dotfiles and `brew bundle`. This is the payoff of Chapter 10. Under an hour. |
| **Old Intel Mac** | **Do not migrate applications.** It would drag x86 binaries and an Intel Homebrew onto an arm64 machine, and Rosetta is on its way out. Migrate files only. |
| **Company laptop → company laptop** | Whatever IT says; usually Migration Assistant or MDM re-provisioning. |
| **No time this week** | Migrate everything now, do the clean start over a weekend later. Time Machine makes this safe. |

If you do run Migration Assistant, untick *Applications* and *Other files and folders* in the selection screen to get "files and settings only".

Sources, fastest to slowest: a **Time Machine drive** plugged in directly; **Mac-to-Mac over a Thunderbolt cable**; Mac-to-Mac over Wi‑Fi (hours for 500 GB). iCloud Drive with Desktop & Documents sync makes files *appear* once you sign in, but they download on demand — don't rely on it as your only copy during the switch.

### The first 30 minutes: get to a known-good baseline

Each item is expanded in later chapters; this is the checklist.

#### 1. Update macOS

`System Settings → General → Software Update`. New Macs ship with an image that's weeks or months old. Install everything, reboot. Then click ⓘ next to *Automatic Updates* and turn on **all** of: *Check for updates*, *Download new updates*, *Install macOS updates*, *Install application updates from the App Store*, *Install Security Responses and system files*. Also enable **Background Security Improvements** if shown (Tahoe+). Rapid Security Responses (versions with a letter suffix like 27.0.1 (a)) are how Apple patches actively exploited bugs within days — you want them.

> [!NOTE]
> **Golden Gate day-one note.** macOS 27 releases September 14, 2026. If your Mac arrived with Tahoe 26.6, you'll be offered 27.0 as a ~15–20 GB delta update. It's fine to install on day one on a fresh machine; on a work machine with critical tools, waiting for 27.0.1 or 27.1 (2–6 weeks) is the conservative choice. Also note: **installing macOS 27 removes Rosetta 2** if it was present — it can be reinstalled (`softwareupdate --install-rosetta --agree-to-license`), but treat that as a signal to find arm64 versions of whatever needed it.

#### 2. Verify FileVault and save the Recovery Key

`System Settings → Privacy & Security → FileVault` should say **On**. Click **Show** next to the Recovery Key (authenticate with Touch ID) and store the 24-character key in your password manager *as well as* letting it sit in iCloud Keychain. Chapter 16 has the details and the `fdesetup validaterecovery` check.

#### 3. Find My and anti-theft

`System Settings → [Your name] → iCloud → Find My Mac`: on. On Apple silicon this also enables **Activation Lock**, so a stolen Mac can't be erased and reused. On a MacBook, also enable **Stolen Device Protection** (`System Settings → Touch ID & Password`, macOS 26.4+).

#### 4. Fix the basics that annoy developers

Ten quick settings — the rest of System Settings is Chapter 3:

- `Keyboard → Key repeat rate`: fastest. `Delay until repeat`: shortest.
- `Keyboard → Press 🌐 key to`: **Do Nothing** (or Show Emoji & Symbols). Stops accidental emoji pickers.
- `Keyboard → Text Input → Edit…`: turn **off** *Correct spelling automatically*, *Capitalize words automatically*, *Add period with double-space*, and **especially** *Use smart quotes and dashes*. Smart quotes turn `"hello"` into `“hello”` in code pasted into chat, Notes and TextEdit.
- `Trackpad → Point & Click → Tap to click`: on. `Tracking speed`: 7–8 of 10. `Trackpad → More Gestures → App Exposé`: on.
- `Desktop & Dock → Automatically hide and show the Dock`: on. `Show recent applications in Dock`: off.
- `Desktop & Dock → Hot Corners…`: bottom-right → *Lock Screen*; top-right → *Mission Control*.
- `Desktop & Dock → Mission Control → Automatically rearrange Spaces based on most recent use`: **off** (predictable ⌃1–⌃9 desktops).
- `Lock Screen → Require password after screen saver begins or display is turned off`: *Immediately* or *After 1 minute*.
- `General → AirDrop & Handoff → AirDrop`: *Contacts Only*.
- `Appearance → Show scroll bars`: **Always** (wide tables and code views).

#### 5. Finder sanity

Finder → `Settings` (<kbd>⌘</kbd><kbd>,</kbd>):

- *General* → New Finder windows show: **your home folder**.
- *Sidebar*: tick your home folder and *Hard disks*; **untick Recents**.
- *Advanced*: **Show all filename extensions**; **Keep folders on top** (both); *When performing a search*: **Search the Current Folder**; untick *Show warning before changing an extension*.
- In any window: `View → Show Path Bar`, `View → Show Status Bar`, `View → as List`, then `View → Show View Options → Use as Defaults`.
- Hidden files toggle: <kbd>⌘</kbd><kbd>⇧</kbd><kbd>.</kbd> — you need it for `.zshrc`, `.git`, `.env`.

#### 6. Create your directory structure

Decide now where code lives; every script you write will assume it.

```sh
mkdir -p ~/Developer/{scratch,forks,school,work}
```

`~/Developer` is special: macOS gives it a hammer icon, and it's outside the cloud-synced folders. **Never put repositories inside iCloud Drive, Dropbox, OneDrive or Google Drive** — sync clients fight with Git and build tools and will eventually corrupt `.git` or upload gigabytes of `node_modules`. `~/code`, `~/src` or `~/Projects` are equally fine; avoid spaces.

#### 7. Install the command-line developer tools

```sh
xcode-select --install
```

This installs `git`, `clang`, `make`, `swift` and the SDK headers (~2 GB) without the full 15 GB Xcode. Homebrew needs it. Full Xcode is only for iOS/macOS app development — Chapter 7.

#### 8. Sign in where it matters

- App Store (for Xcode and Apple-signed apps; `mas` in your Brewfile uses it).
- Your password manager — Chapter 16. **Set it up before creating any new accounts**; you'll create dozens of developer-service accounts this month.
- Campus Wi‑Fi (802.1X profiles install from your university's onboarding page).

#### 9. Take a snapshot

Plug in your Time Machine SSD and let it do the first backup (Chapter 17). If the next hours of installing go wrong, you can revert to a clean macOS in fifteen minutes.

### The macOS filesystem for developers

A quick map so the rest of the guide makes sense.

| Path | What lives there | Notes |
|---|---|---|
| `/System`, `/usr`, `/bin`, `/sbin` | The **sealed system volume**: read-only, cryptographically signed. | You *cannot* write here even as root (SIP). Use Homebrew's prefix instead. |
| `/Library` | System-wide settings, launch daemons, fonts, Application Support for all users. | Needs admin. |
| `/Applications` | Apps for all users. Homebrew casks install here. | |
| `/opt/homebrew` | **Homebrew on Apple silicon** (`bin/`, `Cellar/`, `Caskroom/`). | `/usr/local` is the *Intel* prefix — its presence on an arm64 Mac means someone installed x86 Homebrew under Rosetta. |
| `~` (`/Users/<you>`) | `Desktop`, `Documents`, `Downloads`, `Library`, `Movies`, `Music`, `Pictures`, `Public`, `Developer`. | |
| `~/Library` | Your app settings (`Preferences/*.plist`), `Caches`, `Application Support`, `LaunchAgents`, `Containers` (sandboxed apps), `Mobile Documents` (iCloud Drive), `Keychains`. | Hidden by default. |
| `~/.config`, `~/.local`, `~/.cache` | XDG directories used by modern CLI tools (Ghostty, mise, starship, nvim, gh…). | Chapter 10 puts these under version control. |
| `/private/etc`, `/private/var`, `/private/tmp` | Unix config, variable data, temp; `/etc`, `/var`, `/tmp` are symlinks to them. | `/etc/zshrc`, `/etc/paths`, `/etc/hosts`, `/etc/ssh/` live here. |
| `/Volumes` | Mounted disks, DMGs, network shares. | Your boot volume is `/` and also `/Volumes/Macintosh HD`. |
| `/Applications/Utilities` | Terminal, Activity Monitor, Disk Utility, Console, Migration Assistant, Screen Sharing… | |

Two Apple-silicon concepts worth knowing on day one:

- **APFS volume group**: your disk is one APFS container holding a sealed *System* volume, a *Data* volume (mounted at `/System/Volumes/Data` and firmlinked into the tree so it looks like one filesystem), *Preboot*, *Recovery* and *VM* (swap). Snapshots are cheap, which is how Time Machine local snapshots and macOS updates roll back.
- **Recovery**: shut down, then *press and hold the power button* until "Loading startup options" appears → *Options*. From there: reinstall macOS, restore from Time Machine, Disk Utility, **Startup Security Utility** (needed for kernel extensions and some tiling window managers — Chapter 6), Terminal. There is no <kbd>⌘</kbd><kbd>R</kbd> on Apple silicon.

### Erasing and reinstalling

`System Settings → General → Transfer or Reset → Erase All Content and Settings` wipes the Data volume, removes your Apple Account and Activation Lock, and returns to Setup Assistant in ~5 minutes *without* reinstalling macOS. It's the right way to sell a Mac and the fastest way to restart a botched setup. For a fully fresh OS image, use Recovery → Reinstall macOS, or restore the Mac from another Mac via Finder/Apple Configurator with an IPSW (DFU mode) — the nuclear option for a Mac that won't boot.

### Common first-week problems

- **"Your system has run out of application memory" / beach-balling on 8–16 GB**: check Activity Monitor → Memory → *Memory Pressure*. Close Chrome tabs, quit idle Electron apps. Revisit Chapter 1's memory table before Apple's 14-day return window closes.
- **Battery draining fast for two days**: Spotlight indexing, Photos analysis and Apple Intelligence model downloads run flat out after setup. It settles.
- **A dialog asks for a password you don't recognise**: usually your *login* password (for Keychain), not your Apple Account password. If a *former owner's* Apple Account is requested, the Mac has Activation Lock — return it.
- **Migration brought over an Intel Homebrew** (`/usr/local/bin/brew` exists; `brew config` shows `Rosetta 2: true`): uninstall it (Chapter 8) and install fresh under `/opt/homebrew`.
- **Can't find Launchpad**: removed in Tahoe. <kbd>⌘</kbd><kbd>Space</kbd> then <kbd>⌘</kbd><kbd>1</kbd> shows the Apps grid (Chapter 4), or pinch with four fingers on the trackpad.

[↑ Back to top](#table-of-contents)

---

## 03. System Settings, pane by pane

System Settings (the iOS-style app that replaced System Preferences in Ventura) has ~30 panes. Most defaults are fine. This chapter lists the settings that materially change how a developer's Mac behaves, in the order the sidebar shows them, with the `defaults write` equivalent where one exists so you can script them (Appendix A does exactly that). Skip anything you don't care about.

> [!TIP]
> Search the Settings sidebar (<kbd>⌘</kbd><kbd>F</kbd> inside the app) rather than hunting through panes. You can also jump straight to a pane from Spotlight — type "trackpad" and press Return.

### Wi‑Fi, Bluetooth, Network

- **Wi‑Fi → ⓘ next to your network → Private Wi‑Fi address**: *Rotating* is the default on public networks and fine; set to *Fixed* on your home network if you use DHCP reservations. Off breaks nothing but reduces privacy.
- **Wi‑Fi → ⓘ → Limit IP address tracking**: on (iCloud Private Relay for Safari/Mail).
- **Network → Wi‑Fi → Details → DNS**: consider `1.1.1.1`/`1.0.0.1` (Cloudflare), `9.9.9.9` (Quad9, malware-blocking) or `8.8.8.8`. Campus networks sometimes require their own DNS for internal hosts; if a lab server stops resolving, this is why.
- **Network → Firewall**: **on**. Click *Options*: *Block all incoming connections* off (breaks AirDrop/file sharing), *Automatically allow built-in software*: on, *Automatically allow downloaded signed software*: on, **Enable stealth mode**: on. The macOS firewall is application-based, not port-based; for port rules use `pf` (Chapter 16).
- **Network → VPN & Filters**: if your university or employer uses a VPN, install its profile here. Modern choices are WireGuard-based (Tailscale is excellent for reaching your home machine or a lab box — Chapter 14).
- **Bluetooth**: pair your keyboard/mouse/AirPods. In Tahoe the menu bar Bluetooth icon is inside Control Center; pin it (see below).

### Battery

- **Low Power Mode**: *Only on Battery* is a good default for students — it caps peak performance and dramatically extends lecture-day battery life. *Never* for engineers who want compiles fast on battery.
- **Charging → Optimized Battery Charging**: on.
- **Charging → Charge Limit** (macOS 26.4+): if the Mac lives on a dock most of the day, set **80%**. Lithium cells age fastest at 100% and warm; this single toggle is the best thing you can do for a 4-year battery. Toggle to 100% before a long day away.
- **Options → Prevent automatic sleeping on power adapter when the display is off**: on if you run servers/long builds on a docked laptop; otherwise off.
- **Options → Wake for network access**: *Only on Power Adapter*.
- Battery health: `System Settings → Battery → Battery Health ⓘ` shows maximum capacity and cycle count. Under 80% after 1000 cycles is the AppleCare replacement threshold.

### General

- **Software Update**: covered in Chapter 2. Everything on, including *Install Security Responses and system files* and *Background Security Improvements*.
- **Storage**: shows categories; the useful button is *Developer* → delete old Xcode caches and simulator runtimes (Chapter 7 does this from the CLI). Turn **on** *Empty Trash automatically* (30 days). Leave *Optimize Storage* and *Store in iCloud* **off** on a dev machine — you do not want macOS evicting your Documents to the cloud.
- **AirDrop & Handoff**: AirDrop *Contacts Only*; Handoff on; *iPhone Cellular Calls* on if you like the Phone app.
- **AutoFill & Passwords**: choose your password manager here (Passwords app, 1Password, Bitwarden…). Turn off duplicates — having two autofill providers is confusing.
- **Date & Time**: 24-hour time on (developers read logs). Set time zone automatically.
- **Language & Region**: *Temperature*, *Measurement system*, *First day of week* to taste. Add a second language here if you type in one. **Translation languages** download packs for Live Translation.
- **Login Items & Extensions**: this is where you'll audit what starts at login (Chapter 18). Anything you don't recognise: right-click → Show in Finder before deleting. *Extensions → File Providers / Finder / Quick Look / Sharing* lists third-party plug-ins.
- **Sharing**: everything **off** unless you need it. **Remote Login (SSH)**: on only if you SSH *into* this Mac (e.g. from your iPad or a Raspberry Pi); restrict to your user, and use keys (Chapter 9). **Screen Sharing** on only if you remote-control it. *Hostname* at the bottom — set something short like `alex-mbp` (this becomes your `.local` mDNS name and shows in the Terminal prompt).
- **Time Machine**: Chapter 17.
- **Transfer or Reset**: erase to sell; Migration Assistant lives here too.

### Accessibility

Not just for disability: several of the most useful *productivity* toggles live here.

- **Display → Reduce motion**: on if Spaces-swiping animations bother you; makes desktop switching snappier.
- **Display → Reduce transparency**: on if Liquid Glass hurts legibility. In macOS 27 prefer the **Liquid Glass slider** in Appearance (below).
- **Display → Pointer → Shake mouse pointer to locate**: on for multi-monitor setups.
- **Zoom → Use scroll gesture with modifier keys to zoom**: on, modifier <kbd>⌃</kbd>. Hold Control and two-finger scroll to zoom into any pixel — invaluable for checking UI alignment and reading small diagrams in lecture PDFs.
- **Pointer Control → Trackpad Options → Use trackpad for dragging → Three Finger Drag**: on. Move windows and select text by dragging with three fingers instead of click-and-hold. Most long-time Mac users consider this the single best hidden setting.
- **Keyboard → Full Keyboard Access**: on if you want to Tab through *every* control in dialogs (also see Keyboard → Keyboard navigation).
- **Spoken Content / Live Captions / Voice Control**: real accessibility features; also nice for proofreading essays (select text → Speech).

### Appearance

- **Appearance**: *Auto* switches Light/Dark with sunset. Dark mode is easier on the eyes for long code sessions; Light is more legible in sunlight. Many editors follow the system.
- **Accent color / Highlight color**: taste. Since Tahoe the *text highlight* colour is separate from the accent colour.
- **Liquid Glass** (Tahoe 26.1+: *Clear / Tinted*; **Golden Gate: a slider** from fully clear to fully tinted): if you find window chrome hard to read, move towards *Tinted*. This doesn't cost performance.
- **Opaque menu bar**: on if the transparent menu bar bugs you.
- **Icon & Widget Style**: *Default* (colour), *Light*, *Dark*, *Clear*, *Tinted*. Default is the most legible for quickly spotting apps in the Dock.
- **Folder Color**: system-wide folder tint; per-folder customisation is in Finder (right-click → Customize Folder).
- **Sidebar icon size**: *Small* fits more Finder sidebar items.
- **Show scroll bars**: **Always**. **Click in the scroll bar to**: *Jump to the spot that's clicked*.

### Apple Intelligence & Siri

- Toggle **Apple Intelligence** globally here. In Golden Gate this also enables **Siri AI** (the LLM assistant that lives in Spotlight and the Siri app). Requirements: any Apple silicon Mac; custom Siri voice and improved on-device dictation need M3+ and 12 GB+.
- **Siri → Keyboard shortcut**: *Hold 🌐 Space* or *Off*. Golden Gate's Spotlight ("Search or Ask") handles typed requests, so voice activation is optional.
- **Extensions → ChatGPT / other providers**: opt-in; Siri can hand off to ChatGPT. You can use it without an OpenAI account (anonymised) or sign in.
- **Privacy**: Apple Intelligence runs on-device where it can and otherwise on **Private Cloud Compute** (Apple-attested servers; in 2026 some capacity runs on Google Cloud with NVIDIA hardware under the same attestation model). If you handle confidential code or data (NDA'd employer, research data), read your employer's policy — Writing Tools on selected text sends that text to PCC. You can disable individual features (Writing Tools, Image Playground, Notification summaries) here.
- **Siri Suggestions & Privacy → Learn from this App**: turn off for apps you don't want indexed into the semantic index (e.g. a banking app).

### Control Center

Everything about the menu bar lives here.

- **Bluetooth, Wi‑Fi, Sound, Now Playing, Screen Mirroring**: *Show in Menu Bar* for the ones you toggle often; the rest stay inside Control Center. You can also **right-click any control inside Control Center → Pin to Menu Bar** (Tahoe+), and **Edit Controls** to add third-party controls.
- **Battery → Show Percentage**: on.
- **Clock options**: *Show the day of the week*, *Show date: Always*, *24-hour*, optionally *Display the time with seconds* (handy when you're timing things).
- **Spotlight**: hide the menu bar icon (you use <kbd>⌘</kbd><kbd>Space</kbd>).
- **Menu Bar Only → Automatically hide and show the menu bar**: *Never* on a laptop screen (the notch region is otherwise wasted); *In Full Screen Only* is the default.
- Reorder menu bar items by <kbd>⌘</kbd>-dragging; remove third-party ones by <kbd>⌘</kbd>-dragging out. If you have more than ~12 icons they disappear behind the notch — see *Ice* or *Bartender* in Chapter 19.

### Desktop & Dock

- **Dock size**: small. **Magnification**: off or subtle. **Position**: *Left* or *Bottom* — Left frees vertical pixels on a 16:10 laptop screen; Bottom is what muscle memory expects.
- **Minimize windows using**: *Scale effect* (faster). **Double-click a window's title bar to**: *Zoom* or *Fill*. **Minimize windows into application icon**: on.
- **Automatically hide and show the Dock**: on. Remove the show delay entirely: `defaults write com.apple.dock autohide-delay -float 0; defaults write com.apple.dock autohide-time-modifier -float 0.15; killall Dock`.
- **Show suggested and recent apps in Dock**: off.
- **Desktop & Stage Manager → Click wallpaper to reveal desktop**: *Only in Stage Manager* (otherwise every stray click on the desktop shoves your windows aside to show widgets).
- **Show items → On Desktop / In Stage Manager**: your call; a clean desktop is faster (Finder renders every icon).
- **Widgets → Show Widgets on Desktop**: off if you never look at them; they cost a little battery.
- **Default web browser**: set it here. **Default terminal** is *not* a system setting — Ghostty offers "Set as default terminal" (Chapter 9).
- **Windows → Prefer tabs when opening documents**: *Always* (Finder, Terminal, TextEdit, Preview then open new docs as tabs).
- **Windows → Tiled windows have margins**: **off** (tighter tiling; Chapter 6). **Drag windows to screen edges to tile**: on. **Drag windows to menu bar to fill screen**: on. **Hold ⌥ key while dragging windows to tile**: on.
- **Mission Control**: *Automatically rearrange Spaces based on most recent use*: **off**. *When switching to an application, switch to a Space with open windows for the application*: on. *Group windows by application*: off (shows every window in Mission Control). **Displays have separate Spaces**: on for multi-monitor.
- **Hot Corners…**: bottom-right *Lock Screen*, top-right *Mission Control*, top-left *Desktop* (reveal), bottom-left *Quick Note* or *–*. Set a modifier (hold <kbd>⌘</kbd>) if you trigger them accidentally.

### Displays

- **Resolution**: for the built-in display, *Default* is right; the "More Space" step is legible on 14"/16" Pro screens and gives a lot more code per screen at the cost of slightly smaller text. Use *Show all resolutions* (right-click a preset) if you need an exact size.
- **Refresh rate**: *ProMotion* (adaptive up to 120 Hz) on Pro. Externals: pick the highest available.
- **External display arrangement**: drag to match physical layout; drag the white menu-bar strip to the display you want as *main* (where new windows and the Dock appear).
- **Night Shift**: schedule *Sunset to Sunrise*, warmth ~50%. **True Tone**: off if you do colour-sensitive work; on for reading.
- **Advanced → Show resolutions as list**; *Allow your pointer and keyboard to move between any nearby Mac or iPad* (Universal Control).
- Text on a non-Retina external monitor looks thin because Apple removed subpixel antialiasing in Mojave. Improve it slightly with `defaults -currentHost write -g AppleFontSmoothing -int 2` (log out to apply) — or, better, buy a 4K/5K display (Chapter 1).

### Screen Saver, Lock Screen, Wallpaper

- **Lock Screen → Start Screen Saver when inactive**: 10–20 min. **Turn display off on battery**: 5 min; **on power adapter**: 15–20 min. **Require password after…**: *Immediately* (with Touch ID it's painless). **Show large clock**: on.
- **Show message when locked**: put your name + a contact email ("If found, please email …"). This is the free version of a lost-laptop recovery plan.
- **Wallpaper**: pick something dark and low-contrast if you spend the day looking at semi-transparent Liquid Glass. Dynamic wallpapers cost a trivial amount of battery.
- Screen Saver → *Show as wallpaper*: on for the animated Aerials (looks great, harmless).

### Notifications & Focus

- **Show previews**: *When Unlocked*.
- **Allow notifications when the display is sleeping / locked / mirroring**: off, off, off (don't leak Slack messages onto a projector).
- Go app by app: Slack/Teams/Discord → *Banners*, sounds off, badges on; Mail → badges only; Calendar → alerts; everything else → off. **Summarize previews** (Apple Intelligence) is fine for group chats.
- **Focus**: create a *Work* focus (allow calendar, your team chat; block social) and a *Do Not Disturb* schedule for sleep. Enable *Share across devices*. Tie **Focus filters** to apps (Safari tab group, Mail account, Calendar set). Chapter 21 automates Focus with Shortcuts.

### Sound

- **Alert volume**: low. **Play sound on startup**: your call (off for lecture halls). **Play feedback when volume is changed**: on.
- **Output**: if you use a USB DAC or dock audio, macOS remembers per-device volume. Hold <kbd>⌥</kbd> while clicking the Sound menu item to switch input/output quickly.

### Touch ID & Password

- Enrol 2–3 fingers. Enable **Use Touch ID for**: unlocking, Apple Pay, iTunes/App Store, autofill, *fast user switching*.
- **Stolen Device Protection** (MacBooks, 26.4+): on.
- **Apple Watch**: unlock and approve requests with your watch if you have one.
- Touch ID for `sudo` in Terminal is configured in `/etc/pam.d/sudo_local` — Chapter 9.

### Users & Groups

- Best practice (and what the ERNW Tahoe hardening guide recommends): a **standard** account for daily use and a separate **admin** account you never log into but authenticate as when needed. The practical cost on a single-user machine is a few extra password prompts per week; the benefit is that malware running as you can't silently gain root. Homebrew is fine in this model — install it while temporarily admin (or authenticate once), then `sudo chown -R $(whoami) /opt/homebrew`. If this is too much friction, at least *don't* enable automatic login.
- **Automatic login**: off (it's disabled anyway when FileVault is on).
- **Guest User**: off (Find My can still show a guest login screen on a locked Mac regardless).
- **Login Options** (click ⓘ): *Show password hints*: off. *Fast User Switching* menu: off unless shared.

### Internet Accounts, Game Center, iCloud, Wallet

- **iCloud → iCloud Drive → Desktop & Documents Folders**: **off** on a developer Mac unless you keep code elsewhere. On is convenient for a student who wants essays on iPad and Mac — just keep `~/Developer` outside it.
- **iCloud → Optimize Mac Storage**: off if you have ≥ 512 GB; you don't want files evicted.
- **Advanced Data Protection**: **on**. End-to-end encrypts iCloud Drive, Photos, Notes, Backups, Reminders, Messages in iCloud. Requires a recovery contact or recovery key (set both up, store the key in your password manager).
- **Access iCloud Data on the Web**: on if you use icloud.com.
- **Private Relay** (iCloud+): on for Safari; it can interfere with campus networks that require local DNS — turn off per-network if so.
- **Hide My Email**: use it for every signup that isn't a professional identity.
- **Passwords app**: Chapter 16. Turn on **Detect Compromised Passwords** and, on Golden Gate, review the **automatic password change** feature for weak/compromised logins.

### Keyboard

Covered in depth in Chapter 5. The essentials:

- **Key repeat rate**: fastest; **Delay until repeat**: shortest. Faster still via `defaults write -g KeyRepeat -int 1; defaults write -g InitialKeyRepeat -int 10` (values below the slider's minimum; log out to apply).
- **Adjust keyboard brightness in low light**: on. **Keyboard brightness → Turn keyboard backlight off after inactivity**: 1 min.
- **Press 🌐 key to**: *Do Nothing*. **Keyboard navigation**: on (Tab moves focus across all controls).
- **Text Input → Input Sources → Edit…**: *Show Input menu in menu bar* if you switch layouts; **Correct spelling automatically**: off; **Capitalize words automatically**: off; **Show inline predictive text**: off (it's distracting when coding in text fields); **Add period with double-space**: off; **Use smart quotes and dashes**: **OFF**.
- **Text Replacements**: add your email, address, and snippets like `;date` → today's date (or use a snippets tool — Chapter 19). They sync via iCloud.
- **Keyboard Shortcuts…**: see Chapter 5 for the remaps; at minimum **Modifier Keys…** → map <kbd>Caps Lock</kbd> to <kbd>⌃ Control</kbd> (or <kbd>⎋ Escape</kbd> for Vim users), and in *Mission Control* turn on <kbd>⌃</kbd><kbd>1</kbd>…<kbd>⌃</kbd><kbd>9</kbd> *Switch to Desktop N*. In *Spotlight*, check that <kbd>⌘</kbd><kbd>Space</kbd> isn't hijacked by an input-source switcher (*Input Sources → Select the previous input source* — move it to <kbd>⌃</kbd><kbd>Space</kbd> or off).
- **Dictation**: on if you use it; it's on-device and works offline. Shortcut: *Press 🌐 twice* or off.

### Trackpad & Mouse

- **Point & Click**: *Tracking speed* 7–8; *Click* Medium; *Force Click and haptic feedback* on; *Look up & data detectors*: *Tap with Three Fingers* (keeps Force-click for other uses); *Secondary click*: *Click or Tap with Two Fingers*; **Tap to click**: on.
- **Scroll & Zoom**: *Natural scrolling*: your call (on matches iPhone; off matches Windows and scroll wheels — the *Mouse* pane has an independent toggle since Tahoe, so you can have natural on trackpad and traditional on mouse). Smart zoom, rotate: on.
- **More Gestures**: *Swipe between pages*: two fingers; *Swipe between full-screen applications*: **three or four fingers** (this is how you move between Spaces — Chapter 6); *Notification Center*: two-finger swipe from right edge; *Mission Control*: swipe up with three/four fingers; **App Exposé**: swipe down (on); *Launchpad*: pinch (still works as Apps view); *Show Desktop*: spread.
- **Mouse** (Magic Mouse or third-party): *Tracking speed* high; *Scrolling speed* high; disable **mouse acceleration** if you game or want 1:1 movement: `defaults write -g com.apple.mouse.scaling -1` (log out). Logitech users: install *Logi Options+* for gesture mapping; steer clear of old *Logitech Control Center*.

### Printers, Game Controllers, Passwords, Screen Time

- **Printers & Scanners**: add your campus printer via IPP/AirPrint; most universities publish a queue URL. Nothing else to configure.
- **Screen Time**: useful for *yourself* — set *Downtime* for sleep and *App Limits* for whatever eats your evenings. It also shows honest weekly usage.

### Privacy & Security

The most important pane; Chapter 16 goes deep. Quick pass:

- **Location Services**: on; scroll down → *System Services → Details*: leave *Find My Mac*, *Time zone*, *Networking* on; *Significant locations* and *Mac analytics* off if you like.
- **Full Disk Access / Files and Folders / Accessibility / Input Monitoring / Screen & System Audio Recording / Automation**: these fill up as you install tools (terminals, window managers, Raycast, screen recorders). Review quarterly; remove anything you uninstalled. A tiling window manager or text expander will need *Accessibility*. A terminal will ask for *Full Disk Access* when you `ls ~/Library/Mail`.
- **Local Network**: apps that scan your LAN (Spotify, dev servers, Docker) ask here.
- **App Management**: allow your editor/updater (e.g. Homebrew via Terminal) to modify other apps.
- **Developer Tools**: add Terminal/Ghostty so you can run unsigned binaries you built yourself without Gatekeeper prompts.
- **Security → Allow applications from**: *App Store & Known Developers*. There is no "Anywhere" option in the UI since Sequoia, and `sudo spctl --master-disable` no longer works. To open an unsigned app: try to open it, get refused, then come back here and click **Open Anyway** (within an hour). Or remove the quarantine flag: `xattr -d com.apple.quarantine /Applications/Foo.app`. Homebrew casks can install with `--no-quarantine`.
- **FileVault**: on; Recovery Key stored.
- **Lockdown Mode**: off for everyone except journalists/activists/people with a specific adversary — it disables JIT in Safari, blocks most attachments, and breaks many dev sites.
- **Advanced… (at the bottom)**: *Log out automatically after inactivity*: off (kills long-running jobs); **Require an administrator password to access system-wide settings**: on; *Allow accessories to connect*: **Ask for New Accessories** (this is the USB data-blocker — a good default for laptops).
- **Analytics & Improvements**: off. **Apple Advertising → Personalized Ads**: off.

### Scripting these settings

Every checkbox above is stored in a `.plist` under `~/Library/Preferences` (per-user) or `/Library/Preferences` (system) and can be set with `defaults write`. Apps read them at launch, so most changes need `killall Dock`, `killall Finder`, `killall SystemUIServer` or a logout. Appendix A collects our recommended set into a single idempotent script; here is the flavour:

```sh
# Finder: show extensions, path bar, status bar, list view, hidden ~/Library
defaults write NSGlobalDomain AppleShowAllExtensions -bool true
defaults write com.apple.finder ShowPathbar -bool true
defaults write com.apple.finder ShowStatusBar -bool true
defaults write com.apple.finder FXPreferredViewStyle -string "Nlsv"
defaults write com.apple.finder FXDefaultSearchScope -string "SCcf"
defaults write com.apple.finder _FXSortFoldersFirst -bool true
chflags nohidden ~/Library

# Dock: autohide fast, no recents, small
defaults write com.apple.dock autohide -bool true
defaults write com.apple.dock autohide-delay -float 0
defaults write com.apple.dock autohide-time-modifier -float 0.15
defaults write com.apple.dock show-recents -bool false
defaults write com.apple.dock tilesize -int 40
defaults write com.apple.dock mru-spaces -bool false

# Keyboard: fast repeat, no autocorrect/smart quotes
defaults write NSGlobalDomain KeyRepeat -int 1
defaults write NSGlobalDomain InitialKeyRepeat -int 10
defaults write NSGlobalDomain NSAutomaticSpellingCorrectionEnabled -bool false
defaults write NSGlobalDomain NSAutomaticCapitalizationEnabled -bool false
defaults write NSGlobalDomain NSAutomaticPeriodSubstitutionEnabled -bool false
defaults write NSGlobalDomain NSAutomaticQuoteSubstitutionEnabled -bool false
defaults write NSGlobalDomain NSAutomaticDashSubstitutionEnabled -bool false
defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool false   # key repeat instead of accent popup

# Trackpad: tap to click, three-finger drag
defaults write com.apple.AppleMultitouchTrackpad Clicking -bool true
defaults write com.apple.AppleMultitouchTrackpad TrackpadThreeFingerDrag -bool true

# Screenshots: PNG into ~/Pictures/Screenshots, no shadow
mkdir -p ~/Pictures/Screenshots
defaults write com.apple.screencapture location -string "$HOME/Pictures/Screenshots"
defaults write com.apple.screencapture disable-shadow -bool true

# Misc: expand save/print dialogs, always show scroll bars, 24h clock
defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode -bool true
defaults write NSGlobalDomain PMPrintingExpandedStateForPrint -bool true
defaults write NSGlobalDomain AppleShowScrollBars -string "Always"
defaults write com.apple.menuextra.clock Show24Hour -bool true

killall Dock Finder SystemUIServer 2>/dev/null
```

Two cautions: (1) Apple silently renames or removes keys between releases — verify with `defaults read <domain>` after a major upgrade; a key that no longer exists is harmless but does nothing. (2) A handful of settings (Accessibility permissions, FileVault, Firewall state, Gatekeeper) *cannot* be set with `defaults` for security reasons; they need `sudo` tooling (`fdesetup`, `/usr/libexec/ApplicationFirewall/socketfilterfw`, `spctl`) or an MDM profile. Appendix A handles those separately.

To discover the key for any checkbox: run `defaults read > /tmp/before.txt`, flip the setting, `defaults read > /tmp/after.txt`, and `diff` them.

[↑ Back to top](#table-of-contents)

---

## 04. Finder, Dock & Spotlight

Three built-in tools you'll touch hundreds of times a day. Finder is more capable than its reputation; the Dock is best minimised; and Spotlight, since macOS 26, is a genuine launcher that changes the calculus on Raycast and Alfred.

### Finder

#### Views and navigation

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

#### Sidebar, toolbar and favourites

- Drag your project folders, `~/Developer`, and `~/Library` (after `chflags nohidden ~/Library`) into the sidebar's *Favorites*. Remove *Recents* and *AirDrop*.
- Right-click the toolbar → *Customize Toolbar…*: add *Path*, *New Folder*, *Get Info*, *Delete*, *Connect*, and a **Quick Actions** button. Drag any app or script onto the toolbar while holding <kbd>⌘</kbd> to get a one-click launcher (e.g. your terminal or editor: drop VS Code there and drag folders onto it).
- **Connect to Server** (<kbd>⌘</kbd><kbd>K</kbd>): `smb://nas.local/share`, `nfs://`, `ftp://`, `vnc://`. Tick *Remember* and add to Favorites. Golden Gate speeds up SMB browsing noticeably.

#### Quick Look

Select a file and press <kbd>Space</kbd>. It previews images, PDFs, video, Office docs, and — with plugins — code, Markdown, JSON, archives and more. <kbd>⌘</kbd><kbd>Y</kbd> also works. Arrow keys move through the selection; <kbd>⌥</kbd><kbd>Space</kbd> opens full screen. Quick Look supports *Markup* (annotate PDFs/images) and *Trim* (video) directly.

Essential Quick Look extensions for developers (all via Homebrew, all free):

```sh
brew install --cask qlmarkdown syntax-highlight   # Markdown preview; syntax-highlighted source for 100+ languages
brew install --cask quicklook-json qlstephen      # pretty JSON; plain-text files without extensions (README, Makefile, LICENSE)
brew install --cask quicklook-csv qlvideo         # CSV as table; thumbnails for more video codecs
brew install --cask betterzip                     # peek inside zip/tar without extracting (paid, but the QL plugin works in trial)
```

After installing, run `qlmanage -r` to reload, and approve each extension in `System Settings → General → Login Items & Extensions → Quick Look`.

#### Smart Folders and Spotlight queries

`File → New Smart Folder` builds a saved search. Examples worth saving to the sidebar:

- *Kind is Source Code, Modified within last 7 days* → "This week's code".
- *Name contains `.env`* in `~/Developer` → occasional audit of secrets on disk.
- *Size > 500 MB* → what's eating the disk (also see `ncdu`, Chapter 18).

Raw query syntax works in the Finder search field and Spotlight: `kind:pdf date:this week`, `name:report kind:document`, `tag:urgent`, `modified:>2026-09-01`. In the search field, click the **+** to add criteria and *Other…* to pick from hundreds of metadata attributes (e.g. *Pixel width*, *Codec*).

#### Archive and disk images

- Right-click → *Compress* makes a `.zip` (Archive Utility handles zip, tar.gz, bz2, xz; **not** rar or 7z — use `brew install --cask keka` or `brew install sevenzip`).
- Disk images: double-click a `.dmg` to mount; drag the app to `/Applications`; **eject** the image from the sidebar afterwards. Since Tahoe, new images default to **ASIF** (Apple Sparse Image Format), which is dramatically faster and near-native SSD speed — the right format for VM disks and encrypted vaults: `Disk Utility → File → New Image → Blank Image → Format: APFS, Encryption: 256-bit AES, Image Format: sparse` gives you an encrypted folder that mounts with a password.

#### Things Finder still doesn't do well (and fixes)

| Gap | Fix |
|---|---|
| Two-pane file management (Norton Commander style) | **Marta** (free), **ForkLift 4**, **Commander One**; or `yazi` in the terminal (Chapter 9) |
| Bulk operations on thousands of files | Terminal: `fd`, `rg`, `rsync` — Chapter 9 |
| Show folder sizes instantly | `View → Show View Options → Calculate all sizes` (List view), or **OmniDiskSweeper** / `ncdu` |
| Cut (⌘X) files | Use <kbd>⌘</kbd><kbd>C</kbd> then <kbd>⌘</kbd><kbd>⌥</kbd><kbd>V</kbd> — Finder's "Move here" |
| Open a folder as a *project* | Drag it onto your editor's Dock icon, or `code .`, `zed .`, `cursor .` from Terminal |
| Automatic Downloads cleanup | **Hazel** (paid) rules, or a Shortcuts folder automation — Chapter 21 |
| `.DS_Store` files on network shares / repos | `defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true; defaults write com.apple.desktopservices DSDontWriteUSBStores -bool true` and add `.DS_Store` to your global gitignore (Chapter 10) |

### The Dock

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

### Spotlight (macOS 26+)

Spotlight was rebuilt in Tahoe and became a real launcher, then got Siri AI inside it in Golden Gate. If you last used it in Sonoma, relearn it.

#### The four views

Press <kbd>⌘</kbd><kbd>Space</kbd>, then:

| Key | View | What it does |
|---|---|---|
| <kbd>⌘</kbd><kbd>1</kbd> | **Apps** | A grid of every installed app (this replaced Launchpad, which is gone), including iPhone apps via iPhone Mirroring. Type to filter. |
| <kbd>⌘</kbd><kbd>2</kbd> | **Files** | Recent files with type filters at the top; supports **slash filters** `/pdf`, `/word`, `/image`, `/text` then <kbd>Return</kbd>. |
| <kbd>⌘</kbd><kbd>3</kbd> | **Actions** | Hundreds of system and app commands: *Send Message*, *Create Event*, *Set Timer*, *Convert to PDF*, *Resize Image*, run any **Shortcut**. Apps expose their own via App Intents (e.g. Ghostty can focus a terminal). |
| <kbd>⌘</kbd><kbd>4</kbd> | **Clipboard** | Clipboard history (see below). |

Other shortcuts inside Spotlight: <kbd>↑</kbd> recalls previous *searches* (like shell history); <kbd>⌘</kbd><kbd>Return</kbd> reveals the selected file in Finder; <kbd>⌘</kbd><kbd>C</kbd> copies the result's path; <kbd>Tab</kbd> or <kbd>⌘</kbd><kbd>I</kbd> shows a preview/info pane; <kbd>⌘</kbd><kbd>L</kbd> jumps to the dictionary definition; <kbd>⌘</kbd><kbd>B</kbd> searches the web. Type maths (`2^32-1`, `15% of 84`, `120 usd in eur`, `3pm PST in London`) and get answers inline.

#### Quick Keys

Spotlight assigns short abbreviations to your most-used *actions*: type `sm` → *Send Message*, `cr` → *Create Reminder*, `nn` → *New Note*, then <kbd>Return</kbd> and fill in the parameters inline without opening the app. They're auto-assigned by usage; see and reset them in `System Settings → Spotlight`. Any Shortcut you build (Chapter 21) becomes an action and can get a Quick Key — this is how you run "Start Deep Work Focus + open project + start timer" from four keystrokes.

#### Clipboard history

Enable it once (Spotlight → <kbd>⌘</kbd><kbd>4</kbd> → *Turn On*, or `System Settings → Spotlight → Clipboard History`). It records text, images, files and URLs with source app and timestamp. <kbd>Return</kbd> pastes as **plain text** at the cursor (so it also replaces the old <kbd>⌘</kbd><kbd>⌥</kbd><kbd>⇧</kbd><kbd>V</kbd> paste-and-match-style habit); the small button to the right of an item makes it the *current* clipboard instead.

Limits you should know: **items expire after 8 hours**, nothing can be pinned, and there's no single-key shortcut to open the clipboard view — it's <kbd>⌘</kbd><kbd>Space</kbd> then <kbd>⌘</kbd><kbd>4</kbd>. Passwords copied from Apple's Passwords app are excluded, but third-party managers' copies may appear — copy something else right after pasting a secret. For persistent, pinnable history, add **Maccy** (free, open source, `brew install --cask maccy`) or use Raycast's clipboard manager.

#### Search settings

`System Settings → Spotlight`: turn off categories you never want in results (*Siri Suggestions*, *Websites*, *Movies*, *Fonts*), and **Search Privacy…** to exclude folders — add your `node_modules`-heavy monorepo, VM disk folders, and Time Machine drives if indexing them slows things. Golden Gate rebuilt the search index (26.6 pre-optimised it); if search is wrong or slow, rebuild with `sudo mdutil -E /` and give it an hour.

For developers, note that Spotlight indexes file *contents* for text, code, PDFs and Office docs; `mdfind "kind:source 'TODO'"` uses the same index from the CLI, and `mdls file` shows the metadata it extracted.

#### Siri AI in Spotlight (Golden Gate)

In macOS 27, <kbd>⌘</kbd><kbd>Space</kbd> is labelled **Search or Ask**. Plain queries search as before; questions ("what's the door code Sarah texted me", "summarise this PDF", "convert this table to CSV") are routed to Siri AI, which can read your local index (Mail, Messages, Notes, Files) and take actions in apps. Attach files with the **+**. **Visual Intelligence** is <kbd>⌘</kbd><kbd>⇧</kbd><kbd>Space</kbd>: drag a rectangle on screen and ask about it (great for "what does this compiler error mean" without copying text). Siri AI is opt-in (`System Settings → Apple Intelligence & Siri`) and English-only at launch; requests that leave the device go to Private Cloud Compute. If you'd rather Spotlight *only* searched, turn Siri AI off there.

### Raycast, Alfred, LaunchBar: do you still need one?

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

[↑ Back to top](#table-of-contents)

---

## 05. Keyboard, shortcuts & input

macOS is a keyboard-first operating system wearing a mouse-first costume. Nearly everything has a shortcut, most text fields share the same Emacs-derived navigation keys, and modifier keys are remappable at the system level. Learn this chapter once and every app gets faster.

### The modifier keys and what they mean

| Key | Symbol | Role |
|---|---|---|
| Command | <kbd>⌘</kbd> | App-level actions: copy, paste, save, quit, switch apps. Equivalent to <kbd>Ctrl</kbd> on Windows/Linux for *shortcuts*. |
| Option (Alt) | <kbd>⌥</kbd> | Modifies: word-wise movement, special characters, alternate menu items (hold ⌥ while a menu is open to see them). |
| Control | <kbd>⌃</kbd> | Terminal/Emacs-style text editing (<kbd>⌃</kbd><kbd>A</kbd>, <kbd>⌃</kbd><kbd>E</kbd>, <kbd>⌃</kbd><kbd>K</kbd>), window/Space management, right-click (<kbd>⌃</kbd>-click). |
| Shift | <kbd>⇧</kbd> | Extend selection; reverse direction of many shortcuts. |
| Function / Globe | <kbd>fn</kbd> / <kbd>🌐</kbd> | Function-row behaviour; emoji picker; a fourth modifier in some apps. On Apple silicon it's also used by native window tiling (<kbd>fn</kbd><kbd>⌃</kbd><kbd>←</kbd>). |
| Caps Lock | | Wasted real estate — remap it (below). |

The key insight for switchers: **<kbd>⌘</kbd> is where your thumb is**, so <kbd>⌘</kbd><kbd>C</kbd>/<kbd>V</kbd>/<kbd>Z</kbd>/<kbd>S</kbd>/<kbd>W</kbd>/<kbd>Q</kbd>/<kbd>T</kbd> are one-hand chords, and <kbd>⌃</kbd> is free for the terminal — <kbd>⌃</kbd><kbd>C</kbd> interrupts a process while <kbd>⌘</kbd><kbd>C</kbd> copies, with no conflict. This is why the Mac terminal experience is nicer than Windows'.

### Remap Caps Lock (do this today)

`System Settings → Keyboard → Keyboard Shortcuts… → Modifier Keys`. Choose the keyboard in the dropdown (each keyboard is remapped separately) and set **Caps Lock → ⌃ Control**. Control is the most useful key with the worst factory position; on the home row it makes terminal editing, tmux prefixes, and IDE shortcuts effortless. Vim users often prefer **Caps Lock → ⎋ Escape**, or — with Karabiner — *Escape when tapped, Control when held* (the "dual-role" setup), which is what most heavy keyboard users end up with.

While you're there, on a **Windows-layout keyboard**, swap **⌥ Option ↔ ⌘ Command** so the key next to the space bar is Command like on a Mac keyboard. (Many mechanical keyboards have a hardware Mac/Win switch or DIP setting — use that instead if present.)

### Karabiner-Elements: the remapper

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

### Text editing shortcuts that work everywhere

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

### System shortcuts worth memorising

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

### Keyboard navigation of the UI

- `System Settings → Keyboard → Keyboard navigation`: **on**. Then <kbd>Tab</kbd> moves through *all* controls (buttons too), <kbd>Space</kbd> presses, <kbd>Return</kbd> is the default button, <kbd>⎋</kbd> cancels.
- <kbd>⌃</kbd><kbd>F2</kbd> (or <kbd>fn</kbd><kbd>⌃</kbd><kbd>F2</kbd>) focuses the **menu bar**; type to jump to a menu; arrows navigate. <kbd>⌃</kbd><kbd>F3</kbd> focuses the Dock. <kbd>⌃</kbd><kbd>F8</kbd> focuses menu bar extras (status items).
- <kbd>⌘</kbd><kbd>⇧</kbd><kbd>/</kbd> opens Help → Search: type any menu command; it highlights where it lives and pressing <kbd>Return</kbd> runs it. This is the fastest way to run an obscure command in any app.
- In dialogs, the first letter of a button often activates it when Full Keyboard Access is on.

### Custom app shortcuts

`System Settings → Keyboard → Keyboard Shortcuts… → App Shortcuts → +`. Pick an app (or *All Applications*), type the **exact menu item title** (including `…` typed as <kbd>⌥</kbd><kbd>;</kbd>), assign a key. Examples people set:

- *All Applications*: `Merge All Windows` → <kbd>⌘</kbd><kbd>⇧</kbd><kbd>M</kbd>; `Export as PDF…` → <kbd>⌘</kbd><kbd>⇧</kbd><kbd>E</kbd>; `Move Window to Left Side of Screen` → something ergonomic.
- *Safari*: `Show Web Inspector` if the default clashes; `Pin Tab`.
- *Finder*: `New Terminal at Folder` → <kbd>⌘</kbd><kbd>⌥</kbd><kbd>T</kbd>.
- *Mail*: `Archive` → <kbd>⌘</kbd><kbd>E</kbd>.

Menu items in the *Services* submenu are enabled here too (`Keyboard Shortcuts → Services`) — turn off the dozens you never use; they clutter every right-click menu.

### Function keys and the Touch Bar's legacy

- **Use F1, F2, etc. keys as standard function keys**: `Keyboard → Keyboard Shortcuts… → Function Keys`. Developers using IDE debuggers (<kbd>F5</kbd>–<kbd>F11</kbd>) usually turn this **on** and hit <kbd>fn</kbd> for brightness/volume. Alternatively keep media keys and let the IDE bindings use <kbd>fn</kbd>.
- Per-app exceptions: `Keyboard → Keyboard Shortcuts… → Function Keys` has none, but Karabiner can switch behaviour per app (e.g. standard F-keys only in Xcode/IntelliJ/VS Code).

### Input sources and typing in other languages

- `Keyboard → Text Input → Edit… → +` to add layouts/languages. **Show Input menu in menu bar**. Switch with <kbd>⌃</kbd><kbd>Space</kbd> (previous) / <kbd>⌃</kbd><kbd>⌥</kbd><kbd>Space</kbd> (next) — **and make sure this doesn't collide with <kbd>⌘</kbd><kbd>Space</kbd> for Spotlight** (check the *Input Sources* section of Keyboard Shortcuts).
- **Automatically switch to a document's input source**: on if you write in two scripts.
- **Unicode Hex Input** layout: hold <kbd>⌥</kbd> and type a code point (`2192` → →). Handy for maths symbols.
- **US International – PC** or **ABC – Extended** give dead keys for accents on a US keyboard; the standard **ABC** layout has them via <kbd>⌥</kbd> chords as shown above.
- **Dictation** (<kbd>🌐</kbd> twice by default, or set your own): on-device, offline, punctuation by voice ("comma", "new line"), works in any text field. Golden Gate's improved dictation (M3+, 12 GB+) is noticeably more accurate.

### Coming from Windows or Linux: the translation table

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

### Hardware keyboard notes

- **Keyboard layout wizard** appears the first time you plug in an unknown keyboard (ISO vs ANSI detection). If <kbd>§</kbd> and <kbd>`</kbd> are swapped on a European keyboard, rerun it: `Keyboard → Change Keyboard Type…` (or Karabiner's *Devices* tab has a per-device `§`/`` ` `` swap).
- **Mechanical keyboards with QMK/VIA**: set the Mac layout in firmware (swap GUI/Alt, map F-keys to media as you like). Then nothing in macOS needs remapping and the board works identically on your Linux box.
- **Bluetooth lag**: pair via USB-C once (Apple keyboards), keep the dongle in a USB-A port rather than a hub for Logitech Bolt receivers, and avoid 2.4 GHz Wi‑Fi congestion — Apple's N1 chip (M5 Pro/Max, M6) with Bluetooth 6 is markedly better here.
- **Two keyboards, two layouts**: `Keyboard → Text Input → Edit…` is global, but Karabiner can force a per-device input source.

[↑ Back to top](#table-of-contents)

---

## 06. Window management, Spaces & displays

macOS's window model confuses newcomers: there is no "maximise" in the Windows sense, apps can have many windows across many desktops, and full-screen is its own thing. Once you understand the three layers — **Spaces**, **tiling**, and **switching** — it's very fast. This chapter sets up the built-ins, then picks a third-party manager if you want more.

### Mental model

- A **Space** (virtual desktop) is a full-screen canvas. Each display has its own set of Spaces (`Displays have separate Spaces`: on). Full-screen apps become their own Space.
- **Windows** float in a Space. macOS remembers window positions per app and restores them on relaunch (Golden Gate also restores them across display connect/disconnect much better than before).
- **The green button** (or double-clicking the title bar) *zooms/fills* the window to the content's natural size or the full screen; **holding <kbd>⌥</kbd>** while clicking it fills the screen without entering full-screen mode; **hovering** it shows the tiling menu (Fill, Center, Left/Right/Top/Bottom halves, quarters, *Move to display*, *Enter Full Screen*).
- **Hiding** (<kbd>⌘</kbd><kbd>H</kbd>) an app removes its windows but keeps it in <kbd>⌘</kbd><kbd>Tab</kbd>; **minimising** (<kbd>⌘</kbd><kbd>M</kbd>) sends the window to the Dock and *out* of <kbd>⌘</kbd><kbd>Tab</kbd> — which is why most Mac users never minimise.

### Native window tiling (Sequoia+)

macOS finally does Windows-style snapping:

- **Drag a window to a screen edge** → it tiles to that half (top edge = fill; corners = quarters). A ghost outline previews the result. Hold <kbd>⌥</kbd> while dragging to get the outline immediately.
- **Keyboard**: <kbd>fn</kbd><kbd>⌃</kbd><kbd>←</kbd>/<kbd>→</kbd>/<kbd>↑</kbd>/<kbd>↓</kbd> = left half / right half / top half / bottom half; <kbd>fn</kbd><kbd>⌃</kbd><kbd>F</kbd> = fill; <kbd>fn</kbd><kbd>⌃</kbd><kbd>C</kbd> = centre; <kbd>fn</kbd><kbd>⌃</kbd><kbd>⇧</kbd> + arrows = quarters; <kbd>fn</kbd><kbd>⌃</kbd><kbd>R</kbd> = revert. On external keyboards without <kbd>fn</kbd>, use <kbd>🌐</kbd> or remap in `Keyboard Shortcuts → Windows`, where you can also **rebind these** to <kbd>⌃</kbd><kbd>⌥</kbd> + arrows (the Rectangle convention).
- **Menu**: `Window → Move & Resize` lists every arrangement, including *Left & Right*, *Top & Bottom*, *Quarters* which arrange **two or four windows at once**.
- Settings: `Desktop & Dock → Windows`: **Tiled windows have margins: off** (tight), *Drag windows to screen edges to tile*: on, *Drag windows to menu bar to fill screen*: on, *Hold ⌥ key while dragging windows to tile*: on.

For a lot of people — two windows side-by-side, one maximised, occasionally thirds — this is enough, and it needs no Accessibility permission. Its limits: no thirds/two-thirds by keyboard, no "move to next display" hotkey, no per-app rules, and the snapping zones are a bit coarse. That's where the third-party tools come in.

### Spaces and Mission Control

Set up once:

1. `System Settings → Desktop & Dock → Mission Control`: **Automatically rearrange Spaces based on most recent use: OFF**. This is the single most important setting — with it on, your Spaces shuffle constantly and <kbd>⌃</kbd><kbd>3</kbd> stops meaning anything.
2. `Keyboard → Keyboard Shortcuts… → Mission Control`: enable **Switch to Desktop 1…9** (<kbd>⌃</kbd><kbd>1</kbd>…<kbd>⌃</kbd><kbd>9</kbd>). They appear only after the Spaces exist — create them first.
3. Open Mission Control (<kbd>⌃</kbd><kbd>↑</kbd>, three/four-finger swipe up, or <kbd>F3</kbd>), hover top-right → **+** to add Spaces. Create 4–6 and give them roles — e.g. **1 Communication** (mail, Slack), **2 Browser/research**, **3 Code** (editor + terminal), **4 Second project / school**, **5 Media/notes**. Right-click a Space in Mission Control to rename? (Not possible — but Spaces auto-name from full-screen apps; wallpaper per Space is possible: set a wallpaper while on that Space.)
4. **Assign apps to Spaces**: right-click an app's Dock icon → *Options → Assign To → This Desktop*. Slack always opens on 1, your IDE on 3, etc. *All Desktops* is great for a music player or a floating notes window. `When switching to an application, switch to a Space with open windows for the application`: on — so <kbd>⌘</kbd><kbd>Tab</kbd> to Slack jumps to Space 1.
5. Move windows between Spaces by dragging them to the edge of the screen (hold briefly), dragging onto a Space thumbnail in Mission Control, or — fastest — **start dragging the window, then press <kbd>⌃</kbd><kbd>←</kbd>/<kbd>→</kbd>** with the other hand.

Trackpad: three- or four-finger horizontal swipe switches Spaces, up opens Mission Control, down shows the current app's windows (App Exposé). `Accessibility → Display → Reduce motion` makes the switch instant instead of sliding.

Full-screen (<kbd>⌃</kbd><kbd>⌘</kbd><kbd>F</kbd>) is a Space of its own that hides the menu bar and Dock. Great for a single-window focus session on a laptop screen; awkward on a big monitor. **Split View** (hover the green button → *Tile Window to Left of Screen*) puts two full-screen apps side by side with a draggable divider.

### Stage Manager

`Control Center → Stage Manager` (or Desktop & Dock). It groups windows into "stages" shown as thumbnails on the left; clicking one swaps the whole set in. It's a different metaphor from Spaces — like having your open windows as a deck of cards. Some people love it for a single laptop screen; most developers find Spaces + tiling more predictable and leave it off. If you try it, turn off *Show recent apps* to reclaim the left strip and use `Click wallpaper to reveal desktop: Only in Stage Manager`.

### Third-party window managers

Three tiers, from "just snapping" to "i3 on macOS". All need **Accessibility** permission (`Privacy & Security → Accessibility`); the tilers also want **Screen Recording** to read window titles in some cases.

#### Tier 1 — snapping and hotkeys (most people)

| Tool | Price | Why pick it |
|---|---|---|
| **Rectangle** | Free, OSS | The classic. <kbd>⌃</kbd><kbd>⌥</kbd> + arrows/U/I/J/K/Enter/C for halves, quarters, thirds, maximise, centre, *next display* (<kbd>⌃</kbd><kbd>⌥</kbd><kbd>⌘</kbd><kbd>→</kbd>). Snap areas configurable. **Rectangle Pro** ($10) adds layouts, pinning, app-specific rules, stage-like "throw". |
| **Raycast window management** | Free (part of Raycast) | Same actions as Rectangle, assigned via Raycast hotkeys, plus *Reasonable Size*, *Almost Maximize*, custom sizes. If you already run Raycast, don't install a second tool. |
| **Loop** | Free, OSS | Hold a trigger key and move the mouse for a radial menu of positions. Pretty, fast, very configurable; the choice for people who don't want to memorise 15 chords. |
| **Swish** | $16 | Trackpad-gesture window management (swipe on a title bar to tile). Great with Magic Trackpad. |
| **BetterSnapTool / Magnet / Moom** | $3–$10 | Fine; older, still maintained. Moom's custom grid palette remains unique. |

**Recommendation**: Rectangle if you don't use Raycast; Raycast's built-in commands if you do. Bind: left/right halves, left/right two-thirds, maximise, centre, next display, and "reasonable size". That covers 95% of real use.

#### Tier 2 — automatic tiling without disabling security

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

#### Tier 3 — yabai (maximum control, some SIP cost)

**yabai** (free, OSS) + **skhd** (hotkey daemon) is the deepest tiler: BSP layouts, real Spaces integration, window opacity, borders, scripting via a Unix socket. Its full power (creating/destroying/moving Spaces, focusing across displays with animation off, window shadows/opacity) requires **partially disabling System Integrity Protection** and loading a scripting addition into Dock.app:

1. Boot to Recovery (hold power → Options → Terminal): `csrutil enable --without fs --without debug --without nvram` (Apple silicon).
2. Reboot, then `sudo nvram boot-args=-arm64e_preview_abi`, reboot again.
3. Add the sudoers line yabai's wiki gives so it can load the scripting addition without a password.

**This weakens your machine's security posture** (kernel/debug protections) and Apple sometimes breaks the addition on major macOS releases — check yabai's issue tracker before installing Golden Gate. Many yabai users run it *without* the scripting addition (SIP untouched) and accept losing Space manipulation; that is a reasonable middle path. On a work-managed Mac, don't touch SIP; use AeroSpace.

#### Choosing

| You… | Use |
|---|---|
| Just want snap-to-half and maximise | Native tiling + Rectangle or Raycast |
| Use a big monitor and want thirds/two-thirds and quick centring | Rectangle / Raycast / Loop |
| Come from i3/sway/Hyprland and miss auto-tiling | **AeroSpace** |
| Want auto-tiling but keep real macOS Spaces and swipes | Amethyst, or yabai without SIP changes |
| Want everything scriptable and don't mind SIP tweaks | yabai + skhd (+ sketchybar) |
| Prefer gestures | Swish, or Loop |

### Multiple displays

- **Arrangement**: `Displays → Arrange…` (or drag the thumbnails). Put the display with the white bar as your **main display** — the Dock and new windows land there. With a laptop in clamshell, the external becomes main automatically.
- **Displays have separate Spaces** (Mission Control): **on**. Each display gets its own Spaces and menu bar. Off gives one giant Space spanning displays (useful for a single ultra-wide + laptop stretched layout, rarely otherwise).
- **Move a window to another display**: drag; or hover the green button → *Move to <display>*; or Rectangle's <kbd>⌃</kbd><kbd>⌥</kbd><kbd>⌘</kbd><kbd>←</kbd>/<kbd>→</kbd>; or AeroSpace's `move-node-to-monitor`.
- **Scaling**: for a 4K 27" pick the "looks like 2560×1440" (2×-ish) or 3008×1692 option; text stays sharp because macOS renders at 2× and downsamples. 5K 27" = perfect 2× at 2560×1440. A 1440p 27" monitor runs at 1× and text looks thin — that's the display, not a setting.
- **Refresh rate**: choose the max in `Displays`. Golden Gate exposes more high-res and high-refresh modes over Thunderbolt/HDMI and remembers window positions per display configuration much more reliably.
- **Clamshell**: closed lid + external display + power + external keyboard/mouse works out of the box. Keep the lid *open* an inch if the laptop gets hot under sustained load (the keyboard deck dissipates heat).
- **DisplayLink / USB-only docks**: avoid if you can. Thunderbolt/USB4 docks drive displays natively via DisplayPort Alt Mode; DisplayLink needs a driver (screen-recording permission, occasional flicker, no HDCP). If a cheap dock's second monitor doesn't appear, it's DisplayLink.
- **Two displays on base M-chips** (M5 Air/Pro): supported natively since M3 (Air needs the lid closed for two externals on M3; M4/M5 Air drives two with lid open). The Neo drives one.
- **Sidecar** turns an iPad into a display (wired or wireless, touch supported better in GG). **Universal Control** shares one keyboard/mouse across a Mac and iPad sitting next to each other — enable in `Displays → Advanced`.
- **iPhone Mirroring** (Sequoia+) puts your iPhone on the Mac desktop, resizable in GG; iPhone notifications arrive on the Mac. Useful for testing your own iOS app while coding.

### Focus-follows-mouse and other Linux habits

macOS has no system-wide focus-follows-mouse; AeroSpace/yabai offer it for their windows, and Ghostty/iTerm2 have it for their splits. Sloppy-focus fans generally adjust. Middle-click-to-paste doesn't exist outside X11 terminals (XQuartz). Workspaces-per-monitor behaviour is what `Displays have separate Spaces` gives you. Keyboard-driven everything: see the shortcuts in Chapter 5.

### Recommended setups

**Student on a 13"/15" laptop, no monitor**: native tiling for halves; 4 Spaces with roles; <kbd>⌃</kbd><kbd>1–4</kbd> bound; full-screen for the editor during deep work; Raycast or Rectangle for "maximise" and "centre". Reduce motion on.

**Engineer with a 27" 5K + laptop**: main display = the 27"; separate Spaces on; editor two-thirds left / terminal one-third right (Rectangle <kbd>⌃</kbd><kbd>⌥</kbd><kbd>E</kbd>/<kbd>T</kbd>) on Space 1 of the big screen; browser on Space 2; comms on the laptop screen. Assign Slack/Mail to the laptop display's Space.

**Tiling enthusiast**: AeroSpace + JankyBorders, 6 workspaces, apps assigned by `on-window-detected` rules, System Settings/Finder/dialog-heavy apps floated, Ghostty as the terminal with its own splits, `alt-tab` back-and-forth. Native Spaces unused; Mission Control gestures disabled to avoid confusion.

[↑ Back to top](#table-of-contents)

---

## 07. Command Line Tools, Xcode & the toolchain

Every compiler, `git`, `make`, and the system SDK on macOS come from Apple's developer tools. You have two ways to get them, and the right choice depends on whether you will ever build an iOS/macOS app.

### Command Line Tools (CLT) — what almost everyone needs

```sh
xcode-select --install
```

A dialog appears; click *Install*. This downloads ~2 GB into `/Library/Developer/CommandLineTools` and gives you:

- `clang`/`clang++` (Apple's LLVM), `swift`, `swiftc`, `ld`, `lldb`
- `git` (Apple's build, usually a few months behind upstream — Homebrew's `git` will shadow it later)
- `make`, `python3` (a shim that points to the CLT's Python — do **not** use it for projects; Chapter 11), `perl`, `ruby` (system versions, also not for projects)
- headers and the macOS SDK under `…/CommandLineTools/SDKs/MacOSX.sdk`
- `otool`, `nm`, `codesign`, `xcrun`, `dsymutil`, `strip`, `install_name_tool`, `lipo`, `file`

Homebrew requires the CLT and will offer to install them if missing. Verify:

```sh
xcode-select -p          # → /Library/Developer/CommandLineTools
clang --version          # Apple clang version 17.x (Xcode 27 era)
git --version
```

**Updating**: CLT updates arrive via `System Settings → Software Update` (they're listed as "Command Line Tools for Xcode"). If Homebrew complains that the CLT are outdated or "not installed" after a macOS upgrade, the fix is always:

```sh
sudo rm -rf /Library/Developer/CommandLineTools
xcode-select --install
```

### Full Xcode — when you need it

Install Xcode if you will:

- build apps for iOS, iPadOS, macOS, watchOS, tvOS or visionOS (Swift/SwiftUI/UIKit);
- use the **iOS Simulator** (also needed by React Native, Flutter, Expo, Tauri-mobile, Capacitor);
- need **Instruments** (profiling), **Reality Composer**, **Create ML**, or Interface Builder;
- take a mobile-development or graphics/Metal course;
- run certain Homebrew formulae that need the full SDK or `xcodebuild` (rare; Homebrew tells you).

Otherwise skip it: Xcode 27 is ~4 GB to download and **~15 GB installed**, plus 8–10 GB per simulator runtime, and it makes every macOS update also an Xcode update.

**Install**: from the **Mac App Store** (simplest; auto-updates) or download the `.xip` from developer.apple.com/download (faster on slow connections; lets you keep multiple versions). Power users install via **`xcodes`** (`brew install xcodesorg/made/xcodes`) or the **Xcodes.app** GUI, which downloads, unxips and switches versions with `xcodes install 27.0` / `xcodes select 27.0`.

After installing, run it once to accept the licence and install components, or from the shell:

```sh
sudo xcodebuild -license accept
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer   # make the CLT inside Xcode the active toolchain
xcodebuild -runFirstLaunch
```

**Which toolchain is active?** `xcode-select -p` prints either the standalone CLT path or `…/Xcode.app/Contents/Developer`. With Xcode installed, point it at Xcode (as above) so `xcrun`, `swift`, and Homebrew all agree. You still keep the standalone CLT installed — that's normal.

#### Xcode 27 in one paragraph

Xcode 27 (WWDC 2026, ships with macOS 27) is **Apple-silicon-only**, noticeably faster, and adds **coding agents** (agentic workflows that can plan, edit across files, generate SwiftUI views and localisations, with Apple's models or your own provider such as Claude/ChatGPT), a **Device Hub** for managing test devices, untitled projects and standalone Swift files with live previews, improved Instruments/Time Profiler, and Swift 6.3. Simulators for iOS 27 ship with it. If your course or job uses an older Xcode, keep both via `xcodes`.

#### Simulators and disk space

Runtimes are the disk hog. Manage them from `Xcode → Settings → Components` or the CLI:

```sh
xcrun simctl runtime list                      # installed runtimes (each 8–10 GB)
xcrun simctl runtime delete <runtime-id>       # remove one
xcrun simctl list devices                      # simulator devices
xcrun simctl delete unavailable                # remove devices whose runtime is gone
xcrun simctl erase all                         # reset all simulators (frees data, keeps runtimes)
```

Other Xcode caches you can nuke safely (Xcode rebuilds them):

```sh
rm -rf ~/Library/Developer/Xcode/DerivedData/*          # build products, often 10–50 GB
rm -rf ~/Library/Developer/Xcode/Archives/*             # old archives (keep if you need to re-symbolicate crashes)
rm -rf ~/Library/Developer/Xcode/iOS\ DeviceSupport/*   # symbols for devices you no longer own
rm -rf ~/Library/Developer/CoreSimulator/Caches/*
rm -rf ~/Library/Caches/com.apple.dt.Xcode/*
```

`System Settings → General → Storage → Developer` exposes most of these with a delete button. **Xcode shouldn't be in your Time Machine backup** — exclude `~/Library/Developer` (Chapter 17); it's all regenerable.

#### Command-line builds without opening Xcode

- `xcodebuild -list -project Foo.xcodeproj`, `xcodebuild -scheme Foo -destination 'platform=iOS Simulator,name=iPhone 17' build test`.
- `swift build`, `swift test`, `swift run` for Swift packages (no Xcode project needed — the standalone CLT suffice).
- `xcrun simctl boot "iPhone 17" && open -a Simulator` to launch a simulator from a script.
- **Fastlane** (`brew install fastlane`) for signing/TestFlight automation; **xcbeautify** for readable build logs; **SwiftLint**/**SwiftFormat**; **Tuist** or **XcodeGen** to generate projects from a manifest so `.xcodeproj` merge conflicts stop happening.

### Rosetta 2 and the arm64-only future

**Rosetta 2** translates Intel (x86_64) binaries so they run on Apple silicon. It isn't installed by default; the first time you launch an Intel app, macOS offers to install it, or you can do it yourself:

```sh
softwareupdate --install-rosetta --agree-to-license
```

The timeline you need to plan around:

| When | What happens |
|---|---|
| macOS 26.4 (Mar 2026) | Every launch of an Intel-only app shows a deprecation warning. |
| **macOS 27 (Sept 14, 2026)** | The installer **removes Rosetta** if present. You can reinstall it with the command above; it works fully through the 27.x cycle. Homebrew's Intel bottles stop being built this month. |
| **macOS 28 (fall 2027)** | Rosetta is **removed for general apps**; it survives only as a compatibility shim for a short list of old, unmaintained games that depend on Intel-only frameworks. Intel binaries — including anything under `/usr/local` from an x86 Homebrew — will not run. |

What this means for your setup:

1. **Everything you install should be arm64.** Homebrew under `/opt/homebrew` is. Download the "Apple silicon" or "Universal" build of every app; avoid "Intel" builds even when offered. Check any binary with `file /path/to/bin` (look for `arm64`) or in Activity Monitor → add the *Kind* column (Apple vs Intel).
2. **Audit now**: `find /Applications -name "*.app" -maxdepth 2 -exec sh -c 'lipo -archs "{}/Contents/MacOS/$(defaults read "{}/Contents/Info.plist" CFBundleExecutable 2>/dev/null)" 2>/dev/null | grep -q arm64 || echo "{}"' \;` lists apps without an arm64 slice. Or simply sort Activity Monitor by Kind while your usual apps are open.
3. **Delete an Intel Homebrew** if migration brought one over: `arch -x86_64 /usr/local/bin/brew bundle dump --file=~/intel-brewfile` to record what was there, then run Homebrew's official uninstall script with `arch -x86_64` and remove `/usr/local/Homebrew`. Reinstall what you need natively.
4. **Docker images**: `linux/amd64` containers run under QEMU or Rosetta *inside the Linux VM* (Docker Desktop/OrbStack use Rosetta for Linux, which is a *different* mechanism that stays supported for virtualisation). Prefer `linux/arm64` images anyway — they're faster and most official images are multi-arch (Chapter 13).
5. **Node/Python native modules**: rebuild (`npm rebuild`, `pip install --force-reinstall`) after moving from an Intel machine; `node_modules` with x86 `.node` files is the classic "works on my old Mac" bug.
6. **If you truly need x86 macOS software** (an old EDA tool, a legacy game), keep a macOS 27 partition/VM or an old Intel machine around; Golden Gate is the last stop.

Check whether you're currently under Rosetta in a terminal: `uname -m` (should print `arm64`; `x86_64` means the terminal itself is running translated — a common state after copying an Intel terminal's settings). `sysctl -n sysctl.proc_translated` prints `1` if the current process is translated.

### System languages you should *not* use for projects

macOS ships `python3` (via CLT), `perl`, `ruby`, `php` (removed in Monterey), `java` (a stub that prompts to install a JDK), `git`, `zsh`, `bash` 3.2 (2007, GPLv2-frozen), `curl`, `openssl` (actually LibreSSL), `sqlite3`, `tclsh`, `vim`, `nano`, `rsync` (Apple switched to openrsync in Sequoia). These are for the OS and for Apple's scripts. Never `pip install` into the system Python, never `gem install` into system Ruby, don't write scripts that assume bash 4+ features unless you shebang Homebrew's bash. Chapter 11 sets up proper, versioned runtimes.

### Useful Apple CLI tools you already have

| Tool | Use |
|---|---|
| `open` | `open .` (Finder here), `open -a "Visual Studio Code" file`, `open https://…`, `open -R file` (reveal), `open -e file` (TextEdit) |
| `pbcopy` / `pbpaste` | Pipe to/from the clipboard: `cat key.pub \| pbcopy`, `pbpaste > notes.txt` |
| `say` | Text-to-speech: `make && say done` |
| `defaults` | Read/write preferences (Chapter 3) |
| `mdfind` / `mdls` | Spotlight search from the shell |
| `screencapture` | `screencapture -i ~/Desktop/shot.png` (interactive), `-c` to clipboard |
| `sips` | Image resize/convert: `sips -Z 1024 *.png`, `sips -s format jpeg in.png --out out.jpg` |
| `textutil` | Convert docx/rtf/html/txt: `textutil -convert txt notes.docx` |
| `qlmanage -p file` | Quick Look from the shell |
| `caffeinate -d` / `caffeinate -i cmd` | Keep awake / while a command runs |
| `pmset -g` / `pmset -g log` | Power settings and sleep/wake history |
| `networksetup`, `airport` (gone in Sonoma — use `wdutil info`), `scutil --dns` | Network config from the shell |
| `diskutil list`, `diskutil apfs list` | Disks and APFS containers |
| `tmutil` | Time Machine (`tmutil listbackups`, `tmutil addexclusion`) |
| `system_profiler SPHardwareDataType` | Hardware info (or `sysctl -a \| grep machdep.cpu`) |
| `log show --predicate 'process == "kernel"' --last 1h` | Unified logging (Console.app's engine) |
| `launchctl` | Manage launch agents/daemons (Chapter 21) |
| `security` | Keychain from the shell: `security find-generic-password -s "svc" -w` |
| `codesign -dv --verbose=4 App.app`, `spctl -a -vv App.app` | Inspect signatures / Gatekeeper verdict |
| `xattr -l file`, `xattr -d com.apple.quarantine file` | Extended attributes; remove quarantine |
| `plutil -p file.plist` | Pretty-print property lists (`-convert xml1` to edit) |
| `osascript -e 'display notification "done"'` | AppleScript/JXA from the shell |
| `shortcuts run "Name"` | Run a Shortcut from the shell |
| `container` (Tahoe+) | Apple's Linux container CLI (Chapter 13) |

### GNU tools vs BSD tools

macOS userland is **BSD**: `sed`, `awk`, `grep`, `find`, `ls`, `date`, `stat`, `tar`, `xargs` have BSD flags, not GNU ones. `sed -i` needs an argument (`sed -i '' 's/a/b/' f`), `date -d` doesn't exist (`date -v+1d`), `ls --color` fails (`ls -G`), `readlink -f` only appeared in macOS 12.3. Scripts copied from Linux tutorials break here.

Two fixes, pick one:

- **Install GNU versions via Homebrew** (`brew install coreutils findutils gnu-sed gawk grep gnu-tar`) — they install with a `g` prefix (`gsed`, `gls`, `gdate`). To use them *unprefixed*, add the `gnubin` dirs to `PATH` in your shell config (`$(brew --prefix coreutils)/libexec/gnubin` etc.). Be aware this changes behaviour for every script on the machine, including some Homebrew formulae; many people prefer prefixed use only.
- **Write portable scripts**: use `#!/usr/bin/env bash`, avoid GNU-only flags, or use the modern Rust replacements from Chapter 9 (`fd`, `rg`, `sd`, `eza`, `bat`) that behave identically on macOS and Linux.

Homebrew's `bash` (5.x) and `zsh` are current; Apple's `/bin/bash` is stuck at 3.2 for licensing reasons and Apple's `zsh` is fine as a login shell but lags a version or two.

[↑ Back to top](#table-of-contents)

---

## 08. Homebrew

Homebrew is the package manager for macOS. Nearly every command-line tool in this guide and most GUI apps install through it, and a `Brewfile` is how you make a new Mac look like your old one in twenty minutes. This chapter covers Homebrew **6.x** (6.0.0 shipped June 2026), which changed several defaults from what older tutorials show.

### Install

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

The installer asks for your password once (`sudo` to create `/opt/homebrew` and set ownership to your user), installs the Command Line Tools if missing, and finishes with two lines to add to your shell config. On Apple silicon the prefix is **`/opt/homebrew`**; the installer's suggested snippet is:

```sh
echo >> ~/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

`brew shellenv` sets `HOMEBREW_PREFIX`, `PATH`, `MANPATH`, `INFOPATH`. Put it in `~/.zprofile` (login shells) or `~/.zshrc` — Chapter 9 organises this properly. Then:

```sh
brew doctor      # "Your system is ready to brew." — fix anything it flags
brew --prefix    # /opt/homebrew
brew config      # look for "Rosetta 2: false" and "macOS: 27.x-arm64"
```

> [!WARNING]
> If `brew --prefix` prints `/usr/local`, you have an **Intel** Homebrew running under Rosetta (usually inherited via Migration Assistant or by running the installer from an x86 terminal). It will stop receiving binary packages this month and stop working in macOS 28. Record it (`brew bundle dump --file=~/old-brewfile`), uninstall it with the official script under `arch -x86_64`, delete `/usr/local/Homebrew` and `/usr/local/Cellar`, and reinstall natively.

Standard-account users (Chapter 3): run the installer while authenticating as the admin user, then `sudo chown -R $(whoami):admin /opt/homebrew` so your daily account owns it. Homebrew refuses to run as root; multi-user Homebrew is unsupported — one user owns it.

### Concepts

| Term | Meaning |
|---|---|
| **Formula** | A command-line package built from source or, almost always, installed from a prebuilt **bottle**. `brew install ripgrep`. Lives in `/opt/homebrew/Cellar/<name>/<version>` and is symlinked into `/opt/homebrew/bin`, `lib`, etc. |
| **Cask** | A GUI app or large binary (fonts, drivers) installed from the vendor's own download. `brew install --cask ghostty`. The `.app` goes to `/Applications`; metadata to `/opt/homebrew/Caskroom`. |
| **Tap** | A third-party repository of formulae/casks (`brew tap owner/repo`). `homebrew/core` and `homebrew/cask` are built in and served from a JSON API rather than a git clone. |
| **Keg-only** | A formula not symlinked into `bin` because it would shadow a system tool (e.g. `openssl@3`, `libpq`, `curl`). Use `$(brew --prefix libpq)/bin/psql` or add to `PATH` explicitly. |
| **Bottle** | Prebuilt binary for your macOS version/arch. If none exists, `brew` compiles — slow and a sign the formula is unusual or you're on an unsupported macOS. |
| **Brewfile** | A manifest of taps, formulae, casks, Mac App Store apps and extension packages, consumed by `brew bundle`. |
| **Service** | A formula with a launchd definition (Postgres, Redis, nginx): `brew services start postgresql@17`. |

### Everyday commands

```sh
brew search <text>            # formulae and casks; use "brew search --desc" to search descriptions
brew info <pkg>               # what it is, deps, caveats (read caveats!), install status; "brew info --cask"
brew install <pkg>            # formula
brew install --cask <app>     # GUI app
brew exec <formula> -- <cmd>  # run a tool from a formula's environment without installing globally (6.0, like npx)
brew list                     # installed formulae (+ --cask for apps); "brew leaves" = explicitly installed, not deps
brew deps --tree <pkg>        # why is this here?
brew uses --installed <pkg>   # what depends on it
brew update                   # refresh the package index (fast; internal JSON API)
brew outdated                 # what would upgrade
brew upgrade                  # upgrade everything (formulae + casks); "brew upgrade <pkg>" for one
brew pin <pkg> / brew unpin   # freeze a version (formulae and, since 6.0, casks)
brew uninstall <pkg>          # remove; "--zap" for casks deletes prefs/caches too
brew autoremove               # remove orphaned dependencies
brew cleanup [--prune=all]    # delete old versions and downloads (auto-runs periodically; run manually to reclaim GB)
brew doctor                   # health check
brew tap-info --installed     # your taps and their trust status
brew vulns                    # (tap) check installed packages against known CVEs
```

Homebrew 6 turned on **"ask" mode by default for developers** (and it's a one-line opt-in for everyone): `brew install`/`upgrade` print a plan — packages, dependencies, download size — and wait for `y`. Set `HOMEBREW_ASK=1` in your shell config to have it everywhere, or `--yes`/`-y` to skip a prompt in scripts. `brew upgrade` now prints a summary at the end, and cask upgrades can reopen apps that were running.

Casks with `auto_updates true` (apps that update themselves, like Chrome, VS Code, Slack) are skipped by `brew upgrade` unless you pass `--greedy`, so `brew upgrade --greedy` occasionally forces them to the version Homebrew knows.

### Tap trust (new in 6.0)

Third-party taps contain arbitrary Ruby that runs on your machine. Homebrew 6 requires you to **trust a tap explicitly** before its formulae or casks are evaluated:

```sh
brew tap --trust owner/repo          # add and trust in one step
brew tap owner/repo                  # add untrusted → install of its packages is refused until trusted
brew trust owner/repo                # trust later
brew untrust owner/repo
brew tap-info owner/repo             # shows "trusted: true/false"
```

Official taps are trusted by default. Homebrew also stopped auto-tapping (`brew install owner/repo/tool` no longer silently adds the tap). In a Brewfile, write `tap "owner/repo", trusted: true`. Before trusting a tap, look at its GitHub repo — how many stars, who maintains it, does it just wrap binaries from a vendor's releases page. Popular taps you'll likely trust: `hashicorp/tap`, `oven-sh/bun`, `xcodesorg/made`, `FelixKratz/formulae` (sketchybar/borders), `koekeishiya/formulae` (yabai/skhd), `nikitabobko/tap` (AeroSpace), `charmbracelet/tap`, `stripe/stripe-cli`, `supabase/tap`.

### The Brewfile: your machine as code

Create one from your current state:

```sh
brew bundle dump --describe --file=~/.config/homebrew/Brewfile   # --force to overwrite
```

Edit it by hand from then on. A realistic developer Brewfile (yours will differ — this is the shape):

```ruby
# ~/.config/homebrew/Brewfile
tap "oven-sh/bun", trusted: true
tap "nikitabobko/tap", trusted: true

# --- shell & core CLI ---
brew "git"                 # newer than Apple's
brew "gh"                  # GitHub CLI
brew "zsh"                 # optional: newer than /bin/zsh
brew "starship"            # prompt
brew "zoxide"              # smarter cd
brew "fzf"                 # fuzzy finder
brew "ripgrep"             # rg
brew "fd"                  # find
brew "bat"                 # cat with wings
brew "eza"                 # ls
brew "jq", "yq"            # JSON / YAML
brew "tmux"
brew "neovim"
brew "mise"                # runtime versions (node, python, go, java…)
brew "uv"                  # python packaging
brew "direnv"
brew "tldr"                # or tlrc
brew "htop", "btop"
brew "wget", "curl"        # curl is keg-only; Apple's is fine for most uses
brew "coreutils", "gnu-sed", "gawk"   # GNU tools (g-prefixed)
brew "tree", "ncdu", "dust", "duf"
brew "watch", "entr"
brew "hyperfine"           # benchmarking
brew "difftastic", "git-delta"
brew "shellcheck", "shfmt"
brew "pre-commit"
brew "gnupg", "pinentry-mac"
brew "mas"                 # Mac App Store CLI
brew "trash"               # move to Trash from the shell instead of rm
brew "colima", "docker", "docker-compose", "docker-buildx"   # or the OrbStack cask instead of these four
brew "postgresql@17", restart_service: :changed
brew "redis", restart_service: :changed
brew "sqlite"
brew "awscli"
brew "terraform"           # or tofu
brew "kubectl", "k9s", "helm"
brew "oven-sh/bun/bun"

# --- GUI apps ---
cask "ghostty"
cask "visual-studio-code"
cask "zed"
cask "raycast"
cask "rectangle"           # or: cask "nikitabobko/tap/aerospace"
cask "karabiner-elements"
cask "maccy"
cask "1password", "1password-cli"
cask "orbstack"
cask "tableplus"
cask "postman"             # or "bruno"
cask "obsidian"
cask "notion"
cask "slack", "discord", "zoom"
cask "google-chrome", "firefox", "zen"
cask "iina"                # video player
cask "the-unarchiver"
cask "appcleaner"
cask "stats"               # menu bar system monitor
cask "ice"                 # menu bar organiser
cask "font-jetbrains-mono-nerd-font"
cask "font-fira-code-nerd-font"
cask "qlmarkdown", "syntax-highlight", "quicklook-json", "qlstephen"

# --- Mac App Store (needs mas + signed in) ---
mas "Xcode", id: 497799835
mas "Amphetamine", id: 937984704
mas "Kagi for Safari", id: 1622835804

# --- VS Code extensions ---
vscode "ms-python.python"
vscode "esbenp.prettier-vscode"
vscode "eamodio.gitlens"
```

Apply it on a new machine (or after editing):

```sh
brew bundle install --file=~/.config/homebrew/Brewfile   # installs anything missing; parallel since 6.0
brew bundle check                                        # what's missing
brew bundle cleanup                                      # uninstall things NOT in the Brewfile (asks first)
brew bundle add ripgrep --describe                       # append to the Brewfile
brew bundle remove ripgrep
```

Set `HOMEBREW_BUNDLE_FILE=~/.config/homebrew/Brewfile` in your shell config so you can drop `--file`. Homebrew 6 also lets a Brewfile carry `npm`, `cargo`, `go`, `uv` (Python tools), `krew` and even `winget` (on Windows) entries, so global CLI tools from language ecosystems live in the same manifest:

```ruby
uv "ruff"
uv "pre-commit"
npm "typescript"
cargo "cargo-watch"
```

Commit the Brewfile to your dotfiles repo (Chapter 10). Appendix B is a complete annotated Brewfile you can start from.

### Services

Formulae with background daemons integrate with launchd:

```sh
brew services list
brew services start postgresql@17      # start now + at login
brew services run redis                # start now only
brew services stop postgresql@17
brew services restart --all
brew services info postgresql@17       # status, log paths, user
```

Logs go to `/opt/homebrew/var/log/`; data to `/opt/homebrew/var/<service>/`. For databases that should only run when you're actually developing, prefer starting them per project (Chapter 15) or in containers — a Postgres that autostarts at login is a battery cost you'll forget about.

### Fonts, drivers, and other casks

- **Fonts** are casks: `brew install --cask font-jetbrains-mono-nerd-font` (the *Nerd Font* variants include the icons that Starship, eza and Neovim status lines expect). Since Homebrew 4.x the fonts live in the main cask repo — no `homebrew/cask-fonts` tap needed.
- **Drivers/kernel extensions** (Logitech, Wacom, Elgato, VirtualBox) are casks too; on Apple silicon many need approval in `Privacy & Security` after install, and a kext requires *Reduced Security* in Recovery — avoid apps that still ship kexts in 2026.
- **Quarantine**: casks are downloaded with Gatekeeper's quarantine bit set, so the first launch shows the "downloaded from the internet" check. `brew install --cask --no-quarantine <app>` skips that for apps you trust (or `export HOMEBREW_CASK_OPTS="--no-quarantine"` for all). Casks whose signatures fail Gatekeeper are disabled in Homebrew as of September 2026, so anything installable is at least signed.
- `brew install --cask --appdir=~/Applications <app>` installs for your user only.
- **`brew uninstall --zap --cask <app>`** removes preferences, caches, and launch agents listed in the cask definition — the closest thing to a clean uninstall. AppCleaner does the same for non-Homebrew apps.

### Environment variables worth setting

```sh
# ~/.zshenv or ~/.zshrc
export HOMEBREW_NO_ENV_HINTS=1          # quieter
export HOMEBREW_BUNDLE_FILE="$HOME/.config/homebrew/Brewfile"
export HOMEBREW_CASK_OPTS="--no-quarantine"   # optional; see above
export HOMEBREW_NO_ANALYTICS=1          # opt out of anonymous analytics (or `brew analytics off`)
export HOMEBREW_ASK=1                   # always show the plan and confirm
# export HOMEBREW_AUTO_UPDATE_SECS=86400  # update the index at most daily instead of every 5 min
# export HOMEBREW_NO_AUTO_UPDATE=1        # never auto-update on install (then run `brew update` yourself)
```

Defaults that changed in 5.x/6.x and no longer need setting: concurrent downloads (on), the internal JSON API (on), `brew bundle` parallel installs (on), SBOM generation (now **opt-in** via `HOMEBREW_SBOM=1`).

### Maintenance routine

Weekly (or bind it to a Raycast/Shortcuts command):

```sh
brew update && brew upgrade && brew autoremove && brew cleanup --prune=all && brew doctor
```

Occasionally:

- `brew leaves` — anything you don't recognise, `brew uninstall` it.
- `brew bundle cleanup` — prunes to the Brewfile.
- `du -sh $(brew --cache)` — the download cache; `brew cleanup --prune=all` clears it.
- After a **major macOS upgrade**: `brew update`, `brew upgrade`, then `brew doctor`. If many bottles are missing for a brand-new macOS version (the first week or two of Golden Gate), Homebrew builds from source; be patient or wait a week. Reinstall the CLT if `brew doctor` says they're outdated.
- **Every September**: read the Homebrew blog post for the new major version. 6.0's changes (tap trust, ask mode) broke a few people's scripts.

### Homebrew and the Intel deprecation

Per Homebrew's support tiers: with macOS 27 dropping Intel Macs, **macOS x86_64 moved to Tier 3 in September 2026** — no CI, no new bottles, install-from-source only, `brew doctor` warns — and **in September 2027 all Intel macOS code is deleted**. If you still have an Intel Mac on Tahoe, expect increasingly frequent from-source builds; if you have an Intel Homebrew on an Apple silicon Mac, remove it now (above).

### Alternatives and complements

- **MacPorts** — older, uses `/opt/local`, builds more from source, runs as root. Excellent for scientific/legacy Unix software; fine to run *alongside* Homebrew if you keep PATHs straight. Most people don't need it.
- **Nix / nix-darwin / Home Manager** — declarative, reproducible, cross-platform. Powerful and a real rabbit hole; if you already use Nix on Linux, `nix-darwin` can manage Homebrew casks *and* system settings. Homebrew 6 warns when it detects a Nix-managed installation but works.
- **`mise`** (Chapter 11) for language runtimes and dev tools with per-project versions; **`uv tool`**, **`pipx`**, **`npm -g`**, **`cargo install`** for language-specific CLIs — increasingly all recorded in the Brewfile via the 6.0 extensions.
- **Mac App Store + `mas`** for sandboxed apps that update themselves and are tied to your Apple Account.
- **Setapp** ($10/month subscription to ~250 Mac apps) — worth it if you'd otherwise buy 3+ of its apps (CleanShot X, Bartender, TablePlus, Paste, iStat Menus…). Free 7-day trial; students get 50% off.
- **Workbrew** — Homebrew for managed fleets (the Homebrew lead's company). Relevant if your employer manages Macs.
- **BrewUI** — Homebrew's own upcoming official GUI; not ready for general use yet. **Cakebrew** is dead; **Applite** is a decent third-party cask GUI for beginners.

[↑ Back to top](#table-of-contents)

---

## 09. Terminal & shell

You'll spend more hours in the terminal than in any other window. The 2026 recipe: a **GPU-accelerated terminal** (Ghostty), **zsh** with a small hand-written config instead of a heavyweight framework, **Starship** for the prompt, **fzf** and **zoxide** for navigation, and a set of modern Rust replacements for the classic Unix tools. Everything here is in the Brewfile from Chapter 8.

### Choosing a terminal emulator

Terminal.app got 24-bit colour, Powerline glyph support and a new default theme in Tahoe; it's genuinely fine now. Most developers still switch for splits, better keybindings, and speed.

| Terminal | Best for | Config | Notes |
|---|---|---|---|
| **Ghostty** (free, OSS, Zig) | **Default recommendation.** Native macOS UI (real tabs, windows, Liquid Glass), fastest renderer, sensible defaults | `~/.config/ghostty/config` — plain `key = value` | 1.3 (Mar 2026) added scrollback search (<kbd>⌘</kbd><kbd>F</kbd>), native scrollbars, click-to-move-cursor, command-finished notifications, key tables, drag-to-reorder splits, "Set as default terminal". 6-month release cadence. |
| **iTerm2** (free, OSS) | Deepest feature set: shell integration, triggers, tmux `-CC` native integration, per-profile everything, password manager | GUI prefs (exportable JSON) | 15 years of polish; slower rendering than the GPU terminals; still the choice for tmux-CC users. |
| **WezTerm** (free, OSS, Rust) | Cross-platform (identical on Linux/Windows), Lua config, built-in multiplexer, SSH domains | `~/.wezterm.lua` | The pick if you live on more than one OS and want one config. |
| **Kitty** (free, OSS) | Speed, keyboard-driven, kittens (icat, diff, ssh), graphics protocol | `~/.config/kitty/kitty.conf` | Opinionated maintainer, non-native window chrome. Great with Neovim. |
| **Warp** (freemium, closed) | AI-native: blocks, command palette, natural-language → command, agent mode | GUI | Account optional since 2025; a different paradigm; polarising. Try it if you're new to the CLI. |
| **Alacritty** (free, OSS) | Minimal, fast, no tabs/splits (use tmux) | TOML | Purists only. |
| **Terminal.app** | Zero install | GUI | Fine for occasional use; no splits. |

Install Ghostty and make it default (Ghostty → *Set Ghostty as Default Terminal App*):

```sh
brew install --cask ghostty
```

A starter `~/.config/ghostty/config`:

```
# Font (install a Nerd Font via Homebrew cask; icons in prompts need it)
font-family = JetBrainsMono Nerd Font
font-size = 13
font-thicken = true
adjust-cell-height = 10%

# Theme: light/dark follows the system
theme = light:GitHub-Light-Default,dark:GitHub-Dark-Default
background-opacity = 0.97
background-blur = 20
macos-titlebar-style = tabs
macos-option-as-alt = true            # so ⌥ works as Meta in the shell (Emacs bindings, ⌥← word jumps)
cursor-style = bar
cursor-style-blink = false
mouse-hide-while-typing = true
copy-on-select = clipboard
window-save-state = always
window-inherit-working-directory = true
split-inherit-working-directory = true
scrollback-limit = 100000000
shell-integration-features = cursor,sudo,title
notify-on-command-finish = unfocused
notify-on-command-finish-after = 30s

# Keybinds (defaults are good; a few additions)
keybind = super+d=new_split:right
keybind = super+shift+d=new_split:down
keybind = super+alt+left=goto_split:left
keybind = super+alt+right=goto_split:right
keybind = super+alt+up=goto_split:up
keybind = super+alt+down=goto_split:down
keybind = super+shift+enter=toggle_split_zoom
keybind = global:super+grave=toggle_quick_terminal    # drop-down terminal from anywhere
```

Ghostty ships shell integration for zsh/bash/fish that enables: jump between prompts (<kbd>⌘</kbd><kbd>↑</kbd>/<kbd>↓</kbd>), copy last command's output, click to move the cursor in the prompt, `sudo` with Touch ID passthrough, and the working directory in new tabs. `ghostty +list-themes` previews 400+ themes; `ghostty +show-config --default --docs` lists every option.

**iTerm2 users**: turn on *Shell Integration* (iTerm2 → Install Shell Integration), set *Option key = Esc+* in the profile's Keys tab, enable *GPU rendering*, and consider *Triggers* (highlight or notify on regex in output). **tmux -CC** turns tmux windows into native tabs — unique to iTerm2.

### Shell: zsh, configured by hand

macOS's default shell has been **zsh** since Catalina. Keep it. (Fish is lovely but not POSIX; Bash 3.2 is ancient; Nushell is interesting but niche.) If you want the newest zsh, `brew install zsh`, add `/opt/homebrew/bin/zsh` to `/etc/shells`, then `chsh -s /opt/homebrew/bin/zsh` — but Apple's `/bin/zsh` is fine.

#### Skip Oh My Zsh (or use it knowingly)

Oh My Zsh, Prezto and Zim add hundreds of aliases and a plugin manager with a measurable startup cost, and hide *how* things work — exactly what a CS student should be learning. The modern approach is ~60 lines of your own `.zshrc` plus three plugins loaded directly. If you already love OMZ, keep it, trim to 3–5 plugins, and use a fast prompt. Either way, measure: `time zsh -i -c exit` should be under 100 ms.

#### Where zsh reads config

| File | Read when | Put here |
|---|---|---|
| `~/.zshenv` | Every zsh (including scripts) | `PATH`-independent environment variables, `XDG_*`, `EDITOR`. Keep tiny. |
| `~/.zprofile` | Login shells (each new terminal tab on macOS is a login shell) | `eval "$(brew shellenv)"`, `PATH` additions. |
| `~/.zshrc` | Interactive shells | Aliases, functions, completion, prompt, plugins, key bindings. |
| `~/.zlogout` | On exit | Rarely used. |
| `/etc/zshrc`, `/etc/zprofile` | System-wide, before yours | Apple's; `/etc/zprofile` runs `path_helper`, which rebuilds `PATH` from `/etc/paths` and `/etc/paths.d/*` and **reorders** it — which is why `PATH` set in `.zshenv` gets clobbered. Set PATH in `.zprofile` or `.zshrc`. |

#### A complete, fast `.zshrc`

```sh
# ~/.zshrc — no framework, ~50ms startup
# --- Homebrew (also in .zprofile for login shells; harmless twice) ---
eval "$(/opt/homebrew/bin/brew shellenv)"

# --- history: big, shared, deduplicated ---
HISTFILE="$HOME/.zsh_history"
HISTSIZE=200000
SAVEHIST=200000
setopt SHARE_HISTORY INC_APPEND_HISTORY HIST_IGNORE_ALL_DUPS HIST_IGNORE_SPACE HIST_REDUCE_BLANKS HIST_VERIFY EXTENDED_HISTORY

# --- behaviour ---
setopt AUTO_CD            # `..` and `dirname` without cd
setopt AUTO_PUSHD PUSHD_IGNORE_DUPS PUSHD_SILENT
setopt EXTENDED_GLOB GLOB_DOTS NO_CASE_GLOB
setopt INTERACTIVE_COMMENTS
setopt CORRECT            # suggest corrections for mistyped commands
unsetopt BEEP
bindkey -e                # emacs keybindings (⌃A ⌃E ⌃K ⌃R …); `bindkey -v` for vi mode
WORDCHARS='*?_-.[]~=&;!#$%^(){}<>'   # ⌥⌫ stops at / and .

# --- completion ---
autoload -Uz compinit
# cache compdump; rebuild at most once a day
if [[ -n ~/.zcompdump(#qN.mh+24) ]]; then compinit; else compinit -C; fi
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*:descriptions' format '%F{yellow}-- %d --%f'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path "$HOME/.cache/zsh/zcompcache"
# Homebrew site-functions are on fpath via brew shellenv (gh, docker, kubectl completions land there)

# --- plugins (installed via brew; sourced directly, no plugin manager) ---
source "$(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh"
source "$(brew --prefix)/share/zsh-history-substring-search/zsh-history-substring-search.zsh"
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down
ZSH_AUTOSUGGEST_STRATEGY=(history completion)
ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE=40
source "$(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"   # must be last plugin

# --- tools ---
eval "$(starship init zsh)"                # prompt
eval "$(zoxide init zsh --cmd cd)"         # `cd` learns your dirs; `cdi` interactive
eval "$(fzf --zsh)"                        # ⌃R history, ⌃T files, ⌥C cd
eval "$(mise activate zsh)"                # per-project runtimes (Chapter 11)
eval "$(direnv hook zsh)"                  # per-directory env (Chapter 10)
export FZF_DEFAULT_COMMAND='fd --type f --hidden --exclude .git'
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
export FZF_ALT_C_COMMAND='fd --type d --hidden --exclude .git'
export FZF_DEFAULT_OPTS='--height 40% --layout=reverse --border --info=inline'
export FZF_CTRL_T_OPTS="--preview 'bat --color=always --style=numbers --line-range=:200 {}'"

# --- environment ---
export EDITOR="nvim"         # or "code --wait" / "zed --wait"
export VISUAL="$EDITOR"
export PAGER="less -RFX"
export MANPAGER="sh -c 'col -bx | bat -l man -p'"   # coloured man pages
export BAT_THEME="ansi"
export HOMEBREW_NO_ENV_HINTS=1
export HOMEBREW_BUNDLE_FILE="$HOME/.config/homebrew/Brewfile"
export GPG_TTY=$(tty)

# --- aliases ---
alias ls='eza --group-directories-first --icons=auto'
alias ll='eza -lah --git --group-directories-first --icons=auto'
alias lt='eza --tree --level=2 --icons=auto'
alias cat='bat --paging=never'
alias du='dust'
alias df='duf'
alias top='btop'
alias vim='nvim'
alias g='git'
alias gs='git status -sb'
alias gl='git log --oneline --graph --decorate -20'
alias gd='git diff'
alias gp='git push'
alias gc='git commit'
alias gco='git switch'
alias ..='cd ..'
alias ...='cd ../..'
alias rm='trash'                     # brew install trash; `command rm` for the real thing
alias mkd='mkdir -p'
alias path='echo -e ${PATH//:/\\n}'
alias reload='exec zsh'
alias brewup='brew update && brew upgrade && brew autoremove && brew cleanup --prune=all'
alias ip='curl -s https://ifconfig.me && echo'
alias localip="ipconfig getifaddr en0"
alias flushdns='sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder'

# --- functions ---
mkcd() { mkdir -p "$1" && cd "$1"; }
# fuzzy kill
fkill() { ps -ef | sed 1d | fzf -m --header='[kill:process]' | awk '{print $2}' | xargs -r kill -${1:-9}; }
# fuzzy git branch switch
gb() { git branch --all | grep -v HEAD | fzf --preview 'git log --oneline --graph -20 {1}' | sed 's/.* //' | sed 's#remotes/origin/##' | xargs -r git switch; }
# extract anything
extract() {
  case "$1" in
    *.tar.bz2|*.tbz2) tar xjf "$1" ;;  *.tar.gz|*.tgz) tar xzf "$1" ;;  *.tar.xz) tar xJf "$1" ;;
    *.tar) tar xf "$1" ;;  *.bz2) bunzip2 "$1" ;;  *.gz) gunzip "$1" ;;  *.zip) unzip "$1" ;;
    *.7z) 7z x "$1" ;;  *.rar) unrar x "$1" ;;  *) echo "don't know how to extract '$1'" ;;
  esac
}
cheat() { curl -s "cheat.sh/$1"; }

# --- local overrides (not in dotfiles repo) ---
[[ -f ~/.zshrc.local ]] && source ~/.zshrc.local
```

Install the pieces:

```sh
brew install starship zoxide fzf zsh-autosuggestions zsh-syntax-highlighting zsh-history-substring-search \
             eza bat ripgrep fd dust duf btop trash tlrc
```

Don't alias `grep` to `rg` or `find` to `fd` — scripts and tutorials that call `grep` expect BSD grep flags; use the new names directly and let muscle memory follow.

#### Starship prompt

A single binary, fast, works in every shell, configured in `~/.config/starship.toml`. The default shows directory, git branch/status, language versions when relevant, command duration, and exit status. A compact two-line variant:

```toml
# ~/.config/starship.toml
add_newline = true
format = """
$directory$git_branch$git_status$git_state$python$nodejs$rust$golang$java$cmd_duration
$character"""
[character]
success_symbol = "[❯](bold green)"
error_symbol = "[❯](bold red)"
vimcmd_symbol = "[❮](bold yellow)"
[directory]
truncation_length = 4
truncate_to_repo = true
style = "bold cyan"
[git_branch]
symbol = " "
style = "bold purple"
[git_status]
style = "yellow"
ahead = "⇡${count}"
behind = "⇣${count}"
diverged = "⇕⇡${ahead_count}⇣${behind_count}"
[cmd_duration]
min_time = 2000
format = "took [$duration]($style) "
[python]
symbol = " "
format = '[${symbol}(${version} )(\($virtualenv\) )]($style)'
[nodejs]
symbol = " "
```

Presets: `starship preset nerd-font-symbols -o ~/.config/starship.toml` (needs a Nerd Font); `starship preset plain-text-symbols` if you don't want icons. Alternatives: **Powerlevel10k** (zsh-only, extremely fast with its instant prompt, more ornate), **Pure** (minimal), **Oh My Posh** (cross-shell, Windows heritage).

### The modern CLI toolkit

Rust/Go rewrites of the classics: faster, saner defaults, colour, and — importantly — identical on macOS and Linux, so your muscle memory ports to servers.

| Instead of | Use | Why |
|---|---|---|
| `ls` | **eza** | Colours, icons, git status column, tree mode |
| `cat` | **bat** | Syntax highlighting, line numbers, git diff gutter; `bat -p` for plain |
| `grep -r` | **ripgrep (rg)** | 10× faster, respects `.gitignore`, sane defaults |
| `find` | **fd** | Intuitive syntax (`fd pattern`), ignores `.git`, parallel |
| `cd` | **zoxide** | `cd proj` jumps to the most-used matching directory from anywhere |
| `history` / <kbd>⌃</kbd><kbd>R</kbd> | **fzf** (+ **atuin** optional) | Fuzzy everything; atuin syncs shell history across machines with a SQLite DB |
| `du` | **dust** | Visual tree of what's big |
| `df` | **duf** | Readable table |
| `top` | **btop** (or `htop`) | Pretty, mouse-driven, shows per-core and GPU on Apple silicon |
| `sed` (simple substitutions) | **sd** | `sd 'foo' 'bar' file` — no regex-escaping hell |
| `diff` | **difftastic** / **delta** | Syntax-aware diffs (`git difftool`) / beautiful `git diff` pager |
| `man` | **tlrc (tldr)** | Practical examples first: `tldr tar` |
| `curl` for APIs | **xh** or **httpie** | `xh :8080/api name=alex` |
| `jq` | **jq** (still) + **yq** for YAML, **fx** interactive | |
| `time` | **hyperfine** | Statistical benchmarking with warmup |
| `watch` | **watchexec** / `entr` | Re-run on file change: `watchexec -e py pytest` |
| `ps aux \| grep` | **procs** | Coloured, searchable process list |
| `nano`/`vim` for quick edits | **micro** or **helix** | Modern modal (helix) or non-modal (micro) editors |
| File manager | **yazi** | Blazing TUI file manager with previews; `y` shell wrapper cds on exit |
| Git TUI | **lazygit** | Stage hunks, rebase interactively, without memorising flags |
| Docker TUI | **lazydocker** | |
| Kubernetes TUI | **k9s** | |
| Markdown in terminal | **glow** | `glow README.md` |
| JSON/CSV data | **miller (mlr)**, **qsv**, **visidata** | Spreadsheets in the terminal |
| Misc | **ncdu**, **tokei** (LOC counter), **gping**, **dog** (DNS), **bandwhich**, **ouch** (archives), **presenterm** | |

Don't install all of these on day one. Start with `eza bat rg fd zoxide fzf`, add the rest as you notice the need.

### tmux (or not)

With Ghostty/iTerm2/WezTerm splits, **you don't need tmux locally**. You need it for **remote work** (sessions survive SSH disconnects) and if you want one layout that works identically over SSH. `brew install tmux`, then:

```
# ~/.config/tmux/tmux.conf
set -g prefix C-a            # ⌃A instead of ⌃B (Caps Lock → ⌃ makes this trivial)
unbind C-b
bind C-a send-prefix
set -g mouse on
set -g base-index 1
setw -g pane-base-index 1
set -g renumber-windows on
set -g history-limit 100000
set -g default-terminal "tmux-256color"
set -as terminal-features ",xterm-ghostty:RGB"
set -g escape-time 0
set -g focus-events on
bind | split-window -h -c "#{pane_current_path}"
bind - split-window -v -c "#{pane_current_path}"
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R
bind r source-file ~/.config/tmux/tmux.conf \; display "reloaded"
set -g status-position top
# plugins via tpm: `git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm`
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-yank'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'catppuccin/tmux'
run '~/.tmux/plugins/tpm/tpm'
```

**Zellij** is the modern alternative (Rust, discoverable keybindings shown on screen, layouts in KDL, floating panes). Good for beginners who find tmux's prefix-key model opaque.

### SSH

Generate a modern key (one per machine, never copied between machines):

```sh
ssh-keygen -t ed25519 -C "alex@mbp-2026"
# passphrase: yes. Store it in the keychain so you type it once per login:
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

`~/.ssh/config`:

```
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
  ServerAliveInterval 60
  ServerAliveCountMax 3
  IdentitiesOnly yes

Host github.com
  User git

Host uni
  HostName login.cs.university.edu
  User alex42
  ForwardAgent no
  # ProxyJump bastion.university.edu

Host homelab
  HostName 100.101.102.103      # Tailscale IP
  User alex
  LocalForward 5432 localhost:5432
```

Notes:

- `UseKeychain yes` is a macOS-only option: the passphrase is stored in the login keychain and the key auto-loads.
- Upload the public key with `gh ssh-key add ~/.ssh/id_ed25519.pub --title mbp-2026` (GitHub CLI), or `cat ~/.ssh/id_ed25519.pub | pbcopy` and paste it into the web UI.
- Prefer a **hardware key** (YubiKey, `ssh-keygen -t ed25519-sk`) or **1Password's SSH agent** (keys never sit unencrypted on disk; Touch ID approves each use) for your main identity. 1Password: enable *Developer → SSH Agent* and add `IdentityAgent "~/Library/Group Containers/2BUA8C4S2C.com.1password/t/agent.sock"` to the `Host *` block.
- Turn **on** *Remote Login* in Sharing only if you SSH *into* this Mac. If you do, disable password auth (`PasswordAuthentication no` in a file under `/etc/ssh/sshd_config.d/`) and keep the firewall on.
- **mosh** (`brew install mosh`) for flaky Wi‑Fi; **Tailscale** (Chapter 14) to reach your Mac from anywhere without port forwarding.
- Copy files with `rsync -avz --progress src/ user@host:dst/` — install Homebrew's `rsync`; Apple replaced it with the less capable `openrsync` in Sequoia.

### Touch ID for sudo

Apple made this survive OS updates by adding `/etc/pam.d/sudo_local`. Enable it once:

```sh
sudo sh -c 'sed "s/^#auth/auth/" /etc/pam.d/sudo_local.template > /etc/pam.d/sudo_local'
cat /etc/pam.d/sudo_local   # → auth sufficient pam_tid.so
```

Now `sudo` prompts with Touch ID (or your Apple Watch). Inside **tmux**, Touch ID needs `pam_reattach`: `brew install pam-reattach` and add `auth optional /opt/homebrew/lib/pam/pam_reattach.so` as the *first* line of `sudo_local`. Ghostty's `sudo` shell-integration feature forwards the terminal correctly so it works in splits.

### Fonts and rendering

Install a **Nerd Font** (a programming font patched with 3,000+ icons) — `brew install --cask font-jetbrains-mono-nerd-font` (or Fira Code, Iosevka, Monaspace, Cascadia Code, Geist Mono; Berkeley Mono if you pay for fonts). Use it in the terminal *and* your editor so icons in prompts, `eza`, Neovim and Starship render. Apple's **SF Mono** is excellent but has no icon glyphs; Ghostty falls back to a symbols font if installed (`brew install --cask font-symbols-only-nerd-font`).

Ligatures (`->` becoming an arrow) are a taste thing; JetBrains Mono and Fira Code have them, and Ghostty and most editors let you toggle them.

### Common terminal problems

- **`⌥←` inserts weird characters instead of jumping words**: set Option as Meta/Esc+ (Ghostty `macos-option-as-alt = true`; iTerm2 Profiles → Keys → Left Option = Esc+).
- **Slow new tab**: `time zsh -i -c exit`. Culprits: nvm (use mise), `compinit` without cache, Oh My Zsh with many plugins, Conda's init block. Use `zmodload zsh/zprof` at the top of `.zshrc` and `zprof` at the bottom to find it.
- **`PATH` order wrong / Homebrew tools shadowed by system ones**: `/etc/zprofile`'s `path_helper` reorders PATH; make sure `brew shellenv` runs *after* it (in `.zprofile` or `.zshrc`), and check with `which -a git`.
- **Colours look wrong over SSH**: the remote lacks `xterm-ghostty` terminfo — `infocmp -x xterm-ghostty | ssh host tic -x -` installs it, or set `SetEnv TERM=xterm-256color` for that host in `~/.ssh/config`.
- **Locale warnings on servers**: add `export LANG=en_US.UTF-8` to `.zshenv`.
- **Terminal asks for Full Disk Access / Files & Folders**: normal the first time you touch `~/Desktop`, `~/Documents`, `~/Downloads` or `~/Library/Mail`; grant it in Privacy & Security.
- **"Operation not permitted" writing to `/usr/bin`**: that's SIP; use Homebrew's prefix.

[↑ Back to top](#table-of-contents)

---

## 10. Dotfiles & Git

Everything you configured in the last three chapters lives in text files. Put them in a Git repository and a new Mac — or a reset one — goes from Setup Assistant to *your* environment in twenty minutes. This chapter also sets up Git itself the way a working engineer has it, because the defaults are from 2005.

### What counts as dotfiles

Anything under `~` that starts with a `.`, plus the modern `~/.config/*` tree:

| Config | Path |
|---|---|
| zsh | `~/.zshenv`, `~/.zprofile`, `~/.zshrc` |
| Git | `~/.config/git/config`, `~/.config/git/ignore` (XDG paths — no more `~/.gitconfig`) |
| Ghostty | `~/.config/ghostty/config` |
| Starship | `~/.config/starship.toml` |
| mise | `~/.config/mise/config.toml` |
| tmux | `~/.config/tmux/tmux.conf` |
| Neovim | `~/.config/nvim/` |
| Karabiner | `~/.config/karabiner/karabiner.json` |
| AeroSpace | `~/.aerospace.toml` (or `~/.config/aerospace/aerospace.toml`) |
| Homebrew | `~/.config/homebrew/Brewfile` |
| SSH | `~/.ssh/config` (**not** the keys) |
| VS Code | `~/Library/Application Support/Code/User/settings.json`, `keybindings.json` (or use Settings Sync) |
| Zed | `~/.config/zed/settings.json`, `keymap.json` |
| macOS defaults | your `macos-defaults.sh` script (Chapter 3 / Appendix A) |

**Never commit**: `~/.ssh/id_*`, `~/.gnupg/`, `~/.aws/credentials`, `~/.npmrc` with tokens, `~/.netrc`, `.env` files, anything from `~/Library/Keychains`. Chapter 16 covers where secrets go instead.

### Three ways to manage them

#### 1. The bare-repo trick (zero tools)

Your home directory *is* the working tree; the `.git` directory lives elsewhere so `~` doesn't look like a repo.

```sh
git init --bare "$HOME/.dotfiles"
alias dot='git --git-dir="$HOME/.dotfiles" --work-tree="$HOME"'   # put this in .zshrc
dot config status.showUntrackedFiles no
dot add ~/.zshrc ~/.config/ghostty/config ~/.config/starship.toml ~/.config/git/config
dot commit -m "initial dotfiles"
dot remote add origin git@github.com:you/dotfiles.git
dot push -u origin main
```

On a new machine:

```sh
git clone --bare git@github.com:you/dotfiles.git "$HOME/.dotfiles"
alias dot='git --git-dir="$HOME/.dotfiles" --work-tree="$HOME"'
dot checkout            # fails if files exist — move them aside, retry
dot config status.showUntrackedFiles no
```

Pros: no dependencies, files live in place, `dot diff` works. Cons: no templating (same file on every machine), no secrets handling, easy to accidentally `dot add` something large.

#### 2. chezmoi (recommended for more than one machine)

**chezmoi** (`brew install chezmoi`) is a single Go binary that keeps the source of truth in `~/.local/share/chezmoi` and *applies* it to `~`. Its strengths: **templates** (one `.gitconfig` with `{{ if eq .chezmoi.hostname "work-mbp" }}` blocks), **secrets** pulled from 1Password/Bitwarden/Keychain at apply time (never stored in the repo), `run_once_` scripts (install Homebrew, run `brew bundle`, apply `defaults`), and first-class support for macOS/Linux differences.

```sh
chezmoi init                                  # creates the source repo
chezmoi add ~/.zshrc ~/.config/ghostty/config # copies into the source dir (as dot_zshrc, dot_config/ghostty/config)
chezmoi edit ~/.zshrc                         # edit the source version
chezmoi diff                                  # what would change
chezmoi apply                                 # write to ~
chezmoi cd && git add -A && git commit -m "…" && git push
# new machine — one line, including running your install scripts:
sh -c "$(curl -fsLS get.chezmoi.io)" -- init --apply you
```

A secrets template line: `token = {{ onepasswordRead "op://Private/GitHub/token" }}` — chezmoi calls the 1Password CLI at apply time. Machine-specific data lives in `~/.config/chezmoi/chezmoi.toml` (`[data] email = "…"`, `work = true`).

#### 3. GNU Stow / yadm / Nix Home Manager

- **Stow** (`brew install stow`): keep `~/dotfiles/zsh/.zshrc`, `~/dotfiles/ghostty/.config/ghostty/config`, run `stow zsh ghostty` to symlink them into `~`. Simple, transparent, no templating. Very popular.
- **yadm**: the bare-repo trick with templating and encryption bolted on.
- **Home Manager (Nix)**: declarative, reproducible, manages packages *and* config, steep learning curve; the right answer if you're already Nix-curious and wrong for a first-year student.

Pick chezmoi if you have (or will have) a work Mac and a personal Mac; the bare repo or Stow if you have one machine and like simplicity.

### Repository layout and bootstrap

Whatever the tool, include an `install.sh` (idempotent) at the repo root so the sequence on a fresh Mac is:

```sh
xcode-select --install
git clone git@github.com:you/dotfiles.git ~/.dotfiles   # or the chezmoi one-liner
~/.dotfiles/install.sh
```

The script (Appendix A is a complete one) should: install Homebrew if missing → `brew bundle` → link/apply dotfiles → run `macos-defaults.sh` → `mise install` → set up Touch ID sudo → remind you of the manual steps (sign in to 1Password, add SSH key to GitHub, grant Accessibility to Raycast/Karabiner). Keep a `README.md` with those manual steps; you'll thank yourself in two years.

Structure that scales:

```
dotfiles/
├── install.sh
├── Brewfile
├── macos-defaults.sh
├── zsh/            .zshenv .zprofile .zshrc
├── git/            config ignore
├── ghostty/        config
├── starship.toml
├── mise/           config.toml
├── nvim/           …
├── karabiner/      karabiner.json
├── aerospace/      aerospace.toml
├── vscode/         settings.json keybindings.json extensions.txt
└── README.md       manual steps, hardware notes
```

Include `.zshrc.local` in `.gitignore` and source it from `.zshrc` for machine-specific bits (work proxies, secrets, aliases you'd rather not publish).

### Git, configured properly

Homebrew's `git` (`brew install git`) is newer than Apple's. Use the XDG location so `~` stays clean:

```sh
mkdir -p ~/.config/git
```

`~/.config/git/config`:

```ini
[user]
    name = Alex Kowalski
    email = alex@example.com
    signingkey = ~/.ssh/id_ed25519.pub        # sign commits with your SSH key (no GPG needed)
[gpg]
    format = ssh
[gpg "ssh"]
    allowedSignersFile = ~/.config/git/allowed_signers
    # 1Password users: program = /Applications/1Password.app/Contents/MacOS/op-ssh-sign
[commit]
    gpgsign = true
    verbose = true                            # show the diff in the commit message editor
[tag]
    gpgsign = true
[init]
    defaultBranch = main
[core]
    editor = nvim                             # or: code --wait / zed --wait
    pager = delta
    autocrlf = input
    excludesfile = ~/.config/git/ignore
    fsmonitor = true                          # faster status in big repos (uses FSEvents)
    untrackedCache = true
[color]
    ui = auto
[column]
    ui = auto
[branch]
    sort = -committerdate
[tag]
    sort = version:refname
[fetch]
    prune = true
    pruneTags = true
    all = true
[pull]
    rebase = true
[push]
    default = simple
    autoSetupRemote = true                    # first `git push` just works
    followTags = true
[rebase]
    autoSquash = true
    autoStash = true
    updateRefs = true
[merge]
    conflictstyle = zdiff3
[diff]
    algorithm = histogram
    colorMoved = plain
    mnemonicPrefix = true
    renames = true
[rerere]
    enabled = true
    autoupdate = true
[help]
    autocorrect = prompt
[interactive]
    diffFilter = delta --color-only
[delta]
    navigate = true
    side-by-side = false
    line-numbers = true
    hyperlinks = true
[credential]
    helper = osxkeychain                      # HTTPS tokens in the Keychain; `gh auth login` sets this up too
[url "git@github.com:"]
    insteadOf = https://github.com/           # always push over SSH even if you cloned via HTTPS
[alias]
    st = status -sb
    co = checkout
    sw = switch
    br = branch
    ci = commit
    ca = commit --amend --no-edit
    cm = commit -m
    lg = log --oneline --graph --decorate --all -30
    last = log -1 HEAD --stat
    unstage = reset HEAD --
    undo = reset --soft HEAD~1
    wip = !git add -A && git commit -m "wip"
    fixup = commit --fixup
    please = push --force-with-lease
    aliases = config --get-regexp ^alias\\.
    ignored = ls-files --others --ignored --exclude-standard
    root = rev-parse --show-toplevel
    cleanup = "!git branch --merged | grep -vE '(^\\*|main|master|develop)' | xargs -r git branch -d"
[includeIf "gitdir:~/Developer/work/"]
    path = ~/.config/git/config-work          # different email/signing key for work repos
```

Notes on the choices:

- **SSH commit signing** (Git ≥ 2.34) reuses your SSH key — no GPG keyring to manage. Add the same public key to GitHub as a *Signing key* (`gh ssh-key add ~/.ssh/id_ed25519.pub --type signing`), and put `alex@example.com ssh-ed25519 AAAA…` in `~/.config/git/allowed_signers` so `git log --show-signature` verifies locally. With **1Password** as SSH agent, set `gpg.ssh.program` to `op-ssh-sign` and Touch ID approves each signature.
- `fsmonitor` + `untrackedCache` make `git status` instant in monorepos on macOS.
- `pull.rebase = true` and `rebase.autoStash` keep history linear for the solo-dev workflow; teams that merge can flip it.
- `includeIf` lets your work identity kick in automatically for anything under `~/Developer/work/`.
- `delta` (`brew install git-delta`) gives syntax-highlighted, line-numbered diffs; `difftastic` (`git difftool -t difftastic` after `[difftool "difftastic"] cmd = difft "$LOCAL" "$REMOTE"`) understands syntax trees.

Global ignore, `~/.config/git/ignore`:

```
# macOS
.DS_Store
.AppleDouble
.LSOverride
._*
.Spotlight-V100
.Trashes
Icon?
# editors
.idea/
.vscode/*
!.vscode/settings.json
!.vscode/extensions.json
*.swp
*~
.zed/
# envs & secrets (belt and braces — repos should ignore these too)
.env
.env.*
!.env.example
.envrc
.direnv/
# tooling
.mise.local.toml
.tool-versions.local
node_modules/
__pycache__/
.venv/
.pytest_cache/
.ruff_cache/
.mypy_cache/
target/
dist/
build/
```

### GitHub CLI

`brew install gh`, then `gh auth login` (choose SSH, upload your key, authenticate in the browser). It configures the Keychain credential helper too. Daily use:

```sh
gh repo create my-project --private --clone     # new repo + clone
gh repo clone owner/repo
gh pr create --fill                             # PR from the current branch
gh pr checkout 123                              # review someone's PR locally
gh pr view --web
gh pr checks --watch
gh issue list --assignee @me
gh run watch                                    # tail a GitHub Actions run
gh api repos/{owner}/{repo}/releases            # any REST call
gh extension install dlvhdr/gh-dash             # a TUI dashboard of PRs/issues
gh copilot suggest "undo last commit but keep changes"   # gh-copilot extension
```

GitLab has `glab`; Bitbucket has nothing good. **Git GUI clients** if you want one: **Fork** ($50, fast, best interactive rebase UI), **Tower** ($69/yr), **GitKraken**, **Sublime Merge**, **GitHub Desktop** (free, basic), or the Git panels in VS Code/Zed/JetBrains — plus `lazygit` in the terminal, which many people end up preferring to all of them.

### direnv: per-directory environment

`brew install direnv`, hook it in `.zshrc` (`eval "$(direnv hook zsh)"`). Drop a `.envrc` in a project:

```sh
# .envrc
dotenv_if_exists .env          # load KEY=value pairs from .env (which is gitignored)
export DATABASE_URL=postgres://localhost/myapp_dev
PATH_add ./bin ./node_modules/.bin
layout python                  # or `use mise` / `use flake` (nix) — activates a venv automatically
```

`direnv allow` once; from then on, `cd` into the directory loads the environment and leaving it unloads it. `mise` (Chapter 11) can do the env part too (`[env]` in `.mise.toml`), so many people use only mise; direnv remains the standard for teams with mixed tooling and for Nix flakes.

### Secrets hygiene for repos

- Commit `.env.example` with placeholder keys; never `.env`. Add `.env*` to the global ignore (above) *and* each repo's `.gitignore`.
- Install **gitleaks** or **trufflehog** (`brew install gitleaks`) and run it as a pre-commit hook: `pre-commit` (`brew install pre-commit`) with a `.pre-commit-config.yaml` including `gitleaks`. GitHub's push protection also blocks known token formats on push for public repos and for orgs with Advanced Security.
- If you *do* commit a secret: rotate it immediately (assume it's compromised the moment it hits a remote), then rewrite history with `git filter-repo` and force-push. Rotating is the important part; the rewrite is hygiene.
- Store personal API keys in the **macOS Keychain** (`security add-generic-password -a "$USER" -s openai_api_key -w`) and read them in `.zshrc` lazily, or in **1Password** and inject with `op run --env-file=.env.tpl -- npm start`. Both beat a plaintext `export OPENAI_API_KEY=` in your dotfiles.
- SSH keys: one per machine, passphrase-protected, in the Keychain or a hardware token. Revoke a machine's key on GitHub when you sell it.

[↑ Back to top](#table-of-contents)

---

## 11. Languages & runtimes

The rule that prevents 90% of "it works on my machine": **never use the system interpreter, never install runtimes globally with Homebrew when the project pins a version, and manage every language with one tool.** In 2026 that tool is **mise**, with **uv** handling Python's packaging on top. This chapter sets up each major language the way a CS curriculum or a modern job will need it.

### mise: one version manager to rule them all

**mise** (`brew install mise`, "mise-en-place") is a Rust binary that replaces nvm, fnm, pyenv, rbenv, goenv, jenv, sdkman and asdf. It reads `.tool-versions` (asdf-compatible) and `mise.toml`, installs the exact version each project needs, and switches when you `cd`. It also manages **environment variables** and **tasks** per project, which is why it can replace direnv and a Makefile too.

```sh
brew install mise
echo 'eval "$(mise activate zsh)"' >> ~/.zshrc     # already in the Chapter 9 .zshrc
mise doctor
```

Global defaults (used when a project doesn't pin):

```sh
mise use --global node@lts python@3.13 go@latest java@temurin-25 rust@stable bun@latest
mise ls                # what's installed & active
mise outdated
mise upgrade
```

That writes `~/.config/mise/config.toml`:

```toml
[tools]
node = "lts"
python = "3.13"
go = "latest"
java = "temurin-25"
rust = "stable"
bun = "latest"
uv = "latest"
# CLI tools from GitHub releases / npm / cargo / pipx — mise handles these "backends" too
"npm:typescript" = "latest"
"cargo:cargo-watch" = "latest"
"pipx:ruff" = "latest"
"github:jdx/usage" = "latest"

[settings]
experimental = true
idiomatic_version_file_enable_tools = ["node", "python", "ruby"]   # honour .nvmrc / .python-version / .ruby-version
python.uv_venv_auto = true          # auto-create/activate a uv venv when a project has pyproject.toml
```

Per project, in the repo root:

```toml
# mise.toml
[tools]
node = "24"
python = "3.13"
"npm:pnpm" = "10"

[env]
DATABASE_URL = "postgres://localhost/myapp_dev"
_.file = ".env"                     # load .env (gitignored)
_.python.venv = { path = ".venv", create = true }

[tasks.dev]
run = "pnpm dev"
[tasks.test]
run = ["uv run pytest", "pnpm test"]
[tasks.lint]
run = "ruff check . && pnpm lint"
```

Then `mise install` installs exactly those versions, `mise run dev` runs the task, `mise trust` approves a new project's config the first time (untrusted `mise.toml` files don't execute — a good security default). Commit `mise.toml` (or `.tool-versions` for asdf users) so teammates and CI get the same versions; `mise.local.toml` is for personal overrides and goes in the global gitignore.

Why mise over the alternatives in 2026: it's a single fast binary (no shell-function overhead like nvm's 200 ms), covers every language plus arbitrary GitHub-release binaries, is asdf-compatible so existing `.tool-versions` files just work, and the `env`/`tasks` features remove two more tools from your setup. **asdf** (rewritten in Go in 2025) still works but is slower and needs plugins; **nvm** is the slowest thing you can put in a `.zshrc`; **fnm**/**volta** are good but Node-only; **pyenv** is fine but redundant next to uv.

### Python

Python is the language most likely to be a mess on a Mac. There are at least four interpreters on a typical machine (Apple's CLT shim, Homebrew's, one from the python.org installer, a Conda one) and a dozen packaging tools. The 2026 answer is **uv**.

#### uv does everything

**uv** (Astral, Rust; `brew install uv` or via mise) replaces `pip`, `pip-tools`, `pipx`, `pyenv`, `virtualenv`, `poetry` and `twine`, and is 10–100× faster than pip:

```sh
uv python install 3.13 3.12        # managed interpreters, no Homebrew python needed
uv python list
uv init myproject && cd myproject   # pyproject.toml + .python-version + hello.py
uv add requests numpy               # adds to pyproject, resolves, installs into .venv (created automatically)
uv add --dev pytest ruff mypy
uv run python main.py               # runs in the project venv — no `source .venv/bin/activate` needed
uv run pytest
uv lock                             # uv.lock — commit it
uv sync                             # reproduce the env from the lock (what CI and teammates run)
uv tool install ruff                # global CLI tools, isolated (was pipx)
uvx ruff check .                    # run a tool without installing (was pipx run)
uv pip install -r requirements.txt  # drop-in pip for legacy projects
uv venv                             # plain venv if you want one
```

For a course that hands you a `requirements.txt`: `uv venv && uv pip install -r requirements.txt && source .venv/bin/activate` — done in two seconds. If a lecturer's instructions say `python -m venv venv; pip install …`, they still work inside `uv run`/an activated venv; uv is a superset.

**Do not** `pip install` anything into `/usr/bin/python3` (Apple's) or `/opt/homebrew/bin/python3` — modern pip refuses anyway ("externally-managed-environment"). Homebrew's Python exists for Homebrew's own formulae; leave it alone.

**Ruff** (linter + formatter, replaces flake8/isort/black), **mypy** or **pyright**/**ty** (type checking), **pytest**, **ipython**/**Jupyter**: install per project with `uv add --dev`, or globally as tools with `uv tool install`.

#### Python 3.14 and 3.15

3.14 (Oct 2025) is current; **3.15 lands ~October 1, 2026**. 3.13+ offers an optional **free-threaded** build (`uv python install 3.14t`) with the GIL disabled and an experimental JIT — useful for a concurrency course, not for default use. Some scientific packages lag a new release by 1–3 months; if `uv add numpy` fails on 3.15 in October, pin `python = "3.14"` in `mise.toml`.

#### Conda, Jupyter, data science

If your course requires **Anaconda/Miniconda** (common in data-science and stats departments), install **Miniforge** (`brew install --cask miniforge`, conda-forge defaults, arm64-native, no Anaconda licence issues) and run `conda config --set auto_activate_base false` so it doesn't hijack every shell. Prefer `mamba`/`micromamba` for speed. Mixing conda and uv in one project is asking for trouble — pick per project. For Jupyter: `uv add --dev jupyterlab` then `uv run jupyter lab`, or use VS Code's notebook UI (`ms-toolsai.jupyter`), or **JupyterLab Desktop**. **Positron** (Posit's VS Code-based data science IDE) is the R + Python IDE of choice; **RStudio** if you prefer.

Apple silicon notes: NumPy/SciPy use Apple's **Accelerate** BLAS by default (fast); PyTorch supports the **MPS** backend (`torch.device("mps")`) for GPU training on the Mac; TensorFlow via `tensorflow-metal`; JAX via `jax-metal` (experimental). See [ML](#machine-learning-on-apple-silicon) below.

### JavaScript / TypeScript

#### Node.js

Install through mise, never through the Node installer or Homebrew's `node` (which can't switch versions):

```sh
mise use --global node@lts     # Node 24 LTS today; Node 26 becomes LTS in October 2026
mise use node@26               # per project
corepack enable                # lets `pnpm`/`yarn` commands install themselves at the version in package.json
```

**Release schedule change**: Node 26 (April 2026) is the last release under the odd/even model; it enters LTS October 2026 and is supported to April 2029. From October 2026 Node moves to **one major per year (April), every release LTS, an Alpha channel October–March**, with versions matching the year (27.0.0 in April 2027). Practically: pin the current LTS in `mise.toml` and bump once a year.

#### Package managers

- **pnpm** (`mise use -g "npm:pnpm"` or `corepack`) — fast, disk-efficient (content-addressed store), strict; the 2026 default for new projects.
- **npm** — ships with Node; fine; slower; `npm ci` in CI.
- **Bun** (`mise use -g bun@latest`) — a runtime *and* package manager *and* bundler *and* test runner. `bun install` is the fastest installer; `bun run` executes TypeScript directly. Increasingly used as the package manager even for Node projects.
- **Yarn** — Berry (v4) is fine if a project already uses it; don't start new projects on Yarn Classic.
- **Deno** 2.x — Node-compatible, secure-by-default, great for scripts and Fresh apps.

Set `pnpm config set store-dir ~/.local/share/pnpm/store` once. Global CLI tools: `pnpm add -g` or via mise's `npm:` backend so they're in your `config.toml`.

#### Tooling

TypeScript (`pnpm add -D typescript`), **Biome** (linter+formatter, replaces ESLint+Prettier for many stacks) or ESLint 9 + Prettier, **Vite** for front-end, **Vitest**/**Bun test**/**Playwright** for tests. Browser devtools: Safari's Web Inspector (`Settings → Advanced → Show features for web developers`), Chrome DevTools, Firefox Developer Edition. **Node version in VS Code terminals** follows mise automatically because the integrated terminal runs your zsh.

### Java, Kotlin, and the JVM

```sh
mise use --global java@temurin-25     # JDK 25 is the current LTS (Sept 2025)
mise use java@temurin-21              # per project, e.g. a course pinned to 21
mise ls-remote java | grep -E "temurin|zulu|graalvm|corretto" | tail
java -version
```

mise installs from Adoptium (Temurin), Azul (Zulu), Amazon (Corretto), GraalVM, Liberica etc. and sets `JAVA_HOME` automatically. Do **not** use Oracle's `.dmg` installer or Apple's `/usr/bin/java` stub (it just tells you to install a JDK). If a GUI app (IntelliJ, Android Studio, jEnv-style scripts) needs a system-visible JDK, install one as a Homebrew cask too (`brew install --cask temurin@21`), which registers under `/Library/Java/JavaVirtualMachines` and shows in `/usr/libexec/java_home -V`.

Build tools: **Gradle** and **Maven** via mise (`mise use gradle@latest maven@latest`) or Homebrew; **Kotlin** compiler via mise if you need `kotlinc` outside IntelliJ. IDE: **IntelliJ IDEA Community** (free) or **Ultimate** (free for students — Chapter 20). **Android Studio** (`brew install --cask android-studio`) bundles its own JDK and SDK; set `ANDROID_HOME=~/Library/Android/sdk` and add `$ANDROID_HOME/platform-tools` to PATH for `adb`. The Android emulator runs arm64 system images natively and fast on Apple silicon — pick *arm64-v8a* images, never x86.

### Go

```sh
mise use --global go@latest      # Go 1.27 (Aug 2026); mise sets GOROOT, and GOPATH defaults to ~/go
go env GOPATH GOMODCACHE
```

Add `$HOME/go/bin` to PATH for `go install`-ed tools (mise does this if you enable `go.set_gobin`). Go's toolchain directive in `go.mod` can auto-download the right version anyway (`GOTOOLCHAIN=auto`), so `brew install go` is *acceptable* for Go specifically — it's the one language whose own tooling handles versions well. Tooling: `gopls` (installed by VS Code's Go extension / Zed automatically), `golangci-lint` (`brew install golangci-lint`), `air` for live reload, `delve` for debugging (`go install github.com/go-delve/delve/cmd/dlv@latest` — needs codesigning on macOS; the VS Code extension handles it).

### Rust

```sh
mise use --global rust@stable    # or: brew install rustup && rustup-init
rustup component add rust-analyzer clippy rustfmt
cargo install cargo-watch cargo-edit cargo-nextest   # or via mise "cargo:" backend
```

Rust's own `rustup` is excellent and mise wraps it. The 2024 edition is current; `rustup update` twice a year. Apple silicon is a Tier 1 target. Linkers: the default Apple `ld` is fine; `lld` via `brew install llvm` speeds up big builds. Rust-analyzer in VS Code/Zed/RustRover (JetBrains, free for non-commercial) works out of the box.

### C and C++

Apple's **clang** from the CLT is the compiler (`gcc` is a symlink to clang; `g++` too). For a systems or compilers course that assumes GNU GCC specifically (`__attribute__` quirks, `-fanalyzer`, gcc-only sanitisers): `brew install gcc` gives `gcc-15`/`g++-15`. For a newer LLVM than Apple ships: `brew install llvm` (keg-only; add `$(brew --prefix llvm)/bin` to PATH when you want it) — it includes `clangd`, `clang-format`, `clang-tidy`, `lldb`, `lld`, and libc++ with the latest C++26 features.

Build systems: `cmake` and `ninja` (Homebrew), `meson`, `bazel`/`bazelisk`, `just` (a modern Make). Package managers: **vcpkg** or **Conan**; or Homebrew for system libs (`brew install boost fmt eigen sdl2`). Debugging: `lldb` (Apple), or `gdb` via Homebrew (**gdb needs codesigning on macOS** to attach — search "gdb codesign macOS"; most people use lldb or the IDE debugger). Sanitisers: `-fsanitize=address,undefined` works with Apple clang; ThreadSanitizer too. **Valgrind does not run on Apple silicon** — use ASan/LeakSanitizer or Instruments (Leaks/Allocations) instead; if a course *requires* Valgrind, run it in a Linux container (Chapter 13).

Headers: `xcrun --show-sdk-path` for the SDK; Homebrew packages install headers under `/opt/homebrew/include`, which clang doesn't search by default — pass `-I$(brew --prefix)/include -L$(brew --prefix)/lib` or set `CPATH`/`LIBRARY_PATH` in `.zshrc`.

IDE: VS Code + clangd extension (**not** Microsoft's C/C++ IntelliSense — clangd is faster and more accurate), CLion (free for non-commercial), Xcode for Apple-platform C/C++/Objective-C.

### Swift

Comes with Xcode/CLT (Swift 6.3 with Xcode 27). `swift package init`, `swift build`, `swift test`; Swift Package Manager is the build system. Server-side Swift (Vapor, Hummingbird) works on macOS and Linux. **swiftly** is Apple's official toolchain manager for switching Swift versions outside Xcode (`brew install swiftly`). Editors beyond Xcode: VS Code with the Swift extension (SourceKit-LSP), Zed, Neovim.

### Ruby

```sh
mise use --global ruby@3.4       # Ruby 4.0 shipped Dec 2025; 3.4 remains widely used
gem install bundler rails
```

Never use `/usr/bin/ruby` (Apple's, 2.6, for legacy scripts). mise compiles Ruby via ruby-build; `brew install openssl@3 libyaml gmp` first avoids build errors. Rails needs a database (Chapter 15) and `libvips` or `imagemagick` for Active Storage.

### PHP, .NET, others

- **PHP**: `brew install php` (8.5) or `mise use php@8.5`; **Laravel Herd** (free) bundles PHP/nginx/DNS for a zero-config local Laravel setup. Composer via Homebrew.
- **.NET**: `brew install --cask dotnet-sdk` (.NET 10 LTS; .NET 11 in November 2026) or `mise use dotnet@10`. VS Code + C# Dev Kit, or **Rider** (free for non-commercial).
- **Elixir/Erlang**: mise (`erlang@27 elixir@1.18`); `brew install wxwidgets` first for the observer.
- **Haskell**: `ghcup` (official) — `brew install ghcup` then `ghcup tui`; HLS via ghcup.
- **OCaml**: `brew install opam && opam init`.
- **Zig**: `mise use zig@latest` or `brew install zig` (Ghostty is written in it).
- **Lua**: `brew install lua luarocks`; **R**: `brew install --cask r` + Positron/RStudio; **Julia**: `brew install --cask julia` or `juliaup`.
- **Assembly / low-level courses**: Apple silicon is **AArch64**, not x86. If a course teaches x86-64 assembly, run an x86 Linux VM (UTM, Chapter 13) or use the department's servers; `nasm` and `gcc -m32` don't target this hardware. For ARM assembly, `clang -arch arm64` and `lldb` work natively — a genuine advantage.

### Machine learning on Apple silicon

Unified memory makes Macs unusually good for *running* models locally and adequate for *training* small ones; they are not a substitute for NVIDIA GPUs (CUDA) for serious training, so expect to use the university cluster or cloud for that.

- **PyTorch**: `uv add torch torchvision` — arm64 wheels with the **MPS** backend. `device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")`. Most ops are supported; set `PYTORCH_ENABLE_MPS_FALLBACK=1` for the rest.
- **MLX**: Apple's open-source array framework designed for unified memory (`uv add mlx mlx-lm`). Fastest way to run/fine-tune LLMs locally: `mlx_lm.generate --model mlx-community/Llama-3.3-8B-Instruct-4bit --prompt "…"`. macOS 26.2+ gives M5 chips full MLX access to the Neural Accelerators.
- **Core AI** (macOS 27) and the **Foundation Models framework** (macOS 26) are the Swift APIs for building apps on Apple's on-device models — relevant if you write Swift apps.
- **Local LLM runners**: **Ollama** (`brew install ollama`; `ollama run gemma3`), **LM Studio** (GUI, MLX + llama.cpp backends), **llama.cpp** (`brew install llama.cpp`). Rule of thumb: a Q4-quantised model needs roughly *parameters × 0.6 GB* of memory — 8B ≈ 5 GB, 32B ≈ 20 GB, 70B ≈ 40 GB. Keep 8 GB free for the OS.
- **Coding agents locally**: Ollama + Continue/Zed/Cursor can point at a local model; quality trails the hosted frontier models substantially in 2026, but it's free and offline.
- **Jupyter + GPU**: everything above works from a notebook. **TensorFlow** needs `tensorflow-metal`; **JAX** has `jax-metal` (experimental). **scikit-learn**, **pandas**, **polars** are all native and fast.
- Watch **Activity Monitor → GPU** and the memory pressure graph; when a model doesn't fit, macOS swaps and everything crawls.

### The 2026 release calendar (for pinning decisions)

| Language | Current stable (Sept 2026) | Next | Long-term pick for a new project |
|---|---|---|---|
| Python | 3.14 | 3.15 — Oct 2026 | 3.13 or 3.14 (3.15 after the ecosystem catches up ~Dec) |
| Node.js | 24 LTS (Current: 26) | 26 → LTS Oct 2026; 27 Alpha Oct 2026, 27.0 Apr 2027 | 24 now, move to 26 in October |
| Java | JDK 25 LTS (JDK 27 feature release Sept 2026) | next LTS per Oracle's 2-year cadence: JDK 29 (Sept 2027) | Temurin 25 |
| Go | 1.27 | 1.28 — Feb 2027 | latest (Go's compatibility promise makes this safe) |
| Rust | 1.9x stable, 2024 edition | 6-weekly | stable |
| Swift | 6.3 (Xcode 27) | 6.4 — spring 2027 | whatever your Xcode ships |
| Ruby | 4.0 | 4.1 — Dec 2026 | 3.4 or 4.0 |
| .NET | 10 LTS | 11 — Nov 2026 | 10 |
| PHP | 8.5 | 8.6 — Nov 2026 | 8.5 |
| TypeScript | 6.x (TS 7 Go-native compiler rolling out) | | latest |
| Bun | 1.3+ | | latest |

Pin **exact** versions in `mise.toml` for anything you deploy; pin `lts`/`latest` for coursework and throwaway scripts.

### Editors know about mise

VS Code, Zed, Cursor and JetBrains detect the interpreter/runtime from the shell environment mise sets up — as long as you launch them *from a terminal* (`code .`) or have `mise activate` in `.zprofile` so GUI-launched apps inherit it. If VS Code picks the wrong Python, `⌘⇧P → Python: Select Interpreter` and choose `.venv/bin/python`. For JetBrains, add the mise-installed SDK path once (`mise where python@3.13`).

[↑ Back to top](#table-of-contents)

---

## 12. Editors, IDEs & AI coding tools

The editor market split three ways in 2025–2026: **VS Code** remains the free universal default (~76% share in the Stack Overflow survey), **Cursor** is the AI-native fork that a fifth of developers now use, and **Zed** is the fast native newcomer. JetBrains stays the choice for Java/Kotlin and heavy refactoring; Neovim for the terminal-native; Xcode for Apple platforms. You don't have to pick one — most engineers run two.

### The recommendation

| You are… | Install | Why |
|---|---|---|
| A **CS student** | **VS Code** (free) + Copilot Student (free) — and **JetBrains** IDEs for Java/Kotlin courses (free with a student licence) | Every course's instructions assume VS Code; JetBrains for the JVM is what industry uses |
| A **working engineer**, general | **VS Code** or **Cursor** as primary, **Zed** for speed on big repos, terminal agent (Claude Code / Codex) alongside | The AI layer is now the differentiator; VS Code+Copilot vs Cursor is a taste/budget call |
| Deep in one ecosystem | **JetBrains** (IntelliJ/PyCharm/GoLand/RustRover/CLion/WebStorm) | Nothing beats their refactoring, debugger and framework awareness |
| Apple platforms | **Xcode 27** (+ VS Code/Zed for Swift packages) | Required for signing, simulators, Instruments |
| Terminal-native | **Neovim** (LazyVim or kickstart.nvim) or **Helix** | Everything over SSH, zero latency, infinitely configurable |

### Visual Studio Code

```sh
brew install --cask visual-studio-code
```

Launch once, then in the Command Palette (<kbd>⌘</kbd><kbd>⇧</kbd><kbd>P</kbd>) run *Shell Command: Install 'code' command in PATH* so `code .` works (Homebrew's cask usually does this for you). Turn on **Settings Sync** (sign in with GitHub) so extensions, settings, keybindings and snippets follow you to the next machine — or keep `settings.json`/`keybindings.json` in your dotfiles.

#### Settings that matter

`⌘,` → open *settings.json* (the `{}` icon top right). A developer baseline:

```jsonc
{
  // --- editor ---
  "editor.fontFamily": "JetBrainsMono Nerd Font, Menlo, monospace",
  "editor.fontSize": 13,
  "editor.fontLigatures": true,
  "editor.lineHeight": 1.6,
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": { "source.fixAll": "explicit", "source.organizeImports": "explicit" },
  "editor.rulers": [88, 120],
  "editor.minimap.enabled": false,
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active",
  "editor.cursorSmoothCaretAnimation": "on",
  "editor.smoothScrolling": true,
  "editor.linkedEditing": true,
  "editor.stickyScroll.enabled": true,
  "editor.inlineSuggest.enabled": true,
  "editor.accessibilitySupport": "off",
  // --- files ---
  "files.autoSave": "onFocusChange",
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.exclude": { "**/.git": true, "**/node_modules": true, "**/.venv": true, "**/__pycache__": true },
  "files.watcherExclude": { "**/node_modules/**": true, "**/.venv/**": true, "**/target/**": true },
  "search.exclude": { "**/node_modules": true, "**/dist": true, "**/.venv": true },
  // --- workbench ---
  "workbench.startupEditor": "none",
  "workbench.colorTheme": "GitHub Dark Default",
  "workbench.iconTheme": "material-icon-theme",
  "workbench.editor.enablePreview": false,
  "workbench.tree.indent": 16,
  "window.autoDetectColorScheme": true,
  "window.newWindowDimensions": "inherit",
  "window.titleBarStyle": "custom",
  // --- terminal (runs your zsh, inherits mise) ---
  "terminal.integrated.fontFamily": "JetBrainsMono Nerd Font",
  "terminal.integrated.fontSize": 13,
  "terminal.integrated.defaultProfile.osx": "zsh",
  "terminal.integrated.scrollback": 20000,
  "terminal.integrated.macOptionIsMeta": true,
  "terminal.integrated.enableMultiLinePasteWarning": "never",
  // --- git ---
  "git.autofetch": true,
  "git.confirmSync": false,
  "git.enableSmartCommit": true,
  "git.openRepositoryInParentFolders": "always",
  "diffEditor.ignoreTrimWhitespace": false,
  // --- languages ---
  "[python]": { "editor.defaultFormatter": "charliermarsh.ruff", "editor.tabSize": 4 },
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true,
  "[go]": { "editor.defaultFormatter": "golang.go", "editor.tabSize": 4, "editor.insertSpaces": false },
  "[rust]": { "editor.defaultFormatter": "rust-lang.rust-analyzer" },
  "[markdown]": { "editor.wordWrap": "on", "editor.formatOnSave": false },
  "typescript.updateImportsOnFileMove.enabled": "always",
  "javascript.updateImportsOnFileMove.enabled": "always",
  "typescript.preferences.importModuleSpecifier": "relative",
  // --- telemetry / noise ---
  "telemetry.telemetryLevel": "off",
  "update.showReleaseNotes": false,
  "extensions.ignoreRecommendations": false,
  "security.workspace.trust.untrustedFiles": "open"
}
```

#### Extensions (a curated, not exhaustive, list)

```sh
# generic
code --install-extension eamodio.gitlens              # or the lighter mhutchie.git-graph
code --install-extension usernamehw.errorlens          # inline diagnostics
code --install-extension editorconfig.editorconfig
code --install-extension esbenp.prettier-vscode
code --install-extension biomejs.biome
code --install-extension streetsidesoftware.code-spell-checker
code --install-extension pkief.material-icon-theme
code --install-extension github.github-vscode-theme
code --install-extension ms-vscode-remote.remote-ssh     # edit on servers
code --install-extension ms-vscode-remote.remote-containers
code --install-extension ms-azuretools.vscode-containers
code --install-extension redhat.vscode-yaml
code --install-extension tamasfe.even-better-toml
code --install-extension mikestead.dotenv
code --install-extension yzhang.markdown-all-in-one
# languages
code --install-extension ms-python.python charliermarsh.ruff ms-python.debugpy ms-toolsai.jupyter
code --install-extension golang.go
code --install-extension rust-lang.rust-analyzer vadimcn.vscode-lldb
code --install-extension llvm-vs-code-extensions.vscode-clangd
code --install-extension sswg.swift-lang
code --install-extension vscjava.vscode-java-pack
code --install-extension dbaeumer.vscode-eslint
code --install-extension bradlc.vscode-tailwindcss
# AI (pick one)
code --install-extension github.copilot github.copilot-chat
```

Record them in your dotfiles with `code --list-extensions > vscode/extensions.txt` — or as `vscode "…"` lines in the Brewfile (Chapter 8), which `brew bundle` installs.

#### Keyboard essentials (macOS)

<kbd>⌘</kbd><kbd>P</kbd> file, <kbd>⌘</kbd><kbd>⇧</kbd><kbd>P</kbd> command, <kbd>⌘</kbd><kbd>⇧</kbd><kbd>O</kbd> symbol, <kbd>⌘</kbd><kbd>T</kbd> workspace symbol, <kbd>⌘</kbd><kbd>B</kbd> sidebar, <kbd>⌘</kbd><kbd>J</kbd> panel/terminal, <kbd>⌃</kbd><kbd>`</kbd> terminal, <kbd>⌘</kbd><kbd>\</kbd> split, <kbd>⌘</kbd><kbd>1/2/3</kbd> editor group, <kbd>⌥</kbd><kbd>↑/↓</kbd> move line, <kbd>⌥</kbd><kbd>⇧</kbd><kbd>↑/↓</kbd> copy line, <kbd>⌘</kbd><kbd>D</kbd> add selection to next match, <kbd>⌘</kbd><kbd>⇧</kbd><kbd>L</kbd> select all matches, <kbd>F2</kbd> rename, <kbd>F12</kbd> definition, <kbd>⌥</kbd><kbd>F12</kbd> peek, <kbd>⇧</kbd><kbd>F12</kbd> references, <kbd>⌘</kbd><kbd>.</kbd> quick fix, <kbd>⌘</kbd><kbd>K</kbd> <kbd>⌘</kbd><kbd>S</kbd> keybindings editor. Install the **Vim** or **VSCode Neovim** extension if you're modal.

#### VS Code vs VSCodium

VS Code's binary is MIT-licensed source plus Microsoft telemetry, branding and the proprietary Marketplace. **VSCodium** (`brew install --cask vscodium`) is the telemetry-free build using the Open VSX registry; a few extensions (Copilot, Remote SSH, Pylance, C# Dev Kit) are Microsoft-only and don't work there. For students who need Copilot, plain VS Code with `telemetry.telemetryLevel: off` is the pragmatic answer.

### Cursor

**Cursor** (`brew install --cask cursor`) is a fork of VS Code with the AI layer rebuilt as first-class: **Tab** (multi-line predictive edits), **Agent/Composer** (plan and execute multi-file changes, run commands, fix from terminal errors), inline <kbd>⌘</kbd><kbd>K</kbd> edits, codebase indexing, and bundled frontier models (Anthropic, OpenAI, Google, its own). It imports your VS Code settings, keybindings and extensions on first launch; nearly all extensions work.

Pricing (Sept 2026): **Hobby** free (limited), **Pro $20/mo** (~$20 of model credits), **Pro+ $60**, **Ultra $200**, Teams $40/user + base fee. Students have periodically been offered a free year of Pro — check cursor.com/students. The credits model means heavy agent use runs out mid-month; set a spend alert.

Use Cursor if AI assistance is the reason you'd switch editors; stay on VS Code + Copilot if you want a flat price and Microsoft's ecosystem (Remote SSH, Dev Containers, Pylance) without fork lag — Cursor tracks VS Code releases with a delay of weeks. Windsurf (Codeium, now under Cognition) and Google's **Antigravity** (agent-manager IDE) are the other AI-first forks worth a look; Antigravity's multi-agent orchestration is the most different idea in the space.

### Zed

**Zed** (`brew install --cask zed`) is a native Rust editor with a GPU renderer from the creators of Atom: ~180 ms cold start vs 2+ s for Electron editors, ~140 MB idle memory, 8 ms keystroke latency, built-in real-time collaboration (multiplayer editing and voice), Vim mode that's actually good, and an **Agent Panel** that speaks the open **Agent Client Protocol** so you can plug in Claude Code, Gemini CLI, OpenCode or Zed's own hosted models. Language servers install automatically per file type. The editor is free and open source; **Zed Pro** (~$10/mo) is only for hosted AI usage.

Zed is the right choice for large monorepos and for people who find VS Code sluggish, and for pair programming. Its gaps in 2026: a smaller extension ecosystem (no VS Code extension compatibility), a debugger that's newer and less complete than VS Code's, Windows support still maturing. Many people run Zed for editing and VS Code for debugging. Config: `~/.config/zed/settings.json` and `keymap.json` (`⌘,`) — it imports VS Code keybindings and themes.

### JetBrains

IntelliJ IDEA, PyCharm, WebStorm, GoLand, RustRover, CLion, Rider, DataGrip, PhpStorm, RubyMine, Android Studio (Google's fork). Install via **JetBrains Toolbox** (`brew install --cask jetbrains-toolbox`), which manages versions, updates and the `idea`/`pycharm` shell launchers. **Free for students and teachers** (jetbrains.com/academy/student-pack, or via the GitHub Student Developer Pack) — the full Ultimate/Professional editions, renewable yearly while enrolled. WebStorm, RustRover, Rider, CLion and Aqua also have **free non-commercial licences** for everyone since 2024–2025. IntelliJ Community and PyCharm Community are free for any use.

Why JetBrains despite VS Code: language-aware refactoring that's actually safe across a whole project, the best debugger UX, deep framework understanding (Spring, Django, Rails, Next.js), database tools built in (Ultimate), and *everything* working out of the box without assembling extensions. Cost: memory (2–4 GB per IDE), indexing time on first open, and a heavier UI. The **AI Assistant** and **Junie** agent are JetBrains' AI layer (subscription; a free tier exists); Copilot and Claude Code also plug in.

macOS notes: the *IdeaVim* plugin is excellent; enable *Settings → Keymap → macOS* (default) and bind <kbd>⌘</kbd><kbd>⇧</kbd><kbd>A</kbd> (Find Action) into your fingers; increase the heap for big projects (*Help → Change Memory Settings*, 4096 MB); exclude `~/Library/Caches/JetBrains` from Time Machine.

### Neovim

`brew install neovim`. Start from a distribution rather than an empty config:

- **LazyVim** — batteries-included, lazy.nvim plugin manager, LSP/Treesitter/Telescope/Snacks preconfigured, Mason installs language servers. `git clone https://github.com/LazyVim/starter ~/.config/nvim && nvim`.
- **kickstart.nvim** — a single, heavily commented `init.lua` meant to be *read* and owned. Best for learning what each piece does (recommended for students).
- **AstroNvim**, **NvChad**, **LunarVim** — other full distros.

Pair with Ghostty (true colour, Kitty keyboard protocol for extra keybindings, Nerd Font for icons), `ripgrep` and `fd` (Telescope uses them), `lazygit` (Neovim plugin exists), and a clipboard bridge — Neovim on macOS uses `pbcopy`/`pbpaste` automatically for `"+`. AI in Neovim: **codecompanion.nvim**, **avante.nvim**, **copilot.lua**, or just run Claude Code in a split. **Helix** (`brew install helix`) is the modern alternative: Kakoune-style selection-first editing, LSP and Treesitter built in, zero-plugin philosophy — a great choice if you want modal editing without the configuration hobby.

### Xcode (for Apple platforms)

Chapter 7 covers installing it. Settings worth changing: *Text Editing → Display*: line numbers, code folding ribbon, page guide at 120; *Text Editing → Editing*: while editing, automatically trim trailing whitespace including whitespace-only lines; *Themes*: pick a dark one or install one; *Navigation → Command-click*: Jumps to Definition; *Key Bindings*: bind *Refactor → Rename* and *Jump to Definition* if you come from VS Code. Xcode 27's coding agents live in the *Conversation* panel — connect your Claude/ChatGPT account or use Apple's models. Simulators, SwiftUI previews and Instruments are why you tolerate the 15 GB.

### AI coding agents in the terminal

The biggest workflow change of 2025–2026: agents that read your repo, plan, edit files, run tests and iterate, driven from a terminal or an editor panel. They're complementary to whatever editor you use.

| Tool | Vendor / model | Install | Notes |
|---|---|---|---|
| **Claude Code** | Anthropic | `brew install --cask claude-code` or `npm i -g @anthropic-ai/claude-code` | Usage via Claude Pro/Max subscription or API. Skills, hooks, MCP servers, `CLAUDE.md` project memory. Integrates with VS Code/Zed/JetBrains panels. |
| **Codex CLI** | OpenAI | `brew install codex` / `npm i -g @openai/codex` | Included in ChatGPT Plus/Pro; sandboxed execution. |
| **Gemini CLI** | Google | `brew install gemini-cli` | Generous free tier with a Google account. |
| **OpenCode** | open source | `brew install opencode` | Bring any model (local via Ollama, or any API key). |
| **Aider** | open source | `uv tool install aider-chat` | The original; git-native, any model. |
| **Amp** | Sourcegraph | `npm i -g @sourcegraph/amp` | Team-oriented. |
| **GitHub Copilot CLI / coding agent** | GitHub | `gh extension install github/gh-copilot` | Free for students via Copilot Student; the coding agent works on issues → PRs in the cloud. |

Practical habits: give agents a `CLAUDE.md`/`AGENTS.md` at the repo root describing the stack, commands and conventions; run them in a **git worktree** or branch so you can review diffs; keep tests fast so the agent's loop is fast; never paste secrets into a prompt; and for university coursework, **read your integrity policy** — many courses now distinguish "AI for understanding" from "AI for writing the submitted code".

**Model Context Protocol (MCP)** servers give agents tools (GitHub, Postgres, browser, filesystem). Configure them once in `~/.claude.json` / Cursor / Zed settings and every agent can use them.

### Keeping editor configs in sync

- **VS Code / Cursor**: Settings Sync (built in), or commit `settings.json`, `keybindings.json`, `snippets/`, and an `extensions.txt` to dotfiles. Cursor stores its own copies under `~/Library/Application Support/Cursor/User/`.
- **Zed**: `~/.config/zed/` is already a dotfiles-friendly directory; it also has settings sync via a Zed account.
- **JetBrains**: *Settings Sync* (account-based) or export settings to a zip; Toolbox remembers your installed IDEs.
- **Neovim/Helix**: `~/.config/nvim` and `~/.config/helix` — pure text, commit them.
- **Xcode**: themes in `~/Library/Developer/Xcode/UserData/FontAndColorThemes`, key bindings in `…/KeyBindings`, snippets in `…/CodeSnippets` — symlink these into your dotfiles.

### Fonts for code

Same as the terminal (Chapter 9) so glyphs match: **JetBrains Mono**, **Fira Code**, **Monaspace** (GitHub; five variable families that mix), **Cascadia Code**, **Iosevka**, **Geist Mono**, **Commit Mono**, **Berkeley Mono** ($75, the enthusiast favourite), Apple's **SF Mono** (in `/System/Applications/Utilities/Terminal.app/Contents/Resources/Fonts` — copy them to Font Book to use elsewhere). 13 px at 1.6 line height on a Retina display is a comfortable default; 12 px on a 5K 27".

[↑ Back to top](#table-of-contents)

---

## 13. Containers & virtual machines

Every container on a Mac runs inside a Linux virtual machine — macOS has no Linux kernel. What differs between tools is *how many* VMs, how fast the file sharing is, how much memory sits idle, and what it costs. 2026 added a genuinely new option: Apple's own `container` tool, which runs one lightweight VM per container. This chapter picks a default, explains the trade-offs, and covers full VMs for Linux and Windows.

### The landscape in September 2026

| Tool | Model | Price | Idle cost | Compose | Kubernetes | Intel Macs | Notes |
|---|---|---|---|---|---|---|---|
| **OrbStack** | One optimised shared VM; drop-in `docker` CLI; also runs Linux "machines" | Free personal; **$8/user/mo** commercial (triggered above ~$10k/yr income from work using it; 1 licence = 5 devices) | ~400 MB, <1% CPU | ✅ | ✅ built-in | ✅ (last old-Intel build v2.2.2) | **Default recommendation.** Fastest bind mounts (virtiofs, ~3–4× Docker Desktop), instant start, memory actually released when idle, `*.orb.local` DNS for every container, menu bar UI. Closed source. |
| **Docker Desktop** | One shared VM; the official product | Free for <250 employees & <$10M revenue; Pro $9 / Team $15 / Business $24 per user/mo | 1–4 GB, 2–5% CPU | ✅ | ✅ optional | ✅ | Cross-platform (Win/Linux too); the widest ecosystem (extensions, Scout, Build Cloud); heaviest. Use if your employer pays or mandates it. |
| **Apple `container`** | **One micro-VM per container** on the Containerization framework | Free, open source (Apache 2.0) | none when idle | ❌ not yet (mid-2026) | ❌ | ❌ Apple silicon only | 1.0 stable June 2026, ~49k GitHub stars. Strong isolation, higher throughput once running, slower cold start (~0.9 s vs ~0.2 s). Needs macOS 26+. Great for single services and security-sensitive work; not yet a Compose replacement. |
| **Colima** | Lima-based VM + Docker or containerd runtime | Free, open source | ~500 MB | ✅ (with `docker-compose`) | ✅ (k3s flag) | ✅ | CLI only, minimal, scriptable (`colima start --cpu 4 --memory 8`). The purist's Docker Desktop replacement. |
| **Podman + Podman Desktop** | Daemonless engine in a VM (`podman machine`) | Free, open source (Red Hat) | ~500 MB | via `podman compose` | ✅ (kind/minikube) | ✅ | Rootless, OCI-standard, Kubernetes-flavoured (pods, `podman kube play`). Choose if your team/servers are RHEL/Fedora. |
| **Rancher Desktop** | Lima VM + containerd or moby, k3s | Free, open source (SUSE) | ~1 GB | ✅ | ✅ built-in k3s | ✅ | Best free cross-platform option with Kubernetes for mixed-OS teams. |

**Recommendation**: **OrbStack** for students and solo developers (free) and for anyone whose company will pay $8/mo. Keep the `docker` CLI you already know; everything in every tutorial works unchanged. Add **Apple `container`** as a side tool to learn and for isolated single containers; watch it for Compose support. Use **Docker Desktop** when an employer supplies a licence or you need its enterprise features. Use **Colima** if you want zero GUI.

### OrbStack setup

```sh
brew install --cask orbstack
orb                      # first run creates the VM and installs docker/kubectl CLIs into /usr/local/bin & ~/.orbstack
docker run --rm -it alpine uname -m      # aarch64 — you're native
docker context ls        # "orbstack" is default
```

Settings (menu bar → Settings): **Resources**: leave memory at *dynamic* (OrbStack grows and shrinks; cap at half your RAM if you like); **Docker → Rosetta**: on (so `linux/amd64` images run at near-native speed via Rosetta *for Linux*, which is unaffected by the macOS 28 Rosetta removal); **Network**: enable *Access container domains* so every container is reachable at `http://<container>.orb.local` with automatic HTTPS; **Kubernetes**: turn on when needed (a single-node cluster in seconds, `kubectl` context `orbstack`).

Linux machines (`orb create ubuntu`, `orb create -a amd64 debian`) give you full distros with shared home directory, `ssh`, and a `mac` command to call back into macOS. This is the easiest Linux environment on a Mac for a systems course — lighter than a VM, more complete than a container.

### Docker Desktop setup (if you use it)

`brew install --cask docker-desktop`. Settings: **Resources → Memory**: 6–8 GB on a 16–24 GB Mac (containers get *this* memory, not the host's), **CPUs**: half your cores, **Swap**: 1 GB, **Disk image size**: 64 GB+; **General**: *Use Virtualization framework* (default), *VirtioFS* file sharing (default), **Use Rosetta for x86_64/amd64 emulation on Apple Silicon**: on; **Kubernetes**: off unless used; **Software updates**: on. Quit Docker Desktop when you're not developing — it holds its memory reservation.

### Apple `container` (Tahoe+)

```sh
brew install container                # or the signed .pkg from github.com/apple/container/releases
container system start                # installs a Linux kernel image on first run
container run --rm -it alpine sh
container build -t myapp .            # OCI images; Dockerfiles work
container run -d --name web -p 8080:80 nginx
container list                        # ps
container logs web
container system stop
```

Each container is its own lightweight VM booting a minimal Linux (sub-second), which gives kernel-level isolation between containers — a real advantage when you run untrusted or security-sensitive code. Images are standard OCI (pull from Docker Hub/GHCR; push too). Limits in mid-2026: no `compose`, no Kubernetes, CLI only, macOS 26+ for full networking (container-to-container IPs), Apple silicon only, and bind-mount performance is less benchmarked than OrbStack's. Apple ships releases every few weeks; check the README for what's landed.

### Multi-architecture: arm64 vs amd64

Your Mac runs **linux/arm64** containers natively. Most official images (Postgres, Redis, nginx, Node, Python, Go, Debian, Ubuntu, Alpine) are multi-arch and *just work*. When an image is amd64-only (some vendor images, older internal ones), Docker/OrbStack run it under Rosetta or QEMU — slower and occasionally buggy (segfaults in JIT-heavy runtimes, `qemu: uncaught target signal`).

- Check: `docker image inspect img --format '{{.Architecture}}'` or `docker manifest inspect img`.
- Force: `docker run --platform linux/amd64 img` for a one-off; in Compose, `platform: linux/amd64` on the service.
- **Build for production servers (usually amd64) from your Mac**: `docker buildx build --platform linux/amd64,linux/arm64 -t you/app:tag --push .` — buildx uses QEMU (installed automatically) or, better, a remote/native builder. For Go/Rust, cross-compile the binary natively and copy it into a scratch image instead of emulating the compiler.
- **Dev containers and CI parity**: if your CI is amd64 and you develop arm64, pin base images by digest and run the test suite in both; native-extension packages (Python wheels, Node `.node` files) differ per arch — never copy a `node_modules` or `.venv` into an image, install inside it.

### Docker Compose patterns for local development

A typical project's `compose.yaml` (the modern filename; `docker-compose.yml` still works):

```yaml
services:
  db:
    image: postgres:17
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: app
      POSTGRES_DB: app_dev
    ports: ["5432:5432"]
    volumes: ["pgdata:/var/lib/postgresql/data"]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app"]
      interval: 5s
  redis:
    image: redis:7-alpine
    ports: ["6379:6379"]
  app:
    build: .
    command: pnpm dev
    volumes:
      - .:/app                       # bind mount source for hot reload
      - /app/node_modules            # …but keep node_modules inside the container (arch!)
    ports: ["3000:3000"]
    environment:
      DATABASE_URL: postgres://app:app@db:5432/app_dev
    depends_on:
      db: { condition: service_healthy }
volumes:
  pgdata:
```

`docker compose up -d`, `docker compose logs -f app`, `docker compose exec app sh`, `docker compose down -v` (also deletes volumes). Use `docker compose watch` for file sync/rebuild rules. Many developers run *only the databases* in Compose and the app natively via mise — faster iteration, native debugger, no bind-mount overhead (Chapter 15).

**Dev Containers** (`.devcontainer/devcontainer.json`, VS Code / Cursor / JetBrains / GitHub Codespaces) package the whole toolchain in a container so a course or team gets an identical environment on any OS. OrbStack and Docker Desktop both work as the backend.

### Housekeeping

Images and build cache grow silently. Monthly:

```sh
docker system df                       # what's using space
docker system prune -a --volumes       # everything unused (asks first; volumes too — be sure)
docker builder prune                   # build cache only
docker image prune -a                  # dangling + unused images
```

OrbStack shows its total in the menu bar; Docker Desktop's VM disk image lives at `~/Library/Containers/com.docker.docker/Data/vms/0/data/Docker.raw` and only shrinks on prune. Exclude these VM images from Time Machine (Chapter 17).

### Kubernetes locally

- **OrbStack**: toggle Kubernetes in settings — a real single-node cluster, `kubectl config use-context orbstack`.
- **kind** (`brew install kind`): multi-node clusters in Docker; what most Kubernetes courses use.
- **minikube** (`brew install minikube`) with the `docker` or `vfkit` driver; **k3d** for k3s-in-Docker; **Rancher Desktop** for a GUI.
- Tools: `kubectl` (`brew install kubectl`), `k9s` (TUI), `helm`, `kubectx`/`kubens`, `stern` (multi-pod logs), `kustomize`, `skaffold`/`tilt` for dev loops. **Lens** or **Headlamp** for a desktop GUI.

### Full virtual machines

For a whole Linux desktop, a different kernel, Windows, or an x86 OS, you want a VM, not a container.

| Tool | Price | Guest OSes | Notes |
|---|---|---|---|
| **UTM** | Free (App Store $10 for auto-updates) | Linux arm64 (fast, Apple Virtualization), Linux/Windows x86 (slow, QEMU emulation) | Open source. The default for students. "Apple Virtualization" backend for arm64 Linux is near-native; use it for Ubuntu/Fedora/Debian arm64 desktops. |
| **Parallels Desktop** | $99–$120/yr (student discount ~50%) | Windows 11 ARM (best), Linux arm64, macOS | Most polished; Coherence mode (Windows apps as Mac windows), GPU-accelerated Windows, installs Windows 11 with one click. x86 Windows apps run via Windows' own emulation layer. |
| **VMware Fusion** | **Free** (personal and commercial since 2024) | Windows 11 ARM, Linux arm64 | Broadcom made it free; less polished than Parallels but very capable. Good Windows-for-a-course option at $0. |
| **Apple Virtualization.framework** (via `tart`, `lume`, `Virtual Buddy`, or your own Swift) | Free | macOS guests (!), Linux arm64 | **`tart`** (`brew install cirruslabs/cli/tart`) runs macOS VMs from OCI images — the way to test your dotfiles on a clean macOS or run a throwaway Tahoe. Virtual Buddy is the GUI. macOS guests can't sign into iCloud/App Store (2 VM limit). |
| **VirtualBox** | Free | arm64 builds exist but are immature | Avoid on Apple silicon. |

**Windows on Apple silicon**: Windows 11 **ARM** is the only Windows that runs; it's a full Windows with excellent x86/x64 app emulation (Prism), and Microsoft officially licenses it in Parallels/VMware. Get the ISO from Microsoft's site (Windows 11 Arm64 ISO) or let Parallels download it. Performance is very good for Office, Visual Studio, and most dev tools; games with anti-cheat and some drivers don't work. A Windows licence key is needed for activation (students often get one via Azure Dev Tools for Teaching).

**x86 Linux** (for an assembly course, a binary that only exists as x86, or matching a server exactly): UTM with QEMU emulation works but is ~5–10× slower than native. For anything sustained, use the department's servers, a cheap cloud VM, or OrbStack's `-a amd64` machines (Rosetta-accelerated user-space; the kernel is arm64, which is fine for user programs but not for kernel courses).

**Asahi Linux** (bare-metal Fedora on Apple silicon) supports M1 and M2 only — not M3/M4/M5/M6. For everyone else, Linux in a VM or OrbStack machine is the answer.

### Nix and reproducible dev shells

Worth a mention for the reproducibility-minded: the **Determinate Nix installer** (`curl … | sh -s -- install`) installs Nix cleanly on macOS with a separate APFS volume; `nix develop` / `devenv` / `flox` give per-project shells with pinned compilers and libraries — an alternative to both containers and mise for native development. Steep curve; enormous payoff if a whole team adopts it. Don't start here as a first-year.

### Choosing, by scenario

- **Web/backend student, coursework uses Docker**: OrbStack. Done.
- **Security or systems course, want strong isolation**: Apple `container` for individual services; UTM for full Linux.
- **Kubernetes course**: OrbStack Kubernetes or kind; `k9s`.
- **Need Windows for one course (Visual Studio, .NET Framework, Office macros)**: VMware Fusion (free) or Parallels (student price) with Windows 11 ARM.
- **x86 assembly or a kernel course**: UTM QEMU x86 VM (slow but correct) or the university's Linux servers over SSH.
- **Company policy says Docker Desktop**: Docker Desktop with Rosetta on and the memory cap set.
- **Want to test dotfiles on a fresh macOS**: `tart` macOS VM.

[↑ Back to top](#table-of-contents)

---

## 14. Cloud, network & DevOps tooling

The tools that connect your Mac to everything that isn't your Mac: cloud accounts, clusters, APIs, remote machines, CI. The theme is **credentials never in plaintext, one tool per job, everything in the Brewfile.**

### Cloud CLIs

```sh
brew install awscli azure-cli
brew install --cask gcloud-cli            # Google Cloud SDK (cask, not formula)
brew install doctl flyctl                 # DigitalOcean, Fly.io
brew install vercel-cli netlify-cli       # or via npm through mise
brew install cloudflare-wrangler          # Cloudflare Workers/Pages (or npm)
brew install supabase/tap/supabase        # tap trust required (Homebrew 6)
brew install stripe/stripe-cli/stripe
brew install hcloud                       # Hetzner
brew install oci-cli                      # Oracle Cloud (the free tier is real)
```

#### Credentials

- **AWS**: use **IAM Identity Center (SSO)** where your org has it (`aws configure sso`, then `aws sso login --profile work`) — short-lived tokens, nothing long-lived on disk. For personal accounts, create an IAM user with MFA and store the access key in `~/.aws/credentials` **encrypted via a credential process**: `aws-vault` (`brew install aws-vault`) keeps keys in the macOS Keychain and issues temporary STS credentials per shell (`aws-vault exec personal -- aws s3 ls`). Or **granted** (`brew install granted`) for fast profile switching with a browser-tab-per-account. Set `AWS_PROFILE` per project in `mise.toml`.
- **GCP**: `gcloud auth login` and `gcloud auth application-default login` (the latter is what SDKs use). Use *configurations* for multiple projects (`gcloud config configurations create work`).
- **Azure**: `az login` (browser); `az account set --subscription …`.
- **Never** paste long-lived cloud keys into `.zshrc`. If you must keep one, `security add-generic-password` into the Keychain and read it lazily, or store it in 1Password and use `op run` (Chapter 16).
- Install **git-secrets**/**gitleaks** hooks (Chapter 10) — cloud keys in public repos are harvested within minutes.

#### Local emulation

**LocalStack** (AWS emulator, `brew install localstack`), **Firebase Emulator Suite**, **Azurite** (Azure Storage), **MinIO** (S3-compatible object store, `brew install minio`), **Supabase local** (`supabase start` runs Postgres+Auth+Storage in Docker), **Wrangler dev** for Cloudflare. All run fine on Apple silicon under OrbStack.

### Infrastructure as code

- **Terraform** (`brew install terraform` — note: HashiCorp's BSL licence since 2023) or **OpenTofu** (`brew install opentofu`, the open-source fork, drop-in). Pin versions per project with mise (`terraform = "1.13"` / `opentofu = "1.10"`). **tflint**, **trivy** (security scanning), **terraform-docs**, **infracost**.
- **Pulumi** (`brew install pulumi`) if you'd rather write TypeScript/Python/Go.
- **Ansible** (`uv tool install ansible` — it's Python; keep it out of the system interpreter), **Packer**, **Vagrant** (with the QEMU or Parallels provider on Apple silicon — VirtualBox doesn't work well).
- **SST**, **AWS CDK** (`npm i -g aws-cdk` via mise), **Serverless Framework**, **Cloudflare Wrangler** for app-centric deploys.

### Kubernetes and containers, remotely

Chapter 13 covers local clusters. For real ones: `kubectl` + `kubectx`/`kubens` (context switching), **k9s** (the TUI you'll live in), **helm**, **kustomize**, **stern** (tail many pods), **kubecolor**, **kube-ps1** or Starship's `kubernetes` module (shows context in the prompt — critical when you have a prod context configured), **dive** (inspect image layers), **trivy** (scan images), **skopeo**/**crane** (registry ops), **argocd**/**flux** CLIs. Keep `~/.kube/config` out of dotfiles and set `KUBECONFIG` per project if you juggle clusters. Make the prod context *hard* to use by accident: a different colour in Starship, or an alias that requires `--context`.

### HTTP, APIs and debugging

- **CLI**: `curl` (Apple's is fine; `brew install curl` for HTTP/3), **xh** or **httpie** for humane syntax, **jq**/**yq**/**fx** for output, **grpcurl** for gRPC, **websocat** for WebSockets, **hey**/**oha**/**vegeta** for load testing, **mkcert** (`brew install mkcert && mkcert -install`) for locally-trusted HTTPS certificates.
- **GUI API clients**: **Bruno** (free, open source, collections stored as plain files in your repo — the 2026 default), **Postman** (the incumbent; account required, heavy), **Insomnia**, **Hoppscotch** (web), **RapidAPI/Paw** (native Mac, one-time price), **Yaak**. For GraphQL: **Altair** or the built-in playground of your server.
- **Proxies and traffic inspection**: **Proxyman** (native Mac, best UX, free tier), **Charles**, **mitmproxy** (`brew install mitmproxy`, scriptable, CLI/web UI), **HTTP Toolkit**. Each installs a root CA into your Keychain to decrypt TLS — remove it when you're done, and never trust one on a machine you don't control. **Wireshark** (`brew install --cask wireshark`) for packet-level work; install ChmodBPF when prompted so captures don't need `sudo`.
- **Tunnels to localhost** (share a dev server, receive webhooks): **ngrok** (`brew install ngrok`), **Cloudflare Tunnel** (`cloudflared tunnel --url http://localhost:3000`, free, no account for quick tunnels), **Tailscale Funnel**, **localtunnel**, **bore**. Stripe/GitHub webhook testing: `stripe listen --forward-to localhost:3000/webhook`, `gh webhook forward`.
- **DNS**: `dog` or `doggo` (modern `dig`), `dscacheutil -q host -a name example.com` (macOS's resolver), `sudo killall -HUP mDNSResponder` to flush. `/etc/hosts` for local overrides; `dnsmasq` via Homebrew for wildcard `*.test` domains.
- **Ports**: `lsof -iTCP -sTCP:LISTEN -n -P` (what's listening), `lsof -i :3000` (who has it), `kill $(lsof -t -i :3000)`. macOS reserves nothing surprising, but **AirPlay Receiver uses port 5000 and 7000** — turn it off in `System Settings → General → AirDrop & Handoff` if your Flask/AirFlow app can't bind 5000.

### Reaching your machines: Tailscale

**Tailscale** (`brew install --cask tailscale`, free for personal use up to 100 devices/3 users) builds a WireGuard mesh between your Mac, your phone, a home server, a Raspberry Pi and cloud VMs, each with a stable `100.x.y.z` IP and a MagicDNS name (`homelab.tailnet-name.ts.net`). No port forwarding, works across NATs and campus Wi‑Fi, and gives you: `ssh homelab` from anywhere; **Tailscale SSH** (auth by identity, no keys to manage); **Serve/Funnel** to expose a local dev server to your tailnet or the public internet with automatic HTTPS; **exit nodes** (route all traffic through your home connection on sketchy Wi‑Fi); **Taildrop** file sharing. Enable *Remote Login* on the Mac you want to reach (Chapter 3) and restrict `sshd` to the Tailscale interface via ACLs. Alternatives: **ZeroTier**, **NetBird**, plain **WireGuard** (`brew install wireguard-tools`), or **Cloudflare Zero Trust** tunnels.

### Remote development

- **VS Code Remote-SSH** / **Cursor** / **Zed remote** / **JetBrains Gateway**: edit on a Linux box (university server, a cloud GPU VM, your Mac mini at home) with local UI and remote compute. Combine with Tailscale for zero-config reachability and with `tmux` on the remote so long jobs outlive the connection.
- **GitHub Codespaces**, **Gitpod/Ona**, **DevPod** (open source, any backend): full dev environments in the cloud from a `devcontainer.json`. Students get 180 core-hours/month of Codespaces free with the Student Developer Pack — a legitimate way to run x86 Linux or a beefier box than a base Air.
- **mosh** for high-latency links; **eternal terminal (et)**; **Blink**/**Termius** on iPad to SSH into the Mac.

### CI/CD from the laptop

- **act** (`brew install act`) runs GitHub Actions workflows locally in Docker/OrbStack — `act -j test` before pushing saves a lot of "fix CI" commits. arm64 runners images differ slightly from GitHub's amd64 ones; use `--container-architecture linux/amd64` when parity matters.
- **gh run watch**, **gh pr checks --watch** (Chapter 10) for the real thing.
- **pre-commit** hooks (Chapter 10) and **lefthook** (`brew install lefthook`, faster, YAML) make the laptop the first CI stage.
- **Dagger** (`brew install dagger/tap/dagger`) if you want pipelines as code that run identically locally and in CI.
- **Self-hosted runners on a Mac**: GitHub Actions and GitLab both support macOS arm64 runners — useful for iOS builds; run them as a launchd service (Chapter 21) on a Mac mini.

### Databases in the cloud, from the Mac

Connection tooling is Chapter 15; here, the credential rule: use short-lived IAM/database-proxy auth where offered (RDS IAM auth, Cloud SQL Auth Proxy `brew install cloud-sql-proxy`, Supabase/Neon branch tokens), keep connection strings in 1Password or the Keychain, and never in a committed `.env`.

### Observability & profiling tools worth having

`brew install --cask stats` (menu bar CPU/GPU/mem/net — see the Apple silicon P/E core split), `btop`, `bandwhich` (per-process bandwidth), `nettop` (built in), Instruments (in Xcode: Time Profiler, Allocations, System Trace — works on any process, not just Apple apps), `sudo powermetrics --samplers cpu_power,gpu_power` (real-time watts per cluster), `sudo fs_usage -w -f filesys <pid>` and `sudo opensnoop` (file activity), `dtrace` is mostly blocked by SIP — use `eslogger`/Endpoint Security or Instruments instead.

### Recommended "cloud dev" Brewfile fragment

```ruby
tap "hashicorp/tap", trusted: true
tap "supabase/tap", trusted: true
brew "awscli"
brew "aws-vault"
brew "granted"
brew "azure-cli"
cask "gcloud-cli"
brew "opentofu"          # or "hashicorp/tap/terraform"
brew "tflint"
brew "trivy"
brew "kubectl"
brew "kubectx"
brew "k9s"
brew "helm"
brew "stern"
brew "dive"
brew "act"
brew "lefthook"
brew "mkcert"
brew "xh"
brew "grpcurl"
brew "websocat"
brew "oha"
brew "doggo"
brew "ngrok"
brew "cloudflared"
brew "supabase/tap/supabase"
brew "localstack"
cask "tailscale"
cask "bruno"
cask "proxyman"
cask "wireshark"
```

[↑ Back to top](#table-of-contents)

---

## 15. Databases & local development services

Two philosophies for local services: **install natively via Homebrew** (fastest, always on, shares your filesystem) or **run in containers** (isolated, version-per-project, throwaway). Both are fine; the mistake is mixing them for the *same* service and then wondering which Postgres is answering on 5432.

### Which approach

| | Homebrew service / Postgres.app | Containers (OrbStack/Docker Compose) |
|---|---|---|
| Speed | Native; no VM overhead; fastest for heavy queries and large imports | Very fast on OrbStack; a little file-share overhead for bind-mounted data |
| Versions | One major version per formula (`postgresql@17`); switching is fiddly | Any version per project, side by side, trivially |
| Isolation | Shared server, many databases | Each project its own server; `down -v` wipes it |
| Always-on cost | Runs at login if you `brew services start` — small battery/memory cost | Only when the project is up |
| Team parity | Differs from CI/production | Same image as CI/production |
| Recommendation | **Solo/student with one Postgres for everything; SQLite; Redis** | **Anything with a `compose.yaml`; multiple versions; team projects** |

Many developers end up with: **SQLite natively** (it's a library, not a server), **one Homebrew Postgres for scratch work**, and **Compose for real projects**.

### PostgreSQL

#### Native (Homebrew)

```sh
brew install postgresql@17
brew services start postgresql@17         # runs as your user, data in /opt/homebrew/var/postgresql@17
# keg-only: put its bin on PATH (Homebrew prints the exact line)
echo 'export PATH="/opt/homebrew/opt/postgresql@17/bin:$PATH"' >> ~/.zshrc
createdb $(whoami)                        # so plain `psql` connects
psql -c "select version();"
```

Your macOS username is a superuser with no password (local trust auth) — fine for a laptop, never for anything reachable. Create per-project roles anyway to mirror production: `createuser -P app && createdb -O app app_dev`. Config: `/opt/homebrew/var/postgresql@17/postgresql.conf`; logs: `/opt/homebrew/var/log/postgresql@17.log`. Upgrade majors with `brew postgresql-upgrade-database` (back up first).

**Postgres.app** (postgresapp.com, free) is the friendliest native option: a menu bar app that bundles several major versions with PostGIS, click to start/stop, no service management. Add `/Applications/Postgres.app/Contents/Versions/latest/bin` to PATH for `psql`. Great for students.

**Postgres client only** (talking to a container or cloud DB): `brew install libpq` (keg-only) and add its bin to PATH, or `brew link --force libpq`. **pgcli** (`uv tool install pgcli`) is a far nicer interactive client than `psql` (autocomplete, syntax highlighting).

#### In a container

The Compose snippet in Chapter 13. One-off: `docker run -d --name pg -e POSTGRES_PASSWORD=pg -p 5432:5432 -v pgdata:/var/lib/postgresql/data postgres:17`. Use a **named volume** (not a bind mount) for the data directory — bind-mounted Postgres data on macOS is slower and has had permission quirks. If you also run a Homebrew Postgres, map the container to another port (`5433:5432`) or stop the service.

#### Extensions

PostGIS, pgvector, TimescaleDB etc.: `brew install postgis pgvector` (built against the Homebrew formula), or use images that bundle them (`pgvector/pgvector:pg17`, `timescale/timescaledb`, `postgis/postgis`). Postgres.app bundles PostGIS and pgvector.

### MySQL / MariaDB

`brew install mysql` (9.x) or `mysql@8.4` (LTS), `brew services start mysql`, `mysql_secure_installation`. MariaDB is `brew install mariadb`. In containers: `mysql:8.4` / `mariadb:11` — set `MYSQL_ROOT_PASSWORD`. Client-only: `brew install mysql-client`. **mycli** for a better shell.

### SQLite

Already on macOS (`/usr/bin/sqlite3`), but Apple's build is older and lacks some extensions; `brew install sqlite` installs a current version keg-only (`$(brew --prefix sqlite)/bin/sqlite3`). **litecli** (`uv tool install litecli`) for a friendlier shell; **DB Browser for SQLite** or **TablePlus** for a GUI; **Datasette** to explore a SQLite file in the browser. **DuckDB** (`brew install duckdb`) is SQLite's analytical sibling — the fastest way to query CSV/Parquet files from the shell, and it reads Postgres/MySQL too. For 90% of coursework and side projects SQLite (or Turso/libSQL) is the right database.

### Redis, Valkey & friends

`brew install redis` (Redis 8, back under an OSI licence) or `brew install valkey` (the Linux Foundation fork); `brew services start redis`; `redis-cli ping`. Container: `redis:8-alpine` / `valkey/valkey`. **RedisInsight** or **Another Redis Desktop Manager** for a GUI. **Dragonfly** and **KeyDB** are drop-in alternatives if a project uses them.

### MongoDB

MongoDB's server isn't in Homebrew core (licence): `brew tap --trust mongodb/brew && brew install mongodb-community`, `brew services start mongodb-community`; or the `mongo:8` container — the usual choice. **MongoDB Compass** (GUI) and `mongosh` (`brew install mongosh`).

### Everything else, briefly

| Need | Native | Container image |
|---|---|---|
| Elasticsearch / OpenSearch | `brew install opensearch` | `opensearchproject/opensearch`, `elasticsearch:9` (needs `-e discovery.type=single-node`, 1–2 GB RAM) |
| Kafka | `brew install kafka` (KRaft mode, no ZooKeeper) | `apache/kafka`, or **Redpanda** (`redpandadata/redpanda`) — lighter |
| RabbitMQ | `brew install rabbitmq` | `rabbitmq:4-management` |
| NATS | `brew install nats-server` | `nats` |
| ClickHouse | `brew install clickhouse` | `clickhouse/clickhouse-server` |
| Neo4j | `brew install neo4j` | `neo4j` |
| InfluxDB / Prometheus / Grafana | brew formulae | `prom/prometheus`, `grafana/grafana` |
| MinIO (S3) | `brew install minio` | `minio/minio` |
| Mailpit (catch dev email) | `brew install mailpit` | `axllent/mailpit` — point SMTP at `localhost:1025`, read at `:8025` |
| Supabase (Postgres + auth + storage + realtime) | — | `supabase start` (uses Docker) |
| Firebase emulators | `npm i -g firebase-tools` via mise | — |
| LocalStack (AWS) | `brew install localstack` | `localstack/localstack` |

All official images above have arm64 builds. Where a vendor image is amd64-only, see the multi-arch notes in Chapter 13.

### GUI database clients

| Client | Price | Notes |
|---|---|---|
| **TablePlus** | Free (2 tabs/2 connections limit) / $89 one-time / in Setapp | Native, fast, supports Postgres/MySQL/SQLite/Redis/Mongo/MSSQL/… The Mac default. |
| **DBeaver Community** | Free, OSS | Java, heavier, supports everything incl. big-data sources; ER diagrams. |
| **DataGrip** | JetBrains; free for students | Best SQL editor/intellisense; also inside IntelliJ Ultimate/PyCharm Pro. |
| **Postico 2** | Free tier / $60 | Postgres-only, lovely. |
| **Beekeeper Studio** | Free (Community) / paid | Electron, cross-platform, pleasant. |
| **pgAdmin 4** | Free | Postgres official; web UI; admin-focused. |
| **Sequel Ace** | Free, OSS | MySQL/MariaDB only; native; the successor to Sequel Pro. |
| **Azure Data Studio** / **SSMS** | — | Deprecated (ADS, Feb 2026) / Windows only — use the **MSSQL extension for VS Code** or DBeaver for SQL Server. |
| **Compass**, **RedisInsight** | Free | Vendor GUIs for Mongo and Redis. |
| **Drizzle Studio**, **Prisma Studio** | Free | ORM-aware browsers for JS/TS projects. |

### Local HTTPS and custom domains

Browsers treat `localhost` as a secure context, so plain `http://localhost:3000` works for most features (service workers, camera, WebCrypto). You need HTTPS locally when: testing OAuth callbacks that require `https://`, Secure cookies with `SameSite=None`, HTTP/2 or HTTP/3, or multiple subdomains (`app.myproject.test`, `api.myproject.test`).

- **mkcert** (`brew install mkcert nss && mkcert -install`) creates a local CA trusted by Safari/Chrome/Firefox, then `mkcert myproject.test "*.myproject.test" localhost 127.0.0.1 ::1` gives you cert files for your dev server or reverse proxy.
- **Caddy** (`brew install caddy`) as a local reverse proxy: a 3-line `Caddyfile` (`myproject.test { reverse_proxy localhost:3000 }`) with automatic local TLS via its internal CA (`caddy trust` once). **nginx** or **Traefik** if you prefer.
- **Custom domains**: `.test` is reserved for exactly this (never `.dev` — it's a real TLD with HSTS preloaded, so `http://foo.dev` breaks). Add entries to `/etc/hosts` (`sudo nvim /etc/hosts`; `127.0.0.1 myproject.test api.myproject.test`), or run `dnsmasq` (`brew install dnsmasq`) with `address=/.test/127.0.0.1` and a resolver file in `/etc/resolver/test` for wildcard resolution. **OrbStack** gives every container `name.orb.local` with HTTPS for free, which covers the common case.
- Tools that do all of this for you: **Laravel Herd** (PHP), **Laravel Valet**, **DDEV** (Docker-based, any stack, automatic `*.ddev.site` + HTTPS), **Lando**.

### Environment variables and secrets for local services

- Each project gets a `.env` (gitignored) with `DATABASE_URL`, `REDIS_URL`, etc., loaded by `mise` (`_.file = ".env"`), `direnv`, or the framework's dotenv loader. Commit `.env.example`.
- Local passwords can be trivial (`postgres`/`postgres`) — they're bound to `localhost` — but **never reuse a real password** for a local service; it ends up in a screenshot or a repo eventually.
- Bind services to `127.0.0.1`, not `0.0.0.0`, unless you need LAN access (mobile device testing); OrbStack/Docker publish on localhost by default, Homebrew Postgres listens on localhost by default.
- Check what's listening occasionally: `lsof -iTCP -sTCP:LISTEN -n -P | grep -v 127.0.0.1` shows anything exposed to the network.

### A sane local-dev workflow

1. `mise.toml` pins runtimes and loads `.env`; `mise run dev` starts the app.
2. `compose.yaml` runs *only* stateful services (db, cache, queue, mail catcher); `docker compose up -d` once per session, `down` when done.
3. The app runs natively for hot reload and the debugger; it talks to services on `localhost:<port>`.
4. Migrations and seeds are scripts (`mise run db:reset`), so a broken database is a 10-second fix, not a support ticket.
5. A `README` "Local setup" section is three commands. If it's longer, automate the rest.

### Data and disk hygiene

- Postgres/MySQL data under `/opt/homebrew/var` is in your Time Machine backup (fine — it's usually small); Docker named volumes live inside the VM image (excluded, see Chapter 17) — **dump anything you'd miss** (`pg_dump`, `mysqldump`) before `docker system prune --volumes`.
- Large datasets for coursework (CSV dumps, ML corpora): keep them outside the repo and outside iCloud Drive (`~/Developer/data`), and consider an external SSD; Spotlight-exclude the folder (Chapter 4).
- `brew services list` — stop what you're not using this term; every running service costs memory and battery.

[↑ Back to top](#table-of-contents)

---

## 16. Security & privacy

macOS is secure by default in ways Linux and Windows are not: a sealed, signed system volume; hardware-backed encryption keys in the Secure Enclave; app sandboxing and per-resource permission prompts; notarised software. The job is to *not undo* those defaults, then add the handful of things Apple leaves to you: a password manager, backups, a firewall toggle, and habits around secrets. This chapter is written for a student or engineer, not a nation-state target; the [Lockdown Mode](#lockdown-mode-and-high-risk-users) section covers the latter.

### Threat model in one paragraph

Realistic risks for a developer's Mac, in rough order of likelihood: **losing or having the laptop stolen** (FileVault + Find My + backups make this an inconvenience instead of a disaster); **phishing and credential stuffing** on your accounts (password manager + passkeys + 2FA); **malicious packages** pulled in by `npm install`/`pip install`/`brew install` from a compromised tap (supply chain — trust decisions, lockfiles, scanning); **leaking secrets** via a committed `.env` or a screenshot; **info-stealer malware** disguised as a cracked app or a fake "update" (Gatekeeper + not pirating software); and, far down the list, targeted exploits. Configure for the top five; don't cosplay for the sixth.

### FileVault

Full-disk encryption of your Data volume, keyed to your login password and the Secure Enclave. On Apple silicon the drive is *always* encrypted at the hardware level; FileVault is what ties that key to your password so a stolen SSD (or a stolen Mac booted to Recovery) is unreadable.

- **Since Tahoe it's on by default** when you sign into an Apple Account during setup. Verify: `System Settings → Privacy & Security → FileVault` shows **On**, or `fdesetup status` in a terminal.
- **The Recovery Key changed in Tahoe**: the old "store in iCloud" escrow (protected only by your Apple Account password) is gone. The key now lives in **iCloud Keychain (end-to-end encrypted)**, shows up in the **Passwords app**, and can be displayed any time from the FileVault pane via **Show** (Touch ID). Macs upgraded to 26.4+ are migrated to this model.
- **Do this now**: click *Show*, copy the 24-character key into your password manager too, and — if you don't use iCloud Keychain — write it on paper and put it somewhere physically safe. If your login password is ever lost *and* the account can't be reset via Apple Account, the Recovery Key is the **only** way to get your data.
- Verify the stored key works without wiping anything: `sudo fdesetup validaterecovery` → paste key → `true`.
- **Allow my Apple Account to reset this password** (set during setup; changeable in `Users & Groups → ⓘ`) is your other safety net. Keep it on unless you have a specific reason.
- Time Machine and other external drives are **separate**: encrypt them at format time (APFS Encrypted) — Chapter 17. Note that **encrypted HFS+ is deprecated** and unsupported from macOS 28; reformat old backup drives as APFS.
- Sleeping vs shutting down: with FileVault, a *sleeping* Mac holds the key in memory. For maximum safety when travelling, shut down (or at least lock — the Secure Enclave rate-limits guesses). `sudo pmset -a destroyfvkeyonstandby 1 hibernatemode 25` destroys the key on standby at the cost of slower wake; most people don't need this.

### Gatekeeper, notarisation and running unsigned software

Gatekeeper checks that downloaded apps are signed by a registered developer and notarised by Apple (scanned for malware). The rules tightened in Sequoia and stay tight in Tahoe/Golden Gate:

- The right-click → *Open* bypass **no longer exists**, and `spctl --master-disable` (the old "Anywhere" option) **is gone**.
- To run an unsigned or un-notarised app: double-click it (get refused), then `System Settings → Privacy & Security` → scroll to *Security* → click **Open Anyway** (within about an hour). Once.
- From the terminal: `xattr -d com.apple.quarantine /Applications/App.app` removes the quarantine flag so Gatekeeper isn't consulted. Homebrew: `brew install --cask --no-quarantine app`.
- Binaries you compile yourself aren't quarantined and run fine. Binaries you `curl` are quarantined by Safari/Chrome but *not* by `curl` itself.
- Check a signature: `codesign -dv --verbose=4 App.app`; check Gatekeeper's verdict: `spctl -a -vv App.app`. **Notarised** + **Developer ID** = normal commercial software. Ad-hoc signed = built locally.
- **XProtect** (Apple's built-in malware scanner) and **XProtect Remediator** update silently in the background (`Software Update → Install Security Responses and system files`). There is no need for third-party antivirus on a personal Mac; if you want a second opinion, **Malwarebytes** free scans on demand, and Objective-See's free tools (**KnockKnock** — what's persistent, **BlockBlock** — alerts on new persistence, **LuLu** — outbound firewall, **OverSight** — mic/camera use) are excellent and made by a respected researcher.
- **Don't install pirated apps or "activators".** In 2025–2026 the dominant Mac malware (Atomic/AMOS, Poseidon, Cuckoo, Banshee info-stealers) arrives almost exclusively via cracked software, fake app sites in search ads, and fake "update your browser/Zoom" pages, and steals Keychain, browser cookies, crypto wallets and SSH keys. It also increasingly comes as a **terminal command** the page tells you to paste ("ClickFix"). Never paste a command from a website you don't understand into Terminal.

### Firewall and network

- `System Settings → Network → Firewall`: **On**, *Stealth mode* on. It's an application firewall (allows/denies per app) and is off by default on new Macs.
- Outbound firewall (know what phones home): **LuLu** (free) or **Little Snitch** ($59; Little Snitch Mini is free). Useful on a dev machine to notice a package or IDE plugin making unexpected connections.
- `pf` is the packet filter underneath (`/etc/pf.conf`); rarely needed on a laptop.
- **Sharing**: everything off except what you use (Chapter 3). If SSH is on, key-only auth.
- **Public Wi‑Fi**: use a VPN you control (Tailscale exit node at home, or a reputable provider — Mullvad, Proton), or iCloud Private Relay for Safari. Turn off *Auto-Join* for open networks; forget the ones you won't reuse.
- **DNS**: consider encrypted DNS via a configuration profile (Cloudflare/Quad9/NextDNS provide `.mobileconfig` files); NextDNS also blocks trackers and malware domains network-wide.
- **Local network permission** prompts (`Privacy & Security → Local Network`) exist since Sequoia — deny for apps with no business scanning your LAN.

### Passwords, passkeys and 2FA

- **Pick one password manager and set it up before creating accounts**: Apple **Passwords** (free, built in, syncs via iCloud Keychain, passkeys, verification codes, shared groups, Windows/Chrome extension; Golden Gate adds automatic password changing for compromised logins), **1Password** ($3/mo; students 50% off; best for developers: SSH agent, CLI `op`, Git signing, Secrets Automation), **Bitwarden** (free tier is genuinely complete; open source; self-hostable via Vaultwarden), **Proton Pass**. Turn off the browser's built-in saving so you don't get duplicates. The Passwords app is the right default for a student fully in Apple's ecosystem; 1Password if you're a developer who wants the CLI/SSH integration.
- **Passkeys** replace passwords with a device-bound cryptographic credential that can't be phished. Enable them on every account that supports them — Apple Account, Google, GitHub, Microsoft, Amazon, PayPal, most banks, Cloudflare, Vercel — and keep passwords only as fallback. They sync via iCloud Keychain or your manager.
- **2FA**: TOTP codes in the Passwords app or 1Password (both fill them). **Hardware keys** (YubiKey 5C NFC, ~$55; get two) for GitHub, Google, Apple Account (Security Keys for Apple Account), your password manager, and cloud consoles — the strongest protection you can buy for the accounts that unlock everything else. Avoid SMS 2FA when anything else is available.
- **Apple Account**: 2FA on (mandatory), a **recovery contact** and a **recovery key** set (`Sign-In & Security → Account Recovery`), **Advanced Data Protection on**, and review *Devices* twice a year — remove Macs you sold.
- **Stolen Device Protection** (`Touch ID & Password`, MacBooks on 26.4+): requires biometrics — not the password — for sensitive changes when the Mac is away from familiar locations, with a security delay. Turn it on.

### Secrets on disk (the developer part)

Where things live and how to keep them from leaking:

| Secret | Where it should be | Where it should *not* be |
|---|---|---|
| SSH private keys | `~/.ssh/` with a passphrase in the Keychain (`UseKeychain`), or a hardware key, or 1Password's agent | Copied between machines; in Dropbox/iCloud Drive; in a repo |
| Git signing key | Same SSH key (Chapter 10) | A GPG keyring you'll lose the passphrase to |
| API tokens, cloud keys | 1Password (`op run`, `op read`), macOS Keychain (`security add-generic-password`), `aws-vault`, `mise`/`direnv` loading a **gitignored** `.env` | `~/.zshrc`, `~/.npmrc`, `~/.netrc`, committed `.env`, a Slack message |
| Database passwords (prod) | Your cloud's secret manager / 1Password | Local `.env`, a GUI client's saved connection without Keychain |
| Browser cookies/sessions | The browser (they're the #1 target of info-stealers) | Exported HAR files in Downloads |
| Backups of any of the above | Encrypted Time Machine / encrypted disk image | Unencrypted USB sticks |

Tools: `gitleaks` pre-commit hook (Chapter 10); `op` CLI with biometric unlock; **sops**/**age** (`brew install sops age`) for encrypted config files in repos; the Keychain from scripts:

```sh
security add-generic-password -a "$USER" -s openai_api_key -w      # prompts for the value
export OPENAI_API_KEY="$(security find-generic-password -a "$USER" -s openai_api_key -w)"
```

`~/Library/Keychains/login.keychain-db` is encrypted with your login password and included in FileVault and Time Machine — fine. iCloud Keychain syncs it end-to-end encrypted.

### Permissions (TCC) hygiene

Every "X would like to access Y" dialog writes to the TCC database. Review quarterly in `Privacy & Security`:

- **Full Disk Access**: terminals, backup tools, maybe your editor. Anything else — why?
- **Accessibility**: window managers, Karabiner, Raycast/Alfred, text expanders, AltTab. This permission is powerful (it can read and synthesise all input); grant it only to well-known apps.
- **Screen & System Audio Recording**: screenshot tools, video calls, DisplayLink. macOS periodically re-asks for less-used apps.
- **Input Monitoring**: Karabiner, keyboard utilities.
- **Automation** (AppleScript control between apps), **Camera/Microphone**, **Files and Folders**, **Local Network**, **Developer Tools**.
- `tccutil reset All com.example.app` clears an app's grants if a dialog got stuck.
- macOS 26.2+ shows which permissions were granted by an MDM profile (relevant on work Macs); macOS 27 denies apps access to other teams' app containers by default.

### Browser privacy

- **Safari** has the strongest default anti-tracking (ITP, fingerprinting protection strengthened in 26.4, Private Relay, Hide My Email) and the best battery life. Enable *Advanced Tracking and Fingerprinting Protection: in all browsing*, *Prevent cross-site tracking*, *Hide IP address from trackers*. Extensions from the App Store only: **AdGuard** or **Wipr 2** (content blockers), your password manager, **Kagi**. Golden Gate's Safari adds AI tab grouping and page-change alerts; the *Create an Extension* AI feature is fun for small tweaks.
- **Chrome** if you need it (DevTools, Google Workspace, Chrome-only sites): sign out of sync unless you want Google to have your history, turn off *Privacy Sandbox* ad topics, install **uBlock Origin Lite** (MV3) — uBlock Origin proper is Firefox-only now. **Brave** is Chromium with a built-in blocker and no Google account hooks. **Firefox** for uBlock Origin and container tabs; **Zen** is Firefox with Arc's vertical-tab workflow (Arc itself is frozen since 2025 — security patches only). **Orion** (Kagi) is a WebKit browser that runs Chrome *and* Firefox extensions.
- **Two browsers, two identities**: personal in Safari, work/Google in Chrome or a dedicated profile. Browser profiles keep cookies, extensions and history separate — and limit what a malicious extension in one can see.
- **Extensions are the biggest browser risk**: each one you install can read every page. Keep them to a handful from reputable authors.

### Updates

`Software Update`: everything automatic, including **Security Responses and system files** and **Background Security Improvements**. Rapid Security Responses ship within days of an exploited zero-day. App updates: Homebrew (`brew upgrade`) weekly, App Store automatic, and let apps that self-update (browsers, editors, Slack) do so. An out-of-date browser is the most likely way in.

### Lockdown Mode and high-risk users

`Privacy & Security → Lockdown Mode` disables JIT and many web technologies in Safari, blocks most message attachments and link previews, refuses wired accessories while locked, and prevents configuration-profile installs. It's for journalists, activists, dissidents, executives, and security researchers who have reason to believe a well-resourced adversary is targeting them personally. It breaks enough normal developer web tooling that it's the wrong default for everyone else. If that's you: enable it, use a hardware security key on your Apple Account, consider a separate device for sensitive work, and read Apple's Platform Security Guide and the ERNW macOS 26 hardening guide (Appendix E) — they cover MDM-level restrictions this guide skips.

### The admin vs standard account question

Running day-to-day as a **standard user** and keeping a separate admin account means anything that runs as you cannot silently install system-wide persistence or change security settings without an admin password prompt. It's the single most effective *free* hardening step and what enterprise baselines require. The friction on a personal Mac is small — occasional extra prompts for installers, `sudo` requires the admin's credentials — and Homebrew works fine once `/opt/homebrew` is owned by your standard account. Reasonable people skip it on a personal laptop; do it on a machine that has access to production systems.

### When the Mac is lost or stolen

Before it happens: FileVault on, Find My on, Stolen Device Protection on, a lock-screen message with contact details, backups current, and your Apple Account recovery set up.

When it happens: **icloud.com/find** (or Find My on another device) → the Mac → **Mark As Lost** (locks it and shows your message; Activation Lock means it can't be erased and reused) → if it's clearly gone, **Erase This Mac**. Then: change your Apple Account password, revoke the machine's SSH keys on GitHub/servers, rotate any tokens that lived in plaintext on disk (there should be none — see above), sign out sessions in Google/GitHub/Slack (each has a "sign out everywhere"), and notify your employer's IT if it had work data. Your data is unreadable without your password; your Time Machine backup restores everything onto the replacement.

### Quick audit script

Paste into a terminal for a snapshot of the security posture (read-only):

```sh
echo "FileVault:      $(fdesetup status)"
echo "Firewall:       $(/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate)"
echo "Stealth:        $(/usr/libexec/ApplicationFirewall/socketfilterfw --getstealthmode)"
echo "Gatekeeper:     $(spctl --status)"
echo "SIP:            $(csrutil status)"
echo "Auto login:     $(defaults read /Library/Preferences/com.apple.loginwindow autoLoginUser 2>/dev/null || echo off)"
echo "Remote login:   $(systemsetup -getremotelogin 2>/dev/null)"
echo "Auto updates:   $(defaults read /Library/Preferences/com.apple.SoftwareUpdate AutomaticallyInstallMacOSUpdates 2>/dev/null) (1=on)"
echo "Listening TCP:"; lsof -iTCP -sTCP:LISTEN -n -P | awk 'NR>1{print "   "$1, $9}' | sort -u
echo "Login items:"; osascript -e 'tell application "System Events" to get the name of every login item' 2>/dev/null
echo "LaunchAgents:"; ls ~/Library/LaunchAgents /Library/LaunchAgents 2>/dev/null
```

Expected on a well-set-up Mac: FileVault On, Firewall enabled, stealth on, assessments enabled, SIP enabled, no autologin, remote login off (unless you need it), only local (`127.0.0.1`) listeners, and login items you recognise.

[↑ Back to top](#table-of-contents)

---

## 17. Backup & recovery

A developer's Mac holds three kinds of data: **code** (should already be on a Git remote), **documents and media** (irreplaceable), and **configuration** (your dotfiles repo). The goal is to make losing the laptop — to theft, a spilled coffee, a failed SSD, a bad `rm -rf`, or ransomware — cost you an afternoon instead of a semester. The industry rule is **3-2-1**: three copies, on two different media, one off-site. On a Mac that's cheap and mostly automatic.

### The plan

| Copy | Tool | Cost | Protects against |
|---|---|---|---|
| 1. The Mac itself | — | — | — |
| 2. **Local, versioned** | **Time Machine** to an encrypted external SSD (or a NAS) | $100–$180 once | Deleted/overwritten files, bad updates, dead SSD, "I need the version from Tuesday" |
| 3. **Off-site, continuous** | **Backblaze** (or iCloud Drive for documents + Git for code) | $9/mo, or $0 with iCloud+Git | Theft, fire, both copies in the same bag |
| Bonus | **Git remotes** for code, **dotfiles repo** for config, **password manager** for secrets | free | The stuff Time Machine restores slowest |

Time Machine + Backblaze is the standard answer and costs about the same as one coffee a month. Students on a budget: Time Machine + iCloud Drive (200 GB for $2.99) for documents + GitHub for code covers the important 95%.

### Time Machine, done right

#### The drive

- **Size**: at least equal to your Mac's internal storage; 2× is comfortable (Time Machine keeps hourly/daily/weekly versions until the drive fills, then prunes oldest). A **2 TB USB‑C/USB4 SSD** (Samsung T7/T9, SanDisk Extreme, Crucial X9/X10, or an NVMe stick in an enclosure) is the sweet spot at $130–$180; spinning disks work but are slow and fragile.
- **Format**: Time Machine wants **APFS** (Case-sensitive is fine; encrypted is what you want). Erase in Disk Utility: *View → Show All Devices*, select the **device** (not the volume), *Erase*, Scheme **GUID Partition Map**, Format **APFS (Encrypted)**, choose a strong passphrase and **save it in your password manager** — an encrypted backup you can't unlock is a paperweight.
- Since Tahoe 26.6, **encrypted HFS+ (CoreStorage) is deprecated and will not be supported in macOS 28**. If your old Time Machine drive is HFS+, back up elsewhere, erase it as APFS Encrypted, and start fresh.

#### Setup

`System Settings → General → Time Machine → Add Backup Disk…`, pick the drive, **Encrypt Backup** on if you didn't format it encrypted. Then **Options…**:

- **Back up frequency**: *Automatically every hour* (default). Time Machine also keeps **local snapshots** on your internal disk when the drive isn't connected, so laptop users still get hourly point-in-time recovery (`tmutil listlocalsnapshots /`).
- **Exclude** (click **+**): things that are large, regenerable, or already backed up elsewhere:

```
~/Library/Developer                # Xcode DerivedData, simulators (tens of GB, regenerable)
~/Library/Caches
~/Library/Containers/com.docker.docker   # Docker Desktop VM disk
~/.orbstack                        # OrbStack VM data (or ~/OrbStack)
~/.cache
~/.local/share/mise                # runtimes: reinstall with `mise install`
~/.npm  ~/.pnpm-store  ~/.cargo/registry  ~/go/pkg  ~/.gradle  ~/.m2  ~/.cache/uv
~/Library/Application Support/Google/Chrome/Default/Service Worker
~/Library/Application Support/Code/CachedData   (and Cursor, JetBrains caches)
~/VirtualMachines  ~/Library/Containers/com.utmapp.UTM   # VM images — back up separately if you care
~/Downloads                        # opinion: yes, exclude; nothing that matters should live there
node_modules directories           # can't be excluded by pattern in the UI; use tmutil (below) or keep code in Git
```

From the shell, `tmutil addexclusion -p /path` excludes a path permanently (the `-p` flag makes it a *fixed-path* exclusion rather than one that follows the file). For `node_modules`/`.venv`/`target` everywhere: a script that walks `~/Developer` and calls `tmutil addexclusion` (without `-p`, so it sticks to the directory) on each — or accept the bloat; APFS-to-APFS backups are fast.

- **Back up while on battery power**: on for laptops.
- **Show Time Machine in menu bar** (Control Center → Time Machine): yes — you can trigger *Back Up Now* and see status.

#### Using it

- **Restore a file**: open the folder in Finder, then Time Machine menu → *Browse Time Machine Backups*; step back in time, *Restore*. Works inside Mail, Notes and other apps that support it too.
- **Restore everything**: Migration Assistant on a new/wiped Mac (choose the Time Machine disk) — this is how a lost laptop becomes a Tuesday afternoon.
- **Restore macOS + everything**: Recovery → *Restore from Time Machine*.
- `tmutil listbackups`, `tmutil latestbackup`, `tmutil compare` (what changed), `tmutil thinlocalsnapshots / 50000000000 4` (free 50 GB of local snapshots if "System Data" is huge), `tmutil startbackup --block`.
- **NAS / network**: Time Machine over SMB to a Synology/QNAP/TrueNAS/another Mac works well (Golden Gate improved SMB browsing speed). Set a quota on the share so it can't eat the NAS. Wireless backups are slow for the first run — do it over Ethernet.
- **Multiple drives**: Time Machine rotates between them (one at home, one at the office/parents' house = an off-site copy for free).

#### Time Machine's limits

It's not bootable (no bootable backups on Apple silicon — see below), it doesn't back up the VM images you excluded, it can't do bare-metal restore faster than Migration Assistant, and its consistency for open databases (Postgres data dir, VM disks) is file-level, not snapshot-consistent — dump databases separately if they matter.

### A second local copy: clones

**Carbon Copy Cloner** ($50) or **SuperDuper!** ($28) make a complete, browsable copy of your Data volume to another drive on a schedule, with snapshots and a "SafetyNet" for changed files. Since Big Sur, **bootable clones are effectively dead on Apple silicon** — the sealed system volume can only be laid down by Apple's installer; CCC can still attempt it but the developer explicitly recommends a *standard* (data-only) backup plus reinstalling macOS from Recovery, which takes 15 minutes. Do you need CCC if you have Time Machine? Only if you want a second, independent, faster-to-browse local copy, or a scheduled sync of specific folders (e.g. your photo library to a NAS). Nice to have, not required.

For raw folder syncs, `rsync -avh --delete --progress ~/Documents/ /Volumes/Backup/Documents/` (install Homebrew's `rsync`) in a `launchd` job (Chapter 21) is free and dependable.

### Off-site: cloud backup

- **Backblaze Personal Backup** ($9/mo or $99/yr, unlimited, per computer): installs a small agent, backs up *everything* on the internal drive and attached externals (you exclude what you don't want), versions for 30 days (1 year for $2/mo more), restores via web download or a mailed USB drive. Exclude the same caches/VMs as Time Machine. It's the set-and-forget answer for photos, documents, and everything you'd cry over. Set a **private encryption key** (Backblaze can't decrypt; if you lose it, so is your backup).
- **Arq** ($50 one-time + your own storage: Backblaze B2, S3, Google Drive, OneDrive, SFTP, another Mac): client-side encrypted, hourly, versioned, very configurable. The power user's choice; B2 costs ~$6/TB/month.
- **restic** / **Kopia** (free, open source, CLI or Kopia's GUI): encrypted, deduplicated, to any cloud or an SFTP server. Great if you already have a homelab or an S3 bucket and enjoy `launchd` plists.
- **iCloud Drive** with *Desktop & Documents* sync is **sync, not backup**: deleting a file deletes it everywhere (recoverable for 30 days in *Recently Deleted*), and ransomware or a bug syncs too. It's still far better than nothing for documents and pairs well with iCloud+ 200 GB/2 TB plans and Advanced Data Protection. **Do not put code repos in iCloud Drive** (Chapter 2).
- **Photos**: iCloud Photos is the natural place; keep *Download Originals to this Mac* on so the library exists locally and gets Time Machined/Backblazed too — otherwise your only copy is Apple's.

### What about code and config?

- **Code**: every repo has a remote; `git status` clean at the end of the day; unpushed branches are the only exposure. `gh repo list --limit 200` shows what's on GitHub; a monthly `for d in ~/Developer/*/; do (cd "$d" && git status -sb | head -1); done` surfaces repos with no remote or unpushed work.
- **Configuration**: the dotfiles repo (Chapter 10) plus the Brewfile. A fresh Mac becomes yours in 20 minutes — that's your real disaster-recovery plan for the *environment*.
- **Secrets**: the password manager (synced, encrypted) holds the FileVault key, backup drive passphrase, 2FA recovery codes, SSH key passphrases and cloud credentials. **Print the emergency kit / recovery codes** and put them with your passport.
- **Databases**: `pg_dump`/`mysqldump` into a folder Time Machine sees, or accept that local dev data is disposable (it usually is).

### Test the restore

A backup you've never restored from is a hypothesis. Twice a year:

1. Pick a file you edited last week; restore Tuesday's version via Time Machine. Did it work? Was the drive's passphrase where you thought?
2. Log into Backblaze/Arq and download one folder.
3. Boot to Recovery once so you know what it looks like (hold the power button → Options).
4. Optional but recommended once: restore your whole Time Machine backup into a `tart`/UTM macOS VM, or onto a spare Mac, to see that Migration Assistant actually brings back what you expect.

### Recovery: when the Mac won't boot or you need to reinstall

Apple silicon boot options — **shut down, then press and hold the power button** until "Loading startup options":

- **Options → Recovery**: *Restore from Time Machine*, *Reinstall macOS* (keeps your data; fixes a corrupted system), *Safari* (read this guide), *Disk Utility* (First Aid, erase), *Utilities → Terminal*, *Startup Security Utility* (security policy — needed for kexts/yabai), *Share Disk* (mount your Mac's drive on another Mac over USB-C to pull files off — the modern Target Disk Mode).
- **Safe Mode**: hold <kbd>⇧</kbd> while selecting your startup disk in the options screen → *Continue in Safe Mode*. Loads no third-party kexts/login items; clears caches. First thing to try for boot loops or kernel panics after installing something.
- **Fallback recoveryOS**: if Recovery itself is damaged, double-press-and-hold the power button.
- **DFU restore / revive** (bricked Mac, failed firmware update): connect to another Mac with a USB-C cable, use **Finder** (Sequoia+) or **Apple Configurator** → *Revive* (keeps data) or *Restore* (wipes). The IPSW downloads automatically. This is the nuclear option that fixes almost anything short of hardware failure.
- **Erase All Content and Settings** (from a working macOS: `System Settings → General → Transfer or Reset`) is the fast clean-slate: 5 minutes, keeps macOS installed, removes your data and Activation Lock. Then Migration Assistant from Time Machine.

Things that look like disasters but aren't: a **"System Data" category eating 100+ GB** is usually Time Machine local snapshots (`tmutil thinlocalsnapshots`), Xcode caches, or container VM images; a **forgotten login password** is fixed with your Apple Account or the FileVault Recovery Key at the login screen (click *?* or wait for the *Reset* option after three tries); a **spinning wheel at boot after an update** often just needs 20 minutes.

### The minimum viable backup (if you do nothing else)

1. Buy a 2 TB SSD, format APFS Encrypted, plug it in, click *Use as Backup Disk*, save the passphrase in your password manager. Leave it plugged in whenever you're at your desk.
2. Turn on iCloud Photos with originals downloaded, and iCloud Drive for Documents.
3. Push your code. Every day.
4. Put the FileVault Recovery Key and the drive passphrase in the password manager, and print the password manager's emergency kit.

That's an hour of work and it makes a dead laptop a shopping trip, not a tragedy.

[↑ Back to top](#table-of-contents)

---

## 18. Performance & maintenance

Apple-silicon Macs don't slow down the way Intel machines did — there's no spinning disk to fragment, no registry to rot, and macOS manages memory aggressively. What *does* go wrong is predictable: the disk fills up with build artifacts and container images, something you installed once runs at login forever, a runaway process eats a core in the background, and the battery gets cooked by living at 100% on a desk. This chapter covers how to *read* what the machine is doing, then how to fix the handful of things that actually matter.

> [!TIP]
> **The 80/20 of Mac maintenance:** (1) keep ≥15% of the disk free, (2) audit login items twice a year, (3) turn on the charge limit if the Mac lives plugged in, (4) reboot when the uptime passes a couple of weeks. Everything else in this chapter is diagnosis for when something feels wrong.

### Reading Activity Monitor correctly

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

#### Memory pressure, unified memory, and "do I need more RAM?"

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

### Storage: where the space went

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

#### The usual suspects on a developer Mac

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

#### Purgeable space and why `df` disagrees with Finder

Finder shows *available* space including **purgeable** items — local snapshots, iCloud-evicted files, caches macOS knows it can drop. `df -h` shows what's actually free right now. When you're installing something big and get "not enough space" despite Finder saying otherwise, the OS hasn't purged yet. Force it by trying the copy anyway (macOS purges on demand), or delete snapshots as above.

Check the state of your APFS container:

```sh
diskutil apfs list | grep -E "Capacity (In Use|Not Allocated)|Name"
```

#### Keep 15% free

APFS and SSD wear-leveling both want headroom. Below ~10% free, writes slow down, Time Machine local snapshots get purged constantly, and Xcode/Docker start failing in confusing ways. If you're routinely below that, the fix is an external SSD for media and project archives (see [chapter 17](17-backup-and-recovery.html)) or an honest look at whether you need three container runtimes.

### Login items and background processes

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

### Uninstalling properly

Dragging an app to the Trash leaves preferences, caches, launch agents, and sometimes a privileged helper behind. For most apps the leftovers are a few KB of plists and harmless. For anything that installed a kernel/system extension, a VPN, an agent, or a helper (Docker Desktop, antivirus, Adobe, Logitech/Razer software, old Zoom versions), use the vendor's uninstaller or a cleaner:

- `brew uninstall --zap <cask>` — Homebrew's zap stanza deletes the app *and* its known support files. This is the strongest argument for installing GUI apps via casks.
- **AppCleaner** (free) or **Pearcleaner** (free, open source) — drop an app in, see the associated files, delete them together.
- Check **System Settings → General → Login Items & Extensions → Extensions** and **Privacy & Security** for orphaned system extensions; `systemextensionsctl list` in the terminal.

### Battery health

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

### Thermals and fan noise

Apple-silicon Macs throttle gracefully: when they get hot, `kernel_task` appears to use a lot of CPU — that's the scheduler stealing cycles to cool down, not a bug. MacBook Air has no fan and will throttle under sustained load (long compiles, ML training); that's the trade-off you accepted for silence.

To reduce heat:

- Keep the intake vents (hinge area on MacBooks) unobstructed. A stand helps more than any software.
- Sustained 100% CPU from something that *shouldn't* be busy (Spotlight after a migration, a cloud sync client, a runaway Electron app) is the usual cause of a hot idle Mac — Activity Monitor → CPU.
- **Stats** or **iStat Menus** ($) in the menu bar show temperature and fan speed. `sudo powermetrics --samplers smc -i 1000 -n 1` prints die temperatures and fan RPM from the terminal.
- Don't install fan-control software unless you know why. Macs Fan Control can force fans on early, which is fine, but the defaults are already tuned.

### Spotlight and indexing

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

### Updates

- **macOS updates**: System Settings → General → Software Update. Turn on **Install Security Responses and system files** (background security patches). For feature updates, waiting a week or two after release is reasonable on a machine you depend on; security updates (26.6 fixed 155 CVEs) should not wait. See the [security chapter](16-security-and-privacy.html).
- **App Store apps**: automatic updates on.
- **Homebrew**: `brew update && brew upgrade && brew cleanup` weekly, or `brew upgrade --greedy` to include casks with their own auto-updaters. Pin anything you can't afford to have change: `brew pin postgresql@18`.
- **Casks with auto-updaters** (Chrome, VS Code, Slack, Zoom) update themselves; `brew upgrade` skips them unless `--greedy`.
- **Runtimes**: `mise upgrade` for tool versions, `mise self-update` for mise itself (or via brew).
- **Global npm/pip/cargo installs**: the fewer the better. `npm outdated -g`, `uv tool upgrade --all`, `cargo install-update -a` (via `cargo-update`).

Reboot after macOS updates, obviously, but also reboot every couple of weeks regardless. `uptime` shows how long it's been; leaked memory in WindowServer and a dozen helper processes recovers nothing else.

### A maintenance routine that fits in five minutes

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

### When it's actually slow: a diagnostic order

1. `uptime` — over two weeks? Reboot first, then re-evaluate.
2. `df -h /` — under 10% free? Fix that.
3. Activity Monitor → **CPU**, sort by % CPU. Anything sustained above 100% that isn't yours? Sample it, quit it, find why it's running (login items).
4. Activity Monitor → **Memory**, look at pressure. Red? Quit Docker/IDE/browser you aren't using; consider whether you bought enough RAM.
5. Activity Monitor → **Disk**, sort by Bytes Written. Spotlight or a sync client thrashing?
6. `pmset -g thermlog` (or `sudo powermetrics`) — throttled from heat? Clear the vents, close the tab with the WebGL demo.
7. Boot into **Safe Mode** (hold power → Options → hold ⇧ while choosing the volume) — if it's fast there, a third-party login item or extension is the cause. Binary-search the Login Items list.
8. Still slow? [Chapter 22](22-troubleshooting.html) covers logs, Recovery, and when to reinstall.

[↑ Back to top](#table-of-contents)

---

## 19. Daily-driver apps

A developer setup guide that stops at the terminal misses half the day. You'll spend as many hours in a browser, a notes app, a calendar, and Slack as in an editor, and the small utilities — a clipboard manager, a launcher, a window manager — are what make macOS feel *finished*. This chapter is the opinionated app list. Every item is available as a Homebrew cask (or App Store via `mas`) so the whole list installs from the [Brewfile](appendix-b-brewfile.html); the "Install" column gives the cask name.

The bias throughout: **free and open source first**, paid where it's genuinely better, and nothing that needs a subscription to do a job a one-time purchase did in 2019. Prices are current as of September 2026 and will drift.

> [!TIP]
> Don't install all of this on day one. Install the **Tier 1** items (bold in each section), live with the Mac for a week, and add things when you notice a specific friction. A Mac with 15 well-chosen apps beats one with 60 half-configured ones — see [chapter 18](18-performance-and-maintenance.html) on login items.

### Browsers

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

### Password manager

Non-negotiable. See [chapter 16](16-security-and-privacy.html) for the reasoning; here's the choice:

| Option | Cost | Notes |
|---|---|---|
| **Apple Passwords** | Free | The built-in app (since macOS 15) with passkeys, TOTP codes, shared groups, Wi-Fi passwords, and a Windows/Chrome extension. Enough for most people who live in Apple's ecosystem. Now also stores your FileVault recovery key. |
| **Bitwarden** | Free / $10 yr | Open source, cross-platform, self-hostable (Vaultwarden). Free tier has everything one person needs; Premium adds TOTP and file attachments. The default recommendation if you use Android/Windows/Linux too. |
| **1Password** | $36 yr / $60 family | The most polished UI, best browser integration, SSH agent, developer CLI (`op`) for secrets in scripts and env vars. Worth it if your team uses it or you want the SSH/CLI features. Free for GitHub Student Developer Pack holders (one year). |
| **KeePassXC** | Free | Local-only database file; sync it yourself. For people who don't want a cloud in the loop. |

Install: `bitwarden`, `1password` + `1password-cli`, `keepassxc`. Whatever you pick, turn off Safari/Chrome's own password saving so you don't end up with three overlapping vaults.

### Launcher

Spotlight in macOS 26 is good — app launching, calculator, clipboard history (8 hours), file search, Shortcuts actions, Siri/AI answers, and `⌘1`–`⌘4` filtered views (see [chapter 4](04-finder-dock-spotlight.html)). Try living with it for a week before installing a replacement.

If you want more:

| Launcher | Cost | Why |
|---|---|---|
| **Raycast** | Free core; Pro $8 mo for AI/cloud sync | The current default among developers. Extension store (GitHub, Jira, Linear, Homebrew, color pickers, snippets, window management), scriptable in TypeScript, unlimited clipboard history, floating notes, quick AI chat. The free tier is genuinely complete. |
| **Alfred** | Free; Powerpack £34 one-time | The veteran. Workflows are extremely capable; one-time purchase; lighter than Raycast. If you dislike subscriptions and Electron-adjacent UIs, Alfred. |
| **LaunchBar** | $29 | Mature, fast, keyboard-centric; smaller community. |

Bind the launcher to `⌘Space` and move Spotlight to `⌥Space` (or vice versa) in **System Settings → Keyboard → Keyboard Shortcuts → Spotlight**. Install: `raycast`, `alfred`, `launchbar`.

### Clipboard manager

The single highest-value utility most people don't know they need. Copy several things, paste any of them later, with search.

- **Spotlight's built-in history** (macOS 26): `⌘Space` then `⌘4`. Eight hours only, no pinning. Fine to start.
- **Raycast Clipboard History** — if you already run Raycast, it's there (`⌥⌘C` by default, configurable), searchable, with images and pinning.
- **Maccy** (free, open source) — a menu bar clipboard history with fuzzy search. The lightweight standalone pick. `maccy`
- **Paste** ($15 yr) — the pretty one, with iCloud sync to iPhone and pinboards. Subscription.
- **CopyQ** (free) — cross-platform, scriptable, uglier. For people who also use Linux.

Whatever you use, exclude your password manager from history (all of the above support ignoring apps — set it).

### Window management

Covered in depth in [chapter 6](06-window-management.html). Summary for the app list: macOS 26 tiling (drag to edge, `fn+ctrl` shortcuts) handles the basics; **Rectangle** (free) for keyboard-driven halves/thirds; **AeroSpace** (free) for i3-style tiling; **Raycast** has window commands built in. Install: `rectangle`, `aerospace`.

### Notes and knowledge

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

### Tasks, calendar, and time

- **Reminders + Calendar** (built-in) are more than enough for most students. Reminders has smart lists, tags, subtasks, and natural language ("Submit lab Friday 5pm"). Calendar supports Google/Outlook/CalDAV accounts and shows in the menu bar via **Itsycal** (free) or **Dato**.
- **Things 3** ($50 one-time for Mac, separate iPhone/iPad) — the most pleasant task manager on the platform; no subscription. **Todoist** (free / $4 mo) for cross-platform and natural-language entry. **OmniFocus** if you're deep into GTD.
- **Fantastical** ($57 yr) is the calendar power tool (natural-language entry, multiple calendar sets, Zoom integration); the free tier is fine as a menu bar calendar. **BusyCal** ($50 one-time) is the no-subscription alternative.
- **Toggl Track** (free) or **Timing** ($) if you bill hours or want to know where the day went.
- **Itsycal** (`itsycal`, free) — a tiny menu bar calendar. Nearly everyone should install this.

### Email

- **Apple Mail** — free, private, handles Gmail/Exchange/IMAP, Hide My Email, mail categorization since macOS 15. Rules and smart mailboxes are underused. The right default for most people.
- **Thunderbird** — free, open source, cross-platform, extension ecosystem, good for multiple accounts and heavy filtering.
- **Mimestream** ($50 yr) — native Gmail client that speaks the Gmail API (labels, categories, snooze) properly. If you live in Gmail and dislike the web UI, this is the one.
- **Spark**, **Superhuman** ($30 mo) — AI-assisted triage; Superhuman is very fast and very expensive.
- **Proton Mail / Fastmail apps** if that's your provider.

Set your default mail client in **Mail → Settings → General** (yes, the setting lives inside Mail.app even for choosing another app).

### Communication

Almost all of these are Electron apps that want to run at login and eat 400 MB each. Install the ones you actually need and set them to *not* open at login; open them when you sit down to work.

`slack`, `discord`, `zoom`, `microsoft-teams`, `signal`, `telegram`, `whatsapp`. **Messages** and **FaceTime** are built in and, in 2026, do RCS with Android users. For Slack and Discord specifically, the browser version is usually fine and saves memory.

### Files, cloud, and sync

- **iCloud Drive** — already there; Desktop & Documents sync is convenient and dangerous (see [chapter 2](02-first-boot-and-migration.html)). Good for documents; keep code out of it (Git repos + iCloud eviction = corruption risk).
- **Google Drive**, **Dropbox**, **OneDrive** — all use the File Provider API now, so they behave like iCloud (files on demand, no kernel extension). Install the one your school/work uses. Storage tiers are cheaper via a Google One / Microsoft 365 student plan.
- **Syncthing** (free, open source, `syncthing`) — peer-to-peer folder sync without a cloud. Excellent for syncing an Obsidian vault or a projects folder between a laptop and a desktop.
- **Maestral** (free, `maestral`) — open-source Dropbox client that's lighter than the official one.
- **Transmit** ($45) or **Cyberduck** (free) for SFTP/S3 with a GUI; **Mountain Duck** to mount remote storage as a disk. For most engineers, `rsync`/`scp`/`rclone` in the terminal is enough.

Finder quality-of-life (see [chapter 4](04-finder-dock-spotlight.html) for settings): **QuickLook plugins** — `qlmarkdown`, `syntax-highlight`, `quicklook-json`, `qlvideo` let space-bar preview handle Markdown, source code, JSON, and more video formats. Since macOS 15 these need explicit enabling in **System Settings → Login Items & Extensions → Quick Look**.

### PDFs and documents

- **Preview** — built-in, does annotation, form filling, signatures, page reorder, merge (drag thumbnails between windows), and image conversion. Most people never need more.
- **Skim** (free, `skim`) — PDF reader for academics: notes, highlights with export, SyncTeX for LaTeX, presentation mode.
- **PDF Expert** ($80 yr or one-time tier) — if you edit PDFs heavily.
- **Zotero** handles paper PDFs (see above).
- **Pages / Numbers / Keynote** (free, App Store) — perfectly good, and Keynote is the best presentation app on any platform.
- **Microsoft 365** — free for most students through their university; install via `microsoft-office` or the Mac App Store. Word compatibility matters when a professor requires `.docx`.
- **LibreOffice** (free, `libreoffice`) — for when you need an office suite with no account.
- **Typora** ($15) / **MacDown** (free) / **iA Writer** ($50) — Markdown editors when you want to write prose rather than code. Or just VS Code with a Markdown preview.
- **LaTeX**: `mactex-no-gui` (cask, ~2 GB) plus **TeXShop** or VS Code with LaTeX Workshop; or **Overleaf** in the browser for collaborative writing. **Typst** (`typst`) is the modern alternative that compiles instantly and has a much saner syntax; most students writing solo papers should try it first.

### Media

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

### Menu bar and system utilities

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

### Reading and reference

- **Dash** ($30) — offline API documentation for 200+ languages/frameworks with instant search; integrates with Raycast/Alfred and every editor. Paid, one-time, worth it for anyone who reads docs daily. `dash`
- **DevDocs** (free, web / `devdocs` desktop wrapper) — the free equivalent; works offline as a PWA.
- **NetNewsWire** (free, open source, `netnewswire`) — RSS reader, iCloud sync. RSS is still the best way to follow release notes and blogs. **Reeder** ($) is the pretty one.
- **Kindle**, **Apple Books** — built-in / App Store.
- **Anki** (free, `anki`) — spaced repetition. See [chapter 20](20-cs-student-specific.html).

### Terminal-adjacent GUI tools

Covered in their own chapters, but for completeness in the app list: **Ghostty** or **iTerm2** ([chapter 9](09-terminal-and-shell.html)); **VS Code**, **Cursor**, **Zed**, **JetBrains Toolbox** ([chapter 12](12-editors-and-ides.html)); **OrbStack** ([chapter 13](13-containers-and-vms.html)); **TablePlus**, **Postico**, **DBeaver** ([chapter 15](15-databases-and-local-dev.html)); **Fork**, **Tower**, **GitHub Desktop**, **Sublime Merge** for Git GUIs ([chapter 10](10-dotfiles-and-git.html)); **Proxyman** or **Charles** for HTTP debugging; **Bruno**/**Postman**/**Insomnia** for API clients ([chapter 14](14-cloud-and-devops-tooling.html)); **Kaleidoscope** ($) or **Meld** (free) for visual diffs.

### Games and fun (yes, really)

Mac gaming in 2026 is real: **Steam** (`steam`), **CrossOver** ($74 yr; runs Windows games via Wine + Apple's Game Porting Toolkit), **Whisky** (free, `whisky` — the free Wine/GPTK wrapper), and Apple's own Games app (macOS 26) for Arcade and Store titles. **Heroic** for Epic/GOG. **OpenEmu** for retro. Set Steam to *not* launch at login.

### What to skip

- **Antivirus** — see [chapter 16](16-security-and-privacy.html). XProtect + Gatekeeper + common sense; Malwarebytes free for an occasional scan if paranoid.
- **CleanMyMac, MacKeeper, "memory cleaners", "battery optimizers"** — see [chapter 18](18-performance-and-maintenance.html).
- **Adobe Creative Cloud** unless a course requires it; Affinity and Pixelmator are free now.
- **Java runtimes from java.com** — install via mise or `brew install openjdk` ([chapter 11](11-languages-and-runtimes.html)).
- **Flash, Silverlight, Java browser plugins** — if a university system requires one, complain to IT; it's 2026.
- **Anything that asks to install a kernel extension** on Apple silicon — legitimate software uses system extensions now; a kext is a red flag or abandonware.

### The Tier 1 list

If you install nothing else from this chapter: **a password manager**, **Raycast or Alfred**, **a clipboard manager** (or Raycast's), **Rectangle or AeroSpace**, **Obsidian or Apple Notes**, **Itsycal**, **IINA**, **Shottr**, **Ice**, **Stats**, **AppCleaner**, **The Unarchiver**, **Karabiner-Elements** (if remapping), and **Zotero** (if writing). All are free. Everything is in [Appendix B](appendix-b-brewfile.html) with the optional items commented out.

[↑ Back to top](#table-of-contents)

---

## 20. CS-student specific

Most of this guide applies to anyone who writes software. This chapter is about the parts that are specifically *university*: the free software you're entitled to, the toolchains individual courses expect, the x86 Linux machine your systems class assumes you have, the lab servers you'll SSH into at 2 AM, and the writing you'll do. It also has an honest section on the Mac's weak spots for a CS degree — there are a few — and the workarounds.

> [!IMPORTANT]
> Read your course's setup instructions *first*, then this chapter. Many CS departments publish Mac-specific notes and provide a VM image or a container. If a course says "use the lab machines" or "use our Docker image," do that; it eliminates a whole category of "works on my machine" problems at submission time.

### Free stuff: claim it in week one

Student status unlocks a surprising amount of software and services. Most need a `.edu` (or equivalent) email or a student ID upload. Do this before buying anything.

| Program | What you get | Notes |
|---|---|---|
| **GitHub Student Developer Pack** | GitHub Pro (private repos w/ full features), **GitHub Copilot Pro free**, JetBrains all-products pack, Namecheap domain, DigitalOcean/Azure credits, 1Password (1 yr), Termius, Notion, and ~100 more | Apply at education.github.com. Re-verify each year. The single best perk list. |
| **JetBrains Educational** | All IDEs (IntelliJ Ultimate, PyCharm Pro, CLion, WebStorm, DataGrip, GoLand, RustRover…) free | Direct or via GitHub pack. Renew annually. |
| **Apple Education pricing** | ~10% off Macs, discounted AppleCare+; back-to-school promos usually add a gift card or accessories | Verified via UNiDAYS in most countries. See [chapter 1](01-hardware-and-buying.html). |
| **Apple Developer Program** | Free to build and run on your own devices; $99 yr to publish. Some universities are in the **iOS Developer University Program** — ask | Sideloading your own app to your iPhone is free with a free Apple ID. |
| **Microsoft 365** | Word/Excel/PowerPoint + 1 TB OneDrive, free at most universities | Through your school's portal. Also **Azure for Students**: $100 credit, no card. |
| **Google Workspace for Education** | Usually unlimited-ish Drive, Colab (free GPU time), Gemini | Depends on your institution. Colab is the cheapest way to get a GPU for an ML course. |
| **AWS Educate / Academy** | Credits and labs | Varies by school. |
| **Notion, Figma, Canva, Miro, Linear** | Free education plans | Figma Education is the full professional tier. |
| **Tableau, MATLAB, Mathematica, Autodesk** | Free via campus licenses | Check your IT software portal. MATLAB is usually a campus site license. |
| **Apple Music / Spotify / YouTube Premium** | Student plans ~50% off | Apple Music student includes TV+. |
| **Amazon Prime Student, Adobe (60% off), Cursor Pro (free 1 yr), Perplexity Pro, Warp** | Discounts / free tiers | Cursor's student offer requires .edu; check current terms. |
| **Overleaf** | Often institutional Premium | Check your library site. |
| **Zotero storage** | Some libraries fund unlimited | Ask the library. |
| **O'Reilly, ACM Digital Library, IEEE Xplore, Safari Books** | Through the library proxy | Set up the library's browser extension/EZproxy bookmarklet; you'll need papers behind paywalls from year two. |
| **ACM student membership** | $19 yr; includes O'Reilly access at many chapters | Worth it just for O'Reilly. |

Set a calendar reminder to re-verify GitHub Education and JetBrains each September.

### The course-by-course toolchain

A CS degree touches a lot of languages. The approach from [chapter 11](11-languages-and-runtimes.html) — `mise` for runtimes, `uv` for Python, Homebrew for compilers — handles all of them. Here's what each typical course expects and the Mac-specific gotchas.

#### Intro programming (Python / Java)

- **Python**: `uv python install 3.13` (or whatever the course pins — check; intro courses often lag a version). Use `uv init` per assignment folder, `uv add` for packages. Never `sudo pip`. Run scripts with `uv run script.py`. If the course insists on Anaconda, install `miniforge` via brew instead (same conda, no bloat, Apple-silicon native) and `conda init zsh`.
- **Java**: `mise use -g java@21` (or 25 — current LTS is 25, most courses want 17 or 21). IntelliJ IDEA Ultimate is free (above) and is what most Java courses assume. `brew install --cask intellij-idea`. If the course uses BlueJ or Greenfoot, both have Apple-silicon builds.
- **Scratch/Snap/Racket/Scheme** (some intro courses): `brew install --cask racket`; DrRacket is fine on Apple silicon.

#### C, C++, and systems programming

This is where the Mac diverges most from what courses assume. Apple's `cc` is **Clang**, not GCC, and macOS is not Linux.

- `xcode-select --install` gives you `clang`, `clang++`, `make`, `lldb`, `git` ([chapter 7](07-command-line-tools-and-xcode.html)). For most C/C++ coursework this is all you need. `gcc` on a Mac is a symlink to clang.
- **If the course requires real GCC** (specific flags, `-fanalyzer`, GCC-only extensions, or an autograder that uses GCC): `brew install gcc` and invoke as `gcc-15` / `g++-15`. Or, better, do the work in a Linux container/VM (below) so your environment matches the grader.
- **Valgrind does not run on Apple silicon macOS.** This is the #1 systems-course pain point. Options: (a) use Clang's sanitizers — `clang -fsanitize=address,undefined -g` catches most of what Valgrind would; (b) `leaks --atExit -- ./prog` (Apple's built-in leak checker); (c) run Valgrind inside an x86-64 or arm64 Linux container (Valgrind has arm64 Linux support). Most courses accept sanitizer output.
- **GDB** is a pain on macOS (code signing required, and it's flaky on Apple silicon). Use **LLDB** — same concepts, slightly different commands (`b`, `r`, `n`, `s`, `p`, `bt` all work). Or debug in a Linux container with GDB. VS Code's C/C++ extension uses LLDB on Mac transparently; **CodeLLDB** is the better extension.
- **Headers differ**: `#include <malloc.h>` doesn't exist (use `<stdlib.h>`); `<sys/epoll.h>` doesn't exist (macOS uses kqueue); `<endian.h>` is `<machine/endian.h>`; no `<sys/sendfile.h>`. Assignments that dip into Linux syscalls need Linux. Assignments that use POSIX generally compile fine.
- **Assembly**: courses teach x86-64 or RISC-V or ARM. On Apple silicon your native assembly is ARM64 — great if the course is ARM, irrelevant otherwise. For x86-64 assembly homework, use a Linux VM/container with `gcc`/`nasm`/`gdb` (Rosetta-accelerated x86 containers via OrbStack are fast enough). For RISC-V, `brew install riscv-gnu-toolchain` (from `riscv-software-src/riscv`) plus `qemu`, or the **Venus**/**RARS** simulators in the browser/Java.
- **Make/CMake**: `brew install cmake ninja`. CLion (free) handles CMake projects well.
- **Threads/OS courses**: xv6 (`riscv64` toolchain + qemu, above), Pintos (needs x86 — Linux VM), and anything with `fork()`-heavy code works natively.

**Recommended setup for a systems course:** native Clang + sanitizers for daily work, plus an Ubuntu container (`orb create ubuntu:24.04 cs` or the course's Docker image) for the autograder-matching build and Valgrind/GDB. See [chapter 13](13-containers-and-vms.html). With OrbStack, `cd` into your project and run `orb -m cs make test` — the same files, Linux toolchain.

#### Data structures & algorithms

Usually Java, C++, or Python; covered above. For competitive programming: `brew install gcc` for `bits/stdc++.h` (Clang lacks it; or create your own precompiled header), and use a fast judge client (**cph** extension in VS Code, or **Competitive Companion**).

#### Web development

Node via `mise use -g node@24` (26 is LTS from October 2026); `pnpm` or `npm`. Everything in [chapter 11](11-languages-and-runtimes.html) applies. Browser DevTools in Chrome or Firefox. If the course uses PHP/Laravel: `brew install php composer` or Laravel Herd.

#### Databases

`brew install postgresql@18` and `brew services run postgresql@18`, or a container. `sqlite3` is preinstalled. **TablePlus** (free tier) or **DBeaver** (free) for a GUI. MySQL courses: `brew install mysql` or a `mysql:9` container. Oracle: only via container (`gvenzl/oracle-free`, arm64 available). SQL Server: `mcr.microsoft.com/azure-sql-edge` or the 2025 arm64 preview in a container. See [chapter 15](15-databases-and-local-dev.html).

#### Machine learning & data science

The Mac is genuinely good here up to a point.

- **Python stack**: `uv add numpy pandas scikit-learn matplotlib jupyter`. Everything is Apple-silicon native now.
- **PyTorch**: `uv add torch torchvision` — the **MPS** backend uses the GPU (`device = "mps"`). Fast enough for coursework and small models; not CUDA. Some ops still fall back to CPU (`PYTORCH_ENABLE_MPS_FALLBACK=1`).
- **JAX**: `jax-metal` plugin, experimental. **TensorFlow**: `tensorflow-metal`, maintenance mode. Prefer PyTorch on a Mac.
- **MLX** (Apple's framework): `uv add mlx mlx-lm` — the fastest way to run and fine-tune LLMs locally on Apple silicon. `mlx_lm.generate --model mlx-community/Llama-3.2-3B-Instruct-4bit --prompt "..."`.
- **Local LLMs for studying**: **Ollama** (`brew install ollama`) or **LM Studio** (cask). A 16 GB Mac runs 7–8B models comfortably; 32 GB runs 20–30B; a 70B model wants 48 GB+. See [chapter 1](01-hardware-and-buying.html) for RAM planning.
- **When you need CUDA** (a course that requires it, or a model that won't fit): Google Colab (free tier, or Pro $10 mo), Kaggle notebooks (free 30 hrs/week GPU), your department's GPU cluster (SSH + Slurm — see below), Lambda/RunPod/Vast.ai for cheap hourly rentals. The Mac becomes a thin client; **VS Code Remote-SSH** or **JupyterLab over an SSH tunnel** (`ssh -L 8888:localhost:8888 user@gpu-box`) makes it feel local.
- **Jupyter**: `uv tool install jupyterlab`, or use VS Code's notebook UI (better diffing, git integration). **Positron** (Posit's VS Code fork for data science) or **RStudio** if the course is R-heavy (`brew install --cask r rstudio`; or `mise use r`).
- **conda/Anaconda**: if a course insists, `brew install --cask miniforge`. Don't install full Anaconda — 5 GB, slow shell startup, and it hijacks `python` globally.

#### Mobile development

- **iOS/Swift**: install **Xcode** from the App Store (or `xcodes` — see [chapter 7](07-command-line-tools-and-xcode.html)); it's 12+ GB, budget storage and an hour. Simulators are another 5–8 GB per iOS version. This is the one course where the Mac is *required*, not merely nice.
- **Android**: `brew install --cask android-studio`; the emulator runs arm64 Android images natively and fast on Apple silicon. Set `ANDROID_HOME` and add `platform-tools` to PATH for `adb`. Flutter: `mise use -g flutter`; React Native: Node + Watchman (`brew install watchman`) + Xcode/Android Studio.

#### Theory, math, and writing-heavy courses

- **LaTeX**: `brew install --cask mactex-no-gui` (2.5 GB — the full `mactex` adds GUI apps you won't use) or **BasicTeX** (100 MB, then `tlmgr install` packages as needed). Editor: VS Code + **LaTeX Workshop**, or **TeXShop**/**TeXstudio**. **Skim** as the PDF viewer for SyncTeX. Or **Overleaf** for group projects (institutional Premium is common).
- **Typst** (`brew install typst`): compiles in milliseconds, saner syntax, `typst watch paper.typ`. Most professors accept a PDF and don't care what made it. **Tinymist** VS Code extension for live preview. Templates exist for most conference formats. Recommended for solo problem sets.
- **Markdown → PDF**: `brew install pandoc` and `pandoc notes.md -o notes.pdf` (needs a TeX engine; Typst can be the engine: `pandoc -t typst`). **Quarto** for notebooks-as-documents.
- **Diagrams**: **Excalidraw** (web / VS Code extension / Obsidian plugin) for hand-drawn style; **draw.io** (`drawio`) for formal; **Mermaid** inline in Markdown; **Graphviz** (`brew install graphviz`) for automata and graphs; **TikZ** if you're deep in LaTeX.
- **Math tools**: `brew install --cask mathpix-snipping-tool` (screenshot → LaTeX, student pricing), **SageMath** (cask), **Wolfram Engine** free for developers, **GeoGebra**, Python with `sympy`. **Lean 4** (`brew install elan-init`, then VS Code extension) if you take a formal methods course.
- **Automata/logic**: **JFLAP** (Java, works), **Logisim Evolution** (`brew install --cask logisim-evolution`), **Digital**.

#### Other languages you may meet

`mise` handles Go, Rust, Ruby, Elixir, Erlang, Zig, Deno, Bun, Haskell (via `ghcup` — `mise use ghc` or `brew install ghcup`), OCaml (`brew install opam`), Prolog (`brew install swi-prolog`), Lisp (`brew install sbcl` + Emacs/SLIME or VS Code), Standard ML (`brew install smlnj`), Lua, Kotlin (`brew install kotlin` or via IntelliJ), Scala (`brew install coursier` → `cs setup`), Fortran (`brew install gcc` gives `gfortran`), Ada, COBOL — yes, `brew install gnucobol`. Nothing in a CS curriculum lacks an Apple-silicon build in 2026.

### When you need Linux

You will. The four routes, cheapest-friction first:

1. **OrbStack Linux machine** (`orb create ubuntu:24.04`) — a full Ubuntu userland sharing your Mac filesystem, starts in a second, near-native speed. `orb -m ubuntu bash` drops you in; your `~/code` is at the same path. Handles 90% of "this only works on Linux." Free for personal/student use. See [chapter 13](13-containers-and-vms.html).
2. **The course's Docker image** — `docker run -it -v "$PWD":/work course/image` and your files are inside. Exactly matches the autograder.
3. **x86-64 Linux** — for x86 assembly, Pintos, old binaries, or a course VM shipped as an `.ova`. Options: `orb create --arch amd64 ubuntu` (Rosetta-translated, surprisingly fast for compiles and gdb; you lose Rosetta on macOS 28, so prefer arm64 where possible); **UTM** (free; QEMU-based, full emulation — slow but runs anything, including that `.ova` after conversion); **VMware Fusion** (free since 2024) or **Parallels** (paid, $100 yr; student discount) both run **arm64** Linux/Windows fast but **not x86**. Full x86 emulation is 5–20× slower than native; fine for a shell and gdb, painful for builds. If a course truly needs x86 performance, use the department's Linux servers.
4. **Remote Linux** — see the next section. A `$5/mo` VPS or the lab servers is often the least-friction x86 machine you'll ever have.

> [!NOTE]
> A "Linux VM" for a CS course does not need to be Ubuntu Desktop with a GUI. Terminal-only Ubuntu Server or the OrbStack machine, with VS Code Remote-SSH or `orb` integration for editing, is faster and uses a quarter of the RAM. If you need a GUI for a specific tool, run it with X forwarding (`brew install --cask xquartz`) or in a full UTM VM.

### Windows (for the one course that needs it)

Visual Studio (not Code), .NET Framework (not modern .NET — that runs natively), MS Access, some CAD or EDA tools, and games. Options: **Windows 11 ARM** in **Parallels** (easiest; it's a licensed, supported path — Parallels downloads the ISO; student pricing available), **VMware Fusion** (free; bring your own ISO from Microsoft's site), or **UTM** (free, slower). Windows on ARM runs x86/x64 apps through its own emulation, and it's decent. A cheap alternative for occasional use: your university's **Windows virtual lab** (Citrix/AVD), or **Windows 365**. Don't dual-boot — Boot Camp doesn't exist on Apple silicon.

### Remote machines: lab servers, clusters, and cloud

By second year you'll live in `ssh`. Make it good.

```sh
# ~/.ssh/config
Host lab
  HostName lab.cs.university.edu
  User yourid
  ForwardAgent no
  ControlMaster auto
  ControlPath ~/.ssh/cm-%r@%h:%p
  ControlPersist 10m
  ServerAliveInterval 60

Host gpu1
  HostName gpu1.cs.university.edu
  User yourid
  ProxyJump lab            # bastion hop; lab is reachable, gpu1 isn't
  LocalForward 8888 localhost:8888   # Jupyter
```

- **Keys, not passwords**: `ssh-keygen -t ed25519` and `ssh-copy-id lab`. Use `UseKeychain yes` + `AddKeysToAgent yes` so Touch ID (via the Keychain) unlocks the key. Full SSH setup in [chapter 9](09-terminal-and-shell.html).
- **Don't lose work to a dropped connection**: run long jobs in `tmux` on the server (`tmux new -s work`, later `tmux attach -t work`). Or **mosh** (`brew install mosh`; needs the server side installed) for a connection that survives Wi-Fi changes and sleep.
- **Edit remotely as if local**: VS Code **Remote-SSH** (installs a server component in your home directory — works on most lab machines without root), or **Zed** remote, or JetBrains **Gateway**. Or edit locally and `rsync -avz --exclude .git ./ lab:~/proj/` before running. Or mount with `sshfs` (via `macfuse` — needs a system extension; the Finder integration is nice but flaky).
- **Slurm clusters** (GPU/HPC): `sbatch job.sh`, `squeue -u $USER`, `srun --pty bash` for interactive; load modules with `module load cuda/12.6`. Keep a `~/.bashrc`/`.zshrc` on the cluster in your dotfiles repo with a hostname branch ([chapter 10](10-dotfiles-and-git.html)).
- **VPN**: universities require it off-campus; usually **Cisco Secure Client**, **GlobalProtect**, or **WireGuard**/**OpenVPN** profiles. Install from your IT portal, not Homebrew (licensing). Use split tunneling if offered so your Spotify doesn't go through campus.
- **Cheap always-on Linux**: a $4–6/mo VPS (Hetzner, DigitalOcean w/ GitHub Education credits, Oracle Cloud's free arm64 tier) as a personal x86 or arm box, tunnel endpoint, and place to leave `tmux` running. **Tailscale** (free for personal, `brew install --cask tailscale`) puts your Mac, the VPS, and your phone on one private network — SSH to any of them from anywhere, no port forwarding.

### Version control for coursework

Everything in [chapter 10](10-dotfiles-and-git.html), plus:

- **One repo per course** (`~/code/uni/cs240/`) with a folder per assignment, or one repo per assignment if the course uses GitHub Classroom (it will create them). *Private.* Public solutions violate most academic integrity policies, and a future employer searching your GitHub won't be impressed by `hw3_final_FINAL2.py`.
- **Commit at every working state** — the autograder eating your submission, a bad `rm`, a laptop theft: all recoverable with a pushed commit.
- **`.gitignore` for the course's language** — `gh repo create --gitignore Python` or `gitignore.io`. Never commit `venv/`, `node_modules/`, `.o` files, or `.DS_Store` (the global ignore from chapter 10 handles the last one).
- **Group projects**: agree on a branch/PR flow in the first meeting, protect `main`, use Issues, use `git blame` for blame only at the retro. Use the GitHub Classroom template if provided.
- **Academic integrity and AI tools**: know your course's policy on Copilot/Cursor/ChatGPT *before* the assignment. Many intro courses ban them; many upper-level courses allow them with disclosure. Some autograders detect Copilot-style output. Disable Copilot per-workspace (`"github.copilot.enable": {"*": false}` in the course's `.vscode/settings.json`) so you don't accidentally cross a line.

### Studying on the Mac

- **Notes**: Obsidian or Apple Notes ([chapter 19](19-daily-driver-apps.html)). For lecture notes with math, Obsidian's MathJax (`$…$`) is the fastest path; **Notability**/**GoodNotes** on iPad with Sidecar/Universal Control if you handwrite.
- **Spaced repetition**: **Anki** (`brew install --cask anki`) for anything with definitions — theory courses, networking layers, complexity classes, syscalls. Free on Mac; the iOS app is $25 once.
- **Focus**: macOS **Focus modes** (Control Center) with per-Focus Home Screen/notification filtering; **Screen Time** app limits; **Cold Turkey**/**Focus** for hard blocking; **Raycast Focus** for lighter sessions. Keep Slack/Discord closed during study blocks (not just muted).
- **Reading papers**: **Zotero** + Better BibTeX plugin exports `.bib` for LaTeX/Typst; **Skim** or **Preview** for annotation; **Sioyek** (`brew install --cask sioyek`) is a keyboard-driven PDF reader designed for papers and textbooks.
- **Lecture recordings**: **IINA** at 1.5–2× with pitch correction; **Whisper** locally (`brew install whisper-cpp` or MacWhisper) for transcripts of recorded lectures — Apple silicon runs the `large-v3-turbo` model faster than real time.
- **Problem sets**: a `template/` folder with a `main.typ` or `hw.tex`, a `Makefile`, and a `README` you copy per assignment. Small thing, saves an hour a week over a semester.

### Battery and hardware, student edition

- A MacBook Air M5 or Neo makes it through a full day of lectures on battery. A 14" Pro does too; a 16" Pro is heavy in a backpack — buy it only if you're genuinely doing local ML or video.
- Enable the **80% charge limit** ([chapter 18](18-performance-and-maintenance.html)) if you mostly work at a desk; turn it off for exam weeks when you're never near an outlet.
- **Low Power Mode** on battery for note-taking days.
- Use the **USB-C charger from your phone** in lecture halls — any 20 W+ USB-C PD brick slow-charges a MacBook. Carry a compact 65–70 W GaN charger (Anker, UGREEN) rather than Apple's; it's smaller and charges the phone too.
- **AppleCare+** is worth it for a laptop that lives in a backpack for four years; accidental damage claims are $99–299 vs. a $700+ screen. Education pricing discounts it.
- **Find My** on, **Activation Lock** on (automatic with Find My), and **Stolen Device Protection** (macOS 26.4+) on. Laptop theft from libraries is common; a stolen Mac with Activation Lock is a brick for the thief. See [chapter 16](16-security-and-privacy.html).
- Back up. Your thesis is not safe on one SSD. Time Machine to a $60 external drive plus GitHub for code plus iCloud/Backblaze for documents ([chapter 17](17-backup-and-recovery.html)).

### The honest list of Mac disadvantages for CS

- **No Valgrind, flaky GDB**, x86 assembly needs emulation, no `epoll` — systems courses are where you'll notice you're not on Linux. The container/VM route fixes all of it.
- **8 GB isn't enough** for Docker + IDE + browser. If you already own an 8 GB machine, run containers on a VPS or the lab servers and keep local work light.
- **x86 Windows software** (some CAD/EDA, old lab software, anticheat games) — emulation only. A Windows PC in the lab or a cloud desktop is the workaround.
- **Rosetta ends with macOS 28** — Intel-only Mac apps and x86 containers will need alternatives by 2027–2028. For a student starting in 2026 on a 4-year degree, plan for arm64-native everything.
- **Cost** — offset by education pricing and the fact that a $600–1,100 Mac outlasts the degree.

Everything else — Unix shell, native Git, Docker performance, battery life, the display, the trackpad, the fact that your TA's demo will probably be on a Mac — favors it.

[↑ Back to top](#table-of-contents)
