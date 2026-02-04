---
name: audit
description: Search Microsoft 365 audit logs for user activities, admin actions, and security events. Use for investigating incidents or compliance reporting.
---

# M365 Audit Log Search Skill

Search unified audit logs in Microsoft 365.

## Prerequisites
- Microsoft Graph API access with AuditLog.Read.All permission
- Or Office 365 Management API credentials

## Steps to Execute

1. **Parse Query**: Extract search parameters:
   - User(s) to search
   - Date range (default: last 7 days)
   - Activity types
   - Record type (Exchange, SharePoint, Azure AD, etc.)

2. **Build Search**: Construct audit log query
   ```bash
   # Using Microsoft Graph
   curl -s -H "Authorization: Bearer $TOKEN" \
     "https://graph.microsoft.com/v1.0/auditLogs/directoryAudits?\$filter=activityDateTime ge 2024-01-01"
   ```

3. **For Sign-in Logs**:
   ```bash
   curl -s -H "Authorization: Bearer $TOKEN" \
     "https://graph.microsoft.com/v1.0/auditLogs/signIns?\$filter=userPrincipalName eq 'user@domain.com'"
   ```

4. **Filter and Format**: Process results based on user request

## Output Format

```
## Audit Log Search Results

### Query
- User: jsmith@company.com
- Date Range: 2024-01-08 to 2024-01-15
- Activity Types: All

### Summary
- Total Events: 156
- Admin Actions: 12
- Sign-ins: 89
- File Activities: 45
- Mailbox Activities: 10

### Recent Activity (Last 24h)

| Time | Activity | Target | IP Address | Result |
|------|----------|--------|------------|--------|
| 09:30 | Sign-in | - | 203.0.113.1 | Success |
| 09:35 | FileAccessed | report.xlsx | 203.0.113.1 | Success |
| 10:00 | MailItemsAccessed | Inbox | 203.0.113.1 | Success |

### Admin Actions

| Time | Admin | Action | Target | Details |
|------|-------|--------|--------|---------|
| 08:00 | admin@company.com | UserPasswordReset | jsmith | Forced reset |
| 07:45 | admin@company.com | GroupMemberAdded | VPN-Users | Added jsmith |

### Sign-in Analysis
- Unique Locations: 2 (New York, Home IP)
- Unique Devices: 3
- Failed Attempts: 2
- MFA Prompted: 5 times

### Suspicious Activity
- None detected

### Export Options
- CSV: [Download link]
- JSON: [Download link]
```

## Example Usage
User: `/m365:audit jsmith@company.com`
User: `/m365:audit admin actions last 30 days`
User: `/m365:audit failed signins`
User: `/m365:audit password changes`
