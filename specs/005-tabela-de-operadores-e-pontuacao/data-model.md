# Data Model: Tabela de operadores e pontuação

Fonte: `docs/01` §4.2 e `Tag` (`src/clite/lexer/tags.py`, nomes do PR #44).

| Lexema | Tag | Lexema | Tag |
| --- | --- | --- | --- |
| `=` | `ASSIGN` | `&&` | `LOGICAL_AND` |
| `==` | `EQUAL` | `\|\|` | `LOGICAL_OR` |
| `!=` | `NOT_EQUAL` | `!` | `NOT` |
| `<` | `LESS_THAN` | `+` | `PLUS` |
| `<=` | `LESS_EQUAL` | `-` | `MINUS` |
| `>` | `GREATER_THAN` | `*` | `STAR` |
| `>=` | `GREATER_EQUAL` | `/` | `SLASH` |
| `%` | `PERCENT` | `[` `]` | `LBRACKET` `RBRACKET` |
| `;` `,` | `SEMICOLON` `COMMA` | `{` `}` | `LBRACE` `RBRACE` |
| `(` `)` | `LPAREN` `RPAREN` | | |

Total: 17 operadores + 6 pontuações = 23 lexemas.

## Regras derivadas da tabela

- **Compostos**: lexemas de 2 caracteres (`==`, `!=`, `<=`, `>=`, `&&`, `||`).
- **Prefixo isolado inválido**: primeiro caractere de um composto que não é lexema
  sozinho. Hoje: `&` e `|`. (`=`, `!`, `<`, `>` valem sozinhos.)
- **Entidades já existentes, sem mudança**: `Token`, `Tag`, `KEYWORDS`.
- **`LexicalError`**: passa a aceitar o código; padrão continua `E1001`.
