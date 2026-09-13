<!--
number: 14
part: Part III — Developer environment
description: Cloud CLIs and credentials done safely, Terraform/OpenTofu, Kubernetes tooling, API clients, HTTP debugging, Tailscale for reaching your machines, and GitHub Actions locally.
-->
# Cloud, network & DevOps tooling

The tools that connect your Mac to everything that isn't your Mac: cloud accounts, clusters, APIs, remote machines, CI. The theme is **credentials never in plaintext, one tool per job, everything in the Brewfile.**

## Cloud CLIs

```sh
brew install awscli azure-cli
brew install --cask gcloud-cli            # Google Cloud SDK (cask, not formula)
brew install doctl flyctl                 # DigitalOcean, Fly.io
brew install vercel-cli netlify-cli       # or via npm through mise
brew install cloudflare-wrangler          # Cloudflare Workers/Pages (or npm)
brew install supabase/tap/supabase        # tap trust required (Homebrew 6)
brew install stripe/stripe-cli/stripe
brew install hcloud                       # Hetzner
brew install oci-cli                      # Oracle Cloud (the free tier is real)
```

### Credentials

- **AWS**: use **IAM Identity Center (SSO)** where your org has it (`aws configure sso`, then `aws sso login --profile work`) — short-lived tokens, nothing long-lived on disk. For personal accounts, create an IAM user with MFA and store the access key in `~/.aws/credentials` **encrypted via a credential process**: `aws-vault` (`brew install aws-vault`) keeps keys in the macOS Keychain and issues temporary STS credentials per shell (`aws-vault exec personal -- aws s3 ls`). Or **granted** (`brew install granted`) for fast profile switching with a browser-tab-per-account. Set `AWS_PROFILE` per project in `mise.toml`.
- **GCP**: `gcloud auth login` and `gcloud auth application-default login` (the latter is what SDKs use). Use *configurations* for multiple projects (`gcloud config configurations create work`).
- **Azure**: `az login` (browser); `az account set --subscription …`.
- **Never** paste long-lived cloud keys into `.zshrc`. If you must keep one, `security add-generic-password` into the Keychain and read it lazily, or store it in 1Password and use `op run` (Chapter 16).
- Install **git-secrets**/**gitleaks** hooks (Chapter 10) — cloud keys in public repos are harvested within minutes.

### Local emulation

**LocalStack** (AWS emulator, `brew install localstack`), **Firebase Emulator Suite**, **Azurite** (Azure Storage), **MinIO** (S3-compatible object store, `brew install minio`), **Supabase local** (`supabase start` runs Postgres+Auth+Storage in Docker), **Wrangler dev** for Cloudflare. All run fine on Apple silicon under OrbStack.

## Infrastructure as code

- **Terraform** (`brew install terraform` — note: HashiCorp's BSL licence since 2023) or **OpenTofu** (`brew install opentofu`, the open-source fork, drop-in). Pin versions per project with mise (`terraform = "1.13"` / `opentofu = "1.10"`). **tflint**, **trivy** (security scanning), **terraform-docs**, **infracost**.
- **Pulumi** (`brew install pulumi`) if you'd rather write TypeScript/Python/Go.
- **Ansible** (`uv tool install ansible` — it's Python; keep it out of the system interpreter), **Packer**, **Vagrant** (with the QEMU or Parallels provider on Apple silicon — VirtualBox doesn't work well).
- **SST**, **AWS CDK** (`npm i -g aws-cdk` via mise), **Serverless Framework**, **Cloudflare Wrangler** for app-centric deploys.

## Kubernetes and containers, remotely

Chapter 13 covers local clusters. For real ones: `kubectl` + `kubectx`/`kubens` (context switching), **k9s** (the TUI you'll live in), **helm**, **kustomize**, **stern** (tail many pods), **kubecolor**, **kube-ps1** or Starship's `kubernetes` module (shows context in the prompt — critical when you have a prod context configured), **dive** (inspect image layers), **trivy** (scan images), **skopeo**/**crane** (registry ops), **argocd**/**flux** CLIs. Keep `~/.kube/config` out of dotfiles and set `KUBECONFIG` per project if you juggle clusters. Make the prod context *hard* to use by accident: a different colour in Starship, or an alias that requires `--context`.

## HTTP, APIs and debugging

- **CLI**: `curl` (Apple's is fine; `brew install curl` for HTTP/3), **xh** or **httpie** for humane syntax, **jq**/**yq**/**fx** for output, **grpcurl** for gRPC, **websocat** for WebSockets, **hey**/**oha**/**vegeta** for load testing, **mkcert** (`brew install mkcert && mkcert -install`) for locally-trusted HTTPS certificates.
- **GUI API clients**: **Bruno** (free, open source, collections stored as plain files in your repo — the 2026 default), **Postman** (the incumbent; account required, heavy), **Insomnia**, **Hoppscotch** (web), **RapidAPI/Paw** (native Mac, one-time price), **Yaak**. For GraphQL: **Altair** or the built-in playground of your server.
- **Proxies and traffic inspection**: **Proxyman** (native Mac, best UX, free tier), **Charles**, **mitmproxy** (`brew install mitmproxy`, scriptable, CLI/web UI), **HTTP Toolkit**. Each installs a root CA into your Keychain to decrypt TLS — remove it when you're done, and never trust one on a machine you don't control. **Wireshark** (`brew install --cask wireshark`) for packet-level work; install ChmodBPF when prompted so captures don't need `sudo`.
- **Tunnels to localhost** (share a dev server, receive webhooks): **ngrok** (`brew install ngrok`), **Cloudflare Tunnel** (`cloudflared tunnel --url http://localhost:3000`, free, no account for quick tunnels), **Tailscale Funnel**, **localtunnel**, **bore**. Stripe/GitHub webhook testing: `stripe listen --forward-to localhost:3000/webhook`, `gh webhook forward`.
- **DNS**: `dog` or `doggo` (modern `dig`), `dscacheutil -q host -a name example.com` (macOS's resolver), `sudo killall -HUP mDNSResponder` to flush. `/etc/hosts` for local overrides; `dnsmasq` via Homebrew for wildcard `*.test` domains.
- **Ports**: `lsof -iTCP -sTCP:LISTEN -n -P` (what's listening), `lsof -i :3000` (who has it), `kill $(lsof -t -i :3000)`. macOS reserves nothing surprising, but **AirPlay Receiver uses port 5000 and 7000** — turn it off in `System Settings → General → AirDrop & Handoff` if your Flask/AirFlow app can't bind 5000.

## Reaching your machines: Tailscale

**Tailscale** (`brew install --cask tailscale`, free for personal use up to 100 devices/3 users) builds a WireGuard mesh between your Mac, your phone, a home server, a Raspberry Pi and cloud VMs, each with a stable `100.x.y.z` IP and a MagicDNS name (`homelab.tailnet-name.ts.net`). No port forwarding, works across NATs and campus Wi‑Fi, and gives you: `ssh homelab` from anywhere; **Tailscale SSH** (auth by identity, no keys to manage); **Serve/Funnel** to expose a local dev server to your tailnet or the public internet with automatic HTTPS; **exit nodes** (route all traffic through your home connection on sketchy Wi‑Fi); **Taildrop** file sharing. Enable *Remote Login* on the Mac you want to reach (Chapter 3) and restrict `sshd` to the Tailscale interface via ACLs. Alternatives: **ZeroTier**, **NetBird**, plain **WireGuard** (`brew install wireguard-tools`), or **Cloudflare Zero Trust** tunnels.

## Remote development

- **VS Code Remote-SSH** / **Cursor** / **Zed remote** / **JetBrains Gateway**: edit on a Linux box (university server, a cloud GPU VM, your Mac mini at home) with local UI and remote compute. Combine with Tailscale for zero-config reachability and with `tmux` on the remote so long jobs outlive the connection.
- **GitHub Codespaces**, **Gitpod/Ona**, **DevPod** (open source, any backend): full dev environments in the cloud from a `devcontainer.json`. Students get 180 core-hours/month of Codespaces free with the Student Developer Pack — a legitimate way to run x86 Linux or a beefier box than a base Air.
- **mosh** for high-latency links; **eternal terminal (et)**; **Blink**/**Termius** on iPad to SSH into the Mac.

## CI/CD from the laptop

- **act** (`brew install act`) runs GitHub Actions workflows locally in Docker/OrbStack — `act -j test` before pushing saves a lot of "fix CI" commits. arm64 runners images differ slightly from GitHub's amd64 ones; use `--container-architecture linux/amd64` when parity matters.
- **gh run watch**, **gh pr checks --watch** (Chapter 10) for the real thing.
- **pre-commit** hooks (Chapter 10) and **lefthook** (`brew install lefthook`, faster, YAML) make the laptop the first CI stage.
- **Dagger** (`brew install dagger/tap/dagger`) if you want pipelines as code that run identically locally and in CI.
- **Self-hosted runners on a Mac**: GitHub Actions and GitLab both support macOS arm64 runners — useful for iOS builds; run them as a launchd service (Chapter 21) on a Mac mini.

## Databases in the cloud, from the Mac

Connection tooling is Chapter 15; here, the credential rule: use short-lived IAM/database-proxy auth where offered (RDS IAM auth, Cloud SQL Auth Proxy `brew install cloud-sql-proxy`, Supabase/Neon branch tokens), keep connection strings in 1Password or the Keychain, and never in a committed `.env`.

## Observability & profiling tools worth having

`brew install --cask stats` (menu bar CPU/GPU/mem/net — see the Apple silicon P/E core split), `btop`, `bandwhich` (per-process bandwidth), `nettop` (built in), Instruments (in Xcode: Time Profiler, Allocations, System Trace — works on any process, not just Apple apps), `sudo powermetrics --samplers cpu_power,gpu_power` (real-time watts per cluster), `sudo fs_usage -w -f filesys <pid>` and `sudo opensnoop` (file activity), `dtrace` is mostly blocked by SIP — use `eslogger`/Endpoint Security or Instruments instead.

## Recommended "cloud dev" Brewfile fragment

```ruby
tap "hashicorp/tap", trusted: true
tap "supabase/tap", trusted: true
brew "awscli"
brew "aws-vault"
brew "granted"
brew "azure-cli"
cask "gcloud-cli"
brew "opentofu"          # or "hashicorp/tap/terraform"
brew "tflint"
brew "trivy"
brew "kubectl"
brew "kubectx"
brew "k9s"
brew "helm"
brew "stern"
brew "dive"
brew "act"
brew "lefthook"
brew "mkcert"
brew "xh"
brew "grpcurl"
brew "websocat"
brew "oha"
brew "doggo"
brew "ngrok"
brew "cloudflared"
brew "supabase/tap/supabase"
brew "localstack"
cask "tailscale"
cask "bruno"
cask "proxyman"
cask "wireshark"
```
