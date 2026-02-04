---
name: query
description: Search ServiceNow incidents, requests, or other records by query string. Use when looking up tickets or finding related incidents.
---

# ServiceNow Query Skill

Search ServiceNow records using various criteria.

## Prerequisites
Set these environment variables:
- `SNOW_INSTANCE`: Your ServiceNow instance (e.g., company.service-now.com)
- `SNOW_USER`: ServiceNow username
- `SNOW_PASSWORD`: ServiceNow password (or use OAuth token)

## Steps to Execute

1. **Parse Query**: Extract search terms from user input (ticket number, keywords, status, etc.)

2. **Build API Request**: Construct ServiceNow Table API query
   ```
   GET https://{instance}/api/now/table/incident
   ?sysparm_query={encoded_query}
   &sysparm_limit=10
   &sysparm_display_value=true
   ```

3. **Execute Request**: Use curl via Bash with basic auth:
   ```bash
   curl -s -u "$SNOW_USER:$SNOW_PASSWORD" \
     -H "Accept: application/json" \
     "https://$SNOW_INSTANCE/api/now/table/incident?sysparm_query=..."
   ```

4. **Format Results**: Present findings in a readable table

## Query Examples
- By number: `number=INC0012345`
- By short description: `short_descriptionLIKEpassword reset`
- By state: `state=2` (In Progress)
- By assignment group: `assignment_group.name=IT Support`

## Output Format

```
## ServiceNow Search Results

Found X records matching "{query}"

| Number | Short Description | State | Assigned To | Updated |
|--------|-------------------|-------|-------------|---------|
| INC001 | Password reset    | Open  | John Doe    | 2024-01-15 |
| ...    | ...               | ...   | ...         | ...     |

### Quick Actions
- View details: `/snow:query INC0012345`
- Update ticket: `/snow:update INC0012345`
```

## Example Usage
User: `/snow:query password reset`
User: `/snow:query INC0012345`
User: `/snow:query state=1 assignment_group=IT`
