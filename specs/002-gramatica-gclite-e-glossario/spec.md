# Feature Specification: Gramática GClite e glossário

**Feature Branch**: `docs/002-gramatica-gclite-e-glossario`
**Created**: 2026-11-19 · **Status**: Draft
**Input**: `docs: 002 - documentar a gramática de referência do núcleo CLite,
os tokens, a precedência, o glossário mínimo e o catálogo inicial de casos difíceis`

<!--
  REGRA DO PROJETO: meta de 70 linhas; se passar de 100, seja mais conciso.
  Tabelas e checklists em vez de prosa. Explique o conceito que será implementado.
  Não repita docs/01, docs/02, AGENTS.md nem tickets. Cite.
  Leia .specify/memory/constitution.md antes de preencher.
-->

## User Scenarios & Testing

### User Story 1 - Estudar a definição da linguagem (Priority: P1)

Como estudante, quero consultar uma única referência da sintaxe concreta e
abstrata para entender o que o parser deve reconhecer e o que a AST preserva.

**Why this priority**: evita que a implementação invente regras incompatíveis.

**Independent Test**: revisão de `docs/01-linguagem-clite.md` contra os itens do
ticket e abertura de cada link a partir de `docs/README.md`.

**Acceptance Scenarios**:

1. **Given** a gramática, **When** o leitor consulta `{ }` e `[ ]`, **Then** a
   cardinalidade e a opcionalidade ficam explícitas.
2. **Given** as tabelas de tokens e precedência, **When** o leitor analisa uma
   expressão, **Then** identifica tokens, ordem e associatividade.

---

### User Story 2 - Consultar termos e bordas (Priority: P2)

Como revisor, quero encontrar definições do vocabulário e casos traiçoeiros para
validar a documentação sem depender de conhecimento implícito.

**Independent Test**: conferir as seis entradas do glossário e o catálogo de
`docs/06-casos-dificeis.md`.

### Edge Cases

- `whilea`, `<=`, floats malformados, `else` pendente e comparações encadeadas;
  os comportamentos devem seguir `docs/06-casos-dificeis.md`.

## Requirements

### Functional Requirements

- **FR-001**: `docs/01-linguagem-clite.md` MUST conter a EBNF v1 completa e
  explicar `{ }` e `[ ]`, sintaxe concreta e sintaxe abstrata.
- **FR-002**: `docs/01-linguagem-clite.md` MUST conter tabelas completas de
  tokens e de precedência/associatividade.
- **FR-003**: A documentação MUST definir token, lexema, AST, parser, tabela de
  símbolos e type checking em linguagem de estudo.
- **FR-004**: `docs/06-casos-dificeis.md` MUST conter o catálogo inicial de
  casos léxicos, sintáticos, semânticos e de execução.
- **FR-005**: `docs/README.md` MUST apontar para os documentos existentes sem
  links quebrados.

### Key Entities

- **GClite**: gramática concreta de referência do núcleo CLite.
- **Glossário**: vocabulário mínimo para ler as fases do front-end.
- **Catálogo de casos difíceis**: entradas-limite e seus comportamentos esperados.

## Success Criteria

### Measurable Outcomes

- **SC-001**: Os 5 requisitos funcionais são verificáveis por revisão documental.
- **SC-002**: Os três links de documentação do ticket abrem arquivos existentes.
- **SC-003**: Uma revisão por pares confirma a checklist sem itens pendentes.

## Assumptions

- A gramática documentada é a v1; a extensão OO permanece em `docs/02`.
- Não há código, testes automatizados ou mudança de semântica neste ticket.

## Fora de escopo, riscos e referências

- **Fora de escopo**: implementar lexer/parser; alterar a extensão OO; criar testes
  executáveis para cada caso do catálogo.
- **Riscos**: divergência futura entre código e documentação — mitigar exigindo
  atualização conjunta em `docs/01`; glossário espalhado — mitigar com seção
  explícita e links no índice.
- **Referências**: `docs/01-linguagem-clite.md`, `docs/02-extensao-oo.md`,
  `docs/06-casos-dificeis.md`, Tucker e Noonan §§2.1.3, 2.3.1–2.3.2 e 2.5.1–2.5.3.
