---
name: curl
description: Convert API requests to curl commands or vice versa.
---

# Curl Converter Skill

Convert between formats and curl.

## Output
```
## Curl Command

### From Request
POST https://api.example.com/users
Content-Type: application/json
Authorization: Bearer token123
{"name": "John", "email": "john@example.com"}

### Generated Curl
```bash
curl -X POST 'https://api.example.com/users' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer token123' \
  -d '{"name": "John", "email": "john@example.com"}'
```

### Other Formats

**Python (requests):**
```python
import requests
response = requests.post(
    'https://api.example.com/users',
    headers={'Authorization': 'Bearer token123'},
    json={'name': 'John', 'email': 'john@example.com'}
)
```

**JavaScript (fetch):**
```javascript
fetch('https://api.example.com/users', {
  method: 'POST',
  headers: {'Content-Type': 'application/json', 'Authorization': 'Bearer token123'},
  body: JSON.stringify({name: 'John', email: 'john@example.com'})
})
```
```

## Example Usage
- `/api:curl POST https://api.example.com/data -d '{"key":"value"}'`
- `/api:curl --from-browser` (paste from browser dev tools)
