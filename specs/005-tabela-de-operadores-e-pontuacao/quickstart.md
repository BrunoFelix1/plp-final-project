# Quickstart: validar a #7

Pré-requisito: `uv sync` (ou Docker com Python 3.12 + uv).

| Passo | Comando | Resultado esperado |
| --- | --- | --- |
| 1. Teste da feature | `uv run pytest tests/unit/lexer/test_operators.py -q` | todos passam; 23 lexemas |
| 2. Regressão do #6 | `uv run pytest tests/unit/lexer/test_scanner.py -q` | verde, só `@` como inválido |
| 3. Números mágicos | `uv run python -m tools.magic_numbers src tests tools scripts` | sem achados |
| 4. Gate completo | `uv run ruff check . && uv run mypy src && uv run pytest` | verde |

## Verificação manual (Python)

```python
from clite.lexer.lexer import Lexer
Lexer("a <= b").scan()   # IDENT; depois LESS_EQUAL "<=" na coluna 3
Lexer("a & b")           # scan() até o '&' levanta E1002 (linha 1, coluna 3)
```

Esperado: `a<=b` e `a < = b` dão sequências diferentes (`<=` vs `<` `=`).
