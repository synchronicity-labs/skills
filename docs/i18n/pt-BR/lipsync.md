---
title: "Skill lipsync"
subtitle: "Sincronize os lábios de um vídeo com um novo áudio ou um roteiro digitado."
description: "A skill de agente lipsync da sync. labs faz uma pessoa em um vídeo acompanhar uma nova fala: uma narração, uma tomada regravada, uma música ou um roteiro que a sync. narra. Ela informa o custo e espera a aprovação antes."
og:description: "Sincronize os lábios de um vídeo de uma pessoa real com um novo áudio ou um roteiro digitado a partir do seu agente, com uma estimativa antes de qualquer geração."
source-sha256: 58edce026081002df42de0999296238a3f949e65c29651b4a6a39fe8a9bac0f3
---

# lipsync

> [!TIP]
> Instale esta skill com `npx skills add synchronicity-labs/skills --skill lipsync`, ou obtenha todas as skills com o plugin do Claude Code. Veja [Skills de agente](overview.md).

## O que faz

A `lipsync` pega um vídeo de alguém falando e faz a boca da pessoa acompanhar uma nova fala. A fala pode ser uma narração, uma tomada regravada, uma música ou um roteiro que a sync. narra para você. Você recebe um único MP4, com a imagem original e o novo áudio.

Antes de qualquer cobrança, o agente salva seus arquivos na sync., calcula a duração da fala, informa o custo e espera o seu sinal verde.

## Quando usar

Use quando você já tem imagens de uma pessoa real e quer que ela diga outra coisa.

| O que você tem | Use |
| --- | --- |
| Um vídeo e um novo áudio, ou um vídeo e um roteiro | `lipsync` |
| Um clipe do Veo, Kling, Sora ou de outro gerador | [ai-video-to-talking](ai-video-to-talking.md) |
| Uma foto ou ilustração | [talking-photo](talking-photo.md) |
| Um vídeo que deve falar outro idioma | [translate-and-dub](translate-and-dub.md) |
| Uma ou duas palavras erradas em uma tomada que, fora isso, está boa | [edit-dialogue](edit-dialogue.md) |
| Dezenas de vídeos ou arquivos de áudio | [batch-lipsync](batch-lipsync.md) |

## Experimente

- “Sincronize os lábios de ./interview.mp4 com ./new-take.wav”
- “Faça o cara de https://example.com/talk.mp4 dizer o que está neste mp3”
- “Sincronize meu clipe musical ./take3.mov com a mixagem final”

## O que você precisa

- O servidor MCP da sync. conectado ou `SYNC_API_KEY` definida. A skill [setup](setup.md) orienta você em qualquer uma das opções.
- O vídeo como arquivo local, URL pública, ID de asset da sync. ou link do YouTube, TikTok, Instagram ou Facebook.
- A fala como áudio, ou como roteiro mais uma voz.

## Perguntas frequentes

**Por que parou para me perguntar antes de criar o vídeo?**
Toda geração é cobrada, então a skill sempre mostra a estimativa primeiro e espera a aprovação. Diga logo de início “pode seguir, qualquer coisa abaixo de $5 está ok” e ela não vai parar duas vezes.

**Meu áudio é mais longo que o vídeo. O que acontece?**
O agente pergunta qual [modo de sincronização](https://sync.so/docs/developer-guides/sync-mode) você quer: reproduzir o vídeo para frente e para trás (`bounce`, o padrão), repeti-lo em loop, cortar a fala quando o vídeo termina, continuar o vídeo em silêncio ou acelerar ou desacelerar o vídeo para caber (`remap`).

**Há duas pessoas na cena.**
O agente pergunta quem deve falar e direciona a sync. para esse rosto. Sem essa indicação, a sync. escolhe sozinha quem está falando.

**Ela se recusou a enviar meu arquivo.**
Ela verifica se o arquivo é mesmo uma mídia antes de gastar qualquer coisa. Um arquivo que não é vídeo nem áudio, ou um endereço de upload que não é da própria sync., interrompe a execução com uma explicação. Nada é cobrado.

**Qual modelo ela usa?**
O `sync-3`, o modelo mais avançado, a menos que você peça outro. A lista vem da sua conta, não da skill.

**Cadê meu vídeo?**
O agente passa o link exato do resultado. Em um agente de programação, ele se oferece para baixar o arquivo ao lado do seu original.

## Está funcionando se

- Você vê uma estimativa antes de qualquer geração começar.
- Os arquivos locais são enviados uma única vez, e uma nova tentativa reutiliza o mesmo upload.
- A mensagem final traz um link que reproduz seu vídeo com a nova fala.
