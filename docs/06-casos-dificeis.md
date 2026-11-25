# Casos difíceis e como tratá-los

> Lista viva. Cada linha vira um teste (`tests/unit` ou `tests/errors`) e, quando
> necessário, um ticket. Se você encontrou um caso novo, adicione antes de
> corrigir.
>
> As seções 1–4 descrevem o núcleo v1. Casos de classes e objetos ficam
> identificados separadamente como futuros e pertencem ao desenho de `docs/02`.

## 1. Léxico

| Caso | Entrada | Comportamento esperado |
| --- | --- | --- |
| Maior casamento | `whilea` | um identificador, não `while` + `a` |
| Operador composto | `a<=b` | tokens `a`, `<=`, `b` |
| Operador quebrado | `a < = b` | `<` e `=`; erro sintático em `=` |
| Float malformado | `5.` / `.5` | erro léxico `E1001` |
| Float com dois pontos | `1.2.3` | `1.2` seguido de erro em `.` |
| Char vazio | `''` | erro léxico `E1001` |
| Char longo | `'ab'` | erro léxico `E1001` |
| Char imprimível | `' '` | válido (espaço é imprimível) |
| Comentário | `// x = 1;` | ignorado até a nova linha |
| Comentário no fim do arquivo | `int main() { } // fim` | válido |
| Barra ambígua | `a / b` vs `a // b` | divisão vs comentário |
| Caractere inválido | `@`, `#`, `&` sozinho | `@` e `#`: `E1001`; `&` ou `\|` sozinho: `E1002`; com linha/coluna |
| Palavra reservada | `int while;` | erro léxico ou sintático claro |
| Palavra da v2 na v1 | `int class;` | erro: `class` é reservada |

## 2. Sintático

| Caso | Entrada | Comportamento esperado |
| --- | --- | --- |
| `else` pendente | `if (a) if (b) x = 1; else x = 2;` | `else` pertence ao `if` interno |
| Bloco sem `;` | `{ x = 1; }` | válido: bloco não leva `;` |
| `;` solto | `;` | comando `Skip`, válido |
| Comparação encadeada | `a < b < c` | erro: relacionais não associativos |
| Igualdade encadeada | `a == b == c` | erro |
| Atribuição como expressão | `x = y = 1;` | erro sintático |
| Falta de `;` | `x = 1` | erro no token seguinte |
| Declaração sem tipo | `x;` | erro: esperava tipo |
| Array com tamanho variável | `int v[n];` | erro: tamanho é literal |
| Array sem tamanho | `int v[];` | erro |
| Vírgula em declaração | `int a, b;` | válido |
| Múltiplos arrays | `int a[2], b;` | válido |
| `main` errado | `void main()` | erro: `main` é `int` |
| Código após `}` | `int main() {} x = 1;` | erro: fim inesperado |

## 3. Semântico / tipos

| Caso | Entrada | Comportamento esperado |
| --- | --- | --- |
| Não declarada | `x = 1;` sem declarar | `E3001` |
| Duplicada | `int x; int x;` | `E3002` |
| `float` recebe `int` | `float x; x = 1;` | `E3003` (use `float(1)`) |
| `int` recebe `float` | `int x; x = 2.5;` | `E3003` |
| `int` recebe `char` | `char c; int x; x = c;` | válido |
| `char` recebe `int` | `char c; c = 65;` | `E3003` (use `char(65)`) |
| `bool` em aritmética | `true + 1` | `E3004` |
| `int` em condição | `if (1) …` | `E3005` |
| Tipos mistos | `1 + 2.0` | `E3004` (use `float(1) + 2.0`) |
| `%` em float | `2.0 % 1.0` | `E3004` |
| `bool()` | `bool(1)` | `E3007` |
| `!` em int | `!1` | `E3006` |
| `-` em bool | `-true` | `E3006` |
| Índice não inteiro | `v[1.0]` | `E3008` |
| `undef` | `int x; x = x + 1;` | `E4001` na execução |

## 4. Execução

| Caso | Entrada | Comportamento esperado |
| --- | --- | --- |
| Divisão por zero | `1 / 0` | `E4002` |
| Resto por zero | `1 % 0` | `E4002` |
| Índice negativo | `v[-1]` | `E4003` (expressão válida, execução falha) |
| Índice no limite | `v[10]` em `int v[10]` | `E4003` |
| `while` infinito | `while (true) ;` | não trava os testes: use timeout no harness |
| Truncamento | `7 / 2` | `3` |
| Divisão negativa | `-7 / 2` | `-3` (trunca em direção a zero) |
| Curto-circuito | `false && (1 / 0 == 0)` | `false`, sem erro |
| Curto-circuito `\|\|` | `true \|\| (1 / 0 == 0)` | `true`, sem erro |

### 4.1 Casos OO (futuros)

Estes casos não fazem parte da gramática v1; documentam comportamentos previstos
para a extensão descrita em `docs/02`.

| Caso | Entrada | Comportamento esperado |
| --- | --- | --- |
| Aliasing de objeto | `a = c; a.pernas = 3;` | muda também `c.pernas` |
| Campo `undef` | `print(c.pernas);` após `new` | `E4102` |
| Método sem `return` | caminho que cai no fim | `E4103` |

## 5. Como testar

- Erros: `pytest tests/errors -q` com um caso por pasta/arquivo e a tupla
  `(codigo, linha, coluna)` esperada.
- Programas válidos: `pytest -m conformance -q`.
- O harness de conformidade impõe **timeout de 5 s** por programa, para que
  `while (true)` falhe o teste em vez de travar o CI.
- Todo caso desta tabela precisa de teste com o mesmo nome do caso, para que a
  documentação e a suíte não divirjam.
