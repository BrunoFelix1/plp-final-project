---
description: Cria e atualiza tickets e pull requests de LLM no formato do projeto, com objetivo, critérios verificáveis e paralelismo. Use antes de abrir issue/PR.
---

Você transforma uma necessidade em ticket pequeno e verificável. Formatos
obrigatórios: `docs/agents/ticket-format.md` e `docs/agents/pull-request.md`.

## Antes de criar

1. Procure ticket equivalente no board (`gh issue list --search "..."`).
2. Verifique se cabe em `size/S` (até 2 h). Se não, divida.
3. Identifique arquivos tocados e tickets que podem rodar em paralelo.
4. Escolha o milestone pela data de `docs/04-plano-de-aprendizado.md`.

## Regras

- Título `tipo: NNN - slug`, com `feat:`, `fix:`, `docs:` ou `chore:`.
- Um requisito por ticket; 3–5 itens em “Pronto quando”.
- Nomeie o **conceito implementado** no corpo e cite **pelo menos uma
  referência de livro** com capítulo/seção (Tucker ou Compiladores).
- Se o ticket muda a gramática, inclua em “Pronto quando” a atualização de
  `docs/01` no mesmo PR.
- Sem pontos de história, sem estimar horas.
- Sempre incluir comando de verificação e caso de erro.
- Todo ticket nasce no **Backlog**.
- Não copie conteúdo de docs; referencie.
- Em PR: `Closes #N`, comando de teste **executado** e aprendizado em 3 linhas.

## Formato de saída

Para ticket: o corpo em Markdown, pronto para `gh issue create --body-file`.
Para PR: o corpo em Markdown, pronto para `gh pr create --body-file`.

Ao final, informe: número da issue/PR, labels aplicadas e milestone.
