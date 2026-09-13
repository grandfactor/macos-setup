#!/bin/zsh
# macos-defaults.sh — opinionated macOS preferences for developers (macOS 26/27, Apple silicon)
# Idempotent: safe to re-run. Review before running; every line is optional.
# Usage:  zsh scripts/macos-defaults.sh
# Companion to The macOS Setup Guide, chapter 3 (System settings) and Appendix A.

set -u
osascript -e 'tell application "System Settings" to quit' 2>/dev/null

echo "▶ General / appearance"
defaults write NSGlobalDomain AppleInterfaceStyleSwitchesAutomatically -bool true   # Auto light/dark
defaults write NSGlobalDomain AppleShowScrollBars -string "Always"
defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode -bool true          # expanded save dialog
defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode2 -bool true
defaults write NSGlobalDomain PMPrintingExpandedStateForPrint -bool true             # expanded print dialog
defaults write NSGlobalDomain NSDocumentSaveNewDocumentsToCloud -bool false          # save to disk, not iCloud, by default
defaults write NSGlobalDomain NSWindowShouldDragOnGesture -bool true                 # ctrl+cmd drag windows anywhere
defaults write NSGlobalDomain NSAutomaticWindowAnimationsEnabled -bool false
defaults write NSGlobalDomain AppleICUForce24HourTime -bool true
defaults write com.apple.menuextra.clock Show24Hour -bool true
defaults write com.apple.menuextra.clock ShowSeconds -bool false
defaults write com.apple.LaunchServices LSQuarantine -bool true                      # keep the "downloaded from" dialog (security)

echo "▶ Keyboard & text"
defaults write NSGlobalDomain KeyRepeat -int 1                     # fastest (2 = slightly saner)
defaults write NSGlobalDomain InitialKeyRepeat -int 10             # shortest delay
defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool false # hold = repeat, not accents
defaults write NSGlobalDomain AppleKeyboardUIMode -int 2           # full keyboard access (Tab through controls)
defaults write NSGlobalDomain NSAutomaticSpellingCorrectionEnabled -bool false
defaults write NSGlobalDomain NSAutomaticCapitalizationEnabled -bool false
defaults write NSGlobalDomain NSAutomaticPeriodSubstitutionEnabled -bool false
defaults write NSGlobalDomain NSAutomaticQuoteSubstitutionEnabled -bool false
defaults write NSGlobalDomain NSAutomaticDashSubstitutionEnabled -bool false
defaults write NSGlobalDomain NSAutomaticInlinePredictionEnabled -bool false
defaults write com.apple.HIToolbox AppleFnUsageType -int 0         # fn key does nothing (no emoji/dictation popup)

echo "▶ Trackpad & mouse"
defaults write com.apple.AppleMultitouchTrackpad Clicking -bool true
defaults write com.apple.driver.AppleBluetoothMultitouch.trackpad Clicking -bool true
defaults write NSGlobalDomain com.apple.mouse.tapBehavior -int 1
defaults -currentHost write NSGlobalDomain com.apple.mouse.tapBehavior -int 1
defaults write com.apple.AppleMultitouchTrackpad TrackpadThreeFingerDrag -bool true
defaults write com.apple.driver.AppleBluetoothMultitouch.trackpad TrackpadThreeFingerDrag -bool true
defaults write NSGlobalDomain com.apple.trackpad.scaling -float 2.0
defaults write NSGlobalDomain com.apple.swipescrolldirection -bool true   # "natural" scrolling; false to invert

echo "▶ Finder"
defaults write NSGlobalDomain AppleShowAllExtensions -bool true
defaults write com.apple.finder AppleShowAllFiles -bool false           # ⌘⇧. toggles anyway
defaults write com.apple.finder ShowPathbar -bool true
defaults write com.apple.finder ShowStatusBar -bool true
defaults write com.apple.finder _FXShowPosixPathInTitle -bool false
defaults write com.apple.finder FXPreferredViewStyle -string "Nlsv"     # list view
defaults write com.apple.finder FXDefaultSearchScope -string "SCcf"     # search current folder
defaults write com.apple.finder FXEnableExtensionChangeWarning -bool false
defaults write com.apple.finder _FXSortFoldersFirst -bool true
defaults write com.apple.finder NewWindowTarget -string "PfHm"          # new windows open Home
defaults write com.apple.finder NewWindowTargetPath -string "file://${HOME}/"
defaults write com.apple.finder ShowExternalHardDrivesOnDesktop -bool true
defaults write com.apple.finder ShowRemovableMediaOnDesktop -bool true
defaults write com.apple.finder WarnOnEmptyTrash -bool false
defaults write com.apple.finder QLEnableTextSelection -bool true
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true
defaults write com.apple.desktopservices DSDontWriteUSBStores -bool true
defaults write com.apple.frameworks.diskimages skip-verify -bool true
chflags nohidden ~/Library
sudo chflags nohidden /Volumes 2>/dev/null

echo "▶ Dock, Mission Control, Stage Manager"
defaults write com.apple.dock autohide -bool true
defaults write com.apple.dock autohide-delay -float 0
defaults write com.apple.dock autohide-time-modifier -float 0.15
defaults write com.apple.dock show-recents -bool false
defaults write com.apple.dock tilesize -int 40
defaults write com.apple.dock magnification -bool false
defaults write com.apple.dock minimize-to-application -bool true
defaults write com.apple.dock mineffect -string "scale"
defaults write com.apple.dock show-process-indicators -bool true
defaults write com.apple.dock mru-spaces -bool false                    # don't reorder Spaces by use
defaults write com.apple.dock expose-group-apps -bool true             # group windows in Mission Control
defaults write com.apple.dock enterMissionControlByTopWindowDrag -bool false
defaults write com.apple.WindowManager EnableStandardClickToShowDesktop -bool false  # click wallpaper: don't hide windows
defaults write com.apple.WindowManager GloballyEnabled -bool false     # Stage Manager off
defaults write com.apple.WindowManager EnableTilingByEdgeDrag -bool true
defaults write com.apple.WindowManager EnableTopTilingByEdgeDrag -bool true
defaults write com.apple.WindowManager EnableTiledWindowMargins -bool false
# Hot corners: bottom-right = lock screen (13), top-right = desktop (4); 0 = none. Modifier 0.
defaults write com.apple.dock wvous-br-corner -int 13
defaults write com.apple.dock wvous-br-modifier -int 0
defaults write com.apple.dock wvous-tr-corner -int 4
defaults write com.apple.dock wvous-tr-modifier -int 0
# Uncomment to wipe default Dock apps (then pin your own):
# defaults write com.apple.dock persistent-apps -array

echo "▶ Screenshots"
mkdir -p "$HOME/Pictures/Screenshots"
defaults write com.apple.screencapture location -string "$HOME/Pictures/Screenshots"
defaults write com.apple.screencapture type -string "png"
defaults write com.apple.screencapture disable-shadow -bool true
defaults write com.apple.screencapture include-date -bool true
defaults write com.apple.screencapture show-thumbnail -bool true

echo "▶ Safari (developer)"
defaults write com.apple.Safari IncludeDevelopMenu -bool true 2>/dev/null
defaults write com.apple.Safari WebKitDeveloperExtrasEnabledPreferenceKey -bool true 2>/dev/null
defaults write com.apple.Safari ShowFullURLInSmartSearchField -bool true 2>/dev/null
defaults write com.apple.Safari AutoOpenSafeDownloads -bool false 2>/dev/null
defaults write com.apple.Safari AutoFillPasswords -bool false 2>/dev/null   # if you use a password manager
defaults write NSGlobalDomain WebKitDeveloperExtras -bool true

echo "▶ Terminal / TextEdit / Activity Monitor"
defaults write com.apple.terminal SecureKeyboardEntry -bool true
defaults write com.apple.terminal StringEncodings -array 4                # UTF-8
defaults write com.apple.TextEdit RichText -int 0                         # plain text by default
defaults write com.apple.TextEdit PlainTextEncoding -int 4
defaults write com.apple.TextEdit PlainTextEncodingForWrite -int 4
defaults write com.apple.ActivityMonitor ShowCategory -int 0              # all processes
defaults write com.apple.ActivityMonitor IconType -int 5                  # CPU history in Dock icon
defaults write com.apple.ActivityMonitor SortColumn -string "CPUUsage"
defaults write com.apple.ActivityMonitor SortDirection -int 0

echo "▶ Software update"
defaults write com.apple.SoftwareUpdate AutomaticCheckEnabled -bool true
defaults write com.apple.SoftwareUpdate ScheduleFrequency -int 1
defaults write com.apple.SoftwareUpdate AutomaticDownload -int 1
defaults write com.apple.SoftwareUpdate CriticalUpdateInstall -int 1
defaults write com.apple.commerce AutoUpdate -bool true                   # App Store auto-update

echo "▶ Time Machine / misc"
defaults write com.apple.TimeMachine DoNotOfferNewDisksForBackup -bool true
defaults write com.apple.CrashReporter DialogType -string "none"          # don't show crash dialogs; use Console
defaults write com.apple.print.PrintingPrefs "Quit When Finished" -bool true
defaults write com.apple.ImageCapture disableHotPlug -bool true           # Photos doesn't open on iPhone plug-in
defaults write com.apple.Music userWantsPlaybackNotifications -bool false 2>/dev/null

echo "▶ Security (needs sudo; safe defaults — see chapter 16)"
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on >/dev/null
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on >/dev/null
sudo defaults write /Library/Preferences/com.apple.loginwindow GuestEnabled -bool false
sudo defaults write /Library/Preferences/com.apple.loginwindow SHOWFULLNAME -bool true   # name+password fields, not user list
sudo defaults write /Library/Preferences/com.apple.loginwindow LoginwindowText -string "Property of $(id -F). If found: <your email>"
defaults write com.apple.screensaver askForPassword -int 1
defaults write com.apple.screensaver askForPasswordDelay -int 0
sudo pmset -a destroyfvkeyonstandby 1 hibernatemode 25 2>/dev/null       # FileVault key wiped on sleep (stricter; comment out if wake is slow)

echo "▶ Applying"
for app in Dock Finder SystemUIServer cfprefsd; do killall "$app" 2>/dev/null; done
echo "Done. Some changes (keyboard repeat, trackpad, Stage Manager) need logout/login."
