# Orchestration Plugin

Multi-agent orchestration for Claude Code with the Builder/Validator pattern.

Based on concepts from [IndyDevDan's Claude Code Hooks Mastery](https://github.com/disler/claude-code-hooks-mastery).

## Features

- **Builder/Validator Pattern**: Two-agent pairing for quality assurance
- **Self-Validating Agents**: Embedded hooks for automatic code validation
- **Task System Integration**: Use Claude Code's TaskCreate/TaskUpdate for agent communication
- **Windows Compatible**: All hooks work on Windows 11

## Skills

| Skill | Description |
|-------|-------------|
| `/orchestration:plan-with-team` | Create a plan with specialized agent teams |
| `/orchestration:execute-plan` | Execute a plan using the Task system |

## Agents

### Builder Agent
- Focuses on ONE task
- Self-validates with embedded hooks (ruff, type checking)
- Reports completion status

### Validator Agent
- Verifies Builder's work
- Runs validation checks
- Reports success/failure with feedback

## Installation

### 1. Copy hooks to your project

```powershell
# From your project directory
Copy-Item -Path "C:\Users\crissantos\claude-plugins\orchestration-plugin\hooks\*" -Destination ".\.claude\hooks\" -Recurse
```

### 2. Configure settings.json

Copy `settings.json.template` to your project's `.claude/settings.json` and adjust paths.

### 3. Install dependencies

```powershell
pip install ruff  # For Python validation
```

## Usage

### Creating a Plan with Team

```
/orchestration:plan-with-team Update all API endpoints to use async/await

Orchestration: Create builder/validator pairs for each endpoint file
```

### Executing the Plan

```
/orchestration:execute-plan specs/async-update.md
```

## Hooks Reference

| Hook | Purpose | Blocks? |
|------|---------|---------|
| `pre_tool_use.py` | Block dangerous commands, protect .env files | Yes |
| `post_tool_use.py` | Log tool usage, run code validation | No |
| `stop.py` | Self-validation when agent completes | No |
| `subagent_stop.py` | Log/announce subagent completion | No |

## Windows Notes

- Uses `python` instead of `uv run` for simplicity
- Environment variable: `%CLAUDE_PROJECT_DIR%` (not `$CLAUDE_PROJECT_DIR`)
- Paths use backslashes in settings.json

## Task System Commands

```javascript
// Create task
TaskCreate({ subject: "...", description: "...", activeForm: "..." })

// Update task
TaskUpdate({ taskId: "1", status: "completed" })

// Set dependencies
TaskUpdate({ taskId: "2", addBlockedBy: ["1"] })

// List tasks
TaskList()
```

## Credits

- Concepts: [IndyDevDan](https://github.com/disler) / [YouTube](https://youtube.com/@IndyDevDan)
- Implementation: crissantos
