---
title: "Skill troubleshoot"
subtitle: "Descubra por que um trabalho falhou, travou ou foi rejeitado e retome sem pagar duas vezes."
description: "A skill de agente troubleshoot da sync. labs descobre por que um trabalho da sync. falhou, travou ou foi rejeitado, explica a causa real em palavras simples, retoma o trabalho sem iniciar um segundo trabalho pago e pode relatar o problema à sync."
og:description: "Descubra a partir do seu agente por que um trabalho da sync. falhou, travou ou foi rejeitado e retome sem pagar duas vezes."
source-sha256: 8de9f50b08fda9e8256cefecc063b3e44871e28eb125c0e2060560fcdabb8fff
---

# troubleshoot

> [!TIP]
> Instale esta skill com `npx skills add synchronicity-labs/skills --skill troubleshoot`, ou obtenha todas as skills com o plugin do Claude Code. Veja [Skills de agente](overview.md).

## O que faz

A `troubleshoot` descobre por que um trabalho da sync. falhou, travou ou foi rejeitado, explica a causa real em palavras simples e retoma o trabalho sem iniciar um segundo trabalho pago. Quando o problema foi um erro confuso ou um recurso que falta, ela também pode enviar um relato curto para a equipe da sync., sem segredos nem mídia anexados.

## Quando usar

| O que aconteceu | Use |
| --- | --- |
| Um trabalho falhou, foi rejeitado ou parece travado | `troubleshoot` |
| Um 402, 429 ou outro erro da sync. | `troubleshoot` |
| As ferramentas da sync. sumiram ou dizem que você saiu da conta | `troubleshoot`, que conecta você de novo da mesma forma que a [setup](setup.md) |
| Você ainda não conectou a sync. | [setup](setup.md) |
| Seu próprio código recebe erros da API | [sync-api](sync-api.md) |

## Experimente

- “Meu lipsync falhou, por quê?”
- “Esta dublagem está processando há 20 minutos”
- “Continuo recebendo concurrency_limit_reached”
- “O vídeo saiu, mas a boca parece estranha”

## O que você precisa

- O servidor MCP da sync. conectado, para ler o status dos trabalhos e a sua conta. Sem ele, a skill ainda consegue explicar uma mensagem de erro que você colar.
- O texto do erro, ou o ID da geração ou do batch, se você tiver.

## Perguntas frequentes

**Fui cobrado pelo trabalho que falhou?**
Não. Gerações que falham não são cobradas.

**Ainda está processando. Devo iniciar de novo?**
Não. Pendente não é o mesmo que falho, e um segundo trabalho não termina antes. A skill continua acompanhando o mesmo trabalho.

**Minha solicitação deu timeout. Ela chegou a ser processada?**
Talvez. A skill procura o trabalho, ou repete a solicitação idêntica com a mesma chave, que devolve o original em vez de iniciar outro.

**O resultado parece errado.**
As causas mais comuns estão no original: um rosto virado ou coberto, várias pessoas no quadro, música sob a voz ou baixa resolução. A skill verifica esses pontos e sugere o `sync-3` se um modelo mais antigo foi usado. Tentar de novo é uma nova geração paga, então ela informa o custo antes.

**O que o relato para a sync. inclui?**
O tipo de problema, o erro exato, a ferramenta e o ID do trabalho. Nunca a sua chave, links assinados, dados pessoais ou mídia.

## Está funcionando se

- Você recebe a causa real, com o código de erro quando houver um.
- Nenhum segundo trabalho pago começa sem que você aprove uma nova tentativa.
- O trabalho original é retomado de onde parou.
