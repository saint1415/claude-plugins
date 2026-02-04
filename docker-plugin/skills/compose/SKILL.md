---
name: compose
description: Manage Docker Compose stacks - view status, start/stop services, and troubleshoot issues.
---

# Docker Compose Management Skill

Manage multi-container applications.

## Steps

1. **Find Compose Files**:
   ```bash
   find . -name "docker-compose*.yml" -o -name "compose*.yml"
   ```

2. **Show Status**:
   ```bash
   docker compose ps
   docker compose top
   ```

3. **Output Format**:
   ```
   ## Docker Compose: {project}

   ### Services
   | Service | Status | Ports | Health |
   |---------|--------|-------|--------|
   | web | Up | 80:80 | healthy |
   | db | Up | - | healthy |
   | redis | Up | 6379 | - |

   ### Resource Usage
   | Service | CPU | Memory |
   |---------|-----|--------|
   | web | 5% | 256MB |

   ### Quick Commands
   ```bash
   docker compose up -d
   docker compose down
   docker compose restart web
   docker compose logs -f web
   ```
   ```

## Example Usage
- `/docker:compose`
- `/docker:compose up`
- `/docker:compose restart web`
