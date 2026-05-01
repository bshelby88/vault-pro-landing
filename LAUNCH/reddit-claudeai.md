# r/ClaudeAI post — Vault Pro

## Title
Built a Claude-powered Obsidian vault — dashboards, multi-agent specs, daily templates [Free launch week]

## Body

Hey r/ClaudeAI 👋

If you run Claude Code AND Obsidian, you've probably noticed they don't talk to each other. Claude has no persistent home; Obsidian has no agent layer. Two halves of the same brain.

I built **Vault Pro** to bridge them — an Obsidian vault pre-structured to be operated by Claude Code:

**8 folders, all functional from day 1:**

- **00-Start** — Dashboard with live Dataview queries (today's tasks, agent runs, blocked projects)
- **10-Skills** — Skill index for `~/.claude/skills/`
- **20-Agents** — 3 runnable Hermes multi-agent specs (orchestrator + worker patterns)
- **30-Daily** — Daily + monthly review templates with EOD reflection
- **40-Projects** — Project tracker with status fields
- **50-Workflows** — Lead-gen pipeline + 4 Hermes orchestration patterns
- **60-Knowledge** — ICP framework + retrospectives
- **70-Templates** — Note + agent + project starters

**Why it works:** Claude reads the vault as working memory. "What's blocked?" → reads 40-Projects, opens the right note. EOD fill the daily template, monthly review auto-rolls (recurring agent that drafts the prior month).

**Install:** `unzip` → open as Obsidian vault. Templater + Dataview recommended.

**Free launch week**, lifetime updates: https://vault-pro-landing.vercel.app

**GitHub:** https://github.com/bshelby88/claude-obsidian-vault-pro

If you've been hand-rolling this layer, save yourself the bootstrap. Open to feature requests for v1.1.
