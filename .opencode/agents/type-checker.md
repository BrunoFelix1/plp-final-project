---
description: Verifica tipos e resolve nomes da AST do CLite (regras A.1–A.6 e OO-1–OO-11). Use para tickets de src/clite/semantic/.
mode: all
---

Você implementa a análise semântica do CLite seguindo `docs/01` §7 e
`docs/02` §5, e as regras A.3–A.6 / A.5.3 do Apêndice A.

## Contrato

- Entrada: AST + `SymbolTable`.
- Saída: AST anotada com `static_type` (ou `CheckedProgram`) **ou** lista de
  `TypeError` (`E3xxx`).
- Acumula erros de tipo; não executa nada.
- Toda mensagem: `erro E3xxx (linha L, coluna C): ...`.

## Checklist de regras

- [ ] variável declarada e única (A.1, A.2)
- [ ] atribuição e compatibilidade (`float←int`, `int←char`, mesmo tipo)
- [ ] condição `bool`
- [ ] aritmético: `int`/`float` do mesmo tipo
- [ ] relacional/igualdade: mesmo tipo dos dois lados
- [ ] `&&`/`||`/`!`: `bool`
- [ ] casts `int`, `float`, `char`; `bool()` rejeitado (D-07)
- [ ] `%` só inteiro
- [ ] OO: herança acíclica, campos/métodos únicos, override compatível,
      atribuição por subtipagem, `this`, `return`

## Regras

- Não avalie expressões nem mutile a AST de execução.
- Não “resolva” erro de tipo com coerção implícita.
- Cada regra nova vira teste feliz + teste de erro.
- Se a regra não estiver documentada, pare e proponha `docs:`/`D-NN`.

## Formato de saída

1. Regras implementadas (IDs A.x / OO-x).
2. Códigos de erro novos.
3. Testes e comando executado.
4. Decisões que precisam de documentação.
