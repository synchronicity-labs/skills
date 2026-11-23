---
title: "setup-Skill"
subtitle: "Verbinde sync. mit deinem Agenten, prüfe dein Konto und komm zu deinem ersten Video."
description: "Der setup-Skill von sync. labs verbindet sync. mit Claude Code, Codex, Cursor und anderen Agenten, zeigt deinen Tarif und deine Credits an und schlägt ein erstes Video vor. Er startet nie kostenpflichtige Arbeit."
og:description: "Verbinde sync. mit deinem Agenten, prüfe Konto, Tarif und Credits und komm zu deinem ersten Video."
source-sha256: "a70f996d1087e283947ecd88b7b219296cb72a977a3939556997446eb9bbf2c2"
---

# setup

> [!TIP]
> Installiere diesen Skill mit `npx skills add synchronicity-labs/skills --skill setup` oder hol dir alle Skills mit dem Claude Code-Plugin. Siehe [Agent Skills](overview.md).

## Was er macht

`setup` verbindet sync. mit deinem Agenten und bringt dich in wenigen Minuten zu deinem ersten Video. Er prüft die Verbindung, meldet dich bei Bedarf an, zeigt dein Konto, deinen Tarif und deine verbleibenden Credits und listet auf, was du erstellen kannst, jeweils mit einem Beispiel-Prompt. Der setup-Skill selbst startet nie kostenpflichtige Arbeit.

Verbindungsoptionen, die Anmeldung, Datenschutz oder Abrechnung betreffen, werden vor der Nutzung erklärt. Importierte Medien und Antworten des Dienstes werden als Daten behandelt, nicht als Anweisungen. Kostenpflichtige Vorgänge benötigen weiterhin deine Zustimmung zum Kostenvoranschlag.

## Wann du ihn nutzt

- Direkt nach der Installation der Skills oder des Plugins.
- Wenn sync.-Tools fehlen oder abgemeldet sind.
- Um dein Konto, deinen Tarif oder deine Credits zu prüfen.

Medienanfragen wie „mach das lippensynchron“ gehen direkt an den jeweiligen Skill, der dich bei Bedarf auf dieselbe Weise verbindet. Wenn etwas fehlgeschlagen ist oder hängt, nutze [troubleshoot](troubleshoot.md).

## Probier es aus

- „Richte sync. ein“
- „Wie viele sync-Credits habe ich noch?“

## Verbinden

| Agent | So geht's |
| --- | --- |
| Claude Code mit dem Plugin | Führe `/mcp` aus, wähle `sync` und melde dich an |
| Claude Code ohne das Plugin | `claude mcp add --transport http sync https://mcp.sync.so/mcp`, dann `/mcp` |
| Claude.ai oder Claude Desktop | Settings, Connectors, Add custom connector, `https://mcp.sync.so/mcp` |
| Codex | `codex mcp add sync --url https://mcp.sync.so/mcp`, dann `codex mcp login sync` |
| Cursor | Füge `{"mcpServers": {"sync": {"url": "https://mcp.sync.so/mcp"}}}` zu `.cursor/mcp.json` hinzu |
| Skripte und CI | Setze `SYNC_API_KEY` oder starte den lokalen Server mit `npx -y @sync.so/mcp-server@latest` |

Der gehostete Server meldet dich mit deinem sync.-Konto an, es gibt also keinen Schlüssel zu kopieren. Für einen API-Schlüssel siehe [Authentifizierung](https://sync.so/docs/api-reference/guides/authentication). Mehr über den Server selbst findest du in der Anleitung zum [MCP-Server](https://sync.so/docs/plugins-and-extensions/mcp-server).

Ein Agent, der Befehle ausführen kann, verbindet dich auch ohne Browser: Gib ihm deine E-Mail-Adresse, er führt `npx -y @sync.so/mcp-server@latest setup` aus, und du nennst ihm den sechsstelligen Code, den sync. dir per E-Mail schickt. Eine neue E-Mail-Adresse bekommt ein kostenloses Konto, ein bestehendes Konto verbindet seinen persönlichen Workspace. sync. schickt dir eine E-Mail, wenn sich ein Agent verbindet, mit einem Link, der ihn wieder trennt.

## Häufige Fragen

**Nach dem Verbinden heißt es, die Tools seien nicht da.**
Die meisten Agenten laden neue MCP-Server erst nach einem Neustart oder Neuladen.

**Brauche ich einen kostenpflichtigen Tarif?**
Nein. Jedes Konto startet mit ein paar kostenlosen Generierungen pro Monat. Kostenpflichtige Tarife erhöhen die Längenlimits und die Anzahl gleichzeitiger Aufträge und entfernen ab Creator das Wasserzeichen.

**Was soll ich nutzen, den gehosteten Server oder npm?**
Den gehosteten Server für die interaktive Nutzung, weil du dich mit deinem Konto anmeldest. Das npm-Paket mit einem API-Schlüssel für Skripte, CI und Agenten ohne Zugriff auf Remote-Server.

## Es funktioniert, wenn

- Du den Namen deiner Organisation und deine verbleibenden Credits oder dein Kontingent siehst.
- Du eine kurze Liste mit Ideen zum Ausprobieren bekommst und nichts berechnet wird.
