---
title: "Skill ai-video-to-talking"
subtitle: "Dê falas a clipes gerados por IA no Veo, Kling, Sora e outros."
description: "A skill de agente ai-video-to-talking da sync. labs dá falas a vídeos gerados por IA no Veo, Kling, Sora, Runway e outros geradores, escolhe uma voz adequada e sincroniza os lábios do personagem, inclusive em cenas com vários planos."
og:description: "Faça personagens de vídeos gerados por IA dizerem as suas falas, incluindo cenas com vários planos e dois personagens."
source-sha256: 2da61aa54d453eba92f1fa339fa9da3fa171c87d410601398b6427170f09c5bd
---

# ai-video-to-talking

> [!TIP]
> Instale esta skill com `npx skills add synchronicity-labs/skills --skill ai-video-to-talking`, ou obtenha todas as skills com o plugin do Claude Code. Veja [Skills de agente](overview.md).

## O que faz

A `ai-video-to-talking` dá falas a vídeos gerados por IA. Clipes do Veo, Kling, Sora, Runway, Hailuo, Luma, Seedance ou Wan costumam vir sem som ou com uma fala que você não quer. Esta skill escreve a fala ou usa a sua, escolhe uma voz que combina com o personagem e sincroniza os lábios para que ele fale de verdade.

A sync. não gera o vídeo. Se você só tem uma ideia, a skill escreve um prompt para o seu gerador de vídeo que produz um clipe fácil de sincronizar e assume a partir do momento em que você o tiver.

## Quando usar

| O que você tem | Use |
| --- | --- |
| Um clipe gerado, ou uma ideia para um | `ai-video-to-talking` |
| Imagens reais e uma narração | [lipsync](lipsync.md) |
| Uma imagem estática | [talking-photo](talking-photo.md) |

## Experimente

- “Meu clipe do Veo de uma barista não tem diálogo. Faça ela dizer: bom dia, latte de aveia de novo?”
- “Preciso de um anúncio estilo UGC em que um cara segura nosso energético e diz que é gostoso. Vou fazer o clipe no Kling.”
- “Esta cena do Sora tem dois personagens conversando. Dê estas falas a eles.”

## O que você precisa

- O servidor MCP da sync. conectado ou `SYNC_API_KEY` definida. A skill [setup](setup.md) orienta você em qualquer uma das opções.
- O clipe, ou acesso a um gerador de vídeo.
- A fala, ou uma descrição do que o personagem deve dizer.

## Perguntas frequentes

**O que faz um clipe gerado sincronizar bem?**
Um único personagem de frente para a câmera, o rosto ocupando boa parte do quadro, a boca desobstruída, a câmera estável, um único plano contínuo e o personagem já se movendo como se estivesse falando. O guia de prompts da skill explica isso, com um prompt de exemplo.

**Minha fala é mais longa que o clipe.**
Clipes gerados costumam ter de 5 a 10 segundos, o que comporta cerca de 12 a 25 palavras. A skill sugere encurtar a fala, gerar um clipe mais longo ou usar um [modo de sincronização](https://sync.so/docs/developer-guides/sync-mode) que estende o vídeo.

**Ela consegue lidar com dois personagens ou vários planos?**
Sim, com a ferramenta de timeline. Cada fala recebe sua própria voz e é posicionada no plano em que aquele personagem fala. As falas, as vozes e o custo total são combinados antes de qualquer criação.

**Posso usar minha própria voz?**
Sim, grave e envie o áudio. A skill também pode clonar uma voz, mas só quando você pede e a amostra é sua. A clonagem salva uma voz na sua conta uma única vez; se a resposta se perder, a skill confere sua lista de vozes antes de tentar de novo.

## Está funcionando se

- O personagem diz exatamente as suas palavras, com uma voz que combina com ele.
- Nada é gerado antes de você aprovar a fala, a voz e o custo.
- Em uma cena com vários planos, cada fala cai no personagem certo.
