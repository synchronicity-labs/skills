---
title: "Skill localize-campaign"
subtitle: "Localize um conjunto de vídeos para vários mercados: plano, piloto, execução e planilha de revisão."
description: "A skill de agente localize-campaign da sync. labs produz cada vídeo de uma campanha, curso ou linha de produtos em cada idioma de destino: ela associa mercados a idiomas, estima o custo da matriz, faz um piloto com uma versão e depois executa o restante com uma planilha de revisão."
og:description: "Localize vários vídeos em vários idiomas a partir do seu agente, com um piloto primeiro e uma planilha de revisão no final."
source-sha256: 1da869421315f34ece2a880344bb9e5a1a6f20f02c65f76e84caa179ba54edb7
---

# localize-campaign

> [!TIP]
> Instale esta skill com `npx skills add synchronicity-labs/skills --skill localize-campaign`, ou obtenha todas as skills com o plugin do Claude Code. Veja [Skills de agente](overview.md).

## O que faz

A `localize-campaign` pega um conjunto de vídeos, como os anúncios de uma campanha, um curso ou vídeos de produto, e produz cada um deles em cada idioma de destino. Ela associa seus mercados a idiomas, monta a matriz de vídeos por idioma, estima o custo total, faz um piloto com uma versão para que nomes e termos sejam conferidos cedo e depois executa o restante. Você recebe arquivos com nomes consistentes e um `review.csv` que as equipes regionais podem usar para aprovar.

## Quando usar

| O que você tem | Use |
| --- | --- |
| Vários vídeos, vários mercados ou idiomas | `localize-campaign` |
| Um vídeo em alguns idiomas | [translate-and-dub](translate-and-dub.md) |
| Muitos vídeos com nova fala no mesmo idioma | [batch-lipsync](batch-lipsync.md) |

## Experimente

- “Vamos lançar na região DACH, no Brasil e no Japão no mês que vem. Localize estes três anúncios.”
- “Faça nossos cinco vídeos de onboarding em espanhol, francês e italiano”

## O que você precisa

- O servidor MCP da sync. conectado ou `SYNC_API_KEY` definida. A skill [setup](setup.md) orienta você em qualquer uma das opções.
- Os vídeos de origem, cada um com sua fala original.

## Perguntas frequentes

**Eu passei mercados, não idiomas.**
É o esperado. O agente faz a associação (DACH para alemão, Brasil para português, Japão para japonês) e pede sua confirmação antes de estimar o custo.

**Por que um piloto primeiro?**
Um nome de produto ou slogan mal traduzido se repetiria em todas as versões. Uma versão, conferida por você ou por um falante nativo, pega o problema pelo preço de uma única dublagem.

**O que não muda?**
Texto na tela, legendas embutidas, logotipos e cartelas finais ficam no idioma de origem. O agente avisa logo de início para que ninguém se surpreenda na revisão.

**Como os arquivos são nomeados?**
`<campaign>_<video>_<lang>.mp4` por padrão, por exemplo `spring24_hero-30s_de.mp4`. Combine outro padrão antes da execução, se precisar.

**Dá para rodar tudo em um único batch?**
Não é preciso. Depois do piloto, as demais versões começam juntas, até o limite do seu plano, com uma única chamada a `jobs_create-many` pelo servidor MCP, em qualquer plano pago. Nos planos Scale e superiores, uma execução grande de 20 versões curtas ou mais que pode esperar horas também pode ir pela Batch API, uma fila de processamento cujos resultados podem levar até um dia.

**A execução foi interrompida.**
Cada versão tem sua própria chave salva e seu ID de geração, então a retomada continua de onde parou sem pagar duas vezes.

## Está funcionando se

- Você confirma a associação entre mercados e idiomas e a matriz antes de qualquer custo.
- O piloto volta antes de o restante começar.
- No final, você tem um arquivo por vídeo e idioma, mais uma planilha de revisão.
