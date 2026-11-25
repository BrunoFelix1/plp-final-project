# Tasks: Tabela de operadores e pontuação

**Input**: [spec.md](./spec.md), [plan.md](./plan.md) · **Ticket**: #7
**Pré-requisito**: `uv run pytest -q` verde na branch antes de começar.

<!--
  REGRA DO PROJETO: meta de 70 linhas; uma linha por task.
  Formato: [ID] [P?] [Story?] Descrição — arquivo — teste.
-->

## Phase 1: Setup

- [X] T001 [Setup] Confirmar branch `feat/007-...` e base verde — `pyproject.toml` — `uv run pytest -q`

## Phase 2: User Story 1 — tokens de operadores e pontuação (P1)

- [X] T002 [US1] Teste: os 23 lexemas, um token cada, com tag, lexema e posição; a tabela tem exatamente esses 23 — `tests/unit/lexer/test_operators.py` — `uv run pytest tests/unit/lexer/test_operators.py -q`
- [X] T003 [US1] Criar `OPERATORS` (lexema → `Tag`), `MAX_LEXEME_LENGTH` e `ISOLATED_PREFIXES` derivados da tabela — `src/clite/lexer/operators.py` — import sem erro
- [X] T004 [US1] Implementar `_scan_symbol` (tenta o maior lexema primeiro, depois o menor) — `src/clite/lexer/lexer.py` — `uv run pytest tests/unit/lexer/test_operators.py -q`
- [X] T005 [US1] Testes de borda: `a<=b`, `a < = b`, `x = y == z`, `===`, `a//b`, `a/b`, `-1`, `1+2`, `a<b` = `a < b` — `tests/unit/lexer/test_operators.py` — `uv run pytest tests/unit/lexer/test_operators.py -q`
- [X] T006 [US1] Ajustar `test_unknown_character_fails` para só `@` (FR-006) — `tests/unit/lexer/test_scanner.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`

## Phase 3: User Story 2 — `&` e `|` isolados (P2)

- [X] T007 [US2] Teste: `a & b`, `a | b`, `&`, `|` → `E1002` com linha/coluna; `&&&`/`|||` → composto e depois `E1002` na coluna 3; `@` e `.` seguem `E1001`; formato da mensagem — `tests/unit/lexer/test_operators.py` — `uv run pytest tests/unit/lexer/test_operators.py -q`
- [X] T008 [US2] `LexicalError` aceitar `code` (padrão `E1001`) e levantar `E1002` para prefixo isolado — `src/clite/lexer/lexer.py` — `uv run pytest tests/unit/lexer -q`

## Phase 4: Polish

- [X] T009 [P] [Docs] Registrar `E1002` na linha "Caractere inválido" — `docs/06-casos-dificeis.md` — leitura
- [X] T010 [P] [Docs] Citar `E1002` no exemplo léxico da tabela de erros — `docs/03-arquitetura-frontend.md` — leitura
- [X] T011 [P] [QA] Gate completo — `Makefile` — `uv run ruff check .`, `uv run mypy src`, `uv run pytest -q`, `uv run python -m tools.magic_numbers src tests tools scripts`
- [X] T012 [P] [QA] Executar as provas manuais de [quickstart.md](./quickstart.md) — `quickstart.md`
- [X] T013 [P] [Docs] Confirmar que `docs/01` não muda (§4.2 já lista os 23 lexemas) — `docs/01-linguagem-clite.md`

## Dependencies

| Task | Depende de | Bloqueia |
| --- | --- | --- |
| T002 | T001 | T003 |
| T003 | T002 | T004 |
| T004 | T003 | T005, T006 |
| T005, T006 | T004 | T007 |
| T007 | T006 | T008 |
| T008 | T007 | T009–T013 |

## Implementation Strategy

MVP = User Story 1 verde (T002–T006). Cada teste é escrito antes do código e deve
falhar antes de passar. Cada phase termina com o gate verde.
