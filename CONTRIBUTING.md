# Contributing to Claude Code Custom Plugins

Thank you for your interest in contributing! This document provides guidelines for contributing to this plugin collection.

## Table of Contents

- [Getting Started](#getting-started)
- [Plugin Architecture](#plugin-architecture)
- [Creating a New Plugin](#creating-a-new-plugin)
- [Skill Development](#skill-development)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Code Style](#code-style)

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/claude-plugins.git
   cd claude-plugins
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/my-new-plugin
   ```

## Plugin Architecture

Each plugin follows a standard directory structure:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Required: Plugin manifest
├── skills/
│   └── skill-name/
│       └── SKILL.md         # Required: Skill definition
├── agents/                   # Optional: Custom agent definitions
│   └── agent-name.md
├── hooks/                    # Optional: Lifecycle hooks
│   ├── pre_tool_use.py
│   └── post_tool_use.py
├── scripts/                  # Optional: Helper scripts
│   └── helper.py
├── references/               # Optional: Reference documentation
│   └── docs.md
└── README.md                 # Recommended: Plugin documentation
```

### Plugin Manifest (plugin.json)

```json
{
  "name": "my-plugin",
  "description": "Brief description (shown in plugin list)",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "url": "https://github.com/username"
  },
  "keywords": ["category", "feature", "technology"],
  "repository": "https://github.com/username/repo"
}
```

## Creating a New Plugin

### Step 1: Create Directory Structure

```bash
mkdir -p my-plugin/.claude-plugin my-plugin/skills/my-skill
```

### Step 2: Create Plugin Manifest

Create `.claude-plugin/plugin.json`:

```json
{
  "name": "my-plugin",
  "description": "What this plugin does",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  },
  "keywords": ["keyword1", "keyword2"]
}
```

### Step 3: Create Your First Skill

Create `skills/my-skill/SKILL.md`:

```markdown
# My Skill

<skill-description>
One-line description shown in help output.
</skill-description>

## Overview

Detailed explanation of what this skill does and when to use it.

## Instructions

Step-by-step instructions for Claude on how to execute this skill:

1. First, analyze the user's request
2. Then, perform the necessary actions
3. Finally, present the results

## Parameters

- `param1`: Description of parameter 1
- `param2`: Description of parameter 2 (optional)

## Examples

### Basic Usage
```
/my-plugin:my-skill parameter1
```

### Advanced Usage
```
/my-plugin:my-skill parameter1 --option value
```

## Notes

- Important considerations
- Limitations or requirements
```

### Step 4: Test Your Plugin

```bash
claude --plugin-dir ./my-plugin
```

Then try your skill:
```
/my-plugin:my-skill test
```

## Skill Development

### Best Practices

1. **Clear Instructions**: Write explicit, step-by-step instructions for Claude
2. **Examples**: Include multiple examples covering common use cases
3. **Error Handling**: Describe how to handle edge cases and errors
4. **Documentation**: Document all parameters and options

### Skill Types

#### Information Skills
Provide expert knowledge and guidance:
```markdown
## Instructions

When the user invokes this skill:
1. Understand their specific question or context
2. Provide relevant expert knowledge
3. Include practical examples
4. Suggest next steps if appropriate
```

#### Action Skills
Perform specific tasks:
```markdown
## Instructions

When the user invokes this skill with `<target>`:
1. Validate the input
2. Execute the necessary commands using Bash tool
3. Parse and format the output
4. Present results clearly
```

#### Analysis Skills
Analyze data or code:
```markdown
## Instructions

When the user provides `<input>`:
1. Read and understand the input
2. Apply analysis criteria
3. Identify issues or insights
4. Provide actionable recommendations
```

### Adding References

For complex skills, include reference documentation:

```
skills/my-skill/
├── SKILL.md
└── references/
    ├── best_practices.md
    └── examples.md
```

Reference in SKILL.md:
```markdown
## References

See the following documents for detailed information:
- [Best Practices](./references/best_practices.md)
- [Examples](./references/examples.md)
```

### Adding Scripts

For skills that need helper scripts:

```
skills/my-skill/
├── SKILL.md
└── scripts/
    └── analyzer.py
```

Reference in SKILL.md:
```markdown
## Implementation

Use the helper script at `scripts/analyzer.py`:
```bash
python scripts/analyzer.py --input <file>
```
```

## Testing

### Manual Testing

1. Load your plugin:
   ```bash
   claude --plugin-dir ./my-plugin
   ```

2. Verify skill appears in help:
   ```
   /help
   ```

3. Test each skill with various inputs:
   ```
   /my-plugin:my-skill basic-test
   /my-plugin:my-skill edge-case
   /my-plugin:my-skill error-input
   ```

### Checklist

- [ ] Plugin loads without errors
- [ ] All skills appear in `/help` output
- [ ] Skills execute correctly with valid input
- [ ] Skills handle invalid input gracefully
- [ ] Documentation is clear and complete
- [ ] Examples work as documented

## Pull Request Process

1. **Update Documentation**: Ensure README.md reflects your changes
2. **Test Thoroughly**: Verify all skills work correctly
3. **Commit with Clear Messages**:
   ```bash
   git add .
   git commit -m "Add my-plugin with skill1, skill2 skills

   - Skill1 does X
   - Skill2 does Y

"
   ```
4. **Push to Your Fork**:
   ```bash
   git push origin feature/my-new-plugin
   ```
5. **Create Pull Request**: Include:
   - Description of the plugin/changes
   - List of new skills added
   - Any dependencies or requirements
   - Testing performed

## Code Style

### Markdown

- Use ATX-style headers (`#`, `##`, `###`)
- Include blank lines before and after code blocks
- Use fenced code blocks with language identifiers
- Keep lines under 100 characters when possible

### Python (for scripts/hooks)

- Follow PEP 8 style guide
- Use type hints where appropriate
- Include docstrings for functions
- Handle exceptions gracefully

### JSON

- Use 2-space indentation
- Include all required fields
- Validate JSON syntax before committing

## Questions?

If you have questions about contributing, please:
1. Check existing plugins for examples
2. Review the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code)
3. Open an issue for discussion

Thank you for contributing!
