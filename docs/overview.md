---
title: "sync. labs agent skills"
subtitle: "Lipsync, dub and make talking video from Claude Code, Codex, Cursor and other agents."
description: "Install the official sync. labs agent skills to lipsync videos, make photos and AI characters talk, translate and dub, fix spoken words, localize campaigns, run batch lipsync, and build sync. into apps from your agent."
og:description: "Official sync. labs agent skills for lipsync, dubbing, talking photos, dialogue edits, campaign localization, batch runs and API integrations."
---

# sync. labs agent skills

The sync. labs agent skills teach your agent how to do sync. work end to end: lipsync videos, make photos and AI characters talk, translate and dub, fix spoken words, localize whole campaigns, run lipsync in bulk, and build sync. into your own apps. They work with Claude Code, Codex, Cursor, Gemini CLI, Hermes and any agent that reads [Agent Skills](https://agentskills.io).

Each skill is a folder with a `SKILL.md` of instructions, plus reference files and scripts that the agent loads only when a task needs them. Describe what you want in plain language, and the agent picks the matching skill.

<!-- card icon="fa-brands fa-github" -->
**[synchronicity-labs/skills on GitHub](https://github.com/synchronicity-labs/skills)**
Source for every skill, the plugin manifests and a changelog. MIT licensed.

> [!NOTE]
> Every skill quotes the cost before starting paid work and waits for your approval. The setup skill itself never starts paid work.

## Install the skills

### Any agent (skills.sh)

Install every skill with [skills.sh](https://skills.sh):

```bash
npx skills add synchronicity-labs/skills
```

Add `--skill <name>` to install one skill, for example `--skill lipsync`, or `--agent claude-code` to pick the agent.

### Claude Code plugin

The plugin installs the skills and connects the sync. MCP server in one step.

1. **Add the marketplace**

   ```text
   /plugin marketplace add synchronicity-labs/skills
   ```

2. **Install the plugin**

   ```text
   /plugin install sync@sync
   ```

3. **Sign in**

   Run `/mcp`, select `sync` and sign in with your sync. account.

### Codex and Cursor

Codex and Cursor read the plugin manifests in the repository's `.codex-plugin/` and `.cursor-plugin/` folders. Both manifests connect the hosted sync. MCP server. You can also install the skills with skills.sh and connect the server by following the [setup skill](setup.md) steps for your agent.

## Connect sync.

The skills use the hosted [sync. MCP server](https://sync.so/docs/plugins-and-extensions/mcp-server) at `https://mcp.sync.so/mcp`. You sign in with your sync. account, so there's no key to copy. The [setup skill](setup.md) walks any agent through connecting, and its page lists the steps for each agent.

For scripts, CI, agents that can't use remote servers, and the [sync-api skill](sync-api.md), create an [API key](https://sync.so/settings/api-keys) and set it as `SYNC_API_KEY` instead. To use the same MCP tools locally with that key, run the npm package:

```bash
npx -y @sync.so/mcp-server@latest
```

## Skills

| Skill | What it does | Try |
| --- | --- | --- |
| [setup](setup.md) | Connects sync. to your agent, checks your account and gets you to a first video. | "Set up sync." |
| [lipsync](lipsync.md) | Lip-syncs a video to new audio or a typed script. | "Lipsync ./talk.mp4 to ./new-take.wav" |
| [talking-photo](talking-photo.md) | Makes a photo, portrait or character talk. | "Make this headshot say: welcome to the team" |
| [ai-video-to-talking](ai-video-to-talking.md) | Gives dialogue to AI-generated clips from Veo, Kling, Sora and others, including multi-shot scenes. | "My Veo clip has no dialogue. Make her say this line." |
| [translate-and-dub](translate-and-dub.md) | Dubs a video into other languages with matching lips. | "Dub this YouTube video into Spanish" |
| [edit-dialogue](edit-dialogue.md) | Changes or removes a few spoken words in the speaker's own voice. | "Change the price I say to $49" |
| [localize-campaign](localize-campaign.md) | Localizes a set of videos across markets: plan, pilot, run, review sheet. | "Make these three ads in Spanish, German and Japanese" |
| [batch-lipsync](batch-lipsync.md) | Lip-syncs every row of a CSV or folder, resumably, within your plan's limits or through the Batch API. | "Lipsync each row of leads.csv onto presenter.mp4" |
| [sync-api](sync-api.md) | Builds sync. into apps with the REST API or the Python and TypeScript SDKs: uploads, idempotency, webhooks, errors. | "Add sync. lipsync to my Next.js app" |
| [troubleshoot](troubleshoot.md) | Finds why a job failed, stalled or was rejected, resumes it without paying twice, and can report the problem to sync. | "My lipsync failed, why?" |

Each skill's page has example prompts, what you need, common questions and how to tell it's working.

## Paid work is always approved first

Every generation is billed, so every skill quotes the cost before it starts paid work and waits for you to say go. If you'd rather not be asked twice, give a budget up front, for example "go ahead, anything under $5 is fine". Runs over many videos, such as [localize-campaign](localize-campaign.md) and [batch-lipsync](batch-lipsync.md), quote the whole run and offer a pilot before the rest.

<!-- llms-ignore -->
## Related resources

- [MCP Server](https://sync.so/docs/plugins-and-extensions/mcp-server): connect AI clients to sync. labs
- [ChatGPT Plugin](https://sync.so/docs/plugins-and-extensions/chatgpt-plugin): use sync. labs inside ChatGPT
- [SDKs](https://sync.so/docs/developer-guides/sdk): official Python and TypeScript SDKs
- [Authentication](https://sync.so/docs/api-reference/guides/authentication): create and use an API key
<!-- /llms-ignore -->
