# Feature Specification: CLI `tokens` e testes golden

**Feature Branch**: `feat/008-cli-tokens-e-testes-golden`
**Created**: 2026-11-25 · **Status**: Draft
**Input**: `feat: 008 - cli-tokens-e-testes-golden` (#8)

<!-- REGRA DO PROJETO: meta de 70 linhas; não repita docs/01, docs/02 nem o ticket. -->

## Conceito

**Testar a gramática léxica pelos terminais.** Expor a sequência de tokens na CLI
permite validar o léxico sem parser e comparar a saída com a especificação: é a
separação prática entre reconhecer e analisar (Compiladores §3.1 e §3.4; Tucker
§2.3.1). Um teste *golden* congela a saída esperada de um programa em arquivo; se o
léxico mudar, o diff mostra exatamente o que mudou.

## User Scenarios & Testing

### User Story 1 - Ver os tokens de um programa (Priority: P1)

Como estudante, quero rodar `clite tokens arquivo.clite` e ler uma linha por token,
para conferir o léxico sem precisar do parser.

**Independent Test**: `uv run clite tokens examples/lexico/basico.clite`

**Acceptance Scenarios**:

1. **Given** `int x;`, **Then** `INT int 1:1`, `IDENT x 1:5` e `SEMICOLON ; 1:6`.
2. **Given** o mesmo arquivo duas vezes, **Then** a saída é idêntica byte a byte.
3. **Given** um arquivo vazio, **Then** nenhuma linha e exit `0`.

### User Story 2 - Falhar com uma mensagem (Priority: P2)

Como quem escreve programas, quero uma única mensagem `E1xxx` e exit `1` quando o
léxico falha, para corrigir sem ruído.

**Independent Test**: `uv run pytest tests/unit/test_cli_tokens.py -q`

**Acceptance Scenarios**:

1. **Given** `a @ b`, **Then** uma linha em stderr (`erro E1001 (linha 1, coluna 3): …`),
   stdout vazio e exit `1`.
2. **Given** `a & b`, **Then** `E1002` com a mesma regra.

### User Story 3 - Congelar o léxico (Priority: P2)

Como mantenedor, quero arquivos golden versionados, para que mudança no léxico apareça
como diff de teste.

**Independent Test**: um teste parametrizado sobre `tests/golden/lexer/`.

**Acceptance Scenarios**:

1. **Given** ≥3 programas em `examples/lexico/`, **Then** cada um tem saída esperada
   em `tests/golden/lexer/` e o teste compara byte a byte.

### Edge Cases

- Arquivo inexistente: `erro: arquivo não encontrado` e exit `2` (já existe no #4).
- Arquivo que não é UTF-8: mensagem em stderr e exit `2`.
- Char com espaço (`' '`) sai como `CHAR_LITERAL ' ' 1:1`; o lexema mantém as aspas.

## Requirements

### Functional Requirements

- **FR-001**: `clite tokens <arquivo>` imprime uma linha por token: `TAG lexema linha:coluna`.
- **FR-002**: O `EOF` não é impresso; arquivo vazio gera saída vazia e exit `0`.
- **FR-003**: Erro léxico: exit `1`, uma única linha `erro E1xxx (linha L, coluna C): …` em
  stderr, nada em stdout (tudo ou nada).
- **FR-004**: Erros de uso da CLI (arquivo ausente, ilegível) saem com `2`; sucesso com `0`.
- **FR-005**: Existem ao menos 3 programas em `examples/lexico/` com golden em
  `tests/golden/lexer/` (saída esperada em `.tokens`; erro em `.err`).
- **FR-006**: Os demais subcomandos continuam `E9000` com exit `2`.
- **FR-007**: `docs/03` §6 descreve o formato de saída do `tokens` e os códigos de saída.

## Success Criteria

### Measurable Outcomes

- **SC-001**: O comando do ticket imprime uma linha por token do `basico.clite`.
- **SC-002**: Os goldens passam; alterar uma linha de um golden faz o teste falhar.
- **SC-003**: `pytest`, `ruff check`, `mypy src` e `tools.magic_numbers` verdes.

## Fora de escopo

- Parser, AST e `--max-errors` (#11, #19); regeneração automática dos goldens.

## Riscos

| Risco | Mitigação |
| --- | --- |
| Depende do #7, ainda em review (#46) | empilhar a branch e ligar o PR depois do merge |
| Golden frágil a fim de linha no Windows | `.gitattributes` já normaliza para LF |

## Assumptions

- `EOF` é marcador interno do scanner, não um token do programa (decisão desta spec).
- Erro reaproveita o formato do `LexicalError` (D-12), sem stack trace. Pastas `examples/lexico/` e
  `tests/golden/lexer/` já constam em `examples/README.md`.
