---
name: plan
description: Run terraform plan and summarize changes in a readable format.
---

# Terraform Plan Skill

Preview infrastructure changes.

## Steps

1. **Run Plan**:
   ```bash
   terraform plan -out=tfplan
   terraform show -json tfplan
   ```

2. **Output**:
   ```
   ## Terraform Plan Summary

   ### Changes
   | Action | Count |
   |--------|-------|
   | Create | 3 |
   | Update | 2 |
   | Delete | 1 |

   ### Resources to Create
   - aws_instance.web (t3.medium)
   - aws_security_group.web
   - aws_lb.main

   ### Resources to Update
   - aws_instance.api (tags changed)
   - aws_rds_cluster.db (storage increased)

   ### Resources to Delete
   - aws_instance.old_web

   ### Estimated Cost Impact
   - Current: $150/month
   - After: $180/month
   - Change: +$30/month
   ```

## Example Usage
- `/tf:plan`
- `/tf:plan --target=aws_instance.web`
