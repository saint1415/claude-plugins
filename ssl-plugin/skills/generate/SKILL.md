---
name: generate
description: Generate SSL private keys and Certificate Signing Requests (CSRs).
---

# SSL CSR Generator Skill

Create keys and CSRs.

## Steps

1. **Generate Key and CSR**:
   ```bash
   openssl req -new -newkey rsa:2048 -nodes -keyout {domain}.key -out {domain}.csr -subj "/CN={domain}/O={org}/C={country}"
   ```

2. **Output**:
   ```
   ## SSL Key & CSR Generated

   ### Files Created
   - Private Key: example.com.key
   - CSR: example.com.csr

   ### CSR Details
   - Common Name: example.com
   - Organization: Example Inc
   - Country: US
   - Key Size: 2048 bit

   ### CSR Content
   -----BEGIN CERTIFICATE REQUEST-----
   MIICvDCCAaQCAQAwdzELMAkGA1UEBhMCVVMx...
   -----END CERTIFICATE REQUEST-----

   ### Next Steps
   1. Submit CSR to Certificate Authority
   2. Keep private key secure
   3. Install certificate when received

   ### Commands Used
   ```bash
   openssl req -new -newkey rsa:2048 -nodes \
     -keyout example.com.key \
     -out example.com.csr \
     -subj "/CN=example.com/O=Example Inc/C=US"
   ```
   ```

## Example Usage
- `/ssl:generate example.com`
- `/ssl:generate example.com --org "My Company" --country US`
- `/ssl:generate --self-signed example.com`
