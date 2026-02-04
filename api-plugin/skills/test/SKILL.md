---
name: test
description: Test API endpoints with various HTTP methods and display formatted responses.
---

# API Test Skill

Test HTTP endpoints.

## Steps
1. **Make Request**:
   ```bash
   curl -s -w "\n%{http_code}" -X {method} "{url}" -H "Content-Type: application/json" -d '{body}'
   ```

2. **Output**:
   ```
   ## API Test: {method} {url}

   ### Request
   - Method: GET
   - URL: https://api.example.com/users/1
   - Headers: Content-Type: application/json

   ### Response
   - Status: 200 OK
   - Time: 125ms
   - Size: 256 bytes

   ### Body
   ```json
   {
     "id": 1,
     "name": "John Doe",
     "email": "john@example.com"
   }
   ```

   ### Headers
   - Content-Type: application/json
   - X-Request-Id: abc123
   ```

## Example Usage
- `/api:test GET https://api.example.com/users`
- `/api:test POST https://api.example.com/users -d '{"name":"John"}'`
