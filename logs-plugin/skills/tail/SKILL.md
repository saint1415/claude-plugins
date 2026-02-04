---
name: tail
description: Follow log files in real-time with optional filtering.
---

# Log Tail Skill

Stream log output with filtering.

## Steps

1. **Follow Log File**:
   ```bash
   # Windows (PowerShell)
   Get-Content -Path {logfile} -Wait -Tail 50
   Get-Content -Path {logfile} -Wait | Select-String "{pattern}"

   # Linux/Mac
   tail -f {logfile}
   tail -f {logfile} | grep --line-buffered "{pattern}"
   ```

2. **Output**: Streams matching log lines in real-time

## Example Usage
- `/logs:tail C:\logs\app.log`
- `/logs:tail app.log --filter error`
- `/logs:tail /var/log/syslog --lines 100`
