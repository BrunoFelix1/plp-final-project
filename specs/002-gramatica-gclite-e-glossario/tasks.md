# Tasks: Gramática GClite e glossário

**Input**: `spec.md`, `plan.md`, `research.md`, `data-model.md`, `quickstart.md`
**Pré-requisito**: revisar a checklist de qualidade; não há código de runtime.

<!--
  Uma linha por task. [P] = pode rodar em paralelo; [US] = história atendida.
  As tasks de documentação não devem marcar a checklist pertencente ao revisor.
-->

## Phase 1: Setup

- [x] T001 [P] Preparar a implementação na branch correta e confirmar o escopo dos três documentos — `specs/002-gramatica-gclite-e-glossario/` — `git status --short`
- [x] T002 [P] Mapear FR-001–FR-005 e SC-001–SC-003 para os critérios de revisão — `specs/002-gramatica-gclite-e-glossario/checklists/documentation.md` — inspeção da matriz

## Phase 2: Foundational

- [x] T003 [P] Consolidar o padrão editorial: `docs/01` como fonte v1, `docs/02` como desenho OO e nenhum contrato externo — `docs/01-linguagem-clite.md` — revisão contra `research.md`

## Phase 3: User Story 1 (P1)

- **Objetivo**: permitir que o estudante leia a sintaxe concreta, a AST, tokens e precedência sem ambiguidades.
- **Teste independente**: revisar `docs/01-linguagem-clite.md` e abrir os links do índice.
- [x] T004 [US1] Corrigir `Booleano`, explicar `decpart`/`body`, representar conversão na AST e consolidar a tabela de reservadas/`||` — `docs/01-linguagem-clite.md` — revisão das seções 3–6
- [x] T005 [US1] Atualizar a descrição do índice para incluir o glossário e manter somente links para arquivos existentes — `docs/README.md` — checagem de links relativos

## Phase 4: User Story 2 (P2)

- **Objetivo**: permitir que o revisor encontre o vocabulário mínimo e diferencie bordas da v1 de exemplos OO futuros.
- **Teste independente**: localizar as seis definições e as quatro categorias de `docs/06-casos-dificeis.md`.
- [x] T006 [US2] Adicionar seção explícita com token, lexema, AST, parser, tabela de símbolos e type checking — `docs/01-linguagem-clite.md` — busca pelos seis termos
- [x] T007 [US2] Esclarecer o caso de variável não inicializada e rotular exemplos OO/`print` como futuros, preservando o catálogo v1 — `docs/06-casos-dificeis.md` — revisão das seções 1–4

## Phase 5: Polish

- [x] T008 [P] Fazer revisão cruzada dos cinco FRs, três SCs e checklist de qualidade sem marcar itens do revisor — `specs/002-gramatica-gclite-e-glossario/` — `git diff --check`
- [x] T009 [P] Validar todos os destinos Markdown relativos do índice e conferir as bordas documentadas — `docs/README.md`, `docs/06-casos-dificeis.md` — script de links + revisão manual
- [x] T010 Rodar os gates gerais e registrar o resultado no PR — `Makefile`, `docs/` — `make check`

## Dependencies

| Task | Depende de | Bloqueia |
| --- | --- | --- |
| T003 | T001–T002 | T004–T007 |
| T004 | T003 | T006 |
| T005 | T003 | T008–T009 |
| T006 | T004 | T008 |
| T007 | T003 | T008–T009 |
| T010 | T008–T009 | — |

## Parallel Example

```text
# Após T001–T003, podem rodar juntas (arquivos disjuntos):
T004  docs/01-linguagem-clite.md (gramática/AST)
T005  docs/README.md
T007  docs/06-casos-dificeis.md
```

## Implementation Strategy

MVP = User Story 1: `docs/01` e `docs/README` claros e navegáveis. Depois,
concluir User Story 2 com glossário e catálogo separado. Cada fase termina com
revisão documental; `make check` é o gate final, pois não há teste de runtime.

## Phase 6: Convergence

- [ ] T011 Solicitar revisão por pares da checklist `specs/002-gramatica-gclite-e-glossario/checklists/documentation.md` e registrar a aprovação ou os ajustes necessários per SC-003 (missing)
- [x] T012 Abrir ou atualizar o PR com `make check` e seu resultado, conforme a documentação operacional per T010 / Constitution VII (partial)
