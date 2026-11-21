# Checklist: Qualidade dos requisitos documentais — Arquitetura do front-end

**Spec**: [spec.md](../spec.md) · **Plan**: [plan.md](../plan.md) ·
**Tasks**: ainda não geradas

<!--
  Checklist do revisor ("testes unitários dos requisitos"). [x] = o requisito
  está bem escrito; NÃO significa que o docs/03 já foi alterado.
  Marque [x] apenas com evidência.
-->

## Requirement Completeness

- [ ] CHK001 - Os 3 itens "Pronto quando" do ticket #3 (diagrama + tabela, contratos, erros + CLI) têm um FR correspondente? [Completeness, Spec §FR-001–FR-004]
- [ ] CHK002 - A lista de módulos do FR-001 bate exatamente com `ls src/clite`? [Completeness, Spec §FR-001]
- [ ] CHK003 - As 4 lacunas do plano (L1–L4) estão todas ligadas a um FR ou SC da spec? [Completeness, Plan §Phase 1]
- [ ] CHK004 - A spec diz o que acontece com o `docs/README.md`, que o ticket também lista? [Completeness, Spec §FR-005, Plan §Structure]

## Requirement Clarity

- [ ] CHK005 - "Citar no diagrama" está definido (na caixa da fase ou em uma legenda abaixo do diagrama)? [Clarity, Spec §FR-001]
- [ ] CHK006 - O critério para marcar algo como v2 é explícito (o item só existe com classes e métodos)? [Clarity, Spec §FR-003, Research R3]
- [ ] CHK007 - O FR-004 deixa claro que §5 (erros) e §6 (CLI) só precisam **existir e estar corretos**, sem mudança obrigatória? [Clarity, Spec §FR-004, Plan §Phase 1]
- [ ] CHK008 - O papel do `cli` (ponto de entrada, não fase) está diferenciado dos módulos de fase? [Clarity, Spec §FR-001]

## Requirement Consistency

- [ ] CHK009 - A referência à decisão dos visitantes (D-02) é consistente entre spec, plano, research e `docs/05`? [Consistency, Spec §FR-002]
- [ ] CHK010 - O nome `symbols` é usado de forma consistente no cabeçalho e na tabela §2? [Consistency, Research R1]
- [ ] CHK011 - A política de erros do docs/03 §5 é consistente com D-12 (léxico/sintático param; tipos acumulam)? [Consistency, Spec §FR-004]
- [ ] CHK012 - O contrato do estado de execução da v1 é consistente com o escopo único (D-06)? [Consistency, Spec §FR-003]
- [ ] CHK013 - A edição já feita pelo dev (`TypeChecker` → `Semantic` no diagrama) é consistente com o nome usado em §2 e §4.3? [Consistency, Plan §Technical Context]

## Acceptance Criteria Quality

- [ ] CHK014 - O SC-001 (9/9 módulos + `cli`) pode ser verificado por um comando reproduzível? [Measurability, Spec §SC-001, Quickstart §1]
- [ ] CHK015 - "Zero referências cruzadas erradas" (SC-002) lista quais referências conferir? [Clarity, Spec §SC-002]
- [ ] CHK016 - O SC-003 identifica quem faz a revisão por pares e qual o padrão de aprovação? [Completeness, Spec §SC-003, Gap]
- [ ] CHK017 - Os critérios separam a qualidade do documento de "`make check` verde", que só prova que nada quebrou? [Clarity, Spec §SC-004]

## Scenario & Edge Case Coverage

- [ ] CHK018 - Está definido como citar um módulo planejado que ainda não existe (`cli.py`), sem prometer prazo? [Edge Case, Spec §Edge Cases]
- [ ] CHK019 - A divergência do próprio livro (`symbol` × `symbols`) está registrada com a fonte? [Edge Case, Research R1]

## Dependencies & Assumptions

- [ ] CHK020 - O risco de conflito com o PR #38 em `docs/README.md` tem mitigação explícita? [Assumption, Spec §Riscos]
- [ ] CHK021 - A premissa de "edição cirúrgica" (T0) está traduzida em limite verificável (~20 linhas, 1 arquivo)? [Assumption, Plan §Constitution Check]
- [ ] CHK022 - O que fica fora de escopo (implementar fases, mudar D-02, corrigir `errors.py`) está explícito? [Completeness, Spec §Fora de escopo]

## Notas

- CHK016 depende de decisão humana: quem do time revisa o PR do 003 (adiado pelo dev).
- CHK005 esclarecido (21/11): pacotes ao lado das caixas, apoio como seta lateral,
  `cli.py` no topo, `errors.py` em linha própria → Spec §FR-001.
- CHK013 esclarecido (21/11): `Semantic (TypeChecker)` conforme Compiladores §1.2.3
  e Tucker §2.4/§6.1 → Spec §FR-001a, Research R3a.
