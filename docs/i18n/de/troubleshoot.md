---
title: "troubleshoot-Skill"
subtitle: "Finde heraus, warum ein Auftrag fehlgeschlagen ist, hängt oder abgelehnt wurde, und setz ihn fort, ohne doppelt zu zahlen."
description: "Der troubleshoot-Skill von sync. labs findet heraus, warum ein sync.-Auftrag fehlgeschlagen ist, hängt oder abgelehnt wurde, erklärt die eigentliche Ursache in einfachen Worten, setzt die Arbeit fort, ohne einen zweiten kostenpflichtigen Auftrag zu starten, und kann das Problem an sync. melden."
og:description: "Finde aus deinem Agenten heraus, warum ein sync.-Auftrag fehlgeschlagen ist, hängt oder abgelehnt wurde, und setz ihn fort, ohne doppelt zu zahlen."
source-sha256: 8de9f50b08fda9e8256cefecc063b3e44871e28eb125c0e2060560fcdabb8fff
---

# troubleshoot

> [!TIP]
> Installiere diesen Skill mit `npx skills add synchronicity-labs/skills --skill troubleshoot` oder hol dir alle Skills mit dem Claude Code-Plugin. Siehe [Agent Skills](overview.md).

## Was er macht

`troubleshoot` findet heraus, warum ein sync.-Auftrag fehlgeschlagen ist, hängt oder abgelehnt wurde, erklärt dir die eigentliche Ursache in einfachen Worten und setzt die Arbeit fort, ohne einen zweiten kostenpflichtigen Auftrag zu starten. Wenn das Problem eine unklare Fehlermeldung oder eine fehlende Funktion war, kann er außerdem einen kurzen Bericht an das sync.-Team schicken, ohne Geheimnisse oder Medien anzuhängen.

## Wann du ihn nutzt

| Was passiert ist | Nimm |
| --- | --- |
| Ein Auftrag ist fehlgeschlagen, wurde abgelehnt oder scheint zu hängen | `troubleshoot` |
| Ein 402, 429 oder ein anderer sync.-Fehler | `troubleshoot` |
| Die sync.-Tools sind verschwunden oder melden, dass du abgemeldet bist | `troubleshoot`, der dich auf dieselbe Weise wieder verbindet wie [setup](setup.md) |
| Du hast sync. noch nicht verbunden | [setup](setup.md) |
| Dein eigener Code bekommt Fehler von der API | [sync-api](sync-api.md) |

## Probier es aus

- „Mein Lipsync ist fehlgeschlagen, warum?“
- „Diese Synchronisation wird seit 20 Minuten verarbeitet“
- „Ich bekomme ständig concurrency_limit_reached“
- „Das Video ist fertig, aber der Mund sieht falsch aus“

## Was du brauchst

- Den verbundenen sync. MCP-Server, um den Auftragsstatus und dein Konto zu lesen. Ohne ihn kann der Skill trotzdem eine Fehlermeldung erklären, die du einfügst.
- Den Fehlertext oder, falls vorhanden, die ID der Generierung oder des Batches.

## Häufige Fragen

**Wurde mir der fehlgeschlagene Auftrag berechnet?**
Nein. Fehlgeschlagene Generierungen werden nicht berechnet.

**Er wird noch verarbeitet. Soll ich ihn neu starten?**
Nein. Ausstehend heißt nicht fehlgeschlagen, und ein zweiter Auftrag wird nicht früher fertig. Der Skill prüft weiter denselben Auftrag.

**Meine Anfrage ist in ein Timeout gelaufen. Ist sie durchgegangen?**
Vielleicht. Der Skill sucht nach dem Auftrag oder wiederholt die identische Anfrage mit demselben Schlüssel, was das Original zurückgibt, statt einen weiteren zu starten.

**Das Ergebnis sieht falsch aus.**
Die üblichen Ursachen liegen im Ausgangsmaterial: ein abgewandtes oder verdecktes Gesicht, mehrere Personen im Bild, Musik unter der Stimme oder eine niedrige Auflösung. Der Skill prüft diese Punkte und schlägt `sync-3` vor, wenn ein älteres Modell verwendet wurde. Ein neuer Versuch ist eine neue kostenpflichtige Generierung, deshalb nennt er zuerst die Kosten.

**Was enthält der Bericht an sync.?**
Die Art des Problems, den genauen Fehler, das Tool und die Auftrags-ID. Niemals deinen Schlüssel, signierte Links, persönliche Daten oder Medien.

## Es funktioniert, wenn

- Du die eigentliche Ursache bekommst, mit dem Fehlercode, wenn es einen gibt.
- Kein zweiter kostenpflichtiger Auftrag startet, solange du keinem neuen Versuch zustimmst.
- Die ursprüngliche Arbeit dort weitermacht, wo sie aufgehört hat.
