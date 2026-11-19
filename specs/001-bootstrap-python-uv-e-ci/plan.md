# Implementation Plan: Bootstrap Python, uv e CI

**Branch**: `chore/001-bootstrap-python-uv-e-ci` · **Date**: 2026-11-18 ·
**Spec**: [spec.md](spec.md)

<!--
  REGRA DO PROJETO: meta de 70 linhas; se passar de 100, seja mais conciso. Sem repetir a spec.
  Tabelas primeiro e uma breve explicação do conceito.
  Toda decisão nova vira D-NN em docs/05-decisoes.md.
-->

## Summary

Auditar e, somente se necessário, completar a fundação já versionada: manifesto
uv, Makefile, pre-commit, workflow e teste de fumaça. A validação deve preservar
o código de linguagem intocado e confirmar que local e CI usam o mesmo contrato.

## Technical Context

| Item | Valor |
| --- | --- |
| Python | 3.12+ |
| Dependências de runtime | nenhuma |
| Testes | pytest (+ hypothesis quando fizer sentido) |
| Qualidade | ruff, mypy --strict em `src/` |
| Arquivos | `pyproject.toml`, `uv.lock`, `Makefile`, `.pre-commit-config.yaml` |
| CI/teste | `.github/workflows/ci.yml`, `tests/test_smoke.py` |
| Runtime | pacote raiz `src/clite/__init__.py`; nenhuma dependência nova |

## Constitution Check

| Princípio | Como este plano cumpre |
| --- | --- |
| I. Aprendizado | ambiente reproduzível e automação de qualidade |
| II. Fidelidade à gramática | sem mudança de gramática |
| III. Fatia pequena | apenas arquivos declarados no ticket #1 |
| IV. Teste primeiro | importar `clite` e rodar `make check` |
| V. Python padrão | dependências somente no grupo `dev` |
| VI. Escopo | sem lexer, parser, semântica ou interpretador |

Violações: [nenhuma | D-NN com justificativa].

## Project Structure

```text
pyproject.toml · uv.lock · Makefile
.pre-commit-config.yaml · .github/workflows/ci.yml
tests/test_smoke.py · src/clite/__init__.py
```

**Structure Decision**: a configuração fica na raiz; o teste importa o pacote
instalável, evitando acoplar o bootstrap a uma fase futura da linguagem.

## Phase 0: Research

| Pergunta | Resposta | Fonte |
| --- | --- | --- |
| Como reproduzir dependências? | `uv.lock` + `uv sync --frozen` no CI. | ticket #1 |
| Qual gate local? | `make check`: ruff, mypy e pytest. | `AGENTS.md` §3 |
| Qual entrada do CI? | push/PR para `main` e execução manual. | `.github/workflows/ci.yml` |

## Phase 1: Design

| Artefato | Conteúdo |
| --- | --- |
| Contratos | comandos `uv sync`, `make check` e workflow de qualidade |
| Erros | nenhum código E1xxx–E4xxx; ferramenta deve retornar não-zero |
| Testes | smoke import; lint, tipos e suíte pytest |

## Complexity Tracking

| Violação | Por que é necessária | Alternativa descartada |
| --- | --- | --- |
| [nenhuma] | — | — |
