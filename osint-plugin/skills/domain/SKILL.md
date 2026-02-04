---
name: domain
description: Perform domain reconnaissance including WHOIS, DNS records, and subdomain enumeration. Use when investigating a domain's security posture or gathering intelligence.
---

# Domain Reconnaissance Skill

When the user provides a domain name, perform comprehensive reconnaissance:

## Steps to Execute

1. **WHOIS Lookup**: Use the WebFetch tool to query `https://who.is/whois/{domain}` or use Bash with `whois {domain}` if available

2. **DNS Records**: Query DNS records using:
   - `nslookup {domain}` or `dig {domain} ANY` via Bash
   - Look for A, AAAA, MX, TXT, NS, CNAME records

3. **Security Headers Check**: Use WebFetch to analyze the domain's HTTP security headers

4. **SSL/TLS Info**: Check certificate details if HTTPS is available

## Output Format

Present findings in a structured format:

```
## Domain: {domain}

### Registration Info
- Registrar: ...
- Created: ...
- Expires: ...
- Name Servers: ...

### DNS Records
- A: ...
- MX: ...
- TXT: ...

### Security Assessment
- HTTPS: Yes/No
- Security Headers: Present/Missing
- SPF: Valid/Invalid/Missing
- DMARC: Valid/Invalid/Missing
```

## Example Usage
User: `/osint:domain example.com`

## API Keys
- If SHODAN_API_KEY environment variable is set, use Shodan API for additional data
- If VIRUSTOTAL_API_KEY is set, check domain reputation
