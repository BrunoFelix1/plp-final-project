# Contrato: lexer → parser

Interface que o ticket #6 entrega e que o #7 (operadores) e o #10/#11 (parser)
consomem. Não descreve a implementação interna.

## API pública

```python
from clite.lexer.lexer import Lexer, LexicalError
from clite.lexer.tokens import Token


class Lexer:
    def __init__(self, source: str) -> None: ...
    def scan(self) -> Token: ...


class LexicalError(Exception):
    code: str  # "E1001"
    line: int  # 1-based
    column: int  # 1-based
    message: str  # texto sem código nem posição
```

## Pré-condições

- `source` é `str`; o alfabeto é ASCII imprimível mais espaço/tab/CR/LF
  (`docs/01` §4.1).
- `scan()` pode ser chamado repetidamente até receber `EOF`.

## Pós-condições

| Situação | Resultado |
| --- | --- |
| Identificador | `Token(Tag.IDENT, lexeme, line, column)` |
| Inteiro | `Token(Tag.INT_LITERAL, lexeme, line, column)` |
| Float válido | `Token(Tag.FLOAT_LITERAL, lexeme, line, column)` |
| Booleano | `Token(Tag.TRUE/FALSE, lexeme, line, column)` |
| Caractere | `Token(Tag.CHAR_LITERAL, lexeme, line, column)` |
| Reservada | `Token(KEYWORDS[lexeme], lexeme, line, column)` |
| Fim do fonte | `Token(Tag.EOF, "", line, column)`; chamadas seguintes repetem `EOF` |
| Entrada inválida | levanta `LexicalError` com `code`, `line` e `column` |

- `lexeme` é sempre o texto original, sem normalização.
- `line`/`column` apontam o **primeiro** caractere do lexema.
- O scanner para no primeiro erro (D-12); não há recuperação nesta fatia.

## Exemplos normativos

| Fonte | Tokens (tag e lexeme) |
| --- | --- |
| `abc abc123` | `IDENT "abc"`, `IDENT "abc123"` |
| `42 3.14` | `INT_LITERAL "42"`, `FLOAT_LITERAL "3.14"` |
| `true false` | `TRUE "true"`, `FALSE "false"` |
| `'a'` | `CHAR_LITERAL "'a'"` |
| `while` | `WHILE "while"` |
| `whilea` | `IDENT "whilea"` |
| `5.` | `LexicalError` no ponto |
| `''` | `LexicalError` na aspa |
| `;` | `LexicalError` no caractere (até o #7) |

## Fora do contrato

- Operadores e pontuação (`<=`, `;`, `(`, …) — ticket #7; até lá, `E1001`.
- Recuperação de erro, múltiplos diagnósticos e hierarquia em `errors.py` — #19.
- Conversão de `lexeme` para valor (`int`, `float`, `char`) — interpretador.
