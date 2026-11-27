# Feature Specification: AST base e nós de expressão

**Feature Branch**: `feat/009-ast-base-e-nos-de-expressao`
**Created**: 2026-11-26 · **Status**: Draft
**Input**: ticket `feat: 009 - ast-base-e-nos-de-expressao` (issue #9)

## Conceito (projeto acadêmico)

**Sintaxe abstrata** (Tucker e Noonan §2.5.1–2.5.3; Apêndice A.2): a AST descarta
pontuação e parênteses e guarda só a estrutura que semântica e execução precisam.
É a representação intermediária sobre a qual o verificador de tipos e o avaliador
percorrerão; por ser dados puros e imutáveis (D-02), destrava o parser (010) em
paralelo. **Por que importa**: sem árvore canônica, cada fase reimplementaria
sua própria visão do programa. **Como verificar**: construção, igualdade,
imutabilidade e posição, cobertas por testes unitários.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Construir qualquer nó de `docs/01` §6 (Priority: P1)

O desenvolvedor constrói cada nó de §6 e a árvore-exemplo da issue
(`Assign(VarRef('x'), Binary('+', VarRef('x'), IntLiteral(1)))`).

**Why this priority**: é o contrato do ticket; sem os nós, nenhuma fase avança.

**Independent Test**: `uv run pytest tests/unit/ast/test_nodes.py -q`

**Acceptance Scenarios**:

1. **Given** módulo de nós importado, **When** construo os 17 nós de §6, **Then** nenhum falha.
2. **Given** dois nós com mesmos campos, **When** comparo, **Then** iguais; mudando um campo (mesmo aninhado), diferentes.
3. **Given** nó pronto, **When** tento alterar um campo, **Then** erro de imutabilidade.

### User Story 2 - Posição em todo nó (Priority: P2)

Cada nó carrega linha/coluna para as mensagens de erro das fases seguintes.

**Why this priority**: erros E1xxx–E4xxx reportam posição lida dos nós.

**Independent Test**: casos de posição no mesmo arquivo de teste.

**Acceptance Scenarios**:

1. **Given** nó sem posição informada, **When** inspeciono line/column, **Then** valor padrão "não informado".
2. **Given** nó com line/column explícitos, **When** inspeciono, **Then** valores preservados.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: O sistema MUST expor os nós de `docs/01` §6: `Program`, `VarDecl`, `ArrayDecl`, `Skip`, `Block`, `Assign`, `If`, `While`, `VarRef`, `ArrayRef`, `Binary`, `Unary`, `Convert`, `IntLiteral`, `FloatLiteral`, `BoolLiteral`, `CharLiteral`.
- **FR-002**: Todo nó MUST ser imutável e MUST carregar `line`/`column` (padrão "não informado"; aceita valor explícito).
- **FR-003**: O tipo declarado (declarações e conversão) MUST ser `int`, `float`, `char` ou `bool`.
- **FR-004**: Igualdade MUST comparar a estrutura completa (campos e subárvores).
- **FR-005**: Nenhum nó MUST conter lógica de execução ou de tipos (dados puros, D-02).

### Key Entities

- **Nó**: unidade imutável da árvore; campos de domínio + posição.
- **Aliases de união** (só tipos, sem lógica): `Declaration`, `Command`, `Expression`.

## Success Criteria *(mandatory)*

- **SC-001**: `uv run pytest tests/unit/ast/test_nodes.py -q` verde (construção, igualdade, imutabilidade, posição).
- **SC-002**: `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src` e `uv run pytest -q` verdes, incluindo `tests/quality` (números mágicos).

## Assumptions

- Nó `Print` (D-04) **fora** do escopo: ticket cobre só `docs/01` §6; entra com o parser.
- Dependência do ticket #4 já resolvida na `main`; `types.py` segue vazio até o ticket de semântica (o campo `tipo` usa o alias `CliteType` em `nodes.py`).
- Sem classes base/visitante agora; aliases de união bastam na v1.
- `ast/__init__.py` permanece intocado; imports diretos de `clite.ast.nodes`.

## Fora de escopo

1. Parser e semântica (ticket 010+).
2. Nó `Print` e extensões de observabilidade (D-04; divergência §3/§6 no ticket 033).
3. Nós OO (classes, campos, métodos — tickets 028/029).

## Riscos

| Risco | Mitigação |
| --- | --- |
| Parser (010, paralelo) esperar nó fora desta lista | tabela do FR-001 é o contrato; validar no `/speckit.plan` |
| Números mágicos nos testes dos nós | constantes nomeadas; `tests/quality` no check |

## Referências

`docs/01` §6/§12 · `docs/05` D-02, D-04, D-07 · `docs/03` §2, §4.2 · `docs/06` §2 · issue #9
