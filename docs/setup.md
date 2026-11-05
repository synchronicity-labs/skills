# setup

## What it does

`setup` connects sync. to your agent and gets you to a first video in a couple of minutes. It checks the connection, signs you in if needed, shows your account, plan and remaining credits, and lists what you can make with an example prompt for each. Setup itself never starts paid work.

## When to reach for it

- Right after installing the skills or the plugin.
- When sync. tools are missing or signed out.
- To check your account, plan or credits.

Media requests like "lipsync this" go straight to their own skill, which connects you the same way when needed. If something failed or seems stuck, use [troubleshoot](troubleshoot.md).

## Try

- "Set up sync."
- "How much sync credit do I have left?"

## Connect

| Agent | How |
| --- | --- |
| Claude Code with the plugin | Run `/mcp`, select `sync` and sign in |
| Claude Code without the plugin | `claude mcp add --transport http sync https://mcp.sync.so/mcp`, then `/mcp` |
| Claude.ai or Claude Desktop | Settings, Connectors, Add custom connector, `https://mcp.sync.so/mcp` |
| Codex | `codex mcp add sync --url https://mcp.sync.so/mcp`, then `codex mcp login sync` |
| Cursor | Add `{"mcpServers": {"sync": {"url": "https://mcp.sync.so/mcp"}}}` to `.cursor/mcp.json` |
| Scripts and CI | Set `SYNC_API_KEY`, or run the local server with `npx -y @sync.so/mcp-server@latest` |

The hosted server signs you in with your sync. account, so there's no key to copy.

## Common questions

**It says the tools aren't there after I connected.**
Most agents load new MCP servers only after a restart or reload.

**Do I need a paid plan?**
No. Every account starts with a few free generations each month. Paid plans raise length limits and concurrency, and remove the watermark from Creator up.

**Which should I use, the hosted server or npm?**
The hosted server for interactive use, since you sign in with your account. The npm package with an API key for scripts, CI and agents that can't use remote servers.

## It's working if

- You see your organization's name and your remaining credits or allowance.
- You get a short list of things to try, and nothing is charged.
