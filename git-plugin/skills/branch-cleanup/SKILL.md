---
name: branch-cleanup
description: Find and clean up stale or merged branches. Identifies branches safe to delete.
---

# Branch Cleanup Skill

Identify and remove stale branches.

## Steps

1. **Find Merged Branches**:
   ```bash
   git branch --merged main
   ```

2. **Find Stale Branches** (no commits in X days):
   ```bash
   git for-each-ref --sort=-committerdate refs/heads/ --format='%(committerdate:short) %(refname:short)'
   ```

3. **Output Format**:
   ```
   ## Branch Cleanup Report

   ### Safe to Delete (Merged)
   - feature/login (merged 30d ago)
   - bugfix/typo (merged 60d ago)

   ### Stale (No commits > 90 days)
   - old-experiment (180d old)

   ### Cleanup Commands
   ```bash
   # Delete merged branches
   git branch -d feature/login bugfix/typo

   # Force delete stale
   git branch -D old-experiment
   ```
   ```

## Example Usage
- `/git:branch-cleanup`
- `/git:branch-cleanup --days 30`
