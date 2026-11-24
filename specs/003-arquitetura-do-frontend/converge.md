# Convergência: Arquitetura do front-end

**Resultado**: convergido · 2026-11-21 · ticket `docs: 003` (#3)

## Verificação

| Item | Evidência | Resultado |
| --- | --- | --- |
| FR-001 / SC-001 | diagrama §1 (linhas 25–54) cita `lexer/`, `parser/`, `ast/`, `semantic/`, `interpreter/`, `symbols.py`, `types.py`, `values.py`, `errors.py`, `cli.py` | 10/10 |
| FR-001 (posição) | pacote ao lado da caixa; apoio como seta lateral; `cli.py` no topo; `errors.py` em linha própria | atendido |
| FR-001a | caixa `Semantic (TypeChecker)` | atendido |
| FR-002 / SC-002 | §2 cita D-02 e o modelo orientado a objeto × orientado a fase; cabeçalho usa `symbols` | atendido |
| FR-003 / US2 | §§4.3–4.4 marcam (v2) globais de classe, retorno, classe corrente, heap, `ReturnSignal`; v1 = escopo único (D-06) | atendido |
| FR-004 | §5 coerente com D-12; §6 CLI completa; sem mudança | atendido |
| FR-005 | `docs/README.md` e `README.md` apontam para `docs/03-arquitetura-frontend.md` (nome inalterado) | atendido |
| SC-004 | `make check` = `ruff check` + `mypy src` + `pytest` | passou |
| Constituição T0 | só `docs/03` alterado (+29/−19); `git diff --check` limpo | atendida |

## Observação (fora do escopo)

`uv run ruff format --check .` falha em `.specify/memory/constitution.md`, que é
anterior a este ticket e já registrado em `specs/001-.../converge.md`. Por isso o
`make check` e o CI não incluem esse comando. O `quickstart.md` §4 deste ticket
o lista; vale como referência, mas o gate oficial é o `make check`.

## Comandos finais

```text
uv run ruff check .
uv run mypy src
uv run pytest -q
git diff --check
```

Todos terminaram com código 0. Nenhuma task de convergência foi adicionada.

## Fora de escopo e referências

- Implementar fases; mudar D-02; corrigir `src/clite/errors.py`.
- Referências: `spec.md`, `plan.md`, `tasks.md`, `research.md`; Compiladores §1.2 e
  Apêndice A; Tucker e Noonan §2.4 e §6.1.
