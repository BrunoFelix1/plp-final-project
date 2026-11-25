# Research: Lexer de identificadores, literais e posição

Decisões técnicas que a spec não fixa. Todas partem de `docs/01` §4, `docs/06` §1,
D-12 e do contrato já entregue pelo #5.

## D1. Onde definir o erro `E1001`

- **Decisão**: `class LexicalError(Exception)` em `src/clite/lexer/lexer.py`, com
  `code`, `line`, `column` e `message`; `str()` no formato de D-12.
- **Por quê**: `errors.py` é arquivo do ticket #19 (`erros-diagnosticos-e-recuperacao`);
  editar agora criaria conflito de escopo e de merge.
- **Alternativas**: (a) `errors.py` — viola a lista de arquivos do #6; (b) `ValueError`
  — não carrega código nem posição, quebra o teste de erro.

## D2. Emitir token de `EOF`

- **Decisão**: ao esgotar o fonte, `scan()` devolve `Token(Tag.EOF, "", linha, coluna)`
  e continua devolvendo `EOF` nas chamadas seguintes.
- **Por quê**: o parser do #10/#11 precisa de um terminador estável; `Tag.EOF` já
  existe (300) e evita `StopIteration` no meio da fase seguinte.
- **Alternativas**: `StopIteration`/`None` — obrigaria o parser a tratar dois casos.

## D3. Contagem de linha e coluna

- **Decisão**: ambas 1-based; a coluna aponta o primeiro caractere do lexema; ao
  consumir `\n`, `line += 1` e `column = 1`.
- **Por quê**: `docs/01` §4.3.6 e D-12 exigem posição para o diagnóstico.
- **Alternativas**: coluna 0-based — divergiria dos exemplos de `docs/06`.

## D4. Ordem de reconhecimento

- **Decisão**: espaço/comentário → identificador/reservada → número → caractere →
  erro. `//` só é comentário quando não está dentro de literal.
- **Por quê**: garante maior casamento (`whilea`) e `'/'` como char válido.
- **Alternativas**: tentar comentário depois de `/` — conflita com o operador do #7.

## D5. Float malformado e `1.2.3`

- **Decisão**: `5.` e `.5` falham no ponto; em `1.2.3`, emite `FLOAT_LITERAL "1.2"`
  e falha no segundo ponto.
- **Por quê**: `docs/01` §4.3.3 e `docs/06` §1 descrevem exatamente isso.
- **Alternativas**: aceitar `5.` como float — gramática proíbe.

## D6. Constantes em vez de números mágicos

- **Decisão**: `WHITESPACE = " \t\r\n"`, `DOT = "."`, `QUOTE = "'"`, `SLASH = "/"`,
  `NEWLINE = "\n"`; índices usam `0`/`1`, permitidos por AGENTS §5.6.
- **Por quê**: `tools.magic_numbers` falha o CI com números soltos.
- **Alternativas**: `# magic: allow` — só com justificativa e evitável aqui.
