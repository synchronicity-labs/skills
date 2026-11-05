---
title: "ai-video-to-talking-Skill"
subtitle: "Gib KI-generierten Clips aus Veo, Kling, Sora und anderen Dialog."
description: "Der ai-video-to-talking-Skill von sync. labs gibt KI-generierten Videos aus Veo, Kling, Sora, Runway und anderen Generatoren Dialog, wählt eine passende Stimme und macht die Figur lippensynchron, auch in Szenen mit mehreren Einstellungen."
og:description: "Lass Figuren in KI-generierten Videos deine Sätze sprechen, auch in Szenen mit mehreren Einstellungen und zwei Figuren."
source-sha256: 2da61aa54d453eba92f1fa339fa9da3fa171c87d410601398b6427170f09c5bd
---

# ai-video-to-talking

> [!TIP]
> Installiere diesen Skill mit `npx skills add synchronicity-labs/skills --skill ai-video-to-talking` oder hol dir alle Skills mit dem Claude Code-Plugin. Siehe [Agent Skills](overview.md).

## Was er macht

`ai-video-to-talking` gibt KI-generierten Videos Dialog. Clips aus Veo, Kling, Sora, Runway, Hailuo, Luma, Seedance oder Wan kommen meist stumm zurück oder mit Sprache, die du nicht willst. Dieser Skill schreibt den Satz oder übernimmt deinen, wählt eine Stimme, die zur Figur passt, und macht sie lippensynchron, damit sie wirklich spricht.

sync. erzeugt das Video nicht. Wenn du nur eine Idee hast, schreibt der Skill einen Prompt für deinen Videogenerator, der einen gut lippensynchronisierbaren Clip liefert, und übernimmt, sobald du ihn hast.

## Wann du ihn nutzt

| Was du hast | Nimm |
| --- | --- |
| Einen generierten Clip oder eine Idee dafür | `ai-video-to-talking` |
| Echte Aufnahmen und ein Voiceover | [lipsync](lipsync.md) |
| Ein Standbild | [talking-photo](talking-photo.md) |

## Probier es aus

- „Mein Veo-Clip mit einer Barista hat keinen Dialog. Lass sie sagen: Morgen, wieder ein Hafer-Latte?“
- „Ich brauche eine Anzeige im UGC-Stil, in der ein Typ unseren Energydrink hält und sagt, dass er gut schmeckt. Den Clip mache ich in Kling.“
- „In dieser Sora-Szene reden zwei Figuren. Gib ihnen diese Sätze.“

## Was du brauchst

- Den verbundenen sync. MCP-Server oder eine gesetzte `SYNC_API_KEY`. Der [setup](setup.md)-Skill führt dich durch beides.
- Den Clip oder Zugang zu einem Videogenerator.
- Den Satz oder eine Beschreibung dessen, was die Figur sagen soll.

## Häufige Fragen

**Was macht einen generierten Clip gut lippensynchronisierbar?**
Eine einzelne Figur mit Blick in die Kamera, ein Gesicht, das einen guten Teil des Bildes füllt, ein freier Mund, eine ruhige Kamera, eine durchgehende Einstellung und eine Figur, die sich schon so bewegt, als würde sie sprechen. Der Prompt-Leitfaden des Skills erklärt das, mit einem Beispiel-Prompt.

**Mein Satz ist länger als der Clip.**
Generierte Clips sind oft 5 bis 10 Sekunden lang, was etwa 12 bis 25 Wörtern entspricht. Der Skill schlägt vor, den Satz zu kürzen, einen längeren Clip zu generieren oder einen [Sync-Modus](https://sync.so/docs/developer-guides/sync-mode) zu nutzen, der das Video verlängert.

**Kann er zwei Figuren oder mehrere Einstellungen?**
Ja, mit dem Timeline-Tool. Jeder Satz bekommt seine eigene Stimme und wird auf die Einstellung gelegt, in der diese Figur spricht. Sätze, Stimmen und Gesamtkosten werden abgestimmt, bevor etwas erstellt wird.

**Kann ich meine eigene Stimme verwenden?**
Ja, nimm sie auf und übergib das Audio. Der Skill kann auch eine Stimme klonen, aber nur, wenn du darum bittest und dir die Aufnahme gehört. Beim Klonen wird eine Stimme einmal in deinem Konto gespeichert; geht die Antwort verloren, prüft der Skill deine Stimmenliste, bevor er es erneut versucht.

## Es funktioniert, wenn

- Die Figur genau deine Worte spricht, mit einer Stimme, die zu ihr passt.
- Nichts generiert wird, bevor du Satz, Stimme und Kosten freigegeben hast.
- In einer Szene mit mehreren Einstellungen jeder Satz bei der richtigen Figur landet.
