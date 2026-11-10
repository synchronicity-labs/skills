---
title: "edit-dialogue-Skill"
subtitle: "Ändere oder entferne einzelne gesprochene Wörter in der eigenen Stimme der sprechenden Person."
description: "Der edit-dialogue-Skill von sync. labs korrigiert einzelne gesprochene Wörter in einem Video mit einer sprechenden Person ohne Nachdreh: Er transkribiert, spielt dir die neuen Wörter als Vorschau in der eigenen Stimme der Person vor und passt dann nur an dieser Stelle die Lippen neu an."
og:description: "Korrigiere einen falschen Preis, Namen, ein Datum oder ein Wort in einem Video, in der eigenen Stimme der sprechenden Person, ohne Nachdreh."
source-sha256: e600a9398994cc8954d04bcfe97d32f8830b99c91552aa7b7db8ccc11762a46e
---

# edit-dialogue

> [!TIP]
> Installiere diesen Skill mit `npx skills add synchronicity-labs/skills --skill edit-dialogue` oder hol dir alle Skills mit dem Claude Code-Plugin. Siehe [Agent Skills](overview.md).

## Was er macht

`edit-dialogue` korrigiert einzelne gesprochene Wörter in einem Video ohne Nachdreh. Er transkribiert das Video, ordnet deine Korrektur den genauen Wörtern zu, erzeugt die neuen Wörter in der eigenen Stimme der sprechenden Person, lässt dich eine Vorschau anhören und passt dann nur an dieser Stelle die Lippen neu an. Alles andere behält Originalbild und Originalton.

## Wann du ihn nutzt

| Was du hast | Nimm |
| --- | --- |
| Einen falschen Preis, Namen, ein falsches Datum oder Wort oder ein Füllwort, das raus soll | `edit-dialogue` |
| Ein komplett neues Skript | [lipsync](lipsync.md) mit einer ausgewählten Stimme |
| Dasselbe Video in einer anderen Sprache | [translate-and-dub](translate-and-dub.md) |
| Eine Aufnahme, personalisiert für jeden Empfänger | `edit-dialogue`, eine Vorschau und ein Video pro Empfänger |

## Probier es aus

- „In ./promo.mp4 sage ich 39 $ pro Monat. Jetzt sind es 49 $, korrigiere nur das.“
- „Schneide das ‚äh‘ nach ‚jährlich abgerechnet‘ in diesem Video raus“
- „Der Name sollte Siobhan sein, nicht Shannon“

## Was du brauchst

- Den verbundenen sync. MCP-Server. Der [setup](setup.md)-Skill führt dich durch die Einrichtung. Die REST-Version dieses Workflows ist im Early Access; siehe [Transcription and Dialogue Editing](https://sync.so/docs/developer-guides/dialogue-editing).
- Ein Video mit einer sprechenden Person, bis zu 10 Minuten lang.

## Häufige Fragen

**Warum zeigt er mir das Transkript?**
Damit ihr beide auf dieselben Wörter zeigen könnt. Jede Änderung und jede Entfernung ist an ein Wort im Transkript gebunden, so bleibt die Bearbeitung exakt.

**Kostet die Vorschau Geld?**
Das kann sein. Die Vorschau klont die Stimme der sprechenden Person und erzeugt die neuen Wörter, deshalb erwähnt der Agent das, wenn er die Änderungen bestätigt. Für das fertige Video gibt es eine separate Kostenschätzung, bevor es erstellt wird.

**Ein Name klingt falsch.**
Bitte um eine Aussprache. Der Agent fügt eine Lautschreibung wie „shivawn“ hinzu, geschrieben als normales Wort, und erstellt eine neue Vorschau.

**Einige Änderungen sind fehlgeschlagen.**
Meist ist die neue Formulierung zu lang für die Lücke, die sie füllt. Der Agent sagt, welche Änderungen fehlgeschlagen sind, und schlägt kürzere Formulierungen vor.

**Kann er eine Version pro Empfänger erstellen?**
Ja. Du legst die Änderungen für jeden Empfänger in einer Tabelle fest, die Vorschauen starten zusammen, und nach einer einzigen Freigabe der Gesamtsumme starten auch die Videos zusammen, bis zum Limit deines Tarifs. Über den MCP-Server ist das ein Aufruf von `jobs_create-many` für die Vorschauen und einer für die Videos, in jedem kostenpflichtigen Tarif. Wartende Renderaufträge über die Batch API brauchen die ausdrückliche Freigabe der Organisation und den Scale-Tarif oder höher, auch für Probeläufe. Der Zugriff ist standardmäßig deaktiviert. Wende dich an support@sync.so, um die Freigabe zu beantragen. Nutzer und Organisationsadministratoren können ihn nicht selbst aktivieren. Zeilen zur Dialogbearbeitung brauchen zusätzlich eine eigene Early-Access-Freigabe.

**Kann ich einen ganzen Absatz ersetzen?**
Dieser Workflow ist für gezielte Wörter gedacht. Für ein neues Skript ist lipsync mit einer Stimme das bessere Werkzeug, und der Agent sagt dir das auch.

## Es funktioniert, wenn

- Im Vorschau-Audio nur deine Wörter geändert sind.
- Du Vorschau und Kosten freigibst, bevor das Video erstellt wird.
- Das Ergebnis das Originalvideo abspielt, in dem nur diese Wörter anders sind.
