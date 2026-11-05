---
title: "Skill talking-photo"
subtitle: "Faça uma foto, um retrato ou um personagem falar."
description: "A skill de agente talking-photo da sync. labs transforma uma foto, um retrato ou um personagem ilustrado em um vídeo falado a partir de um roteiro ou de uma gravação, com uma voz escolhida da sua conta e uma estimativa antes de criar qualquer coisa."
og:description: "Transforme uma foto, um retrato ou um personagem ilustrado em um vídeo falado a partir do seu agente."
source-sha256: 6aeeae5c018d350384c8f655da3d437d6aa76de342cb9d799b6880c5bf405d61
---

# talking-photo

> [!TIP]
> Instale esta skill com `npx skills add synchronicity-labs/skills --skill talking-photo`, ou obtenha todas as skills com o plugin do Claude Code. Veja [Skills de agente](overview.md).

## O que faz

A `talking-photo` transforma uma imagem estática em um vídeo falado. Envie uma foto, um retrato ou um personagem ilustrado, junto com um roteiro ou uma gravação, e ela devolve um MP4 desse rosto falando. O vídeo tem a mesma duração da fala.

Se você ainda não tem uma imagem e o seu agente consegue gerar imagens, ele se oferece para criar uma que funcione bem: um único rosto nítido, olhando para a câmera, enquadrado da cabeça aos ombros.

## Quando usar

| O que você tem | Use |
| --- | --- |
| Uma foto, um retrato ou um personagem ilustrado | `talking-photo` |
| Um vídeo de uma pessoa real | [lipsync](lipsync.md) |
| Um clipe de vídeo gerado | [ai-video-to-talking](ai-video-to-talking.md) |

## Experimente

- “Faça o retrato da nossa CEO dizer: bem-vindo à Acme, que bom ter você aqui”
- “Crie uma barista simpática em estilo cartoon e faça ela dizer bom dia”
- “Faça ./portrait.png dizer o que está em ./greeting.mp3”

## O que você precisa

- O servidor MCP da sync. conectado ou `SYNC_API_KEY` definida. A skill [setup](setup.md) orienta você em qualquer uma das opções.
- Uma imagem com um único rosto humano ou humanoide nítido. Animais e personagens não humanoides não são compatíveis.
- Um roteiro, ou um arquivo de áudio, uma URL ou um asset da sync.

## Perguntas frequentes

**Ela pode escolher a voz por mim?**
Sim. Ela lista as vozes da sua conta e sugere duas ou três que combinam com o personagem. Diga “escolha você mesma” e ela decide.

**Por que a estimativa é “aproximada”?**
Com um roteiro, a duração da fala é estimada pela contagem de palavras até que ela seja gerada. A síntese de voz é cobrada separadamente do lipsync, e o agente avisa isso.

**Minha imagem foi rejeitada.**
A sync. precisa de um único rosto nítido e de tamanho razoável. Fotos em grupo, rostos muito pequenos e perfis são as causas mais comuns. O agente explica qual é o caso e sugere um enquadramento mais fechado, da cabeça aos ombros.

**Posso fazer uma celebridade dizer algo?**
Não. A skill se recusa a colocar palavras na boca de uma pessoa real e identificável para enganar. Suas próprias fotos, sua equipe (com autorização) e personagens fictícios não têm problema.

## Está funcionando se

- O agente escolhe uma voz da lista da sua conta, não um ID inventado.
- Você vê a estimativa antes de o vídeo ser criado.
- O resultado é um único MP4 do rosto dizendo exatamente as suas palavras.
