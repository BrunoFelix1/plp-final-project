# Convergência: Bootstrap Python, uv e CI

**Resultado**: convergido · 2026-11-18 · ticket `chore: 001` (#1)

## Verificação

| Item | Evidência | Resultado |
| --- | --- | --- |
| FR-001 / SC-001 | `uv sync --frozen` | passou |
| FR-002 / SC-002 | `make check` | passou |
| FR-003 / AC3 | workflow chama `make check` em PR para `main` | atendido |
| FR-004 / AC2 | `uv run pytest -q` | 1 teste passou |
| Constituição | sem mudança de gramática ou runtime | atendida |

## Correção aplicada

O workflow substituiu gates duplicados por `make check`. A versão anterior
incluía `ruff format --check .`, que falhava ao formatar um exemplo Markdown da
constituição; a correção evita alterar documento protegido pela regra T0 e torna
local e CI equivalentes.

## Comandos finais

```text
uv sync --frozen && make check
uv run pytest -q
uv run ruff check .
uv run mypy src
git diff --check
```

Todos terminaram com código 0. Não há tasks de convergência pendentes.

## Fora de escopo e referências

- Lexer, parser, semântica, interpretador e publicação continuam fora do ticket.
- Referências: `spec.md`, `plan.md`, `tasks.md`, `AGENTS.md` §3 e `docs/03` §1.
