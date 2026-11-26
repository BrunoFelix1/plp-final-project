# Implementation Plan: CLI `tokens` e testes golden

**Branch**: `feat/008-cli-tokens-e-testes-golden` · **Date**: 2026-11-25
**Spec**: [spec.md](./spec.md) · **Ticket**: #8

<!-- REGRA DO PROJETO: meta de 70 linhas; sem repetir a spec. Decisão nova vira D-NN em docs/05. -->

## Summary

`tokens` lê o arquivo, chama um novo `tokenize(source)` (varre até o `EOF` sem
incluí-lo), formata cada token e imprime só no fim. Assim um erro léxico não deixa saída
parcial: o `LexicalError` vira uma linha em stderr e exit `1`. Os goldens vivem em
`tests/golden/lexer/` e usam como entrada `examples/lexico/`. Sem mudar a gramática.

## Technical Context

| Item | Valor |
| --- | --- |
| Python | 3.12+; dependências de runtime: nenhuma |
| Testes | pytest (`capsys`) |
| Qualidade | `ruff`, `mypy --strict` em `src/`, `tools.magic_numbers` |
| Módulos afetados | `lexer/lexer.py`, `cli.py`, `__main__.py`, `docs/03` §6 |
| Novos | `examples/lexico/*.clite`, `tests/golden/lexer/*`, `tests/unit/test_cli_tokens.py` |

## Constitution Check

| Princípio | Como este plano cumpre |
| --- | --- |
| I. Aprendizado | A CLI mostra o léxico sem parser; o golden documenta o contrato |
| II. Fidelidade à gramática | `docs/01` não muda; `docs/03` §6 ganha o formato de saída |
| III. Fatia pequena | Um helper no lexer, um comando na CLI e os dados de teste |
| IV. Teste primeiro | `test_cli_tokens.py` falha antes: formato, erro, vazio, goldens |
| V. Python padrão | Nenhuma dependência |
| VI. Escopo | Sem parser, AST nem `--max-errors` |

Violações: nenhuma. Desvio de processo: a branch nasce de `feat/007` porque o #46 ainda
não entrou na `main`.

## Project Structure

```text
src/clite/lexer/lexer.py            # + tokenize(source) -> list[Token]
src/clite/cli.py                    # + format_token, run_tokens; executar_comando(args)
src/clite/__main__.py               # passa args ao despacho
examples/lexico/*.clite             # basico, operadores, literais, erro_caractere, erro_e1002
tests/golden/lexer/*.tokens|.err    # saída esperada (stdout ou stderr)
tests/unit/test_cli_tokens.py       # formato, exit codes e goldens; test_cli.py usa `parse`
```

**Structure Decision**: entradas em `examples/lexico/` (já citado em `examples/README.md`);
só a saída esperada fica em `tests/golden/`, sem duplicar o `.clite`.

## Phase 0: Research

| Pergunta | Resposta | Fonte |
| --- | --- | --- |
| Imprimir o `EOF`? | Não: é marcador interno do scanner | Spec §Assumptions |
| Saída parcial antes do erro? | Não: acumula e imprime no fim (tudo ou nada) | D-12 |
| Formato da linha? | `f"{tag.name} {lexeme} {line}:{column}"` | `docs/03` §6 |
| Códigos de saída? | `0` ok, `1` erro de programa, `2` uso | `docs/03` §6 |
| Arquivo ilegível? | `OSError`/`UnicodeDecodeError` → mensagem e `2` | `docs/03` §6 |
| Raiz do repo nos testes? | `Path(__file__).resolve().parents[REPO_ROOT_DEPTH]` | AGENTS §5.6 |

## Phase 1: Design

| Artefato | Conteúdo |
| --- | --- |
| Contratos | `tokenize(str) -> list[Token]`; `format_token(Token) -> str`; `run_tokens(Path) -> int`; `executar_comando(Namespace) -> int` |
| Erros | sem código novo: `E1001`/`E1002` do #6/#7 |
| Testes | 5 goldens, linha única, vazio, erro com stdout vazio, `parse` ainda `E9000` |
| Quickstart | [`quickstart.md`](./quickstart.md) |

### Ordem do TDD

1. Teste da linha `TAG lexema linha:coluna` e do arquivo vazio.
2. `tokenize` + `format_token` + `run_tokens`; despacho por `args.comando`.
3. Teste de erro: stderr com uma linha, stdout vazio, exit `1`.
4. `examples/lexico/*` e goldens, com o teste parametrizado.
5. Ajustar `test_cli.py`, `docs/03` §6 e rodar o gate.

## Complexity Tracking

| Violação | Por que é necessária | Alternativa descartada |
| --- | --- | --- |
| nenhuma | — | — |
