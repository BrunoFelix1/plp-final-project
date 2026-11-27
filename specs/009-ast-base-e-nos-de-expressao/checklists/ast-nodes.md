# Checklist: Qualidade de requisitos — AST base e nós de expressão

**Spec**: [spec.md](../spec.md) · **Plan**: [plan.md](../plan.md) · **Tasks**: pendente (`/speckit.tasks`)
**Criado**: 2026-11-26 · **Profundidade**: Standard · **Audiência**: revisor do PR
<!--
  REGRA DO PROJETO: meta de 70 linhas; se passar de 100, seja mais conciso.
  "Unit tests for English": cada item testa a QUALIDADE DOS REQUISITOS, não a
  implementação. [x] só com revisão do revisor; gerado intencionalmente vazio.
-->

## Completeza dos requisitos

- [x] CHK001 - A lista de nós do FR-001 cobre **exatamente** todos os nós de `docs/01` §6, sem omissões e sem nós extras? [Completeza, Spec §FR-001]
- [x] CHK002 - Os campos e tipos de cada nó estão especificados (ex.: `Assign.target` restrito a `VarRef | ArrayRef`)? [Completeza, Spec §FR-001 + data-model.md]
- [x] CHK003 - Igualdade, imutabilidade e posição são exigidos para **todo** nó, e não apenas ilustrados nos exemplos? [Completeza, Spec §FR-002/FR-004]
- [x] CHK004 - O padrão de posição "não informado" está definido para todos os nós, sem exceção? [Completeza, Spec §FR-002]

## Clareza e ambiguidade

- [x] CHK005 - "Não informado" está quantificado sem ambiguidade (inteiro `0`, não `null`)? [Clareza, Spec §FR-002]
- [x] CHK006 - "Sem lógica" está delimitado de forma verificável (dados puros; nenhum método de execução/tipos)? [Clareza, Spec §FR-005]
- [x] CHK007 - O escopo de `CliteType` deixa claro que a restrição é estática e que o nó **não** valida em runtime (D-07 é regra do semântico)? [Ambiguidade, Spec §FR-003]

## Consistência

- [x] CHK008 - Os nomes dos nós são consistentes entre spec (FR-001), data-model.md e `docs/01` §6? [Consistência]
- [x] CHK009 - Alguma decisão D1–D6 do plan contradiz um FR da spec? [Consistência, Plan §Phase 0]
- [x] CHK010 - A exclusão do nó `Print` é consistente entre spec (Premissas + Fora de escopo) e contrato do módulo? [Consistência, Spec §Fora de escopo + contracts/ast-nodes.md]

## Qualidade dos critérios de aceite

- [x] CHK011 - Cada SC é verificável por comando único, sem julgamento subjetivo? [Mensurabilidade, Spec §SC-001/SC-002]
- [x] CHK012 - Os cenários de aceite de US1/US2 estão rastreáveis a FRs específicos? [Rastreabilidade, Spec §User Stories]

## Cobertura de cenários

- [x] CHK013 - Há requisitos para o cenário de consumo paralelo (parser 010 construindo os nós via contrato)? [Cobertura, Spec §Riscos]
- [x] CHK014 - O comportamento para entrada fora do domínio (ex.: string de tipo inválida) está definido como rejeição estática, e não como erro de runtime? [Cobertura/Gap, Spec §FR-003]

## Cobertura de casos de borda

- [x] CHK015 - Os casos de borda listados (alvo de atribuição a array, igualdade aninhada, `If` sem `else`) têm requisito correspondente explícito? [Borda, Spec §Edge Cases]

## Dependências e premissas

- [x] CHK016 - A dependência do ticket #4 e o estado vazio de `types.py` estão documentados como premissas? [Dependência, Spec §Assumptions]
- [x] CHK017 - A premissa "`ast/__init__.py` intocado" é validável contra os consumidores futuros (imports diretos)? [Premissa, Spec §Assumptions]
- [x] CHK018 - A regra de números mágicos está contemplada como parte mensurável dos critérios de sucesso? [Completeza, Spec §SC-002]

## Notas

- `/speckit.implement` lê o estado deste checklist mas não altera marcadores.
- `checklists/requirements.md` (checklist embutido do `/speckit.specify`) permanece separado.
- 18/18 itens verificados contra o repositório e a issue #9 em 2026-11-26, por
  delegação do revisor (AGENTS.md §5.5). Ajustes aplicados para satisfazer os
  itens: contagem 15→17 nós (spec US1, tasks T002), `else`→`else_branch` no
  data-model/contracts (`else` é palavra reservada do Python) e premissa do
  ticket #4/`types.py` acrescentada à spec (CHK016).
