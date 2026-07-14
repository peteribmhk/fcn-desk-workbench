[CmdletBinding()]
param(
    [string]$RepoRoot = "",
    [string]$Repo = "peteribmhk/fcn-desk-workbench",
    [string]$Remote = "origin",
    [string]$Branch = "main",
    [string]$Message = "Update FCN workbench"
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

function Invoke-GitCapture {
    $gitArgs = $args
    $output = & $script:Git -c "safe.directory=$($script:SafeRepoRoot)" -C $script:RepoRoot @gitArgs
    if ($LASTEXITCODE -ne 0) {
        throw "git $($gitArgs -join ' ') failed with exit code $LASTEXITCODE"
    }
    return $output
}

function Invoke-GhJson {
    param(
        [string[]]$Args,
        [object]$Body = $null
    )

    if ($null -eq $Body) {
        $json = & $script:Gh @Args
    } else {
        $temp = New-TemporaryFile
        try {
            $bodyJson = $Body | ConvertTo-Json -Depth 50
            [System.IO.File]::WriteAllText($temp.FullName, $bodyJson, [System.Text.UTF8Encoding]::new($false))
            $json = & $script:Gh @Args --input $temp.FullName
        } finally {
            Remove-Item -LiteralPath $temp.FullName -Force -ErrorAction SilentlyContinue
        }
    }

    if ($LASTEXITCODE -ne 0) {
        throw "gh $($Args -join ' ') failed with exit code $LASTEXITCODE"
    }

    if (-not $json) {
        return $null
    }
    return $json | ConvertFrom-Json
}

function Publish-ByGitHubApi {
    $remoteRef = Invoke-GhJson -Args @("api", "repos/$Repo/git/ref/heads/$Branch")
    $baseSha = $remoteRef.object.sha
    $knownRemote = (Invoke-GitCapture rev-parse "$Remote/$Branch").Trim()
    if ($knownRemote -ne $baseSha) {
        throw "GitHub has newer commits than the local tracking branch. Run scripts/sync-from-github.ps1 first before publishing."
    }

    $baseCommit = Invoke-GhJson -Args @("api", "repos/$Repo/git/commits/$baseSha")
    $baseTree = $baseCommit.tree.sha

    $paths = Invoke-GitCapture ls-files
    $entries = @()

    foreach ($path in $paths) {
        $repoPath = $path.Replace("\", "/")
        $fullPath = Join-Path $script:RepoRoot $path
        if (-not (Test-Path -LiteralPath $fullPath -PathType Leaf)) {
            continue
        }

        $content = [System.IO.File]::ReadAllText($fullPath, [System.Text.Encoding]::UTF8)
        $blob = Invoke-GhJson -Args @("api", "repos/$Repo/git/blobs") -Body @{
            content = $content
            encoding = "utf-8"
        }
        $entries += @{
            path = $repoPath
            mode = "100644"
            type = "blob"
            sha = $blob.sha
        }
    }

    $tree = Invoke-GhJson -Args @("api", "repos/$Repo/git/trees") -Body @{
        base_tree = $baseTree
        tree = $entries
    }

    $commit = Invoke-GhJson -Args @("api", "repos/$Repo/git/commits") -Body @{
        message = $Message
        tree = $tree.sha
        parents = @($baseSha)
    }

    $updated = Invoke-GhJson -Args @("api", "-X", "PATCH", "repos/$Repo/git/refs/heads/$Branch") -Body @{
        sha = $commit.sha
        force = $false
    }

    Write-Host "Published by GitHub API: $($commit.sha)"
    Write-Host "Remote ref now: $($updated.object.sha)"
}

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
    $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
    $RepoRoot = Split-Path -Parent $scriptDir
}

$script:RepoRoot = (Resolve-Path -LiteralPath $RepoRoot).Path
$script:SafeRepoRoot = $script:RepoRoot.Replace("\", "/")
$script:Git = Resolve-Tool "git" "C:\Program Files\Git\cmd\git.exe"
$script:Gh = Resolve-Tool "gh" "C:\Program Files\GitHub CLI\gh.exe"

Write-Host "FCN publish to GitHub master"
Write-Host "Repo: $script:RepoRoot"
Write-Host "GitHub: $Repo"

Invoke-Git rev-parse --is-inside-work-tree | Out-Null

Invoke-Git add -A
$hasStagedChanges = $true
& $script:Git -c "safe.directory=$($script:SafeRepoRoot)" -C $script:RepoRoot diff --cached --quiet
if ($LASTEXITCODE -eq 0) {
    $hasStagedChanges = $false
} elseif ($LASTEXITCODE -ne 1) {
    throw "git diff --cached --quiet failed with exit code $LASTEXITCODE"
}

if ($hasStagedChanges) {
    Invoke-Git commit -m $Message
} else {
    Write-Host "No uncommitted file changes to commit."
}

try {
    Invoke-Git fetch $Remote $Branch
    & $script:Git -c "safe.directory=$($script:SafeRepoRoot)" -C $script:RepoRoot merge-base --is-ancestor "$Remote/$Branch" HEAD
    if ($LASTEXITCODE -eq 1) {
        throw "GitHub has newer commits than this local branch. Run scripts/sync-from-github.ps1 first, then reapply or republish the intended changes."
    } elseif ($LASTEXITCODE -ne 0) {
        throw "git merge-base check failed with exit code $LASTEXITCODE"
    }
    Invoke-Git push $Remote $Branch
    Write-Host "Published by normal git push."
} catch {
    Write-Host "Normal git publish failed: $($_.Exception.Message)"
    if ($_.Exception.Message -like "GitHub has newer commits*") {
        throw
    }
    Write-Host "Falling back to GitHub API publish."
    Publish-ByGitHubApi
}

Write-Host "Publish complete. Future Codex/ChatGPT sessions should sync from GitHub before FCN work."
