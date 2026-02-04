---
name: hash
description: Generate cryptographic hashes (MD5, SHA1, SHA256, SHA512) for text or files.
---

# Hash Generator Skill

Create cryptographic hashes.

## Steps

1. **Generate Hashes**:
   ```bash
   # Windows (PowerShell)
   [System.BitConverter]::ToString((New-Object Security.Cryptography.MD5CryptoServiceProvider).ComputeHash([Text.Encoding]::UTF8.GetBytes("text")))
   Get-FileHash -Path filename -Algorithm SHA256
   certutil -hashfile filename SHA256

   # Linux/Mac
   echo -n "text" | md5sum
   echo -n "text" | sha1sum
   echo -n "text" | sha256sum
   sha256sum filename
   ```

2. **Output**:
   ```
   ## Hash Results

   Input: "Hello World"

   | Algorithm | Hash |
   |-----------|------|
   | MD5 | b10a8db164e0754105b7a99be72e3fe5 |
   | SHA1 | 0a4d55a8d778e5022fab701977c5d840bbc486d0 |
   | SHA256 | a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e |
   | SHA512 | 2c74fd17edafd80e8447b0d46741ee243b7eb74dd2149a0ab1b9246fb30382f27e853d8585719e0e67cbda0daa8f51671064615d645ae27acb15bfb1447f459b |
   ```

## Example Usage
- `/crypto:hash "my password"`
- `/crypto:hash file.txt`
- `/crypto:hash "text" --algorithm sha256`
