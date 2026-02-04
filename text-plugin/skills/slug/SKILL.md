---
name: slug
description: Generate URL-friendly slugs from text.
---

# Slug Generator Skill

Convert text to URL-friendly slugs.

## Rules Applied
1. Convert to lowercase
2. Replace spaces with hyphens
3. Remove special characters
4. Remove accents/diacritics (if transliterate)
5. Collapse multiple hyphens
6. Trim leading/trailing hyphens

## Output Format
```
## Slug Generator

Input: "My Blog Post Title!"
Slug: `my-blog-post-title`

### Options Applied
- Lowercase: Yes
- Special chars removed: !
- Transliterate: No
```

## Common Transformations
| Input | Output |
|-------|--------|
| "Hello World!" | `hello-world` |
| "Product #1 - Best!" | `product-1-best` |
| "Cafe au lait" | `cafe-au-lait` |
| "Cafe au lait" (transliterate) | `cafe-au-lait` |

## Example Usage
- `/text:slug "My Blog Post Title!"`
- `/text:slug "Produit en Francais" --transliterate`
- `/text:slug "API v2.0 Release Notes" --max-length 30`
