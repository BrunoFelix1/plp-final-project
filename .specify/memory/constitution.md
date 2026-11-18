# Constituição do CLite

**Versão:** 1.0.0 · **Ratificada em:** 17/11/2026 · **Última emenda:** 17/11/2026

Projeto acadêmico de um interpretador para a linguagem CLite, em Python, com
extensão orientada a objetos. Esta constituição vale para toda spec, plano e
implementação; um plano que a violar precisa registrar a violação e justificá-la.

## Princípios

### I. Aprendizado primeiro (NÃO NEGOCIÁVEL)

Toda decisão prioriza o entendimento do desenvolvedor. Código precisa ser
legível, dividido por fase e acompanhado do conceito que exercita. Otimização de
desempenho e esperteza sintática não são objetivos.

### II. Fidelidade à gramática documentada

`docs/01-linguagem-clite.md` e `docs/02-extensao-oo.md` são a fonte da verdade.
Nenhuma implementação pode divergir sem que o documento mude no mesmo PR.
Mudança de gramática sempre precede o código que a implementa.

### III. Fatias verticais pequenas

Cada incremento cabe em um ticket e em um PR revisável, com a `main` sempre
verde. É proibido acumular léxico, parser e interpretador em um único PR. O
trabalho paralelo é explicitamente declarado nos tickets.

### IV. Teste como especificação

Todo comportamento novo tem teste que falha antes e passa depois. Programas
`.clite` de conformidade provam a linguagem de ponta a ponta. Casos de erro são
testados por código, linha e coluna.

### V. Python padrão, tipado e sem dependências de runtime

Python 3.12+, biblioteca padrão apenas. `mypy --strict` em `src/`, `ruff` para
estilo, `pytest` para testes. Nenhuma biblioteca de parser ou lexer: a graça é
construir o front-end.

### VI. Escopo controlado

A v1 (núcleo) precisa estar completa e verde antes da v2 (OO). A v2 cobre
classes, herança, polimorfismo e sobreescrita, e nada além: sem classe abstrata,
reflexão, construtores, sobrecarga, `null` ou funções de topo sem emenda nesta
constituição.

### VII. Documentação operacional

Tickets e PRs seguem `docs/agents/ticket-format.md` e
`docs/agents/pull-request.md`. Todo PR declara e executa o comando de teste.

## Saída de comandos SDD

Specs, planos, tasks, checklists e relatórios gerados por comandos SDD devem ser
**sucintos, resumidos e objetivos**: no máximo 1 página por artefato, tabelas e
checklists em vez de prosa, sem repetir `docs/`, `AGENTS.md` ou tickets.

## Restrições técnicas

- Sem dependências de runtime; dependências de desenvolvimento ficam no grupo
  `dev` do `pyproject.toml`.
- Erros sempre com código (`E1xxx`–`E4xxx`), linha e coluna, em português.
- Nós da AST são dados; checagem e avaliação ficam em visitantes.
- O fluxo é unidirecional: `lexer → parser → ast → semantic → interpreter`.

## Fluxo de desenvolvimento

1. Ticket pequeno no board, com objetivo, conceito e verificação.
2. Branch `tipo/NNN-slug`.
3. Teste → implementação mínima → refatoração.
4. `make check` verde.
5. PR no formato do projeto, com `Closes #N` e comando de teste executado.
6. Revisão humana; merge squash; card para QA.

## Governança

- Emendas exigem PR que atualize esta constituição e registre a justificativa.
- Enquanto o projeto for acadêmico, o mantenedor do repositório aprova emendas.
- Decisões técnicas que afetam a linguagem também viram `D-NN` em
  `docs/05-decisoes.md`.
