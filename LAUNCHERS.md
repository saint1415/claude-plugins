# Claude Code Launchers

Quick ways to start Claude Code with all plugins.

## Quick Start

### YOLO Mode (Recommended for autonomous work)
```cmd
C:\Users\crissantos\claude-plugins\claude-yolo.cmd
```

Or in PowerShell:
```powershell
C:\Users\crissantos\claude-plugins\claude.ps1 -yolo
```

### Normal Mode (With permission prompts)
```cmd
C:\Users\crissantos\claude-plugins\claude-full.cmd
```

## All Options

```powershell
# Full mode - all 42 plugins
.\claude.ps1

# YOLO mode - skip all permission prompts
.\claude.ps1 -yolo

# Include community plugins (1,500+ extra skills)
.\claude.ps1 -yolo -community

# Minimal - just core plugins (faster startup)
.\claude.ps1 -minimal

# Specific profile
.\claude.ps1 -profile security
.\claude.ps1 -profile devops
.\claude.ps1 -profile productivity

# List all available plugins
.\claude.ps1 -list
```

## Profiles

| Profile | Plugins |
|---------|---------|
| `minimal` | engineering, superpowers, workflow, git |
| `security` | osint, ssl, compliance, aws-iam, crypto |
| `devops` | docker, k8s, terraform, aws-iam |
| `productivity` | servicenow, m365-admin, youtrack, pm, workflow |

## Add to PATH (Optional)

To run `claude-yolo` from anywhere:

```powershell
# Add to user PATH
$path = [Environment]::GetEnvironmentVariable("Path", "User")
$newPath = "C:\Users\crissantos\claude-plugins"
if ($path -notlike "*$newPath*") {
    [Environment]::SetEnvironmentVariable("Path", "$path;$newPath", "User")
    Write-Host "Added to PATH. Restart terminal to use."
}
```

Then just run:
```cmd
claude-yolo
claude-full
```

## Create Desktop Shortcut

```powershell
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\Desktop\Claude YOLO.lnk")
$Shortcut.TargetPath = "C:\Users\crissantos\claude-plugins\claude-yolo.cmd"
$Shortcut.WorkingDirectory = $env:USERPROFILE
$Shortcut.Save()
```

## What is YOLO Mode?

YOLO mode (`--dangerously-skip-permissions`) allows Claude to:
- Execute bash commands without asking
- Write/edit files without confirmation
- Run git commands autonomously

**Use when:**
- You trust the current task
- You want autonomous multi-agent workflows
- You're in a safe/sandboxed environment

**Avoid when:**
- Working with sensitive systems
- Running untrusted code
- In production environments
