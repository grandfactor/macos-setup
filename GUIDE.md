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
