# Tasks: Tabela de símbolos (ticket 012)

**Input**: `specs/012-tabela-de-simbolos/spec.md`, `plan.md`
**Pré-requisito**: `make check` verde antes de começar.

<!--
  REGRA DO PROJETO: meta de 70 linhas; se passar de 100, seja mais conciso. Uma linha por task.
  Formato: [ID] [P?] [Story?] Descrição — arquivo — teste.
  [P] = pode rodar em paralelo (arquivos disjuntos).
-->

## Phase 1: Setup

- [X] T001 [P] [Setup] Criar suíte com constantes de posição nomeadas (padrão de `test_nodes.py`; nomes no formato T2 `test_<comportamento>_quando_<condição>`) — `tests/unit/semantic/test_symbols.py` — `uv run pytest tests/unit/semantic/test_symbols.py -q` (coleta sem erros)

## Phase 2: Foundational

Nenhuma task bloqueante: `src/clite/symbols.py` já existe como esqueleto
importável e nenhum pré-requisito comum falta.

## Phase 3: User Story 1 — Registrar e resolver nomes (P1)

- [X] T002 [US1] RED: `test_declara_e_resolve_quando_variavel_registrada` e `test_declara_e_resolve_quando_array_registrado` (nós devolvidos intactos) — `tests/unit/semantic/test_symbols.py` — `uv run pytest tests/unit/semantic/test_symbols.py -q` (falha: `SymbolTable` inexistente)
- [X] T003 [US1] GREEN: implementar `SymbolTable` com `declare`/`lookup` sobre `dict` interno — `src/clite/symbols.py` — `uv run pytest tests/unit/semantic/test_symbols.py -q` (verde)

## Phase 4: User Story 2 — Detectar duplicidade (P1)

- [X] T004 [US2] RED: `test_declara_duplicado_quando_nome_repetido` (E3002 na linha/coluna da 2ª), `test_declara_duplicado_quando_array_repetido`, `test_declara_duplicado_quando_tipo_diferente`, `test_declara_duplicado_quando_em_bloco_distinto` — `tests/unit/semantic/test_symbols.py` — `uv run pytest tests/unit/semantic/test_symbols.py -q` (falha)
- [X] T005 [US2] GREEN: implementar `SemanticError` (padrão `LexicalError` da #7), `ERROR_CODE_DUPLICATE = "E3002"` e verificação em `declare` — `src/clite/symbols.py` — `uv run pytest tests/unit/semantic/test_symbols.py -q` (verde)

## Phase 5: User Story 3 — Nome inexistente e lista (P2)

- [X] T006 [US3] RED: `test_busca_inexistente_quando_com_posicao` (E3001), `test_busca_inexistente_quando_sem_posicao` (0, 0), `test_lista_quando_tres_declaracoes`, `test_tabela_vazia_quando_busca` — `tests/unit/semantic/test_symbols.py` — `uv run pytest tests/unit/semantic/test_symbols.py -q` (falha)
- [X] T007 [US3] GREEN: `ERROR_CODE_UNDECLARED = "E3001"` no `lookup` + property `declarations` (cópia defensiva, ordem de inserção) — `src/clite/symbols.py` — `uv run pytest tests/unit/semantic/test_symbols.py -q` (verde)

## Phase 6: Polish

- [X] T008 [P] [Docs] Confirmar diff de `docs/01` vazio (sem mudança de gramática) e registrar aprendizado no corpo do PR — `docs/01-linguagem-clite.md` — conferência visual do diff
- [X] T009 [P] [QA] Rodar `make check` (Windows: `uv run ruff check .` + `uv run ruff format --check .` + `uv run mypy src` + `uv run pytest`) e marcar `checklists/symbols.md` item a item — `make check` — saída verde

## Dependencies

| Task | Depende de | Bloqueia |
| --- | --- | --- |
| T002 | T001 | T003 |
| T003 | T002 | T004, T006 |
| T004 | T003 | T005 |
| T005 | T004 | T007 |
| T006 | T003 | T007 |
| T007 | T005, T006 | T008, T009 |

## Parallel Example

```text
# Podem rodar juntas (arquivos disjuntos):
T008  conferência do diff de docs/01
T009  make check + checklist symbols.md
```

## Implementation Strategy

MVP = User Story 1 verde (T002–T003: tabela declara e resolve). Depois US2
(unicidade/E3002) e US3 (E3001/lista), cada uma terminando com a suíte do
ticket verde. RED antes de GREEN em todas as histórias (constituição T2).
Como todas as tasks tocam o mesmo par de arquivos, a ordem é sequencial;
T008/T009 são os únicos paralelizáveis. O ticket #12 só fecha com
`make check` verde (T009).
