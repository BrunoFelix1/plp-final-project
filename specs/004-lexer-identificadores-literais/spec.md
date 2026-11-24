# Feature Specification: Lexer de identificadores, literais e posição

**Feature Branch**: `feat/006-lexer-identificadores-literais-e-posicao`
**Created**: 2026-11-24 · **Status**: Draft
**Input**: `feat: 006 - lexer-identificadores-literais-e-posicao` (#6)

<!-- REGRA DO PROJETO: meta de 70 linhas; não repita docs/01, docs/02 nem o ticket. -->

## Conceito

**Maior casamento sobre um autômato finito.** O scanner é uma máquina de estados:
cada caractere move o estado e o token só sai quando nenhum outro pode continuar o
lexema. Por isso `whilea` é identificador e `5.` é erro (Tucker §3.2.2;
Compiladores §3.4 e §3.6). A fronteira testada é texto → `Token(tag, lexeme,
linha, coluna)`. Operadores e recuperação de erro não entram aqui.

## User Scenarios & Testing

### User Story 1 - Produzir tokens classificados (Priority: P1)

Como parser, quero identificadores, literais e reservadas já classificados e
posicionados, para nunca lidar com texto bruto.

**Why this priority**: é a entrada de todas as fases seguintes do front-end.

**Independent Test**: `uv run pytest tests/unit/lexer/test_scanner.py -q`

**Acceptance Scenarios**:

1. **Given** `abc abc123 42 3.14 true 'a' while`, **Then** IDENT, IDENT, INT,
   FLOAT, TRUE, CHAR e WHILE, na ordem, com o lexema original.
2. **Given** `whilea`, **Then** um único IDENT (maior casamento), não WHILE + IDENT.
3. **Given** espaços, tabs e quebras, **Then** nenhum token e a linha avança;
   `a<b` e `a < b` produzem a mesma sequência.

### User Story 2 - Falhar com posição (Priority: P2)

Como quem escreve programas, quero que entrada inválida falhe com `E1001` e
posição, para corrigir sem adivinhar.

**Independent Test**: casos de erro em `tests/unit/lexer/test_scanner.py`.

**Acceptance Scenarios**:

1. **Given** `5.` ou `.5`, **Then** `E1001` com linha e coluna do ponto.
2. **Given** `''` ou `'ab'`, **Then** `E1001` na aspa inicial.
3. **Given** `@`, **Then** `E1001` com a posição do caractere.

### Edge Cases

- `1.2.3` → FLOAT `1.2` e `E1001` no segundo ponto (docs/06 §1).
- `' '` é CHAR válido; `''` e `'ab'` não. Comentário sem newline é ignorado.
- `int x;` gera `INT`, `IDENT` e `E1001` no `;` até o #7 (decisão CHK015).
- Reservada nunca vira identificador: a tabela é consultada antes (docs/01 §4.4).

## Requirements

### Functional Requirements

- **FR-001**: Identificador: letra seguida de letras/dígitos, com maior casamento.
- **FR-002**: Inteiro: sequência de dígitos.
- **FR-003**: Float: dígitos dos dois lados do ponto; `5.` e `.5` são erro.
- **FR-004**: `true` e `false` são booleanos, não identificadores.
- **FR-005**: Caractere: exatamente um imprimível entre aspas simples, sem escapes.
- **FR-006**: Reservada: consultar `KEYWORDS`/`is_reserved` (#5) antes do IDENT.
- **FR-007**: Ignorar espaço, tab, CR, LF e comentário `//` até o fim da linha.
- **FR-008**: Todo token carrega linha e coluna 1-based do primeiro caractere.
- **FR-009**: Rejeitar `5.`, `.5`, `''`, `'ab'` e caractere desconhecido com
  `E1001`, informando linha e coluna.
- **FR-010**: Operadores e pontuação ficam para o #7; até lá, qualquer caractere
  fora do subconjunto do 006 (inclusive `;`, `+`, `(`) falha com `E1001`.

### Key Entities

- **Token**: tag, lexeme, linha, coluna — existe em `src/clite/lexer/tokens.py`.
- **Tag**: categoria do token; nomes atuais vêm do PR #44.
- **Reservadas**: `KEYWORDS` e `is_reserved()` — existem desde o #5.

## Success Criteria

### Measurable Outcomes

- **SC-001**: Os sete lexemas do ticket geram os tokens esperados no teste.
- **SC-002**: Os quatro casos inválidos geram `E1001` com linha e coluna no teste.
- **SC-003**: `pytest`, `ruff check`, `mypy src` e `tools.magic_numbers` verdes.

## Assumptions

- O #5 está entregue; `Token`, `KEYWORDS` e `is_reserved` não são redefinidos.
- Operadores/pontuação entram no #7; recuperação e múltiplos erros, no #19.
- O scanner consulta `KEYWORDS` em vez de hardcodar tag (protege contra o PR #44).
- Sem números mágicos: valores de domínio viram constantes nomeadas (AGENTS §5.6).
- `docs/03` define `src/clite/lexer/lexer.py` com `Lexer.scan()` como entrada da fase.
