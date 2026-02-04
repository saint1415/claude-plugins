---
name: my-tickets
description: List all tickets assigned to you or your team. Use for a quick view of your current workload.
---

# My ServiceNow Tickets Skill

View tickets assigned to you or your team.

## Prerequisites
Set these environment variables:
- `SNOW_INSTANCE`: Your ServiceNow instance
- `SNOW_USER`: ServiceNow username
- `SNOW_PASSWORD`: ServiceNow password
- `SNOW_USER_ID` (optional): Your ServiceNow user sys_id for faster queries

## Steps to Execute

1. **Determine Scope**: Check if user wants:
   - Their personal tickets (default)
   - Team/group tickets
   - Specific status filter

2. **Build Query**: Construct appropriate filter
   ```
   # Personal tickets
   assigned_to.user_name={username}^stateNOT IN6,7

   # Team tickets
   assignment_group.name={group}^stateNOT IN6,7
   ```

3. **Execute Query**:
   ```bash
   curl -s -u "$SNOW_USER:$SNOW_PASSWORD" \
     -H "Accept: application/json" \
     "https://$SNOW_INSTANCE/api/now/table/incident?sysparm_query={query}&sysparm_limit=25&sysparm_display_value=true"
   ```

4. **Format Results**: Group by priority/state for easy scanning

## Output Format

```
## My Open Tickets

### Summary
- Total Open: X tickets
- High Priority: X
- In Progress: X
- On Hold: X

### High Priority (P1/P2)
| Number | Description | State | Age |
|--------|-------------|-------|-----|
| INC001 | Server down | In Progress | 2h |

### Normal Priority
| Number | Description | State | Age |
|--------|-------------|-------|-----|
| INC002 | Password reset | New | 1d |
| INC003 | VPN issue | On Hold | 3d |

### Quick Actions
- View ticket: `/snow:query {number}`
- Update ticket: `/snow:update {number}`
```

## Example Usage
User: `/snow:my-tickets`
User: `/snow:my-tickets team=IT Support`
User: `/snow:my-tickets state=in_progress`
