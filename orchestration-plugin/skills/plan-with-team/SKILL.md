---
name: plan-with-team
description: Create a plan with a team of specialized agents (Builder/Validator pattern). This is a template meta-prompt that generates structured plans with self-validation.
---

# Plan with Team

A template meta-prompt for creating plans with specialized agent teams.

## Purpose

Generate a structured plan that:
1. Breaks work into focused tasks
2. Assigns Builder and Validator agents to each task
3. Sets up task dependencies
4. Includes self-validation hooks

## Usage

```
/orchestration:plan-with-team <request> [--orchestration <guidance>]
```

## Input Format

**User Request**: What you want to build/accomplish

**Orchestration Prompt** (optional): High-level guidance on team composition
- How to group tasks
- Special validation requirements
- Parallelization preferences

## Output Format

The plan will be generated in this structure:

```markdown
# Plan: {plan_name}

## Objective
{what_we_are_building}

## Problem Statement
{why_this_is_needed}

## Solution Approach
{how_we_will_solve_it}

## Team Orchestration

### Team Members

| Name | Role | Agent Type | Resume on Failure |
|------|------|------------|-------------------|
| {task}_builder | Build {task} | builder | true |
| {task}_validator | Validate {task} | validator | false |

## Step-by-Step Tasks

### Task 1: {task_name}
- **Owner**: {task}_builder
- **Description**: {detailed_description}
- **Acceptance Criteria**: {what_defines_done}
- **Blocked By**: []

### Task 2: Validate {task_name}
- **Owner**: {task}_validator
- **Description**: Validate Task 1 completion
- **Blocked By**: [Task 1]

## Validation Commands
{commands_to_verify_work}

## Notes
{additional_context}
```

## Workflow

1. **Analysis Phase**
   - Read the codebase to understand current state
   - Identify files that need modification
   - Determine dependencies

2. **Team Composition**
   - Create Builder/Validator pairs for each major task
   - Use orchestration prompt to guide team structure

3. **Task Planning**
   - Break work into focused, single-purpose tasks
   - Set up dependencies (validators block on builders)
   - Enable parallel execution where possible

4. **Self-Validation**
   - Include validation commands for each task
   - Ensure plan contains required sections

## Example

**Request**: Update all Python scripts to use type hints

**Orchestration**: Create one builder per file, validators check type correctness

**Generated Plan**:
```markdown
# Plan: Add Type Hints

## Team Members
| Name | Role | Agent Type |
|------|------|------------|
| utils_builder | Add types to utils.py | builder |
| utils_validator | Validate utils.py types | validator |
| main_builder | Add types to main.py | builder |
| main_validator | Validate main.py types | validator |

## Tasks
1. utils_builder: Add type hints to utils.py
2. utils_validator: Validate types (blocked by 1)
3. main_builder: Add type hints to main.py
4. main_validator: Validate types (blocked by 3)
5. Integration validator: Run mypy on entire project (blocked by 2, 4)
```

## Best Practices

1. **Focused Tasks**: Each task should do ONE thing
2. **Clear Ownership**: Every task has exactly one owner
3. **Validation Coverage**: Every build task has a corresponding validate task
4. **Parallelization**: Independent tasks should not block each other
5. **Self-Validation**: Include commands to verify the plan worked
