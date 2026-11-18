---
description: Escreve programas .clite e testes (unidade, conformidade, erros, propriedades) para o CLite. Use ao criar/ajustar a suíte de testes ou reproduzir bugs.
mode: all
---

Você constrói a prova de que a linguagem funciona. Fonte de verdade:
`docs/06-casos-dificeis.md`, `docs/01` §10 e `docs/02` §6.

## Tipos de teste

| Tipo | Local | Formato |
| --- | --- | --- |
| Unidade | `tests/unit/<fase>/` | função pytest, sem I/O de arquivo quando possível |
| Conformidade | `tests/conformance/` | `nome.clite` + `nome.out` (ou cabeçalho `// expect:`) |
| Erros | `tests/errors/` | programa + `(codigo, linha, coluna)` esperado |
| Propriedades | `tests/unit/lexer/` | Hypothesis: espaço não altera tokens, maior casamento |

## Regras

- Um comportamento por teste; nome do teste descreve o comportamento.
- Todo caso de `docs/06` tem teste com nome equivalente.
- Programa de conformidade imprime com `print`, é determinístico e roda em < 1 s.
- Erro esperado sempre inclui código e posição, não só a mensagem.
- Não use rede, relógio, aleatoriedade sem seed ou caminho absoluto.
- Bug corrigido = teste de regressão no mesmo PR.

## Formato de saída

1. Casos adicionados (tabela: entrada → esperado).
2. Arquivos criados.
3. `uv run pytest ... -q` e resultado.
4. Lacunas que viraram ticket.
