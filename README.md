# Claude Code Custom Plugins

[![Plugins](https://img.shields.io/badge/Plugins-40-blue)]()
[![Skills](https://img.shields.io/badge/Skills-191-green)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%2011-lightgrey)]()
[![Claude Code](https://img.shields.io/badge/Claude%20Code-1.0.33%2B-purple)]()

A comprehensive collection of custom plugins for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), Anthropic's official CLI for Claude. These plugins extend Claude Code with specialized skills for security, DevOps, engineering, business strategy, and more.

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Plugin Categories](#plugin-categories)
  - [Security & OSINT](#security--osint)
  - [IT & Productivity](#it--productivity)
  - [Cloud & DevOps](#cloud--devops)
  - [Engineering & Development](#engineering--development)
  - [Business & Strategy](#business--strategy)
  - [Networking & APIs](#networking--apis)
  - [Data & Text Processing](#data--text-processing)
  - [Documents & Files](#documents--files)
  - [Calculators & Converters](#calculators--converters)
  - [Creative & Design](#creative--design)
  - [Performance & Testing](#performance--testing)
  - [Scaffolding & Generation](#scaffolding--generation)
  - [External Services](#external-services)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [Orchestration](#orchestration)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Features

- **40 Specialized Plugins** covering security, DevOps, engineering, business, and productivity
- **191 Skills** (slash commands) for quick access to expert knowledge and automation
- **Multi-Agent Orchestration** with Builder/Validator pattern for complex tasks
- **Windows 11 Compatible** with PowerShell hooks and scripts
- **Modular Architecture** - load only the plugins you need
- **Self-Validating Agents** with embedded code quality hooks

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
$plugins = Get-ChildItem -Directory |
    Where-Object { Test-Path "$_\.claude-plugin\plugin.json" } |
    ForEach-Object { "--plugin-dir", "./$($_.Name)" }
claude @plugins
```

## Plugin Categories

### Security & OSINT

| Plugin | Skills | Description |
|--------|--------|-------------|
| [osint-plugin](./osint-plugin/) | `domain`, `ip`, `email`, `headers` | Security reconnaissance and OSINT tools |
| [ssl-plugin](./ssl-plugin/) | `check`, `expire`, `chain`, `generate` | SSL/TLS certificate analysis and generation |
| [email-plugin](./email-plugin/) | `spf`, `dmarc`, `headers`, `blacklist` | Email security and deliverability analysis |
| [compliance-plugin](./compliance-plugin/) | `pci`, `hipaa`, `gdpr`, `soc2` | Compliance audit checklists and guidance |
| [ra-qm-plugin](./ra-qm-plugin/) | 12 skills | Regulatory affairs & quality management (ISO 13485, FDA, MDR, GDPR) |

**Example Usage:**
```
/osint:domain example.com          # WHOIS, DNS, subdomain enumeration
/osint:headers https://example.com # Analyze security headers
/ssl:check google.com              # Full certificate analysis
/ssl:expire google.com             # Days until expiration
```

### IT & Productivity

| Plugin | Skills | Description |
|--------|--------|-------------|
| [servicenow-plugin](./servicenow-plugin/) | `query`, `create`, `update`, `my-tickets` | ServiceNow ticket management |
| [m365-admin-plugin](./m365-admin-plugin/) | `user`, `audit`, `risky-users`, `licenses` | Microsoft 365 administration |
| [git-plugin](./git-plugin/) | `pr-review`, `changelog`, `stats`, `branch-cleanup` | Git workflow automation |
| [pm-plugin](./pm-plugin/) | 6 skills | Project management & Atlassian tools |
| [comms-plugin](./comms-plugin/) | `internal-comms`, `slack-gif-creator` | Communication tools |

**Example Usage:**
```
/pm-skills:jira-expert             # Jira best practices
/pm-skills:confluence-expert       # Confluence documentation
/pm-skills:scrum-master            # Scrum facilitation
```

### Cloud & DevOps

| Plugin | Skills | Description |
|--------|--------|-------------|
| [aws-iam-plugin](./aws-iam-plugin/) | `iam-audit`, `who-can`, `unused-roles`, `policy-check` | AWS IAM security analysis |
| [docker-plugin](./docker-plugin/) | `cleanup`, `scan`, `compose`, `logs` | Docker container management |
| [k8s-plugin](./k8s-plugin/) | `status`, `logs`, `debug`, `scale` | Kubernetes cluster management |
| [terraform-plugin](./terraform-plugin/) | `plan`, `validate`, `cost`, `drift` | Terraform infrastructure tools |

**Example Usage:**
```
/docker:cleanup                    # Remove unused images/containers
/docker:scan myimage:latest        # Vulnerability scan
/k8s:status                        # Cluster health overview
/k8s:logs deployment/myapp -n prod # Pod logs
```

### Engineering & Development

| Plugin | Skills | Description |
|--------|--------|-------------|
| [engineering-plugin](./engineering-plugin/) | 18 skills | Comprehensive engineering expertise (backend, frontend, DevOps, security) |
| [devtools-plugin](./devtools-plugin/) | `mcp-builder`, `skill-creator`, `template-skill`, `webapp-testing` | Developer tools and builders |
| [superpowers-plugin](./superpowers-plugin/) | 14 skills | Advanced development workflows (TDD, debugging, planning) |
| [orchestration-plugin](./orchestration-plugin/) | `plan-with-team`, `execute-plan` | Multi-agent orchestration with Builder/Validator pattern |

**Example Usage:**
```
/engineering-skills:senior-backend      # Backend development guidance
/engineering-skills:senior-devops       # DevOps best practices
/engineering-skills:tdd-guide           # Test-driven development
/superpowers:systematic-debugging       # Structured debugging approach
/superpowers:subagent-driven-development # Parallel agent development
```

### Business & Strategy

| Plugin | Skills | Description |
|--------|--------|-------------|
| [c-level-plugin](./c-level-plugin/) | `ceo-advisor`, `cto-advisor` | C-level advisory skills |
| [product-plugin](./product-plugin/) | 5 skills | Product management and UX design |
| [marketing-plugin](./marketing-plugin/) | 5 skills | Marketing strategy and content creation |

**Example Usage:**
```
/c-level-skills:ceo-advisor        # Strategic decision-making
/c-level-skills:cto-advisor        # Technical leadership
/product:agile-product-owner       # Product ownership best practices
```

### Networking & APIs

| Plugin | Skills | Description |
|--------|--------|-------------|
| [nettools-plugin](./nettools-plugin/) | `ping`, `ports`, `dns`, `trace` | Network diagnostics |
| [api-plugin](./api-plugin/) | `test`, `mock`, `doc`, `curl` | API testing and documentation |

### Data & Text Processing

| Plugin | Skills | Description |
|--------|--------|-------------|
| [json-plugin](./json-plugin/) | `format`, `validate`, `diff`, `convert` | JSON utilities |
| [regex-plugin](./regex-plugin/) | `build`, `test`, `explain`, `library` | Regex building and testing |
| [text-plugin](./text-plugin/) | `case`, `count`, `lorem`, `slug` | Text transformation tools |
| [logs-plugin](./logs-plugin/) | `parse`, `search`, `stats`, `tail` | Log file analysis |

**Example Usage:**
```
/json:format '{"a":1,"b":2}'       # Pretty print
/json:diff file1.json file2.json   # Compare JSON files
/regex:build                       # Interactive regex builder
```

### Documents & Files

| Plugin | Skills | Description |
|--------|--------|-------------|
| [document-plugin](./document-plugin/) | `pdf`, `docx`, `pptx`, `xlsx` | Office document processing |
| [file-plugin](./file-plugin/) | `hash`, `diff`, `find-dups`, `size` | File operations and analysis |
| [db-plugin](./db-plugin/) | `query`, `schema`, `backup`, `migrate` | Database utilities |

### Cryptography & Security

| Plugin | Skills | Description |
|--------|--------|-------------|
| [crypto-plugin](./crypto-plugin/) | `hash`, `encode`, `password`, `jwt` | Cryptographic utilities |

**Example Usage:**
```
/crypto:hash "my secret"           # MD5, SHA1, SHA256, SHA512
/crypto:password --length 20       # Generate secure password
/crypto:jwt <token>                # Decode and validate JWT
```

### Calculators & Converters

| Plugin | Skills | Description |
|--------|--------|-------------|
| [calc-plugin](./calc-plugin/) | `unit`, `finance`, `subnet`, `date` | Various calculators |
| [time-plugin](./time-plugin/) | `convert`, `schedule`, `countdown`, `cron` | Timezone and scheduling tools |
| [color-plugin](./color-plugin/) | `convert`, `palette`, `contrast`, `gradient` | Color format tools |

### Creative & Design

| Plugin | Skills | Description |
|--------|--------|-------------|
| [creative-plugin](./creative-plugin/) | 5 skills | Algorithmic art, brand guidelines, theme design |

### Performance & Testing

| Plugin | Skills | Description |
|--------|--------|-------------|
| [perf-plugin](./perf-plugin/) | `benchmark`, `profile`, `memory`, `lighthouse` | Performance testing tools |

### Scaffolding & Generation

| Plugin | Skills | Description |
|--------|--------|-------------|
| [scaffold-plugin](./scaffold-plugin/) | `react`, `python`, `node`, `go` | Project scaffolding |
| [qr-plugin](./qr-plugin/) | `generate`, `decode`, `wifi`, `vcard` | QR code generation |

### External Services

| Plugin | Skills | Description |
|--------|--------|-------------|
| [weather-plugin](./weather-plugin/) | `current`, `forecast`, `alerts`, `history` | Weather information |
| [finance-plugin](./finance-plugin/) | `stock`, `crypto`, `currency`, `compound` | Financial data and calculators |

## Installation

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) v1.0.33 or higher
- Windows 11 (for full compatibility) or macOS/Linux
- PowerShell 7+ (for Windows scripts)

### Clone the Repository

```bash
git clone https://github.com/saint1415/claude-plugins.git
cd claude-plugins
```

### Verify Installation

```bash
claude --plugin-dir ./osint-plugin --version
```

## Configuration

### API Keys (Environment Variables)

Some plugins require API keys for external services:

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

## Usage Examples

### Security Audit Workflow

```bash
# Load security plugins
claude --plugin-dir ./osint-plugin --plugin-dir ./ssl-plugin --plugin-dir ./compliance-plugin

# In Claude Code:
/osint:domain targetcompany.com
/ssl:check targetcompany.com
/compliance:pci
```

### DevOps Workflow

```bash
# Load DevOps plugins
claude --plugin-dir ./docker-plugin --plugin-dir ./k8s-plugin --plugin-dir ./terraform-plugin

# In Claude Code:
/docker:cleanup
/k8s:status
/terraform:plan
```

### Engineering Workflow

```bash
# Load engineering plugins
claude --plugin-dir ./engineering-plugin --plugin-dir ./superpowers-plugin

# In Claude Code:
/engineering-skills:senior-backend
/superpowers:test-driven-development
```

## Orchestration

The **orchestration-plugin** enables multi-agent workflows using the Builder/Validator pattern.

### Concepts

- **Builder Agent**: Focuses on ONE task, self-validates with embedded hooks
- **Validator Agent**: Verifies Builder's work, runs validation checks
- **Task System**: Uses Claude Code's TaskCreate/TaskUpdate for agent communication

### Usage

```bash
claude --plugin-dir ./orchestration-plugin

# In Claude Code:
/orchestration:plan-with-team Update all API endpoints to use async/await
/orchestration:execute-plan specs/async-update.md
```

### Setting Up Hooks

Copy the hooks to your project:

```powershell
Copy-Item -Path ".\orchestration-plugin\hooks\*" -Destination ".\.claude\hooks\" -Recurse
```

See [orchestration-plugin/README.md](./orchestration-plugin/README.md) for detailed setup instructions.

## Project Structure

```
claude-plugins/
├── README.md                    # This file
├── .gitignore                   # Git ignore rules
│
├── osint-plugin/                # Security & OSINT
│   ├── .claude-plugin/
│   │   └── plugin.json          # Plugin manifest
│   └── skills/
│       ├── domain/SKILL.md
│       ├── ip/SKILL.md
│       └── ...
│
├── engineering-plugin/          # Engineering expertise
│   ├── .claude-plugin/
│   │   └── plugin.json
│   └── skills/
│       ├── senior-backend/SKILL.md
│       ├── senior-frontend/SKILL.md
│       └── ...
│
├── orchestration-plugin/        # Multi-agent orchestration
│   ├── .claude-plugin/
│   │   └── plugin.json
│   ├── agents/
│   │   ├── builder.md
│   │   └── validator.md
│   ├── hooks/
│   │   ├── pre_tool_use.py
│   │   ├── post_tool_use.py
│   │   └── ...
│   └── skills/
│       ├── plan-with-team/SKILL.md
│       └── execute-plan/SKILL.md
│
└── ... (37 more plugins)
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/my-new-plugin`
3. **Follow the plugin structure**:
   ```
   my-plugin/
   ├── .claude-plugin/
   │   └── plugin.json
   ├── skills/
   │   └── my-skill/
   │       └── SKILL.md
   └── README.md
   ```
4. **Test your plugin**: `claude --plugin-dir ./my-plugin`
5. **Submit a pull request**

### Plugin Manifest Template

```json
{
  "name": "my-plugin",
  "description": "Brief description of what this plugin does",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  },
  "keywords": ["keyword1", "keyword2"]
}
```

### Skill Template

```markdown
# Skill Name

<skill-description>
Brief description of what this skill does.
</skill-description>

## Instructions

Detailed instructions for Claude on how to execute this skill.

## Examples

Example usage and expected outputs.
```

## Credits

- **Original Plugins**: [crissantos](https://github.com/saint1415)
- **Engineering, Marketing, Product, PM, RA/QM, C-Level, Creative plugins**: [Alireza Rezvani](https://github.com/alirezarezvani/claude-skills) (MIT License)
- **Superpowers plugin**: [superpowers](https://github.com/superpowers) (MIT License)
- **Orchestration concepts**: [IndyDevDan](https://github.com/disler) / [YouTube](https://youtube.com/@IndyDevDan)

## License

This project is licensed under the MIT License - see individual plugin directories for specific license information.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-02-04 | Added orchestration-plugin with Builder/Validator pattern, Windows hooks |
| 2.0.0 | 2026-02-02 | Added 11 plugins from skills collection - now 39 plugins with 189 skills |
| 1.1.0 | 2026-02-02 | Expanded to 28 plugins with 112 skills, Windows compatibility fixes |
| 1.0.0 | 2026-02-02 | Initial release with 4 plugins and 16 skills |

