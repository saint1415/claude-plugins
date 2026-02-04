---
name: lighthouse
description: Run Lighthouse web performance audit on URLs.
---

# Lighthouse Audit Skill

Web performance analysis using Google Lighthouse.

## Prerequisites
- Node.js installed
- Lighthouse CLI: `npm install -g lighthouse`

## Steps

1. **Run Lighthouse Audit**:
   ```bash
   lighthouse {url} --output json --output-path report.json --chrome-flags="--headless"

   # Mobile (default)
   lighthouse {url} --preset perf

   # Desktop
   lighthouse {url} --preset desktop
   ```

2. **Parse Results**: Extract key metrics from JSON report

3. **Output Format**:
   ```
   ## Lighthouse Report: {url}

   ### Performance Scores
   | Category | Score |
   |----------|-------|
   | Performance | 92 |
   | Accessibility | 88 |
   | Best Practices | 100 |
   | SEO | 95 |

   ### Core Web Vitals
   | Metric | Value | Rating |
   |--------|-------|--------|
   | LCP (Largest Contentful Paint) | 1.2s | Good |
   | FID (First Input Delay) | 12ms | Good |
   | CLS (Cumulative Layout Shift) | 0.05 | Good |

   ### Opportunities
   - Serve images in next-gen formats (save 500KB)
   - Eliminate render-blocking resources
   ```

## Example Usage
- `/perf:lighthouse https://example.com`
- `/perf:lighthouse https://example.com --desktop`
