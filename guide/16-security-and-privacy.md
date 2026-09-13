<!--
number: 16
part: Part IV — Security, backup & maintenance
description: A realistic threat model, FileVault and its new recovery-key rules, Gatekeeper and notarisation, the firewall, passwords and passkeys, secrets on disk, permissions hygiene, browser privacy, Lockdown Mode, and what to do when a laptop is lost.
-->
# Security & privacy

macOS is secure by default in ways Linux and Windows are not: a sealed, signed system volume; hardware-backed encryption keys in the Secure Enclave; app sandboxing and per-resource permission prompts; notarised software. The job is to *not undo* those defaults, then add the handful of things Apple leaves to you: a password manager, backups, a firewall toggle, and habits around secrets. This chapter is written for a student or engineer, not a nation-state target; the [Lockdown Mode](#lockdown-mode-and-high-risk-users) section covers the latter.

## Threat model in one paragraph

Realistic risks for a developer's Mac, in rough order of likelihood: **losing or having the laptop stolen** (FileVault + Find My + backups make this an inconvenience instead of a disaster); **phishing and credential stuffing** on your accounts (password manager + passkeys + 2FA); **malicious packages** pulled in by `npm install`/`pip install`/`brew install` from a compromised tap (supply chain — trust decisions, lockfiles, scanning); **leaking secrets** via a committed `.env` or a screenshot; **info-stealer malware** disguised as a cracked app or a fake "update" (Gatekeeper + not pirating software); and, far down the list, targeted exploits. Configure for the top five; don't cosplay for the sixth.

## FileVault

Full-disk encryption of your Data volume, keyed to your login password and the Secure Enclave. On Apple silicon the drive is *always* encrypted at the hardware level; FileVault is what ties that key to your password so a stolen SSD (or a stolen Mac booted to Recovery) is unreadable.

- **Since Tahoe it's on by default** when you sign into an Apple Account during setup. Verify: `System Settings → Privacy & Security → FileVault` shows **On**, or `fdesetup status` in a terminal.
- **The Recovery Key changed in Tahoe**: the old "store in iCloud" escrow (protected only by your Apple Account password) is gone. The key now lives in **iCloud Keychain (end-to-end encrypted)**, shows up in the **Passwords app**, and can be displayed any time from the FileVault pane via **Show** (Touch ID). Macs upgraded to 26.4+ are migrated to this model.
- **Do this now**: click *Show*, copy the 24-character key into your password manager too, and — if you don't use iCloud Keychain — write it on paper and put it somewhere physically safe. If your login password is ever lost *and* the account can't be reset via Apple Account, the Recovery Key is the **only** way to get your data.
- Verify the stored key works without wiping anything: `sudo fdesetup validaterecovery` → paste key → `true`.
- **Allow my Apple Account to reset this password** (set during setup; changeable in `Users & Groups → ⓘ`) is your other safety net. Keep it on unless you have a specific reason.
- Time Machine and other external drives are **separate**: encrypt them at format time (APFS Encrypted) — Chapter 17. Note that **encrypted HFS+ is deprecated** and unsupported from macOS 28; reformat old backup drives as APFS.
- Sleeping vs shutting down: with FileVault, a *sleeping* Mac holds the key in memory. For maximum safety when travelling, shut down (or at least lock — the Secure Enclave rate-limits guesses). `sudo pmset -a destroyfvkeyonstandby 1 hibernatemode 25` destroys the key on standby at the cost of slower wake; most people don't need this.

## Gatekeeper, notarisation and running unsigned software

Gatekeeper checks that downloaded apps are signed by a registered developer and notarised by Apple (scanned for malware). The rules tightened in Sequoia and stay tight in Tahoe/Golden Gate:

- The right-click → *Open* bypass **no longer exists**, and `spctl --master-disable` (the old "Anywhere" option) **is gone**.
- To run an unsigned or un-notarised app: double-click it (get refused), then `System Settings → Privacy & Security` → scroll to *Security* → click **Open Anyway** (within about an hour). Once.
- From the terminal: `xattr -d com.apple.quarantine /Applications/App.app` removes the quarantine flag so Gatekeeper isn't consulted. Homebrew: `brew install --cask --no-quarantine app`.
- Binaries you compile yourself aren't quarantined and run fine. Binaries you `curl` are quarantined by Safari/Chrome but *not* by `curl` itself.
- Check a signature: `codesign -dv --verbose=4 App.app`; check Gatekeeper's verdict: `spctl -a -vv App.app`. **Notarised** + **Developer ID** = normal commercial software. Ad-hoc signed = built locally.
- **XProtect** (Apple's built-in malware scanner) and **XProtect Remediator** update silently in the background (`Software Update → Install Security Responses and system files`). There is no need for third-party antivirus on a personal Mac; if you want a second opinion, **Malwarebytes** free scans on demand, and Objective-See's free tools (**KnockKnock** — what's persistent, **BlockBlock** — alerts on new persistence, **LuLu** — outbound firewall, **OverSight** — mic/camera use) are excellent and made by a respected researcher.
- **Don't install pirated apps or "activators".** In 2025–2026 the dominant Mac malware (Atomic/AMOS, Poseidon, Cuckoo, Banshee info-stealers) arrives almost exclusively via cracked software, fake app sites in search ads, and fake "update your browser/Zoom" pages, and steals Keychain, browser cookies, crypto wallets and SSH keys. It also increasingly comes as a **terminal command** the page tells you to paste ("ClickFix"). Never paste a command from a website you don't understand into Terminal.

## Firewall and network

- `System Settings → Network → Firewall`: **On**, *Stealth mode* on. It's an application firewall (allows/denies per app) and is off by default on new Macs.
- Outbound firewall (know what phones home): **LuLu** (free) or **Little Snitch** ($59; Little Snitch Mini is free). Useful on a dev machine to notice a package or IDE plugin making unexpected connections.
- `pf` is the packet filter underneath (`/etc/pf.conf`); rarely needed on a laptop.
- **Sharing**: everything off except what you use (Chapter 3). If SSH is on, key-only auth.
- **Public Wi‑Fi**: use a VPN you control (Tailscale exit node at home, or a reputable provider — Mullvad, Proton), or iCloud Private Relay for Safari. Turn off *Auto-Join* for open networks; forget the ones you won't reuse.
- **DNS**: consider encrypted DNS via a configuration profile (Cloudflare/Quad9/NextDNS provide `.mobileconfig` files); NextDNS also blocks trackers and malware domains network-wide.
- **Local network permission** prompts (`Privacy & Security → Local Network`) exist since Sequoia — deny for apps with no business scanning your LAN.

## Passwords, passkeys and 2FA

- **Pick one password manager and set it up before creating accounts**: Apple **Passwords** (free, built in, syncs via iCloud Keychain, passkeys, verification codes, shared groups, Windows/Chrome extension; Golden Gate adds automatic password changing for compromised logins), **1Password** ($3/mo; students 50% off; best for developers: SSH agent, CLI `op`, Git signing, Secrets Automation), **Bitwarden** (free tier is genuinely complete; open source; self-hostable via Vaultwarden), **Proton Pass**. Turn off the browser's built-in saving so you don't get duplicates. The Passwords app is the right default for a student fully in Apple's ecosystem; 1Password if you're a developer who wants the CLI/SSH integration.
- **Passkeys** replace passwords with a device-bound cryptographic credential that can't be phished. Enable them on every account that supports them — Apple Account, Google, GitHub, Microsoft, Amazon, PayPal, most banks, Cloudflare, Vercel — and keep passwords only as fallback. They sync via iCloud Keychain or your manager.
- **2FA**: TOTP codes in the Passwords app or 1Password (both fill them). **Hardware keys** (YubiKey 5C NFC, ~$55; get two) for GitHub, Google, Apple Account (Security Keys for Apple Account), your password manager, and cloud consoles — the strongest protection you can buy for the accounts that unlock everything else. Avoid SMS 2FA when anything else is available.
- **Apple Account**: 2FA on (mandatory), a **recovery contact** and a **recovery key** set (`Sign-In & Security → Account Recovery`), **Advanced Data Protection on**, and review *Devices* twice a year — remove Macs you sold.
- **Stolen Device Protection** (`Touch ID & Password`, MacBooks on 26.4+): requires biometrics — not the password — for sensitive changes when the Mac is away from familiar locations, with a security delay. Turn it on.
