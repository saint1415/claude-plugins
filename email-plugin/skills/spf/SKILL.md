---
name: spf
description: Check and validate SPF records for a domain.
---

# SPF Validator Skill

Validate Sender Policy Framework records for email authentication.

## Steps

1. **Lookup SPF Record**:
   ```bash
   # Windows/Linux
   nslookup -type=TXT {domain} | Select-String "v=spf1"

   # Or using dig (Linux/Mac)
   dig TXT {domain} +short | grep spf
   ```

2. **Parse SPF Mechanisms**:
   - `ip4:` - Allowed IPv4 addresses/ranges
   - `ip6:` - Allowed IPv6 addresses/ranges
   - `include:` - Include other SPF records
   - `a:` - A record of domain
   - `mx:` - MX records of domain
   - `all` - Default action (-all, ~all, ?all, +all)

3. **Validate and Report**:
   ```
   ## SPF Analysis: {domain}

   ### SPF Record
   `v=spf1 include:_spf.google.com include:sendgrid.net ip4:192.168.1.0/24 -all`

   ### Mechanisms
   | Type | Value | Status |
   |------|-------|--------|
   | include | _spf.google.com | Valid |
   | include | sendgrid.net | Valid |
   | ip4 | 192.168.1.0/24 | Valid |

   ### Evaluation
   - DNS Lookups: 4/10 (under limit)
   - Policy: Hard Fail (-all)
   - Verdict: PASS
   ```

## Example Usage
- `/email:spf example.com`
- `/email:spf example.com --check-ip 1.2.3.4`
