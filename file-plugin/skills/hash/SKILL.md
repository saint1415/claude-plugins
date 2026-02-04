---
name: hash
description: Calculate file hashes (MD5, SHA256) for integrity verification.
---

# File Hash Skill

Calculate and verify file checksums.

## Steps

1. **Calculate Hash**:
   ```bash
   # Windows (PowerShell)
   Get-FileHash -Path {file} -Algorithm SHA256
   certutil -hashfile {file} MD5
   certutil -hashfile {file} SHA256

   # Linux/Mac
   sha256sum {file}
   md5sum {file}
   ```

2. **Verify Against Expected**:
   Compare calculated hash against provided/expected value

3. **Output Format**:
   ```
   ## File Hash: {filename}

   | Algorithm | Hash |
   |-----------|------|
   | MD5 | d41d8cd98f00b204e9800998ecf8427e |
   | SHA256 | e3b0c44298fc1c149afbf4c8996fb924... |

   ### Verification
   - Status: MATCH / MISMATCH
   ```

## Example Usage
- `/file:hash document.pdf`
- `/file:hash installer.exe --verify abc123...`
