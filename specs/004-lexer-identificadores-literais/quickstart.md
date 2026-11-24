# Quickstart: validar o lexer do #6

Guia de verificação. O contrato está em [`contracts/lexer.md`](./contracts/lexer.md);
os casos detalhados, em [`data-model.md`](./data-model.md).

## Pré-requisitos

```bash
uv sync
```

## 1. Teste do ticket

```bash
uv run pytest tests/unit/lexer/test_scanner.py -q
```

Esperado: todos os testes do scanner passando, incluindo os cinco casos de erro.

## 2. Prova manual — tokens válidos

```bash
uv run python -c "from clite.lexer.lexer import Lexer; l=Lexer(\"abc 42\"); print(l.scan()); print(l.scan()); print(l.scan())"
```

Esperado:

```text
Token(tag=<Tag.IDENT: 256>, lexeme='abc', line=1, column=1)
Token(tag=<Tag.INT_LITERAL: 257>, lexeme='42', line=1, column=5)
Token(tag=<Tag.EOF: 300>, lexeme='', line=1, column=7)
```

## 3. Prova manual — erro com posição

```bash
uv run python -c "from clite.lexer.lexer import Lexer; Lexer('5.').scan()"
```

Esperado: a última linha da saída é
`LexicalError: erro E1001 (linha 1, coluna 2): ...` — o ponto é o segundo
caractere. O comando termina com código diferente de zero de propósito.

## 4. Gate completo (mesmo do PR)

```bash
uv run ruff check .
uv run mypy src
uv run pytest -q
uv run python -m tools.magic_numbers src tests tools scripts
```

Esperado: lint e tipos sem achados, suíte verde, nenhum número mágico.

## Critério de pronto

- [ ] Os sete lexemas do ticket produzem os tokens esperados.
- [ ] `5.`, `.5`, `''`, `'ab'` e `@` produzem `E1001` com linha e coluna.
- [ ] `;`, `+` e `(` produzem `E1001` até o #7 (decisão A).
- [ ] `whilea` é um `IDENT`; comentários e espaços não geram token.
- [ ] O gate completo passa.
