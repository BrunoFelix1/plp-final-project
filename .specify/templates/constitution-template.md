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

## Saída de comandos SDD

Artefatos com no máximo 1 página, em tabelas/checklists, sem repetir o
repositório.

## Governance

Emendas via PR, com justificativa e atualização da versão. Decisões técnicas
viram `D-NN` em `docs/05-decisoes.md`.

**Version**: 1.0.0 · **Ratified**: 17/11/2026 · **Last Amended**: 17/11/2026
