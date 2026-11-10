---
title: "Skills de agente da sync. labs"
subtitle: "Sincronize lábios, duble e crie vídeos falados no Claude Code, Codex, Cursor e outros agentes."
description: "Instale as skills de agente oficiais da sync. labs para sincronizar os lábios de vídeos, fazer fotos e personagens de IA falarem, traduzir e dublar, corrigir palavras faladas, localizar campanhas, rodar lipsync em lote e integrar a sync. a apps a partir do seu agente."
og:description: "Skills de agente oficiais da sync. labs para lipsync, dublagem, fotos falantes, edição de diálogos, localização de campanhas, execuções em lote e integrações com a API."
source-sha256: 24b8cddee31c4d5d92596b8f747b83bf2483caf8e4a4eb585163234f70db670c
---

# Skills de agente da sync. labs

As skills de agente da sync. labs ensinam o seu agente a fazer o trabalho da sync. de ponta a ponta: sincronizar os lábios de vídeos, fazer fotos e personagens de IA falarem, traduzir e dublar, corrigir palavras faladas, localizar campanhas inteiras, rodar lipsync em grande volume e integrar a sync. aos seus próprios apps. Elas funcionam com Claude Code, Codex, Cursor, Gemini CLI, Hermes e qualquer agente que leia [Agent Skills](https://agentskills.io).

Cada skill é uma pasta com um `SKILL.md` de instruções, além de arquivos de referência e scripts que o agente só carrega quando uma tarefa precisa deles. Descreva o que você quer com suas próprias palavras, e o agente escolhe a skill certa.

<!-- card icon="fa-brands fa-github" -->
**[synchronicity-labs/skills no GitHub](https://github.com/synchronicity-labs/skills)**
O código-fonte de cada skill, os manifestos do plugin e um changelog. Licença MIT.

> [!NOTE]
> Toda skill informa o custo antes de iniciar um trabalho pago e espera a sua aprovação. A própria skill setup nunca inicia trabalho pago.

## Instalar as skills

### Qualquer agente (skills.sh)

Instale todas as skills com o [skills.sh](https://skills.sh):

```bash
npx skills add synchronicity-labs/skills
```

Adicione `--skill <name>` para instalar uma única skill, por exemplo `--skill lipsync`, ou `--agent claude-code` para escolher o agente.

### Plugin do Claude Code

O plugin instala as skills e conecta o servidor MCP da sync. em uma única etapa.

1. **Adicione o marketplace**

   ```text
   /plugin marketplace add synchronicity-labs/skills
   ```

2. **Instale o plugin**

   ```text
   /plugin install sync@sync
   ```

3. **Entre na sua conta**

   Execute `/mcp`, selecione `sync` e entre com sua conta da sync.

### Codex e Cursor

O Codex e o Cursor leem os manifestos do plugin nas pastas `.codex-plugin/` e `.cursor-plugin/` do repositório. Os dois manifestos conectam o servidor MCP hospedado da sync. Você também pode instalar as skills com o skills.sh e conectar o servidor seguindo as etapas da [skill setup](setup.md) para o seu agente.

## Conectar a sync.

As skills usam o [servidor MCP da sync.](https://sync.so/docs/plugins-and-extensions/mcp-server) hospedado em `https://mcp.sync.so/mcp`. Você entra com sua conta da sync., então não há nenhuma chave para copiar. A [skill setup](setup.md) guia qualquer agente na conexão, e a página dela lista as etapas para cada agente.

Para scripts, CI, agentes que não podem usar servidores remotos e a [skill sync-api](sync-api.md), crie uma [chave de API](https://sync.so/settings/api-keys) e defina-a como `SYNC_API_KEY`. Para usar as mesmas ferramentas MCP localmente com essa chave, execute o pacote npm:

```bash
npx -y @sync.so/mcp-server@latest
```

## Skills

| Skill | O que faz | Experimente |
| --- | --- | --- |
| [setup](setup.md) | Conecta a sync. ao seu agente, confere sua conta e leva você até o primeiro vídeo. | “Configure a sync.” |
| [lipsync](lipsync.md) | Sincroniza os lábios de um vídeo com um novo áudio ou um roteiro digitado. | “Sincronize os lábios de ./talk.mp4 com ./new-take.wav” |
| [talking-photo](talking-photo.md) | Faz uma foto, um retrato ou um personagem falar. | “Faça este retrato dizer: bem-vindo ao time” |
| [ai-video-to-talking](ai-video-to-talking.md) | Dá falas a clipes gerados por IA no Veo, Kling, Sora e outros, incluindo cenas com vários planos. | “Meu clipe do Veo não tem diálogo. Faça ela dizer esta fala.” |
| [translate-and-dub](translate-and-dub.md) | Dubla um vídeo em outros idiomas com os lábios sincronizados. | “Duble este vídeo do YouTube em espanhol” |
| [edit-dialogue](edit-dialogue.md) | Muda ou remove algumas palavras faladas na própria voz de quem fala. | “Mude o preço que eu falo para $49” |
| [localize-campaign](localize-campaign.md) | Localiza um conjunto de vídeos para vários mercados: plano, piloto, execução e planilha de revisão. Batches em fila exigem aprovação da organização e o plano Scale ou superior. | “Faça estes três anúncios em espanhol, alemão e japonês” |
| [batch-lipsync](batch-lipsync.md) | Sincroniza os lábios de cada linha de um CSV ou pasta dentro dos limites do seu plano, com retomada segura. Batches em fila exigem aprovação da organização e o plano Scale ou superior. | “Sincronize cada linha de leads.csv em presenter.mp4” |
| [sync-api](sync-api.md) | Integra a sync. a apps com a API REST ou os SDKs de Python e TypeScript: uploads, idempotência, webhooks e erros. Inclui batches em fila com aprovação da organização nos planos Scale e superiores. | “Adicione o lipsync da sync. ao meu app Next.js” |
| [troubleshoot](troubleshoot.md) | Descobre por que um trabalho falhou, travou ou foi rejeitado, retoma sem pagar duas vezes e pode relatar o problema à sync. | “Meu lipsync falhou, por quê?” |

A página de cada skill traz prompts de exemplo, o que você precisa, perguntas frequentes e como saber que está funcionando.

## Trabalho pago é sempre aprovado antes

Toda geração é cobrada, então toda skill informa o custo antes de iniciar um trabalho pago e espera o seu sinal verde. Se preferir não ser consultado duas vezes, defina um orçamento logo de início, por exemplo “pode seguir, qualquer coisa abaixo de $5 está ok”. Execuções com muitos vídeos, como [localize-campaign](localize-campaign.md) e [batch-lipsync](batch-lipsync.md), estimam o custo da execução inteira e oferecem um piloto antes do restante. Depois dessa única aprovação, o restante começa junto em vez de um por um.

<!-- llms-ignore -->
## Recursos relacionados

- [Servidor MCP](https://sync.so/docs/plugins-and-extensions/mcp-server): conecte clientes de IA à sync. labs
- [Plugin do ChatGPT](https://sync.so/docs/plugins-and-extensions/chatgpt-plugin): use a sync. labs dentro do ChatGPT
- [SDKs](https://sync.so/docs/developer-guides/sdk): SDKs oficiais de Python e TypeScript
- [Autenticação](https://sync.so/docs/api-reference/guides/authentication): crie e use uma chave de API
<!-- /llms-ignore -->
