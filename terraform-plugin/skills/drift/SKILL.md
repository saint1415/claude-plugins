---
name: drift
description: Detect configuration drift between Terraform state and actual infrastructure.
---

# Terraform Drift Detection Skill

Find state vs reality differences.

## Steps

1. **Refresh and Compare**:
   ```bash
   terraform plan -refresh-only
   ```

2. **Output**:
   ```
   ## Drift Detection Report

   ### Summary
   - Resources in state: 25
   - Resources with drift: 3
   - Resources missing: 1

   ### Drifted Resources

   #### aws_instance.web
   | Attribute | Expected | Actual |
   |-----------|----------|--------|
   | instance_type | t3.medium | t3.large |
   | tags.Environment | prod | production |

   #### aws_security_group.web
   - Extra ingress rule added manually (port 8080)

   ### Missing Resources
   - aws_instance.temp (deleted outside Terraform)

   ### Remediation
   ```bash
   # Accept drift into state
   terraform apply -refresh-only

   # Or fix infrastructure
   terraform apply
   ```
   ```

## Example Usage
- `/tf:drift`
- `/tf:drift --detailed`
