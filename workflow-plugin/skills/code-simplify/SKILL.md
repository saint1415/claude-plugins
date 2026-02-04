# Code Simplify

<skill-description>
Simplify and clean up code after implementation is complete.
</skill-description>

## Overview

> "I use a few subagents regularly: code-simplifier simplifies the code after Claude is done working."
> — Boris Cherny

Run this after completing an implementation to clean up and simplify the result.

## Steps to Execute

1. **Identify Changed Files**:
   ```bash
   git diff --name-only HEAD~1
   ```

2. **Review Each File**: Look for:
   - Unnecessary complexity
   - Duplicate code
   - Over-abstraction
   - Dead code
   - Verbose patterns that could be simpler

3. **Apply Simplifications**:
   - Remove unused imports
   - Consolidate duplicate logic
   - Simplify conditionals
   - Use language idioms
   - Remove unnecessary comments

4. **Verify Behavior**: Ensure tests still pass
   ```bash
   npm test  # or appropriate test command
   ```

## Simplification Checklist

### Remove
- [ ] Unused imports
- [ ] Unused variables
- [ ] Dead code paths
- [ ] Redundant comments (code should be self-documenting)
- [ ] Over-engineered abstractions for one-time use

### Consolidate
- [ ] Duplicate logic → shared function
- [ ] Similar conditionals → single check
- [ ] Repeated patterns → loop or map

### Simplify
- [ ] Nested ternaries → if/else or early return
- [ ] Complex boolean logic → named variables
- [ ] Deep nesting → early returns
- [ ] Callback chains → async/await

### Improve
- [ ] Variable names → clear and descriptive
- [ ] Function names → describe what they do
- [ ] Magic numbers → named constants

## Output Format

```
## Code Simplification Report

### Files Reviewed
- src/auth/oauth.ts
- src/auth/session.ts
- tests/auth.test.ts

### Changes Made

#### src/auth/oauth.ts
- Removed 3 unused imports
- Consolidated duplicate token refresh logic
- Simplified callback URL construction

**Before:**
```typescript
const baseUrl = config.baseUrl;
const path = '/auth/callback';
const provider = 'google';
const callbackUrl = baseUrl + path + '/' + provider;
```

**After:**
```typescript
const callbackUrl = `${config.baseUrl}/auth/callback/google`;
```

#### src/auth/session.ts
- No changes needed

### Summary
- Lines removed: 23
- Functions simplified: 2
- Tests passing: ✓

---

Code is now simpler and more maintainable.
```

## When to Use

- After completing a feature
- Before creating a PR
- When revisiting old code
- After merging multiple contributions
