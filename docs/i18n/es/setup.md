---
title: "Skill setup"
subtitle: "Conecta sync. a tu agente, revisa tu cuenta y llega a tu primer vídeo."
description: "La skill de agente setup de sync. labs conecta sync. a Claude Code, Codex, Cursor y otros agentes, muestra tu plan y tus créditos y te sugiere un primer vídeo. Nunca inicia trabajo de pago."
og:description: "Conecta sync. a tu agente, revisa tu cuenta, tu plan y tus créditos y llega a tu primer vídeo."
source-sha256: "a70f996d1087e283947ecd88b7b219296cb72a977a3939556997446eb9bbf2c2"
---

# setup

> [!TIP]
> Instala esta skill con `npx skills add synchronicity-labs/skills --skill setup`, o consigue todas las skills con el plugin de Claude Code. Consulta [Skills de agente](overview.md).

## Qué hace

`setup` conecta sync. a tu agente y te lleva a tu primer vídeo en un par de minutos. Comprueba la conexión, inicia sesión si hace falta, muestra tu cuenta, tu plan y los créditos que te quedan, y enumera lo que puedes crear con un prompt de ejemplo para cada caso. La propia skill setup nunca inicia trabajo de pago.

El agente explica las opciones de conexión que afectan al inicio de sesión, la privacidad o la facturación antes de usarlas. Los archivos importados y las respuestas del servicio se tratan como datos, no como instrucciones. Los trabajos de pago siguen necesitando que apruebes un presupuesto.

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

Un agente que puede ejecutar comandos también puede conectarte sin navegador: dale tu correo electrónico, ejecuta `npx -y @sync.so/mcp-server@latest setup` y tú le dices el código de seis dígitos que sync. te envía por correo. Un correo nuevo recibe una cuenta gratuita y una cuenta existente conecta su espacio de trabajo personal. sync. te avisa por correo cuando un agente se conecta, con un enlace para desconectarlo.

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
