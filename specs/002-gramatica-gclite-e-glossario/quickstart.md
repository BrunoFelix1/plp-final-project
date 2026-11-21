# Quickstart de validação

## Pré-requisitos

- Estar na branch `docs/002-gramatica-gclite-e-glossario`.
- Ter o ambiente do projeto sincronizado com `uv sync`.

## Verificação documental

1. Abra `docs/README.md` e siga os links para `01`, `02`, `03`, `04`, `05` e
   `06`; cada destino deve existir.
2. Em `docs/01-linguagem-clite.md`, confira a EBNF, a explicação de `{ }` e
   `[ ]`, `Booleano`, a AST com conversão, as tabelas de tokens/precedência e
   as seis entradas do glossário.
3. Em `docs/06-casos-dificeis.md`, confira as quatro categorias e os casos
   `whilea`, `<=`, float malformado, `else` pendente e comparação encadeada;
   confirme que exemplos OO estão identificados como futuros.
4. Execute `git diff --check` para detectar problemas de whitespace.

## Verificação do projeto

```bash
make check
```

Resultado esperado: documentação sem links quebrados, checklist do ticket sem
pendências e os gates existentes de lint, tipos e testes verdes. O modelo dos
conceitos está em [data-model.md](data-model.md); não há contratos externos.
