<!--
number: 02
part: Part I — Before you start
description: Setup Assistant choices that are hard to undo, clean install vs Migration Assistant, the first 30 minutes, and getting to a known-good baseline.
-->
# First boot, Setup Assistant & migration

The first fifteen minutes with a new Mac contain three or four decisions that are annoying to reverse later: the account name, whether FileVault is on, how much you hand to iCloud, and whether you migrate an old mess onto a clean machine. This chapter walks through them in order, then gets you to a known-good baseline before you install anything.

## Before you unbox: decide these three things

1. **Clean install or migrate?** See [below](#migrate-or-start-clean). Short version: *migrate documents and settings, not applications*, unless the old Mac was set up recently and carefully.
2. **Which Apple Account?** Use your **personal** Apple Account, not a university or employer one — those get deleted when you leave, taking purchases, iCloud data and Find My with you. If the Mac is company-owned and MDM-enrolled, follow IT's instructions; the rest of this guide still applies inside the constraints they set.
3. **Short username.** Setup Assistant derives your home folder name (`/Users/<short name>`) from your full name. Pick something short, lowercase, no spaces — `alex`, not `Alexandra Kowalski`. Renaming it later is possible but fiddly, and it appears in every path you'll ever paste into a chat.

## Setup Assistant, step by step

The order below is macOS 26/27 on a new Mac; a wiped Mac is the same.

| Screen | Recommendation | Why |
|---|---|---|
| Language / Country | Your real region. | Affects date formats, keyboard, App Store country. Changeable later. |
| Accessibility | Skip unless needed. | All of it lives in System Settings → Accessibility. |
| Wi‑Fi | Join your network. | Needed for activation on Apple silicon. |
| Migration Assistant | **"Not now"** if you want a clean setup; see below. | You can run it later from `/Applications/Utilities`. |
| Sign in with your Apple Account | **Sign in.** | Enables Find My (anti-theft), iCloud Keychain (passwords, FileVault recovery key), Passwords app, Continuity. Use 2FA. |
| Create a computer account | Full name; **short username lowercase**; strong password; **"Allow my Apple Account to reset this password" — yes** unless you have a strict threat model. | The reset option is your safety net if you forget the login password; the Recovery Key covers the FileVault side. |
| Location Services | Yes. | Find My, time zone, Weather; per-app control later. |
| Analytics | Off (both toggles) unless you want to help Apple. | |
| Screen Time | Skip. | |
| Siri & Apple Intelligence | Enable if you want; Apple Intelligence downloads ~7 GB of models — fine to enable, configurable later. | On Golden Gate, Siri AI is turned on in Settings afterwards anyway. |
| **FileVault** | **On.** Since Tahoe it's on by default when signed into an Apple Account. Let it store the key in iCloud Keychain. | Full-disk encryption; Chapter 16 explains the recovery-key change. |
| Touch ID | Enrol at least two fingers. | Unlock, `sudo` (Chapter 9), password managers, App Store. |
| Apple Pay | Optional. | |
| Appearance | Auto. | Chapter 3 tunes Liquid Glass. |

When you land on the desktop: **do not start installing apps yet.** Do the baseline below first — ten minutes that save reinstalling.

## Migrate or start clean?

**Migration Assistant** (from a Time Machine backup, another Mac over Wi‑Fi/Thunderbolt, or a Windows PC) copies user accounts, applications, settings and files. It works remarkably well and is the right choice for *non-technical* users. For developers it has a downside: it faithfully copies the accumulated cruft of years — three Python installs, a `/usr/local` Homebrew from Intel days, launch agents from apps deleted in 2022, and 40 GB of `node_modules`.

| Coming from | Do this |
|---|---|
| **Brand new to Mac** (Windows/Linux/Chromebook) | Clean start. Copy documents via cloud drive or external SSD. Windows Migration Assistant is fine for photos/mail/contacts. |
| **Old Mac set up carelessly (most people)** | Clean start + selective migration: sign in to iCloud, copy `~/Documents`, `~/Pictures`, `~/Developer` from a Time Machine or external drive, reinstall apps via a Brewfile (Chapter 8). Keep the old Mac (or its backup) for a month. |
| **Old Mac with dotfiles + Brewfile** | Clean start, then `git clone` your dotfiles and `brew bundle`. This is the payoff of Chapter 10. Under an hour. |
| **Old Intel Mac** | **Do not migrate applications.** It would drag x86 binaries and an Intel Homebrew onto an arm64 machine, and Rosetta is on its way out. Migrate files only. |
| **Company laptop → company laptop** | Whatever IT says; usually Migration Assistant or MDM re-provisioning. |
| **No time this week** | Migrate everything now, do the clean start over a weekend later. Time Machine makes this safe. |

If you do run Migration Assistant, untick *Applications* and *Other files and folders* in the selection screen to get "files and settings only".

Sources, fastest to slowest: a **Time Machine drive** plugged in directly; **Mac-to-Mac over a Thunderbolt cable**; Mac-to-Mac over Wi‑Fi (hours for 500 GB). iCloud Drive with Desktop & Documents sync makes files *appear* once you sign in, but they download on demand — don't rely on it as your only copy during the switch.

## The first 30 minutes: get to a known-good baseline

Each item is expanded in later chapters; this is the checklist.

### 1. Update macOS

`System Settings → General → Software Update`. New Macs ship with an image that's weeks or months old. Install everything, reboot. Then click ⓘ next to *Automatic Updates* and turn on **all** of: *Check for updates*, *Download new updates*, *Install macOS updates*, *Install application updates from the App Store*, *Install Security Responses and system files*. Also enable **Background Security Improvements** if shown (Tahoe+). Rapid Security Responses (versions with a letter suffix like 27.0.1 (a)) are how Apple patches actively exploited bugs within days — you want them.

> [!NOTE]
> **Golden Gate day-one note.** macOS 27 releases September 14, 2026. If your Mac arrived with Tahoe 26.6, you'll be offered 27.0 as a ~15–20 GB delta update. It's fine to install on day one on a fresh machine; on a work machine with critical tools, waiting for 27.0.1 or 27.1 (2–6 weeks) is the conservative choice. Also note: **installing macOS 27 removes Rosetta 2** if it was present — it can be reinstalled (`softwareupdate --install-rosetta --agree-to-license`), but treat that as a signal to find arm64 versions of whatever needed it.

### 2. Verify FileVault and save the Recovery Key

`System Settings → Privacy & Security → FileVault` should say **On**. Click **Show** next to the Recovery Key (authenticate with Touch ID) and store the 24-character key in your password manager *as well as* letting it sit in iCloud Keychain. Chapter 16 has the details and the `fdesetup validaterecovery` check.

### 3. Find My and anti-theft

`System Settings → [Your name] → iCloud → Find My Mac`: on. On Apple silicon this also enables **Activation Lock**, so a stolen Mac can't be erased and reused. On a MacBook, also enable **Stolen Device Protection** (`System Settings → Touch ID & Password`, macOS 26.4+).

### 4. Fix the basics that annoy developers

Ten quick settings — the rest of System Settings is Chapter 3:

- `Keyboard → Key repeat rate`: fastest. `Delay until repeat`: shortest.
- `Keyboard → Press 🌐 key to`: **Do Nothing** (or Show Emoji & Symbols). Stops accidental emoji pickers.
- `Keyboard → Text Input → Edit…`: turn **off** *Correct spelling automatically*, *Capitalize words automatically*, *Add period with double-space*, and **especially** *Use smart quotes and dashes*. Smart quotes turn `"hello"` into `“hello”` in code pasted into chat, Notes and TextEdit.
- `Trackpad → Point & Click → Tap to click`: on. `Tracking speed`: 7–8 of 10. `Trackpad → More Gestures → App Exposé`: on.
- `Desktop & Dock → Automatically hide and show the Dock`: on. `Show recent applications in Dock`: off.
- `Desktop & Dock → Hot Corners…`: bottom-right → *Lock Screen*; top-right → *Mission Control*.
- `Desktop & Dock → Mission Control → Automatically rearrange Spaces based on most recent use`: **off** (predictable ⌃1–⌃9 desktops).
- `Lock Screen → Require password after screen saver begins or display is turned off`: *Immediately* or *After 1 minute*.
- `General → AirDrop & Handoff → AirDrop`: *Contacts Only*.
- `Appearance → Show scroll bars`: **Always** (wide tables and code views).

### 5. Finder sanity

Finder → `Settings` (<kbd>⌘</kbd><kbd>,</kbd>):

- *General* → New Finder windows show: **your home folder**.
- *Sidebar*: tick your home folder and *Hard disks*; **untick Recents**.
- *Advanced*: **Show all filename extensions**; **Keep folders on top** (both); *When performing a search*: **Search the Current Folder**; untick *Show warning before changing an extension*.
- In any window: `View → Show Path Bar`, `View → Show Status Bar`, `View → as List`, then `View → Show View Options → Use as Defaults`.
- Hidden files toggle: <kbd>⌘</kbd><kbd>⇧</kbd><kbd>.</kbd> — you need it for `.zshrc`, `.git`, `.env`.

### 6. Create your directory structure

Decide now where code lives; every script you write will assume it.

```sh
mkdir -p ~/Developer/{scratch,forks,school,work}
```

`~/Developer` is special: macOS gives it a hammer icon, and it's outside the cloud-synced folders. **Never put repositories inside iCloud Drive, Dropbox, OneDrive or Google Drive** — sync clients fight with Git and build tools and will eventually corrupt `.git` or upload gigabytes of `node_modules`. `~/code`, `~/src` or `~/Projects` are equally fine; avoid spaces.

### 7. Install the command-line developer tools

```sh
xcode-select --install
```

This installs `git`, `clang`, `make`, `swift` and the SDK headers (~2 GB) without the full 15 GB Xcode. Homebrew needs it. Full Xcode is only for iOS/macOS app development — Chapter 7.

### 8. Sign in where it matters

- App Store (for Xcode and Apple-signed apps; `mas` in your Brewfile uses it).
- Your password manager — Chapter 16. **Set it up before creating any new accounts**; you'll create dozens of developer-service accounts this month.
- Campus Wi‑Fi (802.1X profiles install from your university's onboarding page).

### 9. Take a snapshot

Plug in your Time Machine SSD and let it do the first backup (Chapter 17). If the next hours of installing go wrong, you can revert to a clean macOS in fifteen minutes.

## The macOS filesystem for developers

A quick map so the rest of the guide makes sense.

| Path | What lives there | Notes |
|---|---|---|
| `/System`, `/usr`, `/bin`, `/sbin` | The **sealed system volume**: read-only, cryptographically signed. | You *cannot* write here even as root (SIP). Use Homebrew's prefix instead. |
| `/Library` | System-wide settings, launch daemons, fonts, Application Support for all users. | Needs admin. |
| `/Applications` | Apps for all users. Homebrew casks install here. | |
| `/opt/homebrew` | **Homebrew on Apple silicon** (`bin/`, `Cellar/`, `Caskroom/`). | `/usr/local` is the *Intel* prefix — its presence on an arm64 Mac means someone installed x86 Homebrew under Rosetta. |
| `~` (`/Users/<you>`) | `Desktop`, `Documents`, `Downloads`, `Library`, `Movies`, `Music`, `Pictures`, `Public`, `Developer`. | |
| `~/Library` | Your app settings (`Preferences/*.plist`), `Caches`, `Application Support`, `LaunchAgents`, `Containers` (sandboxed apps), `Mobile Documents` (iCloud Drive), `Keychains`. | Hidden by default. |
| `~/.config`, `~/.local`, `~/.cache` | XDG directories used by modern CLI tools (Ghostty, mise, starship, nvim, gh…). | Chapter 10 puts these under version control. |
| `/private/etc`, `/private/var`, `/private/tmp` | Unix config, variable data, temp; `/etc`, `/var`, `/tmp` are symlinks to them. | `/etc/zshrc`, `/etc/paths`, `/etc/hosts`, `/etc/ssh/` live here. |
| `/Volumes` | Mounted disks, DMGs, network shares. | Your boot volume is `/` and also `/Volumes/Macintosh HD`. |
| `/Applications/Utilities` | Terminal, Activity Monitor, Disk Utility, Console, Migration Assistant, Screen Sharing… | |

Two Apple-silicon concepts worth knowing on day one:

- **APFS volume group**: your disk is one APFS container holding a sealed *System* volume, a *Data* volume (mounted at `/System/Volumes/Data` and firmlinked into the tree so it looks like one filesystem), *Preboot*, *Recovery* and *VM* (swap). Snapshots are cheap, which is how Time Machine local snapshots and macOS updates roll back.
- **Recovery**: shut down, then *press and hold the power button* until "Loading startup options" appears → *Options*. From there: reinstall macOS, restore from Time Machine, Disk Utility, **Startup Security Utility** (needed for kernel extensions and some tiling window managers — Chapter 6), Terminal. There is no <kbd>⌘</kbd><kbd>R</kbd> on Apple silicon.

## Erasing and reinstalling

`System Settings → General → Transfer or Reset → Erase All Content and Settings` wipes the Data volume, removes your Apple Account and Activation Lock, and returns to Setup Assistant in ~5 minutes *without* reinstalling macOS. It's the right way to sell a Mac and the fastest way to restart a botched setup. For a fully fresh OS image, use Recovery → Reinstall macOS, or restore the Mac from another Mac via Finder/Apple Configurator with an IPSW (DFU mode) — the nuclear option for a Mac that won't boot.

## Common first-week problems

- **"Your system has run out of application memory" / beach-balling on 8–16 GB**: check Activity Monitor → Memory → *Memory Pressure*. Close Chrome tabs, quit idle Electron apps. Revisit Chapter 1's memory table before Apple's 14-day return window closes.
- **Battery draining fast for two days**: Spotlight indexing, Photos analysis and Apple Intelligence model downloads run flat out after setup. It settles.
- **A dialog asks for a password you don't recognise**: usually your *login* password (for Keychain), not your Apple Account password. If a *former owner's* Apple Account is requested, the Mac has Activation Lock — return it.
- **Migration brought over an Intel Homebrew** (`/usr/local/bin/brew` exists; `brew config` shows `Rosetta 2: true`): uninstall it (Chapter 8) and install fresh under `/opt/homebrew`.
- **Can't find Launchpad**: removed in Tahoe. <kbd>⌘</kbd><kbd>Space</kbd> then <kbd>⌘</kbd><kbd>1</kbd> shows the Apps grid (Chapter 4), or pinch with four fingers on the trackpad.
