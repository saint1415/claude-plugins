# YouTrack My Issues

<skill-description>
List issues assigned to you with status overview.
</skill-description>

## Prerequisites

- `YOUTRACK_URL`: YouTrack instance URL
- `YOUTRACK_TOKEN`: Permanent token

## Steps to Execute

1. **Query Assigned Issues**:
   ```bash
   curl -s -H "Authorization: Bearer $YOUTRACK_TOKEN" \
     -H "Accept: application/json" \
     "$YOUTRACK_URL/api/issues?\$top=100&fields=idReadable,summary,project(name),state(name),priority(name),created,updated&query=assignee:me%20state:-Resolved,-Done,-Cancelled"
   ```

2. **Group by State**: Organize issues by workflow state

3. **Calculate Metrics**: Count by state and priority

## Output Format

```
## My Issues

### Summary
| State | Count |
|-------|-------|
| In Progress | 3 |
| Open | 5 |
| **Total** | **8** |

---

### In Progress (3)

| ID | Summary | Project | Priority | Updated |
|----|---------|---------|----------|---------|
| PROJ-123 | Fix login bug | MyProject | Critical | 2h ago |
| PROJ-124 | Update API docs | Backend | Normal | 1d ago |
| API-45 | Rate limiting | API | Major | 3h ago |

### Open (5)

| ID | Summary | Project | Priority | Updated |
|----|---------|---------|----------|---------|
| PROJ-125 | Add dark mode | MyProject | Normal | 5d ago |
| PROJ-126 | Refactor auth | MyProject | Minor | 1w ago |
| ... | ... | ... | ... | ... |

---

### Quick Actions
- Start issue: `/youtrack:update <ID> --state "In Progress"`
- Complete issue: `/youtrack:update <ID> --state Done`
- View all in YouTrack: [My Issues](https://your-instance.youtrack.cloud/issues?q=assignee:me)
```

## Filters

```
# Only in progress
/youtrack:my-issues --state "In Progress"

# Specific project
/youtrack:my-issues --project MyProject

# High priority only
/youtrack:my-issues --priority Critical,Major

# Include resolved
/youtrack:my-issues --all
```
