---
title: "Skill talking-photo"
subtitle: "Faites parler une photo, un portrait ou un personnage."
description: "Le skill d'agent talking-photo de sync. labs transforme une photo, un portrait ou un personnage illustré en vidéo parlante à partir d'un script ou d'un enregistrement, avec une voix choisie dans votre compte et une estimation avant toute création."
og:description: "Transformez une photo, un portrait ou un personnage illustré en vidéo parlante depuis votre agent."
source-sha256: 6aeeae5c018d350384c8f655da3d437d6aa76de342cb9d799b6880c5bf405d61
---

# talking-photo

> [!TIP]
> Installez ce skill avec `npx skills add synchronicity-labs/skills --skill talking-photo`, ou obtenez tous les skills avec le plugin Claude Code. Voir [Skills d'agent](overview.md).

## Ce qu'il fait

`talking-photo` transforme une image fixe en vidéo parlante. Donnez-lui une photo, un portrait ou un personnage illustré, ainsi qu'un script ou un enregistrement, et il renvoie un MP4 de ce visage en train de parler. La vidéo dure aussi longtemps que la parole.

Si vous n'avez pas encore d'image et que votre agent sait en générer, il propose d'en créer une qui fonctionne bien : un seul visage net, face à la caméra, cadré en buste.

## Quand l'utiliser

| Ce que vous avez | Utilisez |
| --- | --- |
| Une photo, un portrait ou un personnage illustré | `talking-photo` |
| Une vidéo d'une personne réelle | [lipsync](lipsync.md) |
| Un clip vidéo généré | [ai-video-to-talking](ai-video-to-talking.md) |

## Essayez

- « Fais dire au portrait de notre PDG : bienvenue chez Acme, nous sommes ravis de vous accueillir »
- « Crée une barista sympathique en dessin animé et fais-lui dire bonjour »
- « Fais dire à ./portrait.png ce qu'il y a dans ./greeting.mp3 »

## Ce dont vous avez besoin

- Le serveur MCP de sync. connecté, ou `SYNC_API_KEY` défini. Le skill [setup](setup.md) vous guide dans les deux cas.
- Une image avec un seul visage humain ou humanoïde bien net. Les animaux et les personnages non humanoïdes ne sont pas pris en charge.
- Un script, ou un fichier audio, une URL ou un asset sync.

## Questions fréquentes

**Peut-il choisir la voix pour moi ?**
Oui. Il liste les voix de votre compte et en propose deux ou trois qui conviennent au personnage. Dites « choisis toi-même » et il tranche.

**Pourquoi l'estimation est-elle « approximative » ?**
Pour un script, la durée de la parole est estimée à partir du nombre de mots tant qu'elle n'a pas été générée. La synthèse vocale est facturée séparément du lipsync, et l'agent le précise.

**Mon image a été refusée.**
sync. a besoin d'un seul visage net, d'une taille raisonnable. Les photos de groupe, les visages minuscules et les profils sont les causes habituelles. L'agent vous indique laquelle et suggère un cadrage plus serré en buste.

**Puis-je faire dire quelque chose à une célébrité ?**
Non. Le skill refuse de mettre des mots dans la bouche d'une personne réelle et identifiable pour tromper. Vos propres photos, votre équipe (avec son accord) et les personnages de fiction ne posent pas de problème.

## Tout fonctionne si

- L'agent choisit une voix dans la liste de votre compte, pas un ID inventé.
- Vous voyez l'estimation avant la création de la vidéo.
- Le résultat est un seul MP4 du visage prononçant exactement vos mots.
