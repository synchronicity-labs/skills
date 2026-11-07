---
title: "Skill translate-and-dub"
subtitle: "Duble um vídeo em outros idiomas com os lábios sincronizados."
description: "A skill de agente translate-and-dub da sync. labs traduz a fala de um vídeo para outros idiomas e ressincroniza os lábios de quem fala, a partir de um arquivo local, uma URL ou um link do YouTube, TikTok, Instagram ou Facebook."
og:description: "Duble um vídeo em outros idiomas com os lábios sincronizados a partir do seu agente, com uma estimativa por idioma antes."
source-sha256: 7f634da776bfe7c98f91c58950211d376361728413314e96ff125972692270bb
---

# translate-and-dub

> [!TIP]
> Instale esta skill com `npx skills add synchronicity-labs/skills --skill translate-and-dub`, ou obtenha todas as skills com o plugin do Claude Code. Veja [Skills de agente](overview.md).

## O que faz

A `translate-and-dub` traduz a fala de um vídeo para outros idiomas e ressincroniza os lábios de quem fala com o áudio dublado. Você recebe um MP4 por idioma, identificado com o idioma. Funciona a partir de um arquivo local, uma URL pública ou um link do YouTube, TikTok, Instagram ou Facebook.

## Quando usar

| O que você tem | Use |
| --- | --- |
| Um vídeo, um ou mais idiomas | `translate-and-dub` |
| Vários vídeos para vários mercados | [localize-campaign](localize-campaign.md) |
| Um vídeo e o seu próprio áudio traduzido | [lipsync](lipsync.md) |
| Só legendas | Não é um trabalho para a sync. |

## Experimente

- “Duble este vídeo do YouTube em espanhol e português do Brasil”
- “Traduza ./keynote.mp4 para japonês”
- “Faça de https://example.com/demo.mp4 uma versão em alemão”

## O que você precisa

- O servidor MCP da sync. conectado ou `SYNC_API_KEY` definida. A skill [setup](setup.md) orienta você em qualquer uma das opções.
- Um vídeo com a fala original na faixa de áudio.

## Perguntas frequentes

**Quais idiomas são compatíveis?**
O agente consulta a lista atualizada antes de estimar o custo. Se um idioma não estiver lá, ele indica o mais próximo disponível.

**Como é o preço?**
Pela duração do vídeo de origem, uma vez por idioma. A estimativa mostra o detalhamento por idioma e o total. Se as cobranças de um provedor de voz externo não estiverem incluídas, o agente avisa.

**O texto na tela é traduzido?**
Não. Títulos, legendas embutidas e logotipos ficam como estão. Só a fala muda.

**Os idiomas são dublados um depois do outro?**
Não. Depois de uma única aprovação, todos os idiomas começam juntos, até o limite do seu plano. Pelo servidor MCP, isso é uma única chamada a `jobs_create-many`.

**Um idioma falhou.**
Cada idioma é um trabalho separado, então os outros terminam normalmente. O agente informa qual falhou e por quê.

**A dublagem falhou com um erro do provedor de voz.**
Se você conectou sua própria chave da ElevenLabs à sync., os créditos ou a validade dessa chave costumam ser a causa.

**Ela não quis dublar um clipe musical.**
Músicas e clipes musicais protegidos por direitos autorais exigem a permissão do detentor dos direitos. Use um vídeo que seja seu ou que você tenha licença para localizar.

## Está funcionando se

- Os idiomas são verificados antes da estimativa.
- Há um trabalho pago por idioma, e nunca um reenvio para conferir o andamento.
- Cada link de resultado é identificado com o idioma.
