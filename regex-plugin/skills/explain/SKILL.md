---
name: explain
description: Explain what a regex pattern does in plain English.
---

# Regex Explainer Skill

Break down regex patterns into understandable components.

## Analysis Steps
1. Identify anchors (^, $, \b)
2. Parse character classes ([...])
3. Identify quantifiers (+, *, ?, {n,m})
4. Find groups and alternations
5. Explain special characters

## Output Format
```
## Regex Explanation

Pattern: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`

### Summary
This regex validates an email address format.

### Breakdown
| Component | Pattern | Meaning |
|-----------|---------|---------|
| Start | `^` | Must start at beginning |
| Local part | `[a-zA-Z0-9._%+-]+` | One or more alphanumeric, dots, underscores, percent, plus, hyphen |
| At symbol | `@` | Literal @ character |
| Domain | `[a-zA-Z0-9.-]+` | One or more alphanumeric, dots, hyphens |
| Dot | `\.` | Literal period |
| TLD | `[a-zA-Z]{2,}` | Two or more letters |
| End | `$` | Must end at string end |

### Test Cases
| Input | Match |
|-------|-------|
| user@example.com | Yes |
| test.email+tag@sub.domain.org | Yes |
| invalid@.com | No |
| @missing.com | No |
```

## Example Usage
- `/regex:explain "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"`
- `/regex:explain "\\d{3}-\\d{2}-\\d{4}"` (SSN pattern)
- `/regex:explain "(?=.*[A-Z])(?=.*\\d).{8,}"` (password)
