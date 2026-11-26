# Checklist: CLI `tokens` e golden do #8 — qualidade dos requisitos

**Spec**: [spec.md](../spec.md) · **Plan**: [plan.md](../plan.md) · **Tasks**: [tasks.md](../tasks.md)

<!-- Esta checklist testa os REQUISITOS (texto), não a implementação (AGENTS §5.5). -->

## Requisitos e completude

- [X] CHK001 - Cada FR tem cenário, edge case ou task?
      [FR-001–003 → US1/US2; FR-004 → Edge Cases; FR-005 → US3; FR-006 → T005; FR-007 → T011]
- [X] CHK002 - Os 4 itens "Pronto quando" do ticket #8 estão cobertos?
      [Spec §US1.1, FR-001; §US2.1, FR-003; §SC-001–002]
- [X] CHK003 - O fora de escopo é verificável (parser, `--max-errors`)?
      [Spec §Fora de escopo]

## Clareza

- [X] CHK004 - O formato `TAG lexema linha:coluna` tem exemplo concreto?
      [Spec §US1.1: `INT int 1:1`]
- [X] CHK005 - "Uma única mensagem" está definida (stderr, uma linha, stdout vazio)?
      [Spec §FR-003, §US2.1]
- [X] CHK006 - Os três exit codes estão ancorados em docs?
      [Spec §FR-004; docs/03 §6]

## Consistência

- [X] CHK007 - O `Tag.name` impresso existe para os 23 lexemas e literais?
      [Consistency, tags.py pós-#44; operators.py do #7]
- [X] CHK008 - `E1001`/`E1002` seguem o formato D-12 sem código novo?
      [Consistency, Plan §Phase 1 Erros; docs/05 D-12]
- [X] CHK009 - Goldens ficam estáveis no Windows (fim de linha)?
      [Consistency, `.gitattributes`: `* text=auto eol=lf`]
- [X] CHK010 - `examples/lexico/` e `tests/golden/lexer/` batem com `examples/README.md` e o ticket?
      [Consistency, examples/README.md; ticket §Pronto quando]

## Cenários e bordas

- [X] CHK011 - Arquivo vazio, inexistente e não-UTF-8 têm resultado definido?
      [Coverage, Spec §US1.3 e Edge Cases]
- [X] CHK012 - `parse`/`check`/`run` seguem `E9000`, sem regressão do #4?
      [Coverage, FR-006; T005]

## Itens que dependem de decisão humana

- [ ] CHK013 - Aceitar duas decisões desta spec: `EOF` não impresso e erro "tudo ou nada"?
      Decisão de produto do time; o ticket não as define.
- [ ] CHK014 - Aceitar empilhar a branch em `feat/007` enquanto o #46 não entra na `main`?

## Notas

- 12 itens verificados contra spec, plan e ticket; 2 abertos por dependerem de decisão humana.
