# Checklist: Operadores e pontuação do #7 — qualidade dos requisitos

**Spec**: [spec.md](../spec.md) · **Plan**: [plan.md](../plan.md) · **Tasks**: [tasks.md](../tasks.md)

<!--
  REGRA DO PROJETO: meta de 70 linhas; marque [X] apenas com evidência (AGENTS §5.5).
  Esta checklist testa os REQUISITOS (texto), não a implementação.
-->

## Requisitos e completude

- [X] CHK001 - Cada FR tem cenário, edge case ou task que o verifica?
      [Completeness, FR-001–002 → US1; FR-004–005 → US2; FR-003 → T002–T004; FR-006 → T006; FR-007 → T009–T010]
- [X] CHK002 - Os 23 lexemas estão enumerados em um só lugar verificável?
      [Completeness, data-model.md: 17 operadores + 6 pontuações = 23]
- [X] CHK003 - O fora de escopo é verificável (precedência #10, CLI #8, recuperação #19)?
      [Completeness, Spec §Fora de escopo e Assumptions]

## Clareza

- [X] CHK004 - "Maior casamento" está ancorado em exemplos (`a<=b` vs `a < = b`, `===`)?
      [Clarity, Spec §US1.2–3 e Edge Cases]
- [X] CHK005 - A posição do `E1002` está definida (símbolo isolado, coluna do `&`/`|`)?
      [Clarity, Spec §US2.1; Edge `&&&` → coluna 3]
- [X] CHK006 - "Prefixo isolado" é derivável sem lista escrita à mão?
      [Clarity, plan.md §Phase 0; data-model §Regras derivadas]

## Consistência

- [X] CHK007 - As 23 tags citadas existem em `tags.py` com os nomes pós-#44?
      [Consistency, conferido: ASSIGN…GREATER_EQUAL, PLUS…LOGICAL_OR, SEMICOLON…RBRACKET]
- [X] CHK008 - O formato da mensagem segue D-12 (`erro E1002 (linha L, coluna C)`)?
      [Consistency, docs/05 D-12; plan §Phase 1 → `LexicalError`]
- [X] CHK009 - A spec respeita FR-010 do #6 (operadores ficam para o #7) sem contradizê-lo?
      [Consistency, specs/004 FR-010 × Spec §FR-006]
- [X] CHK010 - O `/` não conflita com o comentário `//`?
      [Consistency, Edge Cases `a//b`; plan §Phase 0; docs/06 §1 "Barra ambígua"]

## Cenários e bordas

- [X] CHK011 - Bordas de docs/06 aplicáveis estão cobertas (`a<=b`, `a < = b`, `&` sozinho, `/`)?
      [Coverage, docs/06 §1; Spec §Edge Cases]
- [X] CHK012 - `E1001` continua definido para `@`, `#` e `.`?
      [Coverage, Spec §FR-005 e Edge `5.`]

## Itens que dependiam de decisão humana

- [X] CHK013 - `E1002` sem entrada D-NN em `docs/05` é aceitável?
      [Decisão, Bruno, 2026-11-25: aceito; é registro de código em docs/03 e docs/06]
- [X] CHK014 - O ticket #7 foi atualizado para listar `lexer.py`, `test_scanner.py`,
      `docs/03` e `docs/06`? [Evidência: issue #7, linha "Arquivos que toca"]

## Notas

- 14 itens verificados: 12 contra spec, plan, data-model e código; 2 resolvidos pelo
  Bruno (decisão e edição da issue). O gate (SC-003) foi conferido em `converge.md`.
