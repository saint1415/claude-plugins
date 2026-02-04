---
name: ping
description: Ping hosts to check connectivity and measure latency. Supports multiple targets and continuous monitoring.
---

# Network Ping Skill

Test network connectivity and latency.

## Steps

1. **Execute Ping**:
   ```bash
   # Windows
   ping -n 5 {host}

   # Linux/Mac
   ping -c 5 {host}
   ```

2. **Parse Results**: Extract latency stats

3. **Output**:
   ```
   ## Ping Results: {host}

   | Metric | Value |
   |--------|-------|
   | Packets Sent | 5 |
   | Packets Received | 5 |
   | Packet Loss | 0% |
   | Min Latency | 10ms |
   | Avg Latency | 15ms |
   | Max Latency | 25ms |

   ### Status: REACHABLE
   ```

## Example Usage
- `/net:ping google.com`
- `/net:ping 8.8.8.8 --count 10`
