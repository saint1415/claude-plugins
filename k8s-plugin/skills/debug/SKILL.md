---
name: debug
description: Debug Kubernetes pods and deployments - describe resources, check events, and troubleshoot issues.
---

# K8s Debug Skill

Troubleshoot Kubernetes resources.

## Steps

1. **Gather Debug Info**:
   ```bash
   kubectl describe pod {pod}
   kubectl get events --field-selector involvedObject.name={pod}
   kubectl exec -it {pod} -- /bin/sh
   ```

2. **Output**:
   ```
   ## Debugging: {resource}

   ### Pod Info
   - Status: CrashLoopBackOff
   - Restarts: 5
   - Age: 10m

   ### Recent Events
   | Time | Type | Reason | Message |
   |------|------|--------|---------|
   | 2m | Warning | BackOff | Back-off restarting |
   | 5m | Normal | Pulled | Image pulled |

   ### Container Status
   - State: Waiting
   - Reason: CrashLoopBackOff
   - Exit Code: 1
   - Last Termination: OOMKilled

   ### Resource Issues
   - Memory limit may be too low (128Mi)
   - CPU requests not set

   ### Recommendations
   1. Check logs: `kubectl logs {pod} --previous`
   2. Increase memory limit
   3. Add resource requests
   ```

## Example Usage
- `/k8s:debug my-pod`
- `/k8s:debug deployment/my-app`
