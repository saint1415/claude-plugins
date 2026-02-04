# Community Plugins

This directory contains community plugin collections cloned from GitHub.

## Included Collections

| Directory | Source | Contents |
|-----------|--------|----------|
| `plugins-plus-skills/` | [jeremylongshore/claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) | 270+ plugins, 1,537 skills |
| `trailofbits-skills/` | [trailofbits/skills](https://github.com/trailofbits/skills) | Security research skills |
| `agent-skills/` | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 200+ agent skills |

## Usage

Load plugins from community collections:

```powershell
# Trail of Bits security skills
claude --plugin-dir .\community\trailofbits-skills

# Specific plugin from plugins-plus-skills
claude --plugin-dir .\community\plugins-plus-skills\plugins\devops-automation-pack
```

## Updating

To update community plugins:

```powershell
cd community\plugins-plus-skills
git pull

cd ..\trailofbits-skills
git pull

cd ..\agent-skills
git pull
```

## Note

These directories are git submodules/clones and are not tracked in the main repository.
