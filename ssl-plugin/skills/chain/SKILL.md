---
name: chain
description: Validate the SSL certificate chain including intermediate and root certificates.
---

# SSL Chain Validation Skill

Verify certificate chain.

## Steps

1. **Get Chain**:
   ```bash
   echo | openssl s_client -showcerts -servername {domain} -connect {domain}:443
   ```

2. **Output**:
   ```
   ## Certificate Chain: {domain}

   ### Chain Structure
   1. **Leaf Certificate** (example.com)
      - Issuer: R3 (Let's Encrypt)
      - Valid: 2024-01-01 to 2024-04-01

   2. **Intermediate** (R3)
      - Issuer: ISRG Root X1
      - Valid: 2020-09-04 to 2025-09-15

   3. **Root** (ISRG Root X1)
      - Self-signed
      - Valid: 2015-06-04 to 2035-06-04

   ### Chain Validation
   - Complete: Yes
   - Trusted: Yes
   - Order: Correct

   ### Issues
   - None found
   ```

## Example Usage
- `/ssl:chain example.com`
