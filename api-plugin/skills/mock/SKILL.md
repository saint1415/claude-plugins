---
name: mock
description: Generate mock/fake data for API testing - users, products, addresses, etc.
---

# Mock Data Generator Skill

Generate fake data for testing.

## Output
```
## Generated Mock Data

### Users (5)
```json
[
  {"id": 1, "name": "John Smith", "email": "john.smith@example.com", "phone": "555-0101"},
  {"id": 2, "name": "Jane Doe", "email": "jane.doe@example.com", "phone": "555-0102"}
]
```

### Products (3)
```json
[
  {"id": 1, "name": "Widget Pro", "price": 29.99, "sku": "WGT-001"},
  {"id": 2, "name": "Gadget Plus", "price": 49.99, "sku": "GDG-002"}
]
```

### Addresses (2)
```json
[
  {"street": "123 Main St", "city": "New York", "state": "NY", "zip": "10001"}
]
```
```

## Example Usage
- `/api:mock users 10`
- `/api:mock products --fields name,price,description`
