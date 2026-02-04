# Workflow Plugin for Claude Code

Development workflow automation inspired by [Boris Cherny's Claude Code patterns](https://x.com/bcherny/status/2007179832300581177).

## Philosophy

> "I use slash commands for every 'inner loop' workflow that I do many times a day. This saves from repeated prompting and allows Claude to use these workflows too."
> — Boris Cherny, Creator of Claude Code

## Skills

| Skill | Description |
|-------|-------------|
| `/workflow:commit-push-pr` | Commit changes, push branch, create PR in one command |
| `/workflow:plan-review` | Review and iterate on implementation plan before coding |
| `/workflow:code-simplify` | Simplify code after implementation is complete |
| `/workflow:verify-app` | End-to-end verification of application |

## Usage

### Daily Development Loop

```
# 1. Start with a plan
/workflow:plan-review

# 2. Implement (Claude codes)
# ... Claude writes code ...

# 3. Simplify the result
/workflow:code-simplify

# 4. Ship it
/workflow:commit-push-pr
```

### Boris Cherny's Tips Implemented

1. **Plan Mode First**: Most sessions start in Plan mode. Go back and forth until you like the plan, then switch to auto-accept.

2. **Slash Commands**: Every repeated workflow becomes a command.

3. **Subagents**: `code-simplify` and `verify-app` are subagent-style workflows that run after primary work.

4. **CLAUDE.md**: Anytime Claude does something incorrectly, add it to CLAUDE.md so it doesn't happen again.

## Examples

```
# After finishing a feature
/workflow:commit-push-pr

# Before starting complex work
/workflow:plan-review Update the authentication system to use OAuth2

# After Claude completes implementation
/workflow:code-simplify

# Before merging
/workflow:verify-app
```
