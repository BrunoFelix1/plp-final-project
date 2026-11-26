# Convergência: Tabela de operadores e pontuação

**Resultado**: convergido · 2026-11-25 · ticket `feat: 007` (#7)

## Verificação

| Item | Evidência | Resultado |
| --- | --- | --- |
| FR-001 / SC-001 | `test_each_lexeme_is_a_single_token`: 23 casos, tag + lexema + posição | atendido |
| FR-002 | `test_composite_operator_is_one_token` (6 compostos), `a < = b`, `===` | atendido |
| FR-003 | `OPERATORS` em `operators.py`; `test_table_has_exactly_the_documented_lexemes`; grep em `lexer.py` sem lexema de operador | atendido |
| FR-004 / SC-002 | `E1002` em `a & b`, `a \| b`, `&`, `\|` e na 3ª coluna de `&&&`/`\|\|\|`; formato D-12 | atendido |
| FR-005 | `@`, `#` e `.` seguem `E1001` (linha 1, coluna 1) | atendido |
| FR-006 | `test_unknown_character_fails` reduzido a `@` | atendido |
| FR-007 | `docs/06` (Caractere inválido) e `docs/03` §5 citam `E1002` | atendido |
| SC-003 | `ruff check`, `mypy src`, `pytest` (109 passaram), `tools.magic_numbers` — Python 3.12 em Docker | passou |
| Plan: derivar `ISOLATED_PREFIXES` e `MAX_LEXEME_LENGTH` da tabela | `operators.py`; hoje `{'&': '&&', '|': '||'}` e 2 | atendido |
| Constituição T0 | `git diff --check` limpo; `lexer.py` +22/−6, `test_scanner.py` +1/−1 | atendida |
| `docs/01` | não alterado; §4.2 já lista os 23 lexemas | conforme o plano |

## Pendências humanas (resolvidas)

- CHK013: Bruno aceitou `E1002` sem D-NN em `docs/05`.
- CHK014: issue #7 atualizada (`lexer.py`, `test_scanner.py`, `docs/03`, `docs/06`).
- Não há task de convergência a acrescentar; `tasks.md` mantém T001–T013 concluídas.

## Observações

- `ruff format --check .` na raiz falha em `.specify/memory/constitution.md` (anterior; fora do gate).
- A decisão `E1002` fica em `lexer.py`; o #19 a move para `errors.py`.

## Próximo passo

Rodar `make check` e conferir a consistência da branch; depois, commits e PR com `Closes #7`.
