---
title: "Skill sync-api"
subtitle: "Integre a sync. a apps com a API REST ou os SDKs de Python e TypeScript."
description: "A skill de agente sync-api da sync. labs ajuda o seu agente de programação a integrar a sync. a um app, backend, script ou pipeline: uploads, gerações com chaves de idempotência, webhooks verificados, polling, erros e limites de concorrência."
og:description: "Faça o seu agente de programação escrever integrações da sync. no servidor com chaves de idempotência, webhooks verificados e tratamento correto de 429."
source-sha256: 1b2d510001c97cc2617187e1c85cdcf498c6d4b091c3c10d9d2b1d7dee9e4193
---

# sync-api

> [!TIP]
> Instale esta skill com `npx skills add synchronicity-labs/skills --skill sync-api`, ou obtenha todas as skills com o plugin do Claude Code. Veja [Skills de agente](overview.md).

## O que faz

A `sync-api` ajuda o seu agente de programação a integrar a sync. ao seu próprio app, backend, script ou pipeline. Ela escreve código de servidor que envia mídias, cria gerações com chaves de idempotência, verifica webhooks, faz polling como alternativa e trata erros e limites de concorrência, usando a API REST ou os [SDKs](https://sync.so/docs/developer-guides/sdk) oficiais de Python (`syncsdk`) e TypeScript (`@sync.so/sdk`).

## Quando usar

| O que você está fazendo | Use |
| --- | --- |
| Escrevendo ou revisando código que chama a API da sync. | `sync-api` |
| Depurando um 429, um webhook ou uma cobrança duplicada | `sync-api` |
| Criando um vídeo neste chat | [lipsync](lipsync.md), [talking-photo](talking-photo.md), [translate-and-dub](translate-and-dub.md) |
| Rodando um CSV de trabalhos uma única vez | [batch-lipsync](batch-lipsync.md) |

## Experimente

- “Adicione ao meu app Express um endpoint que sincroniza os lábios de uma URL de vídeo com uma URL de áudio usando a sync.”
- “Escreva um script Python que duble em espanhol cada vídeo de ./in”
- “Adicione uma rota Next.js que verifique os webhooks da sync.”
- “Nosso worker continua recebendo 429 concurrency_limit_reached. Qual é a correção certa?”

## O que você precisa

- Uma chave de API da sync. em [sync.so/settings/api-keys](https://sync.so/settings/api-keys), definida como `SYNC_API_KEY` no servidor. Veja [Autenticação](https://sync.so/docs/api-reference/guides/authentication).
- Python 3.8 ou posterior, ou Node 18 ou posterior, para os SDKs.

## Perguntas frequentes

**Por que o código salva uma chave antes de chamar a API?**
`POST /v2/generate` aceita um `Idempotency-Key`. Criado uma vez por trabalho e reutilizado em cada nova tentativa, ele transforma uma nova tentativa após um timeout em uma repetição da geração original, em vez de uma segunda geração paga. Veja [Idempotent Requests](https://sync.so/docs/api-reference/guides/idempotency).

**Webhooks ou polling?**
[Webhooks](https://sync.so/docs/api-reference/guides/webhooks), verificados com o cabeçalho `Sync-Signature`, para produção. Uma consulta periódica pega as entregas que o seu endpoint perdeu.

**O SDK não tem um campo que a documentação menciona.**
Os SDKs podem ficar atrás da API. A skill chama esse endpoint por HTTP em vez de forçar os tipos.

**O que fazer com um 429?**
Espere o tempo que a resposta indica, tente de novo com a mesma chave de idempotência e mantenha no máximo o limite de concorrência do seu plano em trabalhos em andamento, com uma fila do seu lado. Veja [Concorrência e limites de taxa](https://sync.so/docs/api-reference/guides/rate-limits).

**Quem pode criar um batch em fila?**
A Batch API exige aprovação explícita da organização e o plano Scale ou superior, inclusive para simulações. O acesso fica desativado por padrão. Sem aprovação, a criação retorna `403 batch_access_not_enabled` antes de verificar o plano. Fale com support@sync.so para solicitar aprovação. Usuários e administradores da organização não podem ativar o acesso. Depois da aprovação, um plano abaixo de Scale retorna `402 plan_feature_unavailable`. Jobs existentes, status de batch e resultados continuam disponíveis. Requisições normais dentro da concorrência do plano e `jobs_create-many` do MCP continuam disponíveis em qualquer plano pago.

## Está funcionando se

- A chave de API fica no servidor, nunca em código de navegador ou de app móvel.
- Cada criação leva uma chave de idempotência que foi salva antes da chamada.
- O handler de webhooks confere a assinatura com o corpo bruto antes de fazer o parse.
