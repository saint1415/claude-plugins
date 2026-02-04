---
name: execute-plan
description: Execute a plan with team orchestration using the Claude Code Task system.
---

# Execute Plan with Team

Execute a generated plan using the Task system for multi-agent orchestration.

## Usage

```
/orchestration:execute-plan <plan_file>
```

## How It Works

1. **Parse the Plan**: Read the plan file and extract tasks, team members, dependencies

2. **Create Task List**: Use TaskCreate to set up all tasks with:
   - Subject (task name)
   - Description (what to do)
   - Owner (agent type)
   - Dependencies (blockedBy)

3. **Launch Agents**: For each task:
   - Spawn appropriate agent (Builder or Validator)
   - Agent works on their focused task
   - Agent updates task status on completion

4. **Orchestrate**: Primary agent monitors task completion:
   - Receives SubagentStop events
   - Unblocks dependent tasks
   - Launches next wave of agents

## Task System Commands

```javascript
// Create a task
TaskCreate({
  subject: "Add type hints to utils.py",
  description: "...",
  activeForm: "Adding type hints"
})

// Update task status
TaskUpdate({
  taskId: "1",
  status: "in_progress"  // or "completed"
})

// Set dependencies
TaskUpdate({
  taskId: "2",
  addBlockedBy: ["1"]  // Task 2 waits for Task 1
})

// List all tasks
TaskList()

// Get task details
TaskGet({ taskId: "1" })
```

## Execution Flow

```
┌─────────────────┐
│  Parse Plan     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Create Tasks    │──── TaskCreate for each task
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Set Dependencies│──── TaskUpdate with blockedBy
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Launch Builders │──── Parallel Task agents (unblocked tasks)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Builders Report │──── SubagentStop events
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│Launch Validators│──── Now unblocked
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   All Complete  │
└─────────────────┘
```

## Agent Spawning

For each task, spawn with the Task tool:

```
Task({
  description: "Build: {task_subject}",
  prompt: "You are a Builder agent. Your ONE task: {task_description}...",
  subagent_type: "general-purpose"
})
```

## Monitoring Progress

The primary agent will:
1. Receive notifications when sub-agents complete
2. Check task list status
3. Launch next batch of agents
4. Report overall completion

## Example

```
> /orchestration:execute-plan specs/add-type-hints.md

Creating task list...
✓ Task 1: Add types to utils.py (builder)
✓ Task 2: Validate utils.py (validator, blocked by 1)
✓ Task 3: Add types to main.py (builder)
✓ Task 4: Validate main.py (validator, blocked by 3)

Launching parallel builders...
→ utils_builder started
→ main_builder started

[utils_builder completed] ✓
→ utils_validator started

[main_builder completed] ✓
→ main_validator started

[utils_validator completed] ✓
[main_validator completed] ✓

All tasks complete!
```
