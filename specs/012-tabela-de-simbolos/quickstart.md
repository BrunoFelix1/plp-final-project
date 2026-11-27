# Quickstart: validar a tabela de símbolos (ticket 012)

## Pré-requisitos

- Ambiente sincronizado: `uv sync`
- Branch: `feat/012-tabela-de-simbolos-e-resolucao-de-nomes` (base: `feat/009`)

## Comandos de validação

```bash
# 1. Teste do ticket — declaração, duplicidade, busca, exposição
uv run pytest tests/unit/semantic/test_symbols.py -q
# Antes da implementação: coleta falha (arquivo não existe) = RED.

# 2. Qualidade geral (mesmo do CI; make check no Linux/macOS)
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
```

## Cenários cobertos (mapa teste → expectativa)

| Cenário | Teste | Esperado |
| --- | --- | --- |
| `int x;` registrado e buscado | declara e resolve | devolve o próprio `VarDecl` |
| array `int v[10];` registrado e buscado | declara e resolve (array) | devolve o próprio `ArrayDecl` |
| `int x; int x;` (2ª: linha 4, coluna 9) | duplicado | `SemanticError` code=E3002, line=4, column=9 |
| `int v[5]; int v[5];` | duplicado (array) | E3002 |
| `int x; float x;` | duplicado (tipo diferente) | E3002 |
| busca sem registrar (linha 2, coluna 5) | inexistente | code=E3001, line=2, column=5 |
| busca sem posição | inexistente (sem posição) | E3001 com (0, 0) |
| três declarações | lista em ordem | lista na ordem de inserção |
| tabela vazia | tabela vazia | E3001 na busca; lista vazia |

## Critério de pronto

- SC-001/SC-002/SC-003 da spec: comandos acima verdes e cada erro exibindo
  código, linha e coluna na mensagem.
