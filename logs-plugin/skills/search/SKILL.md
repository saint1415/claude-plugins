---
name: search
description: Search through log files with pattern matching and time filtering.
---

# Log Search Skill

Find entries in log files. Supports regex, time ranges, and multiple files.

## Example Usage
- `/logs:search error app.log`
- `/logs:search "connection refused" --since "1 hour ago"`
