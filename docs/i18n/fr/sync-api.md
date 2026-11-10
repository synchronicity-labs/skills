---
title: "Skill sync-api"
subtitle: "Intégrez sync. dans vos applications avec l'API REST ou les SDK Python et TypeScript."
description: "Le skill d'agent sync-api de sync. labs aide votre agent de code à intégrer sync. dans une application, un backend, un script ou un pipeline : imports, générations avec clés d'idempotence, webhooks vérifiés, polling, erreurs et limites de concurrence."
og:description: "Faites écrire à votre agent de code des intégrations sync. côté serveur avec clés d'idempotence, webhooks vérifiés et gestion correcte des erreurs 429."
source-sha256: 1b2d510001c97cc2617187e1c85cdcf498c6d4b091c3c10d9d2b1d7dee9e4193
---

# sync-api

> [!TIP]
> Installez ce skill avec `npx skills add synchronicity-labs/skills --skill sync-api`, ou obtenez tous les skills avec le plugin Claude Code. Voir [Skills d'agent](overview.md).

## Ce qu'il fait

`sync-api` aide votre agent de code à intégrer sync. dans votre propre application, backend, script ou pipeline. Il écrit du code côté serveur qui importe des médias, crée des générations avec des clés d'idempotence, vérifie les webhooks, interroge l'API en solution de secours, et gère les erreurs et les limites de concurrence, via l'API REST ou les [SDK](https://sync.so/docs/developer-guides/sdk) officiels Python (`syncsdk`) et TypeScript (`@sync.so/sdk`).

## Quand l'utiliser

| Ce que vous faites | Utilisez |
| --- | --- |
| Écrire ou relire du code qui appelle l'API sync. | `sync-api` |
| Déboguer une erreur 429, un webhook ou une facturation en double | `sync-api` |
| Créer une vidéo dans ce chat | [lipsync](lipsync.md), [talking-photo](talking-photo.md), [translate-and-dub](translate-and-dub.md) |
| Traiter une seule fois un CSV de travaux | [batch-lipsync](batch-lipsync.md) |

## Essayez

- « Ajoute à mon app Express un endpoint qui synchronise les lèvres d'une URL vidéo sur une URL audio avec sync. »
- « Écris un script Python qui double en espagnol chaque vidéo de ./in »
- « Ajoute une route Next.js qui vérifie les webhooks sync. »
- « Notre worker reçoit sans arrêt 429 concurrency_limit_reached. Quelle est la bonne solution ? »

## Ce dont vous avez besoin

- Une clé API sync. obtenue sur [sync.so/settings/api-keys](https://sync.so/settings/api-keys), définie dans `SYNC_API_KEY` sur le serveur. Voir [Authentification](https://sync.so/docs/api-reference/guides/authentication).
- Python 3.8 ou version ultérieure, ou Node 18 ou version ultérieure, pour les SDK.

## Questions fréquentes

**Pourquoi le code enregistre-t-il une clé avant d'appeler l'API ?**
`POST /v2/generate` accepte un `Idempotency-Key`. Créé une fois par travail et réutilisé à chaque nouvelle tentative, il transforme une nouvelle tentative après un timeout en rejeu de la génération d'origine au lieu d'une deuxième génération payante. Voir [Idempotent Requests](https://sync.so/docs/api-reference/guides/idempotency).

**Webhooks ou polling ?**
Les [webhooks](https://sync.so/docs/api-reference/guides/webhooks), vérifiés avec l'en-tête `Sync-Signature`, pour la production. Une interrogation périodique rattrape les livraisons manquées par votre endpoint.

**Le SDK n'a pas un champ mentionné dans la documentation.**
Les SDK peuvent être en retard sur l'API. Le skill appelle alors cet endpoint en HTTP au lieu de forcer les types.

**Que faire face à une erreur 429 ?**
Attendez le délai indiqué dans la réponse, réessayez avec la même clé d'idempotence et ne gardez pas plus de travaux en cours que la limite de concurrence de votre forfait, avec une file d'attente de votre côté. Voir [Concurrence et limites de débit](https://sync.so/docs/api-reference/guides/rate-limits).

**Qui peut créer un batch en file d'attente ?**
La Batch API nécessite l'approbation explicite de l'organisation et un forfait Scale ou supérieur, y compris pour les tests à blanc. L'accès est désactivé par défaut. Sans approbation, la création renvoie `403 batch_access_not_enabled` avant le contrôle du forfait. Contactez support@sync.so pour demander l'approbation. Les utilisateurs et les administrateurs de l'organisation ne peuvent pas activer l'accès. Après approbation, un forfait inférieur à Scale renvoie `402 plan_feature_unavailable`. Les travaux existants, les statuts des batches et leurs résultats restent disponibles. Les requêtes classiques dans la limite du forfait et `jobs_create-many` du MCP restent disponibles avec tout forfait payant.

## Tout fonctionne si

- La clé API reste sur le serveur, jamais dans du code navigateur ou mobile.
- Chaque création porte une clé d'idempotence enregistrée avant l'appel.
- Le gestionnaire de webhooks vérifie la signature sur le corps brut avant de l'analyser.
