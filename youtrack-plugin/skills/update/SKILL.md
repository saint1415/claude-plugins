# YouTrack Update Issue

<skill-description>
Update YouTrack issue fields, state, assignee, and custom fields.
</skill-description>

## Prerequisites

- `YOUTRACK_URL`: YouTrack instance URL
- `YOUTRACK_TOKEN`: Permanent token with write access

## Steps to Execute

1. **Parse Input**: Extract issue ID and fields to update
   - Issue ID (required)
   - State
   - Assignee
   - Priority
   - Sprint
   - Comment

2. **Update Fields**:
   ```bash
   # Update state
   curl -s -X POST "$YOUTRACK_URL/api/issues/<id>/fields/State" \
     -H "Authorization: Bearer $YOUTRACK_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"name": "In Progress"}'

   # Update assignee
   curl -s -X POST "$YOUTRACK_URL/api/issues/<id>/fields/Assignee" \
     -H "Authorization: Bearer $YOUTRACK_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"login": "john.doe"}'
   ```

3. **Add Comment** (if provided):
   ```bash
   curl -s -X POST "$YOUTRACK_URL/api/issues/<id>/comments" \
     -H "Authorization: Bearer $YOUTRACK_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"text": "<comment>"}'
   ```

4. **Confirm Update**: Show updated fields

## Output Format

```
## Issue Updated: PROJ-123

| Field | Old Value | New Value |
|-------|-----------|-----------|
| State | Open | In Progress |
| Assignee | Unassigned | John Doe |

**Comment Added:** "Starting work on this now"

### Current Status
- **State:** In Progress
- **Assignee:** John Doe
- **Sprint:** Sprint 5

[View in YouTrack](https://your-instance.youtrack.cloud/issue/PROJ-123)
```

## Examples

```
# Change state
/youtrack:update PROJ-123 --state "In Progress"

# Assign issue
/youtrack:update PROJ-123 --assignee john.doe

# Multiple updates
/youtrack:update PROJ-123 --state Done --comment "Fixed in commit abc123"

# Set priority
/youtrack:update PROJ-123 --priority Critical

# Add to sprint
/youtrack:update PROJ-123 --sprint "Sprint 5"

# Just add comment
/youtrack:update PROJ-123 --comment "Waiting for design review"
```

## Common Workflows

### Start Working
```
/youtrack:update PROJ-123 --state "In Progress" --assignee me
```

### Complete Issue
```
/youtrack:update PROJ-123 --state Done --comment "Completed and deployed"
```

### Reassign
```
/youtrack:update PROJ-123 --assignee jane.smith --comment "Reassigning for frontend expertise"
```
