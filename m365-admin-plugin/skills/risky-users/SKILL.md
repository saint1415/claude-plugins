---
name: risky-users
description: List users flagged as risky by Azure AD Identity Protection. Use for security monitoring and incident response.
---

# M365 Risky Users Skill

Query Azure AD Identity Protection for risky users and sign-ins.

## Prerequisites
- Microsoft Graph API access
- Permissions: IdentityRiskUser.Read.All, IdentityRiskEvent.Read.All
- Azure AD P2 license (for Identity Protection features)

## Steps to Execute

1. **Get Risky Users**: Query Identity Protection
   ```bash
   curl -s -H "Authorization: Bearer $TOKEN" \
     "https://graph.microsoft.com/v1.0/identityProtection/riskyUsers"
   ```

2. **Get Risk Detections**: Detailed risk events
   ```bash
   curl -s -H "Authorization: Bearer $TOKEN" \
     "https://graph.microsoft.com/v1.0/identityProtection/riskDetections"
   ```

3. **Categorize by Risk Level**: Group users by risk severity

4. **Get User Details**: For each risky user, fetch profile info

## Output Format

```
## Risky Users Report

### Summary
| Risk Level | Count | Action Required |
|------------|-------|-----------------|
| High | 2 | Immediate |
| Medium | 5 | Within 24h |
| Low | 12 | Review weekly |

### High Risk Users (Immediate Action)

#### 1. jsmith@company.com
| Field | Value |
|-------|-------|
| Risk Level | High |
| Risk State | atRisk |
| Risk Detail | userPerformedSecuredPasswordChange |
| Last Updated | 2024-01-15 10:30 UTC |

**Risk Detections:**
- Unfamiliar sign-in properties (High) - 2024-01-15
- Anonymous IP address (Medium) - 2024-01-14
- Impossible travel (Medium) - 2024-01-13

**Recommended Actions:**
1. Contact user to verify activity
2. Reset password if compromised
3. Revoke active sessions
4. Enable MFA if not already

#### 2. admin@company.com
| Field | Value |
|-------|-------|
| Risk Level | High |
| Risk State | confirmedCompromised |
...

### Medium Risk Users

| User | Risk Detail | Last Detection | Days at Risk |
|------|-------------|----------------|--------------|
| user1@company.com | Leaked credentials | 2024-01-10 | 5 |
| user2@company.com | Unfamiliar location | 2024-01-12 | 3 |

### Remediation Commands

```powershell
# Dismiss risk for confirmed safe user
Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/identityProtection/riskyUsers/dismiss" -Body '{"userIds":["user-id"]}'

# Confirm user compromised
Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/identityProtection/riskyUsers/confirmCompromised" -Body '{"userIds":["user-id"]}'
```
```

## Example Usage
User: `/m365:risky-users`
User: `/m365:risky-users --level high`
User: `/m365:risky-users jsmith@company.com`
