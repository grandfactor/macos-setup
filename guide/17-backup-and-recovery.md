<!--
number: 17
part: Part IV — Security, backup & maintenance
description: The 3-2-1 strategy on a Mac — Time Machine done right (encrypted APFS, exclusions), a second local copy, cloud backup, what iCloud is and isn't, testing restores, and recovering a Mac that won't boot.
-->
# Backup & recovery

A developer's Mac holds three kinds of data: **code** (should already be on a Git remote), **documents and media** (irreplaceable), and **configuration** (your dotfiles repo). The goal is to make losing the laptop — to theft, a spilled coffee, a failed SSD, a bad `rm -rf`, or ransomware — cost you an afternoon instead of a semester. The industry rule is **3-2-1**: three copies, on two different media, one off-site. On a Mac that's cheap and mostly automatic.

## The plan

| Copy | Tool | Cost | Protects against |
|---|---|---|---|
| 1. The Mac itself | — | — | — |
| 2. **Local, versioned** | **Time Machine** to an encrypted external SSD (or a NAS) | $100–$180 once | Deleted/overwritten files, bad updates, dead SSD, "I need the version from Tuesday" |
| 3. **Off-site, continuous** | **Backblaze** (or iCloud Drive for documents + Git for code) | $9/mo, or $0 with iCloud+Git | Theft, fire, both copies in the same bag |
| Bonus | **Git remotes** for code, **dotfiles repo** for config, **password manager** for secrets | free | The stuff Time Machine restores slowest |

Time Machine + Backblaze is the standard answer and costs about the same as one coffee a month. Students on a budget: Time Machine + iCloud Drive (200 GB for $2.99) for documents + GitHub for code covers the important 95%.

## Time Machine, done right

### The drive

- **Size**: at least equal to your Mac's internal storage; 2× is comfortable (Time Machine keeps hourly/daily/weekly versions until the drive fills, then prunes oldest). A **2 TB USB‑C/USB4 SSD** (Samsung T7/T9, SanDisk Extreme, Crucial X9/X10, or an NVMe stick in an enclosure) is the sweet spot at $130–$180; spinning disks work but are slow and fragile.
- **Format**: Time Machine wants **APFS** (Case-sensitive is fine; encrypted is what you want). Erase in Disk Utility: *View → Show All Devices*, select the **device** (not the volume), *Erase*, Scheme **GUID Partition Map**, Format **APFS (Encrypted)**, choose a strong passphrase and **save it in your password manager** — an encrypted backup you can't unlock is a paperweight.
- Since Tahoe 26.6, **encrypted HFS+ (CoreStorage) is deprecated and will not be supported in macOS 28**. If your old Time Machine drive is HFS+, back up elsewhere, erase it as APFS Encrypted, and start fresh.

### Setup

`System Settings → General → Time Machine → Add Backup Disk…`, pick the drive, **Encrypt Backup** on if you didn't format it encrypted. Then **Options…**:

- **Back up frequency**: *Automatically every hour* (default). Time Machine also keeps **local snapshots** on your internal disk when the drive isn't connected, so laptop users still get hourly point-in-time recovery (`tmutil listlocalsnapshots /`).
- **Exclude** (click **+**): things that are large, regenerable, or already backed up elsewhere:

```
~/Library/Developer                # Xcode DerivedData, simulators (tens of GB, regenerable)
~/Library/Caches
~/Library/Containers/com.docker.docker   # Docker Desktop VM disk
~/.orbstack                        # OrbStack VM data (or ~/OrbStack)
~/.cache
~/.local/share/mise                # runtimes: reinstall with `mise install`
~/.npm  ~/.pnpm-store  ~/.cargo/registry  ~/go/pkg  ~/.gradle  ~/.m2  ~/.cache/uv
~/Library/Application Support/Google/Chrome/Default/Service Worker
~/Library/Application Support/Code/CachedData   (and Cursor, JetBrains caches)
~/VirtualMachines  ~/Library/Containers/com.utmapp.UTM   # VM images — back up separately if you care
~/Downloads                        # opinion: yes, exclude; nothing that matters should live there
node_modules directories           # can't be excluded by pattern in the UI; use tmutil (below) or keep code in Git
```

From the shell, `tmutil addexclusion -p /path` excludes a path permanently (the `-p` flag makes it a *fixed-path* exclusion rather than one that follows the file). For `node_modules`/`.venv`/`target` everywhere: a script that walks `~/Developer` and calls `tmutil addexclusion` (without `-p`, so it sticks to the directory) on each — or accept the bloat; APFS-to-APFS backups are fast.

- **Back up while on battery power**: on for laptops.
- **Show Time Machine in menu bar** (Control Center → Time Machine): yes — you can trigger *Back Up Now* and see status.

### Using it

- **Restore a file**: open the folder in Finder, then Time Machine menu → *Browse Time Machine Backups*; step back in time, *Restore*. Works inside Mail, Notes and other apps that support it too.
- **Restore everything**: Migration Assistant on a new/wiped Mac (choose the Time Machine disk) — this is how a lost laptop becomes a Tuesday afternoon.
- **Restore macOS + everything**: Recovery → *Restore from Time Machine*.
- `tmutil listbackups`, `tmutil latestbackup`, `tmutil compare` (what changed), `tmutil thinlocalsnapshots / 50000000000 4` (free 50 GB of local snapshots if "System Data" is huge), `tmutil startbackup --block`.
- **NAS / network**: Time Machine over SMB to a Synology/QNAP/TrueNAS/another Mac works well (Golden Gate improved SMB browsing speed). Set a quota on the share so it can't eat the NAS. Wireless backups are slow for the first run — do it over Ethernet.
- **Multiple drives**: Time Machine rotates between them (one at home, one at the office/parents' house = an off-site copy for free).

### Time Machine's limits

It's not bootable (no bootable backups on Apple silicon — see below), it doesn't back up the VM images you excluded, it can't do bare-metal restore faster than Migration Assistant, and its consistency for open databases (Postgres data dir, VM disks) is file-level, not snapshot-consistent — dump databases separately if they matter.

## A second local copy: clones

**Carbon Copy Cloner** ($50) or **SuperDuper!** ($28) make a complete, browsable copy of your Data volume to another drive on a schedule, with snapshots and a "SafetyNet" for changed files. Since Big Sur, **bootable clones are effectively dead on Apple silicon** — the sealed system volume can only be laid down by Apple's installer; CCC can still attempt it but the developer explicitly recommends a *standard* (data-only) backup plus reinstalling macOS from Recovery, which takes 15 minutes. Do you need CCC if you have Time Machine? Only if you want a second, independent, faster-to-browse local copy, or a scheduled sync of specific folders (e.g. your photo library to a NAS). Nice to have, not required.

For raw folder syncs, `rsync -avh --delete --progress ~/Documents/ /Volumes/Backup/Documents/` (install Homebrew's `rsync`) in a `launchd` job (Chapter 21) is free and dependable.

## Off-site: cloud backup

- **Backblaze Personal Backup** ($9/mo or $99/yr, unlimited, per computer): installs a small agent, backs up *everything* on the internal drive and attached externals (you exclude what you don't want), versions for 30 days (1 year for $2/mo more), restores via web download or a mailed USB drive. Exclude the same caches/VMs as Time Machine. It's the set-and-forget answer for photos, documents, and everything you'd cry over. Set a **private encryption key** (Backblaze can't decrypt; if you lose it, so is your backup).
- **Arq** ($50 one-time + your own storage: Backblaze B2, S3, Google Drive, OneDrive, SFTP, another Mac): client-side encrypted, hourly, versioned, very configurable. The power user's choice; B2 costs ~$6/TB/month.
- **restic** / **Kopia** (free, open source, CLI or Kopia's GUI): encrypted, deduplicated, to any cloud or an SFTP server. Great if you already have a homelab or an S3 bucket and enjoy `launchd` plists.
- **iCloud Drive** with *Desktop & Documents* sync is **sync, not backup**: deleting a file deletes it everywhere (recoverable for 30 days in *Recently Deleted*), and ransomware or a bug syncs too. It's still far better than nothing for documents and pairs well with iCloud+ 200 GB/2 TB plans and Advanced Data Protection. **Do not put code repos in iCloud Drive** (Chapter 2).
- **Photos**: iCloud Photos is the natural place; keep *Download Originals to this Mac* on so the library exists locally and gets Time Machined/Backblazed too — otherwise your only copy is Apple's.

## What about code and config?

- **Code**: every repo has a remote; `git status` clean at the end of the day; unpushed branches are the only exposure. `gh repo list --limit 200` shows what's on GitHub; a monthly `for d in ~/Developer/*/; do (cd "$d" && git status -sb | head -1); done` surfaces repos with no remote or unpushed work.
- **Configuration**: the dotfiles repo (Chapter 10) plus the Brewfile. A fresh Mac becomes yours in 20 minutes — that's your real disaster-recovery plan for the *environment*.
- **Secrets**: the password manager (synced, encrypted) holds the FileVault key, backup drive passphrase, 2FA recovery codes, SSH key passphrases and cloud credentials. **Print the emergency kit / recovery codes** and put them with your passport.
- **Databases**: `pg_dump`/`mysqldump` into a folder Time Machine sees, or accept that local dev data is disposable (it usually is).

## Test the restore

A backup you've never restored from is a hypothesis. Twice a year:

1. Pick a file you edited last week; restore Tuesday's version via Time Machine. Did it work? Was the drive's passphrase where you thought?
2. Log into Backblaze/Arq and download one folder.
3. Boot to Recovery once so you know what it looks like (hold the power button → Options).
4. Optional but recommended once: restore your whole Time Machine backup into a `tart`/UTM macOS VM, or onto a spare Mac, to see that Migration Assistant actually brings back what you expect.

## Recovery: when the Mac won't boot or you need to reinstall

Apple silicon boot options — **shut down, then press and hold the power button** until "Loading startup options":

- **Options → Recovery**: *Restore from Time Machine*, *Reinstall macOS* (keeps your data; fixes a corrupted system), *Safari* (read this guide), *Disk Utility* (First Aid, erase), *Utilities → Terminal*, *Startup Security Utility* (security policy — needed for kexts/yabai), *Share Disk* (mount your Mac's drive on another Mac over USB-C to pull files off — the modern Target Disk Mode).
- **Safe Mode**: hold <kbd>⇧</kbd> while selecting your startup disk in the options screen → *Continue in Safe Mode*. Loads no third-party kexts/login items; clears caches. First thing to try for boot loops or kernel panics after installing something.
- **Fallback recoveryOS**: if Recovery itself is damaged, double-press-and-hold the power button.
- **DFU restore / revive** (bricked Mac, failed firmware update): connect to another Mac with a USB-C cable, use **Finder** (Sequoia+) or **Apple Configurator** → *Revive* (keeps data) or *Restore* (wipes). The IPSW downloads automatically. This is the nuclear option that fixes almost anything short of hardware failure.
- **Erase All Content and Settings** (from a working macOS: `System Settings → General → Transfer or Reset`) is the fast clean-slate: 5 minutes, keeps macOS installed, removes your data and Activation Lock. Then Migration Assistant from Time Machine.

Things that look like disasters but aren't: a **"System Data" category eating 100+ GB** is usually Time Machine local snapshots (`tmutil thinlocalsnapshots`), Xcode caches, or container VM images; a **forgotten login password** is fixed with your Apple Account or the FileVault Recovery Key at the login screen (click *?* or wait for the *Reset* option after three tries); a **spinning wheel at boot after an update** often just needs 20 minutes.

## The minimum viable backup (if you do nothing else)

1. Buy a 2 TB SSD, format APFS Encrypted, plug it in, click *Use as Backup Disk*, save the passphrase in your password manager. Leave it plugged in whenever you're at your desk.
2. Turn on iCloud Photos with originals downloaded, and iCloud Drive for Documents.
3. Push your code. Every day.
4. Put the FileVault Recovery Key and the drive passphrase in the password manager, and print the password manager's emergency kit.

That's an hour of work and it makes a dead laptop a shopping trip, not a tragedy.
