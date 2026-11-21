# Data Model: documentação do CLite

O “modelo” deste ticket é um conjunto de entidades editoriais, não dados de
runtime.

| Entidade | Conteúdo | Validação |
| --- | --- | --- |
| GClite | produções EBNF, notação e exemplos | `{ }` = repetição; `[ ]` = opcional; `Booleano` |
| Token | categoria, lexema e posição | tabela cobre reservadas, literais, operadores e pontuação |
| Precedência | níveis, operadores e associatividade | ordem coincide com `docs/01` §5 |
| AST | nós abstratos, incluindo conversão | não confundir com árvore de análise concreta |
| Glossário | token, lexema, AST, parser, tabela de símbolos e type checking | seis definições curtas e didáticas |
| Caso difícil | entrada, categoria e comportamento esperado | v1 separada de exemplos OO/futuros |

## Relações e restrições

- GClite é a referência; tokens e precedência explicam como lê-la.
- O glossário aponta para as fases descritas em `docs/03`, sem redefini-las.
- Cada caso difícil deve ter comportamento observável e não pode introduzir
  construção fora de `docs/01`.
- O índice deve apontar para arquivos existentes; não criar uma segunda fonte.
