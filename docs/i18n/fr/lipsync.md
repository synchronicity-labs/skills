---
title: "Skill lipsync"
subtitle: "Synchronisez les lèvres d'une vidéo avec un nouvel audio ou un script saisi."
description: "Le skill d'agent lipsync de sync. labs fait correspondre une personne filmée à une nouvelle parole : une voix off, une prise réenregistrée, une chanson ou un script auquel sync. donne une voix. Il annonce d'abord le coût et attend votre accord."
og:description: "Synchronisez depuis votre agent les lèvres d'une vidéo d'une personne réelle avec un nouvel audio ou un script saisi, avec une estimation avant toute génération."
source-sha256: 58edce026081002df42de0999296238a3f949e65c29651b4a6a39fe8a9bac0f3
---

# lipsync

> [!TIP]
> Installez ce skill avec `npx skills add synchronicity-labs/skills --skill lipsync`, ou obtenez tous les skills avec le plugin Claude Code. Voir [Skills d'agent](overview.md).

## Ce qu'il fait

`lipsync` prend une vidéo d'une personne qui parle et fait correspondre sa bouche à une nouvelle parole. Il peut s'agir d'une voix off, d'une prise réenregistrée, d'une chanson ou d'un script auquel sync. donne une voix pour vous. Vous récupérez un seul MP4, avec l'image d'origine et le nouvel audio.

Avant toute facturation, l'agent enregistre vos fichiers dans sync., calcule la durée de la parole, annonce le coût et attend votre feu vert.

## Quand l'utiliser

Utilisez-le quand vous avez déjà des images d'une personne réelle et que vous voulez lui faire dire autre chose.

| Ce que vous avez | Utilisez |
| --- | --- |
| Une vidéo et un nouvel audio, ou une vidéo et un script | `lipsync` |
| Un clip Veo, Kling, Sora ou d'un autre générateur | [ai-video-to-talking](ai-video-to-talking.md) |
| Une photo ou une illustration | [talking-photo](talking-photo.md) |
| Une vidéo qui doit parler une autre langue | [translate-and-dub](translate-and-dub.md) |
| Un ou deux mots erronés dans une prise par ailleurs réussie | [edit-dialogue](edit-dialogue.md) |
| Des dizaines de vidéos ou de fichiers audio | [batch-lipsync](batch-lipsync.md) |

## Essayez

- « Synchronise les lèvres de ./interview.mp4 sur ./new-take.wav »
- « Fais dire au gars de https://example.com/talk.mp4 ce qu'il y a dans ce mp3 »
- « Synchronise mon clip musical ./take3.mov sur le mix final »

## Ce dont vous avez besoin

- Le serveur MCP de sync. connecté, ou `SYNC_API_KEY` défini. Le skill [setup](setup.md) vous guide dans les deux cas.
- La vidéo sous forme de fichier local, d'URL publique, d'ID d'asset sync. ou de lien YouTube, TikTok, Instagram ou Facebook.
- La parole sous forme d'audio, ou d'un script accompagné d'une voix.

## Questions fréquentes

**Pourquoi s'est-il arrêté pour me demander avant de créer la vidéo ?**
Chaque génération est facturée : le skill affiche donc toujours l'estimation d'abord et attend votre accord. Dites dès le départ « vas-y, tout ce qui coûte moins de 5 $ me va » et il ne s'arrêtera pas deux fois.

**Mon audio est plus long que ma vidéo. Que se passe-t-il ?**
L'agent vous demande quel [mode de synchronisation](https://sync.so/docs/developer-guides/sync-mode) vous voulez : lire la vidéo en aller-retour (`bounce`, par défaut), la mettre en boucle, couper la parole à la fin de la vidéo, prolonger la vidéo en silence, ou accélérer ou ralentir la vidéo pour qu'elle corresponde (`remap`).

**Il y a deux personnes dans le plan.**
L'agent vous demande qui doit parler et oriente sync. vers ce visage. Sans cette précision, sync. choisit lui-même la personne qui parle.

**Il a refusé d'importer mon fichier.**
Il vérifie que le fichier est bien un média avant de dépenser quoi que ce soit. Un fichier qui n'est ni une vidéo ni un audio, ou une adresse d'import qui n'appartient pas à sync., arrête le traitement avec une explication. Rien n'est facturé.

**Quel modèle utilise-t-il ?**
`sync-3`, le modèle le plus performant, sauf si vous en demandez un autre. La liste provient de votre compte, pas du skill.

**Où est ma vidéo ?**
L'agent vous donne le lien exact du résultat. Dans un agent de code, il propose de télécharger le fichier à côté de votre source.

## Tout fonctionne si

- Vous voyez une estimation avant le lancement de toute génération.
- Les fichiers locaux sont importés une seule fois, et une nouvelle tentative réutilise le même import.
- Le message final contient un lien qui lit votre vidéo avec la nouvelle parole.
