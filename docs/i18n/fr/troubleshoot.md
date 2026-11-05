---
title: "Skill troubleshoot"
subtitle: "Trouvez pourquoi une tâche a échoué, s'est bloquée ou a été refusée, et reprenez-la sans payer deux fois."
description: "Le skill d'agent troubleshoot de sync. labs trouve pourquoi une tâche sync. a échoué, s'est bloquée ou a été refusée, explique la vraie cause en termes simples, reprend le travail sans lancer une deuxième tâche payante et peut signaler le problème à sync."
og:description: "Découvrez depuis votre agent pourquoi une tâche sync. a échoué, s'est bloquée ou a été refusée, et reprenez-la sans payer deux fois."
source-sha256: 8de9f50b08fda9e8256cefecc063b3e44871e28eb125c0e2060560fcdabb8fff
---

# troubleshoot

> [!TIP]
> Installez ce skill avec `npx skills add synchronicity-labs/skills --skill troubleshoot`, ou obtenez tous les skills avec le plugin Claude Code. Voir [Skills d'agent](overview.md).

## Ce qu'il fait

`troubleshoot` trouve pourquoi une tâche sync. a échoué, s'est bloquée ou a été refusée, vous explique la vraie cause en termes simples et reprend le travail sans lancer une deuxième tâche payante. Quand le problème venait d'une erreur peu claire ou d'une fonctionnalité manquante, il peut aussi envoyer un court rapport à l'équipe sync., sans secrets ni médias joints.

## Quand l'utiliser

| Ce qui s'est passé | Utilisez |
| --- | --- |
| Une tâche a échoué, a été refusée ou semble bloquée | `troubleshoot` |
| Une erreur 402, 429 ou une autre erreur sync. | `troubleshoot` |
| Les outils sync. ont disparu ou indiquent que vous êtes déconnecté | `troubleshoot`, qui vous reconnecte de la même façon que [setup](setup.md) |
| Vous n'avez pas encore connecté sync. | [setup](setup.md) |
| Votre propre code reçoit des erreurs de l'API | [sync-api](sync-api.md) |

## Essayez

- « Mon lipsync a échoué, pourquoi ? »
- « Ce doublage est en cours de traitement depuis 20 minutes »
- « J'obtiens sans arrêt concurrency_limit_reached »
- « La vidéo est sortie, mais la bouche n'a pas l'air juste »

## Ce dont vous avez besoin

- Le serveur MCP de sync. connecté, pour lire l'état des tâches et votre compte. Sans lui, le skill peut quand même expliquer un message d'erreur que vous collez.
- Le texte de l'erreur, ou l'ID de la génération ou du batch si vous l'avez.

## Questions fréquentes

**La tâche qui a échoué m'a-t-elle été facturée ?**
Non. Les générations qui échouent ne sont pas facturées.

**C'est toujours en cours de traitement. Dois-je la relancer ?**
Non. En attente ne veut pas dire échoué, et une deuxième tâche ne finira pas plus tôt. Le skill continue de vérifier la même tâche.

**Ma requête a expiré. Est-elle passée ?**
Peut-être. Le skill cherche la tâche, ou relance la requête identique avec la même clé, ce qui renvoie l'original au lieu d'en lancer une autre.

**Le résultat n'a pas l'air bon.**
Les causes habituelles viennent de la source : un visage tourné ou masqué, plusieurs personnes dans le cadre, de la musique sous la voix ou une faible résolution. Le skill vérifie ces points et suggère `sync-3` si un modèle plus ancien a été utilisé. Réessayer est une nouvelle génération payante, il annonce donc d'abord le coût.

**Que contient le rapport envoyé à sync. ?**
Le type de problème, l'erreur exacte, l'outil et l'ID de la tâche. Jamais votre clé, des liens signés, des données personnelles ni des médias.

## Tout fonctionne si

- Vous obtenez la vraie cause, avec le code d'erreur quand il y en a un.
- Aucune deuxième tâche payante ne démarre sans que vous approuviez une nouvelle tentative.
- Le travail d'origine reprend là où il s'était arrêté.
