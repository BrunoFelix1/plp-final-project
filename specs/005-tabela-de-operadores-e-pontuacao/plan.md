# Implementation Plan: Tabela de operadores e pontuação

**Branch**: `feat/007-tabela-de-operadores-e-pontuacao` · **Date**: 2026-11-25
**Spec**: [spec.md](./spec.md) · **Ticket**: #7

<!-- REGRA DO PROJETO: meta de 70 linhas; sem repetir a spec. Decisão nova vira D-NN em docs/05. -->

## Summary

Um dicionário `OPERATORS` (lexema → `Tag`) é a única fonte dos 23 lexemas. O scanner
do #6 lê até dois caracteres, tenta o par e depois o caractere sozinho (maior
casamento). `&` e `|` são prefixo de `&&`/`||` mas não existem sozinhos: o
scanner os detecta **a partir da tabela** e levanta `E1002`. Não altera a gramática.

## Technical Context

| Item | Valor |
| --- | --- |
| Python | 3.12+ |
| Dependências de runtime | nenhuma |
| Testes | pytest |
| Qualidade | `ruff`, `mypy --strict` em `src/`, `tools.magic_numbers` |
| Módulos afetados | `lexer/operators.py` (novo), `lexer/lexer.py`, `test_operators.py` (novo), `test_scanner.py`, `docs/03`, `docs/06` |
| Documento da gramática | `docs/01` §4.2 (já cobre; sem mudança) |

## Constitution Check

| Princípio | Como este plano cumpre |
| --- | --- |
| I. Aprendizado | A tabela torna visível o contrato léxico; o `E1002` nasce do maior casamento |
| II. Fidelidade à gramática | Segue `docs/01` §4.2–4.3; `E1002` é registrado em docs/03 e docs/06 |
| III. Fatia pequena | Um arquivo novo de código, um de teste e dois ajustes cirúrgicos |
| IV. Teste primeiro | `test_operators.py` falha antes: 23 lexemas, compostos, `&`/`|`, posição |
| V. Python padrão | Nenhuma dependência |
| VI. Escopo | Sem precedência (#10), CLI (#8) nem recuperação de erro (#19) |

Violações: nenhuma. O ticket não lista `lexer.py` em "Arquivos que toca"; ajustar a issue.

## Project Structure

```text
src/clite/lexer/operators.py          # OPERATORS (lexema -> Tag); novo
src/clite/lexer/lexer.py              # _scan_symbol + LexicalError com código
tests/unit/lexer/test_operators.py    # novo
tests/unit/lexer/test_scanner.py      # test_unknown_character_fails: só "@"
```

**Structure Decision**: a tabela fica fora do `lexer.py` (como o ticket manda) e o
scanner só a consulta. `errors.py` continua stub: o #19 unifica os erros.

## Phase 0: Research

| Pergunta | Resposta | Fonte |
| --- | --- | --- |
| Como achar `&`/`\|` isolados sem repetir lexemas? | prefixos de lexemas de 2 chars que não são lexema sozinhos | FR-003 |
| Comprimento máximo do lexema? | derivado da tabela (`max(len)`), sem literal `2` | AGENTS §5.6 |
| `//` vs `/`? | `_skip_trivia` consome `//` antes; `/` chega ao scanner como divisão | `docs/06` §1 |
| `-1`? | `-` e `1`: não há literal negativo; o parser decide | `docs/01` §5 |
| Onde mora `E1002`? | constante em `lexer.py`; o #19 move para `errors.py` | D-12 |
| Posição do token de 2 chars? | do primeiro caractere | `docs/01` §4.3.6 |

## Phase 1: Design

| Artefato | Conteúdo |
| --- | --- |
| Contratos | `OPERATORS: dict[str, Tag]`; `LexicalError(line, column, message, code=ERROR_CODE)` |
| Dados | [`data-model.md`](./data-model.md): os 23 lexemas e suas tags |
| Erros | `E1002` para `&`/`\|` isolado; `E1001` para o resto (inclui `@`) |
| Quickstart | [`quickstart.md`](./quickstart.md) |

### Ordem do TDD

1. Teste dos 23 lexemas (falha: `;`, `+` ainda dão `E1001`).
2. Tabela + `_scan_symbol` com o caractere único.
3. Compostos: `<=`, `>=`, `==`, `!=`, `&&`, `||` e `a < = b`.
4. `E1002` (`a & b`, `&&&`) e `E1001` para `@`.
5. Ajustar o teste do #6, docs/03 e docs/06; rodar `tools.magic_numbers`.

## Complexity Tracking

| Violação | Por que é necessária | Alternativa descartada |
| --- | --- | --- |
| nenhuma | — | — |
