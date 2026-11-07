---
title: "localize-campaign-Skill"
subtitle: "Lokalisiere eine Reihe von Videos für mehrere Märkte: Plan, Pilot, Durchlauf, Review-Tabelle."
description: "Der localize-campaign-Skill von sync. labs erstellt jedes Video einer Kampagne, eines Kurses oder einer Produktreihe in jeder Zielsprache: Er ordnet Märkte Sprachen zu, schätzt die Kosten der Matrix, testet eine Version im Pilotlauf und führt dann den Rest mit einer Review-Tabelle aus."
og:description: "Lokalisiere aus deinem Agenten mehrere Videos in mehrere Sprachen, mit einem Pilotlauf zuerst und einer Review-Tabelle am Ende."
source-sha256: 1da869421315f34ece2a880344bb9e5a1a6f20f02c65f76e84caa179ba54edb7
---

# localize-campaign

> [!TIP]
> Installiere diesen Skill mit `npx skills add synchronicity-labs/skills --skill localize-campaign` oder hol dir alle Skills mit dem Claude Code-Plugin. Siehe [Agent Skills](overview.md).

## Was er macht

`localize-campaign` nimmt eine Reihe von Videos, etwa die Anzeigen einer Kampagne, einen Kurs oder Produktvideos, und erstellt jedes davon in jeder Zielsprache. Er ordnet deine Märkte Sprachen zu, legt die Matrix aus Videos und Sprachen an, schätzt die Gesamtkosten, testet eine Version im Pilotlauf, damit Namen und Begriffe früh geprüft werden, und führt dann den Rest aus. Du bekommst einheitlich benannte Dateien und eine `review.csv`, mit der regionale Teams freigeben können.

## Wann du ihn nutzt

| Was du hast | Nimm |
| --- | --- |
| Mehrere Videos, mehrere Märkte oder Sprachen | `localize-campaign` |
| Ein Video in wenige Sprachen | [translate-and-dub](translate-and-dub.md) |
| Viele Videos mit neuer Sprache in derselben Sprache | [batch-lipsync](batch-lipsync.md) |

## Probier es aus

- „Wir starten nächsten Monat in DACH, Brasilien und Japan. Lokalisiere diese drei Anzeigen.“
- „Mach unsere fünf Onboarding-Videos auf Spanisch, Französisch und Italienisch“

## Was du brauchst

- Den verbundenen sync. MCP-Server oder eine gesetzte `SYNC_API_KEY`. Der [setup](setup.md)-Skill führt dich durch beides.
- Die Quellvideos, jeweils mit ihrer Originalsprache.

## Häufige Fragen

**Ich habe Märkte angegeben, keine Sprachen.**
Das ist so vorgesehen. Der Agent ordnet sie zu (DACH zu Deutsch, Brasilien zu Portugiesisch, Japan zu Japanisch) und bittet dich um Bestätigung, bevor er die Kosten schätzt.

**Warum zuerst ein Pilotlauf?**
Ein falsch übersetzter Produktname oder Slogan würde sich sonst in jeder Version wiederholen. Eine Version, geprüft von dir oder einer Person mit der Zielsprache als Muttersprache, fängt das zum Preis einer einzigen Synchronisation ab.

**Was ändert sich nicht?**
Text im Bild, eingebrannte Untertitel, Logos und Abspanntafeln bleiben in der Ausgangssprache. Der Agent sagt dir das vorab, damit niemand im Review überrascht wird.

**Wie heißen die Dateien?**
Standardmäßig `<campaign>_<video>_<lang>.mp4`, zum Beispiel `spring24_hero-30s_de.mp4`. Wenn du ein anderes Muster brauchst, lege es vor dem Durchlauf fest.

**Kann alles in einem Batch laufen?**
Das ist nicht nötig. Nach dem Pilotlauf starten die übrigen Versionen zusammen, bis zum Limit deines Tarifs, mit einem einzigen Aufruf von `jobs_create-many` über den MCP-Server, in jedem kostenpflichtigen Tarif. Ab dem Scale-Tarif kann ein großer Lauf mit 20 oder mehr kurzen Versionen, der Stunden warten kann, auch über die Batch API laufen, eine Warteschlange, deren Ergebnisse bis zu einem Tag dauern können.

**Der Durchlauf wurde unterbrochen.**
Jede Version hat ihren eigenen gespeicherten Schlüssel und ihre Generierungs-ID, deshalb macht die Fortsetzung dort weiter, wo sie aufgehört hat, ohne doppelt zu zahlen.

## Es funktioniert, wenn

- Du die Zuordnung von Märkten zu Sprachen und die Matrix bestätigst, bevor Kosten entstehen.
- Der Pilotlauf zurückkommt, bevor der Rest startet.
- Du am Ende eine Datei pro Video und Sprache hast, dazu eine Review-Tabelle.
