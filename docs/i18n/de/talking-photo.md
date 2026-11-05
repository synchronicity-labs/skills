---
title: "talking-photo-Skill"
subtitle: "Lass ein Foto, ein Porträt oder eine Figur sprechen."
description: "Der talking-photo-Skill von sync. labs macht aus einem Foto, einem Porträtfoto oder einer illustrierten Figur ein sprechendes Video, aus einem Skript oder einer Aufnahme, mit einer Stimme aus deinem Konto und einer Kostenschätzung, bevor etwas erstellt wird."
og:description: "Mach aus deinem Agenten aus einem Foto, einem Porträtfoto oder einer illustrierten Figur ein sprechendes Video."
source-sha256: 6aeeae5c018d350384c8f655da3d437d6aa76de342cb9d799b6880c5bf405d61
---

# talking-photo

> [!TIP]
> Installiere diesen Skill mit `npx skills add synchronicity-labs/skills --skill talking-photo` oder hol dir alle Skills mit dem Claude Code-Plugin. Siehe [Agent Skills](overview.md).

## Was er macht

`talking-photo` macht aus einem Standbild ein sprechendes Video. Gib ihm ein Foto, ein Porträtfoto oder eine illustrierte Figur, dazu ein Skript oder eine Aufnahme, und du bekommst eine MP4-Datei, in der dieses Gesicht spricht. Das Video ist so lang wie die Sprache.

Wenn du noch kein Bild hast und dein Agent Bilder erzeugen kann, bietet er an, eines zu erstellen, das gut funktioniert: ein klares Gesicht, Blick in die Kamera, Kopf und Schultern im Bild.

## Wann du ihn nutzt

| Was du hast | Nimm |
| --- | --- |
| Ein Foto, ein Porträt oder eine illustrierte Figur | `talking-photo` |
| Ein Video einer echten Person | [lipsync](lipsync.md) |
| Einen generierten Videoclip | [ai-video-to-talking](ai-video-to-talking.md) |

## Probier es aus

- „Lass das Porträtfoto unserer CEO sagen: Willkommen bei Acme, schön, dass du da bist“
- „Erstelle eine freundliche Cartoon-Barista und lass sie Guten Morgen sagen“
- „Lass ./portrait.png sagen, was in ./greeting.mp3 ist“

## Was du brauchst

- Den verbundenen sync. MCP-Server oder eine gesetzte `SYNC_API_KEY`. Der [setup](setup.md)-Skill führt dich durch beides.
- Ein Bild mit einem klaren menschlichen oder menschenähnlichen Gesicht. Tiere und nicht humanoide Figuren werden nicht unterstützt.
- Ein Skript oder eine Audiodatei, eine URL oder ein sync.-Asset.

## Häufige Fragen

**Kann er die Stimme für mich auswählen?**
Ja. Er listet die Stimmen in deinem Konto auf und schlägt zwei oder drei vor, die zur Figur passen. Sag „such selbst eine aus“, dann entscheidet er.

**Warum ist die Kostenschätzung „ungefähr“?**
Bei einem Skript wird die Länge der Sprache anhand der Wortanzahl geschätzt, bis sie gesprochen ist. Die Sprachsynthese wird getrennt vom Lipsync abgerechnet, und der Agent weist darauf hin.

**Mein Bild wurde abgelehnt.**
sync. braucht ein einzelnes, klares Gesicht in angemessener Größe. Gruppenfotos, winzige Gesichter und Profilansichten sind die üblichen Ursachen. Der Agent erklärt, woran es liegt, und schlägt einen engeren Ausschnitt mit Kopf und Schultern vor.

**Kann ich einen Promi etwas sagen lassen?**
Nein. Der Skill lehnt es ab, einer echten, identifizierbaren Person zur Täuschung Worte in den Mund zu legen. Deine eigenen Fotos, dein Team (mit Einverständnis) und fiktive Figuren sind kein Problem.

## Es funktioniert, wenn

- Der Agent eine Stimme aus der Liste deines Kontos wählt, keine erfundene ID.
- Du die Kostenschätzung siehst, bevor das Video erstellt wird.
- Das Ergebnis eine einzige MP4-Datei ist, in der das Gesicht genau deine Worte spricht.
