<!--
number: 07
part: Part III — Developer environment
description: Command Line Tools vs full Xcode, xcode-select, SDKs and simulators, Rosetta 2 and the arm64-only future, and keeping Xcode from eating your disk.
-->
# Command Line Tools, Xcode & the toolchain

Every compiler, `git`, `make`, and the system SDK on macOS come from Apple's developer tools. You have two ways to get them, and the right choice depends on whether you will ever build an iOS/macOS app.

## Command Line Tools (CLT) — what almost everyone needs

```sh
xcode-select --install
```

A dialog appears; click *Install*. This downloads ~2 GB into `/Library/Developer/CommandLineTools` and gives you:

- `clang`/`clang++` (Apple's LLVM), `swift`, `swiftc`, `ld`, `lldb`
- `git` (Apple's build, usually a few months behind upstream — Homebrew's `git` will shadow it later)
- `make`, `python3` (a shim that points to the CLT's Python — do **not** use it for projects; Chapter 11), `perl`, `ruby` (system versions, also not for projects)
- headers and the macOS SDK under `…/CommandLineTools/SDKs/MacOSX.sdk`
- `otool`, `nm`, `codesign`, `xcrun`, `dsymutil`, `strip`, `install_name_tool`, `lipo`, `file`

Homebrew requires the CLT and will offer to install them if missing. Verify:

```sh
xcode-select -p          # → /Library/Developer/CommandLineTools
clang --version          # Apple clang version 17.x (Xcode 27 era)
git --version
```

**Updating**: CLT updates arrive via `System Settings → Software Update` (they're listed as "Command Line Tools for Xcode"). If Homebrew complains that the CLT are outdated or "not installed" after a macOS upgrade, the fix is always:

```sh
sudo rm -rf /Library/Developer/CommandLineTools
xcode-select --install
```

## Full Xcode — when you need it

Install Xcode if you will:

- build apps for iOS, iPadOS, macOS, watchOS, tvOS or visionOS (Swift/SwiftUI/UIKit);
- use the **iOS Simulator** (also needed by React Native, Flutter, Expo, Tauri-mobile, Capacitor);
- need **Instruments** (profiling), **Reality Composer**, **Create ML**, or Interface Builder;
- take a mobile-development or graphics/Metal course;
- run certain Homebrew formulae that need the full SDK or `xcodebuild` (rare; Homebrew tells you).

Otherwise skip it: Xcode 27 is ~4 GB to download and **~15 GB installed**, plus 8–10 GB per simulator runtime, and it makes every macOS update also an Xcode update.

**Install**: from the **Mac App Store** (simplest; auto-updates) or download the `.xip` from developer.apple.com/download (faster on slow connections; lets you keep multiple versions). Power users install via **`xcodes`** (`brew install xcodesorg/made/xcodes`) or the **Xcodes.app** GUI, which downloads, unxips and switches versions with `xcodes install 27.0` / `xcodes select 27.0`.

After installing, run it once to accept the licence and install components, or from the shell:

```sh
sudo xcodebuild -license accept
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer   # make the CLT inside Xcode the active toolchain
xcodebuild -runFirstLaunch
```

**Which toolchain is active?** `xcode-select -p` prints either the standalone CLT path or `…/Xcode.app/Contents/Developer`. With Xcode installed, point it at Xcode (as above) so `xcrun`, `swift`, and Homebrew all agree. You still keep the standalone CLT installed — that's normal.

### Xcode 27 in one paragraph

Xcode 27 (WWDC 2026, ships with macOS 27) is **Apple-silicon-only**, noticeably faster, and adds **coding agents** (agentic workflows that can plan, edit across files, generate SwiftUI views and localisations, with Apple's models or your own provider such as Claude/ChatGPT), a **Device Hub** for managing test devices, untitled projects and standalone Swift files with live previews, improved Instruments/Time Profiler, and Swift 6.3. Simulators for iOS 27 ship with it. If your course or job uses an older Xcode, keep both via `xcodes`.

### Simulators and disk space

Runtimes are the disk hog. Manage them from `Xcode → Settings → Components` or the CLI:

```sh
xcrun simctl runtime list                      # installed runtimes (each 8–10 GB)
xcrun simctl runtime delete <runtime-id>       # remove one
xcrun simctl list devices                      # simulator devices
xcrun simctl delete unavailable                # remove devices whose runtime is gone
xcrun simctl erase all                         # reset all simulators (frees data, keeps runtimes)
```

Other Xcode caches you can nuke safely (Xcode rebuilds them):

```sh
rm -rf ~/Library/Developer/Xcode/DerivedData/*          # build products, often 10–50 GB
rm -rf ~/Library/Developer/Xcode/Archives/*             # old archives (keep if you need to re-symbolicate crashes)
rm -rf ~/Library/Developer/Xcode/iOS\ DeviceSupport/*   # symbols for devices you no longer own
rm -rf ~/Library/Developer/CoreSimulator/Caches/*
rm -rf ~/Library/Caches/com.apple.dt.Xcode/*
```

`System Settings → General → Storage → Developer` exposes most of these with a delete button. **Xcode shouldn't be in your Time Machine backup** — exclude `~/Library/Developer` (Chapter 17); it's all regenerable.

### Command-line builds without opening Xcode

- `xcodebuild -list -project Foo.xcodeproj`, `xcodebuild -scheme Foo -destination 'platform=iOS Simulator,name=iPhone 17' build test`.
- `swift build`, `swift test`, `swift run` for Swift packages (no Xcode project needed — the standalone CLT suffice).
- `xcrun simctl boot "iPhone 17" && open -a Simulator` to launch a simulator from a script.
- **Fastlane** (`brew install fastlane`) for signing/TestFlight automation; **xcbeautify** for readable build logs; **SwiftLint**/**SwiftFormat**; **Tuist** or **XcodeGen** to generate projects from a manifest so `.xcodeproj` merge conflicts stop happening.

## Rosetta 2 and the arm64-only future

**Rosetta 2** translates Intel (x86_64) binaries so they run on Apple silicon. It isn't installed by default; the first time you launch an Intel app, macOS offers to install it, or you can do it yourself:

```sh
softwareupdate --install-rosetta --agree-to-license
```

The timeline you need to plan around:

| When | What happens |
|---|---|
| macOS 26.4 (Mar 2026) | Every launch of an Intel-only app shows a deprecation warning. |
| **macOS 27 (Sept 14, 2026)** | The installer **removes Rosetta** if present. You can reinstall it with the command above; it works fully through the 27.x cycle. Homebrew's Intel bottles stop being built this month. |
| **macOS 28 (fall 2027)** | Rosetta is **removed for general apps**; it survives only as a compatibility shim for a short list of old, unmaintained games that depend on Intel-only frameworks. Intel binaries — including anything under `/usr/local` from an x86 Homebrew — will not run. |

What this means for your setup:

1. **Everything you install should be arm64.** Homebrew under `/opt/homebrew` is. Download the "Apple silicon" or "Universal" build of every app; avoid "Intel" builds even when offered. Check any binary with `file /path/to/bin` (look for `arm64`) or in Activity Monitor → add the *Kind* column (Apple vs Intel).
2. **Audit now**: `find /Applications -name "*.app" -maxdepth 2 -exec sh -c 'lipo -archs "{}/Contents/MacOS/$(defaults read "{}/Contents/Info.plist" CFBundleExecutable 2>/dev/null)" 2>/dev/null | grep -q arm64 || echo "{}"' \;` lists apps without an arm64 slice. Or simply sort Activity Monitor by Kind while your usual apps are open.
3. **Delete an Intel Homebrew** if migration brought one over: `arch -x86_64 /usr/local/bin/brew bundle dump --file=~/intel-brewfile` to record what was there, then run Homebrew's official uninstall script with `arch -x86_64` and remove `/usr/local/Homebrew`. Reinstall what you need natively.
4. **Docker images**: `linux/amd64` containers run under QEMU or Rosetta *inside the Linux VM* (Docker Desktop/OrbStack use Rosetta for Linux, which is a *different* mechanism that stays supported for virtualisation). Prefer `linux/arm64` images anyway — they're faster and most official images are multi-arch (Chapter 13).
5. **Node/Python native modules**: rebuild (`npm rebuild`, `pip install --force-reinstall`) after moving from an Intel machine; `node_modules` with x86 `.node` files is the classic "works on my old Mac" bug.
6. **If you truly need x86 macOS software** (an old EDA tool, a legacy game), keep a macOS 27 partition/VM or an old Intel machine around; Golden Gate is the last stop.

Check whether you're currently under Rosetta in a terminal: `uname -m` (should print `arm64`; `x86_64` means the terminal itself is running translated — a common state after copying an Intel terminal's settings). `sysctl -n sysctl.proc_translated` prints `1` if the current process is translated.

## System languages you should *not* use for projects

macOS ships `python3` (via CLT), `perl`, `ruby`, `php` (removed in Monterey), `java` (a stub that prompts to install a JDK), `git`, `zsh`, `bash` 3.2 (2007, GPLv2-frozen), `curl`, `openssl` (actually LibreSSL), `sqlite3`, `tclsh`, `vim`, `nano`, `rsync` (Apple switched to openrsync in Sequoia). These are for the OS and for Apple's scripts. Never `pip install` into the system Python, never `gem install` into system Ruby, don't write scripts that assume bash 4+ features unless you shebang Homebrew's bash. Chapter 11 sets up proper, versioned runtimes.

## Useful Apple CLI tools you already have

| Tool | Use |
|---|---|
| `open` | `open .` (Finder here), `open -a "Visual Studio Code" file`, `open https://…`, `open -R file` (reveal), `open -e file` (TextEdit) |
| `pbcopy` / `pbpaste` | Pipe to/from the clipboard: `cat key.pub \| pbcopy`, `pbpaste > notes.txt` |
| `say` | Text-to-speech: `make && say done` |
| `defaults` | Read/write preferences (Chapter 3) |
| `mdfind` / `mdls` | Spotlight search from the shell |
| `screencapture` | `screencapture -i ~/Desktop/shot.png` (interactive), `-c` to clipboard |
| `sips` | Image resize/convert: `sips -Z 1024 *.png`, `sips -s format jpeg in.png --out out.jpg` |
| `textutil` | Convert docx/rtf/html/txt: `textutil -convert txt notes.docx` |
| `qlmanage -p file` | Quick Look from the shell |
| `caffeinate -d` / `caffeinate -i cmd` | Keep awake / while a command runs |
| `pmset -g` / `pmset -g log` | Power settings and sleep/wake history |
| `networksetup`, `airport` (gone in Sonoma — use `wdutil info`), `scutil --dns` | Network config from the shell |
| `diskutil list`, `diskutil apfs list` | Disks and APFS containers |
| `tmutil` | Time Machine (`tmutil listbackups`, `tmutil addexclusion`) |
| `system_profiler SPHardwareDataType` | Hardware info (or `sysctl -a \| grep machdep.cpu`) |
| `log show --predicate 'process == "kernel"' --last 1h` | Unified logging (Console.app's engine) |
| `launchctl` | Manage launch agents/daemons (Chapter 21) |
| `security` | Keychain from the shell: `security find-generic-password -s "svc" -w` |
| `codesign -dv --verbose=4 App.app`, `spctl -a -vv App.app` | Inspect signatures / Gatekeeper verdict |
| `xattr -l file`, `xattr -d com.apple.quarantine file` | Extended attributes; remove quarantine |
| `plutil -p file.plist` | Pretty-print property lists (`-convert xml1` to edit) |
| `osascript -e 'display notification "done"'` | AppleScript/JXA from the shell |
| `shortcuts run "Name"` | Run a Shortcut from the shell |
| `container` (Tahoe+) | Apple's Linux container CLI (Chapter 13) |

## GNU tools vs BSD tools

macOS userland is **BSD**: `sed`, `awk`, `grep`, `find`, `ls`, `date`, `stat`, `tar`, `xargs` have BSD flags, not GNU ones. `sed -i` needs an argument (`sed -i '' 's/a/b/' f`), `date -d` doesn't exist (`date -v+1d`), `ls --color` fails (`ls -G`), `readlink -f` only appeared in macOS 12.3. Scripts copied from Linux tutorials break here.

Two fixes, pick one:

- **Install GNU versions via Homebrew** (`brew install coreutils findutils gnu-sed gawk grep gnu-tar`) — they install with a `g` prefix (`gsed`, `gls`, `gdate`). To use them *unprefixed*, add the `gnubin` dirs to `PATH` in your shell config (`$(brew --prefix coreutils)/libexec/gnubin` etc.). Be aware this changes behaviour for every script on the machine, including some Homebrew formulae; many people prefer prefixed use only.
- **Write portable scripts**: use `#!/usr/bin/env bash`, avoid GNU-only flags, or use the modern Rust replacements from Chapter 9 (`fd`, `rg`, `sd`, `eza`, `bat`) that behave identically on macOS and Linux.

Homebrew's `bash` (5.x) and `zsh` are current; Apple's `/bin/bash` is stuck at 3.2 for licensing reasons and Apple's `zsh` is fine as a login shell but lags a version or two.
