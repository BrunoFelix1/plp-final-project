# Tasks: Bootstrap Python, uv e CI

**Input**: `spec.md`, `plan.md` · **Ticket**: `chore: 001` (#1)
**Pré-requisito**: confirmar a branch correta antes de alterar arquivos.

## Phase 1: Setup

- [x] T001 [P] Auditar manifesto, lockfile e pacote instalável — `pyproject.toml`, `uv.lock`, `src/clite/__init__.py` — `uv sync --frozen`
- [x] T002 [P] Auditar comandos locais e hooks — `Makefile`, `.pre-commit-config.yaml` — `make help`
- [x] T003 [P] Auditar workflow para PR em `main` — `.github/workflows/ci.yml` — `gh workflow list`

## Phase 2: User Story 1 (P1)

- [x] T004 [US1] Executar teste de fumaça e gates individuais — `tests/test_smoke.py` — `uv run pytest -q`, `uv run ruff check .`, `uv run mypy src`
- [x] T005 [US1] Alinhar o CI ao gate local — `.github/workflows/ci.yml` — `make check`

## Phase 3: Polish

- [x] T006 [P] Validar instalação congelada e estado limpo — `uv.lock`, `.gitignore` — `uv sync --frozen`
- [x] T007 [P] Rodar gate final do ticket — repositório inteiro — `make check`

## Dependencies

| Task | Depende de | Bloqueia |
| --- | --- | --- |
| T004 | T001–T003 | T005 |
| T005 | T004 | T006–T007 |
| T006–T007 | T005 | entrega |

## Parallel Example

```text
T001, T002 e T003 podem ser auditadas em paralelo; não alteram arquivos.
```

## Implementation Strategy

MVP = `uv sync` + teste de fumaça + `make check` verde. A auditoria corrigiu
o workflow para usar o mesmo gate local, sem reformatar documentos existentes.
