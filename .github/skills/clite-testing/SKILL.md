---
name: Testes CLite
description: Escrever e executar testes do interpretador CLite — unidade, conformidade com programas .clite, casos de erro e propriedades. Use ao implementar ticket ou revisar PR.
---

# Testes CLite

## Comandos

```bash
uv run pytest -q                      # tudo
uv run pytest tests/unit -q           # unidade
uv run pytest -m conformance -q       # programas .clite
uv run pytest --cov --cov-report=term-missing
make check                            # lint + tipos + testes (CI)
```

## Estrutura

```text
tests/
├── unit/
│   ├── lexer/
│   ├── parser/
│   ├── semantic/
│   └── interpreter/
├── conformance/
│   ├── caso.clite
│   └── caso.out          # saída esperada, linha a linha
└── errors/
    └── caso.clite        # + tupla (codigo, linha, coluna) no teste
```

## Convenções

- Nome do teste descreve comportamento: `test_float_exige_digito_dos_dois_lados`.
- Um comportamento por teste; sem `assert` múltiplo não relacionado.
- Conformidade: determinístico, sem I/O além de `print`, < 1 s, timeout 5 s.
- Erro: valide código `E....`, linha e coluna — não só o texto.
- Propriedades úteis: espaço em branco não muda os tokens; maior casamento;
  lexer idempotente ao reinserir espaços.
- Todo caso de `docs/06-casos-dificeis.md` tem teste equivalente.
- Bug corrigido entra com teste de regressão no mesmo PR.

## Fluxo TDD

1. Escreva o teste e rode: deve falhar pelo motivo certo.
2. Implemente o mínimo.
3. Rode o teste, depois `make check`.
4. Refatore sem mudar comportamento.
