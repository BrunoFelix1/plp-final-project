# Quickstart: AST base e nós de expressão

Como provar o ticket de ponta a ponta (T2: Red → Green → Refactor).

## Pré-requisitos

- Branch `feat/009-ast-base-e-nos-de-expressao`; ambiente com `uv sync`.

## RED — teste primeiro

1. Criar `tests/unit/ast/test_nodes.py` com:
   - construção dos 15 nós (parametrizado);
   - árvore-exemplo da issue igual a cópia literal;
   - igualdade rasa e aninhada (mudar campo → diferentes);
   - `FrozenInstanceError` ao escrever atributo;
   - posição: padrão `0/0` e valores explícitos preservados.
2. Rodar: `uv run pytest tests/unit/ast/test_nodes.py -q`
   **Esperado**: falha (módulo `clite.ast.nodes` não existe).

## GREEN — implementar o mínimo

3. Criar `src/clite/ast/nodes.py` conforme [data-model.md](data-model.md) e o
   contrato [contracts/ast-nodes.md](contracts/ast-nodes.md).
4. Rodar: `uv run pytest tests/unit/ast/test_nodes.py -q`
   **Esperado**: verde.

## Refactor + verificação final

| Comando | Esperado |
| --- | --- |
| `uv run ruff check .` | sem achados |
| `uv run ruff format --check .` | sem divergência |
| `uv run mypy src` | sem erros |
| `uv run pytest -q` | suíte inteira verde, incl. `tests/quality` (números mágicos) |
| `uv run pytest tests/unit/ast/test_nodes.py -q` | comando do ticket, verde |
