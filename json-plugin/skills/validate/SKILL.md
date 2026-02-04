---
name: validate
description: Validate JSON syntax and optionally validate against a JSON Schema.
---

# JSON Validator Skill

Check JSON validity and schema compliance.

## Steps

1. **Validate Syntax**:
   ```bash
   echo '{json}' | python3 -m json.tool > /dev/null 2>&1 && echo "Valid" || echo "Invalid"
   ```

2. **Output**:
   ```
   ## JSON Validation

   ### Syntax Check
   Status: VALID / INVALID

   ### Errors Found (if any)
   - Line 5: Unexpected token '}'
   - Line 8: Missing comma after value

   ### Schema Validation (if schema provided)
   Status: COMPLIANT / NON-COMPLIANT

   | Path | Error |
   |------|-------|
   | $.email | Required field missing |
   | $.age | Expected number, got string |
   ```

## Example Usage
- `/json:validate '{"name": "test"}'`
- `/json:validate data.json --schema schema.json`
