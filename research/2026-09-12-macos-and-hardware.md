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
