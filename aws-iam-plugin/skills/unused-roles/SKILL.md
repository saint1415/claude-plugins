---
name: unused-roles
description: Find IAM roles that haven't been used recently. Helps identify roles that can be cleaned up for better security hygiene.
---

# AWS Unused Roles Skill

Identify IAM roles not used within a specified timeframe.

## Prerequisites
- AWS CLI configured
- IAM permissions to list and describe roles
- Access Analyzer enabled (optional, for better data)

## Steps to Execute

1. **List All Roles**: Get all IAM roles
   ```bash
   aws iam list-roles --query 'Roles[*].[RoleName,Arn,CreateDate]' --output json
   ```

2. **Check Last Used**: For each role, get usage info
   ```bash
   aws iam get-role --role-name ROLE_NAME \
     --query 'Role.RoleLastUsed' --output json
   ```

3. **Check Access Analyzer** (if enabled):
   ```bash
   aws accessanalyzer list-findings \
     --analyzer-name ANALYZER_NAME \
     --filter 'resourceType={"eq":["AWS::IAM::Role"]}'
   ```

4. **Calculate Age**: Compare last used date with threshold (default 90 days)

5. **Categorize Results**: Group by severity

## Output Format

```
## Unused IAM Roles Report

### Summary
- Total Roles: X
- Never Used: X
- Not Used in 90+ days: X
- Not Used in 30-90 days: X

### Never Used Roles
| Role Name | Created | Description |
|-----------|---------|-------------|
| old-lambda-role | 2023-01-15 | Lambda execution |
| test-role | 2022-06-20 | Testing |

### Not Used in 90+ Days
| Role Name | Last Used | Days Inactive |
|-----------|-----------|---------------|
| dev-deploy | 2023-10-01 | 120 |
| admin-temp | 2023-09-15 | 135 |

### Roles to Review (30-90 days)
| Role Name | Last Used | Days Inactive |
|-----------|-----------|---------------|
| ci-runner | 2024-01-01 | 45 |

### Recommendations
1. Delete roles never used: old-lambda-role, test-role
2. Review 90+ day inactive roles with team
3. Set up CloudWatch alerts for role usage

### Cleanup Commands
```bash
# Review before running!
aws iam delete-role --role-name old-lambda-role
aws iam delete-role --role-name test-role
```
```

## Example Usage
User: `/aws:unused-roles`
User: `/aws:unused-roles --days 60`
User: `/aws:unused-roles --profile production`
