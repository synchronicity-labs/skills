---
title: "translate-and-dub-Skill"
subtitle: "Synchronisiere ein Video in andere Sprachen, mit passenden Lippenbewegungen."
description: "Der translate-and-dub-Skill von sync. labs übersetzt die Sprache in einem Video in andere Sprachen und passt die Lippen der sprechenden Person neu an, aus einer lokalen Datei, einer URL oder einem Link zu YouTube, TikTok, Instagram oder Facebook."
og:description: "Synchronisiere aus deinem Agenten ein Video in andere Sprachen, mit passenden Lippenbewegungen und vorab einer Kostenschätzung pro Sprache."
source-sha256: 7f634da776bfe7c98f91c58950211d376361728413314e96ff125972692270bb
---

# translate-and-dub

> [!TIP]
> Installiere diesen Skill mit `npx skills add synchronicity-labs/skills --skill translate-and-dub` oder hol dir alle Skills mit dem Claude Code-Plugin. Siehe [Agent Skills](overview.md).

## Was er macht

`translate-and-dub` übersetzt die Sprache in einem Video in andere Sprachen und passt die Lippen der sprechenden Person an das synchronisierte Audio an. Du bekommst eine MP4-Datei pro Sprache, jeweils mit der Sprache beschriftet. Das funktioniert mit einer lokalen Datei, einer öffentlichen URL oder einem Link zu YouTube, TikTok, Instagram oder Facebook.

## Wann du ihn nutzt

| Was du hast | Nimm |
| --- | --- |
| Ein Video, eine oder mehrere Sprachen | `translate-and-dub` |
| Mehrere Videos für mehrere Märkte | [localize-campaign](localize-campaign.md) |
| Ein Video und dein eigenes übersetztes Audio | [lipsync](lipsync.md) |
| Nur Untertitel | Keine Aufgabe für sync. |

## Probier es aus

- „Synchronisiere dieses YouTube-Video auf Spanisch und brasilianisches Portugiesisch“
- „Übersetze ./keynote.mp4 ins Japanische“
- „Mach von https://example.com/demo.mp4 eine deutsche Version“

## Was du brauchst

- Den verbundenen sync. MCP-Server oder eine gesetzte `SYNC_API_KEY`. Der [setup](setup.md)-Skill führt dich durch beides.
- Ein Video mit der Originalsprache auf der Tonspur.

## Häufige Fragen

**Welche Sprachen werden unterstützt?**
Der Agent prüft die aktuelle Liste, bevor er die Kosten schätzt. Fehlt eine Sprache, nennt er die nächstliegende verfügbare.

**Wie wird der Preis berechnet?**
Nach der Länge des Quellvideos, einmal pro Sprache. Die Kostenschätzung zeigt die Aufschlüsselung pro Sprache und die Summe. Wenn Gebühren eines externen Stimmanbieters nicht enthalten sind, sagt der Agent das.

**Wird Text im Bild übersetzt?**
Nein. Titel, Untertitel im Bild und Logos bleiben, wie sie sind. Nur die Sprache ändert sich.

**Werden die Sprachen nacheinander synchronisiert?**
Nein. Nach einer einzigen Freigabe starten alle Sprachen zusammen, bis zum Limit deines Tarifs. Über den MCP-Server ist das ein einziger Aufruf von `jobs_create-many`.

**Eine Sprache ist fehlgeschlagen.**
Jede Sprache ist ein eigener Auftrag, die anderen werden also trotzdem fertig. Der Agent meldet, welche fehlgeschlagen ist und warum.

**Die Synchronisation ist mit einem Fehler des Stimmanbieters fehlgeschlagen.**
Wenn du deinen eigenen ElevenLabs-Schlüssel mit sync. verbunden hast, sind meist die Credits oder die Gültigkeit dieses Schlüssels die Ursache.

**Er wollte kein Musikvideo synchronisieren.**
Urheberrechtlich geschützte Songs und Musikvideos brauchen die Erlaubnis der Rechteinhaber. Nutze ein Video, das dir gehört oder für dessen Lokalisierung du eine Lizenz hast.

## Es funktioniert, wenn

- Die Sprachen vor der Kostenschätzung geprüft werden.
- Es pro Sprache einen kostenpflichtigen Auftrag gibt und nie eine erneute Übermittlung, um den Fortschritt zu prüfen.
- Jeder Ergebnislink mit seiner Sprache beschriftet ist.
