# Tasks: Lexer de identificadores, literais e posição

**Input**: [spec.md](./spec.md), [plan.md](./plan.md) · **Ticket**: #6
**Pré-requisito**: `uv run pytest -q` verde na branch antes de começar.

<!--
  REGRA DO PROJETO: meta de 70 linhas; uma linha por task.
  Formato: [ID] [P?] [Story?] Descrição — arquivo — teste.
  [P] = pode rodar em paralelo (arquivos disjuntos).
-->

## Phase 1: Setup

- [X] T001 [Setup] Confirmar branch `feat/006-...` e base verde — `pyproject.toml` — `uv run pytest -q`

## Phase 2: Foundational

- [X] T002 [Core] Criar `LexicalError` (`code="E1001"`, `line`, `column`, `message`, `__str__` no formato D-12) e constantes `WHITESPACE`, `DOT`, `QUOTE`, `SLASH`, `NEWLINE` — `src/clite/lexer/lexer.py` — import sem erro
- [X] T003 [Core] Criar helper `scan_all(source)` que chama `scan()` até `Tag.EOF` — `tests/unit/lexer/test_scanner.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`

## Phase 3: User Story 1 — tokens válidos (P1)

- [X] T004 [US1] Teste: `abc`, `abc123`, `whilea` (um `IDENT`, maior casamento) — `tests/unit/lexer/test_scanner.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T005 [US1] Implementar roteamento de letra e `_identifier` — `src/clite/lexer/lexer.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T006 [US1] Teste: `42`, `3.14`, `5.0`, `0.5` — `tests/unit/lexer/test_scanner.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T007 [US1] Implementar `_number` (float só com dígitos dos dois lados) — `src/clite/lexer/lexer.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T008 [US1] Teste: `true`, `false` e reservadas (`while`, `int`, `print`) — `tests/unit/lexer/test_scanner.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T009 [US1] Consultar `KEYWORDS` antes de devolver `IDENT` — `src/clite/lexer/lexer.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T010 [US1] Teste: `'a'` e `' '`, com `lexeme` incluindo as aspas — `tests/unit/lexer/test_scanner.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T011 [US1] Implementar `_char_literal` (um imprimível entre aspas) — `src/clite/lexer/lexer.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T012 [US1] Teste: espaços/tabs/CR/LF, comentário `//` e comentário sem newline; linha/coluna 1-based — `tests/unit/lexer/test_scanner.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T013 [US1] Implementar `_skip_trivia` e avanço de `line`/`column` — `src/clite/lexer/lexer.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T014 [US1] Teste: `EOF` com `lexeme=""` e chamadas seguintes repetindo `EOF` — `tests/unit/lexer/test_scanner.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T015 [US1] Implementar retorno estável de `Token(Tag.EOF, "", line, column)` — `src/clite/lexer/lexer.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`

## Phase 4: User Story 2 — erros com posição (P2)

- [X] T016 [US2] Teste: `5.` e `.5` levantam `LexicalError` na coluna do ponto — `tests/unit/lexer/test_scanner.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T017 [US2] Implementar erro de float incompleto — `src/clite/lexer/lexer.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T018 [US2] Teste: `''` e `'ab'` levantam `LexicalError` na aspa inicial — `tests/unit/lexer/test_scanner.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T019 [US2] Implementar erro de char vazio ou longo — `src/clite/lexer/lexer.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T020 [US2] Teste: `@`, `;`, `+`, `(` e `1.2.3` (FLOAT `1.2` e erro no segundo ponto) — `tests/unit/lexer/test_scanner.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`
- [X] T021 [US2] Implementar `E1001` para caractere fora do subconjunto, inclusive operador/pontuação até o #7 — `src/clite/lexer/lexer.py` — `uv run pytest tests/unit/lexer/test_scanner.py -q`

## Phase 5: Polish

- [X] T022 [P] [QA] Rodar o gate completo — `Makefile` — `uv run ruff check .`, `uv run mypy src`, `uv run pytest -q`, `uv run python -m tools.magic_numbers src tests tools scripts`
- [X] T023 [P] [QA] Executar as provas manuais de [quickstart.md](./quickstart.md) e conferir a saída — `quickstart.md`
- [X] T024 [P] [Docs] Confirmar que `docs/01` §4 não muda (gramática já coberta) e registrar no PR — `docs/01-linguagem-clite.md`

## Dependencies

| Task | Depende de | Bloqueia |
| --- | --- | --- |
| T002 | T001 | T003–T024 |
| T003 | T002 | T004 |
| T004–T015 | sequência TDD (teste → implementação) | T016 |
| T016–T021 | sequência TDD, após US1 | T022 |
| T022–T024 | T002–T021 | PR |

## Parallel Example

```text
# Depois de T021, podem rodar juntas (arquivos disjuntos):
T022  gate completo
T023  provas manuais de quickstart.md
T024  conferência de docs/01
```

## Implementation Strategy

MVP = User Story 1 (T001–T015): o scanner devolve identificadores, literais,
reservadas e `EOF` corretamente. Depois, US2 (T016–T021) fecha o contrato de erro.
Cada fase termina com o teste do scanner verde; o gate completo fecha o PR.
