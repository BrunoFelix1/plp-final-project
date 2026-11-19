# Checklist de requisitos: fundação de qualidade

**Spec**: [spec.md](../spec.md) · **Plano**: [plan.md](../plan.md)

## Completude

- [ ] CHK001 Os quatro FRs têm uma tarefa ou critério de aceite rastreável?
  [Completeness, Spec §Requirements]
- [ ] CHK002 O requisito de execução em pull requests está explicitamente
  limitado à branch `main`? [Clarity, Spec §FR-003]

## Consistência e mensuração

- [ ] CHK003 `make check` e o workflow descrevem o mesmo conjunto mínimo de
  gates, sem conflito de responsabilidades? [Consistency, Spec §SC-002]
- [ ] CHK004 Os critérios distinguem instalação reprodutível de execução de
  testes? [Measurability, Spec §SC-001–SC-002]

## Cenários e limites

- [ ] CHK005 O cenário de clone limpo e o cenário de falha do teste de fumaça
  estão suficientemente claros? [Coverage, Spec §User Story 1]
- [ ] CHK006 A exclusão de publicação e de fases da linguagem evita expansão de
  escopo? [Scope, Spec §Fora de escopo]

## Premissas e dependências

- [ ] CHK007 A premissa Ubuntu/uv no CI e a mitigação de divergência de versões
  estão declaradas? [Assumption, Spec §Assumptions e riscos]
