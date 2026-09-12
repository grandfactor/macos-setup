# Research notes: macOS versions & Mac hardware (as of 2026-09-12)

## macOS versions
- **macOS 26 "Tahoe"** (released Sept 2025). Liquid Glass redesign, Spotlight overhaul (clipboard
  history, actions, quick keys), Phone app on Mac, Live Translation, Foundation Models framework,
  **Containerization framework** + `container` CLI (apple/container on GitHub; Linux containers in
  lightweight VMs, optimized for Apple silicon). Terminal.app got 24-bit color + Powerline glyphs.
  Last version to support Intel Macs (only 2019 MBP 16", 2020 27" iMac, 2019 Mac Pro, 2020 MBP 13" 4-port).
- **macOS 27 "Golden Gate"** — announced WWDC June 8 2026, **ships September 14, 2026** (2 days from now).
  - **Apple silicon only. No Intel support.** Runs on every M-series Mac + "MacBook Neo".
  - Liquid Glass transparency slider (System Settings > Appearance). Less-rounded corners, uniform
    toolbars, edge-to-edge sidebars, coloured sidebar icons return.
  - **Siri AI** (Gemini-derived Apple Foundation models; Private Cloud Compute, some on Google Cloud/NVIDIA).
    Lives in Spotlight: Cmd+Space = "Search or Ask". Standalone Siri app. Write with Siri systemwide.
    Custom Siri voice + improved on-device dictation need **M3+ and >=12GB RAM**.
  - **Visual Intelligence on Mac**: Cmd+Shift+Space (or Cmd+Shift+6) select screen region; also in Cmd+Shift+5.
  - Safari: AI tab grouping, "Create an Extension" via natural language, "Notify Me" page monitoring.
  - Shortcuts: "Describe a Shortcut" natural language creation.
  - Passwords app auto-changes weak/compromised passwords.
  - Notes: Markdown copy/paste, section links.
  - Performance: better external display window restoration, more hi-res/high-refresh modes,
    faster AirDrop, faster SMB/NAS browsing, rebuilt search index.
  - Spotlight/Shortcuts indexing faster. Image Playground has daily caps (more with iCloud+).
  - New parental controls (Time Allowances, Ask to Browse).
- Apple Intelligence languages: EN, DA, NL, FR, DE, IT, NO, PT, ES, SV, TR, VI, ZH (simp/trad), JA, KO.

## Hardware (2026)
- **MacBook Air M5** (13"/15") announced Mar 3 2026, avail Mar 11. Up to 32GB RAM, 4TB SSD.
  Base: 16GB/512GB. 10-core CPU / 8-core GPU base. 12MP Center Stage camera.
- **MacBook Pro 14" M5** — std 1TB, $1,699 ($1,599 edu). (M5 14" originally Oct 2025)
- **MacBook Pro M5 Pro / M5 Max** announced Mar 3 2026 (avail Mar 11):
  - M5 Pro: 15-core (5 "super" + 10 perf) or 18-core (6+12) CPU; 16/20-core GPU; starts 1TB.
  - M5 Max: 18-core CPU; 20/32/40-core GPU; starts 2TB; up to 128GB RAM.
  - New "super cores" nomenclature; Neural Accelerator in every GPU core.
  - N1 wireless chip: Wi-Fi 7, Bluetooth 6. Thunderbolt 5 x3, HDMI 8K, SDXC, MagSafe 3.
  - Up to 24h battery; 50% fast charge in 30 min w/ 96W+.
  - External displays: M5 Pro up to 2, M5 Max up to 4.
  - Prices: 14" M5 Pro $2,199 ($2,049 edu); 16" M5 Pro $2,699 ($2,499 edu);
    14" M5 Max $3,599 ($3,299 edu); 16" M5 Max $3,899 ($3,599 edu).
- **"MacBook Neo"** — a new lower-cost MacBook line (mentioned as supported by macOS 27;
  reviewers compare Air M5 vs Neo). Need details.
- Sept 9 2026 Apple event: "iPhone Duo and more".
- AppleCare One (US) multi-device plan exists.

## Additional (2026-09-12, second pass)
### Rosetta 2 timeline
- macOS 26 Tahoe: last Intel-Mac release; Intel Macs get security updates ~3 years (to ~Sept 2029).
- macOS 26.4 began warning users when launching Intel (x86_64) apps.
- **macOS 27 install removes Rosetta 2 if previously installed; it CAN be reinstalled**
  (`softwareupdate --install-rosetta --agree-to-license`). Golden Gate = last full Rosetta release.
- **macOS 28 (fall 2027): Rosetta 2 removed for general apps**; only kept for a set of old unmaintained games.
  => Guide must push: avoid x86 Homebrew (/usr/local), prefer arm64 everything; check `file`/Activity Monitor "Kind".
- Xcode 27: Apple-silicon only, coding agents (agentic workflows), Device Hub, untitled projects/standalone
  Swift files w/ previews, improved Instruments; ~30% faster (per press). Game Porting Toolkit 4.
- New frameworks: **Core AI** (build/run/deploy AI models on Apple silicon; unified memory), MLX (open source),
  Foundation Models framework (from macOS 26), Containerization.
- macOS 27 denies cross-team app container access by default (security hardening).
- macOS 27 installs as a Delta Update via System Settings (~19.5GB from Tahoe).

### MacBook Neo (Mar 2026) — budget Mac
- 13.0" 2408x1506 IPS, 500 nits, sRGB. A18 Pro chip (6-core CPU 2P+4E, 5-core GPU), **8GB RAM only**
  (LPDDR5X, 60GB/s), 256GB $599 ($499 edu) / 512GB $699? Touch ID on higher config only.
  2x USB-C (one USB3 10Gb/s + DP1.4, one USB2), 3.5mm jack, Wi-Fi 6E, BT 6, 1080p camera, 1 ext display 4K60,
  36.5Wh battery (16h video), 20W charger, 1.23kg. Colours silver/blush/citrus/indigo.
  => Verdict for CS students: OK for web/notes/light coding; 8GB is a hard ceiling for Docker/IDEs/VMs.
     Recommend Air M5 16GB+ as the real floor for SWE.

### Desktops (Aug 25 2026, ship Sept 22)
- **Mac mini M6**: 12-core CPU, 12-core GPU w/ Neural Accelerators, 16GB std -> 32GB, 170GB/s, $899 ($799 edu).
  Wi-Fi 7/BT 6, 2.5GbE std (10GbE option), TB5. "World's fastest single-thread".
- **Mac mini M5 Pro**: up to 18-core CPU/20-core GPU, up to 64GB, 307GB/s, $1,699 ($1,599 edu).
- **Mac Studio M5 Max**: 18-core CPU (6 super + 12 perf), up to 40-core GPU, up to 128GB, 614GB/s, $2,499 ($2,299 edu).
- **Mac Studio M5 Ultra**: up to 36-core CPU, 80-core GPU, up to 512GB (late Oct), $5,499 ($5,099 edu).
  TB5 clustering for distributed inference; up to 8 displays. Studio Display XDR exists (5K 120Hz).
- Note M6 generation has begun (Mac mini first); MacBook Pro M6 (OLED rumored) likely late 2026/2027.
- Apple Upgrade = US leasing program (Klarna).
