# CLite em Python

Interpretador da **CLite**, a linguagem didática do capítulo 2 de Tucker e
Noonan, escrito em Python e organizado como o **front-end completo** do Apêndice
A de *Compiladores: Princípios, Técnicas e Ferramentas*.

O projeto tem um objetivo prioritário: **aprender como uma linguagem de
programação é construída** — do caractere ao resultado da execução. Cada fase é
visível, testável e documentada.

> **Status:** planejamento e esqueleto. Nenhuma fase da linguagem foi
> implementada ainda. Os tickets no board definem a ordem de construção.

## O que você vai encontrar

| Fase | O que faz | Onde |
| --- | --- | --- |
| Léxico | remove espaços/comentários e produz tokens com linha e coluna | `src/clite/lexer/` |
| Sintático | parser descendente recursivo que produz a AST | `src/clite/parser/` |
| Semântico | resolve nomes e verifica tipos antes de executar | `src/clite/semantic/` |
| Execução | avalia a AST sobre um estado de variáveis e objetos | `src/clite/interpreter/` |

```text
programa.clite → [lexer] → tokens → [parser] → AST → [checker] → [interpretador] → saída
```

## Escopo

**v1 — núcleo CLite** (Tucker e Noonan, 2.3 e Apêndice A)

- `int`, `bool`, `float`, `char`; variáveis e arrays de tamanho fixo;
- atribuição, bloco, `if`/`else`, `while`, `;` (skip);
- expressões com precedência e associatividade definidas;
- sistema de tipos A.1–A.6 e semântica A.1–A.12;
- erros com código, linha e coluna.

**v2 — orientação a objetos** (`docs/02-extensao-oo.md`)

- classes com campos e métodos, herança simples (`extends`);
- `new`, `this`, acesso a campo, chamada de método;
- sobreescrita e polimorfismo por despacho dinâmico.

**Fora de escopo:** classe abstrata, interface, reflexão, construtores,
sobrecarga, `null`, exceções, funções de topo, geração de código de máquina.
As justificativas estão em [`docs/05-decisoes.md`](docs/05-decisoes.md).

## Começando

O projeto roda em **Linux, macOS e Windows 10/11**. Você só precisa de Git e
[`uv`](https://docs.astral.sh/uv/); o `uv` instala e gerencia o Python 3.12
sozinho. O `make` é opcional: no Windows, use os comandos `uv run` equivalentes.

> **Git, se ainda não tiver:** Linux `sudo apt install git` (Debian/Ubuntu) ou
> `sudo dnf install git` (Fedora); macOS `xcode-select --install` ou
> `brew install git`; Windows `winget install --id Git.Git -e`. Confirme com
> `git --version`.

### 1. Instale o `uv`

**Linux**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**macOS**

```bash
brew install uv
# alternativa sem Homebrew:
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell)**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Se preferir um gerenciador de pacotes:

```powershell
winget install --id=astral-sh.uv -e
```

Feche e reabra o terminal e confirme:

```bash
uv --version
uv python install 3.12
```

> Se você já tem Python 3.12+ instalado, o `uv` reaproveita a versão do sistema.
> O comando `uv python install` garante uma versão gerenciada e reprodutível.

### 2. Clone e sincronize o ambiente

```bash
git clone https://github.com/BrunoFelix1/plp-final-project.git
cd plp-final-project
uv sync
```

O `uv sync` cria a `.venv`, instala as dependências de desenvolvimento e respeita
o `uv.lock` versionado.

### 3. Verifique a instalação

**Linux e macOS**

```bash
make check              # lint + tipos + testes (mesmo conjunto do CI)
make test               # apenas os testes
```

**Windows (PowerShell ou Prompt de Comando), sem `make`**

```powershell
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
```

Se você usa **Git Bash** ou **WSL** no Windows, os comandos do Linux/macOS
funcionam, incluindo `make` e os scripts `.specify/scripts/bash/`.

### 4. Opcional: hooks de pre-commit

```bash
uv run pre-commit install
```

A CLI `clite` será criada no ticket `feat: 004`; até lá, os comandos acima
validam apenas o esqueleto.

### Problemas comuns

| Sintoma | Causa provável | Solução |
| --- | --- | --- |
| `uv: command not found` | terminal aberto antes da instalação | feche e reabra o terminal; no Windows, confira o `PATH` |
| PowerShell bloqueia o instalador | política de execução | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` e tente de novo |
| `make: command not found` | Windows sem `make` | use os quatro comandos `uv run` acima, ou Git Bash/WSL |
| `python` não encontrado | Python não está no `PATH` | `uv python install 3.12` e use `uv run` (não chame `python` direto) |
| scripts do Spec-Kit não executam | são Bash | rode no Linux/macOS, Git Bash ou WSL |
| acentos/paths com espaço | shell padrão do Windows | use aspas e, de preferência, Git Bash/WSL |

## Tecnologias

| Camada | Escolha | Por quê |
| --- | --- | --- |
| Linguagem | Python 3.12+ | legibilidade e foco no conceito |
| Sistemas | Linux, macOS, Windows 10/11 | mesma base de código e comandos `uv run` |
| Ambiente | [uv](https://docs.astral.sh/uv/) | instalação rápida, Python gerenciado e lockfile reprodutível |
| Testes | pytest + pytest-cov + Hypothesis | unidade, conformidade e propriedades |
| Lint/format | Ruff | uma ferramenta, configuração única |
| Tipos | mypy (strict em `src/`) | contrato entre fases |
| Hooks | pre-commit | feedback antes do commit |
| CI | GitHub Actions | mesmo conjunto do `make check` em todo PR |
| SDD | Spec-Kit (`specify`) | especificar antes de implementar |

Sem dependências de runtime: o interpretador usa apenas a biblioteca padrão.

## Estrutura do repositório

```text
.
├── AGENTS.md                 # guia para agentes de IA e pessoas
├── README.md
├── SPECKIT-USAGE.md          # como usar o SDD neste projeto
├── pyproject.toml            # projeto, pytest, ruff, mypy
├── Makefile                  # atalhos: check, test, lint, types
├── docs/                     # gramática, arquitetura, decisões, casos difíceis
├── examples/                 # programas .clite (criados junto com cada fase)
├── jornadas/                 # roteiros HTML de onboarding
├── src/clite/                # implementação (esqueleto de pacotes)
├── tests/                    # unidade, conformidade e erros
├── specs/                    # artefatos do Spec-Kit
├── .specify/                 # constituição, templates e scripts do Spec-Kit
├── .opencode/                # comandos, agentes e skills do OpenCode
└── .github/                  # CI, agentes/skills do Copilot e templates
```

## Documentação

Leia [`docs/README.md`](docs/README.md). Atalhos:

- [Gramática e semântica da v1](docs/01-linguagem-clite.md)
- [Extensão orientada a objetos](docs/02-extensao-oo.md)
- [Arquitetura do front-end](docs/03-arquitetura-frontend.md)
- [Plano de aprendizado e cronograma](docs/04-plano-de-aprendizado.md)
- [Decisões (ADRs)](docs/05-decisoes.md)
- [Casos difíceis](docs/06-casos-dificeis.md)

## Roadmap

| Milestone | Até | Entrega |
| --- | --- | --- |
| M1 · Fundação e léxico | 21/11/2026 | ferramentas, gramática documentada, lexer e CLI `tokens` |
| M2 · Núcleo executável | 26/11/2026 | parser, AST, tipos, interpretador e arrays |
| M3 · Conformidade | 01/12/2026 | erros, casts, suíte de conformidade e gate de cobertura |
| M4 · Orientação a objetos | 04/12/2026 | classes, herança, override e polimorfismo |
| M5 · Entrega | 06/12/2026 | manual, demos, release v1.0.0 |

O board do GitHub concentra os tickets pequenos, um por incremento verificável:
<https://github.com/users/BrunoFelix1/projects/3/views/1>.
As colunas são Backlog, To Do, In Progress, In Review, Ready for QA, In QA e
Released; os milestones M1–M5 têm as datas da tabela acima.

## Spec-Driven Development

```text
Copilot:  /speckit-specify  /speckit-plan  /speckit-checklist  /speckit-tasks
          /speckit-implement  /speckit-converge
OpenCode: /speckit.specify  /speckit.plan  /speckit.checklist  /speckit.tasks
          /speckit.implement  /speckit.converge
```

A sequência é conduzida pelo usuário: ao fim de cada comando, revise o artefato
e invoque o próximo. O agente não encadeia comandos automaticamente.

Todos os artefatos do SDD são gerados em formato **sucinto e objetivo** (ver
[`docs/agents/sdd-conciso.md`](docs/agents/sdd-conciso.md)). O guia completo
está em [`SPECKIT-USAGE.md`](SPECKIT-USAGE.md).

## Jornadas

Roteiros guiados para conhecer o projeto, com progresso e anotações salvos no
navegador:

- [Jornada inicial do desenvolvedor](jornadas/jornada-inicial-desenvolvedor.html)
  — 30 min para entender o contexto, o repositório, o board, os conceitos e o
  método de aprendizado, terminando com a escolha do primeiro ticket.

## Como contribuir

1. Escolha um ticket no board e leia o documento da fase.
2. Crie a branch `tipo/NNN-slug`.
3. Implemente com teste; rode `make check` (ou os comandos `uv run`
   equivalentes no Windows).
4. Abra o PR no formato de
   [`docs/agents/pull-request.md`](docs/agents/pull-request.md), com `Closes #N`
   e o comando de teste executado.
5. Mova o card no board conforme o fluxo de QA.

## Licença

MIT — ver [`LICENSE`](LICENSE).
