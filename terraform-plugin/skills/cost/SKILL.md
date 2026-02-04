---
name: cost
description: Estimate infrastructure costs from Terraform plan using Infracost or similar tools.
---

# Terraform Cost Estimation Skill

Estimate infrastructure costs.

## Steps

1. **Run Cost Estimation**:
   ```bash
   infracost breakdown --path .
   ```

2. **Output**:
   ```
   ## Infrastructure Cost Estimate

   ### Monthly Cost Summary
   | Category | Current | Planned | Diff |
   |----------|---------|---------|------|
   | Compute | $100 | $130 | +$30 |
   | Storage | $50 | $50 | $0 |
   | Network | $25 | $35 | +$10 |
   | **Total** | **$175** | **$215** | **+$40** |

   ### Cost by Resource
   | Resource | Type | Monthly |
   |----------|------|---------|
   | aws_instance.web | t3.large | $60 |
   | aws_rds_cluster.db | db.r5.large | $100 |
   | aws_lb.main | ALB | $20 |

   ### Cost Saving Suggestions
   - Use Reserved Instances: save ~30%
   - Consider spot instances for web: save ~60%
   ```

## Example Usage
- `/tf:cost`
- `/tf:cost --compare main`
