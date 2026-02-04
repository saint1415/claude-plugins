---
name: doc
description: Generate API documentation from OpenAPI/Swagger specs or by analyzing endpoints.
---

# API Documentation Skill

Generate or analyze API docs.

## Output
```
## API Documentation

### Endpoints

#### GET /users
Get all users

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| limit | int | No | Max results (default: 10) |
| offset | int | No | Pagination offset |

**Response:**
```json
{
  "users": [{"id": 1, "name": "John"}],
  "total": 100
}
```

#### POST /users
Create a new user

**Request Body:**
```json
{
  "name": "string (required)",
  "email": "string (required)",
  "role": "string (optional)"
}
```
```

## Example Usage
- `/api:doc openapi.yaml`
- `/api:doc https://api.example.com`
