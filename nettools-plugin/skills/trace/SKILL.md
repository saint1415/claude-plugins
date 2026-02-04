---
name: trace
description: Trace the network route to a destination, showing each hop along the way.
---

# Traceroute Skill

Trace network path to destination.

## Steps

1. **Execute Traceroute**:
   ```bash
   traceroute {host}
   # Or on Windows: tracert {host}
   ```

2. **Output**:
   ```
   ## Traceroute: {host}

   | Hop | IP | Hostname | Latency |
   |-----|----|-----------| --------|
   | 1 | 192.168.1.1 | router.local | 1ms |
   | 2 | 10.0.0.1 | isp-gateway | 10ms |
   | 3 | * | * | timeout |
   | 4 | 72.14.215.85 | google.com | 25ms |

   ### Summary
   - Total Hops: 4
   - Timeouts: 1
   - Final Latency: 25ms
   ```

## Example Usage
- `/net:trace google.com`
- `/net:trace 8.8.8.8 --max-hops 20`
