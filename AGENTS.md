# AGENTS.md

Guia operacional para agentes de IA (OpenCode, GitHub Copilot, Claude Code) e
para pessoas que entrarem no projeto. Leia antes de abrir o editor.

## 1. Contexto em um parágrafo

Este repositório implementa **CLite**, a linguagem didática do capítulo 2 de
Tucker e Noonan, em Python. A arquitetura segue o **front-end completo** do
Apêndice A de *Compiladores: Princípios, Técnicas e Ferramentas*: léxico →
sintático → semântico → execução. Depois da v1 (núcleo), a gramática é estendida
com classes, herança, polimorfismo e sobreescrita. O objetivo prioritário é
**aprendizado**, não performance nem completude.

## 2. Fonte da verdade

Leia, nesta ordem, antes de qualquer mudança:

1. `docs/01-linguagem-clite.md` — gramática e semântica da v1.
2. `docs/02-extensao-oo.md` — extensão OO (v2).
3. `docs/03-arquitetura-frontend.md` — fases, pacotes e mapa do Apêndice A.
4. `docs/05-decisoes.md` — decisões e alternativas descartadas.
5. `docs/06-casos-dificeis.md` — comportamentos esperados nas bordas.

Se o código divergir dos documentos, **pare** e abra um ticket `docs:` ou
`fix:`; não “conserte” o documento para justificar o código sem discussão.

## 3. Comandos

```bash
uv sync                                  # ambiente + dependências de desenvolvimento
uv run pytest                            # testes unitários e de conformidade
uv run pytest -m conformance             # só programas .clite de ponta a ponta
uv run ruff check .                      # lint
uv run ruff format .                     # formatação
uv run mypy src                          # tipos (strict)
make check                               # lint + tipos + testes (mesmo do CI)
```

Em Windows sem `make`, rode `uv run ruff check .`, `uv run ruff format --check .`,
`uv run mypy src` e `uv run pytest`. Os scripts do Spec-Kit são Bash: use
Linux/macOS, Git Bash ou WSL.

O comando de teste **sempre** aparece no corpo do ticket e no PR. Um PR sem o
comando executado não é mesclado.

## 4. Regras de implementação

- Python 3.12+, sem dependências de runtime. O parser é escrito à mão.
- Tipagem estática em `src/` (`mypy --strict`). `Any` exige justificativa no PR.
- Nós da AST são `dataclass` imutáveis; comportamento fica nos visitantes
  (`semantic/checker.py`, `interpreter/evaluator.py`), conforme D-02.
- Uma fase nunca importa a outra “de volta”: o fluxo é sempre
  `lexer → parser → ast → semantic → interpreter`.
- Erros sempre com código (`E1xxx`–`E4xxx`), linha e coluna, em português.
- Nada de `print` de depuração no código final; use a instrução `print` da
  linguagem e os testes.
- Comentários e mensagens em português; identificadores em inglês.
- Toda mudança de gramática atualiza `docs/01` (gramática **implementada**) no
  mesmo PR. `docs/02` é o desenho-alvo da v2 e só muda se o desenho mudar.

## 5. Fluxo de trabalho por ticket

1. Leia o ticket e o trecho do livro indicado. Se o requisito for ambíguo,
   pergunte antes de codar.
2. Confira o campo **Paralelismo** do ticket: se outra pessoa/agente estiver nos
   mesmos arquivos, negocie a ordem.
3. Crie a branch `tipo/NNN-slug` a partir da `main`.
4. Escreva o teste primeiro (quando fizer sentido) e veja falhar.
5. Implemente o mínimo para passar. Sem “melhorias de passagem”.
6. Rode `make check` e o comando específico do ticket.
7. Abra o PR no formato de `docs/agents/pull-request.md`, referenciando o ticket
   com `Closes #N`.
8. Ao entrar em revisão, mova o card para **In Review**; após o merge, ele segue
   o fluxo de QA até **Released**.

## 6. Limites de escopo

- **Não** implemente OO antes de a suíte de conformidade da v1 estar verde.
- **Não** adicione construtores, `null`, `for`, `do/while`, strings, funções de
  topo ou exceções sem ticket aprovado e atualização de `docs/05`.
- **Não** troque a biblioteca padrão por dependências externas sem justificar.
- **Não** reescreva documentos inteiros para “deixar mais bonito”; mudanças
  cirúrgicas, com diff revisável.

## 7. Tickets e PRs

- Formato obrigatório: [`docs/agents/ticket-format.md`](docs/agents/ticket-format.md).
- PR: [`docs/agents/pull-request.md`](docs/agents/pull-request.md).
- Título de ticket: `<tipo>: <NNN> - <slug>`, com `feat:`, `fix:`, `docs:` ou
  `chore:`.
- Todo ticket declara o **conceito implementado** e pelo menos uma
  **referência de livro** com capítulo e seção; sem isso não entra em To Do.
- Todo ticket declara se pode rodar em paralelo e quais arquivos toca.
- Labels mínimas: tipo, área (`lexer`, `parser`, `ast`, `types`, `interpreter`,
  `oo`, `infra`, `docs`) e tamanho (`size/S`, `size/M`). Não há etapa de
  triagem por label neste projeto.
- Board: Backlog → To Do → In Progress → In Review → Ready for QA → In QA →
  Released. Ticket novo entra no **Backlog**.
- Board do projeto: <https://github.com/users/BrunoFelix1/projects/3/views/1>.

## 8. Spec-Driven Development (SDD)

O projeto usa Spec-Kit (`specify`). Comandos no Copilot usam hífen
(`/speckit-specify`); no OpenCode usam ponto (`/speckit.specify`).

**Regra de saída:** todo artefato gerado por comando SDD (`spec.md`, `plan.md`,
`tasks.md`, checklists, relatórios) deve ser **sucinto, resumido e objetivo**:
tabelas em vez de prosa, no máximo 1 página por artefato, sem repetir o que já
está no repositório. Detalhes em
[`docs/agents/sdd-conciso.md`](docs/agents/sdd-conciso.md) e em
[`SPECKIT-USAGE.md`](SPECKIT-USAGE.md).

Antes de implementar via `/speckit.implement`, confirme que existe ticket
correspondente no board. Spec não substitui ticket: ela explica **o quê** e
**por quê**; o ticket recorta a fatia verificável.

## 9. Agentes e skills disponíveis

Agentes (`.opencode/agents/` e `.github/agents/`):

| Agente | Quando usar |
| --- | --- |
| `@grammar-designer` | propor/revisar gramática, ambiguidades, regras de tipo |
| `@lexer-engineer` | tokens, tabela de reservadas, autômato, posição |
| `@parser-engineer` | parser recursivo descendente, AST, precedência |
| `@type-checker` | regras de tipo A.1–A.6 e OO-1–OO-11 |
| `@interpreter-engineer` | estado, avaliação, arrays, despacho |
| `@oo-engineer` | extensão de classes, herança, override, polimorfismo |
| `@test-author` | programas `.clite`, casos de erro, golden tests |
| `@ticket-writer` | abrir/atualizar tickets no formato do projeto |

Skills (`.opencode/skills/` e `.github/skills/`): `clite-grammar`,
`clite-testing`, `clite-ticket`, `clite-pr`, `clite-sdd`.

## 10. Definição de pronto

- [ ] Testes novos cobrem o comportamento e o caso de erro.
- [ ] `make check` verde.
- [ ] `docs/01` atualizado quando a gramática mudou (e `docs/02` se o desenho
      da v2 mudou).
- [ ] PR com comando de teste e aprendizado em 3 linhas.
- [ ] Ticket e board atualizados.
