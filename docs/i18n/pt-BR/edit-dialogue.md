---
title: "Skill edit-dialogue"
subtitle: "Mude ou remova algumas palavras faladas na própria voz de quem fala."
description: "A skill de agente edit-dialogue da sync. labs corrige algumas palavras faladas em um vídeo com um único falante sem regravar: ela transcreve, gera uma prévia das novas palavras na própria voz de quem fala e depois ressincroniza os lábios só naquele trecho."
og:description: "Corrija um preço, nome, data ou palavra errada em um vídeo, na própria voz de quem fala, sem regravar."
source-sha256: 987e84b2b0109308cf6cc142fe8b371eee3106b2a26e7a6b633b9a2acf5a9fd7
---

# edit-dialogue

> [!TIP]
> Instale esta skill com `npx skills add synchronicity-labs/skills --skill edit-dialogue`, ou obtenha todas as skills com o plugin do Claude Code. Veja [Skills de agente](overview.md).

## O que faz

A `edit-dialogue` corrige algumas palavras faladas em um vídeo sem regravar. Ela transcreve o vídeo, associa a sua correção às palavras exatas, sintetiza as novas palavras na própria voz de quem fala, deixa você ouvir uma prévia e depois ressincroniza os lábios só naquele trecho. Todo o resto mantém a imagem e o som originais.

## Quando usar

| O que você tem | Use |
| --- | --- |
| Um preço, nome, data ou palavra errada, ou uma muleta de fala para cortar | `edit-dialogue` |
| Um roteiro totalmente novo | [lipsync](lipsync.md) com uma voz escolhida |
| O mesmo vídeo em outro idioma | [translate-and-dub](translate-and-dub.md) |
| Uma gravação personalizada para cada destinatário | `edit-dialogue`, uma prévia e um vídeo por destinatário |

## Experimente

- “Em ./promo.mp4 eu digo $39 por mês. Agora é $49, corrija só isso.”
- “Corte o ‘hã’ depois de ‘cobrança anual’ neste vídeo”
- “O nome deveria ser Siobhan, não Shannon”

## O que você precisa

- O servidor MCP da sync. conectado. A skill [setup](setup.md) orienta você nesse processo. A versão REST deste fluxo está em acesso antecipado; veja [Transcription and Dialogue Editing](https://sync.so/docs/developer-guides/dialogue-editing).
- Um vídeo com um único falante, de até 10 minutos.

## Perguntas frequentes

**Por que ela me mostra a transcrição?**
Para que vocês dois apontem para as mesmas palavras. Cada mudança e cada remoção fica ligada a uma palavra da transcrição, o que mantém a edição exata.

**A prévia custa dinheiro?**
Pode custar. A prévia clona a voz de quem fala e sintetiza as novas palavras, então o agente menciona isso ao confirmar as edições. O vídeo final tem uma estimativa separada antes de ser criado.

**Um nome saiu errado.**
Peça uma pronúncia. O agente adiciona uma grafia fonética como “shivawn”, escrita como uma palavra comum, e cria uma nova prévia.

**Algumas edições falharam.**
Normalmente o novo texto é longo demais para o espaço que ocupa. O agente informa quais edições falharam e sugere um texto mais curto.

**Dá para fazer uma versão por destinatário?**
Sim. Você combina as edições de cada destinatário em uma única tabela, as prévias começam juntas e, depois de uma única aprovação do total, os vídeos também começam juntos, até o limite do seu plano. Pelo MCP, é uma chamada a `jobs_create-many` para as prévias e outra para os vídeos, em qualquer plano pago.

**Posso substituir um parágrafo inteiro?**
Este fluxo é para palavras pontuais. Para um roteiro novo, lipsync com uma voz é a ferramenta mais adequada, e o agente vai dizer isso.

## Está funcionando se

- No áudio da prévia, só as suas palavras mudaram.
- Você aprova a prévia e o custo antes de o vídeo ser criado.
- O resultado reproduz o vídeo original com apenas essas palavras diferentes.
