---
name: who-can
description: Find all IAM principals (users, roles, groups) that can perform a specific action on a resource. Use for access analysis and security reviews.
---

# AWS Who Can Perform Action Skill

Identify all principals with permission to perform a specific action.

## Prerequisites
- AWS CLI configured
- IAM permissions to simulate policies

## Steps to Execute

1. **Parse Input**: Extract action and resource from user query
   - Action format: `service:action` (e.g., `s3:DeleteBucket`)
   - Resource format: ARN or `*`

2. **List All Principals**: Get users, roles, and groups
   ```bash
   aws iam list-users --query 'Users[*].UserName' --output text
   aws iam list-roles --query 'Roles[*].RoleName' --output text
   ```

3. **Simulate Policy for Each**: Test if they can perform the action
   ```bash
   aws iam simulate-principal-policy \
     --policy-source-arn arn:aws:iam::ACCOUNT:user/USERNAME \
     --action-names s3:DeleteBucket \
     --resource-arns arn:aws:s3:::bucket-name
   ```

4. **Compile Results**: Group by decision (allowed/denied)

## Output Format

```
## Who Can: {action}
Resource: {resource}

### Allowed (X principals)

#### Users
| User | Policy Source | Matched Statement |
|------|---------------|-------------------|
| admin | AdministratorAccess | Allow * |
| devops | DevOpsPolicy | Allow s3:* |

#### Roles
| Role | Policy Source | Matched Statement |
|------|---------------|-------------------|
| EC2-Admin | EC2AdminRole | Allow * |

#### Via Groups
| User | Group | Policy |
|------|-------|--------|
| jsmith | Developers | DevPolicy |

### Access Paths
- admin: Direct policy attachment
- devops: Group membership (DevOps-Group)
- EC2-Admin: Trust policy allows EC2 service

### Recommendations
- X users have broad access - consider restricting
- Role EC2-Admin is overly permissive
```

## Example Usage
User: `/aws:who-can s3:DeleteBucket`
User: `/aws:who-can ec2:TerminateInstances arn:aws:ec2:us-east-1:123456789:instance/*`
User: `/aws:who-can iam:CreateUser`
