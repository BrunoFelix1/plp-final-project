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

> **Antes de implementar:** todo pedido de implementação/codificação feito a uma
> LLM, em português ou inglês, segue o protocolo obrigatório da §5: garantir a
> branch do ticket e começar pelo Spec-Kit `specify`. Não escreva código antes
> disso.

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

- Siga os princípios técnicos **T0–T2** da
  [constituição](.specify/memory/constitution.md): edição cirúrgica, SOLID e
  qualidade, e TDD (Red–Green–Refactor).
- Sem números mágicos: use constantes nomeadas e rode `make magic` (§5.6).
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

## 5. Protocolo obrigatório para implementação por LLM

Vale para qualquer pedido de implementação, correção ou codificação feito a um
agente, **em português ou inglês**. Não escreva código antes de concluir 5.1 e
5.2.

### 5.1 Branch correta (obrigatório)

1. Identifique o ticket pelo formato `tipo: NNN - slug` (ex.:
   `feat: 027 - lexer-e-parser-de-classes`). Sem ticket, pare e crie/peça um
   antes de implementar.
2. Verifique a branch atual:
   ```bash
   git branch --show-current
   ```
3. Decida antes de qualquer edição:
   - **`main`**: crie a branch do ticket a partir da `main` atualizada e anuncie
     isso na primeira resposta (não peça confirmação; a regra já autoriza).
     ```bash
     git fetch origin
     git switch main
     git pull --ff-only
     git switch -c feat/027-lexer-e-parser-de-classes
     ```
   - **branch do próprio ticket** (`tipo/NNN-...`): prossiga.
   - **outra branch**: avise explicitamente antes de começar — “Você está em
     `X`; vou criar a branch `Y` a partir da `main` para este ticket.” — e só
     então crie a branch correta.
4. **Nunca** commite direto na `main`.
5. Se houver alterações não commitadas, **não** troque de branch, não faça stash
   e não descarte nada sem orientação explícita. Pare e pergunte.

O nome da branch **começa pelo tipo + número do ticket**:
`feat/027-...`, `fix/012-...`, `docs/002-...`, `chore/001-...`.

### 5.2 SDD `specify` antes de implementar (obrigatório)

Antes de planejar ou codar, use o Spec-Kit para entender o contexto do ticket,
considerando o projeto e a documentação existentes:

| Ferramenta | Como invocar |
| --- | --- |
| Copilot | skill `@.github/skills/speckit-specify/` (equivale a `/speckit-specify`) |
| OpenCode | `/speckit.specify` |

Passe como contexto o ticket (número, título, corpo), os documentos `docs/01` a
`docs/06` relevantes e o estado atual da fase. O `specify` existe para
**entender antes de implementar**, não para gerar burocracia: mantenha a saída
curta, conforme [`docs/agents/sdd-conciso.md`](docs/agents/sdd-conciso.md).

> **Atenção:** o script do Spec-Kit pode tentar criar uma branch própria
> (`NNN-slug`). Mantenha a branch criada em 5.1 usando
> `GIT_BRANCH_NAME=<tipo/NNN-slug>` (ou a opção equivalente da ferramenta).
> O diretório da spec pode ser `specs/NNN-slug/`; ele não deve trocar a branch
> de trabalho.

Depois do `specify`, siga a sequência fixa abaixo. **Não sugira a sequência
inteira de uma vez**: informe apenas o próximo comando, considerando o último
concluído.

| # | Etapa | Copilot | OpenCode |
| --- | --- | --- | --- |
| 1 | especificar | `@.github/skills/speckit-specify/` | `/speckit.specify` |
| 2 | planejar | `@.github/skills/speckit-plan/` | `/speckit.plan` |
| 3 | checklist | `@.github/skills/speckit-checklist/` | `/speckit.checklist` |
| 4 | tasks | `@.github/skills/speckit-tasks/` | `/speckit.tasks` |
| 5 | implementar | `@.github/skills/speckit-implement/` | `/speckit.implement` |
| 6 | convergir | `@.github/skills/speckit-converge/` | `/speckit.converge` |

`clarify` e `analyze` são opcionais: use apenas se houver dúvida real ou
inconsistência. Eles não substituem a sequência acima.

**A sequência não é automática.** Ao terminar um comando, **pare** e aguarde o
usuário revisar o artefato e invocar o próximo. Nunca encadeie comandos
Spec-Kit sozinho; o fluxo é conduzido pelo usuário.

- **Após cada comando:** não imprima a saída completa no console. Mostre apenas
  o artefato criado, o caminho, 3 bullets de resumo e o próximo comando para o
  usuário executar.
- **Peça revisão:** encerre com “Revise `specs/.../<arquivo>.md` antes de
  seguir.”
- **Próximo comando:** informe **um único** comando, começando com `@` no
  Copilot, relativo ao último passo concluído; não o execute sozinho.
- **Depois de `tasks`:** o próximo comando é `implement`; depois de
  `implement`, `converge`.
- **Se `converge` não retornar problemas:** informe o usuário para rodar os
  testes gerais (`make check`; no Windows, os quatro comandos `uv run ...`) e
  conferir a consistência da branch. Não sugira outro comando speckit.
- **Se `converge` retornar problemas:** corrija e peça para rodar `converge`
  novamente.

Se a spec revelar ambiguidade, escopo maior que o ticket ou conflito com
`docs/01`, pare e proponha a correção do ticket/plano antes de codar.

**Conteúdo dos artefatos SDD**

- Este é um **projeto acadêmico**: explique o conceito que está sendo
  implementado, por que ele importa e como verificar. Não entregue só
  checklist.
- Meta de tamanho: **até 70 linhas por arquivo**. Não é bloqueio; a ideia é ser
  econômico para que conceito + explicação caibam em **menos de 100 linhas**.
  Se for passar de 100 linhas, procure ser ainda mais conciso após a centésima linha.

### 5.3 Fluxo por ticket

1. Leia o ticket, o **Conceito** e a seção **Leitura** (livro com capítulo e
   seção). Se o requisito for ambíguo, pergunte antes de codar.
2. Confira o campo **Paralelismo** do ticket: se outra pessoa/agente estiver nos
   mesmos arquivos, negocie a ordem.
3. Confirme a branch (§5.1) e o `specify` (§5.2).
4. Escreva o teste primeiro (quando fizer sentido) e veja falhar.
5. Implemente o mínimo para passar. Sem “melhorias de passagem”.
6. Atualize `docs/01` no mesmo PR se a gramática mudou.
7. Rode `make check` e o comando específico do ticket.
8. Abra o PR no formato de `docs/agents/pull-request.md`, referenciando o ticket
   com `Closes #N`.
9. Ao entrar em revisão, mova o card para **In Review**; após o merge, ele segue
   o fluxo de QA até **Released**.

### 5.4 Pull request pedido pelo usuário

Quando o pedido for “abrir o PR”:

1. **Rode os testes locais antes de abrir**: `make check` (no Windows, os quatro
   comandos `uv run ...`). Se falhar, não abra o PR; corrija ou relate o erro.
2. Abra o PR com `Closes #N`, título semântico e corpo baseado em
   `docs/agents/pull-request.md` (use `--body-file` para evitar escaping).
3. **Preencha o que for possível**: o que mudou, comando e resultado real,
   checklist, riscos e decisões. No que depender de julgamento humano — como o
   aprendizado pessoal — escreva “a preencher”; não invente.
4. Mova o card para **In Review** e **não faça merge**.

### 5.5 Checklists gerados pelo SDD

Quando o fluxo criar `checklists/documentation.md`,
`checklists/requirements.md` ou outro checklist, verifique **item por item**
contra o repositório e os artefatos gerados:

1. Se o item estiver atendido, marque `- [X]`.
2. Se estiver atendido após um ajuste simples, faça o ajuste e marque `- [X]`.
3. Se o item depender de decisão ou validação humana, mantenha `- [ ]`,
   explique o motivo e avise o usuário para revisar.
4. Não marque item sem verificação real; não invente evidência.

Ao final, informe quantos itens foram verificados, quais continuam abertos e por
quê. Peça revisão apenas dos itens que realmente precisam do usuário.

### 5.6 Números mágicos

- Nenhum número com significado de domínio pode aparecer direto no **código
  Python que implementa o interpretador** — produção, testes e ferramentas em
  `src/`, `tests/`, `tools/` e `scripts/`.
- Programas `.clite` de entrada ou teste **não** são analisados por esta regra e
  podem conter literais numéricos.
- Atribua o valor a uma constante nomeada em `UPPER_SNAKE_CASE`, perto do uso:
  `MAX_TOKEN_LENGTH = 256`.
- Permitidos sem constante: `0` e `1` apenas como identidades estruturais
  (índice, contador, passo) e números dentro de uma atribuição a constante.
- Exceção pontual: `# magic: allow` na mesma linha, com justificativa no PR.
- `make magic` e `tests/quality/test_magic_numbers.py` falham o PR com arquivo,
  linha e valor. Rode antes de abrir ou atualizar o PR.

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
(`/speckit-specify`) e a skill fica em `.github/skills/speckit-specify/`; no
OpenCode usam ponto (`/speckit.specify`).

**Para implementar, o `specify` é obrigatório e é a primeira etapa** (§5.2),
inclusive em pedidos pequenos e escritos em inglês. Ele não substitui o ticket:
serve para entender o contexto antes de planejar ou codar.

A sequência obrigatória é `specify` → `plan` → `checklist` → `tasks` →
`implement` → `converge` (§5.2). Cada comando é invocado pelo usuário depois de
revisar o artefato anterior; o agente não encadeia comandos automaticamente.
Depois de cada comando, peça revisão do arquivo gerado e informe **apenas o
próximo comando**, não a sequência inteira.

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
