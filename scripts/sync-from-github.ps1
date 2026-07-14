[CmdletBinding()]
param(
    [string]$RepoRoot = "",
    [string]$Repo = "peteribmhk/fcn-desk-workbench",
    [string]$Remote = "origin",
    [string]$Branch = "main"
)

$ErrorActionPreference = "Stop"

function Resolve-Tool {
    param(
        [string]$Name,
        [string]$Fallback
    )

    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($cmd) {
        return $cmd.Source
    }

    if (Test-Path -LiteralPath $Fallback) {
        return $Fallback
    }

    throw "Required tool not found: $Name"
}

function Invoke-Git {
    $gitArgs = $args
    & $script:Git -c "safe.directory=$($script:SafeRepoRoot)" -C $script:RepoRoot @gitArgs
    if ($LASTEXITCODE -ne 0) {
        throw "git $($gitArgs -join ' ') failed with exit code $LASTEXITCODE"
    }
}

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
    $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
    $RepoRoot = Split-Path -Parent $scriptDir
}

$script:RepoRoot = (Resolve-Path -LiteralPath $RepoRoot).Path
$script:SafeRepoRoot = $script:RepoRoot.Replace("\", "/")
$script:Git = Resolve-Tool "git" "C:\Program Files\Git\cmd\git.exe"
$script:Gh = Resolve-Tool "gh" "C:\Program Files\GitHub CLI\gh.exe"

Write-Host "FCN GitHub master sync"
Write-Host "Repo: $script:RepoRoot"
Write-Host "Remote branch: $Remote/$Branch"

Invoke-Git rev-parse --is-inside-work-tree | Out-Null

$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$dirty = & $script:Git -c "safe.directory=$($script:SafeRepoRoot)" -C $script:RepoRoot status --porcelain
if ($dirty) {
    Write-Host "Local uncommitted work found. Saving it in a Git stash before sync."
    Invoke-Git stash push -u -m "codex-sync-autostash-$stamp"
}

Write-Host "Fetching latest GitHub state..."
$fetchOk = $true
try {
    Invoke-Git fetch $Remote $Branch
} catch {
    $fetchOk = $false
    Write-Host "Git fetch failed: $($_.Exception.Message)"
}

$localHead = (& $script:Git -c "safe.directory=$($script:SafeRepoRoot)" -C $script:RepoRoot rev-parse HEAD).Trim()

if (-not $fetchOk) {
    $remoteHeadFromApi = (& $script:Gh api "repos/$Repo/commits/$Branch" --jq .sha).Trim()
    if ($LASTEXITCODE -ne 0) {
        throw "Git fetch failed and GitHub API readback also failed."
    }

    if ($localHead -eq $remoteHeadFromApi) {
        Write-Host "Git fetch failed, but GitHub API confirms local HEAD already matches $Repo/$Branch."
        Write-Host "Sync complete: $($localHead.Substring(0, 7))"
        exit 0
    }

    throw "Git fetch failed and GitHub is newer ($($remoteHeadFromApi.Substring(0, 7))). Retry sync when Git transport is available."
}

$remoteHead = (& $script:Git -c "safe.directory=$($script:SafeRepoRoot)" -C $script:RepoRoot rev-parse "$Remote/$Branch").Trim()

if ($localHead -ne $remoteHead) {
    $backupBranch = "backup/local-before-sync-$stamp"
    Write-Host "Local branch differs from GitHub. Preserving local HEAD in $backupBranch."
    Invoke-Git branch $backupBranch $localHead
    Write-Host "Aligning local branch to GitHub master copy..."
    Invoke-Git reset --hard "$Remote/$Branch"
} else {
    Write-Host "Local branch already matches GitHub master copy."
}

$latest = (& $script:Git -c "safe.directory=$($script:SafeRepoRoot)" -C $script:RepoRoot log -1 --pretty="%h %s").Trim()
Write-Host "Sync complete: $latest"
Write-Host "Next: reread AGENTS.md, assistant-operating-instructions.md, desk-memory.md, daily/latest.md, and daily/index.md."
