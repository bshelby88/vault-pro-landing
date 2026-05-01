# r/AI_Agents + r/ObsidianMD post — Vault Pro

## Title
Obsidian vault with built-in multi-agent specs — Claude Code reads it as working memory

## Body

If your stack includes Claude Code (or any agent framework with file access) and Obsidian, you've probably hit the same wall I did: agents have no persistent home, vaults have no agent layer.

I built **Vault Pro** — an Obsidian vault pre-structured for agent-driven operation.

**The interesting bits for agent builders:**

- **20-Agents/** ships 3 runnable Hermes multi-agent specs — orchestrator + worker pattern, parallel + hierarchical
- **50-Workflows/** has 4 orchestration patterns (sequential, parallel, hierarchical, blackboard) — drop in a real lead-gen pipeline as the example
- **00-Start/Dashboard.md** uses Dataview queries to surface "what should the agent work on today?" — agent reads it, picks tasks, writes back results
- **30-Daily/** templates close the loop: agent reflection block, EOD writes, monthly review auto-rolls

**Why this matters for agents:** without persistent memory, every agent run starts from zero. The vault becomes shared-state across agent runs without needing a vector DB.

**Install:** `unzip` → open as Obsidian vault. No MCP setup. Templater + Dataview optional but recommended.

**Free download:** https://vault-pro-landing.vercel.app
**GitHub:** https://github.com/bshelby88/claude-obsidian-vault-pro

Roast it. What agent pattern is missing from v1?
