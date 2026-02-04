---
name: cron
description: Explain cron expressions and show next run times.
---

# Cron Expression Skill

Parse and explain cron schedules, calculate next runs.

## Cron Format
```
* * * * *
| | | | |
| | | | +-- Day of Week (0-7, SUN-SAT)
| | | +---- Month (1-12)
| | +------ Day of Month (1-31)
| +-------- Hour (0-23)
+---------- Minute (0-59)
```

## Special Characters
| Char | Meaning | Example |
|------|---------|---------|
| `*` | Any value | `* * * * *` (every minute) |
| `,` | Multiple values | `1,15 * * * *` (1st and 15th min) |
| `-` | Range | `1-5 * * * *` (1st thru 5th min) |
| `/` | Step | `*/15 * * * *` (every 15 min) |

## Output Format
```
## Cron: 0 9 * * MON-FRI

### Human Readable
"At 9:00 AM, Monday through Friday"

### Schedule Details
| Field | Value | Meaning |
|-------|-------|---------|
| Minute | 0 | At minute 0 |
| Hour | 9 | At 9 AM |
| Day | * | Every day |
| Month | * | Every month |
| Weekday | MON-FRI | Monday to Friday |

### Next 5 Runs
1. Mon, Feb 3, 2026 at 9:00 AM
2. Tue, Feb 4, 2026 at 9:00 AM
3. Wed, Feb 5, 2026 at 9:00 AM
4. Thu, Feb 6, 2026 at 9:00 AM
5. Fri, Feb 7, 2026 at 9:00 AM
```

## Example Usage
- `/time:cron "0 9 * * MON-FRI"`
- `/time:cron --next 5 "*/15 * * * *"`
- `/time:cron --build "every weekday at 9am"`
