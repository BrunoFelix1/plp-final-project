# Feature Specification: [FEATURE NAME]

**Feature Branch**: `[###-feature-name]`
**Created**: [DATE] · **Status**: Draft
**Input**: "$ARGUMENTS"

<!--
  REGRA DO PROJETO: no máximo 1 página. Tabelas e checklists em vez de prosa.
  Não repita docs/01, docs/02, AGENTS.md nem tickets. Cite.
  Leia .specify/memory/constitution.md antes de preencher.
-->

## User Scenarios & Testing *(mandatory)*

### User Story 1 - [título] (Priority: P1)

[1–2 frases: quem faz o quê e por quê.]

**Why this priority**: [valor em uma frase]

**Independent Test**: [comando ou programa `.clite` que prova sozinho]

**Acceptance Scenarios**:

1. **Given** [estado], **When** [ação], **Then** [resultado observável].
2. **Given** [estado], **When** [ação], **Then** [erro/código esperado].

---

### User Story 2 - [título] (Priority: P2)

[Opcional. Mesma estrutura, no máximo 3 histórias.]

### Edge Cases

- [Entrada de borda e comportamento esperado — ver docs/06-casos-dificeis.md]

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: O sistema MUST [capacidade específica].
- **FR-002**: O sistema MUST [capacidade específica].
- **FR-003**: O sistema MUST rejeitar [entrada] com [código/posição].

### Key Entities

- **[Entidade]**: [o que representa, sem detalhe de implementação]

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: [critério verificável por comando ou saída esperada]
- **SC-002**: [`make check` verde com N testes novos]

## Assumptions

- [Premissa de escopo, ambiente ou dependência]
