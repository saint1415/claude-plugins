---
name: update
description: Update an existing ServiceNow ticket. Use to add notes, change status, reassign, or modify ticket fields.
---

# ServiceNow Update Ticket Skill

Modify existing incidents or service requests.

## Prerequisites
Set these environment variables:
- `SNOW_INSTANCE`: Your ServiceNow instance
- `SNOW_USER`: ServiceNow username
- `SNOW_PASSWORD`: ServiceNow password

## Steps to Execute

1. **Identify Ticket**: Extract ticket number from input (e.g., INC0012345)

2. **Get Current State**: First query the ticket to show current values
   ```bash
   curl -s -u "$SNOW_USER:$SNOW_PASSWORD" \
     -H "Accept: application/json" \
     "https://$SNOW_INSTANCE/api/now/table/incident?sysparm_query=number={number}"
   ```

3. **Parse Update Request**: Identify what fields to update:
   - `state`: Change ticket state (1=New, 2=In Progress, 3=On Hold, 6=Resolved, 7=Closed)
   - `work_notes`: Add internal notes
   - `comments`: Add customer-visible notes
   - `assigned_to`: Reassign ticket
   - `close_code`/`close_notes`: For closing tickets

4. **Execute Update**: PATCH request to update
   ```bash
   curl -s -X PATCH \
     -u "$SNOW_USER:$SNOW_PASSWORD" \
     -H "Content-Type: application/json" \
     -d '{"work_notes":"...","state":"2"}' \
     "https://$SNOW_INSTANCE/api/now/table/incident/{sys_id}"
   ```

## Output Format

```
## Ticket Updated: INC0012345

### Changes Made
| Field | Old Value | New Value |
|-------|-----------|-----------|
| State | New | In Progress |
| Work Notes | - | Added note |

### Current Ticket Status
- State: In Progress
- Assigned To: John Doe
- Last Updated: {timestamp}

### Quick Actions
- Add note: `/snow:update INC0012345 note="Working on this"`
- Resolve: `/snow:update INC0012345 state=resolved`
```

## Example Usage
User: `/snow:update INC0012345 state=in_progress`
User: `/snow:update INC0012345 note="Contacted user, awaiting response"`
User: `/snow:update INC0012345 assign=jsmith`
