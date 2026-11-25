# Feature Specification: Tabela de operadores e pontuação

**Feature Branch**: `feat/007-tabela-de-operadores-e-pontuacao`
**Created**: 2026-11-25 · **Status**: Draft
**Input**: `feat: 007 - tabela-de-operadores-e-pontuacao` (#7)

<!-- REGRA DO PROJETO: meta de 70 linhas; não repita docs/01, docs/02 nem o ticket. -->

## Conceito

**Tokens compostos e tabela de terminais.** `<=`, `==`, `&&` são um token só; o
scanner lê o caractere seguinte antes de decidir (maior casamento, docs/01 §4.3),
senão `<=` viraria `<` e `=`. A tabela lexema → tag é o contrato único entre o
léxico e a gramática (Tucker §2.3.1; Compiladores §3.3). Objetivo: o scanner passa
a reconhecer os 23 lexemas de operadores e pontuação de docs/01 §4.2.

## User Scenarios & Testing

### User Story 1 - Reconhecer operadores e pontuação (Priority: P1)

Como parser, quero cada operador e sinal de pontuação como um token classificado e
posicionado, para não olhar caracteres.

**Why this priority**: sem eles o scanner do #6 rejeita `int x;`; o #8 depende disto.

**Independent Test**: `uv run pytest tests/unit/lexer/test_operators.py -q`

**Acceptance Scenarios**:

1. **Given** cada um dos 23 lexemas de docs/01 §4.2, **Then** um token com a tag
   própria, o lexema original e a posição do primeiro caractere.
2. **Given** `a<=b` e `a < = b`, **Then** `IDENT <= IDENT` e `IDENT < = IDENT`.
3. **Given** `x = y == z`, **Then** `=` e `==` distintos (maior casamento).

### User Story 2 - Rejeitar `&` e `|` isolados (Priority: P2)

Como quem escreve programas, quero erro claro para `&` ou `|` sozinhos, para
corrigir `&&`/`||` sem adivinhar.

**Independent Test**: casos de erro em `tests/unit/lexer/test_operators.py`.

**Acceptance Scenarios**:

1. **Given** `a & b` ou `a | b`, **Then** `E1002` na posição do símbolo.
2. **Given** `@`, **Then** continua `E1001` (caractere desconhecido).

### Edge Cases

- `&&&` → `&&` e depois `E1002` na coluna 3; `|||` idem.
- `a//b` é comentário; `a/b` e `a / b` dão `/`. `-1` é `-` e `1` (sem literal negativo).
- `!` sozinho é NOT e `!=` é um token; `=`, `==` e `===` → `==` e `=`.
- `1+2` → INT `+` INT; `5.` continua `E1001`; `.` isolado também.

## Requirements

### Functional Requirements

- **FR-001**: Reconhecer os 17 operadores e as 6 pontuações de docs/01 §4.2, cada
  um com sua tag, lexema e posição (linha/coluna 1-based).
- **FR-002**: Aplicar maior casamento: `<=`, `>=`, `==`, `!=`, `&&`, `||` são um token.
- **FR-003**: Uma única tabela lexema → tag define operadores e pontuação; o scanner
  a consulta e não repete lexemas.
- **FR-004**: `&` ou `|` isolado falha com `E1002`, linha e coluna do símbolo.
- **FR-005**: Qualquer outro caractere desconhecido segue `E1001`.
- **FR-006**: Atualizar o teste do #6 que fixa `;`, `+` e `(` como `E1001`: só `@` fica.
- **FR-007**: Registrar `E1002` em docs/06 (linha de `&` sozinho) e na tabela de erros de docs/03.

### Key Entities

- **Tabela de operadores**: mapa lexema → `Tag`; usa `Tag` do #5 (nomes do PR #44).
- **LexicalError**: já existe no #6 com código fixo `E1001`; precisa carregar `E1002`.

## Success Criteria

### Measurable Outcomes

- **SC-001**: Os 23 lexemas geram a tag esperada no teste, um caso por lexema.
- **SC-002**: `&` e `|` isolados geram `E1002` com linha e coluna; `@` gera `E1001`.
- **SC-003**: `pytest`, `ruff check`, `mypy src` e `tools.magic_numbers` verdes.

## Fora de escopo

- Precedência e associatividade (parser, #10). CLI `tokens` e golden (#8).

## Riscos

| Risco | Mitigação |
| --- | --- |
| `LexicalError` tem `E1001` fixo (#6) | alteração mínima, cobrir `E1001` e `E1002` |
| `scan()` do #6 precisa ramificar por operador | manter a tabela como única fonte (FR-003) |
| Ticket não lista `lexer.py` em "Arquivos que toca" | corrigir o ticket antes do plan |

## Assumptions

- #5 e #6 estão na `main`; `Token`, `KEYWORDS` e `Lexer.scan()` não são redefinidos.
- `E1002` vem só do ticket; docs/01 e docs/06 dizem "erro léxico" sem o código.
- Recuperação e múltiplos erros ficam para o #19; sem números mágicos (AGENTS §5.6).
