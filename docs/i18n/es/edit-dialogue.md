---
title: "Skill edit-dialogue"
subtitle: "Cambia o elimina algunas palabras habladas con la propia voz de quien habla."
description: "La skill de agente edit-dialogue de sync. labs corrige algunas palabras habladas en un vídeo con un solo hablante sin volver a grabar: transcribe, te deja escuchar las palabras nuevas con la propia voz de quien habla y vuelve a sincronizar los labios solo en esa parte."
og:description: "Corrige un precio, un nombre, una fecha o una palabra equivocados en un vídeo, con la propia voz de quien habla y sin volver a grabar."
source-sha256: e600a9398994cc8954d04bcfe97d32f8830b99c91552aa7b7db8ccc11762a46e
---

# edit-dialogue

> [!TIP]
> Instala esta skill con `npx skills add synchronicity-labs/skills --skill edit-dialogue`, o consigue todas las skills con el plugin de Claude Code. Consulta [Skills de agente](overview.md).

## Qué hace

`edit-dialogue` corrige algunas palabras habladas en un vídeo sin volver a grabar. Transcribe el vídeo, relaciona tu corrección con las palabras exactas, sintetiza las palabras nuevas con la propia voz de quien habla, te deja escuchar una vista previa y después vuelve a sincronizar los labios solo en esa parte. Todo lo demás conserva la imagen y el sonido originales.

## Cuándo usarla

| Lo que tienes | Usa |
| --- | --- |
| Un precio, un nombre, una fecha o una palabra equivocados, o una muletilla que quitar | `edit-dialogue` |
| Un guion completamente nuevo | [lipsync](lipsync.md) con una voz elegida |
| El mismo vídeo en otro idioma | [translate-and-dub](translate-and-dub.md) |
| Una grabación personalizada para cada destinatario | `edit-dialogue`, una vista previa y un vídeo por destinatario |

## Prueba

- «En ./promo.mp4 digo $39 al mes. Ahora son $49, corrige solo eso.»
- «Quita el “eh” después de “facturación anual” en este vídeo»
- «El nombre debería ser Siobhan, no Shannon»

## Qué necesitas

- El servidor MCP de sync. conectado. La skill [setup](setup.md) te guía en el proceso. La versión REST de este flujo está en acceso anticipado; consulta [Transcription and Dialogue Editing](https://sync.so/docs/developer-guides/dialogue-editing).
- Un vídeo con un solo hablante, de hasta 10 minutos.

## Preguntas frecuentes

**¿Por qué me enseña la transcripción?**
Para que los dos podáis señalar las mismas palabras. Cada cambio y cada eliminación se vinculan a una palabra de la transcripción, lo que mantiene la edición exacta.

**¿La vista previa cuesta dinero?**
Puede que sí. La vista previa clona la voz de quien habla y sintetiza las palabras nuevas, así que el agente lo menciona al confirmar los cambios. El vídeo final se estima por separado antes de crearlo.

**Un nombre ha salido mal.**
Pide una pronunciación. El agente añade una reescritura fonética como «shivawn», escrita como una palabra normal, y crea una vista previa nueva.

**Algunos cambios han fallado.**
Normalmente el texto nuevo es demasiado largo para el hueco que ocupa. El agente te dice qué cambios fallaron y te sugiere un texto más corto.

**¿Puede hacer una versión por destinatario?**
Sí. Acuerdas las ediciones de cada destinatario en una sola tabla, las vistas previas arrancan juntas y, tras una única aprobación del total, los vídeos también arrancan juntos, hasta el límite de tu plan. El MCP usa una llamada a `jobs_create-many` para los previews y otra para los vídeos, en cualquier plan de pago. Los renders en cola de la Batch API requieren aprobación explícita de la organización y un plan Scale o superior, incluso para pruebas en seco. El acceso está desactivado por defecto. Contacta con support@sync.so para solicitar aprobación. Los usuarios y administradores de la organización no pueden activarlo por su cuenta. Las filas de edición de diálogo también necesitan su propia aprobación de acceso anticipado.

**¿Puedo sustituir un párrafo entero?**
Este flujo es para palabras concretas. Para un guion nuevo, lipsync con una voz es la mejor herramienta, y el agente te lo dirá.

## Funciona si

- En el audio de la vista previa solo cambian tus palabras.
- Apruebas la vista previa y el coste antes de que se cree el vídeo.
- El resultado reproduce el vídeo original con solo esas palabras distintas.
