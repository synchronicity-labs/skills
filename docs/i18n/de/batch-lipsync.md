---
title: "batch-lipsync-Skill"
subtitle: "Mach jede Zeile einer CSV-Datei oder eines Ordners lippensynchron, fortsetzbar, innerhalb der Limits deines Tarifs oder, im Scale-Tarif, über die Batch API."
description: "Der batch-lipsync-Skill von sync. labs macht viele Videos auf einmal lippensynchron, aus einer CSV-Datei, einer Tabelle, einem Ordner oder einer Liste: Er schätzt die Kosten des gesamten Laufs, bietet einen Pilotlauf an, hält sich an die gleichzeitigen Aufträge deines Tarifs und setzt fort, ohne doppelt zu zahlen."
og:description: "Mach aus deinem Agenten jede Zeile einer CSV-Datei oder eines Ordners lippensynchron, fortsetzbar, innerhalb der Limits deines Tarifs oder, im Scale-Tarif, über die Batch API."
source-sha256: dce75e3282ede2eced47c63275e8fa42accbe43a3e500b1e433052a4990cd187
---

# batch-lipsync

> [!TIP]
> Installiere diesen Skill mit `npx skills add synchronicity-labs/skills --skill batch-lipsync` oder hol dir alle Skills mit dem Claude Code-Plugin. Siehe [Agent Skills](overview.md).

## Was er macht

`batch-lipsync` macht viele Videos auf einmal lippensynchron: ein Ergebnis pro Zeile einer CSV-Datei, einer Tabelle, eines Ordners oder einer Liste wie „dieser Moderator mit jeder dieser 40 Audiodateien“. Er erstellt ein Manifest, schätzt die Kosten des gesamten Laufs, bietet einen Pilotlauf an, verarbeitet dann jede Zeile innerhalb der Limits deines Tarifs und sammelt die Ergebnisse in einer Ergebnistabelle.

Mit einem API-Schlüssel nutzt er ein mitgeliefertes Skript, `sync_batch.py`, das jede Datei einmal hochlädt, die gleichzeitigen Aufträge deines Tarifs einhält, nach einer Unterbrechung fortsetzt und jedes Ergebnis herunterlädt. Über den sync. MCP-Server startet er alle Zeilen mit einem einzigen Aufruf von `jobs_create-many`, der die gleichzeitigen Aufträge deines Tarifs einhält, und verfolgt sie alle mit `jobs_get-many`. Wo diese Tools nicht angeboten werden, startet er stattdessen eine Generierung pro Zeile.

Ab dem Scale-Tarif kann ein großer Lauf mit 20 bis 500 kurzen Zeilen, der Stunden warten kann, stattdessen über die [Batch API](https://sync.so/docs/api-reference/guides/batch-processing) laufen, entweder mit dem Skript oder über die Batch-Tools des MCP-Servers.

## Wann du ihn nutzt

| Was du hast | Nimm |
| --- | --- |
| Viele Zeilen mit Video plus Audio oder Skript | `batch-lipsync` |
| Ein personalisiertes Video pro Lead oder Kunde | `batch-lipsync` |
| Eine Aufnahme, personalisiert mit dem Namen jedes Empfängers in derselben Stimme | [edit-dialogue](edit-dialogue.md) |
| Mehrere Videos in andere Sprachen | [localize-campaign](localize-campaign.md) |
| Ein einzelnes Video | [lipsync](lipsync.md) |

## Probier es aus

- „Mach jede Zeile aus leads.csv auf presenter.mp4 lippensynchron“
- „Erstelle eine Version dieser Anzeige für jedes dieser 12 Voiceovers“
- „Lass manifest.csv durch sync laufen, die Summe ist freigegeben“

## Was du brauchst

- Den verbundenen sync. MCP-Server oder `SYNC_API_KEY` und Python 3.9 oder neuer für das Skript. Der [setup](setup.md)-Skill führt dich durch beides.
- Eine Liste, in der jede Zeile ein Video oder Bild und Audio oder ein Skript mit Stimme hat.

## Häufige Fragen

**Warum will er einen Pilotlauf?**
Wenn eine gemeinsame Eingabe falsch ist, etwa die Stimme oder der Bildausschnitt des Moderators, kostet ein Pilotlauf zwei Generierungen statt zweihundert.

**Was verlässt meinen Rechner?**
Die Medien, die Skripte, Dateinamen und die Zeilen-IDs (als Namen der Ergebnisse). Spalten, die der Lauf nicht nutzt, bleiben lokal, also halte Namen und E-Mail-Adressen aus den Zeilen-IDs heraus.

**Er hat mittendrin aufgehört.**
Führe denselben Befehl erneut aus. Fertige Zeilen werden übersprungen, übermittelte Zeilen werden abgefragt statt neu übermittelt, und nichts, was schon bezahlt ist, wird noch einmal bezahlt.

**Ich habe eine Zeile geändert, nachdem sie gelaufen ist.**
Das Skript weigert sich, das Ergebnis dieser Zeile wiederzuverwenden. Gib der geänderten Zeile eine neue ID, damit wird sie zu einer neuen Generierung.

**Startet er die Zeilen eine nach der anderen?**
Nein. Du gibst den gesamten Lauf einmal frei, dann starten die Zeilen zusammen, so viele gleichzeitig, wie dein Tarif verarbeitet. Über den MCP-Server ist das ein Aufruf von `jobs_create-many` pro 50 Zeilen, in jedem kostenpflichtigen Tarif, und Zeilen, die auf einen freien Platz warten müssen, starten, sobald frühere fertig sind.

**Sollte ich die Batch API nutzen?**
Nur ab dem Scale-Tarif, für einen großen Lauf mit 20 bis 500 kurzen Zeilen (jede bis zu 30 Sekunden), wenn eine Bearbeitungszeit von Stunden in Ordnung ist. Ein Batch ist eine Warteschlange zur Verarbeitung, kein schnellerer Weg, ein paar Generierungen zu senden: Der normale Lauf startet jede Zeile sofort, bis zum Limit deines Tarifs. Unterhalb von Scale ist die Batch API nicht verfügbar.

**Einige Zeilen sind fehlgeschlagen.**
Die Ergebnistabelle listet jeden Fehler mit Grund auf. Zeilen, die an fehlerhaften Eingaben gescheitert sind, brauchen eine korrigierte Eingabe. Wiederhole den Rest mit `--retry-failed`.

## Es funktioniert, wenn

- Die Kostenschätzung jede Zeile abdeckt oder dir sagt, für welche Zeilen kein Preis ermittelt werden konnte.
- Die Zeilen nach einer einzigen Freigabe zusammen starten statt einzeln.
- Nie mehr Generierungen gleichzeitig laufen, als dein Tarif erlaubt.
- Ein erneuter Lauf über ein fertiges Manifest nichts Neues erstellt.
