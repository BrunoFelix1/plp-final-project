# Implementation Plan: AST base e nós de expressão

**Branch**: `feat/009-ast-base-e-nos-de-expressao` · **Date**: 2026-11-26 · **Spec**: [spec.md](spec.md)

## Summary

Expor os nós de `docs/01` §6 como dataclasses imutáveis com posição e sem lógica
(D-02), mais aliases de união para declarações, comandos e expressões. Abordagem:
um módulo novo (`clite/ast/nodes.py`) com testes TDD; nenhum outro arquivo muda.

## Technical Context

| Item | Valor |
| --- | --- |
| Python | 3.12+ |
| Dependências de runtime | nenhuma |
| Testes | pytest |
| Qualidade | ruff, mypy --strict em `src/`, regra de números mágicos (`tests/quality`) |
| Módulos afetados | `src/clite/ast/nodes.py`, `tests/unit/ast/test_nodes.py` (ambos novos) |
| Documento da gramática | `docs/01` §6 — **sem mudança** (nós já especificados) |

## Constitution Check

| Princípio | Como este plano cumpre |
| --- | --- |
| I. Aprendizado | Conceito: sintaxe abstrata × árvore de análise; por que `;` não vira nó |
| II. Fidelidade à gramática | Nós = exatamente os de `docs/01` §6; sem `Print` (D-04 fica p/ parser) |
| III. Fatia pequena | Ticket 009, 2 arquivos novos, um PR; parser (010) paralelo |
| IV. Teste primeiro | `tests/unit/ast/test_nodes.py` no RED antes de `nodes.py` (T2) |
| V. Python padrão | `dataclasses`, `typing.Literal`; zero dependência nova |
| VI. Escopo | Sem parser, semântica, Print, nós OO |

Violações: nenhuma.

## Project Structure

```text
src/clite/ast/nodes.py          # NOVO: nós + aliases (dados puros, frozen)
tests/unit/ast/test_nodes.py    # NOVO: construção, igualdade, imutabilidade, posição
```

**Structure Decision**: o ticket fixa esses dois arquivos; `ast/__init__.py` fica
intocado (consumidores importam `clite.ast.nodes` direto) e `types.py` continua
vazio para o ticket de semântica.

## Phase 0: Research

| Pergunta | Resposta | Fonte |
| --- | --- | --- |
| Estrutura dos nós | `@dataclass(frozen=True)`, sem métodos | D-02; T1 |
| Representação do `tipo` | `Literal["int","float","char","bool"]` em `nodes.py` | decisão do usuário; ticket restringe arquivos |
| Posição obrigatória? | `line=0, column=0` padrão ("não informado") | exemplo da issue; regra de mágicos (0/1 livres) |
| Herança entre nós | aliases de união, sem ABC | D-02; visitantes vêm depois |
| `If` sem `else` | campo opcional (`None`) | §6 `[senão?]` |

Detalhes e alternativas descartadas: [research.md](research.md)

## Phase 1: Design

| Artefato | Conteúdo |
| --- | --- |
| Contratos | [contracts/ast-nodes.md](contracts/ast-nodes.md) — superfície pública do módulo p/ parser (010) |
| Erros | nenhum código `E*` novo: nós são dados e não validam nada |
| Testes | construção (15 nós), igualdade rasa/aninhada, `FrozenInstanceError`, posição, árvore-exemplo da issue |
| Dados | [data-model.md](data-model.md) · Validação: [quickstart.md](quickstart.md) |

## Complexity Tracking

| Violação | Por que é necessária | Alternativa descartada |
| --- | --- | --- |
| [nenhuma] | — | — |
