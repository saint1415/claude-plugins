@echo off
REM Claude Code Full Mode - All plugins, normal permissions
REM Just double-click or run from anywhere

pwsh -NoProfile -ExecutionPolicy Bypass -File "%~dp0claude.ps1" %*
