---
title: "Skill talking-photo"
subtitle: "Haz hablar a una foto, un retrato o un personaje."
description: "La skill de agente talking-photo de sync. labs convierte una foto, un retrato o un personaje ilustrado en un vídeo que habla a partir de un guion o una grabación, con una voz elegida de tu cuenta y una estimación antes de crear nada."
og:description: "Convierte una foto, un retrato o un personaje ilustrado en un vídeo que habla desde tu agente."
source-sha256: 6aeeae5c018d350384c8f655da3d437d6aa76de342cb9d799b6880c5bf405d61
---

# talking-photo

> [!TIP]
> Instala esta skill con `npx skills add synchronicity-labs/skills --skill talking-photo`, o consigue todas las skills con el plugin de Claude Code. Consulta [Skills de agente](overview.md).

## Qué hace

`talking-photo` convierte una imagen fija en un vídeo que habla. Dale una foto, un retrato o un personaje ilustrado, junto con un guion o una grabación, y te devuelve un MP4 de esa cara hablando. El vídeo dura lo mismo que la locución.

Si aún no tienes imagen y tu agente puede generar imágenes, se ofrece a crear una que funcione bien: una sola cara clara, mirando a cámara, de cabeza y hombros.

## Cuándo usarla

| Lo que tienes | Usa |
| --- | --- |
| Una foto, un retrato o un personaje ilustrado | `talking-photo` |
| Un vídeo de una persona real | [lipsync](lipsync.md) |
| Un clip de vídeo generado | [ai-video-to-talking](ai-video-to-talking.md) |

## Prueba

- «Haz que el retrato de nuestra CEO diga: bienvenido a Acme, nos alegra que estés aquí»
- «Crea una barista de dibujos animados simpática y haz que diga buenos días»
- «Haz que ./portrait.png diga lo que hay en ./greeting.mp3»

## Qué necesitas

- El servidor MCP de sync. conectado o `SYNC_API_KEY` definida. La skill [setup](setup.md) te guía con cualquiera de las dos opciones.
- Una imagen con una sola cara humana o de aspecto humano bien clara. No se admiten animales ni personajes no humanoides.
- Un guion, o un archivo de audio, una URL o un asset de sync.

## Preguntas frecuentes

**¿Puede elegir la voz por mí?**
Sí. Muestra las voces de tu cuenta y sugiere dos o tres que encajan con el personaje. Di «elige tú» y la escoge.

**¿Por qué la estimación es «aproximada»?**
Con un guion, la duración de la locución se estima a partir del número de palabras hasta que se genera la voz. La síntesis de voz se factura aparte del lipsync, y el agente te lo indica.

**Mi imagen fue rechazada.**
sync. necesita una sola cara clara y de un tamaño razonable. Las fotos de grupo, las caras diminutas y los perfiles son las causas habituales. El agente te explica cuál es y te sugiere un encuadre más cerrado de cabeza y hombros.

**¿Puedo hacer que una celebridad diga algo?**
No. La skill se niega a poner palabras en boca de una persona real e identificable para engañar. Tus propias fotos, tu equipo (con su permiso) y los personajes ficticios no tienen problema.

## Funciona si

- El agente elige una voz de la lista de tu cuenta, no un ID inventado.
- Ves la estimación antes de que se cree el vídeo.
- El resultado es un único MP4 de la cara diciendo exactamente tus palabras.
