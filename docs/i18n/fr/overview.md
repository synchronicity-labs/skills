---
title: "Skills d'agent de sync. labs"
subtitle: "Synchronisez les lèvres, doublez et créez des vidéos parlantes depuis Claude Code, Codex, Cursor et d'autres agents."
description: "Installez les skills d'agent officiels de sync. labs pour synchroniser les lèvres de vidéos, faire parler des photos et des personnages IA, traduire et doubler, corriger des mots prononcés, localiser des campagnes, lancer du lipsync par lots et intégrer sync. dans vos applications depuis votre agent."
og:description: "Skills d'agent officiels de sync. labs pour le lipsync, le doublage, les photos parlantes, la modification de dialogues, la localisation de campagnes, les traitements par lots et les intégrations API."
source-sha256: b2127b6c0b20e7920f0f6566eac05cca6fab410de78464947c0690fc7d640c07
---

# Skills d'agent de sync. labs

Les skills d'agent de sync. labs apprennent à votre agent à réaliser le travail sync. de bout en bout : synchroniser les lèvres de vidéos, faire parler des photos et des personnages IA, traduire et doubler, corriger des mots prononcés, localiser des campagnes entières, lancer du lipsync à grande échelle et intégrer sync. dans vos propres applications. Ils fonctionnent avec Claude Code, Codex, Cursor, Gemini CLI, Hermes et tout agent compatible avec [Agent Skills](https://agentskills.io).

Chaque skill est un dossier contenant un `SKILL.md` d'instructions, ainsi que des fichiers de référence et des scripts que l'agent ne charge que lorsqu'une tâche en a besoin. Décrivez ce que vous voulez en langage courant, et l'agent choisit le skill adapté.

<!-- card icon="fa-brands fa-github" -->
**[synchronicity-labs/skills sur GitHub](https://github.com/synchronicity-labs/skills)**
Le code source de chaque skill, les manifestes du plugin et un journal des modifications. Sous licence MIT.

> [!NOTE]
> Chaque skill annonce le coût avant de lancer un travail payant et attend votre accord. Le skill setup lui-même ne lance jamais de travail payant.

## Installer les skills

### Tous les agents (skills.sh)

Installez tous les skills avec [skills.sh](https://skills.sh) :

```bash
npx skills add synchronicity-labs/skills
```

Ajoutez `--skill <name>` pour installer un seul skill, par exemple `--skill lipsync`, ou `--agent claude-code` pour choisir l'agent.

### Plugin Claude Code

Le plugin installe les skills et connecte le serveur MCP de sync. en une seule étape.

1. **Ajoutez la marketplace**

   ```text
   /plugin marketplace add synchronicity-labs/skills
   ```

2. **Installez le plugin**

   ```text
   /plugin install sync@sync
   ```

3. **Connectez-vous**

   Exécutez `/mcp`, sélectionnez `sync` et connectez-vous avec votre compte sync.

### Codex et Cursor

Codex et Cursor lisent les manifestes du plugin dans les dossiers `.codex-plugin/` et `.cursor-plugin/` du dépôt. Les deux manifestes connectent le serveur MCP hébergé de sync. Vous pouvez aussi installer les skills avec skills.sh et connecter le serveur en suivant les étapes du [skill setup](setup.md) pour votre agent.

## Connecter sync.

Les skills utilisent le [serveur MCP de sync.](https://sync.so/docs/plugins-and-extensions/mcp-server) hébergé à l'adresse `https://mcp.sync.so/mcp`. Vous vous connectez avec votre compte sync., il n'y a donc aucune clé à copier. Le [skill setup](setup.md) guide n'importe quel agent pendant la connexion, et sa page détaille les étapes pour chaque agent.

Pour les scripts, la CI, les agents qui ne peuvent pas utiliser de serveurs distants et le [skill sync-api](sync-api.md), créez plutôt une [clé API](https://sync.so/settings/api-keys) et définissez-la dans `SYNC_API_KEY`. Pour utiliser les mêmes outils MCP en local avec cette clé, lancez le paquet npm :

```bash
npx -y @sync.so/mcp-server@latest
```

## Skills

| Skill | Ce qu'il fait | Essayez |
| --- | --- | --- |
| [setup](setup.md) | Connecte sync. à votre agent, vérifie votre compte et vous mène jusqu'à une première vidéo. | « Configure sync. » |
| [lipsync](lipsync.md) | Synchronise les lèvres d'une vidéo avec un nouvel audio ou un script saisi. | « Synchronise les lèvres de ./talk.mp4 sur ./new-take.wav » |
| [talking-photo](talking-photo.md) | Fait parler une photo, un portrait ou un personnage. | « Fais dire à ce portrait : bienvenue dans l'équipe » |
| [ai-video-to-talking](ai-video-to-talking.md) | Donne la parole aux clips générés par IA avec Veo, Kling, Sora et d'autres, y compris les scènes à plusieurs plans. | « Mon clip Veo n'a pas de dialogue. Fais-lui dire cette réplique. » |
| [translate-and-dub](translate-and-dub.md) | Double une vidéo dans d'autres langues avec des lèvres synchronisées. | « Double cette vidéo YouTube en espagnol » |
| [edit-dialogue](edit-dialogue.md) | Modifie ou supprime quelques mots prononcés, avec la voix même de la personne qui parle. | « Remplace le prix que j'annonce par 49 $ » |
| [localize-campaign](localize-campaign.md) | Localise un ensemble de vidéos pour plusieurs marchés : plan, pilote, exécution, fiche de relecture. | « Décline ces trois pubs en espagnol, en allemand et en japonais » |
| [batch-lipsync](batch-lipsync.md) | Synchronise les lèvres pour chaque ligne d'un CSV ou d'un dossier, avec reprise, dans les limites de votre forfait ou, avec les forfaits Scale, via la Batch API. | « Synchronise chaque ligne de leads.csv sur presenter.mp4 » |
| [sync-api](sync-api.md) | Intègre sync. dans des applications avec l'API REST ou les SDK Python et TypeScript : imports, idempotence, webhooks, erreurs. | « Ajoute le lipsync de sync. à mon app Next.js » |
| [troubleshoot](troubleshoot.md) | Trouve pourquoi une tâche a échoué, s'est bloquée ou a été refusée, la reprend sans payer deux fois et peut signaler le problème à sync. | « Mon lipsync a échoué, pourquoi ? » |

La page de chaque skill présente des exemples de prompts, les prérequis, les questions fréquentes et la façon de vérifier que tout fonctionne.

## Le travail payant est toujours validé d'abord

Chaque génération est facturée : chaque skill annonce donc le coût avant de lancer un travail payant et attend votre feu vert. Si vous préférez ne pas être sollicité deux fois, fixez un budget dès le départ, par exemple « vas-y, tout ce qui coûte moins de 5 $ me va ». Les traitements portant sur de nombreuses vidéos, comme [localize-campaign](localize-campaign.md) et [batch-lipsync](batch-lipsync.md), chiffrent l'ensemble du traitement et proposent un pilote avant le reste. Après cette seule validation, le reste démarre ensemble plutôt qu'un par un.

<!-- llms-ignore -->
## Ressources associées

- [Serveur MCP](https://sync.so/docs/plugins-and-extensions/mcp-server) : connecter des clients IA à sync. labs
- [Plugin ChatGPT](https://sync.so/docs/plugins-and-extensions/chatgpt-plugin) : utiliser sync. labs dans ChatGPT
- [SDK](https://sync.so/docs/developer-guides/sdk) : SDK officiels Python et TypeScript
- [Authentification](https://sync.so/docs/api-reference/guides/authentication) : créer et utiliser une clé API
<!-- /llms-ignore -->
