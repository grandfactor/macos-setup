<!--
number: 11
part: Part III — Developer environment
description: One version manager (mise) for everything, uv for Python, Node/Bun/Deno, Java, Go, Rust, C/C++, Swift, Ruby, .NET, and the ML stack (PyTorch MPS, MLX, Ollama) — with the 2026 release calendar.
-->
# Languages & runtimes

The rule that prevents 90% of "it works on my machine": **never use the system interpreter, never install runtimes globally with Homebrew when the project pins a version, and manage every language with one tool.** In 2026 that tool is **mise**, with **uv** handling Python's packaging on top. This chapter sets up each major language the way a CS curriculum or a modern job will need it.

## mise: one version manager to rule them all

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

## Python

Python is the language most likely to be a mess on a Mac. There are at least four interpreters on a typical machine (Apple's CLT shim, Homebrew's, one from the python.org installer, a Conda one) and a dozen packaging tools. The 2026 answer is **uv**.

### uv does everything

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

### Python 3.14 and 3.15

3.14 (Oct 2025) is current; **3.15 lands ~October 1, 2026**. 3.13+ offers an optional **free-threaded** build (`uv python install 3.14t`) with the GIL disabled and an experimental JIT — useful for a concurrency course, not for default use. Some scientific packages lag a new release by 1–3 months; if `uv add numpy` fails on 3.15 in October, pin `python = "3.14"` in `mise.toml`.

### Conda, Jupyter, data science

If your course requires **Anaconda/Miniconda** (common in data-science and stats departments), install **Miniforge** (`brew install --cask miniforge`, conda-forge defaults, arm64-native, no Anaconda licence issues) and run `conda config --set auto_activate_base false` so it doesn't hijack every shell. Prefer `mamba`/`micromamba` for speed. Mixing conda and uv in one project is asking for trouble — pick per project. For Jupyter: `uv add --dev jupyterlab` then `uv run jupyter lab`, or use VS Code's notebook UI (`ms-toolsai.jupyter`), or **JupyterLab Desktop**. **Positron** (Posit's VS Code-based data science IDE) is the R + Python IDE of choice; **RStudio** if you prefer.

Apple silicon notes: NumPy/SciPy use Apple's **Accelerate** BLAS by default (fast); PyTorch supports the **MPS** backend (`torch.device("mps")`) for GPU training on the Mac; TensorFlow via `tensorflow-metal`; JAX via `jax-metal` (experimental). See [ML](#machine-learning-on-apple-silicon) below.

## JavaScript / TypeScript

### Node.js

Install through mise, never through the Node installer or Homebrew's `node` (which can't switch versions):

```sh
mise use --global node@lts     # Node 24 LTS today; Node 26 becomes LTS in October 2026
mise use node@26               # per project
corepack enable                # lets `pnpm`/`yarn` commands install themselves at the version in package.json
```

**Release schedule change**: Node 26 (April 2026) is the last release under the odd/even model; it enters LTS October 2026 and is supported to April 2029. From October 2026 Node moves to **one major per year (April), every release LTS, an Alpha channel October–March**, with versions matching the year (27.0.0 in April 2027). Practically: pin the current LTS in `mise.toml` and bump once a year.

### Package managers

- **pnpm** (`mise use -g "npm:pnpm"` or `corepack`) — fast, disk-efficient (content-addressed store), strict; the 2026 default for new projects.
- **npm** — ships with Node; fine; slower; `npm ci` in CI.
- **Bun** (`mise use -g bun@latest`) — a runtime *and* package manager *and* bundler *and* test runner. `bun install` is the fastest installer; `bun run` executes TypeScript directly. Increasingly used as the package manager even for Node projects.
- **Yarn** — Berry (v4) is fine if a project already uses it; don't start new projects on Yarn Classic.
- **Deno** 2.x — Node-compatible, secure-by-default, great for scripts and Fresh apps.

Set `pnpm config set store-dir ~/.local/share/pnpm/store` once. Global CLI tools: `pnpm add -g` or via mise's `npm:` backend so they're in your `config.toml`.

### Tooling

TypeScript (`pnpm add -D typescript`), **Biome** (linter+formatter, replaces ESLint+Prettier for many stacks) or ESLint 9 + Prettier, **Vite** for front-end, **Vitest**/**Bun test**/**Playwright** for tests. Browser devtools: Safari's Web Inspector (`Settings → Advanced → Show features for web developers`), Chrome DevTools, Firefox Developer Edition. **Node version in VS Code terminals** follows mise automatically because the integrated terminal runs your zsh.

## Java, Kotlin, and the JVM

```sh
mise use --global java@temurin-25     # JDK 25 is the current LTS (Sept 2025)
mise use java@temurin-21              # per project, e.g. a course pinned to 21
mise ls-remote java | grep -E "temurin|zulu|graalvm|corretto" | tail
java -version
```

mise installs from Adoptium (Temurin), Azul (Zulu), Amazon (Corretto), GraalVM, Liberica etc. and sets `JAVA_HOME` automatically. Do **not** use Oracle's `.dmg` installer or Apple's `/usr/bin/java` stub (it just tells you to install a JDK). If a GUI app (IntelliJ, Android Studio, jEnv-style scripts) needs a system-visible JDK, install one as a Homebrew cask too (`brew install --cask temurin@21`), which registers under `/Library/Java/JavaVirtualMachines` and shows in `/usr/libexec/java_home -V`.

Build tools: **Gradle** and **Maven** via mise (`mise use gradle@latest maven@latest`) or Homebrew; **Kotlin** compiler via mise if you need `kotlinc` outside IntelliJ. IDE: **IntelliJ IDEA Community** (free) or **Ultimate** (free for students — Chapter 20). **Android Studio** (`brew install --cask android-studio`) bundles its own JDK and SDK; set `ANDROID_HOME=~/Library/Android/sdk` and add `$ANDROID_HOME/platform-tools` to PATH for `adb`. The Android emulator runs arm64 system images natively and fast on Apple silicon — pick *arm64-v8a* images, never x86.

## Go

```sh
mise use --global go@latest      # Go 1.27 (Aug 2026); mise sets GOROOT, and GOPATH defaults to ~/go
go env GOPATH GOMODCACHE
```

Add `$HOME/go/bin` to PATH for `go install`-ed tools (mise does this if you enable `go.set_gobin`). Go's toolchain directive in `go.mod` can auto-download the right version anyway (`GOTOOLCHAIN=auto`), so `brew install go` is *acceptable* for Go specifically — it's the one language whose own tooling handles versions well. Tooling: `gopls` (installed by VS Code's Go extension / Zed automatically), `golangci-lint` (`brew install golangci-lint`), `air` for live reload, `delve` for debugging (`go install github.com/go-delve/delve/cmd/dlv@latest` — needs codesigning on macOS; the VS Code extension handles it).

## Rust

```sh
mise use --global rust@stable    # or: brew install rustup && rustup-init
rustup component add rust-analyzer clippy rustfmt
cargo install cargo-watch cargo-edit cargo-nextest   # or via mise "cargo:" backend
```

Rust's own `rustup` is excellent and mise wraps it. The 2024 edition is current; `rustup update` twice a year. Apple silicon is a Tier 1 target. Linkers: the default Apple `ld` is fine; `lld` via `brew install llvm` speeds up big builds. Rust-analyzer in VS Code/Zed/RustRover (JetBrains, free for non-commercial) works out of the box.

## C and C++

Apple's **clang** from the CLT is the compiler (`gcc` is a symlink to clang; `g++` too). For a systems or compilers course that assumes GNU GCC specifically (`__attribute__` quirks, `-fanalyzer`, gcc-only sanitisers): `brew install gcc` gives `gcc-15`/`g++-15`. For a newer LLVM than Apple ships: `brew install llvm` (keg-only; add `$(brew --prefix llvm)/bin` to PATH when you want it) — it includes `clangd`, `clang-format`, `clang-tidy`, `lldb`, `lld`, and libc++ with the latest C++26 features.

Build systems: `cmake` and `ninja` (Homebrew), `meson`, `bazel`/`bazelisk`, `just` (a modern Make). Package managers: **vcpkg** or **Conan**; or Homebrew for system libs (`brew install boost fmt eigen sdl2`). Debugging: `lldb` (Apple), or `gdb` via Homebrew (**gdb needs codesigning on macOS** to attach — search "gdb codesign macOS"; most people use lldb or the IDE debugger). Sanitisers: `-fsanitize=address,undefined` works with Apple clang; ThreadSanitizer too. **Valgrind does not run on Apple silicon** — use ASan/LeakSanitizer or Instruments (Leaks/Allocations) instead; if a course *requires* Valgrind, run it in a Linux container (Chapter 13).

Headers: `xcrun --show-sdk-path` for the SDK; Homebrew packages install headers under `/opt/homebrew/include`, which clang doesn't search by default — pass `-I$(brew --prefix)/include -L$(brew --prefix)/lib` or set `CPATH`/`LIBRARY_PATH` in `.zshrc`.

IDE: VS Code + clangd extension (**not** Microsoft's C/C++ IntelliSense — clangd is faster and more accurate), CLion (free for non-commercial), Xcode for Apple-platform C/C++/Objective-C.

## Swift

Comes with Xcode/CLT (Swift 6.3 with Xcode 27). `swift package init`, `swift build`, `swift test`; Swift Package Manager is the build system. Server-side Swift (Vapor, Hummingbird) works on macOS and Linux. **swiftly** is Apple's official toolchain manager for switching Swift versions outside Xcode (`brew install swiftly`). Editors beyond Xcode: VS Code with the Swift extension (SourceKit-LSP), Zed, Neovim.

## Ruby

```sh
mise use --global ruby@3.4       # Ruby 4.0 shipped Dec 2025; 3.4 remains widely used
gem install bundler rails
```

Never use `/usr/bin/ruby` (Apple's, 2.6, for legacy scripts). mise compiles Ruby via ruby-build; `brew install openssl@3 libyaml gmp` first avoids build errors. Rails needs a database (Chapter 15) and `libvips` or `imagemagick` for Active Storage.

## PHP, .NET, others

- **PHP**: `brew install php` (8.5) or `mise use php@8.5`; **Laravel Herd** (free) bundles PHP/nginx/DNS for a zero-config local Laravel setup. Composer via Homebrew.
- **.NET**: `brew install --cask dotnet-sdk` (.NET 10 LTS; .NET 11 in November 2026) or `mise use dotnet@10`. VS Code + C# Dev Kit, or **Rider** (free for non-commercial).
- **Elixir/Erlang**: mise (`erlang@27 elixir@1.18`); `brew install wxwidgets` first for the observer.
- **Haskell**: `ghcup` (official) — `brew install ghcup` then `ghcup tui`; HLS via ghcup.
- **OCaml**: `brew install opam && opam init`.
- **Zig**: `mise use zig@latest` or `brew install zig` (Ghostty is written in it).
- **Lua**: `brew install lua luarocks`; **R**: `brew install --cask r` + Positron/RStudio; **Julia**: `brew install --cask julia` or `juliaup`.
- **Assembly / low-level courses**: Apple silicon is **AArch64**, not x86. If a course teaches x86-64 assembly, run an x86 Linux VM (UTM, Chapter 13) or use the department's servers; `nasm` and `gcc -m32` don't target this hardware. For ARM assembly, `clang -arch arm64` and `lldb` work natively — a genuine advantage.

## Machine learning on Apple silicon

Unified memory makes Macs unusually good for *running* models locally and adequate for *training* small ones; they are not a substitute for NVIDIA GPUs (CUDA) for serious training, so expect to use the university cluster or cloud for that.

- **PyTorch**: `uv add torch torchvision` — arm64 wheels with the **MPS** backend. `device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")`. Most ops are supported; set `PYTORCH_ENABLE_MPS_FALLBACK=1` for the rest.
- **MLX**: Apple's open-source array framework designed for unified memory (`uv add mlx mlx-lm`). Fastest way to run/fine-tune LLMs locally: `mlx_lm.generate --model mlx-community/Llama-3.3-8B-Instruct-4bit --prompt "…"`. macOS 26.2+ gives M5 chips full MLX access to the Neural Accelerators.
- **Core AI** (macOS 27) and the **Foundation Models framework** (macOS 26) are the Swift APIs for building apps on Apple's on-device models — relevant if you write Swift apps.
- **Local LLM runners**: **Ollama** (`brew install ollama`; `ollama run gemma3`), **LM Studio** (GUI, MLX + llama.cpp backends), **llama.cpp** (`brew install llama.cpp`). Rule of thumb: a Q4-quantised model needs roughly *parameters × 0.6 GB* of memory — 8B ≈ 5 GB, 32B ≈ 20 GB, 70B ≈ 40 GB. Keep 8 GB free for the OS.
- **Coding agents locally**: Ollama + Continue/Zed/Cursor can point at a local model; quality trails the hosted frontier models substantially in 2026, but it's free and offline.
- **Jupyter + GPU**: everything above works from a notebook. **TensorFlow** needs `tensorflow-metal`; **JAX** has `jax-metal` (experimental). **scikit-learn**, **pandas**, **polars** are all native and fast.
- Watch **Activity Monitor → GPU** and the memory pressure graph; when a model doesn't fit, macOS swaps and everything crawls.

## The 2026 release calendar (for pinning decisions)

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

## Editors know about mise

VS Code, Zed, Cursor and JetBrains detect the interpreter/runtime from the shell environment mise sets up — as long as you launch them *from a terminal* (`code .`) or have `mise activate` in `.zprofile` so GUI-launched apps inherit it. If VS Code picks the wrong Python, `⌘⇧P → Python: Select Interpreter` and choose `.venv/bin/python`. For JetBrains, add the mise-installed SDK path once (`mise where python@3.13`).
