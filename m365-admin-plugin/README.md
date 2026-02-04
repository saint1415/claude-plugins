# M365 Admin Plugin for Claude Code

Microsoft 365 and Azure AD administration tools.

## Commands

| Command | Description |
|---------|-------------|
| `/m365:user <email>` | Look up user details, licenses, groups |
| `/m365:audit <query>` | Search audit logs for activities |
| `/m365:risky-users` | List users flagged by Identity Protection |
| `/m365:licenses` | Check license availability and usage |

## Installation

```bash
claude --plugin-dir /path/to/m365-admin-plugin
```

## Configuration (Required)

### Option 1: App Registration (Recommended)

1. Create Azure AD App Registration
2. Grant API permissions:
   - User.Read.All
   - Directory.Read.All
   - AuditLog.Read.All
   - IdentityRiskUser.Read.All
   - Organization.Read.All

3. Set environment variables:
```bash
export M365_TENANT_ID="your-tenant-id"
export M365_CLIENT_ID="your-client-id"
export M365_CLIENT_SECRET="your-client-secret"
```

### Option 2: Microsoft Graph PowerShell

Install and connect:
```powershell
Install-Module Microsoft.Graph
Connect-MgGraph -Scopes "User.Read.All","Directory.Read.All"
```

## Examples

```
# User lookup
/m365:user jsmith@company.com
/m365:user "John Smith"

# Audit log search
/m365:audit jsmith@company.com
/m365:audit admin actions last 30 days
/m365:audit failed signins

# Risky users
/m365:risky-users
/m365:risky-users --level high

# License report
/m365:licenses
/m365:licenses --sku "Microsoft 365 E5"
```

## Microsoft Graph API Endpoints

| Skill | Endpoint |
|-------|----------|
| User | `/users/{id}` |
| Audit | `/auditLogs/directoryAudits`, `/auditLogs/signIns` |
| Risky Users | `/identityProtection/riskyUsers` |
| Licenses | `/subscribedSkus` |

## License Requirements

| Feature | License Required |
|---------|------------------|
| User lookup | Any M365 |
| Audit logs | M365 E3+ |
| Risky users | Azure AD P2 |
| License report | Any M365 |
