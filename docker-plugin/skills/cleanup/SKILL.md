---
name: cleanup
description: Clean up Docker resources - remove unused images, containers, volumes, and networks to free disk space.
---

# Docker Cleanup Skill

Free up disk space by removing unused Docker resources.

## Steps

1. **Analyze Usage**:
   ```bash
   docker system df
   ```

2. **Show What Can Be Removed**:
   ```bash
   # Dangling images
   docker images -f "dangling=true"

   # Stopped containers
   docker ps -a -f "status=exited"

   # Unused volumes
   docker volume ls -f "dangling=true"
   ```

3. **Output Format**:
   ```
   ## Docker Cleanup Analysis

   ### Current Usage
   | Type | Total | Reclaimable |
   |------|-------|-------------|
   | Images | 15.2GB | 8.5GB |
   | Containers | 2.1GB | 1.8GB |
   | Volumes | 5.0GB | 3.2GB |

   ### Cleanup Commands
   ```bash
   # Safe cleanup (unused only)
   docker system prune -f

   # Aggressive (includes unused images)
   docker system prune -a -f

   # Just volumes
   docker volume prune -f
   ```

   ### Space Saved: ~13.5GB
   ```

## Example Usage
- `/docker:cleanup`
- `/docker:cleanup --dry-run`
- `/docker:cleanup --all`
