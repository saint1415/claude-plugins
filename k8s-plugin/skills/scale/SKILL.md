---
name: scale
description: Scale Kubernetes deployments, statefulsets, and replicasets up or down.
---

# K8s Scale Skill

Scale workloads up or down.

## Steps

1. **Check Current Scale**:
   ```bash
   kubectl get deployment {name} -o jsonpath='{.spec.replicas}'
   ```

2. **Scale**:
   ```bash
   kubectl scale deployment {name} --replicas={count}
   ```

3. **Output**:
   ```
   ## Scaling: {deployment}

   ### Before
   - Replicas: 3
   - Ready: 3/3

   ### After
   - Target Replicas: 5
   - Status: Scaling...

   ### Progress
   | Pod | Status |
   |-----|--------|
   | app-abc | Running |
   | app-def | Running |
   | app-ghi | Running |
   | app-jkl | Pending |
   | app-mno | Pending |

   ### Command Used
   ```bash
   kubectl scale deployment my-app --replicas=5
   ```
   ```

## Example Usage
- `/k8s:scale deployment/my-app 5`
- `/k8s:scale statefulset/db 3`
- `/k8s:scale deployment/my-app --auto` (HPA info)
