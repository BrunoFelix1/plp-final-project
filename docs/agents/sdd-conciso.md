# Saída concisa para comandos SDD

Esta regra vale para **todos** os comandos do Spec-Kit neste projeto:
`/speckit.constitution`, `/speckit.specify`, `/speckit.clarify`, `/speckit.plan`,
`/speckit.checklist`, `/speckit.tasks`, `/speckit.analyze`,
`/speckit.implement`, `/speckit.converge` e `/speckit.taskstoissues`.

## Regra

Todo artefato gerado deve ser **sucinto, resumido e objetivo**. O leitor é uma
pessoa com pouco tempo, que precisa entender o que será feito e como verificar.

## Limites

| Artefato | Limite | Forma |
| --- | --- | --- |
| `spec.md` | 1 página | objetivos em bullets, critérios em checklist |
| `plan.md` | 1 página | tabelas de decisão e fases |
| `tasks.md` | 1 página | checklist com ID, arquivo e teste |
| `checklist.md` | 1 página | itens verificáveis, sem prosa |
| `research.md`, `data-model.md` | meia página cada | só o que muda a implementação |
| relatório de `analyze`/`converge` | 15 linhas | achados + ação, sem repetir o plano |

## Proibições

- Repetir conteúdo que já está em `docs/`, `AGENTS.md` ou no ticket.
- Seções vazias, “NEEDS CLARIFICATION” genérico ou texto de exemplo.
- Prosa longa onde cabe tabela ou checklist.
- Reformatar documentos existentes sem necessidade.
- Criar arquivos além dos que o comando pede.

## Obrigatório em qualquer artefato

1. **Objetivo em uma frase.**
2. **Critérios de aceite verificáveis** (comando ou comportamento observável).
3. **Fora de escopo** (1–3 itens).
4. **Riscos** (máximo 3, com mitigação).
5. **Referências** a `docs/01`, `docs/02` ou `docs/06` quando aplicável.

## Relação com tickets

- Spec/plan explicam **o quê** e **por quê**; o ticket recorta a fatia
  verificável.
- Se o comando gerar tasks, cada task deve apontar para um ticket existente ou
  propor um novo no formato de `docs/agents/ticket-format.md`.
- Não crie ticket duplicado: procure no board pelo código (`NNN`).

## Como aplicar

- Os templates em `.specify/templates/` já estão enxutos; comece por eles.
- Ao final de qualquer comando, mostre só: artefato criado, caminho, 3 bullets
  de resumo e o próximo comando sugerido.
