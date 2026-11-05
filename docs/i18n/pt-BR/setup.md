---
title: "Skill setup"
subtitle: "Conecte a sync. ao seu agente, confira sua conta e chegue ao primeiro vídeo."
description: "A skill de agente setup da sync. labs conecta a sync. ao Claude Code, Codex, Cursor e outros agentes, mostra seu plano e seus créditos e sugere um primeiro vídeo. Ela nunca inicia trabalho pago."
og:description: "Conecte a sync. ao seu agente, confira sua conta, seu plano e seus créditos e chegue ao primeiro vídeo."
source-sha256: 8bf4757e0b9fd57ed1bb43b1d923220a2e62a7d62a8dd8ae8c1dd87f2a19d10a
---

# setup

> [!TIP]
> Instale esta skill com `npx skills add synchronicity-labs/skills --skill setup`, ou obtenha todas as skills com o plugin do Claude Code. Veja [Skills de agente](overview.md).

## O que faz

A `setup` conecta a sync. ao seu agente e leva você ao primeiro vídeo em poucos minutos. Ela verifica a conexão, faz o login se necessário, mostra sua conta, seu plano e os créditos restantes e lista o que você pode criar, com um prompt de exemplo para cada caso. A própria skill setup nunca inicia trabalho pago.

## Quando usar

- Logo depois de instalar as skills ou o plugin.
- Quando as ferramentas da sync. estão faltando ou desconectadas.
- Para conferir sua conta, seu plano ou seus créditos.

Pedidos de mídia como “sincronize os lábios disto” vão direto para a skill correspondente, que conecta você da mesma forma quando necessário. Se algo falhou ou parece travado, use a [troubleshoot](troubleshoot.md).

## Experimente

- “Configure a sync.”
- “Quantos créditos da sync ainda tenho?”

## Conectar

| Agente | Como |
| --- | --- |
| Claude Code com o plugin | Execute `/mcp`, selecione `sync` e entre na sua conta |
| Claude Code sem o plugin | `claude mcp add --transport http sync https://mcp.sync.so/mcp` e depois `/mcp` |
| Claude.ai ou Claude Desktop | Settings, Connectors, Add custom connector, `https://mcp.sync.so/mcp` |
| Codex | `codex mcp add sync --url https://mcp.sync.so/mcp` e depois `codex mcp login sync` |
| Cursor | Adicione `{"mcpServers": {"sync": {"url": "https://mcp.sync.so/mcp"}}}` a `.cursor/mcp.json` |
| Scripts e CI | Defina `SYNC_API_KEY` ou execute o servidor local com `npx -y @sync.so/mcp-server@latest` |

O servidor hospedado faz o login com sua conta da sync., então não há nenhuma chave para copiar. Para obter uma chave de API, veja [Autenticação](https://sync.so/docs/api-reference/guides/authentication). Para saber mais sobre o próprio servidor, veja o guia do [servidor MCP](https://sync.so/docs/plugins-and-extensions/mcp-server).

## Perguntas frequentes

**Depois que conectei, diz que as ferramentas não estão lá.**
A maioria dos agentes só carrega novos servidores MCP depois de reiniciar ou recarregar.

**Preciso de um plano pago?**
Não. Toda conta começa com algumas gerações gratuitas por mês. Os planos pagos aumentam os limites de duração e a concorrência e, a partir do Creator, removem a marca d'água.

**O que devo usar, o servidor hospedado ou o npm?**
O servidor hospedado para uso interativo, já que você entra com sua conta. O pacote npm com uma chave de API para scripts, CI e agentes que não podem usar servidores remotos.

## Está funcionando se

- Você vê o nome da sua organização e seus créditos ou sua cota restantes.
- Você recebe uma lista curta de coisas para experimentar, e nada é cobrado.
