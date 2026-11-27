# Contrato: `clite.ast.nodes`

Superfície pública que o parser (010, paralelo) e as fases seguintes podem
assumir. Nada além disto é garantido.

## Garantias

| Garantia | Detalhe |
| --- | --- |
| Import | `from clite.ast.nodes import Program, Assign, ...` (módulo direto; `ast/__init__.py` não reexporta) |
| Imutabilidade | todo nó é frozen; tentativa de escrita → `FrozenInstanceError` |
| Igualdade | estrutural e recursiva (mesmos campos → iguais) |
| Posição | `line`/`column` em todo nó; padrão `0` = não informado; construtor aceita por último |
| Tipos de domínio | `CliteType` restrito a `int/float/char/bool` em declarações e `Convert` |
| Sem lógica | nós não validam, não visitam, não avaliam (D-02) |
| Sem tokens | nós guardam posição, nunca objetos `Token` (`docs/03` §4.2) |

## Lista fechada de nós

`Program`, `VarDecl`, `ArrayDecl`, `Skip`, `Block`, `Assign`, `If`, `While`,
`VarRef`, `ArrayRef`, `Binary`, `Unary`, `Convert`, `IntLiteral`,
`FloatLiteral`, `BoolLiteral`, `CharLiteral` — e nada mais (sem `Print`; D-04
entra com o parser, ticket 033 rastreia a divergência §3/§6).

## Para o parser (010)

- Construção: posicional sem posição (`Binary('+', l, r)`) ou com posição no fim.
- `Assign.target` aceita `VarRef` ou `ArrayRef` (`x = e` e `v[i] = e`).
- `If` sem `else`: `else_branch=None` — não sintetizar `Skip`.
- `ArrayDecl.size` é `int` literal (§6), não expressão.
- Bloco não cria escopo (D-06) — apenas `Block(commands)`.
