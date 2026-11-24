# Research: Arquitetura do front-end

## R1 · Nome do pacote de tipos no Apêndice A

- **Decision**: usar `symbols`.
- **Rationale**: a introdução do Apêndice A lista "main, lexer, symbol, parser e
  inter", mas o código do próprio livro usa `import symbols.*`, e o texto da A.3 diz que
  "a classe Type faz parte do pacote symbols". O código manda.
- **Alternatives**: manter `symbol` (fiel à frase, mas diverge do código e da tabela da §2).

## R2 · Justificativa dos visitantes

- **Decision**: referenciar D-02 e a discussão "orientado a objeto × orientado a
  fase" da introdução do Apêndice A.
- **Rationale**: D-02 (`docs/05`) registra a escolha do time (testabilidade e
  paralelismo). O livro dá a teoria: orientado a objeto facilita adicionar
  **construções**; orientado a fase facilita adicionar/mudar **fases**. O custo
  aceito é que um nó novo exige um caso em cada visitante.
- **Alternatives**: métodos `check`/`eval` nos nós, descartados em D-02.

## R3 · Fronteira v1 / v2 nos contratos

- **Decision**: marcar como (v2) os itens de OO em §4.3 e §4.4.
- **Rationale**: na v1 só há `main`, escopo único (D-06) e nenhuma chamada de
  método. Classe corrente, `this`, heap, pilha de frames e `ReturnSignal` só
  existem com classes (`docs/02`, D-09, D-15).
- **Alternatives**: mover tudo de v2 para o `docs/02` (mais mudança do que o
  ticket pede, o que viola T0).

## R3a · "Semantic" ou "TypeChecker"?

- **Decision**: a caixa se chama `Semantic (TypeChecker)`.
- **Rationale**: Compiladores §1.2.3 e Fig. 1.6: a fase é o "Analisador
  Semântico" e "uma parte importante da análise semântica é a verificação de
  tipo" (Fig. 1.7: "o verificador de tipos no analisador semântico"). Tucker §2.4
  (p. 47): "fase da análise semântica ou verificador de tipo", com 3 tarefas
  (declaração, tipos, conversões); §6.1: a implementação é o "verificador de
  tipos" (`StaticTypeCheck`). Fase = semântica; componente = verificador de tipos.
- **Alternatives**: só `TypeChecker` (esconde a resolução de nomes); só
  `Semantic` (não liga ao nome da classe usado em §2 e §4.3).

## R4 · Módulos no diagrama

- **Decision**: citar os 9 módulos existentes (`lexer`, `parser`, `ast`, `semantic`,
  `interpreter`, `errors`, `types`, `symbols`, `values`) e o ponto de entrada `cli`.
- **Rationale**: é o critério de verificação do ticket ("o diagrama cita todos os
  pacotes de src/clite/").
