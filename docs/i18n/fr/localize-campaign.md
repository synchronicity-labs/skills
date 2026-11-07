---
title: "Skill localize-campaign"
subtitle: "Localisez un ensemble de vidéos pour plusieurs marchés : plan, pilote, exécution, fiche de relecture."
description: "Le skill d'agent localize-campaign de sync. labs produit chaque vidéo d'une campagne, d'une formation ou d'une gamme de produits dans chaque langue cible : il associe les marchés aux langues, chiffre la matrice, réalise un pilote sur une version, puis traite le reste avec une fiche de relecture."
og:description: "Localisez plusieurs vidéos dans plusieurs langues depuis votre agent, avec un pilote d'abord et une fiche de relecture à la fin."
source-sha256: 1da869421315f34ece2a880344bb9e5a1a6f20f02c65f76e84caa179ba54edb7
---

# localize-campaign

> [!TIP]
> Installez ce skill avec `npx skills add synchronicity-labs/skills --skill localize-campaign`, ou obtenez tous les skills avec le plugin Claude Code. Voir [Skills d'agent](overview.md).

## Ce qu'il fait

`localize-campaign` prend un ensemble de vidéos, comme les publicités d'une campagne, une formation ou des vidéos produit, et produit chacune d'elles dans chaque langue cible. Il associe vos marchés aux langues, organise la matrice vidéos par langues, chiffre l'ensemble, réalise un pilote sur une version pour vérifier tôt les noms et les termes, puis traite le reste. Vous obtenez des fichiers nommés de façon cohérente et un `review.csv` que les équipes régionales peuvent valider.

## Quand l'utiliser

| Ce que vous avez | Utilisez |
| --- | --- |
| Plusieurs vidéos, plusieurs marchés ou langues | `localize-campaign` |
| Une vidéo dans quelques langues | [translate-and-dub](translate-and-dub.md) |
| De nombreuses vidéos avec une nouvelle parole dans la même langue | [batch-lipsync](batch-lipsync.md) |

## Essayez

- « Nous lançons le mois prochain en DACH, au Brésil et au Japon. Localise ces trois pubs. »
- « Décline nos cinq vidéos d'onboarding en espagnol, en français et en italien »

## Ce dont vous avez besoin

- Le serveur MCP de sync. connecté, ou `SYNC_API_KEY` défini. Le skill [setup](setup.md) vous guide dans les deux cas.
- Les vidéos sources, chacune avec sa parole d'origine.

## Questions fréquentes

**Je lui ai donné des marchés, pas des langues.**
C'est normal. L'agent les associe (DACH à l'allemand, le Brésil au portugais, le Japon au japonais) et vous demande de confirmer avant de chiffrer.

**Pourquoi un pilote d'abord ?**
Sinon, un nom de produit ou un slogan mal traduit se répéterait dans toutes les versions. Une seule version, vérifiée par vous ou par un locuteur natif, permet de le repérer pour le prix d'un seul doublage.

**Qu'est-ce qui ne change pas ?**
Le texte à l'écran, les sous-titres incrustés, les logos et les cartons de fin restent dans la langue source. L'agent vous le dit dès le départ pour que personne ne soit surpris lors de la relecture.

**Comment les fichiers sont-ils nommés ?**
`<campaign>_<video>_<lang>.mp4` par défaut, par exemple `spring24_hero-30s_de.mp4`. Convenez d'un autre modèle avant le traitement si besoin.

**Peut-il tout traiter en un seul batch ?**
Ce n'est pas nécessaire. Après le pilote, les autres versions démarrent ensemble, dans la limite de votre forfait, en un seul appel à `jobs_create-many` via le serveur MCP, avec n'importe quel forfait payant. Avec les forfaits Scale et supérieurs, un gros traitement de 20 versions courtes ou plus qui peut attendre plusieurs heures peut aussi passer par la Batch API, une file de traitement dont les résultats peuvent prendre jusqu'à une journée.

**Le traitement a été interrompu.**
Chaque version a sa propre clé enregistrée et son ID de génération : la reprise repart là où elle s'était arrêtée, sans payer deux fois.

## Tout fonctionne si

- Vous confirmez l'association marchés et langues ainsi que la matrice avant tout coût.
- Le pilote revient avant le lancement du reste.
- Vous obtenez un fichier par vidéo et par langue, plus une fiche de relecture.
