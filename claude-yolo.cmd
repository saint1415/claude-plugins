@echo off
REM Claude Code YOLO Mode - Quick launcher
REM Just double-click or run from anywhere

pwsh -NoProfile -ExecutionPolicy Bypass -File "%~dp0claude.ps1" -yolo %*
