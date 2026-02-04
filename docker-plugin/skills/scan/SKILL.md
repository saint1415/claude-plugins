---
name: scan
description: Scan Docker images for security vulnerabilities using Trivy, Grype, or Docker Scout.
---

# Docker Image Security Scan Skill

Scan images for vulnerabilities.

## Steps

1. **Determine Scanner Available**:
   - Trivy: `trivy image {image}`
   - Grype: `grype {image}`
   - Docker Scout: `docker scout cves {image}`

2. **Run Scan**:
   ```bash
   trivy image --severity HIGH,CRITICAL {image}
   ```

3. **Output Format**:
   ```
   ## Security Scan: {image}

   ### Summary
   - Critical: 2
   - High: 5
   - Medium: 12
   - Low: 23

   ### Critical Vulnerabilities
   | CVE | Package | Version | Fixed In |
   |-----|---------|---------|----------|
   | CVE-2024-1234 | openssl | 1.1.1 | 1.1.1t |

   ### Recommendations
   1. Update base image to latest
   2. Rebuild with updated packages
   ```

## Example Usage
- `/docker:scan nginx:latest`
- `/docker:scan myapp:v1.0`
