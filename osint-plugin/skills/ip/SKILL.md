---
name: ip
description: Perform IP address reconnaissance including geolocation, reputation checks, and open port information. Use for investigating suspicious IPs or network intelligence.
---

# IP Address Reconnaissance Skill

When the user provides an IP address, gather comprehensive intelligence:

## Steps to Execute

1. **Geolocation**: Use WebFetch to query `https://ipapi.co/{ip}/json/` for location data

2. **Reverse DNS**: Use Bash with `nslookup {ip}` to find associated hostnames

3. **Reputation Check**: If APIs are available:
   - AbuseIPDB: Check for reported abuse
   - Shodan: Check for open ports and services

4. **WHOIS**: Query IP registration info

## Output Format

```
## IP Address: {ip}

### Geolocation
- Country: ...
- City: ...
- ISP: ...
- Organization: ...

### Reverse DNS
- Hostname: ...

### Reputation
- Abuse Reports: X reports
- Risk Score: Low/Medium/High
- Last Reported: ...

### Open Ports (if Shodan available)
- 22/tcp - SSH
- 80/tcp - HTTP
- 443/tcp - HTTPS
```

## Example Usage
User: `/osint:ip 8.8.8.8`

## API Keys
- SHODAN_API_KEY: For port/service enumeration
- ABUSEIPDB_API_KEY: For reputation data
