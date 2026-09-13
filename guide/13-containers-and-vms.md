<!--
number: 13
part: Part III — Developer environment
description: Containers on macOS in 2026 — OrbStack, Docker Desktop, Colima, Podman and Apple's own `container` compared; multi-arch images; Kubernetes locally; Linux and Windows VMs with UTM, Parallels, VMware Fusion and Apple's Virtualization framework.
-->
# Containers & virtual machines

Every container on a Mac runs inside a Linux virtual machine — macOS has no Linux kernel. What differs between tools is *how many* VMs, how fast the file sharing is, how much memory sits idle, and what it costs. 2026 added a genuinely new option: Apple's own `container` tool, which runs one lightweight VM per container. This chapter picks a default, explains the trade-offs, and covers full VMs for Linux and Windows.

## The landscape in September 2026

| Tool | Model | Price | Idle cost | Compose | Kubernetes | Intel Macs | Notes |
|---|---|---|---|---|---|---|---|
| **OrbStack** | One optimised shared VM; drop-in `docker` CLI; also runs Linux "machines" | Free personal; **$8/user/mo** commercial (triggered above ~$10k/yr income from work using it; 1 licence = 5 devices) | ~400 MB, <1% CPU | ✅ | ✅ built-in | ✅ (last old-Intel build v2.2.2) | **Default recommendation.** Fastest bind mounts (virtiofs, ~3–4× Docker Desktop), instant start, memory actually released when idle, `*.orb.local` DNS for every container, menu bar UI. Closed source. |
| **Docker Desktop** | One shared VM; the official product | Free for <250 employees & <$10M revenue; Pro $9 / Team $15 / Business $24 per user/mo | 1–4 GB, 2–5% CPU | ✅ | ✅ optional | ✅ | Cross-platform (Win/Linux too); the widest ecosystem (extensions, Scout, Build Cloud); heaviest. Use if your employer pays or mandates it. |
| **Apple `container`** | **One micro-VM per container** on the Containerization framework | Free, open source (Apache 2.0) | none when idle | ❌ not yet (mid-2026) | ❌ | ❌ Apple silicon only | 1.0 stable June 2026, ~49k GitHub stars. Strong isolation, higher throughput once running, slower cold start (~0.9 s vs ~0.2 s). Needs macOS 26+. Great for single services and security-sensitive work; not yet a Compose replacement. |
| **Colima** | Lima-based VM + Docker or containerd runtime | Free, open source | ~500 MB | ✅ (with `docker-compose`) | ✅ (k3s flag) | ✅ | CLI only, minimal, scriptable (`colima start --cpu 4 --memory 8`). The purist's Docker Desktop replacement. |
| **Podman + Podman Desktop** | Daemonless engine in a VM (`podman machine`) | Free, open source (Red Hat) | ~500 MB | via `podman compose` | ✅ (kind/minikube) | ✅ | Rootless, OCI-standard, Kubernetes-flavoured (pods, `podman kube play`). Choose if your team/servers are RHEL/Fedora. |
| **Rancher Desktop** | Lima VM + containerd or moby, k3s | Free, open source (SUSE) | ~1 GB | ✅ | ✅ built-in k3s | ✅ | Best free cross-platform option with Kubernetes for mixed-OS teams. |

**Recommendation**: **OrbStack** for students and solo developers (free) and for anyone whose company will pay $8/mo. Keep the `docker` CLI you already know; everything in every tutorial works unchanged. Add **Apple `container`** as a side tool to learn and for isolated single containers; watch it for Compose support. Use **Docker Desktop** when an employer supplies a licence or you need its enterprise features. Use **Colima** if you want zero GUI.

## OrbStack setup

```sh
brew install --cask orbstack
orb                      # first run creates the VM and installs docker/kubectl CLIs into /usr/local/bin & ~/.orbstack
docker run --rm -it alpine uname -m      # aarch64 — you're native
docker context ls        # "orbstack" is default
```

Settings (menu bar → Settings): **Resources**: leave memory at *dynamic* (OrbStack grows and shrinks; cap at half your RAM if you like); **Docker → Rosetta**: on (so `linux/amd64` images run at near-native speed via Rosetta *for Linux*, which is unaffected by the macOS 28 Rosetta removal); **Network**: enable *Access container domains* so every container is reachable at `http://<container>.orb.local` with automatic HTTPS; **Kubernetes**: turn on when needed (a single-node cluster in seconds, `kubectl` context `orbstack`).

Linux machines (`orb create ubuntu`, `orb create -a amd64 debian`) give you full distros with shared home directory, `ssh`, and a `mac` command to call back into macOS. This is the easiest Linux environment on a Mac for a systems course — lighter than a VM, more complete than a container.

## Docker Desktop setup (if you use it)

`brew install --cask docker-desktop`. Settings: **Resources → Memory**: 6–8 GB on a 16–24 GB Mac (containers get *this* memory, not the host's), **CPUs**: half your cores, **Swap**: 1 GB, **Disk image size**: 64 GB+; **General**: *Use Virtualization framework* (default), *VirtioFS* file sharing (default), **Use Rosetta for x86_64/amd64 emulation on Apple Silicon**: on; **Kubernetes**: off unless used; **Software updates**: on. Quit Docker Desktop when you're not developing — it holds its memory reservation.

## Apple `container` (Tahoe+)

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

## Multi-architecture: arm64 vs amd64

Your Mac runs **linux/arm64** containers natively. Most official images (Postgres, Redis, nginx, Node, Python, Go, Debian, Ubuntu, Alpine) are multi-arch and *just work*. When an image is amd64-only (some vendor images, older internal ones), Docker/OrbStack run it under Rosetta or QEMU — slower and occasionally buggy (segfaults in JIT-heavy runtimes, `qemu: uncaught target signal`).

- Check: `docker image inspect img --format '{{.Architecture}}'` or `docker manifest inspect img`.
- Force: `docker run --platform linux/amd64 img` for a one-off; in Compose, `platform: linux/amd64` on the service.
- **Build for production servers (usually amd64) from your Mac**: `docker buildx build --platform linux/amd64,linux/arm64 -t you/app:tag --push .` — buildx uses QEMU (installed automatically) or, better, a remote/native builder. For Go/Rust, cross-compile the binary natively and copy it into a scratch image instead of emulating the compiler.
- **Dev containers and CI parity**: if your CI is amd64 and you develop arm64, pin base images by digest and run the test suite in both; native-extension packages (Python wheels, Node `.node` files) differ per arch — never copy a `node_modules` or `.venv` into an image, install inside it.

## Docker Compose patterns for local development

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

## Housekeeping

Images and build cache grow silently. Monthly:

```sh
docker system df                       # what's using space
docker system prune -a --volumes       # everything unused (asks first; volumes too — be sure)
docker builder prune                   # build cache only
docker image prune -a                  # dangling + unused images
```

OrbStack shows its total in the menu bar; Docker Desktop's VM disk image lives at `~/Library/Containers/com.docker.docker/Data/vms/0/data/Docker.raw` and only shrinks on prune. Exclude these VM images from Time Machine (Chapter 17).

## Kubernetes locally

- **OrbStack**: toggle Kubernetes in settings — a real single-node cluster, `kubectl config use-context orbstack`.
- **kind** (`brew install kind`): multi-node clusters in Docker; what most Kubernetes courses use.
- **minikube** (`brew install minikube`) with the `docker` or `vfkit` driver; **k3d** for k3s-in-Docker; **Rancher Desktop** for a GUI.
- Tools: `kubectl` (`brew install kubectl`), `k9s` (TUI), `helm`, `kubectx`/`kubens`, `stern` (multi-pod logs), `kustomize`, `skaffold`/`tilt` for dev loops. **Lens** or **Headlamp** for a desktop GUI.

## Full virtual machines

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

## Nix and reproducible dev shells

Worth a mention for the reproducibility-minded: the **Determinate Nix installer** (`curl … | sh -s -- install`) installs Nix cleanly on macOS with a separate APFS volume; `nix develop` / `devenv` / `flox` give per-project shells with pinned compilers and libraries — an alternative to both containers and mise for native development. Steep curve; enormous payoff if a whole team adopts it. Don't start here as a first-year.

## Choosing, by scenario

- **Web/backend student, coursework uses Docker**: OrbStack. Done.
- **Security or systems course, want strong isolation**: Apple `container` for individual services; UTM for full Linux.
- **Kubernetes course**: OrbStack Kubernetes or kind; `k9s`.
- **Need Windows for one course (Visual Studio, .NET Framework, Office macros)**: VMware Fusion (free) or Parallels (student price) with Windows 11 ARM.
- **x86 assembly or a kernel course**: UTM QEMU x86 VM (slow but correct) or the university's Linux servers over SSH.
- **Company policy says Docker Desktop**: Docker Desktop with Rosetta on and the memory cap set.
- **Want to test dotfiles on a fresh macOS**: `tart` macOS VM.
