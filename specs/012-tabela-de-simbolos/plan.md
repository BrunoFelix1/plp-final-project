# Implementation Plan: Tabela de símbolos e resolução de nomes (ticket 012)

**Branch**: `feat/012-tabela-de-simbolos-e-resolucao-de-nomes` · **Date**: 2026-11-27 · **Spec**: [spec.md](./spec.md)

## Summary

Implementar a tabela de símbolos da fase semântica: registro de declarações
(variáveis e arrays), busca por nome, detecção de duplicidade (`E3002`) e de nome
inexistente (`E3001`), com escopo único (D-06) e exposição da lista de
declarações para o checker (#13/#14). Abordagem: mapa plano nome → nó de
declaração da AST (API AST-cêntrica), com erro semântico local no padrão da
`LexicalError` da #7.

## Technical Context

| Item | Valor |
| --- | --- |
| Python | 3.12+ |
| Dependências de runtime | nenhuma |
| Testes | pytest |
| Qualidade | ruff, mypy --strict em `src/` |
| Módulos afetados | `src/clite/symbols.py` (único módulo de produção) |
| Documento da gramática | `docs/01` — intocado (sem mudança de gramática) |

## Constitution Check

| Princípio | Como este plano cumpre |
| --- | --- |
| I. Aprendizado | Conceito: tabela de símbolos e resolução de nomes (Tucker §4.3–4.5, Apêndice A.3) |
| II. Fidelidade à gramática | Gramática não muda; comportamento segue docs/01 §6, docs/06 §3 e D-06 |
| III. Fatia pequena | Ticket #12; 1 arquivo de produção + 1 de teste; branch stacked na `feat/009` |
| IV. Teste primeiro | `tests/unit/semantic/test_symbols.py` cobre os 4 itens do "Pronto quando" |
| V. Python padrão | Só biblioteca padrão: `dict`, exceção e constantes nomeadas |
| VI. Escopo | Fora: escopo de bloco, v2 (classes/métodos), `types.py` e hierarquia global de erros (#19) |

Violações: nenhuma. O erro local (em vez de semear `errors.py`) segue o
precedente aceito da #7; a #19 (M3) unificará a hierarquia.

## Project Structure

```text
src/clite/symbols.py                  # SemanticError + SymbolTable
tests/unit/semantic/test_symbols.py   # unidade: declarar, buscar, duplicar, expor
```

**Structure Decision**: `symbols.py` já existe como esqueleto do pacote
(docs/03 §3, mapa do Apêndice A) e é a fronteira da fase semântica; o teste
acompanha a organização por fase em `tests/unit/semantic/`. Nenhum outro módulo
é tocado.

## Phase 0: Research

| Pergunta | Resposta | Fonte |
| --- | --- | --- |
| CLite tem escopo único? | Sim, implícito: bloco sem declarações + mapa de tipos único + estado plano | Livro §2.3, §6.3, Regra 8.1; D-06 |
| Padrão de erro antes da #19 | Exceção local por fase: code/line/column + mensagem formatada no construtor | `LexicalError` (lexer.py:29), D-12, docs/03 §5 |
| O que a tabela guarda? | O próprio nó de declaração da AST (fonte única de nome/tipo/posição) | Decisão aprovada no plano; docs/03 §4.3 |
| Códigos E3xxx desta fatia | `E3001` não declarada; `E3002` duplicada | docs/06 §3; issue #12 |

## Phase 1: Design

| Artefato | Conteúdo |
| --- | --- |
| Contratos | [contracts/symbols-api.md](./contracts/symbols-api.md): `SemanticError` e `SymbolTable.declare/lookup/declarations` |
| Erros | `E3001` (posição da referência), `E3002` (posição da 2ª declaração) |
| Testes | Felizes: declare+lookup (var e array), lista em ordem. Erros: duplicado simples/array/misto, inexistente, bloco (D-06), tabela vazia |

## Complexity Tracking

| Violação | Por que é necessária | Alternativa descartada |
| --- | --- | --- |
| [nenhuma] | — | — |
