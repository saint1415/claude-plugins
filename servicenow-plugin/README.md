# ServiceNow Plugin for Claude Code

IT Service Management ticket operations from the command line.

## Commands

| Command | Description |
|---------|-------------|
| `/snow:query <search>` | Search incidents, requests, or other records |
| `/snow:create <description>` | Create a new incident |
| `/snow:update <number> <changes>` | Update an existing ticket |
| `/snow:my-tickets` | View your assigned tickets |

## Installation

```bash
claude --plugin-dir /path/to/servicenow-plugin
```

## Configuration (Required)

Set environment variables:

```bash
export SNOW_INSTANCE="company.service-now.com"
export SNOW_USER="your-username"
export SNOW_PASSWORD="your-password"
```

## Examples

```
# Search for tickets
/snow:query password reset
/snow:query INC0012345
/snow:query state=1 assignment_group=IT

# Create new incident
/snow:create Password reset needed for user jsmith

# Update ticket
/snow:update INC0012345 state=in_progress
/snow:update INC0012345 note="Working on this"

# View your tickets
/snow:my-tickets
/snow:my-tickets team=IT Support
```

## API Reference

The plugin uses the ServiceNow Table API:
- Query: `GET /api/now/table/incident`
- Create: `POST /api/now/table/incident`
- Update: `PATCH /api/now/table/incident/{sys_id}`

## State Values

| State | Value | Description |
|-------|-------|-------------|
| New | 1 | Newly created |
| In Progress | 2 | Being worked |
| On Hold | 3 | Waiting |
| Resolved | 6 | Work complete |
| Closed | 7 | Verified closed |
