# CLite: a linguagem que vamos interpretar

> Fonte: TUCKER, A. B.; NOONAN, R. *Linguagens de Programação: Princípios e
> Paradigmas*, 2. ed., capítulo 2 (a partir de 2.3) e Apêndice A.
>
> Este documento é a **fonte da verdade** da linguagem neste repositório. Se o
> código divergir daqui, o código está errado — ou este documento precisa de um
> ticket `docs:` que justifique a mudança.
>
> **Status da gramática:** v1 implementada; v2 (OO) em implementação. Este
> documento descreve a gramática **implementada na `main`**; `docs/02` descreve
> o desenho-alvo. Cada ticket OO atualiza este arquivo no mesmo PR (§12).

## 1. O que é CLite

CLite é um subconjunto de C criado pelos autores do livro para ensinar sintaxe,
sistemas de tipos e semântica sem o ruído de uma linguagem real. Tem um único
ponto de entrada (`main`), variáveis de quatro tipos primitivos, arrays de
tamanho fixo, atribuição, `if`/`else`, `while`, blocos e expressões com
precedência bem definida. Não tem entrada/saída, funções definidas pelo
programador, nem bibliotecas — no núcleo.

O objetivo do projeto é **entender a construção de uma linguagem**, por isso a
implementação segue as fases do front-end descritas em *Compiladores:
Princípios, Técnicas e Ferramentas* (Apêndice A): léxico → sintático →
semântico → execução.

## 2. Camadas da definição

| Camada | O que define | Onde vive |
| --- | --- | --- |
| Sintaxe léxica | caracteres → tokens (identificadores, literais, palavras reservadas, operadores, pontuação) | `src/clite/lexer/` |
| Sintaxe concreta | tokens → árvore de análise conforme a gramática | `src/clite/parser/` |
| Sintaxe abstrata | forma canônica da árvore usada pelo restante do interpretador | `src/clite/ast/` |
| Sistema de tipos | quais programas são válidos antes de executar | `src/clite/semantic/` |
| Semântica | o que o programa faz quando executado | `src/clite/interpreter/` |

## 3. Gramática concreta (GClite)

Notação: `{ x }` = zero ou mais; `[ x ]` = opcional. **Cuidado:** na gramática
original do livro, `Identificador [ [ Inteiro ] ]` significa *identificador
opcionalmente seguido de `[ Inteiro ]`* — os colchetes internos são a sintaxe do
array, os externos são a metanotação de “opcional”. Não existem colchetes
duplos na linguagem.

```ebnf
Programa        → int main ( ) { Declarações Comandos }
Declarações     → { Declaração }
Declaração      → Tipo Identificador [ [ Inteiro ] ] { , Identificador [ [ Inteiro ] ] } ;
Tipo            → int | bool | float | char
Comandos        → { Comando }
Comando         → ; | Bloco | Atribuição | ComandoSe | ComandoEnquanto
Bloco           → { Comandos }
Atribuição      → Identificador [ [ Expressão ] ] = Expressão ;
ComandoSe       → if ( Expressão ) Comando [ else Comando ]
ComandoEnquanto → while ( Expressão ) Comando

Expressão       → Conjunção { || Conjunção }
Conjunção       → Igualdade { && Igualdade }
Igualdade       → Relação [ OpIgual Relação ]
OpIgual         → == | !=
Relação         → Adição [ OpRel Adição ]
OpRel           → < | <= | > | >=
Adição          → Termo { OpAdição Termo }
OpAdição        → + | -
Termo           → Fator { OpMult Fator }
OpMult          → * | / | %
Fator           → [ OpUn ] Primário
OpUn            → - | !
Primário        → Identificador [ [ Expressão ] ] | Literal | ( Expressão )
                | Tipo ( Expressão )

Identificador   → Letra { Letra | Dígito }
Letra           → a | … | z | A | … | Z
Dígito          → 0 | … | 9
Literal         → Inteiro | Boleano | PontoFlutuante | Caractere
Inteiro         → Dígito { Dígito }
Boleano         → true | false
PontoFlutuante  → Inteiro . Inteiro
Caractere       → ' CaractereASCII '
```

O Apêndice A reescreve as regras de expressão no estilo “pós-fixado”
(`Adição → Termo { Termo AddOp }`). É a mesma linguagem, com outra notação; a
versão acima é a que o parser recursivo descendente segue.

### 3.1 Exemplos válidos

```c
int main() {
    int i, j;
    float x;
    int v[10];
    i = 0;
    while (i < 10) {
        v[i] = i * 2;
        i = i + 1;
    }
    if (v[3] == 6) j = 1; else j = 0;
    x = float(j) / 2.0;
}
```

```c
int main() {
    int a, b[3];
    bool ok;
    a = 1; b[0] = a + 1;
    ok = (a < b[0]) && !(a == b[0]);
}
```

## 4. Sintaxe léxica

### 4.1 Alfabeto

ASCII imprimível. Espaço, tabulação (`\t`), retorno de carro (`\r`) e nova
linha (`\n`) são **espaço em branco** e não geram token. Comentários começam
com `//` e vão até o fim da linha (convenção de C++).

### 4.2 Tokens

| Grupo | Tokens |
| --- | --- |
| Palavras reservadas | `bool` `char` `else` `false` `float` `if` `int` `main` `true` `while` |
| Identificadores | letra seguida de letras/dígitos: `x`, `contador`, `a1` |
| Literais | inteiro (`42`), float (`3.14`), booleano (`true`), caractere (`'a'`) |
| Operadores |  `&&` `=` `==` `!=` `<` `<=` `>` `>=` `+` `-` `*` `/` `%` `!` `[` `]` `\|\|` |
| Pontuação | `;` `,` `{` `}` `(` `)` |

`main` é **reservada em CLite** (difere de C/C++, onde é um identificador
especial). `void`, `class`, `extends`, `new`, `this`, `return` e `print` entram
na lista de reservadas já na v1, mesmo antes da extensão OO, para que nenhum
programa válido da v1 quebre na v2. Ver `docs/05-decisoes.md` (D-03).

### 4.3 Regras de reconhecimento

1. **Maior casamento (maximal munch):** o lexer consome sempre a maior
   sequência que forma um token válido. `whilea` é um identificador, não
   `while` + `a`. `<=` é um token; `< =` são dois.
2. **Espaço em branco é separador, não conteúdo.** `a<b` e `a < b` produzem a
   mesma sequência de tokens.
3. **Float exige dígitos dos dois lados do ponto:** `5.0` e `0.5` valem;
   `5.` e `.5` não. Um ponto isolado não é token — produza `E1001`.
4. **Caractere:** exatamente um caractere imprimível entre aspas simples.
   `''` e `'ab'` são erro léxico. Não há escapes (`'\n'`) no núcleo.
5. **Comentário** não aninha e termina na nova linha; `//` dentro de um literal
   de caractere não é comentário.
6. Todo token carrega `linha` e `coluna` (1-based) para as mensagens de erro.

### 4.4 Palavras reservadas × identificadores

Uma palavra reservada **nunca** pode ser usada como nome de variável, array,
classe, campo, método ou função. O lexer resolve isso com uma tabela de
palavras-chave consultada antes de devolver um identificador. A pergunta “este
nome é reservado?” é respondida por uma função pública do lexer, usada pelo
parser, pela tabela de símbolos e pelos testes.

## 5. Precedência e associatividade

Da maior para a menor precedência:

| Nível | Operadores | Associatividade |
| --- | --- | --- |
| 1 | unário `-` `!` | nenhuma (prefixo) |
| 2 | `*` `/` `%` | esquerda |
| 3 | `+` `-` | esquerda |
| 4 | `<` `<=` `>` `>=` | **nenhuma** |
| 5 | `==` `!=` | **nenhuma** |
| 6 | `&&` | esquerda |
| 7 | `\|\|` | esquerda |

`a < b < c` é **erro sintático** em CLite: operadores relacionais e de
igualdade não são associativos. O mesmo para `a == b == c`. Essa é uma decisão
de projeto herdada de Ada que evita o bug silencioso de C.

## 6. Sintaxe abstrata (núcleo)

```text
Programa      = Declarações decpart; Comandos body
Declaração    = VarDecl(nome, tipo) | ArrayDecl(nome, tipo, tamanho)
Comando       = Skip | Bloco(Comandos) | Atribuição(alvo, fonte)
              | Condicional(teste, então, senão?) | Laço(teste, corpo)
Expressão     = VarRef(nome) | ArrayRef(nome, índice) | Valor
              | Binário(op, esq, dir) | Unário(op, termo)
Valor         = IntValor | FloatValor | BoolValor | CharValor
```

Arrays são de tamanho fixo e o tamanho é um **literal inteiro** na declaração,
não uma expressão (`int v[n];` é erro). Blocos **não** introduzem escopo: todas
as variáveis do programa pertencem ao mesmo mapa de tipos (Apêndice A.3). Essa
é uma simplificação importante e uma pergunta clássica de prova.

## 7. Sistema de tipos (resumo das regras A.1–A.6)

1. Toda variável referenciada deve estar declarada; todo nome declarado é único.
2. Atribuição: `float ← float|int`, `int ← int|char`, `bool ← bool`,
   `char ← char`. Não há promoção implícita de `int` para `float` na
   atribuição — use `float(x)`.
3. Condição de `if` e `while` deve ser `bool`. Não existe “0 é falso”.
4. Aritméticos exigem `int`/`float` nos dois lados e **os dois lados do mesmo
   tipo**; relacionais exigem o mesmo tipo dos dois lados; `&&`/`||` exigem
   `bool`.
5. `!` exige `bool`; `-` exige `int` ou `float`.
6. Conversões explícitas: `int(x)` aceita `float`/`char`; `float(x)` e `char(x)`
   aceitam `int`. `bool(x)` não faz parte da semântica do livro e é rejeitada
   com mensagem clara (ver D-07).

## 8. Semântica (resumo das regras A.1–A.12)

- O estado inicial tem todas as variáveis com `undef` do seu tipo.
- Usar `undef` em qualquer operação torna o programa **sem significado**; nosso
  interpretador aborta com erro de execução `E4001`.
- `int / int` trunca em direção a zero; divisão por zero é erro `E4002`.
- Aritmética `float` segue IEEE 754.
- `&&` e `||` têm curto-circuito: `a && b ≡ if a then b else false`.
- Relacionais produzem `bool`; `false < true`.
- Arrays: índice fora de `[0, tamanho)` é erro `E4003`.
- `=` é atribuição, `==` é igualdade. Confundir os dois gera erro sintático,
  não comportamento silencioso.

## 9. O que o núcleo **não** tem

Funções do programador, `return`, entrada/saída, `for`, `do/while`, `break`,
strings, ponteiros, `null`, escopo de bloco, conversões implícitas, `switch`,
`const`, tipos definidos pelo usuário. Tudo isso só entra se houver ticket e
atualização deste documento.

## 10. Lacunas da definição do livro e como as resolvemos

| Tema | Lacuna no livro | Decisão do projeto |
| --- | --- | --- |
| `%` | aparece na gramática, mas não nas regras de significado | resto inteiro com sinal do dividendo; proibido em `float` |
| `bool(x)` | `Primário` aceita qualquer `Tipo ( … )` | rejeitado com `E3007` |
| `undef` | “sem significado” | erro de execução `E4001` |
| divisão por zero | não tratada | erro de execução `E4002` |
| ordem de avaliação | não definida | esquerda → direita, exceto curto-circuito |
| `5.` / `.5` | proibidos pela gramática | erro léxico `E1001` |
| `'` como literal | a aspa é ASCII imprimível, mas não há escape | a aspa simples não pode ser um literal de caractere |
| comentários | fora da gramática | `//` até o fim da linha |

O racional completo, com alternativas descartadas, está em
[`05-decisoes.md`](05-decisoes.md).

## 11. Para estudar

- Tucker e Noonan, cap. 2 (2.3–2.6): sintaxe, tokens, árvores de análise.
- Tucker e Noonan, cap. 3: análise descendente recursiva.
- Tucker e Noonan, cap. 6: sistema de tipos de CLite.
- Tucker e Noonan, cap. 8: semântica operacional.
- Tucker e Noonan, Apêndice A: definição completa.
- *Compiladores*, cap. 1: o que é um front-end.
- *Compiladores*, cap. 2 e Apêndice A: lexer, parser e classes de AST.

## 12. Governança da gramática (v1 → v2)

**Regra.** `docs/01` descreve a gramática **implementada na `main`**; `docs/02`
descreve o **desenho-alvo** da v2 e o racional. No mesmo PR de cada ticket de
OO, as seções afetadas de `docs/01` são atualizadas para refletir exatamente o
que o parser passou a aceitar. Documento e código nunca entram separados.

| Ticket | Atualização obrigatória em `docs/01` |
| --- | --- |
| `docs: 026` | criar esta seção e a regra de atualização por ticket; nenhuma produção nova |
| `feat: 027` | §3 (gramática concreta): `class`, `extends`, membros, `new`, `this`, `return`, `print` |
| `feat: 028` | §6 (sintaxe abstrata): nós de classe, membro, acesso e chamada |
| `feat: 029` | §3 e §6: `new`, campo, `this` e chamada; §8: modelo de objetos |
| `feat: 030` | §7 (tipos): subtipagem, override, `this`, `return` |
| `feat: 031` | §8 (semântica): despacho dinâmico e busca na hierarquia |
| `feat: 032` | §3 e §8: exemplo OO e gramática final da v2 |
| `feat: 033` | §3/§6: corrigir divergência entre AST exibida e gramática |
| `docs: 034` | revisão integral: manual, gramática e comportamento |
| `chore: 035` | congelar a gramática da release 1.0.0 |
| `chore: 036` | auditoria `docs/01` × parser, sem divergência |

**Checklist de cada ticket OO**

- [ ] A produção nova está no bloco EBNF de §3, na posição correta.
- [ ] A sintaxe abstrata correspondente está em §6.
- [ ] As regras de tipo novas estão em §7, com código de erro.
- [ ] A semântica nova está em §8.
- [ ] Um programa de `examples/oo/` exercita a construção.
- [ ] `docs/02` continua sendo o desenho-alvo; divergência entre os dois é
      registrada como decisão, não escondida.

Quando a v2 estiver completa, `docs/01` passa a ser a referência única da
linguagem e `docs/02` fica como histórico do desenho e das alternativas.
