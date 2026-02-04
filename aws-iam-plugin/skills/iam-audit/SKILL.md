---
name: iam-audit
description: Perform a comprehensive IAM security audit of your AWS account. Checks for overly permissive policies, unused credentials, and security best practices.
---

# AWS IAM Security Audit Skill

Perform comprehensive security analysis of IAM configuration.

## Prerequisites
- AWS CLI installed and configured (`aws configure`)
- Appropriate IAM permissions (IAMReadOnlyAccess minimum)

## Steps to Execute

1. **Check Credential Report**: Generate and analyze credential report
   ```bash
   aws iam generate-credential-report
   aws iam get-credential-report --output text --query Content | base64 -d
   ```

2. **Find Overly Permissive Policies**: Look for `*` in actions/resources
   ```bash
   aws iam list-policies --scope Local --query 'Policies[*].[PolicyName,Arn]' --output table
   ```

3. **Check for Root Account Usage**: Verify root isn't used for daily tasks

4. **MFA Status**: Check MFA enabled for all users
   ```bash
   aws iam list-virtual-mfa-devices
   ```

5. **Access Key Age**: Find old access keys (>90 days)

6. **Unused Roles**: Identify roles not used recently

## Output Format

```
## AWS IAM Security Audit

### Summary
- Total Users: X
- Total Roles: X
- Total Policies: X
- Security Score: X/100

### Critical Findings
| Issue | Severity | Resource | Recommendation |
|-------|----------|----------|----------------|
| Unused access key | High | user/admin | Rotate or delete |
| Missing MFA | High | user/jsmith | Enable MFA |
| Overly permissive | Medium | policy/DevOps | Restrict resources |

### Users Without MFA
- user1@example.com
- user2@example.com

### Old Access Keys (>90 days)
| User | Key ID | Age | Last Used |
|------|--------|-----|-----------|
| admin | AKIA... | 180d | 30d ago |

### Overly Permissive Policies
- AdminAccess: Action: *, Resource: *
- DevOpsPolicy: s3:*, ec2:*

### Recommendations
1. Enable MFA for all IAM users
2. Rotate access keys older than 90 days
3. Review and restrict overly permissive policies
```

## Example Usage
User: `/aws:iam-audit`
User: `/aws:iam-audit --profile production`
