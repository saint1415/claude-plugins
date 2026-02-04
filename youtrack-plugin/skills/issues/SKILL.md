# YouTrack Issues Search

<skill-description>
Search and list YouTrack issues with powerful query filters.
</skill-description>

## Prerequisites

- `YOUTRACK_URL`: YouTrack instance URL
- `YOUTRACK_TOKEN`: Permanent token with YouTrack scope

## Steps to Execute

1. **Parse Query**: Extract search parameters from user input
   - Project filter
   - State filter
   - Assignee filter
   - Text search
   - Date filters

2. **Build API Request**:
   ```bash
   curl -s -H "Authorization: Bearer $YOUTRACK_TOKEN" \
     -H "Accept: application/json" \
     "$YOUTRACK_URL/api/issues?\$top=50&fields=idReadable,summary,project(name),state(name),assignee(name),created,updated&query=<encoded-query>"
   ```

3. **Format Results**: Present in a clean table

## Output Format

```
## YouTrack Issues

### Query: project: MyProject state: Open

| ID | Summary | State | Assignee | Updated |
|----|---------|-------|----------|---------|
| PROJ-123 | Login button not working | Open | John Doe | 2h ago |
| PROJ-124 | Add password reset | Open | Jane Smith | 1d ago |
| PROJ-125 | Performance issue on dashboard | Open | Unassigned | 3d ago |

**Total: 3 issues**

### Quick Actions
- View issue: `/youtrack:issues PROJ-123`
- Update state: `/youtrack:update PROJ-123 --state "In Progress"`
```

## Query Examples

```
# All open issues in project
/youtrack:issues project: MyProject state: Open

# My issues
/youtrack:issues assignee: me

# Recently updated
/youtrack:issues updated: {last 24 hours}

# Bugs only
/youtrack:issues type: Bug state: Open

# Text search
/youtrack:issues "login error"

# Specific issue
/youtrack:issues PROJ-123
```

## Error Handling

- **401 Unauthorized**: Check YOUTRACK_TOKEN is valid
- **404 Not Found**: Check YOUTRACK_URL is correct
- **No results**: Suggest broadening query
