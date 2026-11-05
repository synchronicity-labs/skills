---
title: "sync-api-Skill"
subtitle: "Bau sync. mit der REST-API oder den Python- und TypeScript-SDKs in Apps ein."
description: "Der sync-api-Skill von sync. labs hilft deinem Coding-Agenten, sync. in eine App, ein Backend, ein Skript oder eine Pipeline einzubauen: Uploads, Generierungen mit Idempotenzschlüsseln, verifizierte Webhooks, Polling, Fehler und Limits für gleichzeitige Aufträge."
og:description: "Lass deinen Coding-Agenten serverseitige sync.-Integrationen mit Idempotenzschlüsseln, verifizierten Webhooks und korrekter 429-Behandlung schreiben."
source-sha256: 061702b8ed38fec950d9150ef03d9c00dbdc027e8ec001ce4faf5aaeca1fdec9
---

# sync-api

> [!TIP]
> Installiere diesen Skill mit `npx skills add synchronicity-labs/skills --skill sync-api` oder hol dir alle Skills mit dem Claude Code-Plugin. Siehe [Agent Skills](overview.md).

## Was er macht

`sync-api` hilft deinem Coding-Agenten, sync. in deine eigene App, dein Backend, Skript oder deine Pipeline einzubauen. Er schreibt serverseitigen Code, der Medien hochlädt, Generierungen mit Idempotenzschlüsseln erstellt, Webhooks verifiziert, als Fallback Polling nutzt und Fehler sowie Limits für gleichzeitige Aufträge behandelt, mit der REST-API oder den offiziellen [SDKs](https://sync.so/docs/developer-guides/sdk) für Python (`syncsdk`) und TypeScript (`@sync.so/sdk`).

## Wann du ihn nutzt

| Was du gerade machst | Nimm |
| --- | --- |
| Code schreiben oder prüfen, der die sync.-API aufruft | `sync-api` |
| Einen 429-Fehler, einen Webhook oder eine doppelte Abrechnung debuggen | `sync-api` |
| Ein Video in diesem Chat erstellen | [lipsync](lipsync.md), [talking-photo](talking-photo.md), [translate-and-dub](translate-and-dub.md) |
| Eine CSV-Datei mit Aufträgen einmalig verarbeiten | [batch-lipsync](batch-lipsync.md) |

## Probier es aus

- „Füge meiner Express-App einen Endpoint hinzu, der mit sync. eine Video-URL lippensynchron zu einer Audio-URL macht“
- „Schreib ein Python-Skript, das jedes Video in ./in auf Spanisch synchronisiert“
- „Füge eine Next.js-Route hinzu, die sync.-Webhooks verifiziert“
- „Unser Worker bekommt ständig 429 concurrency_limit_reached. Was ist die richtige Lösung?“

## Was du brauchst

- Einen sync.-API-Schlüssel von [sync.so/settings/api-keys](https://sync.so/settings/api-keys), auf dem Server als `SYNC_API_KEY` gesetzt. Siehe [Authentifizierung](https://sync.so/docs/api-reference/guides/authentication).
- Python 3.8 oder neuer oder Node 18 oder neuer für die SDKs.

## Häufige Fragen

**Warum speichert der Code einen Schlüssel, bevor er die API aufruft?**
`POST /v2/generate` akzeptiert einen `Idempotency-Key`. Einmal pro Auftrag erstellt und bei jedem erneuten Versuch wiederverwendet, macht er aus einem erneuten Versuch nach einem Timeout eine Wiedergabe der ursprünglichen Generierung statt einer zweiten kostenpflichtigen. Siehe [Idempotent Requests](https://sync.so/docs/api-reference/guides/idempotency).

**Webhooks oder Polling?**
[Webhooks](https://sync.so/docs/api-reference/guides/webhooks), verifiziert über den Header `Sync-Signature`, für die Produktion. Ein regelmäßiges Polling fängt Zustellungen ab, die dein Endpoint verpasst hat.

**Dem SDK fehlt ein Feld, das in der Dokumentation steht.**
Die SDKs können hinter der API zurückliegen. Der Skill ruft diesen Endpoint dann per HTTP auf, statt die Typen zu erzwingen.

**Was mache ich mit einem 429?**
Warte die Zeit ab, die die Antwort angibt, versuche es mit demselben Idempotenzschlüssel erneut und halte höchstens so viele Aufträge gleichzeitig in Bearbeitung, wie das Limit deines Tarifs erlaubt, mit einer Warteschlange auf deiner Seite. Siehe [Parallelität und Rate Limits](https://sync.so/docs/api-reference/guides/rate-limits).

## Es funktioniert, wenn

- Der API-Schlüssel auf dem Server liegt, nie in Browser- oder Mobile-Code.
- Jede Erstellung einen Idempotenzschlüssel mitführt, der vor dem Aufruf gespeichert wurde.
- Der Webhook-Handler die Signatur gegen den rohen Body prüft, bevor er ihn parst.
