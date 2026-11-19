# Checklist: [FEATURE]

**Spec**: [link] · **Plan**: [link] · **Tasks**: [link]

<!--
  REGRA DO PROJETO: meta de 70 linhas; se passar de 100, seja mais conciso.
  Marque [x] apenas com evidência (comando, saída ou link).
-->

## Requisitos

- [ ] Cada FR da spec tem teste ou tarefa correspondente.
- [ ] Cada SC é verificável por comando ou saída observável.
- [ ] Fora de escopo declarado e respeitado.

## Linguagem e gramática

- [ ] A gramática implementada corresponde a `docs/01`/`docs/02`.
- [ ] Nomes reservados continuam reservados.
- [ ] Ambiguidades conhecidas (`else` pendente, `Id(`) têm teste.

## Tipos e erros

- [ ] Regras de tipo aplicáveis têm teste feliz e de erro.
- [ ] Mensagens têm código, linha e coluna.
- [ ] `undef`, divisão por zero e índice fora de faixa cobertos quando aplicável.

## Qualidade

- [ ] `uv run pytest` verde.
- [ ] `uv run ruff check .` e `uv run mypy src` verdes.
- [ ] Documentação atualizada no mesmo PR.
- [ ] Ticket e board atualizados.

## Notas

- [Observação curta, se necessária]
