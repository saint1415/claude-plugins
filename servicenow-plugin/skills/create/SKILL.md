---
name: create
description: Create a new ServiceNow incident or request. Use when a user needs to submit a new ticket.
---

# ServiceNow Create Ticket Skill

Create new incidents or service requests in ServiceNow.

## Prerequisites
Set these environment variables:
- `SNOW_INSTANCE`: Your ServiceNow instance
- `SNOW_USER`: ServiceNow username
- `SNOW_PASSWORD`: ServiceNow password

## Steps to Execute

1. **Gather Information**: Ask user for required fields if not provided:
   - Short description (required)
   - Description/details
   - Category
   - Priority/Impact/Urgency
   - Assignment group (optional)

2. **Build API Request**: Construct POST request
   ```bash
   curl -s -X POST \
     -u "$SNOW_USER:$SNOW_PASSWORD" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -d '{"short_description":"...","description":"...","category":"..."}' \
     "https://$SNOW_INSTANCE/api/now/table/incident"
   ```

3. **Parse Response**: Extract ticket number and sys_id from response

4. **Confirm Creation**: Display the new ticket details

## Output Format

```
## Ticket Created Successfully

| Field | Value |
|-------|-------|
| Number | INC0012345 |
| Short Description | {description} |
| State | New |
| Priority | {priority} |
| Assignment Group | {group} |

### Next Steps
- View ticket: `/snow:query INC0012345`
- Update ticket: `/snow:update INC0012345`
- ServiceNow link: https://{instance}/incident.do?sys_id={sys_id}
```

## Example Usage
User: `/snow:create Password reset needed for user jsmith`
User: `/snow:create short_description="VPN not connecting" priority=2 category=Network`
