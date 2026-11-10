---
title: "Skill batch-lipsync"
subtitle: "Sincronize os lábios de cada linha de um CSV ou pasta, com retomada, dentro dos limites do seu plano. Batches em fila exigem aprovação da organização e o plano Scale ou superior."
description: "A skill de agente batch-lipsync da sync. labs sincroniza os lábios de muitos vídeos de uma vez a partir de um CSV, planilha, pasta ou lista: ela estima o custo da execução inteira, oferece um piloto, respeita a concorrência do seu plano e retoma sem pagar duas vezes."
og:description: "Sincronize os lábios de cada linha de um CSV ou pasta a partir do seu agente, com retomada, dentro dos limites do seu plano. Batches em fila exigem aprovação da organização e o plano Scale ou superior."
source-sha256: 88b105777897ba2ccc422d0ae150405831fcb548f0979660ae8d98f556b64469
---

# batch-lipsync

> [!TIP]
> Instale esta skill com `npx skills add synchronicity-labs/skills --skill batch-lipsync`, ou obtenha todas as skills com o plugin do Claude Code. Veja [Skills de agente](overview.md).

## O que faz

A `batch-lipsync` sincroniza os lábios de muitos vídeos de uma vez: um resultado por linha de um CSV, uma planilha, uma pasta ou uma lista como “este apresentador com cada um destes 40 arquivos de áudio”. Ela cria um manifesto, estima o custo da execução inteira, oferece um piloto, depois processa cada linha dentro dos limites do seu plano e reúne os resultados em uma tabela.

Com uma chave de API, ela usa um script incluído, `sync_batch.py`, que envia cada arquivo uma única vez, respeita a concorrência do seu plano, retoma após uma interrupção e baixa todos os resultados. Pelo servidor MCP da sync., ela inicia todas as linhas com uma única chamada a `jobs_create-many`, que respeita a concorrência do seu plano, e acompanha todas com `jobs_get-many`. Quando essas ferramentas não aparecem, ela inicia uma geração por linha.

Com aprovação da organização e o plano Scale ou superior, uma execução grande de 20 a 500 linhas curtas que pode esperar horas pode usar a [Batch API](https://sync.so/docs/api-reference/guides/batch-processing), com o script ou as ferramentas de batch do servidor MCP. O acesso fica desativado por padrão, inclusive para simulações. Fale com support@sync.so para solicitar aprovação. Usuários e administradores da organização não podem ativá-lo por conta própria.

## Quando usar

| O que você tem | Use |
| --- | --- |
| Muitas linhas de vídeo com áudio ou roteiro | `batch-lipsync` |
| Um vídeo personalizado por lead ou cliente | `batch-lipsync` |
| Uma gravação personalizada com o nome de cada destinatário na mesma voz | [edit-dialogue](edit-dialogue.md) |
| Vários vídeos em outros idiomas | [localize-campaign](localize-campaign.md) |
| Um único vídeo | [lipsync](lipsync.md) |

## Experimente

- “Sincronize cada linha de leads.csv em presenter.mp4”
- “Faça uma versão deste anúncio para cada uma destas 12 narrações”
- “Rode manifest.csv na sync, o total está aprovado”

## O que você precisa

- O servidor MCP da sync. conectado, ou `SYNC_API_KEY` e Python 3.9 ou posterior para o script. A skill [setup](setup.md) orienta você em qualquer uma das opções.
- Uma lista em que cada linha tenha um vídeo ou uma imagem, e um áudio ou um roteiro com uma voz.

## Perguntas frequentes

**Por que ela quer um piloto?**
Se uma entrada compartilhada estiver errada, como a voz ou o enquadramento do apresentador, um piloto custa duas gerações em vez de duzentas.

**O que sai da minha máquina?**
As mídias, os roteiros, os nomes de arquivo e os IDs das linhas (usados como nomes dos resultados). As colunas que a execução não usa ficam no seu computador, então não coloque nomes nem e-mails nos IDs das linhas.

**Ela parou no meio.**
Execute o mesmo comando de novo. As linhas concluídas são puladas, as enviadas são consultadas em vez de reenviadas, e nada que já foi pago é pago de novo.

**Mudei uma linha depois que ela rodou.**
O script se recusa a reutilizar o resultado dessa linha. Dê um novo ID à linha alterada, o que a transforma em uma nova geração.

**Ela inicia as linhas uma de cada vez?**
Não. Você aprova a execução inteira uma vez, e depois as linhas começam juntas, tantas ao mesmo tempo quanto o seu plano processa. Pelo servidor MCP, isso é uma chamada a `jobs_create-many` a cada 50 linhas, em qualquer plano pago, e as linhas que precisam esperar uma vaga livre começam assim que as anteriores terminam.

**Devo usar a Batch API?**
Use somente com aprovação da organização e o plano Scale ou superior, para uma execução grande de 20 a 500 linhas curtas, cada uma com até 30 segundos, quando um prazo de horas funciona para você. A simulação exige o mesmo acesso. Sem aprovação, a criação retorna `403 batch_access_not_enabled` antes de verificar o plano. Fale com support@sync.so para solicitar aprovação. Depois da aprovação, um plano abaixo de Scale retorna `402 plan_feature_unavailable`. Use a execução normal enquanto o acesso não estiver disponível. `jobs_create-many` continua disponível em qualquer plano pago, dentro da concorrência do plano. Jobs existentes, status e resultados continuam disponíveis.

**Algumas linhas falharam.**
A tabela de resultados lista cada falha com o motivo. Linhas que falharam por entrada inválida precisam de uma entrada corrigida. Tente as demais de novo com `--retry-failed`.

## Está funcionando se

- A estimativa cobre todas as linhas ou informa quais linhas não conseguiu precificar.
- Depois de uma única aprovação, as linhas começam juntas em vez de uma a uma.
- Nunca rodam ao mesmo tempo mais gerações do que o seu plano permite.
- Rodar de novo um manifesto concluído não cria nada novo.
