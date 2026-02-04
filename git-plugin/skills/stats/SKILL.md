---
name: stats
description: Show repository statistics including contributors, commit frequency, file change history, and code churn.
---

# Repository Statistics Skill

Analyze repository metrics and history.

## Steps

1. **Gather Stats**:
   ```bash
   # Contributor stats
   git shortlog -sn --all

   # Commit frequency
   git log --format='%ai' | cut -d' ' -f1 | uniq -c

   # Lines of code
   git ls-files | xargs wc -l
   ```

2. **Output Format**:
   ```
   ## Repository Statistics

   ### Overview
   - Total Commits: X
   - Contributors: X
   - First Commit: YYYY-MM-DD
   - Latest Commit: YYYY-MM-DD

   ### Top Contributors
   | Author | Commits | % |
   |--------|---------|---|
   | John | 150 | 45% |

   ### Commit Frequency
   - This Week: X
   - This Month: X
   - This Year: X

   ### Most Changed Files
   | File | Changes |
   |------|---------|
   | app.js | 234 |
   ```

## Example Usage
- `/git:stats`
- `/git:stats --author "John"`
