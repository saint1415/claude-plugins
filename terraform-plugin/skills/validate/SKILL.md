---
name: validate
description: Validate Terraform configuration syntax and check for common issues.
---

# Terraform Validate Skill

Check configuration validity.

## Steps

1. **Validate**:
   ```bash
   terraform init -backend=false
   terraform validate
   terraform fmt -check
   ```

2. **Output**:
   ```
   ## Terraform Validation

   ### Syntax Check
   Status: VALID / INVALID

   ### Errors
   | File | Line | Error |
   |------|------|-------|
   | main.tf | 15 | Missing required argument "ami" |

   ### Warnings
   - Variable "env" declared but not used
   - Deprecated attribute "security_groups"

   ### Formatting
   - Files need formatting: 2
   - Run: `terraform fmt`

   ### Best Practices
   - Consider using terraform.tfvars
   - Add description to variables
   ```

## Example Usage
- `/tf:validate`
- `/tf:validate ./modules/vpc`
