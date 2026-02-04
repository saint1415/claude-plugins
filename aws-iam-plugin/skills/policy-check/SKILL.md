---
name: policy-check
description: Analyze an IAM policy document for security issues, overly permissive statements, and best practice violations.
---

# AWS Policy Security Check Skill

Analyze IAM policy documents for security risks.

## Prerequisites
- AWS CLI configured (for managed policies)
- Or provide policy JSON directly

## Steps to Execute

1. **Get Policy Document**: Either:
   - Fetch managed policy: `aws iam get-policy-version --policy-arn ARN --version-id v1`
   - Parse inline JSON from user input
   - Read from file

2. **Analyze Statements**: For each statement check:
   - `Action: "*"` - Allows all actions (critical)
   - `Resource: "*"` - Applies to all resources (high)
   - `NotAction` / `NotResource` - Complex logic (medium)
   - Missing conditions on sensitive actions
   - `Principal: "*"` in resource policies (critical)

3. **Check Specific Patterns**:
   - `iam:*` - Full IAM access
   - `s3:*` - Full S3 access
   - `ec2:*` - Full EC2 access
   - `kms:Decrypt` without conditions
   - `sts:AssumeRole` without conditions

4. **Validate Syntax**: Check for policy errors

## Output Format

```
## Policy Analysis: {policy_name}

### Risk Score: HIGH/MEDIUM/LOW

### Summary
- Statements: X
- Allow Statements: X
- Deny Statements: X
- Critical Issues: X
- Warnings: X

### Critical Issues
| Statement | Issue | Recommendation |
|-----------|-------|----------------|
| Sid: Admin | Action: * | Restrict to specific actions |
| Sid: S3Full | Resource: * | Limit to specific buckets |

### Warnings
| Statement | Issue | Recommendation |
|-----------|-------|----------------|
| Sid: KMS | No conditions | Add kms:ViaService condition |

### Statement Breakdown

#### Statement 1: "AdminAccess"
- Effect: Allow
- Actions: * (CRITICAL - all actions allowed)
- Resources: * (CRITICAL - all resources)
- Conditions: None (WARNING - no restrictions)

### Recommendations
1. Replace `*` with specific actions needed
2. Scope resources to specific ARNs
3. Add conditions for sensitive operations
4. Consider using AWS managed policies

### Suggested Replacement
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "LimitedAccess",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```
```

## Example Usage
User: `/aws:policy-check arn:aws:iam::123456789:policy/MyPolicy`
User: `/aws:policy-check {"Version":"2012-10-17","Statement":[...]}`
User: `/aws:policy-check file://policy.json`
