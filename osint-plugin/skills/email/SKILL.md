---
name: email
description: Validate email addresses and check for data breaches. Use for verifying email legitimacy or checking if credentials may be compromised.
---

# Email Intelligence Skill

When the user provides an email address, perform validation and breach checks:

## Steps to Execute

1. **Format Validation**: Verify the email format is valid

2. **Domain Check**: Verify the email domain exists and has MX records
   - Use `nslookup -type=mx {domain}` via Bash

3. **Breach Check**: If HIBP_API_KEY is available, check HaveIBeenPwned
   - Otherwise, inform user to check manually at https://haveibeenpwned.com

4. **Domain Reputation**: Check if the domain is known for spam/phishing

## Output Format

```
## Email Analysis: {email}

### Validation
- Format: Valid/Invalid
- Domain Exists: Yes/No
- MX Records: Found/Not Found

### Domain Info
- Domain: {domain}
- Mail Server: {mx_record}
- SPF Record: Present/Missing
- DMARC Record: Present/Missing

### Breach Status
- Breaches Found: X breaches
- Most Recent: {date}
- Exposed Data Types: passwords, emails, etc.

### Recommendations
- ...
```

## Example Usage
User: `/osint:email test@example.com`

## Privacy Note
This skill does not store or transmit email addresses beyond the necessary API calls.
