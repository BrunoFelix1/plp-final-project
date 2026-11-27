# Research: Tabela de símbolos (ticket 012)

Data: 2026-11-27. As decisões foram tomadas no plano aprovado em sessão; este
arquivo consolida escolha, justificativa e alternativas.

## D1 — API AST-cêntrica

- **Decisão**: a tabela registra e devolve os nós de declaração da AST
  (`VarDecl`/`ArrayDecl` da #9).
- **Rationale**: fonte única de verdade para nome, tipo e posição; integração
  direta com o checker (#13/#14), que já percorre a AST.
- **Alternativas**: entrada própria (`SymbolEntry`) — duplicaria
  nome/tipo/posição e exigiria conversão no checker; `declare('x', IntType)`
  literal do ticket — não carrega posição, necessária aos erros.

## D2 — Erro semântico local

- **Decisão**: `SemanticError` definida em `symbols.py`, mesmo formato da
  `LexicalError` (lexer.py:29): `code`/`line`/`column`/`message` e mensagem
  `erro E<NNNN> (linha L, coluna C): texto` montada no construtor.
- **Rationale**: precedente aceito da #7; mantém o ticket nos seus arquivos;
  `errors.py` segue esqueleto até a #19 (M3) unificar a hierarquia.
- **Alternativas**: semear `errors.py` agora — antecipa a #19 e toca arquivo
  fora do ticket; retornar código sem lançar — política de erro ambígua e os
  testes do ticket pedem "gera E3002".

## D3 — Tipos como literais da AST

- **Decisão**: a tabela não cria descritores de tipo; usa o `CliteType`
  (Literal) que o nó já carrega.
- **Rationale**: `types.py` é esqueleto e nenhum ticket do M2 o preenche;
  #13/#14 trabalham com os literais da AST.
- **Alternativas**: criar singletons `IntType` etc. agora — escopo extra sem
  consumidor nesta fatia.

## D4 — Escopo único e ordem de inserção

- **Decisão**: mapa plano `dict` (inserção preservada); nenhuma pilha de escopos.
- **Rationale**: D-06 e o livro: blocos não contêm declarações (§2.3), mapa de
  tipos único (§6.3), estado plano (Regra 8.1); `dict` preserva ordem.
- **Alternativas**: pilha de escopos (`Scope`) — generalização sem consumidor na
  v1; a v2 pode reintroduzi-la (docs/03 §3 já lista `Scope`).

## D5 — Posição nos erros

- **Decisão**: `E3002` usa a posição da segunda declaração (nó rejeitado);
  `E3001` usa a posição da referência informada na busca; sem posição, o padrão
  da AST (0, 0 = "não informado").
- **Rationale**: docs/06 §3 e convenção da AST (0 = não informado).
- **Alternativas**: posição do primeiro registro no `E3002` — aponta para a
  declaração antiga, não para a linha do erro.
