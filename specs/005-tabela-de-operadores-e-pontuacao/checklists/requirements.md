# Specification Quality Checklist: Tabela de operadores e pontuação

**Purpose**: validar completude e qualidade da spec antes do `/speckit.plan`
**Created**: 2026-11-25
**Feature**: [spec.md](../spec.md)

## Content Quality

- [X] No implementation details — cita só contratos já entregues (`Token`, `Tag`,
      `LexicalError`, `Lexer.scan()`); o desenho da tabela fica no plan.
- [X] Focused on user value — beneficiários são o parser e quem escreve programas.
- [X] Written for non-technical stakeholders — **com nota**: o público é a equipe;
      token, lexema e maior casamento são o vocabulário do domínio.
- [X] All mandatory sections completed.

## Requirement Completeness

- [X] No `[NEEDS CLARIFICATION]` markers remain.
- [X] Requirements are testable and unambiguous — FR-001 a FR-007 têm caso ou regra
      verificável em docs/01 §4.2–4.3 e no ticket #7.
- [X] Success criteria are measurable — SC-001 conta 23 lexemas; SC-002 nomeia os
      códigos; SC-003 nomeia os comandos.
- [X] Success criteria are technology-agnostic — **com nota**: SC-003 usa os comandos
      que o projeto exige em todo PR.
- [X] All acceptance scenarios are defined.
- [X] Edge cases are identified — `&&&`, `|||`, `a//b`, `-1`, `===`, `5.`.
- [X] Scope is clearly bounded — "Fora de escopo" exclui precedência (#10) e CLI (#8).
- [X] Dependencies and assumptions identified — #5, #6 e #44; E1002 só no ticket.

## Feature Readiness

- [X] All functional requirements have clear acceptance criteria.
- [X] User scenarios cover primary flows.
- [X] Feature meets measurable outcomes defined in Success Criteria.
- [X] No implementation details leak into specification.

## Notes

- **Para o revisor decidir**: o ticket #7 não lista `src/clite/lexer/lexer.py` em
  "Arquivos que toca", mas o scanner do #6 precisa ser alterado (FR-003, FR-006).
- `E1002` não existe em docs/01, docs/03 nem docs/06 hoje; FR-007 o registra.
