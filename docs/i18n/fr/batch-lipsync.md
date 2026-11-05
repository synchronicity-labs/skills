---
title: "Skill batch-lipsync"
subtitle: "Synchronisez les lèvres pour chaque ligne d'un CSV ou d'un dossier, avec reprise, dans les limites de votre forfait ou via la Batch API."
description: "Le skill d'agent batch-lipsync de sync. labs synchronise les lèvres de nombreuses vidéos en une fois à partir d'un CSV, d'un tableur, d'un dossier ou d'une liste : il chiffre l'ensemble du traitement, propose un pilote, respecte la concurrence de votre forfait et reprend sans payer deux fois."
og:description: "Synchronisez depuis votre agent les lèvres pour chaque ligne d'un CSV ou d'un dossier, avec reprise, dans les limites de votre forfait ou via la Batch API."
source-sha256: f377f784e898a1d3716f298a9ebe4a645dd10ebef89f2b1ba50334da4e4e4cdb
---

# batch-lipsync

> [!TIP]
> Installez ce skill avec `npx skills add synchronicity-labs/skills --skill batch-lipsync`, ou obtenez tous les skills avec le plugin Claude Code. Voir [Skills d'agent](overview.md).

## Ce qu'il fait

`batch-lipsync` synchronise les lèvres de nombreuses vidéos en une fois : un résultat par ligne d'un CSV, d'un tableur, d'un dossier ou d'une liste comme « ce présentateur avec chacun de ces 40 fichiers audio ». Il crée un manifeste, chiffre l'ensemble du traitement, propose un pilote, puis traite chaque ligne dans les limites de votre forfait et rassemble les résultats dans un tableau.

Avec une clé API, il utilise un script fourni, `sync_batch.py`, qui importe chaque fichier une seule fois, respecte la concurrence de votre forfait, reprend après une interruption et télécharge chaque résultat. Avec les forfaits Scale et supérieurs, 20 lignes ou plus peuvent passer par la [Batch API](https://sync.so/docs/api-reference/guides/batch-processing), avec le script ou directement via les outils batch du serveur MCP.

## Quand l'utiliser

| Ce que vous avez | Utilisez |
| --- | --- |
| De nombreuses lignes de vidéo avec audio ou script | `batch-lipsync` |
| Une vidéo personnalisée par prospect ou client | `batch-lipsync` |
| Un enregistrement personnalisé avec le nom de chaque destinataire, dans la même voix | Aperçus [edit-dialogue](edit-dialogue.md), puis `batch-lipsync` |
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

**Dois-je utiliser la Batch API ?**
Avec Scale et supérieurs, pour 20 à 500 lignes courtes quand un délai de traitement allant jusqu'à 24 heures vous convient. Avec les autres forfaits payants, un batch ne peut contenir qu'autant de lignes que le forfait en traite simultanément : le traitement classique est donc tout aussi rapide.

**Certaines lignes ont échoué.**
Le tableau des résultats liste chaque échec avec sa cause. Les lignes qui ont échoué à cause d'une entrée incorrecte nécessitent une entrée corrigée. Relancez les autres avec `--retry-failed`.

## Tout fonctionne si

- L'estimation couvre toutes les lignes, ou indique celles qu'elle n'a pas pu chiffrer.
- Jamais plus de générations ne tournent simultanément que ce que votre forfait autorise.
- Relancer un manifeste terminé ne crée rien de nouveau.
