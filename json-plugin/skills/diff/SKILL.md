---
name: diff
description: Compare two JSON objects and show differences.
---

# JSON Diff Skill

Compare JSON structures.

## Steps

1. **Compare JSON**:
   ```bash
   # Using jq
   diff <(jq -S . file1.json) <(jq -S . file2.json)
   ```

2. **Output**:
   ```
   ## JSON Comparison

   ### Summary
   - Added: 2 fields
   - Removed: 1 field
   - Changed: 3 fields

   ### Differences

   | Path | Old Value | New Value |
   |------|-----------|-----------|
   | $.name | "John" | "Jane" |
   | $.age | 30 | 31 |
   | $.city | "NYC" | (removed) |
   | $.country | (none) | "USA" |

   ### Visual Diff
   ```diff
   - "name": "John"
   + "name": "Jane"
   - "age": 30
   + "age": 31
   ```
   ```

## Example Usage
- `/json:diff file1.json file2.json`
- `/json:diff '{"a":1}' '{"a":2}'`
