---
title: "Skills de agente de sync. labs"
subtitle: "Sincroniza labios, dobla y crea vídeos que hablan desde Claude Code, Codex, Cursor y otros agentes."
description: "Instala las skills de agente oficiales de sync. labs para sincronizar los labios de vídeos, hacer hablar a fotos y personajes de IA, traducir y doblar, corregir palabras habladas, localizar campañas, sincronizar labios por lotes e integrar sync. en apps desde tu agente."
og:description: "Skills de agente oficiales de sync. labs para lipsync, doblaje, fotos que hablan, edición de diálogos, localización de campañas, ejecuciones por lotes e integraciones con la API."
source-sha256: b2127b6c0b20e7920f0f6566eac05cca6fab410de78464947c0690fc7d640c07
---

# Skills de agente de sync. labs

Las skills de agente de sync. labs enseñan a tu agente a hacer el trabajo de sync. de principio a fin: sincronizar los labios de vídeos, hacer hablar a fotos y personajes de IA, traducir y doblar, corregir palabras habladas, localizar campañas completas, sincronizar labios a gran escala e integrar sync. en tus propias apps. Funcionan con Claude Code, Codex, Cursor, Gemini CLI, Hermes y cualquier agente que lea [Agent Skills](https://agentskills.io).

Cada skill es una carpeta con un `SKILL.md` de instrucciones, además de archivos de referencia y scripts que el agente carga solo cuando una tarea los necesita. Describe lo que quieres con tus propias palabras y el agente elige la skill adecuada.

<!-- card icon="fa-brands fa-github" -->
**[synchronicity-labs/skills en GitHub](https://github.com/synchronicity-labs/skills)**
El código de cada skill, los manifiestos del plugin y un registro de cambios. Con licencia MIT.

> [!NOTE]
> Cada skill indica el coste antes de empezar cualquier trabajo de pago y espera tu aprobación. La propia skill setup nunca inicia trabajo de pago.

## Instalar las skills

### Cualquier agente (skills.sh)

Instala todas las skills con [skills.sh](https://skills.sh):

```bash
npx skills add synchronicity-labs/skills
```

Añade `--skill <name>` para instalar una sola skill, por ejemplo `--skill lipsync`, o `--agent claude-code` para elegir el agente.

### Plugin de Claude Code

El plugin instala las skills y conecta el servidor MCP de sync. en un solo paso.

1. **Añade el marketplace**

   ```text
   /plugin marketplace add synchronicity-labs/skills
   ```

2. **Instala el plugin**

   ```text
   /plugin install sync@sync
   ```

3. **Inicia sesión**

   Ejecuta `/mcp`, selecciona `sync` e inicia sesión con tu cuenta de sync.

### Codex y Cursor

Codex y Cursor leen los manifiestos del plugin en las carpetas `.codex-plugin/` y `.cursor-plugin/` del repositorio. Ambos manifiestos conectan el servidor MCP alojado de sync. También puedes instalar las skills con skills.sh y conectar el servidor siguiendo los pasos de la [skill setup](setup.md) para tu agente.

## Conectar sync.

Las skills usan el [servidor MCP de sync.](https://sync.so/docs/plugins-and-extensions/mcp-server) alojado en `https://mcp.sync.so/mcp`. Inicias sesión con tu cuenta de sync., así que no tienes que copiar ninguna clave. La [skill setup](setup.md) guía a cualquier agente durante la conexión, y su página recoge los pasos para cada agente.

Para scripts, CI, agentes que no pueden usar servidores remotos y la [skill sync-api](sync-api.md), crea una [clave API](https://sync.so/settings/api-keys) y defínela como `SYNC_API_KEY`. Para usar las mismas herramientas MCP en local con esa clave, ejecuta el paquete de npm:

```bash
npx -y @sync.so/mcp-server@latest
```

## Skills

| Skill | Qué hace | Prueba |
| --- | --- | --- |
| [setup](setup.md) | Conecta sync. a tu agente, revisa tu cuenta y te lleva hasta tu primer vídeo. | «Configura sync.» |
| [lipsync](lipsync.md) | Sincroniza los labios de un vídeo con un audio nuevo o un guion escrito. | «Sincroniza los labios de ./talk.mp4 con ./new-take.wav» |
| [talking-photo](talking-photo.md) | Hace hablar a una foto, un retrato o un personaje. | «Haz que este retrato diga: bienvenido al equipo» |
| [ai-video-to-talking](ai-video-to-talking.md) | Pone diálogo en clips generados con IA en Veo, Kling, Sora y otros, incluidas escenas con varios planos. | «Mi clip de Veo no tiene diálogo. Haz que diga esta frase.» |
| [translate-and-dub](translate-and-dub.md) | Dobla un vídeo a otros idiomas con los labios sincronizados. | «Dobla este vídeo de YouTube al español» |
| [edit-dialogue](edit-dialogue.md) | Cambia o elimina algunas palabras habladas con la propia voz de quien habla. | «Cambia el precio que digo a $49» |
| [localize-campaign](localize-campaign.md) | Localiza un conjunto de vídeos para varios mercados: plan, piloto, ejecución y hoja de revisión. | «Haz estos tres anuncios en español, alemán y japonés» |
| [batch-lipsync](batch-lipsync.md) | Sincroniza los labios de cada fila de un CSV o de una carpeta, con reanudación, dentro de los límites de tu plan o, en los planes Scale, mediante la Batch API. | «Sincroniza cada fila de leads.csv sobre presenter.mp4» |
| [sync-api](sync-api.md) | Integra sync. en apps con la API REST o los SDK de Python y TypeScript: subidas, idempotencia, webhooks y errores. | «Añade lipsync de sync. a mi app de Next.js» |
| [troubleshoot](troubleshoot.md) | Averigua por qué un trabajo falló, se atascó o fue rechazado, lo reanuda sin pagar dos veces y puede informar del problema a sync. | «Mi lipsync ha fallado, ¿por qué?» |

La página de cada skill incluye prompts de ejemplo, lo que necesitas, preguntas frecuentes y cómo saber que está funcionando.

## El trabajo de pago siempre se aprueba antes

Cada generación se factura, así que cada skill indica el coste antes de empezar trabajo de pago y espera a que des luz verde. Si prefieres que no te pregunte dos veces, fija un presupuesto desde el principio, por ejemplo «adelante, cualquier cosa por debajo de $5 me vale». Las ejecuciones con muchos vídeos, como [localize-campaign](localize-campaign.md) y [batch-lipsync](batch-lipsync.md), estiman el coste de toda la ejecución y ofrecen un piloto antes del resto. Tras esa única aprobación, el resto arranca a la vez en lugar de uno a uno.

<!-- llms-ignore -->
## Recursos relacionados

- [Servidor MCP](https://sync.so/docs/plugins-and-extensions/mcp-server): conecta clientes de IA a sync. labs
- [Plugin de ChatGPT](https://sync.so/docs/plugins-and-extensions/chatgpt-plugin): usa sync. labs dentro de ChatGPT
- [SDK](https://sync.so/docs/developer-guides/sdk): SDK oficiales de Python y TypeScript
- [Autenticación](https://sync.so/docs/api-reference/guides/authentication): crea y usa una clave API
<!-- /llms-ignore -->
