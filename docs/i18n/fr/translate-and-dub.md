---
title: "Skill translate-and-dub"
subtitle: "Doublez une vidéo dans d'autres langues avec des lèvres synchronisées."
description: "Le skill d'agent translate-and-dub de sync. labs traduit la parole d'une vidéo dans d'autres langues et resynchronise les lèvres de la personne qui parle, à partir d'un fichier local, d'une URL ou d'un lien YouTube, TikTok, Instagram ou Facebook."
og:description: "Doublez une vidéo dans d'autres langues avec des lèvres synchronisées depuis votre agent, avec d'abord une estimation par langue."
source-sha256: 7f634da776bfe7c98f91c58950211d376361728413314e96ff125972692270bb
---

# translate-and-dub

> [!TIP]
> Installez ce skill avec `npx skills add synchronicity-labs/skills --skill translate-and-dub`, ou obtenez tous les skills avec le plugin Claude Code. Voir [Skills d'agent](overview.md).

## Ce qu'il fait

`translate-and-dub` traduit la parole d'une vidéo dans d'autres langues et resynchronise les lèvres de la personne qui parle sur l'audio doublé. Vous obtenez un MP4 par langue, étiqueté avec sa langue. Il accepte un fichier local, une URL publique ou un lien YouTube, TikTok, Instagram ou Facebook.

## Quand l'utiliser

| Ce que vous avez | Utilisez |
| --- | --- |
| Une vidéo, une ou plusieurs langues | `translate-and-dub` |
| Plusieurs vidéos pour plusieurs marchés | [localize-campaign](localize-campaign.md) |
| Une vidéo et votre propre audio traduit | [lipsync](lipsync.md) |
| Des sous-titres uniquement | Ce n'est pas un travail pour sync. |

## Essayez

- « Double cette vidéo YouTube en espagnol et en portugais du Brésil »
- « Traduis ./keynote.mp4 en japonais »
- « Fais une version allemande de https://example.com/demo.mp4 »

## Ce dont vous avez besoin

- Le serveur MCP de sync. connecté, ou `SYNC_API_KEY` défini. Le skill [setup](setup.md) vous guide dans les deux cas.
- Une vidéo dont la piste audio contient la parole d'origine.

## Questions fréquentes

**Quelles langues sont prises en charge ?**
L'agent consulte la liste à jour avant de chiffrer. Si une langue n'y figure pas, il indique la plus proche qui est disponible.

**Comment le prix est-il calculé ?**
Selon la durée de la vidéo source, une fois par langue. L'estimation détaille le coût par langue et le total. Si des frais d'un fournisseur de voix externe ne sont pas inclus, l'agent le précise.

**Le texte à l'écran est-il traduit ?**
Non. Les titres, les sous-titres incrustés et les logos restent tels quels. Seule la parole change.

**Les langues sont-elles doublées l'une après l'autre ?**
Non. Après une seule validation, toutes les langues démarrent ensemble, dans la limite de votre forfait. Via le serveur MCP, cela représente un seul appel à `jobs_create-many`.

**Une langue a échoué.**
Chaque langue est un travail distinct : les autres se terminent quand même. L'agent indique laquelle a échoué et pourquoi.

**Le doublage a échoué avec une erreur du fournisseur de voix.**
Si vous avez connecté votre propre clé ElevenLabs à sync., les crédits ou la validité de cette clé sont la cause habituelle.

**Il a refusé de doubler un clip musical.**
Les chansons et clips musicaux protégés par le droit d'auteur nécessitent l'autorisation de l'ayant droit. Utilisez une vidéo qui vous appartient ou que vous avez le droit de localiser.

## Tout fonctionne si

- Les langues sont vérifiées avant l'estimation.
- Il y a un seul travail payant par langue, jamais une nouvelle soumission pour suivre l'avancement.
- Chaque lien de résultat est étiqueté avec sa langue.
