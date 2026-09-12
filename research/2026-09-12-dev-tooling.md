# Research notes: developer tooling landscape (as of 2026-09-12)

## Homebrew
- 5.0.0 (Nov 2025): concurrent downloads default, Linux ARM64 official, deprecated casks failing Gatekeeper.
- 5.1.0 (Mar 2026): brew bundle expansion, `brew version-install`, `-full` formula handling.
- **6.0.0 (Jun 11 2026)** — current major:
  - **Tap trust**: third-party taps must be explicitly trusted (`brew tap --trust`, `brew trust`);
    official taps trusted by default; `brew bundle` honours `trusted:`.
  - Internal JSON API default (faster `brew update`).
  - `ask` mode default for developers: install/upgrade show plan + confirm (HOMEBREW_ASK).
  - `brew bundle` parallel installs by default; npm/cargo/go/uv/krew/winget extensions; cleanup asks.
  - `brew exec` (like npx). `brew as-console-user`. `brew update <formula>` = upgrade.
  - Casks pinnable. `brew vulns` (vulnerability check tap). SBOM opt-in (HOMEBREW_SBOM).
  - Initial macOS 27 support.
  - **Sept 2026: Intel x86_64 macOS → Tier 3 (no CI, no new bottles). Sept 2027: deleted entirely.**
  - Casks that fail Gatekeeper disabled Sept 2026.
  - BrewUI (official GUI) upcoming. Supply-chain docs: docs.brew.sh/Supply-Chain-Security.
  - Prefix: /opt/homebrew (arm64). /usr/local is legacy Intel — avoid on Apple silicon.

## Terminals (2026 consensus)
- **Ghostty** (Mitchell Hashimoto, Zig, native GPU, libghostty) — fastest rendering; native macOS UI; minimal config.
  Top pick for most. Config at ~/.config/ghostty/config.
- **iTerm2** — deepest feature set (shell integration, tmux -CC, triggers, profiles). Still great.
- **WezTerm** — Lua config, cross-platform, multiplexer built-in.
- **Kitty** — fast, keyboard-driven, kittens, image protocol.
- **Warp** — AI-native, blocks, opinionated, account required (now optional?), closed source.
- **Alacritty** — minimal, no tabs.
- Terminal.app in Tahoe/GG: 24-bit color, Powerline glyphs, new default theme — actually usable now.

## Containers (2026)
- **Apple `container`** (apple/container, Apache 2.0): 1.0 stable Jun 9 2026, v1.2.x Aug 2026. ~49k stars.
  One lightweight VM per container (Virtualization.framework), Apple silicon only, needs macOS 26+ for full
  networking. **No native Compose yet (mid-2026)**, no k8s, CLI only. Slower cold start (~0.9s) but higher
  throughput. `container system start`, `container run`, `container build`, `container list`.
- **OrbStack** — macOS only, closed source, free personal / $8/user/mo commercial (>$10k/yr from work);
  1 license = 5 devices. ~400MB idle, <1% CPU, virtiofs bind mounts ~3-4x faster than Docker Desktop.
  Built-in k8s, Linux machines. Drop-in docker CLI. v2.2.2 last for old Intel.
- **Docker Desktop** — cross-platform; free for <250 employees & <$10M revenue; Pro $9, Team $15, Business $24/user/mo.
  1-4GB idle. Fastest image builds in some benchmarks. Docker Desktop 4.4x.
- **Colima** (Lima-based, MIT, CLI only), **Podman** + Podman Desktop (daemonless, Red Hat), **Rancher Desktop** (SUSE, k3s).
- Recommendation: students → OrbStack (free) or Colima; try `container` on the side; Docker Desktop if org pays.

## Window management (2026)
- **AeroSpace** — i3-like tiling, no SIP disable, own workspaces (not Spaces). Most-recommended tiler.
- **yabai** — deepest, needs partial SIP disable for some features; pairs with skhd.
- **Amethyst** — xmonad-like, simpler.
- **Rectangle** (free) / Rectangle Pro — keyboard snapping. **Loop** — radial menu snapping. **Raycast** window mgmt built in.
- **BetterStage**, **Swish** (trackpad gestures), **Hammerspoon** (Lua scripting) also.
- Native: Tahoe/Sequoia window tiling (drag to edge, Fn/Globe+Ctrl+arrows), Stage Manager.
