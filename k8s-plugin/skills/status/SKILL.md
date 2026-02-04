---
name: status
description: Show Kubernetes cluster and workload status including pods, deployments, services, and resource usage.
---

# K8s Status Skill

Overview of cluster health and workloads.

## Steps

1. **Get Cluster Status**:
   ```bash
   kubectl cluster-info
   kubectl get nodes
   kubectl top nodes
   kubectl get pods --all-namespaces
   ```

2. **Output**:
   ```
   ## Kubernetes Cluster Status

   ### Cluster Info
   - Context: production
   - Server: https://k8s.example.com
   - Version: v1.28.0

   ### Nodes
   | Name | Status | CPU | Memory | Pods |
   |------|--------|-----|--------|------|
   | node-1 | Ready | 45% | 60% | 25/110 |
   | node-2 | Ready | 30% | 55% | 20/110 |

   ### Pods by Namespace
   | Namespace | Running | Pending | Failed |
   |-----------|---------|---------|--------|
   | default | 10 | 0 | 0 |
   | kube-system | 15 | 0 | 0 |

   ### Problem Pods
   | Pod | Namespace | Status | Restarts |
   |-----|-----------|--------|----------|
   | api-xyz | default | CrashLoopBackOff | 5 |
   ```

## Example Usage
- `/k8s:status`
- `/k8s:status -n production`
