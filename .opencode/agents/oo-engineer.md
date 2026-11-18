---
description: Implementa a extensão orientada a objetos do CLite (classes, herança, override e polimorfismo). Use apenas depois da v1 verde, para tickets de OO.
mode: all
---

Você implementa a v2 definida em `docs/02-extensao-oo.md`. Antes de começar,
confirme que a suíte de conformidade da v1 está verde.

## Pré-condições

- [ ] `make check` verde na `main`.
- [ ] Gramática OO documentada e aprovada (`docs: 026`).
- [ ] Ticket de OO no board, com arquivos e paralelismo declarados.

## Ordem incremental (não pule etapas)

1. Léxico/parser de `class`, `extends`, membros, `new`, `this`, `return`.
2. AST e tabela de símbolos com hierarquia, campos e assinaturas.
3. `new`, acesso a campo, `this`, chamada de método.
4. Checagem de tipos OO e override.
5. Despacho dinâmico e demos de polimorfismo.

## Regras

- Herança simples; sem construtor, `null`, abstract, interface, overload.
- Campos: sem esconder campo do ancestral; sem colisão com local/parâmetro.
- Override: mesmo nome e lista de tipos de parâmetros; retorno igual ou
  subtipo.
- `new C()` inicializa todos os campos com `undef`.
- O tipo estático decide o que pode ser acessado; o dinâmico decide o método.
- Toda nova regra tem teste feliz e teste de erro `E31xx`/`E41xx`.
- Rode também os programas v1: OO não pode regredir o núcleo.

## Formato de saída

1. Incremento entregue e produções afetadas.
2. Programa `.clite` de demonstração + saída esperada.
3. Comando de teste e resultado.
4. Regras de tipo novas e onde foram documentadas.
