---
title: "Agent Skills von sync. labs"
subtitle: "Lippensynchronisation, Synchronisation und sprechende Videos aus Claude Code, Codex, Cursor und anderen Agenten."
description: "Installiere die offiziellen Agent Skills von sync. labs, um aus deinem Agenten Videos lippensynchron zu machen, Fotos und KI-Figuren sprechen zu lassen, zu übersetzen und zu synchronisieren, gesprochene Wörter zu korrigieren, Kampagnen zu lokalisieren, Lipsync im Batch auszuführen und sync. in Apps einzubauen."
og:description: "Offizielle Agent Skills von sync. labs für Lipsync, Synchronisation, sprechende Fotos, Dialogbearbeitung, Kampagnenlokalisierung, Batch-Läufe und API-Integrationen."
source-sha256: b2127b6c0b20e7920f0f6566eac05cca6fab410de78464947c0690fc7d640c07
---

# Agent Skills von sync. labs

Die Agent Skills von sync. labs bringen deinem Agenten bei, sync.-Aufgaben von Anfang bis Ende zu erledigen: Videos lippensynchron machen, Fotos und KI-Figuren sprechen lassen, übersetzen und synchronisieren, gesprochene Wörter korrigieren, ganze Kampagnen lokalisieren, Lipsync in großen Mengen ausführen und sync. in deine eigenen Apps einbauen. Sie funktionieren mit Claude Code, Codex, Cursor, Gemini CLI, Hermes und jedem Agenten, der [Agent Skills](https://agentskills.io) liest.

Jeder Skill ist ein Ordner mit einer `SKILL.md` voller Anweisungen sowie Referenzdateien und Skripten, die der Agent nur lädt, wenn eine Aufgabe sie braucht. Beschreib in eigenen Worten, was du möchtest, und der Agent wählt den passenden Skill.

<!-- card icon="fa-brands fa-github" -->
**[synchronicity-labs/skills auf GitHub](https://github.com/synchronicity-labs/skills)**
Quellcode für jeden Skill, die Plugin-Manifeste und ein Changelog. MIT-lizenziert.

> [!NOTE]
> Jeder Skill nennt die Kosten, bevor kostenpflichtige Arbeit beginnt, und wartet auf deine Freigabe. Der setup-Skill selbst startet nie kostenpflichtige Arbeit.

## Skills installieren

### Jeder Agent (skills.sh)

Installiere alle Skills mit [skills.sh](https://skills.sh):

```bash
npx skills add synchronicity-labs/skills
```

Mit `--skill <name>` installierst du einen einzelnen Skill, zum Beispiel `--skill lipsync`, mit `--agent claude-code` wählst du den Agenten.

### Claude Code-Plugin

Das Plugin installiert die Skills und verbindet den sync. MCP-Server in einem Schritt.

1. **Marketplace hinzufügen**

   ```text
   /plugin marketplace add synchronicity-labs/skills
   ```

2. **Plugin installieren**

   ```text
   /plugin install sync@sync
   ```

3. **Anmelden**

   Führe `/mcp` aus, wähle `sync` und melde dich mit deinem sync.-Konto an.

### Codex und Cursor

Codex und Cursor lesen die Plugin-Manifeste in den Ordnern `.codex-plugin/` und `.cursor-plugin/` des Repositorys. Beide Manifeste verbinden den gehosteten sync. MCP-Server. Du kannst die Skills auch mit skills.sh installieren und den Server mit den Schritten des [setup-Skills](setup.md) für deinen Agenten verbinden.

## sync. verbinden

Die Skills nutzen den gehosteten [sync. MCP-Server](https://sync.so/docs/plugins-and-extensions/mcp-server) unter `https://mcp.sync.so/mcp`. Du meldest dich mit deinem sync.-Konto an, es gibt also keinen Schlüssel zu kopieren. Der [setup-Skill](setup.md) führt jeden Agenten durch die Verbindung, und seine Seite listet die Schritte für jeden Agenten auf.

Für Skripte, CI, Agenten ohne Zugriff auf Remote-Server und den [sync-api-Skill](sync-api.md) erstellst du stattdessen einen [API-Schlüssel](https://sync.so/settings/api-keys) und setzt ihn als `SYNC_API_KEY`. Um dieselben MCP-Tools lokal mit diesem Schlüssel zu nutzen, starte das npm-Paket:

```bash
npx -y @sync.so/mcp-server@latest
```

## Skills

| Skill | Was er macht | Probier es aus |
| --- | --- | --- |
| [setup](setup.md) | Verbindet sync. mit deinem Agenten, prüft dein Konto und bringt dich zum ersten Video. | „Richte sync. ein“ |
| [lipsync](lipsync.md) | Synchronisiert die Lippen in einem Video mit neuem Audio oder einem getippten Skript. | „Synchronisiere ./talk.mp4 lippensynchron mit ./new-take.wav“ |
| [talking-photo](talking-photo.md) | Lässt ein Foto, ein Porträt oder eine Figur sprechen. | „Lass dieses Porträtfoto sagen: Willkommen im Team“ |
| [ai-video-to-talking](ai-video-to-talking.md) | Gibt KI-generierten Clips aus Veo, Kling, Sora und anderen Dialog, auch in Szenen mit mehreren Einstellungen. | „Mein Veo-Clip hat keinen Dialog. Lass sie diesen Satz sagen.“ |
| [translate-and-dub](translate-and-dub.md) | Synchronisiert ein Video in andere Sprachen, mit passenden Lippenbewegungen. | „Synchronisiere dieses YouTube-Video auf Spanisch“ |
| [edit-dialogue](edit-dialogue.md) | Ändert oder entfernt einzelne gesprochene Wörter in der eigenen Stimme der sprechenden Person. | „Ändere den Preis, den ich nenne, auf 49 $“ |
| [localize-campaign](localize-campaign.md) | Lokalisiert eine Reihe von Videos für mehrere Märkte: Plan, Pilot, Durchlauf, Review-Tabelle. | „Mach diese drei Anzeigen auf Spanisch, Deutsch und Japanisch“ |
| [batch-lipsync](batch-lipsync.md) | Synchronisiert jede Zeile einer CSV-Datei oder eines Ordners lippensynchron, fortsetzbar, innerhalb der Limits deines Tarifs oder, im Scale-Tarif, über die Batch API. | „Synchronisiere jede Zeile aus leads.csv auf presenter.mp4“ |
| [sync-api](sync-api.md) | Baut sync. mit der REST-API oder den Python- und TypeScript-SDKs in Apps ein: Uploads, Idempotenz, Webhooks, Fehler. | „Füge meiner Next.js-App sync. Lipsync hinzu“ |
| [troubleshoot](troubleshoot.md) | Findet heraus, warum ein Auftrag fehlgeschlagen ist, hängt oder abgelehnt wurde, setzt ihn fort, ohne doppelt zu zahlen, und kann das Problem an sync. melden. | „Mein Lipsync ist fehlgeschlagen, warum?“ |

Auf der Seite jedes Skills findest du Beispiel-Prompts, die Voraussetzungen, häufige Fragen und woran du erkennst, dass er funktioniert.

## Kostenpflichtige Arbeit wird immer zuerst freigegeben

Jede Generierung wird abgerechnet, deshalb nennt jeder Skill die Kosten, bevor kostenpflichtige Arbeit beginnt, und wartet auf dein Go. Wenn du nicht zweimal gefragt werden willst, nenne vorab ein Budget, zum Beispiel „leg los, alles unter 5 $ ist okay“. Läufe über viele Videos, etwa [localize-campaign](localize-campaign.md) und [batch-lipsync](batch-lipsync.md), nennen die Kosten für den gesamten Lauf und bieten vor dem Rest einen Pilotlauf an. Nach dieser einen Freigabe startet der Rest zusammen statt einzeln.

<!-- llms-ignore -->
## Weitere Ressourcen

- [MCP-Server](https://sync.so/docs/plugins-and-extensions/mcp-server): KI-Clients mit sync. labs verbinden
- [ChatGPT-Plugin](https://sync.so/docs/plugins-and-extensions/chatgpt-plugin): sync. labs in ChatGPT nutzen
- [SDKs](https://sync.so/docs/developer-guides/sdk): offizielle Python- und TypeScript-SDKs
- [Authentifizierung](https://sync.so/docs/api-reference/guides/authentication): einen API-Schlüssel erstellen und verwenden
<!-- /llms-ignore -->
