---
title: "Skill edit-dialogue"
subtitle: "Modifiez ou supprimez quelques mots prononcés, avec la voix même de la personne qui parle."
description: "Le skill d'agent edit-dialogue de sync. labs corrige quelques mots prononcés dans une vidéo à un seul locuteur sans nouveau tournage : il transcrit, vous fait écouter un aperçu des nouveaux mots avec la voix du locuteur, puis resynchronise les lèvres sur ce seul passage."
og:description: "Corrigez un prix, un nom, une date ou un mot erroné dans une vidéo, avec la voix du locuteur, sans nouveau tournage."
source-sha256: e97f36785b8be640b8b1d969367d2b1f7e55a841dadf015870558bb2bc22faf2
---

# edit-dialogue

> [!TIP]
> Installez ce skill avec `npx skills add synchronicity-labs/skills --skill edit-dialogue`, ou obtenez tous les skills avec le plugin Claude Code. Voir [Skills d'agent](overview.md).

## Ce qu'il fait

`edit-dialogue` corrige quelques mots prononcés dans une vidéo sans nouveau tournage. Il transcrit la vidéo, associe votre correction aux mots exacts, synthétise les nouveaux mots avec la voix même du locuteur, vous fait écouter un aperçu, puis resynchronise les lèvres sur ce seul passage. Tout le reste conserve l'image et le son d'origine.

## Quand l'utiliser

| Ce que vous avez | Utilisez |
| --- | --- |
| Un prix, un nom, une date ou un mot erroné, ou une hésitation à couper | `edit-dialogue` |
| Un script entièrement nouveau | [lipsync](lipsync.md) avec une voix choisie |
| La même vidéo dans une autre langue | [translate-and-dub](translate-and-dub.md) |
| Un enregistrement personnalisé pour chaque destinataire | `edit-dialogue` pour les aperçus, puis [batch-lipsync](batch-lipsync.md) |

## Essayez

- « Dans ./promo.mp4, je dis 39 $ par mois. C'est 49 $ maintenant, corrige seulement ça. »
- « Coupe le “euh” après “facturé à l'année” dans cette vidéo »
- « Le nom doit être Siobhan, pas Shannon »

## Ce dont vous avez besoin

- Le serveur MCP de sync. connecté. Le skill [setup](setup.md) vous guide. La version REST de ce workflow est en accès anticipé ; voir [Transcription and Dialogue Editing](https://sync.so/docs/developer-guides/dialogue-editing).
- Une vidéo avec un seul locuteur, de 10 minutes maximum.

## Questions fréquentes

**Pourquoi me montre-t-il la transcription ?**
Pour que vous parliez tous les deux des mêmes mots. Chaque modification et chaque suppression est liée à un mot de la transcription, ce qui garantit une correction exacte.

**L'aperçu est-il payant ?**
Il peut l'être. L'aperçu clone la voix du locuteur et synthétise les nouveaux mots : l'agent le signale donc en confirmant les modifications. La vidéo finale fait l'objet d'une estimation séparée avant sa création.

**Un nom est mal prononcé.**
Demandez une prononciation. L'agent ajoute une graphie phonétique comme « shivawn », écrite comme un mot ordinaire, et crée un nouvel aperçu.

**Certaines modifications ont échoué.**
En général, le nouveau texte est trop long pour l'espace qu'il occupe. L'agent indique les modifications qui ont échoué et propose une formulation plus courte.

**Puis-je remplacer un paragraphe entier ?**
Ce workflow est fait pour des mots ciblés. Pour un nouveau script, lipsync avec une voix est le meilleur outil, et l'agent vous le dira.

## Tout fonctionne si

- Dans l'audio de l'aperçu, seuls vos mots ont changé.
- Vous validez l'aperçu et le coût avant la création de la vidéo.
- Le résultat lit la vidéo d'origine avec seulement ces mots différents.
