# Implementation Plan: Lexer de identificadores, literais e posição

**Branch**: `feat/006-lexer-identificadores-literais-e-posicao` · **Date**: 2026-11-24
**Spec**: [spec.md](./spec.md) · **Ticket**: #6

<!-- REGRA DO PROJETO: meta de 70 linhas; sem repetir a spec. Decisão nova vira D-NN em docs/05. -->

## Summary

Varredura de uma passada sobre `str`: um autômato que acumula o lexema e o
classifica ao encontrar o primeiro caractere que não o continua. Reaproveita
`Token`, `Tag`, `KEYWORDS` e `is_reserved` do #5; não altera a gramática de `docs/01`.

## Technical Context

| Item | Valor |
| --- | --- |
| Python | 3.12+ |
| Dependências de runtime | nenhuma (só `dataclasses` e `enum` já usados) |
| Testes | pytest |
| Qualidade | `ruff`, `mypy --strict` em `src/`, `tools.magic_numbers` |
| Módulos afetados | `src/clite/lexer/lexer.py` (novo), `tests/unit/lexer/test_scanner.py` (novo) |
| Documento da gramática | `docs/01` §4.1–4.4 (já cobre; sem mudança) |

## Constitution Check

| Princípio | Como este plano cumpre |
| --- | --- |
| I. Aprendizado | Expõe o autômato de estados e o maior casamento de forma explícita no código |
| II. Fidelidade à gramática | Segue `docs/01` §4; nenhuma regra nova |
| III. Fatia pequena | Dois arquivos; operadores (#7) e erros (#19) ficam de fora |
| IV. Teste primeiro | `test_scanner.py` cobre cada literal, erro e posição antes do código |
| V. Python padrão | Nenhuma dependência; sem biblioteca de lexer |
| VI. Escopo | Só o subconjunto do ticket #6 |

Violações: nenhuma.

## Project Structure

```text
src/clite/lexer/lexer.py          # Lexer + LexicalError
tests/unit/lexer/test_scanner.py  # casos felizes, erros e posição
```

**Structure Decision**: só o par código/teste do ticket. `tags.py`, `tokens.py`,
`keywords.py` e `errors.py` não mudam; `errors.py` pertence ao #19.

## Phase 0: Research

| Pergunta | Resposta | Fonte |
| --- | --- | --- |
| Onde vive o erro `E1001`? | `LexicalError` em `lexer.py`; o #19 o unifica em `errors.py` | D-12, ticket #19 |
| Formato da mensagem? | `erro E1001 (linha L, coluna C): texto`, sem stack trace | D-12 |
| Emitir `EOF`? | Sim: `Token(Tag.EOF, "", linha, coluna)` ao esgotar o fonte | `docs/03` §4.1; tag já existe |
| Coluna após nova linha? | Volta a 1; linha e coluna são 1-based | `docs/01` §4.3.6 |
| `//` dentro de `'/'`? | O literal de caractere é consumido antes; não vira comentário | `docs/01` §4.3.5 |
| `1.2.3`? | `FLOAT_LITERAL "1.2"`, depois `E1001` no segundo ponto | `docs/06` §1 |
| Números mágicos? | Constantes de caractere no topo; `0`/`1` só como índice/passo | AGENTS §5.6 |

## Phase 1: Design

| Artefato | Conteúdo |
| --- | --- |
| Contratos | [`contracts/lexer.md`](./contracts/lexer.md), [`data-model.md`](./data-model.md) |
| Erros | `E1001` para `5.`, `.5`, `''`, `'ab'`, caractere desconhecido e operador/pontuação até o #7 |
| Testes | 8 casos felizes, 5 erros, 3 bordas; posição verificada em cada erro |
| Quickstart | [`quickstart.md`](./quickstart.md) |

### Ordem do TDD

1. `IDENT` e maior casamento (`whilea`).
2. Literais: inteiro, float, booleano, char.
3. Palavra reservada antes de identificador.
4. Espaço/comentário e contagem de linha.
5. `EOF`.
6. Erros `E1001` com linha e coluna.

## Complexity Tracking

| Violação | Por que é necessária | Alternativa descartada |
| --- | --- | --- |
| Nenhuma | — | — |
