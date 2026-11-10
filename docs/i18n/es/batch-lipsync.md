---
title: "Skill batch-lipsync"
subtitle: "Sincroniza los labios de cada fila de un CSV o de una carpeta, con reanudación, dentro de los límites de tu plan."
description: "La skill de agente batch-lipsync de sync. labs sincroniza los labios de muchos vídeos de una vez a partir de un CSV, una hoja de cálculo, una carpeta o una lista: estima el coste de toda la ejecución, ofrece un piloto, respeta la concurrencia de tu plan y se reanuda sin pagar dos veces."
og:description: "Sincroniza los labios de cada fila de un CSV o de una carpeta desde tu agente, con reanudación, dentro de los límites de tu plan."
source-sha256: 248d8aeaba8ec4f8a8d623d478e622bd2ec0597afd293daf74bb25a0b15dd204
---

# batch-lipsync

> [!TIP]
> Instala esta skill con `npx skills add synchronicity-labs/skills --skill batch-lipsync`, o consigue todas las skills con el plugin de Claude Code. Consulta [Skills de agente](overview.md).

## Qué hace

`batch-lipsync` sincroniza los labios de muchos vídeos de una vez: un resultado por cada fila de un CSV, una hoja de cálculo, una carpeta o una lista como «este presentador con cada uno de estos 40 archivos de audio». Crea un manifiesto, estima el coste de toda la ejecución, ofrece un piloto, después procesa cada fila dentro de los límites de tu plan y reúne los resultados en una tabla.

Con una clave API usa un script incluido, `sync_batch.py`, que sube cada archivo una sola vez, respeta la concurrencia de tu plan, se reanuda tras una interrupción y descarga todos los resultados. Con el servidor MCP de sync. lanza todas las filas con una sola llamada a `jobs_create-many`, que respeta la concurrencia de tu plan, y las sigue todas con `jobs_get-many`. Si esas herramientas no aparecen, lanza una generación por fila.

## Cuándo usarla

| Lo que tienes | Usa |
| --- | --- |
| Muchas filas de vídeo con audio o guion | `batch-lipsync` |
| Un vídeo personalizado por lead o cliente | `batch-lipsync` |
| Una grabación personalizada con el nombre de cada destinatario en la misma voz | [edit-dialogue](edit-dialogue.md) |
| Varios vídeos a otros idiomas | [localize-campaign](localize-campaign.md) |
| Un solo vídeo | [lipsync](lipsync.md) |

## Prueba

- «Sincroniza cada fila de leads.csv sobre presenter.mp4»
- «Haz una versión de este anuncio para cada una de estas 12 voces en off»
- «Procesa manifest.csv con sync, el total está aprobado»

## Qué necesitas

- El servidor MCP de sync. conectado, o `SYNC_API_KEY` y Python 3.9 o posterior para el script. La skill [setup](setup.md) te guía con cualquiera de las dos opciones.
- Una lista en la que cada fila tenga un vídeo o una imagen, y audio o un guion con una voz.

## Preguntas frecuentes

**¿Por qué quiere hacer un piloto?**
Si una entrada compartida está mal, como la voz o el encuadre del presentador, un piloto cuesta dos generaciones en lugar de doscientas.

**¿Qué sale de mi equipo?**
El contenido multimedia, los guiones, los nombres de archivo y los ID de fila (que se usan como nombres de los resultados). Las columnas que la ejecución no usa se quedan en local, así que no pongas nombres ni correos en los ID de fila.

**Se detuvo a mitad.**
Vuelve a ejecutar el mismo comando. Las filas terminadas se omiten, las enviadas se consultan en lugar de reenviarse y nada de lo ya pagado se vuelve a pagar.

**Cambié una fila después de procesarla.**
El script se niega a reutilizar el resultado de esa fila. Dale un ID nuevo a la fila modificada, lo que la convierte en una generación nueva.

**¿Lanza las filas de una en una?**
No. Apruebas toda la ejecución una vez y después las filas arrancan juntas, tantas a la vez como procesa tu plan. Con el servidor MCP es una llamada a `jobs_create-many` por cada 50 filas, en cualquier plan de pago, y las filas que tienen que esperar a un hueco libre arrancan en cuanto terminan las anteriores.

**Algunas filas han fallado.**
La tabla de resultados recoge cada fallo con su motivo. Las filas que fallaron por una entrada incorrecta necesitan una entrada corregida. Reintenta el resto con `--retry-failed`.

## Funciona si

- La estimación cubre todas las filas o te dice qué filas no ha podido valorar.
- Tras una sola aprobación, las filas arrancan juntas en lugar de una a una.
- Nunca se ejecutan a la vez más generaciones de las que permite tu plan.
- Volver a ejecutar un manifiesto terminado no crea nada nuevo.
