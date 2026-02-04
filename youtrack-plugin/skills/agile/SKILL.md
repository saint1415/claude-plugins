# YouTrack Agile Boards

<skill-description>
View agile boards, sprints, and backlog status.
</skill-description>

## Prerequisites

- `YOUTRACK_URL`: YouTrack instance URL
- `YOUTRACK_TOKEN`: Permanent token

## Steps to Execute

1. **List Agile Boards**:
   ```bash
   curl -s -H "Authorization: Bearer $YOUTRACK_TOKEN" \
     -H "Accept: application/json" \
     "$YOUTRACK_URL/api/agiles?fields=id,name,projects(name),currentSprint(name)"
   ```

2. **Get Sprint Details** (if board specified):
   ```bash
   curl -s -H "Authorization: Bearer $YOUTRACK_TOKEN" \
     -H "Accept: application/json" \
     "$YOUTRACK_URL/api/agiles/<board-id>/sprints?fields=id,name,start,finish,issues(idReadable,summary,state(name))"
   ```

3. **Calculate Sprint Metrics**:
   - Total issues
   - Completed vs remaining
   - Issues by state

## Output Format

```
## Agile Boards

| Board | Projects | Current Sprint |
|-------|----------|----------------|
| Development | MyProject, Backend | Sprint 5 |
| Mobile | iOS, Android | Sprint 12 |

---

## Sprint: Sprint 5 (Development)

**Duration:** Jan 15 - Jan 29, 2026
**Progress:** 12/20 issues (60%)

### By State

| State | Count | Issues |
|-------|-------|--------|
| Done | 8 | PROJ-101, PROJ-102, ... |
| In Progress | 4 | PROJ-110, PROJ-111, ... |
| Open | 8 | PROJ-115, PROJ-116, ... |

### Sprint Progress
[████████████░░░░░░░░] 60%

### Burndown
- Day 1: 20 issues
- Day 5: 16 issues
- Day 10 (today): 12 issues
- Remaining days: 4

### At Risk
- PROJ-115: No activity in 3 days
- PROJ-116: Blocked by external dependency

---

### Quick Actions
- View board: [Sprint 5](https://your-instance.youtrack.cloud/agiles/...)
- Add to sprint: `/youtrack:update <ID> --sprint "Sprint 5"`
```

## Examples

```
# List all boards
/youtrack:agile

# View specific board
/youtrack:agile --board "Development"

# View specific sprint
/youtrack:agile --board "Development" --sprint "Sprint 5"

# View backlog
/youtrack:agile --board "Development" --backlog
```
