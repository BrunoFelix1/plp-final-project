# Tasks: Arquitetura do front-end

**Input**: `spec.md`, `plan.md`, `research.md`, `quickstart.md`
**Pré-requisito**: `make check` verde antes de começar; não há código de runtime.

<!--
  Uma linha por task. [P] = pode rodar em paralelo; [US] = história atendida.
  Único arquivo alterado: docs/03-arquitetura-frontend.md (edição cirúrgica, T0).
  As tasks não marcam a checklist do revisor.
-->

## Phase 1: Setup

- [x] T001 Confirmar branch `docs/003-arquitetura-do-frontend`, a edição já feita no diagrama (`Semantic`) e `make check` verde — `docs/03-arquitetura-frontend.md` — `git branch --show-current; git diff --stat`

## Phase 2: Foundational

- [x] T002 Rodar o quickstart §1–§2 **antes** da edição e guardar o resultado (deve mostrar as faltas atuais) — `docs/03-arquitetura-frontend.md` — `quickstart.md §1–§2`

## Phase 3: User Story 1 (P1) — entender o caminho do programa

- **Objetivo**: diagrama e tabela Java → Python completos e corretos.
- **Teste independente**: quickstart §1 com 10 `ok` + leitura do diagrama.
- [x] T003 [US1] Diagrama §1: pacote ao lado de cada caixa (`lexer/`, `parser/ → ast/`, `semantic/`, `interpreter/`) — `docs/03` §1 — quickstart §1
- [x] T004 [US1] Diagrama §1: caixa `Semantic` → `Semantic (TypeChecker)` (FR-001a, R3a) — `docs/03` §1 — revisão visual
- [x] T005 [US1] Diagrama §1: setas laterais `← symbols.py, types.py` (Semantic) e `← values.py` (Interpreter); `cli.py (entrada)` no topo; linha `errors.py: usado por todas as fases (E1xxx–E4xxx)` — `docs/03` §1 — quickstart §1
- [x] T006 [US1] Cabeçalho: pacote Java `symbol` → `symbols` (R1) — `docs/03` cabeçalho — `grep -n "symbol" docs/03-arquitetura-frontend.md`
- [x] T007 [US1] §2, último parágrafo: "Ver D-05" → "Ver D-02" e citar a discussão orientado a objeto × orientado a fase do Apêndice A (R2) — `docs/03` §2 — `grep -n "D-0" docs/03-arquitetura-frontend.md`

## Phase 4: User Story 2 (P2) — separar v1 de v2

- **Objetivo**: os contratos não exigem da v1 o que só existe na v2.
- **Teste independente**: quickstart §3.
- [x] T008 [US2] §4.3: marcar como (v2) "classe corrente", "retorno do método" e as partes de classes/campos/métodos dos globais — `docs/03` §4.3 — leitura
- [x] T009 [US2] §4.4: marcar como (v2) `heap`, frames de chamada de método e `ReturnSignal`; anotar que na v1 o estado é um único mapa de variáveis (D-06) — `docs/03` §4.4 — leitura

## Phase 5: Polish

- [x] T010 [P] Conferir que §5 (erros) bate com D-12 e §6 (CLI) segue completa; **sem mudanças** se já estiverem corretas — `docs/03` §5–§6 — leitura contra `docs/05`
- [x] T011 [P] Conferir o diff: só `docs/03` alterado, nenhuma linha reformatada (T0), ~20 linhas — `docs/03` — `git diff --stat; git diff --check`
- [x] T012 Rodar quickstart §1–§4 e os gates gerais; registrar o resultado no PR — `docs/`, `Makefile` — 4 comandos `uv run`

## Dependencies

| Task | Depende de | Bloqueia |
| --- | --- | --- |
| T002 | T001 | T003–T009 |
| T003, T004, T005 | T002 | T011 |
| T006, T007 | T002 | T011 |
| T008, T009 | T002 | T011 |
| T012 | T010–T011 | — |

## Parallel Example

```text
# Mesmo arquivo: faça em sequência para evitar conflito de edição.
# Seções disjuntas podem ser revisadas juntas:
T006 (cabeçalho)   T007 (§2)   T008–T009 (§4)
```

## Implementation Strategy

MVP = US1 (diagrama + tabela), que fecha o critério de verificação do ticket.
Depois, US2 (v1 × v2). Ao final, `make check` verde e PR com `Closes #3`.
