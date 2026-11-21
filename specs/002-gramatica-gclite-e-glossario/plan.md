# Implementation Plan: Gramática GClite e glossário

**Branch**: `docs/002-gramatica-gclite-e-glossario` · **Date**: 2026-11-20
**Spec**: [spec.md](spec.md)

<!--
  REGRA DO PROJETO: meta de 70 linhas; se passar de 100, seja mais conciso. Sem repetir a spec.
  Tabelas primeiro e uma breve explicação do conceito.
  Toda decisão nova vira D-NN em docs/05-decisoes.md.
-->

## Summary

Completar a referência documental da v1 sem mudar a linguagem: acrescentar um
glossário explícito, corrigir inconsistências didáticas na EBNF/AST e consolidar
tokens, precedência, links e catálogo sem introduzir construções novas.

## Technical Context

| Item | Valor |
| --- | --- |
| Tipo | Documentação Markdown, sem código de runtime |
| Arquivos | `docs/01-linguagem-clite.md`, `docs/06-casos-dificeis.md`, `docs/README.md` |
| Fonte | `docs/01` é a referência da v1; `docs/02` permanece desenho OO |
| Validação | revisão documental, links existentes e `make check` |
| Dependências | nenhuma nova |

## Constitution Check

| Princípio | Como este plano cumpre |
| --- | --- |
| I. Aprendizado | explicita sintaxe concreta, abstrata e vocabulário do front-end |
| II. Fidelidade à gramática | preserva/organiza `docs/01` sem inventar produções |
| III. Fatia pequena | somente os três arquivos documentais do ticket |
| IV. Teste primeiro | checklist de revisão e verificação de links; sem comportamento novo |
| V. Python padrão | nenhuma dependência ou código novo |
| VI. Escopo | não implementa lexer/parser nem altera OO |

Violações: nenhuma.

## Project Structure

```text
docs/01-linguagem-clite.md       # EBNF, tabelas e glossário
docs/06-casos-dificeis.md        # catálogo de entradas-limite
docs/README.md                   # índice e links
```

**Structure Decision**: não criar `docs/glossario.md`; o glossário fica junto da
fonte de verdade para evitar definições concorrentes. Casos OO em `docs/06`
serão rotulados como futuros, sem misturá-los com a v1.

## Phase 0: Research

| Pergunta | Resposta | Fonte |
| --- | --- | --- |
| Onde fica o glossário? | seção explícita em `docs/01` | AGENTS §2; D-02/D-03 |
| Como corrigir a AST? | representar conversão e explicar `decpart`/`body` | `docs/01` §6; Apêndice A |
| Como tratar OO em `docs/06`? | rotular seção futura e remover ambiguidade da v1 | `docs/02`; `docs/06` |
| Como validar links e catálogo? | checagem de arquivos + checklist de revisão | `docs/README.md`; `docs/06` |

## Phase 1: Design

| Artefato | Conteúdo |
| --- | --- |
| Contratos | nenhum: não há API, CLI ou integração nova |
| Conteúdo | glossário de 6 termos; EBNF/AST, tabelas e catálogo revisados |
| Testes | revisão documental, links e `make check`; nenhum erro novo |

## Post-Design Constitution Check

- [x] O design é documental, pequeno e mantém `docs/01` como fonte da verdade.
- [x] Não há violação de dependências, fases, tipagem ou escopo OO.
- [x] O critério de teste é observável e proporcional ao ticket.

## Complexity Tracking

| Violação | Por que é necessária | Alternativa descartada |
| --- | --- | --- |
| [nenhuma] | — | — |
