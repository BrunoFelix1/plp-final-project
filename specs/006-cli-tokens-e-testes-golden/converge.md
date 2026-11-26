# Convergência: CLI `tokens` e testes golden

**Resultado**: convergido · 2026-11-25 · ticket `feat: 008` (#8)

## Verificação

| Item | Evidência | Resultado |
| --- | --- | --- |
| FR-001 / SC-001 | `test_one_line_per_token`: `INT int 1:1`, `IDENT x 1:5`, `SEMICOLON ; 1:6`; CLI sobre `basico.clite` | atendido |
| FR-002 | `test_empty_file_prints_nothing`, `test_eof_is_not_printed` | atendido |
| FR-003 | `test_lexical_error_is_one_line_on_stderr` (`E1001` e `E1002`): exit `1`, stdout vazio, 1 linha | atendido |
| FR-004 | `test_unreadable_file_is_a_usage_error` e `test_arquivo_inexistente`: exit `2` | atendido |
| FR-005 / SC-002 | 5 goldens (3 `.tokens`, 2 `.err`); alterar `2:1`→`2:2` faz `test_token_golden[basico]` falhar | atendido |
| FR-006 | `test_other_commands_are_still_not_implemented` e `test_comando_nao_implementado` (`parse`) | atendido |
| FR-007 | `docs/03` §6: formato de saída, `EOF` omitido, exit codes | atendido |
| SC-003 | `ruff check`, `mypy src`, `pytest` (126 passaram), `tools.magic_numbers` — Python 3.12 em Docker | passou |
| Revisão manual dos goldens | colunas conferidas contra o fonte e `docs/01` §4.2; os 23 lexemas aparecem em `operadores` | feito |
| Constituição T0 | `git diff --check` limpo; `cli.py` e `__main__.py` só com linhas necessárias | atendida |
| `docs/01` | não alterado | conforme o plano |

## Pendências humanas

- CHK013: aceitar `EOF` não impresso e o erro "tudo ou nada" (decisões desta spec).
- CHK014: aceitar a branch empilhada em `feat/007` até o #46 entrar na `main`.
- Não há task de convergência a acrescentar; `tasks.md` mantém T001–T014 concluídas.

## Observações

- `ruff format --check .` na raiz falha em `.specify/memory/constitution.md` (anterior; fora do gate).
- Os goldens são regenerados à mão (`clite tokens … > arquivo`); automatizar fica para depois.

## Próximo passo

Rodar `make check`, conferir a consistência da branch e abrir o PR com `Closes #8`.
