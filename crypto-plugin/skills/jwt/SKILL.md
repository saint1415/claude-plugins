---
name: jwt
description: Decode and analyze JSON Web Tokens (JWT). Shows header, payload, and validates signatures.
---

# JWT Decoder Skill

Analyze JSON Web Tokens.

## Steps

1. **Split and Decode JWT**:
   ```bash
   # JWT has 3 parts: header.payload.signature
   echo {header} | base64 -d
   echo {payload} | base64 -d
   ```

2. **Output**:
   ```
   ## JWT Analysis

   ### Token Info
   - Algorithm: RS256
   - Type: JWT
   - Valid Signature: Unknown (no key provided)

   ### Header
   ```json
   {
     "alg": "RS256",
     "typ": "JWT"
   }
   ```

   ### Payload
   ```json
   {
     "sub": "1234567890",
     "name": "John Doe",
     "iat": 1516239022,
     "exp": 1516242622
   }
   ```

   ### Claims Analysis
   | Claim | Value | Status |
   |-------|-------|--------|
   | sub | 1234567890 | User ID |
   | exp | 2024-01-15 10:30 | EXPIRED |
   | iat | 2024-01-15 09:30 | Issued |

   ### Security Notes
   - Token is expired
   - Consider using shorter expiration times
   ```

## Example Usage
- `/crypto:jwt eyJhbGciOiJIUzI1...`
- `/crypto:jwt {token} --verify {secret}`
