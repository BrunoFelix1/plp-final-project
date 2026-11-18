---
name: Gramática CLite
description: Consultar, validar e alterar a gramática do CLite. Use antes de mexer em lexer/parser, ao propor extensão ou ao revisar ambiguidade e regras de tipo.
---

# Gramática CLite

Fonte da verdade: `docs/01-linguagem-clite.md` (v1) e
`docs/02-extensao-oo.md` (v2).

## Consulta rápida

| Dúvida | Seção |
| --- | --- |
| produção de um comando | `docs/01` §3 |
| tokens e palavras reservadas | `docs/01` §4.2 |
| precedência | `docs/01` §5 |
| tipos | `docs/01` §7, `docs/02` §5 |
| semântica | `docs/01` §8 |
| decisões e lacunas | `docs/05-decisoes.md` |
| casos de borda | `docs/06-casos-dificeis.md` |

## Invariantes

- `main` é palavra reservada.
- Palavras da v2 (`class`, `extends`, `new`, `this`, `return`, `void`, `print`)
  já são reservadas na v1 (D-03).
- `[[ ]]` na gramática do livro é metanotação de “opcional”, não colchete duplo.
- Relacionais e igualdade **não** são associativos.
- Blocos não criam escopo.
- Tamanho de array é literal inteiro.

## Como alterar

1. Abra ticket `docs:` com a produção e o impacto.
2. Edite a produção no documento **antes** do código.
3. Atualize tokens, precedência e regras de tipo afetadas.
4. Liste programas afetados e adicione casos em `docs/06`.
5. Só então abra ticket `feat:` para a implementação.
6. No PR, o diff de `docs/01`/`docs/02` acompanha o diff de código.

## Checagem de ambiguidade

- `else` pendente: resolve no `if` mais interno.
- `Tipo(` × `Id(`: tipo primitivo é reservado; `Id(` é chamada.
- `a < b < c`: erro sintático, não avaliação encadeada.
- `-` unário × binário: o parser decide pelo contexto do fator.
