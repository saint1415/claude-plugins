---
name: check
description: Check SSL/TLS certificate details for a domain including issuer, validity, and security configuration.
---

# SSL Certificate Check Skill

Analyze SSL certificates.

## Steps

1. **Get Certificate**:
   ```bash
   echo | openssl s_client -servername {domain} -connect {domain}:443 2>/dev/null | openssl x509 -noout -text
   ```

2. **Output**:
   ```
   ## SSL Certificate: {domain}

   ### Certificate Info
   | Field | Value |
   |-------|-------|
   | Subject | CN=example.com |
   | Issuer | Let's Encrypt |
   | Valid From | 2024-01-01 |
   | Valid Until | 2024-04-01 |
   | Days Remaining | 75 |

   ### Security
   - Protocol: TLS 1.3
   - Cipher: TLS_AES_256_GCM_SHA384
   - Key Size: 2048 bit RSA

   ### SANs (Subject Alternative Names)
   - example.com
   - www.example.com
   - api.example.com

   ### Grade: A
   ```

## Example Usage
- `/ssl:check example.com`
- `/ssl:check example.com:8443`
