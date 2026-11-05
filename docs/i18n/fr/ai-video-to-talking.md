---
title: "Skill ai-video-to-talking"
subtitle: "Donnez la parole aux clips générés par IA avec Veo, Kling, Sora et d'autres."
description: "Le skill d'agent ai-video-to-talking de sync. labs donne la parole aux vidéos générées par IA avec Veo, Kling, Sora, Runway et d'autres générateurs, choisit une voix adaptée et synchronise les lèvres du personnage, y compris dans les scènes à plusieurs plans."
og:description: "Faites dire vos répliques aux personnages de vidéos générées par IA, y compris dans des scènes à plusieurs plans avec deux personnages."
source-sha256: 2da61aa54d453eba92f1fa339fa9da3fa171c87d410601398b6427170f09c5bd
---

# ai-video-to-talking

> [!TIP]
> Installez ce skill avec `npx skills add synchronicity-labs/skills --skill ai-video-to-talking`, ou obtenez tous les skills avec le plugin Claude Code. Voir [Skills d'agent](overview.md).

## Ce qu'il fait

`ai-video-to-talking` donne la parole aux vidéos générées par IA. Les clips de Veo, Kling, Sora, Runway, Hailuo, Luma, Seedance ou Wan sont souvent muets, ou contiennent des paroles dont vous ne voulez pas. Ce skill écrit la réplique ou reprend la vôtre, choisit une voix qui convient au personnage et synchronise ses lèvres pour qu'il parle vraiment.

sync. ne génère pas la vidéo. Si vous n'avez qu'une idée, le skill rédige pour votre générateur vidéo un prompt qui produit un clip facile à synchroniser, puis prend le relais une fois que vous l'avez.

## Quand l'utiliser

| Ce que vous avez | Utilisez |
| --- | --- |
| Un clip généré, ou une idée de clip | `ai-video-to-talking` |
| Des images réelles et une voix off | [lipsync](lipsync.md) |
| Une image fixe | [talking-photo](talking-photo.md) |

## Essayez

- « Mon clip Veo d'une barista n'a pas de dialogue. Fais-lui dire : bonjour, encore un latte au lait d'avoine ? »
- « Il me faut une pub façon UGC où un gars tient notre boisson énergisante et dit qu'elle est bonne. Je ferai le clip dans Kling. »
- « Cette scène Sora montre deux personnages qui parlent. Donne-leur ces répliques. »

## Ce dont vous avez besoin

- Le serveur MCP de sync. connecté, ou `SYNC_API_KEY` défini. Le skill [setup](setup.md) vous guide dans les deux cas.
- Le clip, ou l'accès à un générateur vidéo.
- La réplique, ou une description de ce que le personnage doit dire.

## Questions fréquentes

**Qu'est-ce qui rend un clip généré facile à synchroniser ?**
Un seul personnage face à la caméra, un visage qui occupe une bonne partie du cadre, une bouche dégagée, une caméra stable, un seul plan continu et un personnage qui bouge déjà comme s'il parlait. Le guide de prompts du skill détaille tout cela, avec un exemple de prompt.

**Ma réplique est plus longue que le clip.**
Les clips générés durent souvent de 5 à 10 secondes, soit environ 12 à 25 mots. Le skill propose de raccourcir la réplique, de générer un clip plus long ou d'utiliser un [mode de synchronisation](https://sync.so/docs/developer-guides/sync-mode) qui prolonge la vidéo.

**Peut-il gérer deux personnages ou plusieurs plans ?**
Oui, avec l'outil de timeline. Chaque réplique reçoit sa propre voix et est placée sur le plan où ce personnage parle. Les répliques, les voix et le coût total sont validés avant toute création.

**Puis-je utiliser ma propre voix ?**
Oui, enregistrez-la et transmettez l'audio. Le skill peut aussi cloner une voix, mais seulement si vous le demandez et que l'échantillon vous appartient. Le clonage enregistre une voix dans votre compte une seule fois ; si la réponse se perd, le skill vérifie votre liste de voix avant de réessayer.

## Tout fonctionne si

- Le personnage dit exactement vos mots, avec une voix qui lui va.
- Rien n'est généré avant que vous ayez validé la réplique, la voix et le coût.
- Dans une scène à plusieurs plans, chaque réplique arrive au bon personnage.
