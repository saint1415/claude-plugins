# Commit, Push, and Create PR

<skill-description>
Complete git workflow: stage changes, commit with good message, push branch, create pull request.
</skill-description>

## Overview

This is the most-used command in Boris Cherny's workflow - executed dozens of times daily. It automates the entire "ship code" cycle.

## Steps to Execute

1. **Check Status**: Review what's changed
   ```bash
   git status
   git diff --stat
   ```

2. **Stage Changes**: Add relevant files (avoid secrets)
   ```bash
   git add <specific-files>
   # Never: git add -A (might include .env, credentials)
   ```

3. **Generate Commit Message**: Based on actual changes
   - Summarize the "why" not the "what"
   - Keep first line under 50 chars
   - Add body for context if needed

4. **Commit**:
   ```bash
   git commit -m "<message>"
   ```

5. **Push Branch**:
   ```bash
   git push -u origin <branch-name>
   ```

6. **Create Pull Request**:
   ```bash
   gh pr create --title "<title>" --body "<body>"
   ```

## Output Format

```
## Shipping Changes

### Changes Staged
- src/auth/login.ts (modified)
- src/auth/oauth.ts (new)
- tests/auth.test.ts (modified)

### Commit
**Message:** Add OAuth2 support to authentication system

**Hash:** abc1234

### Push
**Branch:** feature/oauth2-auth
**Remote:** origin

### Pull Request Created
**Title:** Add OAuth2 support to authentication system
**URL:** https://github.com/user/repo/pull/123

**Summary:**
- Implements OAuth2 flow with Google and GitHub providers
- Adds token refresh logic
- Updates tests for new auth paths

---

Ready for review!
```

## Safety Checks

- Never commit files matching: `.env*`, `*credentials*`, `*secret*`, `*.pem`, `*.key`
- Verify branch is not `main` or `master` before force operations
- Check for merge conflicts before push

## Examples

```
# Standard usage
/workflow:commit-push-pr

# With specific message
/workflow:commit-push-pr "Fix login redirect bug"

# Draft PR
/workflow:commit-push-pr --draft
```
