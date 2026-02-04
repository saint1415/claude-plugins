---
name: user
description: Look up Microsoft 365 user details including profile, licenses, group memberships, and sign-in activity. Use for quick user administration queries.
---

# M365 User Lookup Skill

Query user information from Microsoft 365 / Entra ID.

## Prerequisites
Set environment variables:
- `M365_TENANT_ID`: Azure AD tenant ID
- `M365_CLIENT_ID`: App registration client ID
- `M365_CLIENT_SECRET`: App registration secret

Or use Microsoft Graph PowerShell if available.

## Steps to Execute

1. **Authenticate**: Get access token for Microsoft Graph
   ```bash
   # Get access token
   curl -X POST "https://login.microsoftonline.com/$M365_TENANT_ID/oauth2/v2.0/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "client_id=$M365_CLIENT_ID&scope=https://graph.microsoft.com/.default&client_secret=$M365_CLIENT_SECRET&grant_type=client_credentials"
   ```

2. **Query User**: Search by email, UPN, or display name
   ```bash
   curl -s -H "Authorization: Bearer $TOKEN" \
     "https://graph.microsoft.com/v1.0/users?`$filter=userPrincipalName eq 'user@domain.com'"
   ```

3. **Get Additional Info**:
   - Licenses: `GET /users/{id}/licenseDetails`
   - Groups: `GET /users/{id}/memberOf`
   - Sign-in activity: `GET /users/{id}?$select=signInActivity`
   - Manager: `GET /users/{id}/manager`

## Output Format

```
## User Profile: {displayName}

### Basic Info
| Field | Value |
|-------|-------|
| Display Name | John Smith |
| UPN | jsmith@company.com |
| Email | jsmith@company.com |
| Job Title | IT Administrator |
| Department | Information Technology |
| Office | New York |
| Manager | Jane Doe |

### Account Status
- Account Enabled: Yes
- Last Sign-in: 2024-01-15 09:30 UTC
- MFA Registered: Yes
- Password Last Changed: 2023-12-01
- Account Created: 2020-05-15

### Licenses
| License | Service Plans |
|---------|---------------|
| Microsoft 365 E5 | Exchange, Teams, SharePoint |
| Power BI Pro | Power BI |

### Group Memberships
- All Employees (Security)
- IT-Department (Microsoft 365)
- VPN-Users (Security)

### Quick Actions
- Reset password: [PowerShell command]
- Disable account: [PowerShell command]
- Remove license: [PowerShell command]
```

## Example Usage
User: `/m365:user jsmith@company.com`
User: `/m365:user "John Smith"`
User: `/m365:user --disabled` (list disabled accounts)
