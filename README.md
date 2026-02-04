# Claude Code Custom Plugins

Personal productivity plugins for Claude Code.

**Total: 40 Plugins | 191 Skills**

## Plugins Index

### Security & OSINT
| Plugin | Skills | Description |
|--------|--------|-------------|
| [osint-plugin](./osint-plugin/) | domain, ip, email, headers | Security reconnaissance and OSINT tools |
| [ssl-plugin](./ssl-plugin/) | check, expire, chain, generate | SSL/TLS certificate tools |
| [email-plugin](./email-plugin/) | spf, dmarc, headers, blacklist | Email security analysis |
| [compliance-plugin](./compliance-plugin/) | pci, hipaa, gdpr, soc2 | Compliance audit checklists |
| [ra-qm-plugin](./ra-qm-plugin/) | 12 skills (ISO 13485, FDA, MDR, GDPR, etc.) | Regulatory affairs & quality management |

### IT & Productivity
| Plugin | Skills | Description |
|--------|--------|-------------|
| [servicenow-plugin](./servicenow-plugin/) | query, create, update, my-tickets | ServiceNow ticket management |
| [m365-admin-plugin](./m365-admin-plugin/) | user, audit, risky-users, licenses | Microsoft 365 administration |
| [git-plugin](./git-plugin/) | pr-review, changelog, stats, branch-cleanup | Git workflow automation |
| [pm-plugin](./pm-plugin/) | senior-pm, scrum-master, jira-expert, confluence-expert, atlassian-admin, atlassian-templates | Project management & Atlassian tools |
| [comms-plugin](./comms-plugin/) | internal-comms, slack-gif-creator | Communication tools |

### Cloud & DevOps
| Plugin | Skills | Description |
|--------|--------|-------------|
| [aws-iam-plugin](./aws-iam-plugin/) | iam-audit, who-can, unused-roles, policy-check | AWS IAM security analysis |
| [docker-plugin](./docker-plugin/) | cleanup, scan, compose, logs | Docker container management |
| [k8s-plugin](./k8s-plugin/) | status, logs, debug, scale | Kubernetes cluster management |
| [terraform-plugin](./terraform-plugin/) | plan, validate, cost, drift | Terraform infrastructure tools |

### Engineering & Development
| Plugin | Skills | Description |
|--------|--------|-------------|
| [engineering-plugin](./engineering-plugin/) | 18 skills (senior-backend, senior-frontend, senior-devops, senior-security, tdd-guide, etc.) | Comprehensive engineering expertise |
| [devtools-plugin](./devtools-plugin/) | mcp-builder, skill-creator, template-skill, webapp-testing | Developer tools and builders |
| [superpowers-plugin](./superpowers-plugin/) | 14 skills (TDD, debugging, planning, git-worktrees, subagent-driven-dev, etc.) | Advanced development workflows |
| [orchestration-plugin](./orchestration-plugin/) | plan-with-team, execute-plan + Builder/Validator agents | Multi-agent orchestration with Task system |

### Business & Strategy
| Plugin | Skills | Description |
|--------|--------|-------------|
| [c-level-plugin](./c-level-plugin/) | ceo-advisor, cto-advisor | C-level advisory skills |
| [product-plugin](./product-plugin/) | agile-product-owner, product-manager-toolkit, product-strategist, ui-design-system, ux-researcher-designer | Product team skills |
| [marketing-plugin](./marketing-plugin/) | content-creator, app-store-optimization, marketing-demand-acquisition, marketing-strategy-pmm, social-media-analyzer | Marketing skills |

### Networking & APIs
| Plugin | Skills | Description |
|--------|--------|-------------|
| [nettools-plugin](./nettools-plugin/) | ping, ports, dns, trace | Network diagnostics |
| [api-plugin](./api-plugin/) | test, mock, doc, curl | API testing and documentation |

### Data & Text Processing
| Plugin | Skills | Description |
|--------|--------|-------------|
| [json-plugin](./json-plugin/) | format, validate, diff, convert | JSON utilities |
| [regex-plugin](./regex-plugin/) | build, test, explain, library | Regex building and testing |
| [text-plugin](./text-plugin/) | case, count, lorem, slug | Text transformation tools |
| [logs-plugin](./logs-plugin/) | parse, search, stats, tail | Log file analysis |

### Documents & Files
| Plugin | Skills | Description |
|--------|--------|-------------|
| [document-plugin](./document-plugin/) | pdf, docx, pptx, xlsx | Office document processing |
| [file-plugin](./file-plugin/) | hash, diff, find-dups, size | File operations and analysis |
| [db-plugin](./db-plugin/) | query, schema, backup, migrate | Database utilities |

### Cryptography & Security
| Plugin | Skills | Description |
|--------|--------|-------------|
| [crypto-plugin](./crypto-plugin/) | hash, encode, password, jwt | Cryptographic utilities |

### Calculators & Converters
| Plugin | Skills | Description |
|--------|--------|-------------|
| [calc-plugin](./calc-plugin/) | unit, finance, subnet, date | Various calculators |
| [time-plugin](./time-plugin/) | convert, schedule, countdown, cron | Timezone and scheduling tools |
| [color-plugin](./color-plugin/) | convert, palette, contrast, gradient | Color format tools |

### Creative & Design
| Plugin | Skills | Description |
|--------|--------|-------------|
| [creative-plugin](./creative-plugin/) | algorithmic-art, artifacts-builder, brand-guidelines, canvas-design, theme-factory | Creative and design skills |

### Performance & Testing
| Plugin | Skills | Description |
|--------|--------|-------------|
| [perf-plugin](./perf-plugin/) | benchmark, profile, memory, lighthouse | Performance testing tools |

### Scaffolding & Generation
| Plugin | Skills | Description |
|--------|--------|-------------|
| [scaffold-plugin](./scaffold-plugin/) | react, python, node, go | Project scaffolding |
| [qr-plugin](./qr-plugin/) | generate, decode, wifi, vcard | QR code generation |

### External Services
| Plugin | Skills | Description |
|--------|--------|-------------|
| [weather-plugin](./weather-plugin/) | current, forecast, alerts, history | Weather information |
| [finance-plugin](./finance-plugin/) | stock, crypto, currency, compound | Financial data and calculators |

---

## Quick Start

### Load a Single Plugin
```bash
claude --plugin-dir ./osint-plugin
```

### Load Multiple Plugins
```bash
claude --plugin-dir ./osint-plugin --plugin-dir ./engineering-plugin --plugin-dir ./superpowers-plugin
```

### Load All Plugins (PowerShell)
```powershell
$plugins = Get-ChildItem -Directory | Where-Object { Test-Path "$_\.claude-plugin\plugin.json" } | ForEach-Object { "--plugin-dir ./$($_.Name)" }
claude $plugins
```

---

## Usage Examples

### Engineering Plugin
```
/engineering-skills:senior-backend      # Backend development guidance
/engineering-skills:senior-devops       # DevOps best practices
/engineering-skills:tdd-guide           # Test-driven development
/engineering-skills:tech-stack-evaluator # Evaluate technology choices
```

### Superpowers Plugin
```
/superpowers:systematic-debugging       # Structured debugging approach
/superpowers:test-driven-development    # TDD workflows
/superpowers:subagent-driven-development # Parallel agent development
/superpowers:writing-plans              # Implementation planning
```

### Document Plugin
```
/document:pdf extract report.pdf        # Extract text from PDF
/document:docx create "My Document"     # Create Word document
/document:xlsx parse data.xlsx          # Parse Excel file
/document:pptx generate slides.pptx     # Generate presentation
```

### PM Plugin (Atlassian)
```
/pm-skills:jira-expert                  # Jira best practices
/pm-skills:confluence-expert            # Confluence documentation
/pm-skills:scrum-master                 # Scrum facilitation
/pm-skills:atlassian-admin              # Atlassian administration
```

### C-Level Plugin
```
/c-level-skills:ceo-advisor             # Strategic decision-making
/c-level-skills:cto-advisor             # Technical leadership
```

### RA/QM Plugin (Regulatory)
```
/ra-qm-skills:fda-consultant-specialist # FDA submission guidance
/ra-qm-skills:mdr-745-specialist        # EU MDR compliance
/ra-qm-skills:quality-manager-qms-iso13485 # ISO 13485 QMS
/ra-qm-skills:gdpr-dsgvo-expert         # GDPR compliance
```

### Creative Plugin
```
/creative:algorithmic-art               # Generate algorithmic art
/creative:brand-guidelines              # Create brand guidelines
/creative:theme-factory                 # Design themes
```

### Orchestration Plugin (Multi-Agent)
```
/orchestration:plan-with-team Update API to use async/await
/orchestration:execute-plan specs/async-update.md
```

Builder/Validator pattern:
- Builder agent focuses on ONE task, self-validates
- Validator agent checks Builder's work
- Task system manages dependencies and communication

### Original Plugins (see detailed examples below)
```
/osint:headers https://example.com
/ssl:check google.com
/docker:cleanup
/crypto:hash "my secret"
```

---

## Configuration

### API Keys (Environment Variables)

| Plugin | Variable | Description |
|--------|----------|-------------|
| osint | `SHODAN_API_KEY` | Shodan API for port scanning |
| osint | `VIRUSTOTAL_API_KEY` | VirusTotal for reputation |
| servicenow | `SNOW_INSTANCE`, `SNOW_USER`, `SNOW_PASSWORD` | ServiceNow credentials |
| m365 | `M365_TENANT_ID`, `M365_CLIENT_ID`, `M365_CLIENT_SECRET` | Azure AD app registration |
| weather | `OPENWEATHER_API_KEY` | OpenWeatherMap API |
| finance | `ALPHA_VANTAGE_KEY` | Stock market data |

### Prerequisites by Plugin

| Plugin | Requirements |
|--------|-------------|
| aws-iam | AWS CLI configured with appropriate IAM permissions |
| docker | Docker Desktop or Docker Engine installed |
| k8s | kubectl configured with cluster access |
| terraform | Terraform CLI installed |
| ssl | OpenSSL installed (included with Git for Windows) |
| perf (lighthouse) | Node.js + `npm install -g lighthouse` |
| document | Python + pypdf, pdfplumber, python-docx, openpyxl |

---

## Detailed Usage Examples (Original Plugins)

### Security & OSINT

**osint-plugin**
```
/osint:domain example.com              # WHOIS, DNS, subdomain enumeration
/osint:ip 8.8.8.8                      # IP geolocation and reputation
/osint:email user@example.com          # Email validation, breach check
/osint:headers https://example.com     # Analyze security headers
```

**ssl-plugin**
```
/ssl:check google.com                  # Full certificate analysis
/ssl:expire google.com                 # Days until expiration
/ssl:chain google.com                  # Validate certificate chain
/ssl:generate mysite.com               # Generate CSR and private key
```

### Cloud & DevOps

**docker-plugin**
```
/docker:cleanup                        # Remove unused images/containers
/docker:scan myimage:latest            # Vulnerability scan
/docker:compose up -d                  # Manage compose services
/docker:logs mycontainer --tail 100    # View container logs
```

**k8s-plugin**
```
/k8s:status                            # Cluster health overview
/k8s:logs deployment/myapp -n prod     # Pod logs
/k8s:debug pod/myapp-xxx               # Debug failing pod
/k8s:scale deployment/myapp --replicas 5
```

### Data & Utilities

**json-plugin**
```
/json:format '{"a":1,"b":2}'           # Pretty print
/json:validate data.json               # Schema validation
/json:diff file1.json file2.json       # Compare JSON files
/json:convert data.json --to yaml      # Convert to YAML/CSV
```

**crypto-plugin**
```
/crypto:hash "my secret"               # MD5, SHA1, SHA256, SHA512
/crypto:encode "hello" --base64        # Base64, URL, hex encoding
/crypto:password --length 20           # Generate secure password
/crypto:jwt <token>                    # Decode and validate JWT
```

**calc-plugin**
```
/calc:unit 100 miles to km             # Unit conversion
/calc:finance --loan 300000 --rate 6.5 --years 30
/calc:subnet 192.168.1.0/24            # Network calculations
/calc:date "2025-12-31" - "2025-01-01" # Days between dates
```

---

## Version History

- **2.1.0** (2026-02-04): Added orchestration-plugin with Builder/Validator pattern, Windows hooks - now 40 plugins with 191 skills
- **2.0.0** (2026-02-02): Added 11 plugins from C:\Temp\Skills - now 39 plugins with 189 skills
- **1.1.0** (2026-02-02): Expanded to 28 plugins with 112 skills, Windows compatibility fixes
- **1.0.0** (2026-02-02): Initial release with 4 plugins and 16 skills

---

## Credits

- Original 28 plugins: crissantos
- Engineering, Marketing, Product, PM, RA/QM, C-Level, Creative plugins: [Alireza Rezvani](https://github.com/alirezarezvani/claude-skills) (MIT License)
- Superpowers plugin: [superpowers](https://github.com/superpowers) (MIT License)
