# Feature Specification: Tabela de símbolos e resolução de nomes (ticket 012)

**Feature Branch**: `feat/012-tabela-de-simbolos-e-resolucao-de-nomes`
**Created**: 2026-11-27 · **Status**: Draft
**Input**: ticket #12 + plano aprovado na sessão (API AST-cêntrica; erro local no padrão da #7; branch stacked na `feat/009`)

## Conceito

A tabela de símbolos é a memória de nomes do front-end (Tucker e Noonan §4.4–4.5;
Apêndice A.3): mapeia cada nome declarado à sua declaração, para que o checker
resolva referências e rejeite erros antes de executar. Em CLite o escopo é único
(D-06): blocos não criam escopo, então a estrutura é um mapa plano
nome → declaração, em ordem de inserção.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Registrar e resolver nomes (Priority: P1)

O checker registra cada declaração do programa e resolve cada referência de nome
contra a tabela; quem consulta recebe a declaração original (nome, tipo, posição).

**Why this priority**: sem registro e busca não existe resolução de nomes.

**Independent Test**: `uv run pytest tests/unit/semantic/test_symbols.py -q`

**Acceptance Scenarios**:

1. **Given** declaração `int x;` registrada, **When** o nome `x` é buscado, **Then** a declaração original é devolvida (tipo `int`, posição da declaração).
2. **Given** array `int v[10];` registrado, **When** `v` é buscado, **Then** a declaração de array é devolvida.

### User Story 2 - Detectar declaração duplicada (Priority: P1)

Declarar o mesmo nome duas vezes é erro de programa (docs/06 §3): o segundo
registro falha com `E3002` na posição da segunda declaração.

**Why this priority**: unicidade de nomes é a regra A.3 aplicada ao programa.

**Independent Test**: mesmo comando da US1, cenários de erro.

**Acceptance Scenarios**:

1. **Given** `int x;` registrada, **When** `int x;` (linha 4, coluna 9) é registrada, **Then** erro `E3002` com linha 4 e coluna 9.
2. **Given** `int x;` registrada, **When** `float x;` é registrada, **Then** `E3002` (troca de tipo não contorna a unicidade).
3. **Given** blocos distintos, **When** o mesmo nome é declarado em cada um, **Then** `E3002` — escopo é único (D-06).

### User Story 3 - Sinalizar nome inexistente (Priority: P2)

Buscar um nome não declarado falha com `E3001` na posição da referência; a tabela
também expõe a lista de declarações, contrato com o checker (docs/03 §4.3).

**Why this priority**: habilita o `E3001` do checker e a coleta de declarações.

**Independent Test**: mesmo comando da US1.

**Acceptance Scenarios**:

1. **Given** tabela sem `x`, **When** `x` é buscado (linha 2, coluna 5), **Then** erro `E3001` com linha 2 e coluna 5.
2. **Given** três declarações registradas, **When** a lista é consultada, **Then** as três aparecem em ordem de inserção.

### Edge Cases

- Mesmo nome em bloco interno → duplicado (D-06; docs/06 §3).
- `int v[5]; int v[5];` → `E3002`.
- Busca sem posição informada → `E3001` com posição "não informada" (0, 0), como na AST.
- Tabela vazia: busca falha com `E3001`; lista devolvida é vazia.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: O sistema MUST registrar declarações de variável simples e de array, com nome, tipo e posição.
- **FR-002**: O sistema MUST resolver um nome declarado, devolvendo a declaração original.
- **FR-003**: O sistema MUST rejeitar a segunda declaração de um nome já registrado com `E3002` e a posição da segunda declaração.
- **FR-004**: O sistema MUST sinalizar busca de nome inexistente com `E3001` e a posição da referência.
- **FR-005**: O sistema MUST expor as declarações na ordem em que foram registradas.
- **FR-006**: O sistema MUST manter escopo único: blocos não criam escopo (D-06).
- **FR-007**: Todo erro MUST seguir o formato `erro E<NNNN> (linha L, coluna C): texto`, em português (docs/03 §5).

### Key Entities

- **Declaração**: nó da AST com nome, tipo e posição (variável simples ou array).
- **Tabela de símbolos**: mapa plano nome → declaração, escopo único, ordem de inserção preservada.
- **Erro semântico**: diagnóstico com código `E3xxx`, linha, coluna e mensagem em português.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `uv run pytest tests/unit/semantic/test_symbols.py -q` verde, cobrindo declaração, duplicidade, busca e exposição da lista.
- **SC-002**: `make check` verde com os testes novos (lint, tipos estritos, suíte completa).
- **SC-003**: Cada cenário de erro evidencia código, linha e coluna na mensagem.

## Assumptions

- API AST-cêntrica (decisão aprovada no plano): a tabela recebe e devolve os nós de declaração da #9; `declare('x', IntType)` do ticket equivale a registrar a declaração de `x` com tipo `int`.
- Erro semântico definido no próprio módulo, no padrão da `LexicalError` da #7; a hierarquia global de erros é a issue #19 (M3), que absorverá ambos.
- Tipos permanecem os literais da AST (`"int"`, `"float"`, `"char"`, `"bool"`); `types.py` segue esqueleto.
- Fora de escopo: escopo de bloco, classes/métodos (v2) e mudança de gramática (`docs/01` intocado).
