# Implementation Plan: Arquitetura do front-end

**Branch**: `docs/003-arquitetura-do-frontend` · **Date**: 2026-11-21 · **Spec**: [spec.md](spec.md)

<!--
  REGRA DO PROJETO: meta de 70 linhas; se passar de 100, seja mais conciso. Sem repetir a spec.
  Tabelas primeiro e uma breve explicação do conceito.
  Toda decisão nova vira D-NN em docs/05-decisoes.md.
-->

## Summary

Edição cirúrgica de `docs/03-arquitetura-frontend.md` para fechar as 4 lacunas da
spec: diagrama com todos os módulos, referência D-02, nome do pacote `symbols`
e separação v1/v2 nos contratos. Nenhum código muda.

**Conceito:** o diagrama e os contratos são a "interface" entre fases. Quem
implementa o parser só precisa saber o que o lexer entrega (tokens), não como
ele funciona. Isso só é verdade se o documento estiver correto e completo.

## Technical Context

| Item | Valor |
| --- | --- |
| Tipo de mudança | documentação (Markdown) |
| Arquivo alterado | `docs/03-arquitetura-frontend.md` |
| Arquivos **não** alterados | `docs/README.md` (o link para o docs/03 já existe; evita conflito com o PR #38), `src/` |
| Verificação | revisão por pares + `make check` (garante que nada quebrou) |
| Edição já feita pelo dev | diagrama §1: `TypeChecker` → `Semantic` (mantida) |

## Constitution Check

| Princípio | Como este plano cumpre |
| --- | --- |
| I. Aprendizado | documento explica fases, contratos e a escolha orientada a fase |
| II. Fidelidade | alinha o `docs/03` ao `docs/05` (D-02, D-06, D-12) e ao Apêndice A |
| III. Fatia pequena | 1 arquivo, ~20 linhas alteradas |
| IV. Teste primeiro | não se aplica (sem código); revisão por pares substitui |
| V. Python padrão | sem dependência |
| VI. Escopo | não implementa fases nem altera `errors.py` |
| T0. Edição cirúrgica | só as linhas das 4 lacunas; nada é reformatado |

Violações: nenhuma.

## Project Structure

```text
docs/03-arquitetura-frontend.md   # único arquivo alterado
specs/003-arquitetura-do-frontend/ # artefatos SDD
```

**Structure Decision**: o ticket lista `docs/03` e `docs/README.md`; o segundo já
aponta corretamente para o docs/03, então fica intocado.

## Phase 0: Research

Ver [research.md](research.md).

| Pergunta | Resposta | Fonte |
| --- | --- | --- |
| Nome do pacote Java: `symbol` ou `symbols`? | `symbols` | Compiladores, Apêndice A: `import symbols.*`; "a classe Type faz parte do pacote symbols" |
| Qual decisão justifica os visitantes? | D-02 (D-05 é a stack) | `docs/05` §D-02 |
| Quais módulos o diagrama deve citar? | 9 em `src/clite/` + `cli` | `ls src/clite` |
| O que é v2 nos contratos? | `this`, classe corrente, heap, frames de método, `return`/`ReturnSignal` | `docs/02`; D-09, D-15 |

## Phase 1: Design

| Lacuna | Seção do docs/03 | Mudança |
| --- | --- | --- |
| L1 módulos no diagrama | §1 | pacote ao lado de cada caixa (`lexer/`, `parser/ → ast/`, `semantic/`, `interpreter/`); setas laterais `← symbols.py, types.py` (Semantic) e `← values.py` (Interpreter); `cli.py (entrada)` no topo; linha final `errors.py: usado por todas as fases` |
| L1a nome da fase | §1 | caixa `Semantic` → `Semantic (TypeChecker)`; §2 e §4.3 mantêm `TypeChecker` (é a classe) |
| L2 referência errada | §2, último parágrafo | "Ver D-05" → "Ver D-02"; citar a discussão orientado a objeto × orientado a fase do Apêndice A |
| L3 nome do pacote | cabeçalho | `symbol` → `symbols` |
| L4 v1 × v2 | §§4.3, 4.4 | marcar com "(v2)" os itens de OO; na v1 o estado é um único mapa de variáveis (D-06) |

Contratos, erros (§5) e CLI (§6) já atendem FR-004 e **não mudam**.

## Complexity Tracking

| Violação | Por que é necessária | Alternativa descartada |
| --- | --- | --- |
| nenhuma | — | — |
