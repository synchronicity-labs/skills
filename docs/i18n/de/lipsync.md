---
title: "lipsync-Skill"
subtitle: "Mach ein Video lippensynchron zu neuem Audio oder einem getippten Skript."
description: "Der lipsync-Skill von sync. labs lässt eine Person in einem Video zu neuer Sprache passen: einem Voiceover, einem neu aufgenommenen Take, einem Song oder einem Skript, das sync. vertont. Er nennt zuerst die Kosten und wartet auf deine Freigabe."
og:description: "Mach aus deinem Agenten ein Video einer echten Person lippensynchron zu neuem Audio oder einem getippten Skript, mit einer Kostenschätzung vor jeder Generierung."
source-sha256: 58edce026081002df42de0999296238a3f949e65c29651b4a6a39fe8a9bac0f3
---

# lipsync

> [!TIP]
> Installiere diesen Skill mit `npx skills add synchronicity-labs/skills --skill lipsync` oder hol dir alle Skills mit dem Claude Code-Plugin. Siehe [Agent Skills](overview.md).

## Was er macht

`lipsync` nimmt ein Video, in dem jemand spricht, und passt die Mundbewegungen an neue Sprache an. Das kann ein Voiceover sein, ein neu aufgenommener Take, ein Song oder ein Skript, das sync. für dich vertont. Du bekommst eine einzige MP4-Datei mit dem Originalbild und dem neuen Audio.

Bevor etwas berechnet wird, speichert der Agent deine Dateien bei sync., ermittelt die Länge der Sprache, nennt die Kosten und wartet auf dein Go.

## Wann du ihn nutzt

Nutze ihn, wenn du bereits Aufnahmen einer echten Person hast und sie etwas anderes sagen soll.

| Was du hast | Nimm |
| --- | --- |
| Ein Video und neues Audio oder ein Video und ein Skript | `lipsync` |
| Einen Clip aus Veo, Kling, Sora oder einem anderen Generator | [ai-video-to-talking](ai-video-to-talking.md) |
| Ein Standbild oder eine Illustration | [talking-photo](talking-photo.md) |
| Ein Video, das eine andere Sprache sprechen soll | [translate-and-dub](translate-and-dub.md) |
| Ein oder zwei falsche Wörter in einem sonst guten Take | [edit-dialogue](edit-dialogue.md) |
| Dutzende Videos oder Audiodateien | [batch-lipsync](batch-lipsync.md) |

## Probier es aus

- „Mach ./interview.mp4 lippensynchron zu ./new-take.wav“
- „Lass den Typen in https://example.com/talk.mp4 sagen, was in dieser MP3 ist“
- „Synchronisiere mein Musikvideo ./take3.mov mit dem finalen Mix“

## Was du brauchst

- Den verbundenen sync. MCP-Server oder eine gesetzte `SYNC_API_KEY`. Der [setup](setup.md)-Skill führt dich durch beides.
- Das Video als lokale Datei, öffentliche URL, sync.-Asset-ID oder als Link zu YouTube, TikTok, Instagram oder Facebook.
- Die Sprache als Audio oder als Skript plus Stimme.

## Häufige Fragen

**Warum hat er angehalten und mich gefragt, bevor er das Video erstellt hat?**
Jede Generierung wird abgerechnet, deshalb zeigt der Skill immer zuerst die Kostenschätzung und wartet auf deine Freigabe. Sag gleich zu Beginn „leg los, alles unter 5 $ ist okay“, dann hält er nicht zweimal an.

**Mein Audio ist länger als mein Video. Was passiert?**
Der Agent fragt, welchen [Sync-Modus](https://sync.so/docs/developer-guides/sync-mode) du willst: das Video vor- und zurücklaufen lassen (`bounce`, der Standard), es in einer Schleife abspielen, die Sprache am Videoende abschneiden, das Video stumm weiterlaufen lassen oder das Video schneller oder langsamer abspielen, damit es passt (`remap`).

**Im Bild sind zwei Personen.**
Der Agent fragt, wer sprechen soll, und richtet sync. auf dieses Gesicht aus. Ohne diese Angabe wählt sync. die sprechende Person selbst.

**Er hat sich geweigert, meine Datei hochzuladen.**
Er prüft, ob die Datei wirklich ein Medium ist, bevor er etwas ausgibt. Eine Datei, die weder Video noch Audio ist, oder eine Upload-Adresse, die nicht zu sync. gehört, stoppt den Lauf mit einer Erklärung. Es wird nichts berechnet.

**Welches Modell nutzt er?**
`sync-3`, das leistungsfähigste Modell, außer du wünschst dir ein anderes. Die Liste kommt aus deinem Konto, nicht aus dem Skill.

**Wo ist mein Video?**
Der Agent gibt dir den genauen Link zum Ergebnis. In einem Coding-Agenten bietet er an, die Datei neben deine Quelldatei herunterzuladen.

## Es funktioniert, wenn

- Du eine Kostenschätzung siehst, bevor eine Generierung startet.
- Lokale Dateien einmal hochgeladen werden und ein erneuter Versuch denselben Upload wiederverwendet.
- Die letzte Nachricht einen Link enthält, der dein Video mit der neuen Sprache abspielt.
