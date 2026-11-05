---
title: "Skill translate-and-dub"
subtitle: "Dobla un vídeo a otros idiomas con los labios sincronizados."
description: "La skill de agente translate-and-dub de sync. labs traduce la locución de un vídeo a otros idiomas y vuelve a sincronizar los labios de quien habla, a partir de un archivo local, una URL o un enlace de YouTube, TikTok, Instagram o Facebook."
og:description: "Dobla un vídeo a otros idiomas con los labios sincronizados desde tu agente, con una estimación por idioma antes de empezar."
source-sha256: 3de39f1f8e5d6a108573d5c543d10e7380a08881c78f0209706b1e7bf1f1108f
---

# translate-and-dub

> [!TIP]
> Instala esta skill con `npx skills add synchronicity-labs/skills --skill translate-and-dub`, o consigue todas las skills con el plugin de Claude Code. Consulta [Skills de agente](overview.md).

## Qué hace

`translate-and-dub` traduce la locución de un vídeo a otros idiomas y vuelve a sincronizar los labios de quien habla con el audio doblado. Recibes un MP4 por idioma, etiquetado con su idioma. Funciona con un archivo local, una URL pública o un enlace de YouTube, TikTok, Instagram o Facebook.

## Cuándo usarla

| Lo que tienes | Usa |
| --- | --- |
| Un vídeo, uno o varios idiomas | `translate-and-dub` |
| Varios vídeos para varios mercados | [localize-campaign](localize-campaign.md) |
| Un vídeo y tu propio audio traducido | [lipsync](lipsync.md) |
| Solo subtítulos | No es un trabajo para sync. |

## Prueba

- «Dobla este vídeo de YouTube al español y al portugués de Brasil»
- «Traduce ./keynote.mp4 al japonés»
- «Haz de https://example.com/demo.mp4 una versión en alemán»

## Qué necesitas

- El servidor MCP de sync. conectado o `SYNC_API_KEY` definida. La skill [setup](setup.md) te guía con cualquiera de las dos opciones.
- Un vídeo con su locución original en la pista de audio.

## Preguntas frecuentes

**¿Qué idiomas se admiten?**
El agente consulta la lista actualizada antes de estimar el coste. Si un idioma no está, te indica el más parecido que sí está.

**¿Cómo se calcula el precio?**
Por la duración del vídeo original, una vez por idioma. La estimación muestra el desglose por idioma y el total. Si no incluye los cargos de un proveedor de voz externo, el agente te lo indica.

**¿Se traduce el texto que aparece en pantalla?**
No. Los títulos, los subtítulos incrustados y los logotipos se quedan como están. Solo cambia la locución.

**Ha fallado un idioma.**
Cada idioma es un trabajo independiente, así que los demás terminan igualmente. El agente te dice cuál falló y por qué.

**El doblaje falló con un error del proveedor de voz.**
Si conectaste tu propia clave de ElevenLabs a sync., la causa habitual son los créditos o la validez de esa clave.

**No quiso doblar un videoclip.**
Las canciones y los videoclips protegidos por derechos de autor necesitan el permiso del titular de los derechos. Usa un vídeo que sea tuyo o que tengas licencia para localizar.

## Funciona si

- Los idiomas se comprueban antes de la estimación.
- Hay un trabajo de pago por idioma y nunca se reenvía para consultar el progreso.
- Cada enlace de resultado está etiquetado con su idioma.
