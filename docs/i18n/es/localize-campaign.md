---
title: "Skill localize-campaign"
subtitle: "Localiza un conjunto de vídeos para varios mercados: plan, piloto, ejecución y hoja de revisión."
description: "La skill de agente localize-campaign de sync. labs produce cada vídeo de una campaña, un curso o una serie de producto en cada idioma de destino: asigna idiomas a los mercados, estima el coste de la matriz, hace un piloto con una versión y después ejecuta el resto con una hoja de revisión."
og:description: "Localiza varios vídeos a varios idiomas desde tu agente, con un piloto primero y una hoja de revisión al final."
source-sha256: be752c55e5f10643954e19e5d881c95e767bcc4b0c501e48164d5855d5281879
---

# localize-campaign

> [!TIP]
> Instala esta skill con `npx skills add synchronicity-labs/skills --skill localize-campaign`, o consigue todas las skills con el plugin de Claude Code. Consulta [Skills de agente](overview.md).

## Qué hace

`localize-campaign` toma un conjunto de vídeos, como los anuncios de una campaña, un curso o vídeos de producto, y produce cada uno de ellos en cada idioma de destino. Asigna idiomas a tus mercados, organiza la matriz de vídeos por idioma, estima el coste total, hace un piloto con una versión para revisar pronto nombres y términos y después ejecuta el resto. Recibes archivos con nombres coherentes y un `review.csv` con el que los equipos regionales pueden dar su visto bueno.

## Cuándo usarla

| Lo que tienes | Usa |
| --- | --- |
| Varios vídeos, varios mercados o idiomas | `localize-campaign` |
| Un vídeo a unos pocos idiomas | [translate-and-dub](translate-and-dub.md) |
| Muchos vídeos con una nueva locución en el mismo idioma | [batch-lipsync](batch-lipsync.md) |

## Prueba

- «El mes que viene lanzamos en DACH, Brasil y Japón. Localiza estos tres anuncios.»
- «Haz nuestros cinco vídeos de onboarding en español, francés e italiano»

## Qué necesitas

- El servidor MCP de sync. conectado o `SYNC_API_KEY` definida. La skill [setup](setup.md) te guía con cualquiera de las dos opciones.
- Los vídeos originales, cada uno con su locución original.

## Preguntas frecuentes

**Le di mercados, no idiomas.**
Es lo esperado. El agente los asigna (DACH a alemán, Brasil a portugués, Japón a japonés) y te pide que lo confirmes antes de estimar el coste.

**¿Por qué primero un piloto?**
Un nombre de producto o un eslogan mal traducido se repetiría en todas las versiones. Una versión, revisada por ti o por un hablante nativo, lo detecta por el precio de un solo doblaje.

**¿Qué no cambia?**
El texto en pantalla, los subtítulos incrustados, los logotipos y las cartelas finales se quedan en el idioma original. El agente te lo dice desde el principio para que nadie se sorprenda en la revisión.

**¿Cómo se llaman los archivos?**
`<campaign>_<video>_<lang>.mp4` por defecto, por ejemplo `spring24_hero-30s_de.mp4`. Si necesitas otro patrón, acuérdalo antes de la ejecución.

**¿Puede ejecutar las versiones juntas?**
Sí. Tras el piloto, el resto de versiones arrancan juntas, hasta el límite de tu plan, con una sola llamada a `jobs_create-many` desde el servidor MCP, en cualquier plan de pago.

**La ejecución se interrumpió.**
Cada versión tiene su propia clave guardada y su ID de generación, así que al reanudar continúa donde se detuvo sin pagar dos veces.

## Funciona si

- Confirmas la asignación de mercados a idiomas y la matriz antes de cualquier coste.
- El piloto llega antes de que empiece el resto.
- Terminas con un archivo por vídeo e idioma, más una hoja de revisión.
