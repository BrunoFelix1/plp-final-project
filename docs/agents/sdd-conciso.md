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
| `spec.md` | ≤70 linhas (ideal) | objetivos em bullets, critérios em checklist |
| `plan.md` | ≤70 linhas (ideal) | tabelas de decisão e fases |
| `tasks.md` | ≤70 linhas (ideal) | checklist com ID, arquivo e teste |
| `checklist.md` | ≤70 linhas (ideal) | itens verificáveis, sem prosa |
| `research.md`, `data-model.md` | meia página cada | só o que muda a implementação |
| relatório de `analyze`/`converge` | 15–30 linhas | achados + ação, sem repetir o plano |

**Meta de linhas:** 70 por artefato. Não é bloqueio; a ideia é ser econômico para
que o conceito e a explicação caibam em **menos de 100 linhas**. Se passar de
100, seja ainda mais conciso: o excedente deve explicar o conceito, não repetir.

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
6. **Explicação do conceito** (projeto acadêmico): o que está sendo implementado,
   por que importa e como verificar, em linguagem de quem está aprendendo.

## Relação com tickets

- Spec/plan explicam **o quê** e **por quê**; o ticket recorta a fatia
  verificável.
- Se o comando gerar tasks, cada task deve apontar para um ticket existente ou
  propor um novo no formato de `docs/agents/ticket-format.md`.
- Não crie ticket duplicado: procure no board pelo código (`NNN`).

## Sequência e comunicação

1. `specify`
2. `plan`
3. `checklist`
4. `tasks`
5. implementação das tasks
6. `converge`

- Não despeje a saída do comando no console. Seja conciso.
- Ao final de cada comando, mostre apenas: artefato criado, caminho, 3 bullets de
  resumo, pedido de revisão do arquivo e **um único** próximo comando.
- Não sugira a sequência inteira; o próximo comando depende do último concluído.
- Depois de `tasks`, implemente as tasks; depois, rode `converge`.
- Se `converge` não retornar problemas, oriente rodar os testes gerais
  (`make check`; no Windows, os quatro comandos `uv run ...`) e conferir a
  consistência da branch. Não sugira outro comando Spec-Kit.

## Como aplicar

- Os templates em `.specify/templates/` já estão enxutos; comece por eles.
- Ao final de qualquer comando, mostre só: artefato criado, caminho, 3 bullets
  de resumo, pedido de revisão e o próximo comando.
