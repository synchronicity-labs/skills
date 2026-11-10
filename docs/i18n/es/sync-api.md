---
title: "Skill sync-api"
subtitle: "Integra sync. en apps con la API REST o los SDK de Python y TypeScript."
description: "La skill de agente sync-api de sync. labs ayuda a tu agente de programación a integrar sync. en una app, un backend, un script o un pipeline: subidas, generaciones con claves de idempotencia, webhooks verificados, polling, errores y límites de concurrencia."
og:description: "Haz que tu agente de programación escriba integraciones de sync. en el servidor con claves de idempotencia, webhooks verificados y una gestión correcta de los 429."
source-sha256: 061702b8ed38fec950d9150ef03d9c00dbdc027e8ec001ce4faf5aaeca1fdec9
---

# sync-api

> [!TIP]
> Instala esta skill con `npx skills add synchronicity-labs/skills --skill sync-api`, o consigue todas las skills con el plugin de Claude Code. Consulta [Skills de agente](overview.md).

## Qué hace

`sync-api` ayuda a tu agente de programación a integrar sync. en tu propia app, backend, script o pipeline. Escribe código de servidor que sube contenido multimedia, crea generaciones con claves de idempotencia, verifica webhooks, consulta el estado como alternativa y gestiona errores y límites de concurrencia, usando la API REST o los [SDK](https://sync.so/docs/developer-guides/sdk) oficiales de Python (`syncsdk`) y TypeScript (`@sync.so/sdk`).

## Cuándo usarla

| Lo que estás haciendo | Usa |
| --- | --- |
| Escribir o revisar código que llama a la API de sync. | `sync-api` |
| Depurar un 429, un webhook o un cobro duplicado | `sync-api` |
| Crear un vídeo en este chat | [lipsync](lipsync.md), [talking-photo](talking-photo.md), [translate-and-dub](translate-and-dub.md) |
| Procesar una vez un CSV de trabajos | [batch-lipsync](batch-lipsync.md) |

## Prueba

- «Añade a mi app de Express un endpoint que sincronice los labios de una URL de vídeo con una URL de audio usando sync.»
- «Escribe un script de Python que doble al español cada vídeo de ./in»
- «Añade una ruta de Next.js que verifique los webhooks de sync.»
- «Nuestro worker recibe una y otra vez 429 concurrency_limit_reached. ¿Cuál es la solución correcta?»

## Qué necesitas

- Una clave API de sync. de [sync.so/settings/api-keys](https://sync.so/settings/api-keys), definida como `SYNC_API_KEY` en el servidor. Consulta [Autenticación](https://sync.so/docs/api-reference/guides/authentication).
- Python 3.8 o posterior, o Node 18 o posterior, para los SDK.

## Preguntas frecuentes

**¿Por qué el código guarda una clave antes de llamar a la API?**
`POST /v2/generate` acepta un `Idempotency-Key`. Si se crea una vez por trabajo y se reutiliza en cada reintento, un reintento tras un timeout se convierte en una repetición de la generación original en lugar de una segunda generación de pago. Consulta [Idempotent Requests](https://sync.so/docs/api-reference/guides/idempotency).

**¿Webhooks o polling?**
[Webhooks](https://sync.so/docs/api-reference/guides/webhooks), verificados con la cabecera `Sync-Signature`, para producción. Una consulta periódica recoge las entregas que tu endpoint se haya perdido.

**El SDK no tiene un campo que menciona la documentación.**
Los SDK pueden ir por detrás de la API. La skill llama a ese endpoint por HTTP en lugar de forzar los tipos.

**¿Qué hago con un 429?**
Espera el tiempo que indica la respuesta, reintenta con la misma clave de idempotencia y mantén como máximo tantos trabajos en curso como permita el límite de concurrencia de tu plan, con una cola de tu lado. Consulta [Concurrencia y límites de tasa](https://sync.so/docs/api-reference/guides/rate-limits).

## Funciona si

- La clave API vive en el servidor, nunca en código de navegador o de móvil.
- Cada creación lleva una clave de idempotencia que se guardó antes de la llamada.
- El gestor de webhooks comprueba la firma con el cuerpo sin procesar antes de analizarlo.
