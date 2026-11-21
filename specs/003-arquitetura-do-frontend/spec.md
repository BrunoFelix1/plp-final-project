# Feature Specification: Arquitetura do front-end

**Feature Branch**: `docs/003-arquitetura-do-frontend`
**Created**: 2026-11-21 · **Status**: Draft
**Input**: `docs: 003 - mapear as fases e os pacotes do Apêndice A (Java) para a
arquitetura Python do projeto` (#3)

<!--
  REGRA DO PROJETO: meta de 70 linhas; se passar de 100, seja mais conciso.
  Tabelas e checklists em vez de prosa. Explique o conceito que será implementado.
  Não repita docs/01, docs/02, AGENTS.md nem tickets. Cite.
  Leia .specify/memory/constitution.md antes de preencher.
-->

## Conceito

**Fases do front-end.** A análise (front-end) transforma o fonte em representações
cada vez mais abstratas: caracteres → tokens → árvore → árvore verificada, com a
tabela de símbolos ao lado de todas as fases (Compiladores §1.2). Um interpretador
troca as últimas fases (otimizar e gerar código) por um programa que executa a
representação intermediária (Tucker §2.4). Definir o **contrato** de cada
fronteira é o que permite implementar e testar uma fase por vez. O Apêndice A
agrupa o código por construção (orientado a objeto); nós o agrupamos por fase
(visitantes, D-02).

## User Scenarios & Testing

### User Story 1 - Entender o caminho do programa (Priority: P1)

Como estudante, quero ver num só documento as fases, o que cada uma entrega à
próxima e em que pacote de `src/clite/` ela vive, para implementar uma fase sem
ler as outras.

**Why this priority**: todos os tickets `feat:` dependem desses contratos.

**Independent Test**: revisão de `docs/03-arquitetura-frontend.md` comparando
o diagrama com `ls src/clite`.

**Acceptance Scenarios**:

1. **Given** o diagrama, **When** o leitor procura qualquer módulo de `src/clite/`,
   **Then** encontra o módulo e o seu papel.
2. **Given** a tabela Java → Python, **When** o leitor procura uma classe do
   Apêndice A, **Then** encontra o módulo Python e a decisão correta (D-02).

### User Story 2 - Saber o que é v1 e o que é v2 (Priority: P2)

Como revisor, quero que os contratos separem o núcleo (v1) da extensão OO (v2),
para não exigir de um ticket da v1 algo que só existe na v2.

**Independent Test**: as §§4.3–4.4 marcam `this`, heap, frames e `return` como v2.

### Edge Cases

- Um módulo citado no documento que ainda não existe em `src/clite/` aparece no
  diagrama sem comentário sobre o ticket que o cria.
- O nome do pacote Java fica alinhado ao código do livro (`symbols`).

## Requirements

### Functional Requirements

- **FR-001**: O `docs/03` MUST ter um diagrama de fases que cite os 9 módulos
  de `src/clite/` (`lexer`, `parser`, `ast`, `semantic`, `interpreter`, `errors`,
  `types`, `symbols`, `values`) e o ponto de entrada `cli`. Pacotes de fase vão
  ao lado da caixa da fase; módulos de apoio entram como seta lateral na fase
  que os usa (como a tabela de símbolos na Fig. 1.6 do Compiladores); `cli.py`
  no topo, como entrada; `errors.py` numa linha "usado por todas as fases".
- **FR-001a**: A caixa da fase semântica MUST se chamar `Semantic (TypeChecker)`:
  a fase é a análise semântica e o verificador de tipos é seu componente
  (Compiladores §1.2.3; Tucker §2.4 e §6.1).
- **FR-002**: O `docs/03` MUST ter a tabela Java (Apêndice A) → Python com a
  referência correta à decisão dos visitantes (D-02).
- **FR-003**: O `docs/03` MUST descrever os contratos lexer→parser→checker→
  interpretador, separando o que é v1 do que é v2.
- **FR-004**: O `docs/03` MUST definir a política de erros `E1xxx`–`E4xxx`
  (formato, quando parar e quando coletar) e a CLI (subcomandos e códigos de saída).
- **FR-005**: Os links de `docs/README.md` para o `docs/03` MUST continuar válidos.

### Key Entities

- **Fase**: transformação de uma representação em outra (tokens, AST, AST verificada, estado).
- **Contrato de fronteira**: o que uma fase entrega e o que a seguinte pode assumir.
- **Política de erros**: faixa de códigos por fase e formato da mensagem.

## Success Criteria

### Measurable Outcomes

- **SC-001**: 9/9 módulos de `src/clite/` (mais o `cli`) aparecem no diagrama.
- **SC-002**: Zero referências cruzadas erradas (D-xx, nomes de pacote do livro).
- **SC-003**: Os 3 itens "Pronto quando" do ticket são confirmados em revisão por pares.
- **SC-004**: `make check` continua verde (nenhum código alterado).

## Assumptions

- O `docs/03` já existe e está quase completo: o trabalho é uma **edição
  cirúrgica** (T0), não uma reescrita.
- O PR #38 (ticket 002) também altera `docs/README.md`; só mexer nele se for
  necessário, para evitar conflito.

## Fora de escopo, riscos e referências

- **Fora de escopo**: implementar fases; trocar visitantes por métodos nos nós
  (D-02); corrigir `src/clite/errors.py`.
- **Riscos**: (1) conflito em `docs/README.md` com o PR #38 → não tocar nele salvo
  necessidade; (2) misturar v1/v2 de novo → marcar explicitamente cada item v2.
- **Referências**: Compiladores §1.2 e Apêndice A (intro); Tucker e Noonan §2.4;
  `docs/01`, `docs/02`, `docs/05` (D-02, D-06).
