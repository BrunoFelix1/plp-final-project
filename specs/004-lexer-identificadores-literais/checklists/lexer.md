# Checklist: Lexer do #6 — qualidade dos requisitos

**Spec**: [spec.md](../spec.md) · **Plan**: [plan.md](../plan.md) · **Tasks**: a gerar

<!--
  REGRA DO PROJETO: meta de 70 linhas; marque [X] apenas com evidência (AGENTS §5.5).
  Esta checklist testa os REQUISITOS (texto), não a implementação.
-->

## Requisitos e completude

- [X] CHK001 - Cada FR tem cenário de aceitação ou premissa que a verifica?
      [Completeness, Spec §FR-001–FR-010; US1/US2]
- [X] CHK002 - O contrato público do scanner tem entrada, saída e pré/pós-condições?
      [Completeness, contracts/lexer.md]
- [X] CHK003 - O fim do fonte (`EOF`) está definido, inclusive em chamadas seguintes?
      [Completeness, research D2; contracts §Pós-condições]
- [X] CHK004 - Os limites de escopo (operadores #7, recuperação #19) são verificáveis?
      [Completeness, Spec §FR-010 e Assumptions]

## Clareza

- [X] CHK005 - "Maior casamento" está ancorado em exemplo concreto (`whilea`)?
      [Clarity, Spec §US1.2]
- [X] CHK006 - A posição do erro está definida por caso (ponto vs aspa inicial)?
      [Clarity, Spec §US2]
- [X] CHK007 - "Caractere imprimível" basta para aceitar `' '` e rejeitar `'\n'`?
      [Clarity, docs/01 §4.3.4; data-model §Regras]
- [X] CHK008 - O `lexeme` de um char inclui as aspas?
      [Clarity, contracts §Exemplos normativos]

## Consistência

- [X] CHK009 - As tags citadas existem em `tags.py` com os nomes pós-#44?
      [Consistency, data-model; PR #44]
- [X] CHK010 - O formato da mensagem segue D-12 (`erro E1001 (linha L, coluna C)`)?
      [Consistency, research D1; docs/05 D-12]
- [X] CHK011 - Float, char e comentário não contradizem `docs/01` §4.3?
      [Consistency, Spec §FR-003, FR-005, FR-007]

## Cenários e bordas

- [X] CHK012 - Os casos de `docs/06` §1 aplicáveis estão cobertos (`1.2.3`, `' '`,
      comentário sem newline, `@`)? [Coverage, Spec §Edge Cases]
- [X] CHK013 - Cada erro tem linha e coluna esperadas? [Coverage, Spec §FR-009]
- [X] CHK014 - O fluxo de recuperação está explicitamente fora de escopo?
      [Coverage, Spec §FR-010; Assumptions]
- [X] CHK015 - Está definido o que o scanner faz ao encontrar pontuação ou operador
      ainda não implementados (`;`, `+`, `(`)? [Resolved, Spec §FR-010;
      contracts §Exemplos — decisão A: `E1001` até o #7]

## Dependências e premissas

- [X] CHK016 - A dependência do #5 está validada nos arquivos da `main`?
      [Assumption, plan §Technical Context]
- [X] CHK017 - A premissa de manter `LexicalError` em `lexer.py` até o #19 está
      justificada? [Assumption, research D1; ticket #19]
- [X] CHK018 - A regra de números mágicos está endereçada no plano?
      [Assumption, research D6; AGENTS §5.6]

## Notas

- 18 dos 18 itens verificados contra spec, plan, `docs/01`, `docs/06`, `docs/05`
  e o código da `main` (PRs #42 e #44).
- CHK015 foi resolvido pela decisão A: operador/pontuação gera `E1001` até o #7.
