# [PROJECT_NAME] Constitution

<!--
  Modelo. A constituição vigente do CLite está em .specify/memory/constitution.md.
  Mantenha versão, data de ratificação e governança ao editar.
-->

## Core Principles

### I. Aprendizado primeiro (NÃO NEGOCIÁVEL)

Toda decisão prioriza o entendimento. Código legível, dividido por fase, com o
conceito documentado. Performance não é objetivo.

### II. Fidelidade à gramática documentada

`docs/01` e `docs/02` são a fonte da verdade. Mudança de gramática precede o
código e entra no mesmo PR.

### III. Fatias verticais pequenas

Um ticket, um PR revisável, `main` sempre verde. Trabalho paralelo declarado.

### IV. Teste como especificação

Comportamento novo tem teste que falha antes. Programas `.clite` provam a
linguagem de ponta a ponta. Erros testados por código, linha e coluna.

### V. Python padrão e tipado

Python 3.12+, sem dependências de runtime, `mypy --strict`, `ruff` e `pytest`.

### VI. Escopo controlado

v1 completa antes da v2. OO limitado a classes, herança, polimorfismo e
sobreescrita.

### T0. Edição cirúrgica (P0)

Não reformate linhas existentes. Altere apenas o necessário; linhas novas ou
alteradas respeitam 80–100 colunas.

### T1. SOLID e qualidade

SRP, OCP, LSP, ISP e DIP. Python 3.12+, `dataclass(frozen=True)`,
`Protocol`/ABC, sem threads, DRY e KISS, métodos ≤20 linhas, CC<10 e
aninhamento ≤3.

### T2. TDD

RED → GREEN → REFACTOR. Cobertura de 80% no geral e 100% nos caminhos críticos.
Testes de unidade, conformidade `.clite` e erros com `pytest`, `pytest-cov` e
`Hypothesis`.

## Saída de comandos SDD

Artefatos com meta de 70 linhas; se passar de 100, seja mais conciso, em
tabelas/checklists, sem repetir o repositório.

## Governance

Emendas via PR, com justificativa e atualização da versão. Decisões técnicas
viram `D-NN` em `docs/05-decisoes.md`.

**Version**: 1.1.0 · **Ratified**: 17/11/2026 · **Last Amended**: 18/11/2026
