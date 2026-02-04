---
name: dns
description: Perform DNS lookups for various record types including A, AAAA, MX, TXT, NS, CNAME, SOA.
---

# DNS Lookup Skill

Query DNS records for a domain.

## Steps

1. **Query All Record Types**:
   ```bash
   nslookup -type=A {domain}
   nslookup -type=MX {domain}
   nslookup -type=TXT {domain}
   nslookup -type=NS {domain}
   ```

2. **Output**:
   ```
   ## DNS Records: {domain}

   ### A Records (IPv4)
   - 93.184.216.34

   ### AAAA Records (IPv6)
   - 2606:2800:220:1:248:1893:25c8:1946

   ### MX Records (Mail)
   | Priority | Server |
   |----------|--------|
   | 10 | mail.example.com |

   ### TXT Records
   - v=spf1 include:_spf.google.com ~all
   - google-site-verification=xxx

   ### NS Records (Nameservers)
   - ns1.example.com
   - ns2.example.com
   ```

## Example Usage
- `/net:dns example.com`
- `/net:dns example.com --type MX`
