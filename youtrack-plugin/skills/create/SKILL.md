# YouTrack Create Issue

<skill-description>
Create new issues in YouTrack with specified fields.
</skill-description>

## Prerequisites

- `YOUTRACK_URL`: YouTrack instance URL
- `YOUTRACK_TOKEN`: Permanent token with write access

## Steps to Execute

1. **Parse Input**: Extract issue details
   - Project (required)
   - Summary (required)
   - Description (optional)
   - Type (optional, default: Task)
   - Priority (optional)
   - Assignee (optional)

2. **Create Issue**:
   ```bash
   curl -s -X POST "$YOUTRACK_URL/api/issues?fields=idReadable,summary" \
     -H "Authorization: Bearer $YOUTRACK_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "project": {"id": "<project-id>"},
       "summary": "<summary>",
       "description": "<description>"
     }'
   ```

3. **Set Custom Fields** (if needed):
   ```bash
   curl -s -X POST "$YOUTRACK_URL/api/issues/<id>/fields/Type" \
     -H "Authorization: Bearer $YOUTRACK_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"name": "Bug"}'
   ```

4. **Confirm Creation**: Return issue ID and link

## Output Format

```
## Issue Created

**ID:** PROJ-126
**URL:** https://your-instance.youtrack.cloud/issue/PROJ-126

| Field | Value |
|-------|-------|
| Summary | Login button not responding |
| Project | MyProject |
| Type | Bug |
| State | Open |
| Assignee | Unassigned |

### Next Steps
- Assign: `/youtrack:update PROJ-126 --assignee john.doe`
- Set priority: `/youtrack:update PROJ-126 --priority Critical`
- Add to sprint: `/youtrack:update PROJ-126 --sprint "Sprint 5"`
```

## Examples

```
# Basic issue
/youtrack:create --project MyProject --summary "Fix login bug"

# With description
/youtrack:create --project MyProject --summary "Add dark mode" --description "Users want a dark theme option for the dashboard"

# Bug with priority
/youtrack:create --project MyProject --summary "Crash on startup" --type Bug --priority Critical

# Assigned issue
/youtrack:create --project MyProject --summary "Review PR #45" --assignee john.doe
```

## Field Reference

| Field | API Name | Values |
|-------|----------|--------|
| Type | Type | Bug, Feature, Task, Epic |
| Priority | Priority | Critical, Major, Normal, Minor |
| State | State | Open, In Progress, Done |
| Assignee | Assignee | username or "Unassigned" |
