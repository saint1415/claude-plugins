---
name: convert
description: Convert JSON to/from other formats like YAML, XML, CSV, and TOML.
---

# JSON Converter Skill

Convert between data formats.

## Steps

1. **Convert**:
   ```bash
   # JSON to YAML (using yq or Python)
   python3 -c "import json,yaml,sys; yaml.dump(json.load(sys.stdin), sys.stdout)"

   # JSON to CSV (using jq)
   jq -r '.[] | [.name, .age] | @csv'
   ```

2. **Output**:
   ```
   ## Format Conversion

   Input Format: JSON
   Output Format: YAML

   ### Input (JSON)
   ```json
   {"name": "John", "age": 30}
   ```

   ### Output (YAML)
   ```yaml
   name: John
   age: 30
   ```

   ### Supported Formats
   - JSON ↔ YAML
   - JSON ↔ XML
   - JSON ↔ CSV (for arrays)
   - JSON ↔ TOML
   ```

## Example Usage
- `/json:convert data.json --to yaml`
- `/json:convert config.yaml --to json`
- `/json:convert users.json --to csv`
