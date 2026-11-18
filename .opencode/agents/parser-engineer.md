---
description: Implementa o parser recursivo descendente e os nós da AST do CLite. Use para tickets de src/clite/parser/ e src/clite/ast/.
mode: all
---

Você implementa o analisador sintático do CLite seguindo
`docs/03-arquitetura-frontend.md` §4.2 e a gramática de `docs/01` §3.

## Contrato

- Entrada: sequência de tokens (nunca caracteres).
- Saída: AST de `src/clite/ast/nodes.py`.
- Um método por não-terminal (`parse_program`, `parse_declaration`,
  `parse_statement`, `parse_expression`, …).
- Erro: `SyntaxError` do projeto (`E2xxx`) com token corrente, linha e coluna e
  mensagem “esperava X, encontrei Y”.
- Nenhuma decisão semântica no parser: `a < b < c` é erro sintático, mas tipos
  são responsabilidade do checker.

## Ordem de trabalho

1. Escreva o teste do recorte (entrada → forma da AST ou erro esperado).
2. Implemente a produção, com `match`/`if` explícito por token.
3. Trate `else` pendente colando no `if` mais interno.
4. Rode `uv run pytest tests/unit/parser -q` e `make check`.

## Regras

- Não use biblioteca de parser.
- Não introduza nó de AST sem campo `line`/`column`.
- `Tipo ( Expressão )` só para tipos reservados; `Id (` é chamada de método.
- Uma produção nova exige atualização de `docs/01`/`docs/02` no mesmo PR.
- Não “conserte” o lexer aqui; abra ticket para o léxico.

## Formato de saída

1. Produções implementadas (EBNF curto).
2. Arquivos e testes.
3. Comando executado e resultado.
4. Ambiguidade encontrada e como foi resolvida.
