---
title: "Skill batch-lipsync"
subtitle: "Synchronisez les lèvres pour chaque ligne d'un CSV ou d'un dossier, avec reprise, dans les limites de votre forfait. Les batches en file d'attente nécessitent l'approbation de l'organisation et un forfait Scale ou supérieur."
description: "Le skill d'agent batch-lipsync de sync. labs synchronise les lèvres de nombreuses vidéos en une fois à partir d'un CSV, d'un tableur, d'un dossier ou d'une liste : il chiffre l'ensemble du traitement, propose un pilote, respecte la concurrence de votre forfait et reprend sans payer deux fois."
og:description: "Synchronisez depuis votre agent les lèvres pour chaque ligne d'un CSV ou d'un dossier, avec reprise, dans les limites de votre forfait. Les batches en file d'attente nécessitent l'approbation de l'organisation et un forfait Scale ou supérieur."
source-sha256: 88b105777897ba2ccc422d0ae150405831fcb548f0979660ae8d98f556b64469
---

# batch-lipsync

> [!TIP]
> Installez ce skill avec `npx skills add synchronicity-labs/skills --skill batch-lipsync`, ou obtenez tous les skills avec le plugin Claude Code. Voir [Skills d'agent](overview.md).

## Ce qu'il fait

`batch-lipsync` synchronise les lèvres de nombreuses vidéos en une fois : un résultat par ligne d'un CSV, d'un tableur, d'un dossier ou d'une liste comme « ce présentateur avec chacun de ces 40 fichiers audio ». Il crée un manifeste, chiffre l'ensemble du traitement, propose un pilote, puis traite chaque ligne dans les limites de votre forfait et rassemble les résultats dans un tableau.

Avec une clé API, il utilise un script fourni, `sync_batch.py`, qui importe chaque fichier une seule fois, respecte la concurrence de votre forfait, reprend après une interruption et télécharge chaque résultat. Via le serveur MCP de sync., il lance toutes les lignes en un seul appel à `jobs_create-many`, qui respecte la concurrence de votre forfait, puis les suit toutes avec `jobs_get-many`. Si ces outils ne sont pas proposés, il lance une génération par ligne.

Avec l'approbation de l'organisation et un forfait Scale ou supérieur, un gros traitement de 20 à 500 lignes courtes qui peut attendre plusieurs heures peut passer par la [Batch API](https://sync.so/docs/api-reference/guides/batch-processing), avec le script ou les outils batch du serveur MCP. L'accès est désactivé par défaut, y compris pour les tests à blanc. Contactez support@sync.so pour demander l'approbation. Les utilisateurs et les administrateurs de l'organisation ne peuvent pas l'activer eux-mêmes.

## Quand l'utiliser

| Ce que vous avez | Utilisez |
| --- | --- |
| De nombreuses lignes de vidéo avec audio ou script | `batch-lipsync` |
| Une vidéo personnalisée par prospect ou client | `batch-lipsync` |
| Un enregistrement personnalisé avec le nom de chaque destinataire, dans la même voix | [edit-dialogue](edit-dialogue.md) |
| Plusieurs vidéos dans d'autres langues | [localize-campaign](localize-campaign.md) |
| Une seule vidéo | [lipsync](lipsync.md) |

## Essayez

- « Synchronise chaque ligne de leads.csv sur presenter.mp4 »
- « Fais une version de cette pub pour chacune de ces 12 voix off »
- « Passe manifest.csv dans sync, le total est validé »

## Ce dont vous avez besoin

- Le serveur MCP de sync. connecté, ou `SYNC_API_KEY` et Python 3.9 ou version ultérieure pour le script. Le skill [setup](setup.md) vous guide dans les deux cas.
- Une liste dont chaque ligne contient une vidéo ou une image, et un audio ou un script avec une voix.

## Questions fréquentes

**Pourquoi veut-il faire un pilote ?**
Si une entrée commune est erronée, comme la voix ou le cadrage du présentateur, un pilote coûte deux générations au lieu de deux cents.

**Qu'est-ce qui quitte ma machine ?**
Les médias, les scripts, les noms de fichiers et les ID de ligne (utilisés comme noms des résultats). Les colonnes que le traitement n'utilise pas restent en local : évitez donc les noms et les adresses e-mail dans les ID de ligne.

**Il s'est arrêté à mi-parcours.**
Relancez la même commande. Les lignes terminées sont ignorées, les lignes soumises sont interrogées au lieu d'être renvoyées, et rien de ce qui a déjà été payé ne l'est une seconde fois.

**J'ai modifié une ligne après son traitement.**
Le script refuse de réutiliser le résultat de cette ligne. Donnez un nouvel ID à la ligne modifiée, ce qui en fait une nouvelle génération.

**Lance-t-il les lignes une par une ?**
Non. Vous validez l'ensemble du traitement une seule fois, puis les lignes démarrent ensemble, autant à la fois que votre forfait en traite. Via le serveur MCP, cela représente un appel à `jobs_create-many` par tranche de 50 lignes, avec n'importe quel forfait payant, et les lignes qui doivent attendre une place libre démarrent dès que les précédentes se terminent.

**Dois-je utiliser la Batch API ?**
Uniquement avec l'approbation de l'organisation et un forfait Scale ou supérieur, pour un gros traitement de 20 à 500 lignes courtes, chacune jusqu'à 30 secondes, quand un délai de plusieurs heures vous convient. Le test à blanc nécessite le même accès. Sans approbation, la création renvoie `403 batch_access_not_enabled` avant le contrôle du forfait. Contactez support@sync.so pour demander l'approbation. Après approbation, un forfait inférieur à Scale renvoie `402 plan_feature_unavailable`. Utilisez le traitement classique tant que l'accès manque. `jobs_create-many` reste disponible avec tout forfait payant, dans la limite de sa concurrence. Les travaux existants, leurs statuts et leurs résultats restent disponibles.

**Certaines lignes ont échoué.**
Le tableau des résultats liste chaque échec avec sa cause. Les lignes qui ont échoué à cause d'une entrée incorrecte nécessitent une entrée corrigée. Relancez les autres avec `--retry-failed`.

## Tout fonctionne si

- L'estimation couvre toutes les lignes, ou indique celles qu'elle n'a pas pu chiffrer.
- Après une seule validation, les lignes démarrent ensemble plutôt qu'une par une.
- Jamais plus de générations ne tournent simultanément que ce que votre forfait autorise.
- Relancer un manifeste terminé ne crée rien de nouveau.
