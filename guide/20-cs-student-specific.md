<!--
number: 20
part: Part V — Daily driving & workflows
description: What's different when the Mac is for a CS degree — free software through student programs, the course-by-course toolchain (C/C++, Java, Python, systems, ML, mobile, databases, theory), running x86 Linux and Windows when a class requires it, remote lab machines, LaTeX/Typst, note-taking, and surviving four years on one battery.
-->
# CS-student specific

Most of this guide applies to anyone who writes software. This chapter is about the parts that are specifically *university*: the free software you're entitled to, the toolchains individual courses expect, the x86 Linux machine your systems class assumes you have, the lab servers you'll SSH into at 2 AM, and the writing you'll do. It also has an honest section on the Mac's weak spots for a CS degree — there are a few — and the workarounds.

> [!IMPORTANT]
> Read your course's setup instructions *first*, then this chapter. Many CS departments publish Mac-specific notes and provide a VM image or a container. If a course says "use the lab machines" or "use our Docker image," do that; it eliminates a whole category of "works on my machine" problems at submission time.

## Free stuff: claim it in week one

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

## The course-by-course toolchain

A CS degree touches a lot of languages. The approach from [chapter 11](11-languages-and-runtimes.html) — `mise` for runtimes, `uv` for Python, Homebrew for compilers — handles all of them. Here's what each typical course expects and the Mac-specific gotchas.

### Intro programming (Python / Java)

- **Python**: `uv python install 3.13` (or whatever the course pins — check; intro courses often lag a version). Use `uv init` per assignment folder, `uv add` for packages. Never `sudo pip`. Run scripts with `uv run script.py`. If the course insists on Anaconda, install `miniforge` via brew instead (same conda, no bloat, Apple-silicon native) and `conda init zsh`.
- **Java**: `mise use -g java@21` (or 25 — current LTS is 25, most courses want 17 or 21). IntelliJ IDEA Ultimate is free (above) and is what most Java courses assume. `brew install --cask intellij-idea`. If the course uses BlueJ or Greenfoot, both have Apple-silicon builds.
- **Scratch/Snap/Racket/Scheme** (some intro courses): `brew install --cask racket`; DrRacket is fine on Apple silicon.

### C, C++, and systems programming

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

### Data structures & algorithms

Usually Java, C++, or Python; covered above. For competitive programming: `brew install gcc` for `bits/stdc++.h` (Clang lacks it; or create your own precompiled header), and use a fast judge client (**cph** extension in VS Code, or **Competitive Companion**).

### Web development

Node via `mise use -g node@24` (26 is LTS from October 2026); `pnpm` or `npm`. Everything in [chapter 11](11-languages-and-runtimes.html) applies. Browser DevTools in Chrome or Firefox. If the course uses PHP/Laravel: `brew install php composer` or Laravel Herd.

### Databases

`brew install postgresql@18` and `brew services run postgresql@18`, or a container. `sqlite3` is preinstalled. **TablePlus** (free tier) or **DBeaver** (free) for a GUI. MySQL courses: `brew install mysql` or a `mysql:9` container. Oracle: only via container (`gvenzl/oracle-free`, arm64 available). SQL Server: `mcr.microsoft.com/azure-sql-edge` or the 2025 arm64 preview in a container. See [chapter 15](15-databases-and-local-dev.html).

### Machine learning & data science

The Mac is genuinely good here up to a point.

- **Python stack**: `uv add numpy pandas scikit-learn matplotlib jupyter`. Everything is Apple-silicon native now.
- **PyTorch**: `uv add torch torchvision` — the **MPS** backend uses the GPU (`device = "mps"`). Fast enough for coursework and small models; not CUDA. Some ops still fall back to CPU (`PYTORCH_ENABLE_MPS_FALLBACK=1`).
- **JAX**: `jax-metal` plugin, experimental. **TensorFlow**: `tensorflow-metal`, maintenance mode. Prefer PyTorch on a Mac.
- **MLX** (Apple's framework): `uv add mlx mlx-lm` — the fastest way to run and fine-tune LLMs locally on Apple silicon. `mlx_lm.generate --model mlx-community/Llama-3.2-3B-Instruct-4bit --prompt "..."`.
- **Local LLMs for studying**: **Ollama** (`brew install ollama`) or **LM Studio** (cask). A 16 GB Mac runs 7–8B models comfortably; 32 GB runs 20–30B; a 70B model wants 48 GB+. See [chapter 1](01-hardware-and-buying.html) for RAM planning.
- **When you need CUDA** (a course that requires it, or a model that won't fit): Google Colab (free tier, or Pro $10 mo), Kaggle notebooks (free 30 hrs/week GPU), your department's GPU cluster (SSH + Slurm — see below), Lambda/RunPod/Vast.ai for cheap hourly rentals. The Mac becomes a thin client; **VS Code Remote-SSH** or **JupyterLab over an SSH tunnel** (`ssh -L 8888:localhost:8888 user@gpu-box`) makes it feel local.
- **Jupyter**: `uv tool install jupyterlab`, or use VS Code's notebook UI (better diffing, git integration). **Positron** (Posit's VS Code fork for data science) or **RStudio** if the course is R-heavy (`brew install --cask r rstudio`; or `mise use r`).
- **conda/Anaconda**: if a course insists, `brew install --cask miniforge`. Don't install full Anaconda — 5 GB, slow shell startup, and it hijacks `python` globally.

### Mobile development

- **iOS/Swift**: install **Xcode** from the App Store (or `xcodes` — see [chapter 7](07-command-line-tools-and-xcode.html)); it's 12+ GB, budget storage and an hour. Simulators are another 5–8 GB per iOS version. This is the one course where the Mac is *required*, not merely nice.
- **Android**: `brew install --cask android-studio`; the emulator runs arm64 Android images natively and fast on Apple silicon. Set `ANDROID_HOME` and add `platform-tools` to PATH for `adb`. Flutter: `mise use -g flutter`; React Native: Node + Watchman (`brew install watchman`) + Xcode/Android Studio.

### Theory, math, and writing-heavy courses

- **LaTeX**: `brew install --cask mactex-no-gui` (2.5 GB — the full `mactex` adds GUI apps you won't use) or **BasicTeX** (100 MB, then `tlmgr install` packages as needed). Editor: VS Code + **LaTeX Workshop**, or **TeXShop**/**TeXstudio**. **Skim** as the PDF viewer for SyncTeX. Or **Overleaf** for group projects (institutional Premium is common).
- **Typst** (`brew install typst`): compiles in milliseconds, saner syntax, `typst watch paper.typ`. Most professors accept a PDF and don't care what made it. **Tinymist** VS Code extension for live preview. Templates exist for most conference formats. Recommended for solo problem sets.
- **Markdown → PDF**: `brew install pandoc` and `pandoc notes.md -o notes.pdf` (needs a TeX engine; Typst can be the engine: `pandoc -t typst`). **Quarto** for notebooks-as-documents.
- **Diagrams**: **Excalidraw** (web / VS Code extension / Obsidian plugin) for hand-drawn style; **draw.io** (`drawio`) for formal; **Mermaid** inline in Markdown; **Graphviz** (`brew install graphviz`) for automata and graphs; **TikZ** if you're deep in LaTeX.
- **Math tools**: `brew install --cask mathpix-snipping-tool` (screenshot → LaTeX, student pricing), **SageMath** (cask), **Wolfram Engine** free for developers, **GeoGebra**, Python with `sympy`. **Lean 4** (`brew install elan-init`, then VS Code extension) if you take a formal methods course.
- **Automata/logic**: **JFLAP** (Java, works), **Logisim Evolution** (`brew install --cask logisim-evolution`), **Digital**.

### Other languages you may meet

`mise` handles Go, Rust, Ruby, Elixir, Erlang, Zig, Deno, Bun, Haskell (via `ghcup` — `mise use ghc` or `brew install ghcup`), OCaml (`brew install opam`), Prolog (`brew install swi-prolog`), Lisp (`brew install sbcl` + Emacs/SLIME or VS Code), Standard ML (`brew install smlnj`), Lua, Kotlin (`brew install kotlin` or via IntelliJ), Scala (`brew install coursier` → `cs setup`), Fortran (`brew install gcc` gives `gfortran`), Ada, COBOL — yes, `brew install gnucobol`. Nothing in a CS curriculum lacks an Apple-silicon build in 2026.

## When you need Linux

You will. The four routes, cheapest-friction first:

1. **OrbStack Linux machine** (`orb create ubuntu:24.04`) — a full Ubuntu userland sharing your Mac filesystem, starts in a second, near-native speed. `orb -m ubuntu bash` drops you in; your `~/code` is at the same path. Handles 90% of "this only works on Linux." Free for personal/student use. See [chapter 13](13-containers-and-vms.html).
2. **The course's Docker image** — `docker run -it -v "$PWD":/work course/image` and your files are inside. Exactly matches the autograder.
3. **x86-64 Linux** — for x86 assembly, Pintos, old binaries, or a course VM shipped as an `.ova`. Options: `orb create --arch amd64 ubuntu` (Rosetta-translated, surprisingly fast for compiles and gdb; you lose Rosetta on macOS 28, so prefer arm64 where possible); **UTM** (free; QEMU-based, full emulation — slow but runs anything, including that `.ova` after conversion); **VMware Fusion** (free since 2024) or **Parallels** (paid, $100 yr; student discount) both run **arm64** Linux/Windows fast but **not x86**. Full x86 emulation is 5–20× slower than native; fine for a shell and gdb, painful for builds. If a course truly needs x86 performance, use the department's Linux servers.
4. **Remote Linux** — see the next section. A `$5/mo` VPS or the lab servers is often the least-friction x86 machine you'll ever have.

> [!NOTE]
> A "Linux VM" for a CS course does not need to be Ubuntu Desktop with a GUI. Terminal-only Ubuntu Server or the OrbStack machine, with VS Code Remote-SSH or `orb` integration for editing, is faster and uses a quarter of the RAM. If you need a GUI for a specific tool, run it with X forwarding (`brew install --cask xquartz`) or in a full UTM VM.

## Windows (for the one course that needs it)

Visual Studio (not Code), .NET Framework (not modern .NET — that runs natively), MS Access, some CAD or EDA tools, and games. Options: **Windows 11 ARM** in **Parallels** (easiest; it's a licensed, supported path — Parallels downloads the ISO; student pricing available), **VMware Fusion** (free; bring your own ISO from Microsoft's site), or **UTM** (free, slower). Windows on ARM runs x86/x64 apps through its own emulation, and it's decent. A cheap alternative for occasional use: your university's **Windows virtual lab** (Citrix/AVD), or **Windows 365**. Don't dual-boot — Boot Camp doesn't exist on Apple silicon.

## Remote machines: lab servers, clusters, and cloud

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

## Version control for coursework

Everything in [chapter 10](10-dotfiles-and-git.html), plus:

- **One repo per course** (`~/code/uni/cs240/`) with a folder per assignment, or one repo per assignment if the course uses GitHub Classroom (it will create them). *Private.* Public solutions violate most academic integrity policies, and a future employer searching your GitHub won't be impressed by `hw3_final_FINAL2.py`.
- **Commit at every working state** — the autograder eating your submission, a bad `rm`, a laptop theft: all recoverable with a pushed commit.
- **`.gitignore` for the course's language** — `gh repo create --gitignore Python` or `gitignore.io`. Never commit `venv/`, `node_modules/`, `.o` files, or `.DS_Store` (the global ignore from chapter 10 handles the last one).
- **Group projects**: agree on a branch/PR flow in the first meeting, protect `main`, use Issues, use `git blame` for blame only at the retro. Use the GitHub Classroom template if provided.
- **Academic integrity and AI tools**: know your course's policy on Copilot/Cursor/ChatGPT *before* the assignment. Many intro courses ban them; many upper-level courses allow them with disclosure. Some autograders detect Copilot-style output. Disable Copilot per-workspace (`"github.copilot.enable": {"*": false}` in the course's `.vscode/settings.json`) so you don't accidentally cross a line.

## Studying on the Mac

- **Notes**: Obsidian or Apple Notes ([chapter 19](19-daily-driver-apps.html)). For lecture notes with math, Obsidian's MathJax (`$…$`) is the fastest path; **Notability**/**GoodNotes** on iPad with Sidecar/Universal Control if you handwrite.
- **Spaced repetition**: **Anki** (`brew install --cask anki`) for anything with definitions — theory courses, networking layers, complexity classes, syscalls. Free on Mac; the iOS app is $25 once.
- **Focus**: macOS **Focus modes** (Control Center) with per-Focus Home Screen/notification filtering; **Screen Time** app limits; **Cold Turkey**/**Focus** for hard blocking; **Raycast Focus** for lighter sessions. Keep Slack/Discord closed during study blocks (not just muted).
- **Reading papers**: **Zotero** + Better BibTeX plugin exports `.bib` for LaTeX/Typst; **Skim** or **Preview** for annotation; **Sioyek** (`brew install --cask sioyek`) is a keyboard-driven PDF reader designed for papers and textbooks.
- **Lecture recordings**: **IINA** at 1.5–2× with pitch correction; **Whisper** locally (`brew install whisper-cpp` or MacWhisper) for transcripts of recorded lectures — Apple silicon runs the `large-v3-turbo` model faster than real time.
- **Problem sets**: a `template/` folder with a `main.typ` or `hw.tex`, a `Makefile`, and a `README` you copy per assignment. Small thing, saves an hour a week over a semester.

## Battery and hardware, student edition

- A MacBook Air M5 or Neo makes it through a full day of lectures on battery. A 14" Pro does too; a 16" Pro is heavy in a backpack — buy it only if you're genuinely doing local ML or video.
- Enable the **80% charge limit** ([chapter 18](18-performance-and-maintenance.html)) if you mostly work at a desk; turn it off for exam weeks when you're never near an outlet.
- **Low Power Mode** on battery for note-taking days.
- Use the **USB-C charger from your phone** in lecture halls — any 20 W+ USB-C PD brick slow-charges a MacBook. Carry a compact 65–70 W GaN charger (Anker, UGREEN) rather than Apple's; it's smaller and charges the phone too.
- **AppleCare+** is worth it for a laptop that lives in a backpack for four years; accidental damage claims are $99–299 vs. a $700+ screen. Education pricing discounts it.
- **Find My** on, **Activation Lock** on (automatic with Find My), and **Stolen Device Protection** (macOS 26.4+) on. Laptop theft from libraries is common; a stolen Mac with Activation Lock is a brick for the thief. See [chapter 16](16-security-and-privacy.html).
- Back up. Your thesis is not safe on one SSD. Time Machine to a $60 external drive plus GitHub for code plus iCloud/Backblaze for documents ([chapter 17](17-backup-and-recovery.html)).

## The honest list of Mac disadvantages for CS

- **No Valgrind, flaky GDB**, x86 assembly needs emulation, no `epoll` — systems courses are where you'll notice you're not on Linux. The container/VM route fixes all of it.
- **8 GB isn't enough** for Docker + IDE + browser. If you already own an 8 GB machine, run containers on a VPS or the lab servers and keep local work light.
- **x86 Windows software** (some CAD/EDA, old lab software, anticheat games) — emulation only. A Windows PC in the lab or a cloud desktop is the workaround.
- **Rosetta ends with macOS 28** — Intel-only Mac apps and x86 containers will need alternatives by 2027–2028. For a student starting in 2026 on a 4-year degree, plan for arm64-native everything.
- **Cost** — offset by education pricing and the fact that a $600–1,100 Mac outlasts the degree.

Everything else — Unix shell, native Git, Docker performance, battery life, the display, the trackpad, the fact that your TA's demo will probably be on a Mac — favors it.
