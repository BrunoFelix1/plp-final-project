# Data Model: Lexer de identificadores, literais e posição

## Entidades

| Entidade | Origem | Campos | Invariantes |
| --- | --- | --- | --- |
| `Token` | #5, não muda | `tag: Tag`, `lexeme: str`, `line: int`, `column: int` | `frozen`; `line`/`column` ≥ 1; `lexeme` é o texto original |
| `Tag` | #5, não muda | `IDENT` 256, `INT_LITERAL` 257, `FLOAT_LITERAL` 258, `CHAR_LITERAL` 259, `TRUE` 264, `FALSE` 265, `EOF` 300, reservadas | `IntEnum`; nomes do PR #44 |
| `KEYWORDS` | #5, não muda | `dict[str, Tag]` + `is_reserved()` | consultado antes de devolver `IDENT` |
| `Lexer` | novo | `source: str`, `index: int`, `line: int`, `column: int` | `0 ≤ index ≤ len(source)`; posição aponta o próximo caractere |
| `LexicalError` | novo | `code = "E1001"`, `line`, `column`, `message` | mensagem no formato `erro E1001 (linha L, coluna C): texto` |

## Estados do scanner

| Estado | Consome | Sai para |
| --- | --- | --- |
| inicial | espaço, tab, CR, LF, `//...` | inicial |
| inicial | letra | identificador/reservada |
| inicial | dígito | inteiro ou float |
| inicial | `'` | caractere |
| inicial | fim do fonte | `EOF` |
| inicial | qualquer outro | `E1001` |
| identificador | letra ou dígito | identificador |
| número | dígito | número |
| número | `.` seguido de dígito | float |
| número | `.` sem dígito | `E1001` no ponto |
| float | dígito | float |
| caractere | um imprimível e `'` | `CHAR_LITERAL` |
| caractere | qualquer outra forma | `E1001` na aspa inicial |

## Regras de validação

| Regra | Exemplo | Resultado |
| --- | --- | --- |
| Maior casamento | `whilea` | um `IDENT`, não `WHILE` + `IDENT` |
| Reservada antes de identificador | `while` | `Tag.WHILE` |
| Float exige dígitos dos dois lados | `5.0`, `0.5` | `FLOAT_LITERAL` |
| Float incompleto | `5.`, `.5` | `E1001` no ponto |
| Char único e imprimível | `'a'`, `' '` | `CHAR_LITERAL` |
| Char vazio ou longo | `''`, `'ab'` | `E1001` na aspa inicial |
| Comentário até o fim da linha | `// x` | descartado |
| Comentário sem newline | `// fim` | descartado, sem erro |
| Caractere desconhecido | `@` | `E1001` na posição do caractere |
| Operador/pontuação ainda não implementados | `;`, `+`, `(` | `E1001` até o #7 |

## Transições de posição

- Cada caractere consumido avança `column` em 1.
- Consumir `\n` faz `line += 1` e `column = 1`.
- `EOF` usa a posição do caractere após o último consumido (fim do fonte).
