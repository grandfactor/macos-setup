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

## Secrets on disk (the developer part)

Where things live and how to keep them from leaking:

| Secret | Where it should be | Where it should *not* be |
|---|---|---|
| SSH private keys | `~/.ssh/` with a passphrase in the Keychain (`UseKeychain`), or a hardware key, or 1Password's agent | Copied between machines; in Dropbox/iCloud Drive; in a repo |
| Git signing key | Same SSH key (Chapter 10) | A GPG keyring you'll lose the passphrase to |
| API tokens, cloud keys | 1Password (`op run`, `op read`), macOS Keychain (`security add-generic-password`), `aws-vault`, `mise`/`direnv` loading a **gitignored** `.env` | `~/.zshrc`, `~/.npmrc`, `~/.netrc`, committed `.env`, a Slack message |
| Database passwords (prod) | Your cloud's secret manager / 1Password | Local `.env`, a GUI client's saved connection without Keychain |
| Browser cookies/sessions | The browser (they're the #1 target of info-stealers) | Exported HAR files in Downloads |
| Backups of any of the above | Encrypted Time Machine / encrypted disk image | Unencrypted USB sticks |

Tools: `gitleaks` pre-commit hook (Chapter 10); `op` CLI with biometric unlock; **sops**/**age** (`brew install sops age`) for encrypted config files in repos; the Keychain from scripts:

```sh
security add-generic-password -a "$USER" -s openai_api_key -w      # prompts for the value
export OPENAI_API_KEY="$(security find-generic-password -a "$USER" -s openai_api_key -w)"
```

`~/Library/Keychains/login.keychain-db` is encrypted with your login password and included in FileVault and Time Machine — fine. iCloud Keychain syncs it end-to-end encrypted.

## Permissions (TCC) hygiene

Every "X would like to access Y" dialog writes to the TCC database. Review quarterly in `Privacy & Security`:

- **Full Disk Access**: terminals, backup tools, maybe your editor. Anything else — why?
- **Accessibility**: window managers, Karabiner, Raycast/Alfred, text expanders, AltTab. This permission is powerful (it can read and synthesise all input); grant it only to well-known apps.
- **Screen & System Audio Recording**: screenshot tools, video calls, DisplayLink. macOS periodically re-asks for less-used apps.
- **Input Monitoring**: Karabiner, keyboard utilities.
- **Automation** (AppleScript control between apps), **Camera/Microphone**, **Files and Folders**, **Local Network**, **Developer Tools**.
- `tccutil reset All com.example.app` clears an app's grants if a dialog got stuck.
- macOS 26.2+ shows which permissions were granted by an MDM profile (relevant on work Macs); macOS 27 denies apps access to other teams' app containers by default.

## Browser privacy

- **Safari** has the strongest default anti-tracking (ITP, fingerprinting protection strengthened in 26.4, Private Relay, Hide My Email) and the best battery life. Enable *Advanced Tracking and Fingerprinting Protection: in all browsing*, *Prevent cross-site tracking*, *Hide IP address from trackers*. Extensions from the App Store only: **AdGuard** or **Wipr 2** (content blockers), your password manager, **Kagi**. Golden Gate's Safari adds AI tab grouping and page-change alerts; the *Create an Extension* AI feature is fun for small tweaks.
- **Chrome** if you need it (DevTools, Google Workspace, Chrome-only sites): sign out of sync unless you want Google to have your history, turn off *Privacy Sandbox* ad topics, install **uBlock Origin Lite** (MV3) — uBlock Origin proper is Firefox-only now. **Brave** is Chromium with a built-in blocker and no Google account hooks. **Firefox** for uBlock Origin and container tabs; **Zen** is Firefox with Arc's vertical-tab workflow (Arc itself is frozen since 2025 — security patches only). **Orion** (Kagi) is a WebKit browser that runs Chrome *and* Firefox extensions.
- **Two browsers, two identities**: personal in Safari, work/Google in Chrome or a dedicated profile. Browser profiles keep cookies, extensions and history separate — and limit what a malicious extension in one can see.
- **Extensions are the biggest browser risk**: each one you install can read every page. Keep them to a handful from reputable authors.

## Updates

`Software Update`: everything automatic, including **Security Responses and system files** and **Background Security Improvements**. Rapid Security Responses ship within days of an exploited zero-day. App updates: Homebrew (`brew upgrade`) weekly, App Store automatic, and let apps that self-update (browsers, editors, Slack) do so. An out-of-date browser is the most likely way in.

## Lockdown Mode and high-risk users

`Privacy & Security → Lockdown Mode` disables JIT and many web technologies in Safari, blocks most message attachments and link previews, refuses wired accessories while locked, and prevents configuration-profile installs. It's for journalists, activists, dissidents, executives, and security researchers who have reason to believe a well-resourced adversary is targeting them personally. It breaks enough normal developer web tooling that it's the wrong default for everyone else. If that's you: enable it, use a hardware security key on your Apple Account, consider a separate device for sensitive work, and read Apple's Platform Security Guide and the ERNW macOS 26 hardening guide (Appendix E) — they cover MDM-level restrictions this guide skips.

## The admin vs standard account question

Running day-to-day as a **standard user** and keeping a separate admin account means anything that runs as you cannot silently install system-wide persistence or change security settings without an admin password prompt. It's the single most effective *free* hardening step and what enterprise baselines require. The friction on a personal Mac is small — occasional extra prompts for installers, `sudo` requires the admin's credentials — and Homebrew works fine once `/opt/homebrew` is owned by your standard account. Reasonable people skip it on a personal laptop; do it on a machine that has access to production systems.

## When the Mac is lost or stolen

Before it happens: FileVault on, Find My on, Stolen Device Protection on, a lock-screen message with contact details, backups current, and your Apple Account recovery set up.

When it happens: **icloud.com/find** (or Find My on another device) → the Mac → **Mark As Lost** (locks it and shows your message; Activation Lock means it can't be erased and reused) → if it's clearly gone, **Erase This Mac**. Then: change your Apple Account password, revoke the machine's SSH keys on GitHub/servers, rotate any tokens that lived in plaintext on disk (there should be none — see above), sign out sessions in Google/GitHub/Slack (each has a "sign out everywhere"), and notify your employer's IT if it had work data. Your data is unreadable without your password; your Time Machine backup restores everything onto the replacement.

## Quick audit script

Paste into a terminal for a snapshot of the security posture (read-only):

```sh
echo "FileVault:      $(fdesetup status)"
echo "Firewall:       $(/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate)"
echo "Stealth:        $(/usr/libexec/ApplicationFirewall/socketfilterfw --getstealthmode)"
echo "Gatekeeper:     $(spctl --status)"
echo "SIP:            $(csrutil status)"
echo "Auto login:     $(defaults read /Library/Preferences/com.apple.loginwindow autoLoginUser 2>/dev/null || echo off)"
echo "Remote login:   $(systemsetup -getremotelogin 2>/dev/null)"
echo "Auto updates:   $(defaults read /Library/Preferences/com.apple.SoftwareUpdate AutomaticallyInstallMacOSUpdates 2>/dev/null) (1=on)"
echo "Listening TCP:"; lsof -iTCP -sTCP:LISTEN -n -P | awk 'NR>1{print "   "$1, $9}' | sort -u
echo "Login items:"; osascript -e 'tell application "System Events" to get the name of every login item' 2>/dev/null
echo "LaunchAgents:"; ls ~/Library/LaunchAgents /Library/LaunchAgents 2>/dev/null
```

Expected on a well-set-up Mac: FileVault On, Firewall enabled, stealth on, assessments enabled, SIP enabled, no autologin, remote login off (unless you need it), only local (`127.0.0.1`) listeners, and login items you recognise.
