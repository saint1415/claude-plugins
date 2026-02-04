---
name: expire
description: Check certificate expiration dates for multiple domains. Useful for monitoring and renewal planning.
---

# SSL Expiration Check Skill

Monitor certificate expiration.

## Steps

1. **Check Expiration**:
   ```bash
   echo | openssl s_client -servername {domain} -connect {domain}:443 2>/dev/null | openssl x509 -noout -dates
   ```

2. **Output**:
   ```
   ## Certificate Expiration Report

   ### Expiring Soon (< 30 days)
   | Domain | Expires | Days Left | Action |
   |--------|---------|-----------|--------|
   | api.example.com | 2024-01-20 | 5 | URGENT |
   | dev.example.com | 2024-02-01 | 17 | Renew soon |

   ### Healthy (> 30 days)
   | Domain | Expires | Days Left |
   |--------|---------|-----------|
   | example.com | 2024-04-01 | 75 |
   | www.example.com | 2024-04-01 | 75 |

   ### Renewal Commands (Let's Encrypt)
   ```bash
   certbot renew --cert-name api.example.com
   ```
   ```

## Example Usage
- `/ssl:expire example.com`
- `/ssl:expire example.com,api.example.com,www.example.com`
