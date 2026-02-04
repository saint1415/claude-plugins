---
name: licenses
description: Check Microsoft 365 license availability, usage, and assignments. Use for capacity planning and license management.
---

# M365 License Management Skill

Query and manage Microsoft 365 license inventory.

## Prerequisites
- Microsoft Graph API access
- Permissions: Organization.Read.All, Directory.Read.All

## Steps to Execute

1. **Get Subscribed SKUs**: List all licenses
   ```bash
   curl -s -H "Authorization: Bearer $TOKEN" \
     "https://graph.microsoft.com/v1.0/subscribedSkus"
   ```

2. **Calculate Availability**: For each SKU:
   - Total purchased (prepaidUnits.enabled)
   - Assigned (consumedUnits)
   - Available (prepaidUnits.enabled - consumedUnits)

3. **Get Service Plans**: Detail which services are enabled

4. **Find Users by License** (if requested):
   ```bash
   curl -s -H "Authorization: Bearer $TOKEN" \
     "https://graph.microsoft.com/v1.0/users?\$filter=assignedLicenses/any(x:x/skuId eq '{sku-id}')"
   ```

## Output Format

```
## Microsoft 365 License Report

### Summary
| Status | Count |
|--------|-------|
| Total SKUs | 8 |
| Fully Utilized | 2 |
| Near Capacity (>90%) | 1 |
| Available | 5 |

### License Inventory

| License | Purchased | Assigned | Available | % Used |
|---------|-----------|----------|-----------|--------|
| Microsoft 365 E5 | 100 | 95 | 5 | 95% |
| Microsoft 365 E3 | 500 | 423 | 77 | 85% |
| Power BI Pro | 50 | 50 | 0 | 100% |
| Visio Plan 2 | 25 | 12 | 13 | 48% |
| Project Plan 3 | 10 | 8 | 2 | 80% |

### Near Capacity Alerts
- **Microsoft 365 E5**: Only 5 licenses remaining (95% used)
- **Power BI Pro**: FULLY UTILIZED - No licenses available

### License Details

#### Microsoft 365 E5
- SKU ID: 06ebc4ee-1bb5-47dd-8120-11324bc54e06
- Purchased: 100
- Assigned: 95
- Suspended: 0

**Included Service Plans:**
| Service | Status |
|---------|--------|
| Exchange Online (Plan 2) | Enabled |
| SharePoint Online (Plan 2) | Enabled |
| Microsoft Teams | Enabled |
| Microsoft Defender for Office 365 | Enabled |
| Azure AD Premium P2 | Enabled |

### Cost Optimization Suggestions
1. 5 users have E5 but only use basic features - consider E3
2. 12 users have Power BI Pro with no activity in 90 days
3. Consider volume licensing for additional E5 needs

### Quick Actions
- Assign license: [PowerShell command]
- Remove license: [PowerShell command]
- Purchase more: [Admin center link]
```

## Example Usage
User: `/m365:licenses`
User: `/m365:licenses --sku "Microsoft 365 E5"`
User: `/m365:licenses --available`
User: `/m365:licenses --users-without "Teams"`
