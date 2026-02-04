---
name: headers
description: Analyze HTTP security headers of a website. Use to assess a website's security configuration and identify missing protections.
---

# Security Headers Analysis Skill

When the user provides a URL, analyze its HTTP security headers:

## Steps to Execute

1. **Fetch Headers**: Use Bash with `curl -I -s {url}` to get HTTP headers

2. **Analyze Security Headers**: Check for presence and configuration of:
   - `Strict-Transport-Security` (HSTS)
   - `Content-Security-Policy` (CSP)
   - `X-Frame-Options`
   - `X-Content-Type-Options`
   - `X-XSS-Protection`
   - `Referrer-Policy`
   - `Permissions-Policy`
   - `Cross-Origin-Opener-Policy`
   - `Cross-Origin-Resource-Policy`

3. **Grade the Site**: Assign a security grade based on headers present

## Output Format

```
## Security Headers Analysis: {url}

### Summary
- Grade: A/B/C/D/F
- Headers Present: X/9
- Critical Missing: X

### Header Details

| Header | Status | Value |
|--------|--------|-------|
| Strict-Transport-Security | Present/Missing | max-age=... |
| Content-Security-Policy | Present/Missing | ... |
| X-Frame-Options | Present/Missing | DENY/SAMEORIGIN |
| X-Content-Type-Options | Present/Missing | nosniff |
| X-XSS-Protection | Present/Missing | 1; mode=block |
| Referrer-Policy | Present/Missing | ... |
| Permissions-Policy | Present/Missing | ... |

### Recommendations
1. Add missing header X with value Y
2. ...

### Additional Info
- Server: {server_header}
- TLS Version: ...
```

## Grading Criteria
- A: All critical headers present and properly configured
- B: Most headers present, minor issues
- C: Some important headers missing
- D: Multiple critical headers missing
- F: Minimal or no security headers

## Example Usage
User: `/osint:headers https://example.com`
