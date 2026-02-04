---
name: format
description: Format and prettify JSON with proper indentation. Can also minify JSON.
---

# JSON Formatter Skill

Prettify or minify JSON.

## Steps

1. **Format JSON**:
   ```bash
   echo '{json}' | python3 -m json.tool
   # Or with jq
   echo '{json}' | jq '.'
   ```

2. **Output**:
   ```
   ## Formatted JSON

   Input (minified):
   {"name":"John","age":30,"city":"NYC"}

   Output (prettified):
   ```json
   {
     "name": "John",
     "age": 30,
     "city": "NYC"
   }
   ```

   ### Stats
   - Keys: 3
   - Depth: 1
   - Size: 42 bytes (minified)
   ```

## Example Usage
- `/json:format '{"name":"John"}'`
- `/json:format file.json`
- `/json:format --minify`
