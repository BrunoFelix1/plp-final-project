# Checklist: Requisitos da tabela de símbolos (ticket 012)

**Spec**: [spec.md](../spec.md) · **Plan**: [plan.md](../plan.md)

<!--
  REGRA DO PROJETO: meta de 70 linhas; se passar de 100, seja mais conciso.
  Marque [x] apenas com evidência (comando, saída ou link).
-->

> Testa a **qualidade dos requisitos** (completude, clareza, consistência,
> cobertura), não a implementação. `[x]` significa aprovação do revisor sobre
> o requisito escrito; `/speckit.implement` lê o estado, mas não altera marcas.

## Completude

- [x] CHK001 - Cada item do "Pronto quando" do ticket está refletido em um FR da spec? [Completude, Spec §FR-001–FR-005]
- [x] CHK002 - O comportamento de duplicidade de array está especificado, além de variável simples? [Completude, Spec §US2, §Edge Cases]
- [x] CHK003 - O comportamento da tabela vazia está especificado (busca e lista)? [Completude, Spec §Edge Cases]
- [x] CHK004 - Os códigos `E3001`/`E3002` estão atribuídos univocamente aos seus gatilhos? [Completude, Spec §FR-003/FR-004, Data Model §Erro]

## Clareza

- [x] CHK005 - "Devolve a declaração original" está claro (mesmo nó registrado, com tipo e posição)? [Clareza, Spec §US1]
- [x] CHK006 - A origem da posição do `E3002` é inequívoca (2ª declaração, não a 1ª)? [Clareza, Spec §US2, §FR-003]
- [x] CHK007 - "Posição não informada" na busca está definida com valor concreto (0, 0)? [Clareza, Spec §Edge Cases]
- [x] CHK008 - O formato da mensagem de erro está especificado de forma verificável? [Clareza, Spec §FR-007, docs/03 §5]

## Consistência

- [x] CHK009 - As posições dos erros coincidem entre spec, data-model e contrato? [Consistência, Spec §FR-003/004, Data Model, Contract]
- [x] CHK010 - A regra de escopo único é consistente entre D-06, spec e docs/06 §3? [Consistência, docs/05 D-06, docs/06 §3, Spec §US2.3]

## Cobertura

- [x] CHK011 - Os quatro gatilhos de duplicidade (simples, array, tipo diferente, bloco) têm cenário de aceitação? [Cobertura, Spec §US2, §Edge Cases]
- [x] CHK012 - A ordem da lista exposta tem cenário de aceitação próprio? [Cobertura, Spec §US3.2]

## Mensurabilidade

- [x] CHK013 - Cada SC é verificável por comando ou saída observável? [Mensurabilidade, Spec §SC-001–SC-003]
- [x] CHK014 - Os cenários do quickstart mapeiam 1:1 com os cenários de aceitação da spec? [Rastreabilidade, Quickstart, Spec §US1–US3]

## Premissas e escopo

- [x] CHK015 - As premissas de design (API AST-cêntrica, erro local, tipos literais) estão documentadas na spec e no research? [Premissas, Spec §Assumptions, Research D1–D3]
- [x] CHK016 - A fronteira "fora de escopo" (escopo de bloco, v2, gramática intocada) está declarada e alinhada ao plano? [Premissas, Spec §Assumptions, Plan §Constitution Check VI]

## Notas

- Foco: requisitos da #12 apenas (sem itens de compatibilidade #13/#14/#19).
- Profundidade enxuto (16 itens); audiência: autor, pré-implementação.
- Itens gerados por `/speckit.checklist`; nenhum marcado — avaliação é do revisor.
