---
name: ports
description: Check open ports on a host. Useful for verifying service availability and firewall rules.
---

# Port Scanner Skill

Check which ports are open on a target.

## Steps

1. **Scan Common Ports** (or specified):
   ```bash
   # Windows (PowerShell)
   Test-NetConnection -ComputerName {host} -Port {port}
   1..1024 | ForEach-Object { Test-NetConnection -ComputerName {host} -Port $_ -WarningAction SilentlyContinue }

   # Linux/Mac (netcat)
   nc -zv {host} {port}
   nc -zv {host} 1-1024
   ```

2. **Output**:
   ```
   ## Port Scan: {host}

   ### Open Ports
   | Port | Service | Status |
   |------|---------|--------|
   | 22 | SSH | Open |
   | 80 | HTTP | Open |
   | 443 | HTTPS | Open |
   | 3306 | MySQL | Closed |

   ### Summary
   - Scanned: 10 ports
   - Open: 3
   - Closed: 7
   ```

## Example Usage
- `/net:ports example.com`
- `/net:ports 192.168.1.1 --ports 22,80,443,3389`
