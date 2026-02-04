---
name: password
description: Generate secure random passwords with customizable length, character sets, and patterns.
---

# Password Generator Skill

Create secure random passwords.

## Steps

1. **Generate Password**:
   ```bash
   # Using /dev/urandom
   tr -dc 'A-Za-z0-9!@#$%^&*' < /dev/urandom | head -c 20

   # Using openssl
   openssl rand -base64 24
   ```

2. **Output**:
   ```
   ## Generated Passwords

   ### Strong (Default)
   `Kj9#mP2$xL5nQ8@vR3`

   ### Options Applied
   - Length: 20
   - Uppercase: Yes
   - Lowercase: Yes
   - Numbers: Yes
   - Symbols: Yes

   ### Multiple Passwords
   1. `Kj9#mP2$xL5nQ8@vR3tW`
   2. `Bm4&nH7*pY2kL9#jF6xZ`
   3. `Qw3@eR5$tY8uI1#oP4sD`

   ### Passphrase (XKCD style)
   `correct-horse-battery-staple`

   ### Strength Analysis
   - Entropy: 128 bits
   - Crack Time: centuries
   ```

## Example Usage
- `/crypto:password`
- `/crypto:password --length 32`
- `/crypto:password --no-symbols`
- `/crypto:password --passphrase --words 5`
