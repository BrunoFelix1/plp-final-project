# Tasks: AST base e nós de expressão

**Input**: `specs/009-ast-base-e-nos-de-expressao/spec.md`, `plan.md`
**Ticket**: `feat: 009` (issue #9) · **Pré-requisito**: `make check` verde antes de começar.

<!--
  REGRA DO PROJETO: meta de 70 linhas; uma linha por task.
  Formato: [ID] [P?] [Story?] Descrição — arquivo — teste.
  [P] = arquivos disjuntos (pode rodar em paralelo).
  TDD (T2): todo GREEN é precedido de RED falhando.
-->

## Phase 1: Setup

- [X] T001 Confirmar branch `feat/009-ast-base-e-nos-de-expressao` e ambiente sincronizado — raiz (`uv sync`) — `uv run pytest -q` (suíte atual verde)

## Phase 2: Foundational

Nenhuma: o esqueleto do ticket 004 já está na `main`; sem bloqueios.

## Phase 3: User Story 1 (P1) — construir os nós de §6

Independência: testável com `uv run pytest tests/unit/ast/test_nodes.py -q`.

- [X] T002 [US1] RED: testes de construção dos 17 nós (parametrizado; literais > 1 em constantes UPPER_SNAKE) — `tests/unit/ast/test_nodes.py` — `uv run pytest tests/unit/ast/test_nodes.py -q` (falha: módulo inexistente)
- [X] T003 [US1] RED: igualdade rasa e aninhada, imutabilidade (`FrozenInstanceError`) e árvore-exemplo da issue `Assign(VarRef('x'), Binary('+', VarRef('x'), IntLiteral(1)))` — `tests/unit/ast/test_nodes.py` — mesmo comando (falha)
- [X] T004 [US1] GREEN: implementar os 15 `@dataclass(frozen=True)` + aliases `CliteType`/`Declaration`/`Command`/`Expression`, sem lógica, conforme `data-model.md` — `src/clite/ast/nodes.py` — `uv run pytest tests/unit/ast/test_nodes.py -q` (verde)

## Phase 4: User Story 2 (P2) — posição em todo nó

- [X] T005 [US2] RED: posição — padrão "não informado" (0) e `line`/`column` explícitos preservados — `tests/unit/ast/test_nodes.py` — mesmo comando (falha: campos ausentes)
- [X] T006 [US2] GREEN: adicionar `line: int = 0, column: int = 0` ao fim dos 15 nós — `src/clite/ast/nodes.py` — `uv run pytest tests/unit/ast/test_nodes.py -q` (verde)

## Phase 5: Polish

- [X] T007 [Docs] Conferir que `docs/01` não precisa de patch (gramática inalterada; nós já em §6) — `docs/01-linguagem-clite.md` — revisão visual
- [X] T008 [QA] Suíte completa e qualidade: `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, `uv run pytest -q` (inclui `tests/quality`, números mágicos) — raiz
- [X] T009 [QA] Verificar `checklists/ast-nodes.md` item a item (CHK001–CHK018), marcando só com evidência — `specs/009-ast-base-e-nos-de-expressao/checklists/ast-nodes.md`
- [X] T010 [Board] Preparar corpo do PR (`Closes #9`, comando de teste executado) conforme `docs/agents/pull-request.md`; não abrir sem pedido (§5.4) — raiz

## Dependencies

| Task | Depende de | Bloqueia |
| --- | --- | --- |
| T002, T003 | T001 | T004 |
| T004 | T002, T003 | T005 |
| T005 | T004 | T006 |
| T006 | T005 | T007–T010 |

## Parallel Example

```text
# Dentro do ticket: nenhuma task em paralelo — todos os pares de escrita
# compartilham os 2 arquivos fixados pelo ticket.
# Paralelismo real é ENTRE tickets: 009 (este) ∥ 010 parser (arquivos disjuntos),
# amarrados pelo contrato specs/009.../contracts/ast-nodes.md.
```

## Implementation Strategy

MVP = User Story 1 verde (nós construíveis, iguais e imutáveis). US2 incrementa
posição em todo nó. Cada phase termina com o comando do ticket verde; no fim,
`make check` (Windows: os quatro `uv run ...`) e o card `feat: 009` movido no board.
