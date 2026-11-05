---
title: "Skill troubleshoot"
subtitle: "Averigua por qué un trabajo falló, se atascó o fue rechazado, y reanúdalo sin pagar dos veces."
description: "La skill de agente troubleshoot de sync. labs averigua por qué un trabajo de sync. falló, se atascó o fue rechazado, explica la causa real con palabras sencillas, retoma el trabajo sin iniciar un segundo trabajo de pago y puede informar del problema a sync."
og:description: "Averigua desde tu agente por qué un trabajo de sync. falló, se atascó o fue rechazado, y reanúdalo sin pagar dos veces."
source-sha256: 8de9f50b08fda9e8256cefecc063b3e44871e28eb125c0e2060560fcdabb8fff
---

# troubleshoot

> [!TIP]
> Instala esta skill con `npx skills add synchronicity-labs/skills --skill troubleshoot`, o consigue todas las skills con el plugin de Claude Code. Consulta [Skills de agente](overview.md).

## Qué hace

`troubleshoot` averigua por qué un trabajo de sync. falló, se atascó o fue rechazado, te explica la causa real con palabras sencillas y retoma el trabajo sin iniciar un segundo trabajo de pago. Cuando el problema fue un error confuso o una función que falta, también puede enviar un informe breve al equipo de sync., sin secretos ni contenido multimedia adjuntos.

## Cuándo usarla

| Lo que pasó | Usa |
| --- | --- |
| Un trabajo falló, fue rechazado o parece atascado | `troubleshoot` |
| Un 402, un 429 u otro error de sync. | `troubleshoot` |
| Las herramientas de sync. desaparecieron o dicen que se ha cerrado la sesión | `troubleshoot`, que te vuelve a conectar de la misma forma que [setup](setup.md) |
| Todavía no has conectado sync. | [setup](setup.md) |
| Tu propio código recibe errores de la API | [sync-api](sync-api.md) |

## Prueba

- «Mi lipsync ha fallado, ¿por qué?»
- «Este doblaje lleva 20 minutos procesándose»
- «Me sigue saliendo concurrency_limit_reached»
- «El vídeo salió, pero la boca no se ve bien»

## Qué necesitas

- El servidor MCP de sync. conectado, para consultar el estado del trabajo y tu cuenta. Sin él, la skill igualmente puede explicar un mensaje de error que pegues.
- El texto del error, o el ID de la generación o del batch si lo tienes.

## Preguntas frecuentes

**¿Se me cobró el trabajo que falló?**
No. Las generaciones que fallan no se cobran.

**Sigue procesándose. ¿Debería iniciarlo de nuevo?**
No. Pendiente no es lo mismo que fallido, y un segundo trabajo no terminará antes. La skill sigue consultando el mismo trabajo.

**Mi petición superó el tiempo de espera. ¿Se llegó a procesar?**
Puede que sí. La skill busca el trabajo, o reintenta la petición idéntica con la misma clave, que devuelve el original en lugar de iniciar otro.

**El resultado no se ve bien.**
Las causas habituales están en el original: una cara girada o tapada, varias personas en el encuadre, música bajo la voz o baja resolución. La skill revisa esos puntos y sugiere `sync-3` si se usó un modelo anterior. Volver a intentarlo es una nueva generación de pago, así que primero estima el coste.

**¿Qué incluye el informe a sync.?**
El tipo de problema, el error exacto, la herramienta y el ID del trabajo. Nunca tu clave, enlaces firmados, datos personales ni contenido multimedia.

## Funciona si

- Obtienes la causa real, con el código de error cuando lo hay.
- No se inicia ningún segundo trabajo de pago a menos que apruebes un nuevo intento.
- El trabajo original se reanuda desde donde se detuvo.
