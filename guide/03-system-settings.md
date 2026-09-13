<!--
number: 03
part: Part II — System & interface
description: A pane-by-pane tour of System Settings in macOS 26/27 with the developer-relevant toggles, the Liquid Glass controls, and the defaults-write equivalents for scripting.
-->
# System Settings, pane by pane

System Settings (the iOS-style app that replaced System Preferences in Ventura) has ~30 panes. Most defaults are fine. This chapter lists the settings that materially change how a developer's Mac behaves, in the order the sidebar shows them, with the `defaults write` equivalent where one exists so you can script them (Appendix A does exactly that). Skip anything you don't care about.

> [!TIP]
> Search the Settings sidebar (<kbd>⌘</kbd><kbd>F</kbd> inside the app) rather than hunting through panes. You can also jump straight to a pane from Spotlight — type "trackpad" and press Return.

## Wi‑Fi, Bluetooth, Network

- **Wi‑Fi → ⓘ next to your network → Private Wi‑Fi address**: *Rotating* is the default on public networks and fine; set to *Fixed* on your home network if you use DHCP reservations. Off breaks nothing but reduces privacy.
- **Wi‑Fi → ⓘ → Limit IP address tracking**: on (iCloud Private Relay for Safari/Mail).
- **Network → Wi‑Fi → Details → DNS**: consider `1.1.1.1`/`1.0.0.1` (Cloudflare), `9.9.9.9` (Quad9, malware-blocking) or `8.8.8.8`. Campus networks sometimes require their own DNS for internal hosts; if a lab server stops resolving, this is why.
- **Network → Firewall**: **on**. Click *Options*: *Block all incoming connections* off (breaks AirDrop/file sharing), *Automatically allow built-in software*: on, *Automatically allow downloaded signed software*: on, **Enable stealth mode**: on. The macOS firewall is application-based, not port-based; for port rules use `pf` (Chapter 16).
- **Network → VPN & Filters**: if your university or employer uses a VPN, install its profile here. Modern choices are WireGuard-based (Tailscale is excellent for reaching your home machine or a lab box — Chapter 14).
- **Bluetooth**: pair your keyboard/mouse/AirPods. In Tahoe the menu bar Bluetooth icon is inside Control Center; pin it (see below).

## Battery

- **Low Power Mode**: *Only on Battery* is a good default for students — it caps peak performance and dramatically extends lecture-day battery life. *Never* for engineers who want compiles fast on battery.
- **Charging → Optimized Battery Charging**: on.
- **Charging → Charge Limit** (macOS 26.4+): if the Mac lives on a dock most of the day, set **80%**. Lithium cells age fastest at 100% and warm; this single toggle is the best thing you can do for a 4-year battery. Toggle to 100% before a long day away.
- **Options → Prevent automatic sleeping on power adapter when the display is off**: on if you run servers/long builds on a docked laptop; otherwise off.
- **Options → Wake for network access**: *Only on Power Adapter*.
- Battery health: `System Settings → Battery → Battery Health ⓘ` shows maximum capacity and cycle count. Under 80% after 1000 cycles is the AppleCare replacement threshold.

## General

- **Software Update**: covered in Chapter 2. Everything on, including *Install Security Responses and system files* and *Background Security Improvements*.
- **Storage**: shows categories; the useful button is *Developer* → delete old Xcode caches and simulator runtimes (Chapter 7 does this from the CLI). Turn **on** *Empty Trash automatically* (30 days). Leave *Optimize Storage* and *Store in iCloud* **off** on a dev machine — you do not want macOS evicting your Documents to the cloud.
- **AirDrop & Handoff**: AirDrop *Contacts Only*; Handoff on; *iPhone Cellular Calls* on if you like the Phone app.
- **AutoFill & Passwords**: choose your password manager here (Passwords app, 1Password, Bitwarden…). Turn off duplicates — having two autofill providers is confusing.
- **Date & Time**: 24-hour time on (developers read logs). Set time zone automatically.
- **Language & Region**: *Temperature*, *Measurement system*, *First day of week* to taste. Add a second language here if you type in one. **Translation languages** download packs for Live Translation.
- **Login Items & Extensions**: this is where you'll audit what starts at login (Chapter 18). Anything you don't recognise: right-click → Show in Finder before deleting. *Extensions → File Providers / Finder / Quick Look / Sharing* lists third-party plug-ins.
- **Sharing**: everything **off** unless you need it. **Remote Login (SSH)**: on only if you SSH *into* this Mac (e.g. from your iPad or a Raspberry Pi); restrict to your user, and use keys (Chapter 9). **Screen Sharing** on only if you remote-control it. *Hostname* at the bottom — set something short like `alex-mbp` (this becomes your `.local` mDNS name and shows in the Terminal prompt).
- **Time Machine**: Chapter 17.
- **Transfer or Reset**: erase to sell; Migration Assistant lives here too.

## Accessibility

Not just for disability: several of the most useful *productivity* toggles live here.

- **Display → Reduce motion**: on if Spaces-swiping animations bother you; makes desktop switching snappier.
- **Display → Reduce transparency**: on if Liquid Glass hurts legibility. In macOS 27 prefer the **Liquid Glass slider** in Appearance (below).
- **Display → Pointer → Shake mouse pointer to locate**: on for multi-monitor setups.
- **Zoom → Use scroll gesture with modifier keys to zoom**: on, modifier <kbd>⌃</kbd>. Hold Control and two-finger scroll to zoom into any pixel — invaluable for checking UI alignment and reading small diagrams in lecture PDFs.
- **Pointer Control → Trackpad Options → Use trackpad for dragging → Three Finger Drag**: on. Move windows and select text by dragging with three fingers instead of click-and-hold. Most long-time Mac users consider this the single best hidden setting.
- **Keyboard → Full Keyboard Access**: on if you want to Tab through *every* control in dialogs (also see Keyboard → Keyboard navigation).
- **Spoken Content / Live Captions / Voice Control**: real accessibility features; also nice for proofreading essays (select text → Speech).

## Appearance

- **Appearance**: *Auto* switches Light/Dark with sunset. Dark mode is easier on the eyes for long code sessions; Light is more legible in sunlight. Many editors follow the system.
- **Accent color / Highlight color**: taste. Since Tahoe the *text highlight* colour is separate from the accent colour.
- **Liquid Glass** (Tahoe 26.1+: *Clear / Tinted*; **Golden Gate: a slider** from fully clear to fully tinted): if you find window chrome hard to read, move towards *Tinted*. This doesn't cost performance.
- **Opaque menu bar**: on if the transparent menu bar bugs you.
- **Icon & Widget Style**: *Default* (colour), *Light*, *Dark*, *Clear*, *Tinted*. Default is the most legible for quickly spotting apps in the Dock.
- **Folder Color**: system-wide folder tint; per-folder customisation is in Finder (right-click → Customize Folder).
- **Sidebar icon size**: *Small* fits more Finder sidebar items.
- **Show scroll bars**: **Always**. **Click in the scroll bar to**: *Jump to the spot that's clicked*.

## Apple Intelligence & Siri

- Toggle **Apple Intelligence** globally here. In Golden Gate this also enables **Siri AI** (the LLM assistant that lives in Spotlight and the Siri app). Requirements: any Apple silicon Mac; custom Siri voice and improved on-device dictation need M3+ and 12 GB+.
- **Siri → Keyboard shortcut**: *Hold 🌐 Space* or *Off*. Golden Gate's Spotlight ("Search or Ask") handles typed requests, so voice activation is optional.
- **Extensions → ChatGPT / other providers**: opt-in; Siri can hand off to ChatGPT. You can use it without an OpenAI account (anonymised) or sign in.
- **Privacy**: Apple Intelligence runs on-device where it can and otherwise on **Private Cloud Compute** (Apple-attested servers; in 2026 some capacity runs on Google Cloud with NVIDIA hardware under the same attestation model). If you handle confidential code or data (NDA'd employer, research data), read your employer's policy — Writing Tools on selected text sends that text to PCC. You can disable individual features (Writing Tools, Image Playground, Notification summaries) here.
- **Siri Suggestions & Privacy → Learn from this App**: turn off for apps you don't want indexed into the semantic index (e.g. a banking app).

## Control Center

Everything about the menu bar lives here.

- **Bluetooth, Wi‑Fi, Sound, Now Playing, Screen Mirroring**: *Show in Menu Bar* for the ones you toggle often; the rest stay inside Control Center. You can also **right-click any control inside Control Center → Pin to Menu Bar** (Tahoe+), and **Edit Controls** to add third-party controls.
- **Battery → Show Percentage**: on.
- **Clock options**: *Show the day of the week*, *Show date: Always*, *24-hour*, optionally *Display the time with seconds* (handy when you're timing things).
- **Spotlight**: hide the menu bar icon (you use <kbd>⌘</kbd><kbd>Space</kbd>).
- **Menu Bar Only → Automatically hide and show the menu bar**: *Never* on a laptop screen (the notch region is otherwise wasted); *In Full Screen Only* is the default.
- Reorder menu bar items by <kbd>⌘</kbd>-dragging; remove third-party ones by <kbd>⌘</kbd>-dragging out. If you have more than ~12 icons they disappear behind the notch — see *Ice* or *Bartender* in Chapter 19.

## Desktop & Dock

- **Dock size**: small. **Magnification**: off or subtle. **Position**: *Left* or *Bottom* — Left frees vertical pixels on a 16:10 laptop screen; Bottom is what muscle memory expects.
- **Minimize windows using**: *Scale effect* (faster). **Double-click a window's title bar to**: *Zoom* or *Fill*. **Minimize windows into application icon**: on.
- **Automatically hide and show the Dock**: on. Remove the show delay entirely: `defaults write com.apple.dock autohide-delay -float 0; defaults write com.apple.dock autohide-time-modifier -float 0.15; killall Dock`.
- **Show suggested and recent apps in Dock**: off.
- **Desktop & Stage Manager → Click wallpaper to reveal desktop**: *Only in Stage Manager* (otherwise every stray click on the desktop shoves your windows aside to show widgets).
- **Show items → On Desktop / In Stage Manager**: your call; a clean desktop is faster (Finder renders every icon).
- **Widgets → Show Widgets on Desktop**: off if you never look at them; they cost a little battery.
- **Default web browser**: set it here. **Default terminal** is *not* a system setting — Ghostty offers "Set as default terminal" (Chapter 9).
- **Windows → Prefer tabs when opening documents**: *Always* (Finder, Terminal, TextEdit, Preview then open new docs as tabs).
- **Windows → Tiled windows have margins**: **off** (tighter tiling; Chapter 6). **Drag windows to screen edges to tile**: on. **Drag windows to menu bar to fill screen**: on. **Hold ⌥ key while dragging windows to tile**: on.
- **Mission Control**: *Automatically rearrange Spaces based on most recent use*: **off**. *When switching to an application, switch to a Space with open windows for the application*: on. *Group windows by application*: off (shows every window in Mission Control). **Displays have separate Spaces**: on for multi-monitor.
- **Hot Corners…**: bottom-right *Lock Screen*, top-right *Mission Control*, top-left *Desktop* (reveal), bottom-left *Quick Note* or *–*. Set a modifier (hold <kbd>⌘</kbd>) if you trigger them accidentally.

## Displays

- **Resolution**: for the built-in display, *Default* is right; the "More Space" step is legible on 14"/16" Pro screens and gives a lot more code per screen at the cost of slightly smaller text. Use *Show all resolutions* (right-click a preset) if you need an exact size.
- **Refresh rate**: *ProMotion* (adaptive up to 120 Hz) on Pro. Externals: pick the highest available.
- **External display arrangement**: drag to match physical layout; drag the white menu-bar strip to the display you want as *main* (where new windows and the Dock appear).
- **Night Shift**: schedule *Sunset to Sunrise*, warmth ~50%. **True Tone**: off if you do colour-sensitive work; on for reading.
- **Advanced → Show resolutions as list**; *Allow your pointer and keyboard to move between any nearby Mac or iPad* (Universal Control).
- Text on a non-Retina external monitor looks thin because Apple removed subpixel antialiasing in Mojave. Improve it slightly with `defaults -currentHost write -g AppleFontSmoothing -int 2` (log out to apply) — or, better, buy a 4K/5K display (Chapter 1).

## Screen Saver, Lock Screen, Wallpaper

- **Lock Screen → Start Screen Saver when inactive**: 10–20 min. **Turn display off on battery**: 5 min; **on power adapter**: 15–20 min. **Require password after…**: *Immediately* (with Touch ID it's painless). **Show large clock**: on.
- **Show message when locked**: put your name + a contact email ("If found, please email …"). This is the free version of a lost-laptop recovery plan.
- **Wallpaper**: pick something dark and low-contrast if you spend the day looking at semi-transparent Liquid Glass. Dynamic wallpapers cost a trivial amount of battery.
- Screen Saver → *Show as wallpaper*: on for the animated Aerials (looks great, harmless).

## Notifications & Focus

- **Show previews**: *When Unlocked*.
- **Allow notifications when the display is sleeping / locked / mirroring**: off, off, off (don't leak Slack messages onto a projector).
- Go app by app: Slack/Teams/Discord → *Banners*, sounds off, badges on; Mail → badges only; Calendar → alerts; everything else → off. **Summarize previews** (Apple Intelligence) is fine for group chats.
- **Focus**: create a *Work* focus (allow calendar, your team chat; block social) and a *Do Not Disturb* schedule for sleep. Enable *Share across devices*. Tie **Focus filters** to apps (Safari tab group, Mail account, Calendar set). Chapter 21 automates Focus with Shortcuts.

## Sound

- **Alert volume**: low. **Play sound on startup**: your call (off for lecture halls). **Play feedback when volume is changed**: on.
- **Output**: if you use a USB DAC or dock audio, macOS remembers per-device volume. Hold <kbd>⌥</kbd> while clicking the Sound menu item to switch input/output quickly.

## Touch ID & Password

- Enrol 2–3 fingers. Enable **Use Touch ID for**: unlocking, Apple Pay, iTunes/App Store, autofill, *fast user switching*.
- **Stolen Device Protection** (MacBooks, 26.4+): on.
- **Apple Watch**: unlock and approve requests with your watch if you have one.
- Touch ID for `sudo` in Terminal is configured in `/etc/pam.d/sudo_local` — Chapter 9.

## Users & Groups

- Best practice (and what the ERNW Tahoe hardening guide recommends): a **standard** account for daily use and a separate **admin** account you never log into but authenticate as when needed. The practical cost on a single-user machine is a few extra password prompts per week; the benefit is that malware running as you can't silently gain root. Homebrew is fine in this model — install it while temporarily admin (or authenticate once), then `sudo chown -R $(whoami) /opt/homebrew`. If this is too much friction, at least *don't* enable automatic login.
- **Automatic login**: off (it's disabled anyway when FileVault is on).
- **Guest User**: off (Find My can still show a guest login screen on a locked Mac regardless).
- **Login Options** (click ⓘ): *Show password hints*: off. *Fast User Switching* menu: off unless shared.

## Internet Accounts, Game Center, iCloud, Wallet

- **iCloud → iCloud Drive → Desktop & Documents Folders**: **off** on a developer Mac unless you keep code elsewhere. On is convenient for a student who wants essays on iPad and Mac — just keep `~/Developer` outside it.
- **iCloud → Optimize Mac Storage**: off if you have ≥ 512 GB; you don't want files evicted.
- **Advanced Data Protection**: **on**. End-to-end encrypts iCloud Drive, Photos, Notes, Backups, Reminders, Messages in iCloud. Requires a recovery contact or recovery key (set both up, store the key in your password manager).
- **Access iCloud Data on the Web**: on if you use icloud.com.
- **Private Relay** (iCloud+): on for Safari; it can interfere with campus networks that require local DNS — turn off per-network if so.
- **Hide My Email**: use it for every signup that isn't a professional identity.
- **Passwords app**: Chapter 16. Turn on **Detect Compromised Passwords** and, on Golden Gate, review the **automatic password change** feature for weak/compromised logins.

## Keyboard

Covered in depth in Chapter 5. The essentials:

- **Key repeat rate**: fastest; **Delay until repeat**: shortest. Faster still via `defaults write -g KeyRepeat -int 1; defaults write -g InitialKeyRepeat -int 10` (values below the slider's minimum; log out to apply).
- **Adjust keyboard brightness in low light**: on. **Keyboard brightness → Turn keyboard backlight off after inactivity**: 1 min.
- **Press 🌐 key to**: *Do Nothing*. **Keyboard navigation**: on (Tab moves focus across all controls).
- **Text Input → Input Sources → Edit…**: *Show Input menu in menu bar* if you switch layouts; **Correct spelling automatically**: off; **Capitalize words automatically**: off; **Show inline predictive text**: off (it's distracting when coding in text fields); **Add period with double-space**: off; **Use smart quotes and dashes**: **OFF**.
- **Text Replacements**: add your email, address, and snippets like `;date` → today's date (or use a snippets tool — Chapter 19). They sync via iCloud.
- **Keyboard Shortcuts…**: see Chapter 5 for the remaps; at minimum **Modifier Keys…** → map <kbd>Caps Lock</kbd> to <kbd>⌃ Control</kbd> (or <kbd>⎋ Escape</kbd> for Vim users), and in *Mission Control* turn on <kbd>⌃</kbd><kbd>1</kbd>…<kbd>⌃</kbd><kbd>9</kbd> *Switch to Desktop N*. In *Spotlight*, check that <kbd>⌘</kbd><kbd>Space</kbd> isn't hijacked by an input-source switcher (*Input Sources → Select the previous input source* — move it to <kbd>⌃</kbd><kbd>Space</kbd> or off).
- **Dictation**: on if you use it; it's on-device and works offline. Shortcut: *Press 🌐 twice* or off.

## Trackpad & Mouse

- **Point & Click**: *Tracking speed* 7–8; *Click* Medium; *Force Click and haptic feedback* on; *Look up & data detectors*: *Tap with Three Fingers* (keeps Force-click for other uses); *Secondary click*: *Click or Tap with Two Fingers*; **Tap to click**: on.
- **Scroll & Zoom**: *Natural scrolling*: your call (on matches iPhone; off matches Windows and scroll wheels — the *Mouse* pane has an independent toggle since Tahoe, so you can have natural on trackpad and traditional on mouse). Smart zoom, rotate: on.
- **More Gestures**: *Swipe between pages*: two fingers; *Swipe between full-screen applications*: **three or four fingers** (this is how you move between Spaces — Chapter 6); *Notification Center*: two-finger swipe from right edge; *Mission Control*: swipe up with three/four fingers; **App Exposé**: swipe down (on); *Launchpad*: pinch (still works as Apps view); *Show Desktop*: spread.
- **Mouse** (Magic Mouse or third-party): *Tracking speed* high; *Scrolling speed* high; disable **mouse acceleration** if you game or want 1:1 movement: `defaults write -g com.apple.mouse.scaling -1` (log out). Logitech users: install *Logi Options+* for gesture mapping; steer clear of old *Logitech Control Center*.

## Printers, Game Controllers, Passwords, Screen Time

- **Printers & Scanners**: add your campus printer via IPP/AirPrint; most universities publish a queue URL. Nothing else to configure.
- **Screen Time**: useful for *yourself* — set *Downtime* for sleep and *App Limits* for whatever eats your evenings. It also shows honest weekly usage.

## Privacy & Security

The most important pane; Chapter 16 goes deep. Quick pass:

- **Location Services**: on; scroll down → *System Services → Details*: leave *Find My Mac*, *Time zone*, *Networking* on; *Significant locations* and *Mac analytics* off if you like.
- **Full Disk Access / Files and Folders / Accessibility / Input Monitoring / Screen & System Audio Recording / Automation**: these fill up as you install tools (terminals, window managers, Raycast, screen recorders). Review quarterly; remove anything you uninstalled. A tiling window manager or text expander will need *Accessibility*. A terminal will ask for *Full Disk Access* when you `ls ~/Library/Mail`.
- **Local Network**: apps that scan your LAN (Spotify, dev servers, Docker) ask here.
- **App Management**: allow your editor/updater (e.g. Homebrew via Terminal) to modify other apps.
- **Developer Tools**: add Terminal/Ghostty so you can run unsigned binaries you built yourself without Gatekeeper prompts.
- **Security → Allow applications from**: *App Store & Known Developers*. There is no "Anywhere" option in the UI since Sequoia, and `sudo spctl --master-disable` no longer works. To open an unsigned app: try to open it, get refused, then come back here and click **Open Anyway** (within an hour). Or remove the quarantine flag: `xattr -d com.apple.quarantine /Applications/Foo.app`. Homebrew casks can install with `--no-quarantine`.
- **FileVault**: on; Recovery Key stored.
- **Lockdown Mode**: off for everyone except journalists/activists/people with a specific adversary — it disables JIT in Safari, blocks most attachments, and breaks many dev sites.
- **Advanced… (at the bottom)**: *Log out automatically after inactivity*: off (kills long-running jobs); **Require an administrator password to access system-wide settings**: on; *Allow accessories to connect*: **Ask for New Accessories** (this is the USB data-blocker — a good default for laptops).
- **Analytics & Improvements**: off. **Apple Advertising → Personalized Ads**: off.

## Scripting these settings

Every checkbox above is stored in a `.plist` under `~/Library/Preferences` (per-user) or `/Library/Preferences` (system) and can be set with `defaults write`. Apps read them at launch, so most changes need `killall Dock`, `killall Finder`, `killall SystemUIServer` or a logout. Appendix A collects our recommended set into a single idempotent script; here is the flavour:

```sh
# Finder: show extensions, path bar, status bar, list view, hidden ~/Library
defaults write NSGlobalDomain AppleShowAllExtensions -bool true
defaults write com.apple.finder ShowPathbar -bool true
defaults write com.apple.finder ShowStatusBar -bool true
defaults write com.apple.finder FXPreferredViewStyle -string "Nlsv"
defaults write com.apple.finder FXDefaultSearchScope -string "SCcf"
defaults write com.apple.finder _FXSortFoldersFirst -bool true
chflags nohidden ~/Library

# Dock: autohide fast, no recents, small
defaults write com.apple.dock autohide -bool true
defaults write com.apple.dock autohide-delay -float 0
defaults write com.apple.dock autohide-time-modifier -float 0.15
defaults write com.apple.dock show-recents -bool false
defaults write com.apple.dock tilesize -int 40
defaults write com.apple.dock mru-spaces -bool false

# Keyboard: fast repeat, no autocorrect/smart quotes
defaults write NSGlobalDomain KeyRepeat -int 1
defaults write NSGlobalDomain InitialKeyRepeat -int 10
defaults write NSGlobalDomain NSAutomaticSpellingCorrectionEnabled -bool false
defaults write NSGlobalDomain NSAutomaticCapitalizationEnabled -bool false
defaults write NSGlobalDomain NSAutomaticPeriodSubstitutionEnabled -bool false
defaults write NSGlobalDomain NSAutomaticQuoteSubstitutionEnabled -bool false
defaults write NSGlobalDomain NSAutomaticDashSubstitutionEnabled -bool false
defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool false   # key repeat instead of accent popup

# Trackpad: tap to click, three-finger drag
defaults write com.apple.AppleMultitouchTrackpad Clicking -bool true
defaults write com.apple.AppleMultitouchTrackpad TrackpadThreeFingerDrag -bool true

# Screenshots: PNG into ~/Pictures/Screenshots, no shadow
mkdir -p ~/Pictures/Screenshots
defaults write com.apple.screencapture location -string "$HOME/Pictures/Screenshots"
defaults write com.apple.screencapture disable-shadow -bool true

# Misc: expand save/print dialogs, always show scroll bars, 24h clock
defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode -bool true
defaults write NSGlobalDomain PMPrintingExpandedStateForPrint -bool true
defaults write NSGlobalDomain AppleShowScrollBars -string "Always"
defaults write com.apple.menuextra.clock Show24Hour -bool true

killall Dock Finder SystemUIServer 2>/dev/null
```

Two cautions: (1) Apple silently renames or removes keys between releases — verify with `defaults read <domain>` after a major upgrade; a key that no longer exists is harmless but does nothing. (2) A handful of settings (Accessibility permissions, FileVault, Firewall state, Gatekeeper) *cannot* be set with `defaults` for security reasons; they need `sudo` tooling (`fdesetup`, `/usr/libexec/ApplicationFirewall/socketfilterfw`, `spctl`) or an MDM profile. Appendix A handles those separately.

To discover the key for any checkbox: run `defaults read > /tmp/before.txt`, flip the setting, `defaults read > /tmp/after.txt`, and `diff` them.
