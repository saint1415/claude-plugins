# Plan Review

<skill-description>
Review and iterate on implementation plan before writing code.
</skill-description>

## Overview

> "Most sessions start in Plan mode. If my goal is to write a Pull Request, I use Plan mode, going back and forth with Claude until I like its plan. From there, I switch into auto-accept edits mode and Claude can usually 1-shot it. A good plan is really important!"
> — Boris Cherny

## Steps to Execute

1. **Understand the Goal**: Clarify what we're trying to achieve
   - What's the end state?
   - What are the acceptance criteria?
   - Are there constraints?

2. **Analyze Current State**:
   - Read relevant existing code
   - Identify what needs to change
   - Note dependencies and impacts

3. **Create Plan**:
   - Break into discrete steps
   - Order by dependencies
   - Identify risks or unknowns

4. **Review with User**:
   - Present plan clearly
   - Ask for feedback
   - Iterate until approved

5. **Transition to Implementation**:
   - Switch to auto-accept mode
   - Execute plan step by step

## Output Format

```
## Implementation Plan

### Goal
Add OAuth2 support with Google and GitHub providers.

### Current State
- Auth system uses username/password only
- Session management in `src/auth/session.ts`
- Login UI in `src/components/Login.tsx`

### Proposed Changes

#### Step 1: Add OAuth Client Libraries
- Install `@auth/core` and provider packages
- Configure environment variables

#### Step 2: Create OAuth Routes
- `GET /auth/google` - Initiate Google flow
- `GET /auth/google/callback` - Handle callback
- Same for GitHub

#### Step 3: Update User Model
- Add `provider` field (local, google, github)
- Add `providerId` field
- Handle account linking

#### Step 4: Update Login UI
- Add "Sign in with Google" button
- Add "Sign in with GitHub" button
- Handle OAuth redirects

#### Step 5: Update Tests
- Mock OAuth providers
- Test callback handling
- Test account linking

### Risks
- Account linking edge cases (same email, different providers)
- Token refresh timing

### Questions
1. Should we support account linking (same email = same account)?
2. What scopes do we need from each provider?

---

**Ready to proceed?** Reply with feedback or approval.
```

## Tips

- Don't rush to code - a good plan saves time
- Ask clarifying questions before planning
- Break complex work into mergeable chunks
- Consider what could go wrong
