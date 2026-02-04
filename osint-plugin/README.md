# OSINT Plugin for Claude Code

Security reconnaissance and Open Source Intelligence tools.

## Commands

| Command | Description |
|---------|-------------|
| `/osint:domain <domain>` | Domain reconnaissance (WHOIS, DNS, security analysis) |
| `/osint:ip <ip>` | IP address lookup (geolocation, reputation, reverse DNS) |
| `/osint:email <email>` | Email validation and breach checking |
| `/osint:headers <url>` | HTTP security headers analysis |

## Installation

```bash
claude --plugin-dir /path/to/osint-plugin
```

## Configuration (Optional)

Set environment variables for enhanced features:

```bash
export SHODAN_API_KEY="your-key"      # Port/service data
export VIRUSTOTAL_API_KEY="your-key"  # Reputation data
export ABUSEIPDB_API_KEY="your-key"   # IP abuse reports
```

## Examples

```
# Domain reconnaissance
/osint:domain example.com

# IP lookup
/osint:ip 8.8.8.8

# Email breach check
/osint:email test@example.com

# Security headers analysis
/osint:headers https://example.com
```

## What Each Skill Does

### /osint:domain
- WHOIS registration info
- DNS records (A, MX, TXT, NS)
- SPF/DMARC validation
- SSL certificate info

### /osint:ip
- Geolocation (country, city, ISP)
- Reverse DNS lookup
- Reputation scoring
- Open ports (with Shodan API)

### /osint:email
- Format validation
- MX record verification
- Breach database check
- Domain reputation

### /osint:headers
- Security header analysis
- Grade assignment (A-F)
- Missing header identification
- Remediation recommendations
