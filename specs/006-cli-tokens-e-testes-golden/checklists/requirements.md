# Specification Quality Checklist: CLI `tokens` e testes golden

**Purpose**: validar completude e qualidade da spec antes do `/speckit.plan`
**Created**: 2026-11-25
**Feature**: [spec.md](../spec.md)

## Content Quality

- [X] No implementation details — cita só contratos existentes (`Tag`, `LexicalError`) e o comando.
- [X] Focused on user value — estudante, quem escreve programas e mantenedor.
- [X] Written for non-technical stakeholders — **com nota**: público é a equipe; token e lexema são vocabulário do domínio.
- [X] All mandatory sections completed.

## Requirement Completeness

- [X] No `[NEEDS CLARIFICATION]` markers remain.
- [X] Requirements are testable and unambiguous — FR-001 a FR-007 têm exemplo ou comando.
- [X] Success criteria are measurable — SC-001 a SC-003 nomeiam comando e resultado.
- [X] Success criteria are technology-agnostic — **com nota**: SC-003 usa os comandos exigidos em todo PR.
- [X] All acceptance scenarios are defined.
- [X] Edge cases are identified — vazio, inexistente, não-UTF-8, `' '`.
- [X] Scope is clearly bounded — "Fora de escopo" exclui parser e `--max-errors`.
- [X] Dependencies and assumptions identified — #7 em review (#46); `EOF` omitido é decisão da spec.

## Feature Readiness

- [X] All functional requirements have clear acceptance criteria.
- [X] User scenarios cover primary flows.
- [X] Feature meets measurable outcomes defined in Success Criteria.
- [X] No implementation details leak into specification.

## Notes

- Decisões de produto que o ticket não define (`EOF` não impresso; erro "tudo ou nada") ficam
  abertas em `checklists/cli.md` (CHK013) para revisão humana.
