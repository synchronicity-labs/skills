---
title: "Skill setup"
subtitle: "Conecta sync. a tu agente, revisa tu cuenta y llega a tu primer vídeo."
description: "La skill de agente setup de sync. labs conecta sync. a Claude Code, Codex, Cursor y otros agentes, muestra tu plan y tus créditos y te sugiere un primer vídeo. Nunca inicia trabajo de pago."
og:description: "Conecta sync. a tu agente, revisa tu cuenta, tu plan y tus créditos y llega a tu primer vídeo."
source-sha256: 8bf4757e0b9fd57ed1bb43b1d923220a2e62a7d62a8dd8ae8c1dd87f2a19d10a
---

# setup

> [!TIP]
> Instala esta skill con `npx skills add synchronicity-labs/skills --skill setup`, o consigue todas las skills con el plugin de Claude Code. Consulta [Skills de agente](overview.md).

## Qué hace

`setup` conecta sync. a tu agente y te lleva a tu primer vídeo en un par de minutos. Comprueba la conexión, inicia sesión si hace falta, muestra tu cuenta, tu plan y los créditos que te quedan, y enumera lo que puedes crear con un prompt de ejemplo para cada caso. La propia skill setup nunca inicia trabajo de pago.

## Cuándo usarla

- Justo después de instalar las skills o el plugin.
- Cuando faltan las herramientas de sync. o se ha cerrado la sesión.
- Para revisar tu cuenta, tu plan o tus créditos.

Las peticiones de contenido como «sincroniza los labios de esto» van directamente a su propia skill, que te conecta de la misma forma cuando hace falta. Si algo falló o parece atascado, usa [troubleshoot](troubleshoot.md).

## Prueba

- «Configura sync.»
- «¿Cuántos créditos de sync me quedan?»

## Conectar

| Agente | Cómo |
| --- | --- |
| Claude Code con el plugin | Ejecuta `/mcp`, selecciona `sync` e inicia sesión |
| Claude Code sin el plugin | `claude mcp add --transport http sync https://mcp.sync.so/mcp` y después `/mcp` |
| Claude.ai o Claude Desktop | Settings, Connectors, Add custom connector, `https://mcp.sync.so/mcp` |
| Codex | `codex mcp add sync --url https://mcp.sync.so/mcp` y después `codex mcp login sync` |
| Cursor | Añade `{"mcpServers": {"sync": {"url": "https://mcp.sync.so/mcp"}}}` a `.cursor/mcp.json` |
| Scripts y CI | Define `SYNC_API_KEY` o ejecuta el servidor local con `npx -y @sync.so/mcp-server@latest` |

El servidor alojado inicia sesión con tu cuenta de sync., así que no tienes que copiar ninguna clave. Para obtener una clave API, consulta [Autenticación](https://sync.so/docs/api-reference/guides/authentication). Para saber más sobre el propio servidor, consulta la guía del [servidor MCP](https://sync.so/docs/plugins-and-extensions/mcp-server).

## Preguntas frecuentes

**Después de conectarme dice que las herramientas no están.**
La mayoría de los agentes solo cargan los servidores MCP nuevos después de reiniciar o recargar.

**¿Necesito un plan de pago?**
No. Todas las cuentas empiezan con unas cuantas generaciones gratuitas al mes. Los planes de pago amplían los límites de duración y la concurrencia, y a partir de Creator eliminan la marca de agua.

**¿Qué uso, el servidor alojado o npm?**
El servidor alojado para el uso interactivo, porque inicias sesión con tu cuenta. El paquete de npm con una clave API para scripts, CI y agentes que no pueden usar servidores remotos.

## Funciona si

- Ves el nombre de tu organización y tus créditos o tu cuota restantes.
- Recibes una lista breve de cosas que probar y no se te cobra nada.
