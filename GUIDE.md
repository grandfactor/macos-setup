# The macOS Setup Guide

_For CS students, software engineers and everyone who lives on a Mac — 2026 edition_

> This is the single-document Markdown adaptation of the website. The same content is split chapter-by-chapter in [`guide/`](guide/), and rendered as a site in [`docs/`](docs/). Last reviewed September 2026.

## Table of contents

**Part I — Before you start**

- [01. Hardware & buying guide](#01-hardware-buying-guide) — Which Mac to buy in late 2026, how much RAM and storage you actually need, education pricing, refurbs, and the accessories that matter.

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
