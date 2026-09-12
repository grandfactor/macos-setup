# Tahoe 26.x feature detail + language runtime schedules (2026-09-12)

## Spotlight (Tahoe+)
- Cmd+Space; then **Cmd+1 Apps, Cmd+2 Files, Cmd+3 Actions, Cmd+4 Clipboard**. Apps view replaces Launchpad
  (Launchpad removed). 7-column grid (26.1); grid search results (26.4).
- Files: slash filters `/pdf`, `/word`, `/text`. Up-arrow = search history.
- Actions: run Shortcuts, send message, etc. **Quick Keys** auto-assigned (e.g. `sm`). Reset: Settings > Spotlight.
- Clipboard History: must enable (Spotlight > Clipboard > Turn On or Settings > Spotlight). **Items expire after 8 hours;
  no pinning.** Pastes plain text. → recommend Maccy (free, OSS) / Raycast / Paste for persistent history.
- Settings > Spotlight: disable "Show Related Content" for local-only results.

## Tahoe 26.x point-release timeline
- 26.0 Sept 15 2025; 26.1 Oct 2025 (Liquid Glass Clear/Tinted toggle); 26.2 Dec 12 2025 (Edge Light, TB5 clustering,
  MLX full access M5, Wi-Fi 6E 160MHz, Urgent Reminders, MDM PPPC visibility); 26.3 Feb 11 2026 (Finder column fix);
  26.3.1 Mar 4 (Studio Display 2026 / XDR); 26.3.2 Mar 10 (Neo only); **26.4 Mar 24 2026**: MacBook **charge limit 80-100%**
  (Settings > Battery > Charging), Slow Charger notification, **Stolen Device Protection for MacBooks**
  (Settings > Touch ID & Password), Safari compact tab bar returns, Rosetta warnings, 70+ CVEs; 26.5 late spring.
- Settings paths: Appearance > Opaque menu bar; Appearance > Icon & Widget Style (Default/Clear/Tinted/Light/Dark);
  Appearance > Folder Color; Text Highlight Color separate from accent; Wallpaper > Clock Appearance.
- Right-click folder > Customize Folder (color/symbol/emoji).
- Desktop widgets: Ctrl-click wallpaper > Edit Widgets. "Click wallpaper to reveal desktop" → set "Only in Stage Manager".
- Control Center: Edit Controls; right-click control > Pin to Menu Bar. Cmd-drag to reorder/remove menu bar items.
- Shortcuts Automations tab on Mac (triggers: time, app open/quit, display connect, power, Wi-Fi, Focus, battery, folder).
- Phone app (needs iPhone 11+ iOS 26, same Apple Account). Live Activities in menu bar. Journal, Games app.
- Terminal.app: 24-bit color, Powerline glyphs. **ASIF** disk image format (fast, near-native SSD) — use for VMs.
- Background Security Improvements toggle: Settings > General > Software Update.
- Writing Tools systemwide. Notes math solver, 3D graphs.
- Compatibility: all Apple silicon + Intel (2019 MBP16, 2020 MBP13 4-port, 2020 iMac, 2019 Mac Pro). Neo needs 26.3+.

## Runtimes (Sept 2026)
- **Node.js 26** = Current (Apr 2026), **enters LTS Oct 2026**, EOL Apr 2029. Node 24 LTS (Oct 2025–Apr 2028). Node 22 LTS maint→Apr 2027.
  **New schedule from Oct 2026**: one major/yr (April), every release LTS, Alpha channel Oct–Mar. Node 27 Alpha Oct 2026,
  27.0.0 Apr 2027. Version numbers align with year.
- **Python 3.15 final ~Oct 1 2026**; 3.14 (Oct 2025) current stable. PEP 2026 calendar versioning was REJECTED (stays 3.15).
  Note: 3.14 has free-threaded build option (`python3.14t`), JIT experimental. uv is the tool.
- Java: JDK 25 LTS (Sept 2025); JDK 27 LTS Sept 2027. JDK 26 (Mar 2026), 27 (Sept 2026) non-LTS... Actually JDK LTS cadence
  is every 2 yrs: 21 (2023), 25 (2025), 29 (2027)? — Oracle: LTS every two years: 17, 21, 25. Next LTS = 29 (Sept 2027)? No—
  cadence is 2 years so 25 (Sep 2025) → 27?? Verify. [Oracle moved to 2-yr LTS: 17→21→25→(29 would be 4y) so next = 27? No.]
  DECISION: say "JDK 25 is the current LTS (Sept 2025); JDK 27 ships Sept 2026 as a feature release; use Temurin/Zulu via mise/brew."
- Go 1.26 (Feb 2026), Go 1.27 (Aug 2026). Rust 1.9x stable every 6 weeks; Rust 2024 edition current.
- Swift 6.3 with Xcode 27. Ruby 4.0 (Dec 2025). PHP 8.5 (Nov 2025). .NET 10 LTS (Nov 2025), .NET 11 Nov 2026.
- Bun 1.3+ ; Deno 2.x; pnpm 10.
