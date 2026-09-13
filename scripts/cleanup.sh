#!/bin/sh
# cleanup.sh — monthly disk cleanup for a developer Mac. Safe: only removes caches/artifacts that regenerate.
# Usage: sh scripts/cleanup.sh        (see chapter 18)
set -u
before=$(df -k / | awk 'NR==2{print $4}')

echo "→ Homebrew";     brew cleanup --prune=all -s 2>/dev/null; brew autoremove 2>/dev/null
echo "→ Xcode";        rm -rf ~/Library/Developer/Xcode/DerivedData/* 2>/dev/null
                       xcrun simctl delete unavailable 2>/dev/null || true
echo "→ Containers";   command -v docker >/dev/null 2>&1 && docker system prune -f >/dev/null 2>&1 || true
echo "→ Packages";     command -v npm  >/dev/null 2>&1 && npm cache clean --force >/dev/null 2>&1 || true
                       command -v pnpm >/dev/null 2>&1 && pnpm store prune >/dev/null 2>&1 || true
                       command -v uv   >/dev/null 2>&1 && uv cache clean >/dev/null 2>&1 || true
                       command -v go   >/dev/null 2>&1 && go clean -modcache 2>/dev/null || true
                       command -v mise >/dev/null 2>&1 && mise prune -y >/dev/null 2>&1 || true
echo "→ Caches";       rm -rf ~/Library/Caches/Homebrew/* ~/Library/Caches/pip ~/Library/Caches/Yarn 2>/dev/null
echo "→ Logs";         find ~/Library/Logs -type f -mtime +30 -delete 2>/dev/null
echo "→ Trash";        rm -rf ~/.Trash/* 2>/dev/null
echo "→ Snapshots";    tmutil listlocalsnapshots / 2>/dev/null | sed 's/.*\.//' | while read -r d; do tmutil deletelocalsnapshots "$d" >/dev/null 2>&1; done

after=$(df -k / | awk 'NR==2{print $4}')
echo "Freed ~$(( (after - before) / 1024 )) MB. Free now: $(df -h / | awk 'NR==2{print $4}')"
