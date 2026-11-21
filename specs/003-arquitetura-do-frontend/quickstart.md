# Quickstart: validar o ticket 003

## 1. Módulos citados no diagrama (SC-001)

```bash
ls src/clite
for m in lexer/ parser/ ast/ semantic/ interpreter/ errors.py types.py symbols.py \
         values.py cli.py; do
  grep -qF "$m" docs/03-arquitetura-frontend.md && echo "ok  $m" || echo "FALTA $m"
done
```

Esperado: 10 linhas `ok`. Confira a olho que cada um aparece **no diagrama da §1**,
não só em outra seção.

## 2. Referências cruzadas (SC-002)

```bash
grep -n "D-0[0-9]" docs/03-arquitetura-frontend.md   # visitantes → D-02
grep -n "symbol" docs/03-arquitetura-frontend.md     # só "symbols"
```

## 3. v1 × v2 (US2)

Leia §§4.3–4.4: `this`, classe corrente, heap, frames e `ReturnSignal` marcados como (v2).

## 4. Nada quebrou (SC-004)

```bash
uv run ruff check . ; uv run ruff format --check . ; uv run mypy src ; uv run pytest
```

## 5. Revisão por pares (SC-003)

Um colega confere os 3 itens "Pronto quando" do ticket #3.
