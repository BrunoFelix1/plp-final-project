# Tasks: CLI `tokens` e testes golden

**Input**: [spec.md](./spec.md), [plan.md](./plan.md) · **Ticket**: #8
**Pré-requisito**: `uv run pytest -q` verde na branch antes de começar.

<!--
  REGRA DO PROJETO: meta de 70 linhas; uma linha por task.
  Formato: [ID] [P?] [Story?] Descrição — arquivo — teste.
-->

## Phase 1: Setup

- [X] T001 [Setup] Confirmar branch `feat/008-...` e base verde — `pyproject.toml` — `uv run pytest -q`

## Phase 2: User Story 1 — ver os tokens (P1)

- [X] T002 [US1] Teste: `int x;` gera 3 linhas `TAG lexema linha:coluna`; arquivo vazio gera saída vazia e exit `0`; saída idêntica em duas execuções — `tests/unit/test_cli_tokens.py` — `uv run pytest tests/unit/test_cli_tokens.py -q`
- [X] T003 [US1] `tokenize(source)` (sem `EOF`) — `src/clite/lexer/lexer.py` — import sem erro
- [X] T004 [US1] `format_token` e `run_tokens`; `executar_comando(args)` despacha por `args.comando`; `main` passa `args` — `src/clite/cli.py`, `src/clite/__main__.py` — `uv run pytest tests/unit/test_cli_tokens.py -q`
- [X] T005 [US1] Ajustar `test_comando_nao_implementado` para `parse` (o `tokens` agora funciona) e testar `parse`/`check`/`run` com `E9000` — `tests/unit/test_cli.py` — `uv run pytest tests/unit/test_cli.py -q`

## Phase 3: User Story 2 — erro com uma mensagem (P2)

- [X] T006 [US2] Teste: `a @ b` → exit `1`, stderr de uma linha `E1001 (linha 1, coluna 3)`, stdout vazio; `a & b` → `E1002`; arquivo não UTF-8 → `2` — `tests/unit/test_cli_tokens.py` — `uv run pytest tests/unit/test_cli_tokens.py -q`
- [X] T007 [US2] Tratar `LexicalError` (stderr, exit `1`) e `OSError`/`UnicodeDecodeError` (exit `2`) — `src/clite/cli.py` — `uv run pytest tests/unit/test_cli_tokens.py -q`

## Phase 4: User Story 3 — goldens (P2)

- [X] T008 [US3] Programas `basico`, `operadores`, `literais`, `erro_caractere`, `erro_e1002` — `examples/lexico/*.clite` — `uv run clite tokens examples/lexico/basico.clite`
- [X] T009 [US3] Goldens `.tokens`/`.err` gerados da CLI e **revisados à mão** contra `docs/01` §4.2 — `tests/golden/lexer/` — leitura
- [X] T010 [US3] Teste parametrizado: cada golden × CLI, byte a byte — `tests/unit/test_cli_tokens.py` — `uv run pytest tests/unit/test_cli_tokens.py -q`

## Phase 5: Polish

- [X] T011 [P] [Docs] Formato de saída e exit codes do `tokens` — `docs/03-arquitetura-frontend.md` — leitura
- [X] T012 [P] [QA] Gate completo — `Makefile` — `ruff check`, `mypy src`, `pytest -q`, `tools.magic_numbers`
- [X] T013 [P] [QA] Provas do [quickstart.md](./quickstart.md), inclusive alterar um golden e ver o teste falhar
- [X] T014 [P] [Docs] Confirmar que `docs/01` não muda — `docs/01-linguagem-clite.md`

## Dependencies

| Task | Depende de | Bloqueia |
| --- | --- | --- |
| T002 | T001 | T003 |
| T003–T004 | T002 | T005, T006 |
| T006 | T005 | T007 |
| T008–T010 | T007 | T011–T014 |
