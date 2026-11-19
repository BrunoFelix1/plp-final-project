# Tasks: [FEATURE]

**Input**: `specs/[###-feature]/spec.md`, `plan.md`
**Pré-requisito**: `make check` verde antes de começar.

<!--
  REGRA DO PROJETO: meta de 70 linhas; se passar de 100, seja mais conciso. Uma linha por task.
  Formato: [ID] [P?] [Story?] Descrição — arquivo — teste.
  [P] = pode rodar em paralelo (arquivos disjuntos).
-->

## Phase 1: Setup

- [ ] T001 [P] [Setup] [preparar arquivo/base] — `caminho` — `teste`

## Phase 2: Foundational

- [ ] T002 [P] [Core] [pré-requisito comum] — `caminho` — `teste`

## Phase 3: User Story 1 (P1)

- [ ] T003 [US1] [teste que falha] — `tests/...` — `comando`
- [ ] T004 [US1] [implementação mínima] — `src/clite/...` — `comando`

## Phase 4: User Story 2 (P2)

- [ ] T005 [US2] [implementação] — `caminho` — `comando`

## Phase 5: Polish

- [ ] T006 [P] [Docs] atualizar `docs/01` ou `docs/02` — `docs/...`
- [ ] T007 [P] [QA] rodar `make check` e casos de `docs/06` — `make check`

## Dependencies

| Task | Depende de | Bloqueia |
| --- | --- | --- |
| T004 | T003 | T005 |

## Parallel Example

```text
# Podem rodar juntas (arquivos disjuntos):
T003  tests/unit/lexer/test_identifiers.py
T005  tests/unit/lexer/test_numbers.py
```

## Implementation Strategy

MVP = User Story 1 verde. Depois, incremental por história. Cada phase termina
com `make check` verde e um ticket atualizado no board.
