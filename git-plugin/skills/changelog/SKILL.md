---
name: changelog
description: Generate a changelog from git commits. Supports conventional commits and semantic versioning.
---

# Changelog Generator Skill

Generate changelogs from git history.

## Steps

1. **Get Commits**: Fetch commits since last tag
   ```bash
   git log $(git describe --tags --abbrev=0)..HEAD --oneline
   ```

2. **Parse Commits**: Group by type (feat, fix, docs, etc.)

3. **Generate Changelog**: Format as markdown

## Output Format
```markdown
## [1.2.0] - 2024-01-15

### Added
- New user authentication system (#123)
- Dark mode support (#125)

### Fixed
- Login timeout issue (#120)
- Memory leak in dashboard (#121)

### Changed
- Updated dependencies
- Improved error messages
```

## Example Usage
- `/git:changelog` (since last tag)
- `/git:changelog v1.0.0..v1.1.0`
