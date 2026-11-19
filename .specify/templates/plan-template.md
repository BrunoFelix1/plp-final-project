# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` · **Date**: [DATE] · **Spec**: [link]

<!--
  REGRA DO PROJETO: meta de 70 linhas; se passar de 100, seja mais conciso. Sem repetir a spec.
  Tabelas primeiro e uma breve explicação do conceito.
  Toda decisão nova vira D-NN em docs/05-decisoes.md.
-->

## Summary

[Requisito principal + abordagem técnica em 2–3 linhas.]

## Technical Context

| Item | Valor |
| --- | --- |
| Python | 3.12+ |
| Dependências de runtime | nenhuma |
| Testes | pytest (+ hypothesis quando fizer sentido) |
| Qualidade | ruff, mypy --strict em `src/` |
| Módulos afetados | `src/clite/...` |
| Documento da gramática | `docs/01` / `docs/02` |

## Constitution Check

| Princípio | Como este plano cumpre |
| --- | --- |
| I. Aprendizado | [o conceito exercitado] |
| II. Fidelidade à gramática | [seção de docs atualizada] |
| III. Fatia pequena | [ticket e arquivos tocados] |
| IV. Teste primeiro | [teste principal] |
| V. Python padrão | [sem dependência nova] |
| VI. Escopo | [o que fica de fora] |

Violações: [nenhuma | D-NN com justificativa].

## Project Structure

```text
src/clite/[pacote]/[arquivo].py
tests/[unit|errors|conformance]/[arquivo].py
examples/[programa].clite
```

**Structure Decision**: [por que esses arquivos e não outros.]

## Phase 0: Research

| Pergunta | Resposta | Fonte |
| --- | --- | --- |
| [dúvida técnica] | [decisão] | [livro/seção ou D-NN] |

## Phase 1: Design

| Artefato | Conteúdo |
| --- | --- |
| Contratos | [classes/funções e assinaturas] |
| Erros | [códigos E1xxx–E4xxx novos] |
| Testes | [casos felizes + erros] |

## Complexity Tracking

| Violação | Por que é necessária | Alternativa descartada |
| --- | --- | --- |
| [nenhuma] | — | — |
