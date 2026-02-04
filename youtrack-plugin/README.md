# YouTrack Plugin for Claude Code

JetBrains YouTrack issue tracking and project management integration.

## Skills

| Skill | Description |
|-------|-------------|
| `/youtrack:issues` | Search and list issues |
| `/youtrack:create` | Create new issue |
| `/youtrack:update` | Update issue state/fields |
| `/youtrack:my-issues` | List your assigned issues |
| `/youtrack:agile` | View agile boards and sprints |

## Configuration

### Environment Variables

```bash
export YOUTRACK_URL="https://your-instance.youtrack.cloud"
export YOUTRACK_TOKEN="perm:your-permanent-token"
```

### Getting a Permanent Token

1. Go to YouTrack → Profile → Account Security
2. Click "New token..."
3. Give it a name and select scopes:
   - `YouTrack`
   - `Read` and `Write` for issues
4. Copy the token to `YOUTRACK_TOKEN`

## API Reference

Base URL: `{YOUTRACK_URL}/api`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/issues` | GET | List/search issues |
| `/issues` | POST | Create issue |
| `/issues/{id}` | POST | Update issue |
| `/issues/{id}/fields` | GET | Get issue fields |
| `/agiles` | GET | List agile boards |
| `/agiles/{id}/sprints` | GET | List sprints |

## Examples

```
# Search issues
/youtrack:issues project: MyProject state: Open

# Create issue
/youtrack:create --project MyProject --summary "Bug in login" --type Bug

# Update issue
/youtrack:update PROJ-123 --state "In Progress"

# My assigned issues
/youtrack:my-issues

# View sprint board
/youtrack:agile --board "Development"
```

## Query Syntax

YouTrack uses a powerful query language:

```
# By project
project: ProjectName

# By state
state: Open, "In Progress"

# By assignee
assignee: me
assignee: john.doe

# By type
type: Bug, Feature

# Combinations
project: MyProject state: Open assignee: me

# Text search
summary: login error

# Date filters
created: today
updated: {last week}
```
