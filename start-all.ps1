# Start Claude Code with all plugins loaded
# Usage: pwsh -File C:\Users\crissantos\claude-plugins\start-all.ps1

$pluginDir = "C:\Users\crissantos\claude-plugins"

$plugins = Get-ChildItem $pluginDir -Directory |
    Where-Object { Test-Path (Join-Path $_.FullName ".claude-plugin\plugin.json") } |
    ForEach-Object { "--plugin-dir", $_.FullName }

$count = ($plugins.Count / 2)
Write-Host "Loading $count plugins..." -ForegroundColor Cyan

claude @plugins
