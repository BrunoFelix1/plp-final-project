# Research: Ticket 002

## Decisões

| Decisão | Racional | Alternativas descartadas |
| --- | --- | --- |
| Glossário em `docs/01` | mantém uma fonte de verdade e atende o leitor da gramática | novo arquivo, que duplicaria conceitos |
| Revisar antes de reescrever | a EBNF, tokens, precedência e catálogo já existem | reescrita integral, com diff difícil de revisar |
| Validar links por existência dos arquivos | o ticket pede links locais, não uma ferramenta externa | dependência nova de lint Markdown |

## Achados

- Não há clarificação pendente: o ticket define três arquivos e seis termos.
- `docs/01` já possui EBNF, tokens, precedência e AST, mas precisa explicitar
  conversões, substituir `Boleano` por `Booleano` e explicar `decpart`/`body`.
- A lista de reservadas deve concordar com a regra textual que inclui palavras
  da v2; `||` deve continuar escapado no Markdown e renderizar como `||`.
- `docs/06` tem as quatro categorias, mas deve separar/rotular exemplos OO e
  evitar que `print` pareça parte da gramática v1.
- O trabalho não expõe API, CLI nem contrato de integração novo.
- `docs/02` permanece fora da implementação; a gramática OO é desenho-alvo.

## Referências

`docs/01-linguagem-clite.md` §§2–5, `docs/06-casos-dificeis.md` §§1–4,
`docs/README.md`, `docs/05-decisoes.md` D-02/D-03, Tucker e Noonan §§2.3 e 2.5.
