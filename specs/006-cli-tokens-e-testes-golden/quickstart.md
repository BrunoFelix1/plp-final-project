# Quickstart: validar a #8

Pré-requisito: `uv sync` (ou Docker com Python 3.12 + uv); #7 na branch.

| Passo | Comando | Resultado esperado |
| --- | --- | --- |
| 1. CLI | `uv run clite tokens examples/lexico/basico.clite` | uma linha por token, exit `0` |
| 2. Erro | `uv run clite tokens examples/lexico/erro_caractere.clite; echo $?` | uma linha `erro E1001 …` e `1` |
| 3. Testes | `uv run pytest tests/unit/test_cli_tokens.py -q` | goldens e exit codes passam |
| 4. Mágicos | `uv run python -m tools.magic_numbers src tests tools scripts` | sem achados |
| 5. Gate | `uv run ruff check . && uv run mypy src && uv run pytest -q` | verde |

## Prova de que o golden protege

Altere uma linha de `tests/golden/lexer/basico.tokens` e rode o passo 3: o teste deve
falhar apontando a linha. Reverta com `git checkout -- tests/golden/lexer/basico.tokens`.
