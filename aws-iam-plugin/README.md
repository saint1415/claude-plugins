# AWS IAM Plugin for Claude Code

AWS Identity and Access Management security analysis tools.

## Commands

| Command | Description |
|---------|-------------|
| `/aws:iam-audit` | Comprehensive IAM security audit |
| `/aws:who-can <action>` | Find who can perform an action |
| `/aws:unused-roles` | List unused IAM roles |
| `/aws:policy-check <policy>` | Analyze policy for security issues |

## Agents

| Agent | Description |
|-------|-------------|
| `iam-analyzer` | Deep IAM security analysis with remediation guidance |

## Installation

```bash
claude --plugin-dir /path/to/aws-iam-plugin
```

## Prerequisites

- AWS CLI installed and configured (`aws configure`)
- IAM permissions: IAMReadOnlyAccess minimum
- For full audit: IAMFullAccess or specific permissions

## Examples

```
# Full IAM audit
/aws:iam-audit
/aws:iam-audit --profile production

# Find who can delete S3 buckets
/aws:who-can s3:DeleteBucket
/aws:who-can ec2:TerminateInstances

# Find unused roles
/aws:unused-roles
/aws:unused-roles --days 60

# Analyze a policy
/aws:policy-check arn:aws:iam::123456789:policy/MyPolicy
/aws:policy-check '{"Version":"2012-10-17","Statement":[...]}'
```

## Security Checks Performed

### IAM Audit
- Root account usage
- MFA enforcement
- Access key age and rotation
- Unused credentials
- Overly permissive policies

### Policy Check
- `Action: *` detection
- `Resource: *` detection
- Missing conditions
- Dangerous service combinations
- Best practice violations

## AWS CLI Commands Used

```bash
aws iam get-account-summary
aws iam generate-credential-report
aws iam list-users
aws iam list-roles
aws iam simulate-principal-policy
aws iam get-policy-version
```
