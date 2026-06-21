$ErrorActionPreference = "Stop"

$repoPath = "C:\Users\ZhuanZ1\Documents\Codex\2026-06-07\i-am-a-securities-salesperson-in\outputs\fcn-desk-workbench"

Set-Location $repoPath

git config --global --add safe.directory "C:/Users/ZhuanZ1/Documents/Codex/2026-06-07/i-am-a-securities-salesperson-in/outputs/fcn-desk-workbench"
git remote set-url origin "https://github.com/peteribmhk/fcn-desk-workbench.git"
git push -u origin main

Write-Host ""
Write-Host "Done. Open: https://github.com/peteribmhk/fcn-desk-workbench"

