# Claude Code Launcher with All Plugins
# Usage:
#   .\claude.ps1                    # Normal mode with all plugins
#   .\claude.ps1 -yolo              # YOLO mode (skip permissions)
#   .\claude.ps1 -yolo -community   # YOLO + community plugins
#   .\claude.ps1 -minimal           # Only core plugins

param(
    [switch]$yolo,
    [switch]$community,
    [switch]$minimal,
    [switch]$list,
    [string]$profile = "full"
)

$pluginDir = $PSScriptRoot
$communityDir = Join-Path $pluginDir "community"

# Plugin profiles
$profiles = @{
    "minimal" = @(
        "engineering-plugin",
        "superpowers-plugin",
        "workflow-plugin",
        "git-plugin"
    )
    "security" = @(
        "osint-plugin",
        "ssl-plugin",
        "compliance-plugin",
        "aws-iam-plugin",
        "crypto-plugin"
    )
    "devops" = @(
        "docker-plugin",
        "k8s-plugin",
        "terraform-plugin",
        "aws-iam-plugin"
    )
    "productivity" = @(
        "servicenow-plugin",
        "m365-admin-plugin",
        "youtrack-plugin",
        "pm-plugin",
        "workflow-plugin"
    )
}

# Get all custom plugins
function Get-CustomPlugins {
    Get-ChildItem $pluginDir -Directory |
        Where-Object {
            $_.Name -ne "community" -and
            (Test-Path (Join-Path $_.FullName ".claude-plugin\plugin.json"))
        }
}

# Get community plugins
function Get-CommunityPlugins {
    $plugins = @()

    # plugins-plus-skills
    $ppsDir = Join-Path $communityDir "plugins-plus-skills\plugins"
    if (Test-Path $ppsDir) {
        $plugins += Get-ChildItem $ppsDir -Directory |
            Where-Object { Test-Path (Join-Path $_.FullName ".claude-plugin\plugin.json") }
    }

    # trailofbits
    $tobDir = Join-Path $communityDir "trailofbits-skills"
    if (Test-Path (Join-Path $tobDir ".claude-plugin\plugin.json")) {
        $plugins += Get-Item $tobDir
    }

    return $plugins
}

# List mode
if ($list) {
    Write-Host "`nCustom Plugins:" -ForegroundColor Cyan
    Get-CustomPlugins | ForEach-Object { Write-Host "  - $($_.Name)" }

    Write-Host "`nCommunity Plugins:" -ForegroundColor Cyan
    Get-CommunityPlugins | ForEach-Object { Write-Host "  - $($_.Name)" }

    Write-Host "`nProfiles:" -ForegroundColor Cyan
    $profiles.Keys | ForEach-Object { Write-Host "  - $_" }

    exit 0
}

# Build plugin arguments
$pluginArgs = @()

if ($minimal) {
    # Minimal profile
    $profiles["minimal"] | ForEach-Object {
        $path = Join-Path $pluginDir $_
        if (Test-Path $path) {
            $pluginArgs += "--plugin-dir"
            $pluginArgs += $path
        }
    }
    Write-Host "Loading minimal plugins..." -ForegroundColor Yellow
}
elseif ($profile -ne "full" -and $profiles.ContainsKey($profile)) {
    # Named profile
    $profiles[$profile] | ForEach-Object {
        $path = Join-Path $pluginDir $_
        if (Test-Path $path) {
            $pluginArgs += "--plugin-dir"
            $pluginArgs += $path
        }
    }
    Write-Host "Loading $profile profile..." -ForegroundColor Yellow
}
else {
    # Full - all custom plugins
    Get-CustomPlugins | ForEach-Object {
        $pluginArgs += "--plugin-dir"
        $pluginArgs += $_.FullName
    }
    Write-Host "Loading all custom plugins..." -ForegroundColor Yellow
}

# Add community plugins if requested
if ($community) {
    Write-Host "Adding community plugins..." -ForegroundColor Yellow
    Get-CommunityPlugins | ForEach-Object {
        $pluginArgs += "--plugin-dir"
        $pluginArgs += $_.FullName
    }
}

# Count plugins
$pluginCount = ($pluginArgs.Count / 2)
Write-Host "Loaded $pluginCount plugins" -ForegroundColor Green

# YOLO mode
if ($yolo) {
    Write-Host "YOLO MODE ENABLED" -ForegroundColor Red
    $pluginArgs += "--dangerously-skip-permissions"
}

Write-Host ""

# Launch Claude
claude @pluginArgs
