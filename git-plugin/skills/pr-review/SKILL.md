---
name: pr-review
description: Perform a code review on a pull request or git diff. Analyzes changes for bugs, security issues, and best practices.
---

# PR Review Skill

Analyze code changes and provide review feedback.

## Steps

1. **Get Changes**: Either from PR number or local diff
   ```bash
   # From GitHub PR
   gh pr diff {number}

   # Local changes
   git diff main...HEAD
   ```

2. **Analyze Changes**:
   - Code quality issues
   - Security vulnerabilities
   - Performance concerns
   - Test coverage gaps
   - Documentation needs

3. **Output Format**:
   ```
   ## PR Review: #{number}

   ### Summary
   - Files Changed: X
   - Lines Added: +X
   - Lines Removed: -X

   ### Issues Found
   | Severity | File | Line | Issue |
   |----------|------|------|-------|
   | High | app.js | 42 | SQL injection risk |

   ### Suggestions
   - Consider adding tests for...
   - This could be refactored to...

   ### Approved: Yes/No
   ```

## Example Usage
- `/git:pr-review 123`
- `/git:pr-review` (reviews current branch changes)
