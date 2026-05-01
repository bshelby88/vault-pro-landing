# Show HN draft — Vault Pro

## Title
Show HN: Claude-powered Obsidian vault – dashboards, multi-agent specs, daily templates

## Body

I run Claude Code daily and Obsidian as my second brain. They never talked to each other — Claude has no persistent home, Obsidian has no agent layer. So I built the bridge.

Vault Pro is an Obsidian vault, pre-structured with 8 numbered folders, that's designed to be operated by Claude Code:

- **00-Start** — Dashboard.md with Dataview queries that pull today's tasks, agent runs, active projects
- **10-Skills** — Skill index pointing at `~/.claude/skills/`
- **20-Agents** — 3 runnable Hermes multi-agent specs (orchestrator + worker patterns)
- **30-Daily** — Daily + monthly review templates with EOD reflection blocks
- **40-Projects** — Project tracker w/ status fields for Dataview
- **50-Workflows** — Lead-gen pipeline + 4 Hermes orchestration patterns (sequential, parallel, hierarchical, blackboard)
- **60-Knowledge** — ICP framework, retrospectives folder
- **70-Templates** — Note + agent + project starter templates (Templater-compatible)

The point isn't the templates — it's that Claude Code can read/write the vault as its working memory. Open the dashboard, ask Claude "what's blocked?", it reads `40-Projects/`, surfaces blockers, opens the right note. End of day, fill the daily template, the monthly review auto-rolls.

Install: `unzip vault-pro.zip`, open as Obsidian vault. No MCP, no plugins required (Templater + Dataview recommended but optional).

Free this week. Lifetime updates: https://vault-pro-landing.vercel.app

GitHub: https://github.com/bshelby88/claude-obsidian-vault-pro

Open to feedback — what folder/template should be in v1.1?

---
**Why post this:** The "Claude meets Obsidian" pattern is something a lot of people are hand-rolling. Sharing the structure that worked for me + the multi-agent specs that turned it from a notebook into an actual workspace.
