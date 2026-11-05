---
title: "Skill ai-video-to-talking"
subtitle: "Pon diálogo en clips generados con IA en Veo, Kling, Sora y otros."
description: "La skill de agente ai-video-to-talking de sync. labs pone diálogo en vídeos generados con IA en Veo, Kling, Sora, Runway y otros generadores, elige una voz adecuada y sincroniza los labios del personaje, incluso en escenas con varios planos."
og:description: "Haz que los personajes de vídeos generados con IA digan tus frases, incluidas escenas con varios planos y dos personajes."
source-sha256: 2da61aa54d453eba92f1fa339fa9da3fa171c87d410601398b6427170f09c5bd
---

# ai-video-to-talking

> [!TIP]
> Instala esta skill con `npx skills add synchronicity-labs/skills --skill ai-video-to-talking`, o consigue todas las skills con el plugin de Claude Code. Consulta [Skills de agente](overview.md).

## Qué hace

`ai-video-to-talking` pone diálogo en vídeos generados con IA. Los clips de Veo, Kling, Sora, Runway, Hailuo, Luma, Seedance o Wan suelen salir mudos o con una locución que no quieres. Esta skill escribe la frase o usa la tuya, elige una voz que encaje con el personaje y le sincroniza los labios para que hable de verdad.

sync. no genera el vídeo. Si solo tienes una idea, la skill escribe un prompt para tu generador de vídeo que produzca un clip que se sincronice bien, y continúa en cuanto lo tengas.

## Cuándo usarla

| Lo que tienes | Usa |
| --- | --- |
| Un clip generado, o una idea para uno | `ai-video-to-talking` |
| Imágenes reales y una voz en off | [lipsync](lipsync.md) |
| Una imagen fija | [talking-photo](talking-photo.md) |

## Prueba

- «Mi clip de Veo de una barista no tiene diálogo. Haz que diga: buenos días, ¿otra vez latte de avena?»
- «Necesito un anuncio estilo UGC en el que un chico sostiene nuestra bebida energética y dice que está buena. Haré el clip en Kling.»
- «Esta escena de Sora tiene dos personajes hablando. Dales estas frases.»

## Qué necesitas

- El servidor MCP de sync. conectado o `SYNC_API_KEY` definida. La skill [setup](setup.md) te guía con cualquiera de las dos opciones.
- El clip, o acceso a un generador de vídeo.
- La frase, o una descripción de lo que debe decir el personaje.

## Preguntas frecuentes

**¿Qué hace que un clip generado se sincronice bien?**
Un solo personaje de cara a la cámara, con la cara ocupando buena parte del encuadre, la boca despejada, la cámara estable, un único plano continuo y el personaje ya moviéndose como si hablara. La guía de prompts de la skill lo explica, con un prompt de ejemplo.

**Mi frase es más larga que el clip.**
Los clips generados suelen durar de 5 a 10 segundos, lo que da para unas 12 a 25 palabras. La skill te sugiere acortar la frase, generar un clip más largo o usar un [modo de sincronización](https://sync.so/docs/developer-guides/sync-mode) que alargue el vídeo.

**¿Puede con dos personajes o con varios planos?**
Sí, con la herramienta de línea de tiempo. Cada frase recibe su propia voz y se coloca en el plano donde habla ese personaje. Las frases, las voces y el coste total se acuerdan antes de crear nada.

**¿Puedo usar mi propia voz?**
Sí, grábala y pasa el audio. La skill también puede clonar una voz, pero solo cuando lo pides y la muestra es tuya. La clonación guarda la voz en tu cuenta una sola vez; si la respuesta se pierde, la skill revisa tu lista de voces antes de volver a intentarlo.

## Funciona si

- El personaje dice exactamente tus palabras, con una voz que le va.
- No se genera nada antes de que apruebes la frase, la voz y el coste.
- En una escena con varios planos, cada frase llega al personaje correcto.
