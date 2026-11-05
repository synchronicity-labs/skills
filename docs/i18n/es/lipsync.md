---
title: "Skill lipsync"
subtitle: "Sincroniza los labios de un vídeo con un audio nuevo o un guion escrito."
description: "La skill de agente lipsync de sync. labs hace que una persona de un vídeo coincida con una nueva locución: una voz en off, una toma regrabada, una canción o un guion al que sync. pone voz. Primero estima el coste y espera tu aprobación."
og:description: "Sincroniza los labios de un vídeo de una persona real con un audio nuevo o un guion escrito desde tu agente, con una estimación antes de cada generación."
source-sha256: 58edce026081002df42de0999296238a3f949e65c29651b4a6a39fe8a9bac0f3
---

# lipsync

> [!TIP]
> Instala esta skill con `npx skills add synchronicity-labs/skills --skill lipsync`, o consigue todas las skills con el plugin de Claude Code. Consulta [Skills de agente](overview.md).

## Qué hace

`lipsync` toma un vídeo de alguien hablando y hace que su boca coincida con una nueva locución. Puede ser una voz en off, una toma regrabada, una canción o un guion al que sync. pone voz por ti. Recibes un único MP4 con la imagen original y el audio nuevo.

Antes de cobrar nada, el agente guarda tus archivos en sync., calcula la duración de la locución, estima el coste y espera a que des luz verde.

## Cuándo usarla

Úsala cuando ya tienes imágenes de una persona real y quieres que diga otra cosa.

| Lo que tienes | Usa |
| --- | --- |
| Un vídeo y un audio nuevo, o un vídeo y un guion | `lipsync` |
| Un clip de Veo, Kling, Sora u otro generador | [ai-video-to-talking](ai-video-to-talking.md) |
| Una foto fija o una ilustración | [talking-photo](talking-photo.md) |
| Un vídeo que debe hablar otro idioma | [translate-and-dub](translate-and-dub.md) |
| Una o dos palabras incorrectas en una toma por lo demás buena | [edit-dialogue](edit-dialogue.md) |
| Decenas de vídeos o archivos de audio | [batch-lipsync](batch-lipsync.md) |

## Prueba

- «Sincroniza los labios de ./interview.mp4 con ./new-take.wav»
- «Haz que el chico de https://example.com/talk.mp4 diga lo que hay en este mp3»
- «Sincroniza mi videoclip ./take3.mov con la mezcla final»

## Qué necesitas

- El servidor MCP de sync. conectado o `SYNC_API_KEY` definida. La skill [setup](setup.md) te guía con cualquiera de las dos opciones.
- El vídeo como archivo local, URL pública, ID de asset de sync. o enlace de YouTube, TikTok, Instagram o Facebook.
- La locución como audio, o como guion más una voz.

## Preguntas frecuentes

**¿Por qué se detuvo a preguntarme antes de crear el vídeo?**
Cada generación se factura, así que la skill siempre muestra primero la estimación y espera tu aprobación. Di desde el principio «adelante, cualquier cosa por debajo de $5 me vale» y no se detendrá dos veces.

**Mi audio es más largo que mi vídeo. ¿Qué pasa?**
El agente te pregunta qué [modo de sincronización](https://sync.so/docs/developer-guides/sync-mode) quieres: reproducir el vídeo hacia delante y hacia atrás (`bounce`, el predeterminado), repetirlo en bucle, cortar la locución cuando termina el vídeo, mantener el vídeo en silencio o acelerarlo o ralentizarlo para que encaje (`remap`).

**Hay dos personas en el plano.**
El agente te pregunta quién debe hablar y dirige sync. a esa cara. Si no lo indicas, sync. elige por sí mismo al hablante activo.

**Se negó a subir mi archivo.**
Comprueba que el archivo sea realmente contenido multimedia antes de gastar nada. Un archivo que no es vídeo ni audio, o una dirección de subida que no es de sync., detiene la ejecución con una explicación. No se cobra nada.

**¿Qué modelo usa?**
`sync-3`, el modelo más capaz, salvo que pidas otro. La lista viene de tu cuenta, no de la skill.

**¿Dónde está mi vídeo?**
El agente te da el enlace exacto del resultado. En un agente de programación, se ofrece a descargar el archivo junto a tu original.

## Funciona si

- Ves una estimación antes de que empiece cualquier generación.
- Los archivos locales se suben una sola vez y un reintento reutiliza la misma subida.
- El mensaje final tiene un enlace que reproduce tu vídeo con la nueva locución.
