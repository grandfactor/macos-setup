#!/bin/zsh
# audit.sh — quick security & health check (chapter 16, 18). Read-only; prints ✅/⚠️ per item.
ok()   { print -P "%F{green}✅%f $1"; }
warn() { print -P "%F{yellow}⚠️ %f $1"; }

[[ $(fdesetup status) == *"On"* ]]                          && ok "FileVault on"          || warn "FileVault OFF — System Settings → Privacy & Security"
[[ $(/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate) == *enabled* ]] && ok "Firewall on" || warn "Firewall off"
[[ $(spctl --status 2>&1) == *enabled* ]]                   && ok "Gatekeeper enabled"    || warn "Gatekeeper disabled"
[[ $(csrutil status) == *enabled* ]]                        && ok "SIP enabled"           || warn "SIP disabled"
[[ $(defaults read com.apple.screensaver askForPassword 2>/dev/null) == 1 ]] && ok "Password after screensaver" || warn "No password after screensaver"
[[ $(sudo -n defaults read /Library/Preferences/com.apple.loginwindow GuestEnabled 2>/dev/null) == 0 ]] && ok "Guest account off" || warn "Guest account may be on (or sudo needed)"
[[ $(softwareupdate --schedule 2>/dev/null) == *on* ]]      && ok "Automatic updates on"  || warn "Automatic updates off"
sharing=$(sudo -n launchctl print system 2>/dev/null | grep -cE 'com.apple.(screensharing|smbd|RemoteDesktop.agent)'); [[ ${sharing:-0} -eq 0 ]] && ok "No sharing services running" || warn "$sharing sharing service(s) running — check Sharing settings"
ssh_on=$(systemsetup -getremotelogin 2>/dev/null); [[ $ssh_on == *Off* ]] && ok "Remote Login (SSH) off" || warn "Remote Login: ${ssh_on:-unknown}"
agents=$(ls ~/Library/LaunchAgents 2>/dev/null | wc -l | tr -d ' '); echo "ℹ️  $agents user launch agents — review: ls ~/Library/LaunchAgents"
exts=$(systemextensionsctl list 2>/dev/null | grep -c activated); echo "ℹ️  $exts system extensions active — systemextensionsctl list"
free=$(df -h / | awk 'NR==2{print $4}'); pct=$(df / | awk 'NR==2{gsub("%","",$5); print 100-$5}'); [[ $pct -ge 15 ]] && ok "Disk: $free free ($pct%)" || warn "Disk low: $free free ($pct%) — run scripts/cleanup.sh"
tm=$(tmutil latestbackup 2>/dev/null); [[ -n $tm ]] && ok "Time Machine latest: ${tm:t}" || warn "No Time Machine backup found"
up=$(uptime | sed -E 's/.*up ([^,]+),.*/\1/'); echo "ℹ️  Uptime: $up"
sw=$(sw_vers -productVersion); echo "ℹ️  macOS $sw ($(uname -m)); Rosetta: $([[ -f /Library/Apple/usr/share/rosetta/rosetta ]] && echo installed || echo absent)"
[[ -f ~/.ssh/id_ed25519 ]] && ok "ed25519 SSH key present" || warn "No ~/.ssh/id_ed25519 — ssh-keygen -t ed25519"
grep -qs 'pam_tid.so' /etc/pam.d/sudo_local && ok "Touch ID for sudo" || warn "Touch ID for sudo not configured (/etc/pam.d/sudo_local)"
