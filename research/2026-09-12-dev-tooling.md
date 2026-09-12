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

## Launchers
- Tahoe Spotlight: clipboard history (Cmd+Space then Cmd+4 / Cmd+Ctrl+? ), actions, Quick Keys ("sm" → send message),
  app intents. Golden Gate: Spotlight = "Search or Ask" w/ Siri AI. Many consider it "good enough" for launching.
- Raycast: free tier generous (launcher, clipboard, snippets, window mgmt, extensions store ~2000+); Pro for AI/sync.
- Alfred: one-time Powerpack (~£34), fastest raw search, workflows for automation chaining.
- LaunchBar also exists. Consensus 2026: Spotlight for search, Raycast for most devs, Alfred for power automation.

## Editors (Sept 2026)
- VS Code 1.134 (Aug 19 2026) ~75.9% share (SO survey). Free. Copilot via extension (~$10/mo; free tier exists).
- Cursor 3.19.x (Anysphere, $50B valuation Jul 2026). Hobby free; Pro $20; Pro+ $60; Ultra $200; Teams $40/user+$80 base.
  ~18% share. Fork of VS Code, extensions compatible.
- Zed (Rust, GPU): ~180ms cold start vs ~2.1-2.4s Electron; ~142MB idle RAM. Free core; AI add-on ~$10/mo.
  Agent Client Protocol (ACP) → plug in Claude Code / OpenCode. ~7.3% share. Debugger catching up. Native collab.
- Windsurf, Google Antigravity (agent manager IDE), JetBrains (IntelliJ/PyCharm/CLion etc.; free for students via
  GitHub Student Developer Pack / edu license), Neovim (LazyVim/kickstart), Helix, Sublime Text 4, BBEdit, Nova (Panic).
- Terminal agents: Claude Code, OpenAI Codex CLI, Gemini CLI, OpenCode, Amp, Aider. Xcode 27 has coding agents.
- Student advice: VS Code (free) + Copilot free/student + optional Zed; JetBrains free with edu email.

## Version managers
- **mise** (mise-en-place, Rust) = 2026 default: asdf-compatible, single binary, `.mise.toml`/`.tool-versions`,
  also tasks + env. Replaces nvm/fnm/pyenv/rbenv/goenv.
- **uv** (Astral) for Python: `uv python install 3.13`, `uv venv`, `uv tool install ruff`, `uvx`. Replaces pip/pipx/pyenv/poetry.
- fnm (fast nvm), volta, nvm still used for Node. pnpm/bun for packages. Bun 1.x as runtime.
- asdf rewritten in Go (0.16+, 2025) — new commands; still fine.
- rustup for Rust (brew install rustup / rustup-init). SDKMAN or mise for Java; Homebrew openjdk also fine.
- Go: brew install go (fast moving, brew ok) or mise.

## Security notes (Tahoe/GG)
- **FileVault ON by default** when you sign in with Apple Account during Setup Assistant (Tahoe+).
- Tahoe: Recovery Key now stored in **iCloud Keychain (E2E) & viewable in Passwords app**; old plain iCloud escrow gone;
  "Show" button in System Settings > Privacy & Security > FileVault. `sudo fdesetup validaterecovery`.
- Rapid Security Responses (letter suffix). Enable both "Install macOS updates" and "Install Security Responses & System Files".
- Lockdown Mode exists for high-risk users. Passkeys now mainstream; Passwords app (Sequoia+) handles passkeys.
- Gatekeeper (Sequoia+): no more right-click "Open" bypass; must go to System Settings > Privacy & Security > "Open Anyway".
  `xattr -d com.apple.quarantine`, `spctl` (--master-disable removed in Sequoia).
- ERNW macOS 26 Tahoe Hardening Guide (Feb 2026) on GitHub — cite.
- Admin vs standard account: best practice = daily standard user, separate admin. Note: Homebrew works fine as standard
  user if /opt/homebrew owned by that user (installer needs admin once).
- macOS 27: cross-team container access denied by default.
- Apple Intelligence: Private Cloud Compute; can disable per-feature in System Settings > Apple Intelligence & Siri.
