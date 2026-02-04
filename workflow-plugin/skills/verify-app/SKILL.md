# Verify Application

<skill-description>
End-to-end verification of application functionality.
</skill-description>

## Overview

> "verify-app has detailed instructions for testing Claude Code end to end."
> — Boris Cherny

Run this before merging to ensure the application works correctly.

## Steps to Execute

1. **Build Check**: Ensure the app builds
   ```bash
   npm run build  # or appropriate build command
   ```

2. **Type Check**: Verify no type errors
   ```bash
   npm run typecheck  # or tsc --noEmit
   ```

3. **Lint Check**: Code style compliance
   ```bash
   npm run lint
   ```

4. **Unit Tests**: Run test suite
   ```bash
   npm test
   ```

5. **Integration Tests** (if available):
   ```bash
   npm run test:integration
   ```

6. **Start Application**: Verify it runs
   ```bash
   npm run dev  # Start in background, check for errors
   ```

7. **Smoke Test**: Basic functionality check
   - Can the app start?
   - Do main routes respond?
   - Are there console errors?

## Output Format

```
## Application Verification Report

### Build
✓ Build completed successfully
  - Output: dist/
  - Size: 2.3MB
  - Time: 12s

### Type Check
✓ No type errors
  - Files checked: 156

### Lint
✓ No lint errors
  - Files checked: 156
  - Warnings: 2 (non-blocking)

### Unit Tests
✓ All tests passing
  - Tests: 234
  - Passed: 234
  - Failed: 0
  - Coverage: 87%

### Integration Tests
✓ All tests passing
  - Tests: 45
  - Passed: 45

### Smoke Test
✓ Application starts successfully
  - Server running on port 3000
  - Health check: /api/health → 200 OK
  - No console errors

---

## Summary

| Check | Status |
|-------|--------|
| Build | ✓ Pass |
| Types | ✓ Pass |
| Lint | ✓ Pass |
| Unit Tests | ✓ Pass |
| Integration | ✓ Pass |
| Smoke Test | ✓ Pass |

**Result: Ready to merge**
```

## Failure Handling

If any check fails:

1. **Build Failure**: Check for syntax errors, missing dependencies
2. **Type Errors**: Fix type mismatches, add missing types
3. **Lint Errors**: Run `npm run lint:fix` for auto-fixable issues
4. **Test Failures**: Investigate failing tests, fix or update as needed
5. **Smoke Test**: Check logs for runtime errors

## Customization

Add a `.verify-app.json` in your project root to customize:

```json
{
  "build": "npm run build",
  "typecheck": "tsc --noEmit",
  "lint": "eslint .",
  "test": "jest",
  "integration": "jest --config jest.integration.js",
  "start": "npm run dev",
  "healthCheck": "http://localhost:3000/api/health"
}
```
