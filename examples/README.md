# Programas de exemplo

Programas `.clite` usados para demonstrar e testar a linguagem. Cada pasta
corresponde a um marco:

| Pasta | Conteúdo | Ticket |
| --- | --- | --- |
| `lexico/` | entradas para `clite tokens` (inclui erros léxicos) | `feat: 008` |
| `nucleo/` | programas da v1: declarações, if, while, arrays, casts | `feat: 017` |
| `oo/` | herança, override e polimorfismo | `feat: 032` |

## Convenções

- Todo programa começa com `int main() { ... }`.
- A saída esperada dos programas de conformidade fica em
  `tests/conformance/<nome>.out`.
- Programa de demonstração deve rodar em menos de 1 s.
- Comentários explicam **o conceito** demonstrado, não a sintaxe óbvia.
- Nada de `while (true)` sem condição de parada; o harness tem timeout de 5 s.

## Executar

```bash
uv run clite run examples/nucleo/media.clite
uv run clite tokens examples/lexico/basico.clite
uv run clite parse examples/nucleo/media.clite
```
