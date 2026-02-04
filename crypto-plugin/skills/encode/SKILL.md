---
name: encode
description: Encode and decode text in various formats - Base64, URL encoding, HTML entities, Hex.
---

# Encoding/Decoding Skill

Convert text between different encodings.

## Steps

1. **Encode/Decode**:
   ```bash
   # Base64 encode
   echo -n "text" | base64

   # Base64 decode
   echo "dGV4dA==" | base64 -d

   # URL encode (using Python)
   python3 -c "import urllib.parse; print(urllib.parse.quote('text'))"

   # Hex encode
   echo -n "text" | xxd -p
   ```

2. **Output**:
   ```
   ## Encoding Results

   Input: "Hello World!"

   ### Base64
   - Encoded: SGVsbG8gV29ybGQh
   - Decoded: Hello World!

   ### URL Encoding
   - Encoded: Hello%20World%21

   ### Hex
   - Encoded: 48656c6c6f20576f726c6421

   ### HTML Entities
   - Encoded: Hello&#32;World&#33;
   ```

## Example Usage
- `/crypto:encode "Hello World" --format base64`
- `/crypto:encode SGVsbG8= --decode`
- `/crypto:encode "param=value&other=test" --format url`
