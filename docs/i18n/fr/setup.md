---
title: "Skill setup"
subtitle: "Connectez sync. à votre agent, vérifiez votre compte et obtenez une première vidéo."
description: "Le skill d'agent setup de sync. labs connecte sync. à Claude Code, Codex, Cursor et d'autres agents, affiche votre forfait et vos crédits, et propose une première vidéo. Il ne lance jamais de travail payant."
og:description: "Connectez sync. à votre agent, vérifiez votre compte, votre forfait et vos crédits, et obtenez une première vidéo."
source-sha256: 8bf4757e0b9fd57ed1bb43b1d923220a2e62a7d62a8dd8ae8c1dd87f2a19d10a
---

# setup

> [!TIP]
> Installez ce skill avec `npx skills add synchronicity-labs/skills --skill setup`, ou obtenez tous les skills avec le plugin Claude Code. Voir [Skills d'agent](overview.md).

## Ce qu'il fait

`setup` connecte sync. à votre agent et vous mène à une première vidéo en quelques minutes. Il vérifie la connexion, vous connecte si nécessaire, affiche votre compte, votre forfait et vos crédits restants, puis liste ce que vous pouvez créer avec un exemple de prompt pour chaque cas. Le skill setup lui-même ne lance jamais de travail payant.

## Quand l'utiliser

- Juste après avoir installé les skills ou le plugin.
- Quand les outils sync. sont absents ou déconnectés.
- Pour vérifier votre compte, votre forfait ou vos crédits.

Les demandes de création comme « synchronise les lèvres de cette vidéo » vont directement au skill concerné, qui vous connecte de la même façon si nécessaire. Si quelque chose a échoué ou semble bloqué, utilisez [troubleshoot](troubleshoot.md).

## Essayez

- « Configure sync. »
- « Combien de crédits sync me reste-t-il ? »

## Se connecter

| Agent | Comment |
| --- | --- |
| Claude Code avec le plugin | Exécutez `/mcp`, sélectionnez `sync` et connectez-vous |
| Claude Code sans le plugin | `claude mcp add --transport http sync https://mcp.sync.so/mcp`, puis `/mcp` |
| Claude.ai ou Claude Desktop | Settings, Connectors, Add custom connector, `https://mcp.sync.so/mcp` |
| Codex | `codex mcp add sync --url https://mcp.sync.so/mcp`, puis `codex mcp login sync` |
| Cursor | Ajoutez `{"mcpServers": {"sync": {"url": "https://mcp.sync.so/mcp"}}}` à `.cursor/mcp.json` |
| Scripts et CI | Définissez `SYNC_API_KEY`, ou lancez le serveur local avec `npx -y @sync.so/mcp-server@latest` |

Le serveur hébergé vous connecte avec votre compte sync., il n'y a donc aucune clé à copier. Pour une clé API, voir [Authentification](https://sync.so/docs/api-reference/guides/authentication). Pour en savoir plus sur le serveur lui-même, consultez le guide du [serveur MCP](https://sync.so/docs/plugins-and-extensions/mcp-server).

## Questions fréquentes

**Les outils sont introuvables alors que je viens de me connecter.**
La plupart des agents ne chargent les nouveaux serveurs MCP qu'après un redémarrage ou un rechargement.

**Ai-je besoin d'un forfait payant ?**
Non. Chaque compte démarre avec quelques générations gratuites par mois. Les forfaits payants augmentent les limites de durée et la concurrence, et suppriment le watermark à partir de Creator.

**Que choisir : le serveur hébergé ou npm ?**
Le serveur hébergé pour un usage interactif, puisque vous vous connectez avec votre compte. Le paquet npm avec une clé API pour les scripts, la CI et les agents qui ne peuvent pas utiliser de serveurs distants.

## Tout fonctionne si

- Vous voyez le nom de votre organisation et vos crédits ou votre quota restants.
- Vous obtenez une courte liste d'idées à essayer, et rien n'est facturé.
