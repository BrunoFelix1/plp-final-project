# Checklist: Qualidade dos requisitos documentais

**Spec**: [spec.md](../spec.md) · **Plan**: [plan.md](../plan.md) ·
**Tasks**: ainda não geradas

<!--
  Checklist pertencente ao revisor. [x] significa que a qualidade do requisito
  foi aprovada; não significa que a implementação esteja concluída.
-->

## Requirement Completeness

- [x] CHK001 - Os cinco requisitos funcionais cobrem gramática, tokens, glossário, casos difíceis e links? [Completeness, Spec §FR-001–FR-005]
- [x] CHK002 - As seis entradas obrigatórias do glossário estão explicitamente enumeradas? [Completeness, Spec §FR-003]
- [x] CHK003 - A especificação cobre tanto sintaxe concreta quanto sintaxe abstrata? [Coverage, Spec §FR-001]
- [x] CHK004 - As quatro categorias do catálogo de casos difíceis estão declaradas? [Completeness, Spec §FR-004]
- [x] CHK005 - O escopo identifica os três arquivos documentais e exclui código e OO? [Completeness, Spec §FR-001–FR-005, Fora de escopo]

## Requirement Clarity

- [x] CHK006 - “EBNF v1 completa” está delimitada o suficiente para distinguir produções, metanotação e exemplos? [Clarity, Spec §FR-001]
- [x] CHK007 - Os significados de `{ }` e `[ ]` estão definidos sem ambiguidade? [Clarity, Spec §FR-001]
- [x] CHK008 - A exigência sobre tokens diferencia categoria, lexema e palavras reservadas? [Clarity, Spec §FR-002]
- [x] CHK009 - A precedência especifica ordem e associatividade, inclusive operadores não associativos? [Clarity, Spec §FR-002]
- [x] CHK010 - As seis definições do glossário são distintas, didáticas e adequadas ao leitor estudante? [Clarity, Spec §FR-003]

## Requirement Consistency

- [x] CHK011 - Os requisitos de gramática, tokens e precedência são consistentes entre si? [Consistency, Spec §FR-001–FR-002]
- [x] CHK012 - A fronteira entre a v1 e o desenho OO permanece consistente em todos os requisitos? [Consistency, Spec §Assumptions, FR-004]
- [x] CHK013 - A descrição da AST é consistente com conversões e com a distinção entre árvore concreta e abstrata? [Consistency, Spec §FR-001]
- [x] CHK014 - A exigência de links existentes é compatível com a decisão de não criar um arquivo separado de glossário? [Consistency, Spec §FR-003, FR-005]

## Acceptance Criteria Quality

- [x] CHK015 - Cada requisito funcional pode ser avaliado objetivamente por revisão do documento indicado? [Measurability, Spec §FR-001–FR-005]
- [ ] CHK016 - O critério de links define claramente quais destinos devem ser considerados? [Clarity, Spec §SC-002]
- [ ] CHK017 - O critério de revisão por pares identifica o padrão de aprovação e o responsável? [Completeness, Spec §SC-003]
- [x] CHK018 - Os critérios de sucesso distinguem qualidade dos requisitos de conclusão da implementação? [Clarity, Spec §SC-001–SC-003]

## Scenario and Edge Case Coverage

- [x] CHK019 - As histórias cobrem tanto o estudante que aprende quanto o revisor que avalia a documentação? [Coverage, Spec §User Stories 1–2]
- [x] CHK020 - Os cenários incluem a leitura da metanotação e da precedência como fluxos independentes? [Coverage, Spec §Acceptance Scenarios]
- [x] CHK021 - Os casos `whilea`, `<=`, floats malformados, `else` pendente e comparação encadeada estão ligados a requisitos? [Coverage, Spec §Edge Cases]
- [ ] CHK022 - O requisito de casos difíceis esclarece como tratar exemplos OO e referências a `print` fora da v1? [Gap, Spec §FR-004, §Assumptions]

## Dependencies, Assumptions and Ambiguities

- [x] CHK023 - A suposição de que `docs/01` é a fonte de verdade e `docs/02` é desenho-alvo está explícita? [Assumption, Spec §Assumptions]
- [x] CHK024 - A ausência de API, CLI e contratos externos está documentada como limite do ticket? [Completeness, Plan §Phase 1]
- [ ] CHK025 - As expressões “completa”, “linguagem de estudo” e “sem links quebrados” têm critérios suficientemente objetivos? [Ambiguity, Spec §FR-001, FR-003, FR-005]

## Notes

- Checklist gerada para revisão da qualidade dos requisitos; 21 itens foram
  verificados contra a spec, o plano e os documentos atuais.
- Permanecem abertos: CHK016 (destinos de SC-002), CHK017 (responsável pela
  aprovação por pares), CHK022 (escopo de OO/`print` em `docs/06`) e CHK025
  (termos ainda subjetivos). Requerem decisão ou validação humana.
