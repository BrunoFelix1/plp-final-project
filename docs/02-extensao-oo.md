# Extensão orientada a objetos (CLite-OO)

> Este documento define a **v2** da linguagem. Ele só vale depois que a v1
> (núcleo de Tucker e Noonan) estiver implementada e verde na `main`; a
> implementação entra por incrementos pequenos, um ticket por vez.
>
> **Relação com `docs/01`:** `docs/01` é a gramática **implementada**; este
> documento é o **desenho-alvo** da v2. A cada ticket OO, `docs/01` é atualizado
> no mesmo PR com o que passou a ser aceito (§12 de `docs/01`).

## 1. Escopo

Entra:

- declaração de classe com campos e métodos;
- herança simples (`extends`);
- criação de objetos com `new`;
- acesso a campos e chamada de métodos (`obj.f`, `obj.m(args)`);
- `this` dentro de métodos;
- **sobreescrita** (override) de métodos;
- **polimorfismo** por despacho dinâmico: a variável tem o tipo estático, o
  objeto tem o tipo dinâmico;
- `void`, `return` e uma instrução `print` de apoio ao ensino.

Não entra (decisão explícita):

- classe abstrata, interface, `implements`;
- reflexão, `getClass`, metaprogramação;
- construtores declarados pelo usuário e `super(...)`;
- sobrecarga (overload) de métodos;
- modificadores de acesso (`public`, `private`, `protected`, `static`, `final`);
- `null`, exceções, genéricos, classes internas;
- arrays de objetos;
- funções de topo e variáveis globais do Apêndice A.5 (o Apêndice A as
  apresenta como extensão separada; aqui o foco é OO).

## 2. Gramática (delta sobre a v1)

```ebnf
Programa        → { DeclaraçãoClasse } int main ( ) { Declarações Comandos }

DeclaraçãoClasse → class Id [ extends Id ] { { Membro } }
Membro           → DeclaraçãoCampo | DeclaraçãoMetodo
DeclaraçãoCampo  → Tipo Id { , Id } ;
DeclaraçãoMetodo → TipoRetorno Id ( Parâmetros ) { Declarações Comandos }
TipoRetorno      → Tipo | void
Tipo             → int | bool | float | char | Id
Parâmetros       → [ Parâmetro { , Parâmetro } ]
Parâmetro        → Tipo Id

Comando          → …v1… | ComandoChamada | ComandoRetorno | ComandoPrint
ComandoChamada   → Chamada ;
Chamada          → Id ( Argumentos ) | Pósfixo . Id ( Argumentos )
ComandoRetorno   → return [ Expressão ] ;
ComandoPrint     → print ( Expressão ) ;

Atribuição       → Alvo = Expressão ;
Alvo             → Id [ [ Expressão ] ] | Pósfixo . Id

Expressão        → …v1… 
Fator            → [ OpUn ] Pósfixo
Pósfixo          → Primário { . Id [ ( Argumentos ) ] }
Primário         → Id [ [ Expressão ] ] | this | new Id ( ) | Literal
                 | ( Expressão ) | Tipo ( Expressão )
```

Observações de parsing:

- `Tipo` inclui `Id` (nome de classe), mas só em **declarações** e parâmetros.
  No `Primário`, `Id ( … )` é chamada de método, nunca conversão de tipo —
  conversões só existem para os quatro tipos primitivos, que são palavras
  reservadas.
- `new Id ( )` exige parênteses vazios: não há construtor com argumentos.
- `Alvo` aceita `obj.campo` e `obj.campo.campo`, mas **não** `obj.arr[i]` nem
  `obj.m().campo` como alvo. Arrays só existem como variável local/campo de tipo
  primitivo, acessados diretamente pelo nome (`v[i]`).
- Chamada sem receptor (`m(1, 2)`) dentro de um método equivale a
  `this.m(1, 2)`. Dentro de `main` isso é erro semântico: não há funções.

## 3. Exemplo completo

```c
class Animal {
    int pernas;

    void fala() {
        print(0);
    }
}

class Cachorro extends Animal {
    void fala() {
        print(1);
    }

    int dobro(int x) {
        return x * 2;
    }
}

int main() {
    Animal a;
    Cachorro c;
    a = new Animal();
    c = new Cachorro();
    a.pernas = 4;
    c.pernas = 4;
    a.fala();       // 0
    c.fala();       // 1
    a = c;          // upcast: Cachorro é um Animal
    a.fala();       // 1 — polimorfismo
}
```

## 4. Modelo de execução

- `new C()` cria um objeto com **todos** os campos de `C` e dos ancestrais,
  inicializados com `undef` do tipo declarado. Não há construtor: o programa
  atribui os campos depois do `new`.
- Objetos têm **semântica de referência**: `a = c` copia a referência, não os
  campos. Primitivos têm semântica de valor.
- O tipo **estático** de uma expressão decide o que pode ser acessado e
  chamado. O tipo **dinâmico** do objeto decide qual implementação de método
  roda.
- Despacho: procura-se o método pelo nome na classe dinâmica; se não existir,
  sobe para a superclasse. Implementação de referência: cada classe mantém um
  mapa `nome → método` e um ponteiro para a superclasse (modelo mental de
  *vtable*).
- Campos são resolvidos estaticamente: não há polimorfismo de campo, e o
  projeto **proíbe** esconder um campo do ancestral com o mesmo nome.

## 5. Sistema de tipos

Além das regras A.1–A.6 do núcleo:

| Regra | Conteúdo |
| --- | --- |
| OO-1 | Nomes de classe são únicos. O grafo de `extends` é acíclico. |
| OO-2 | Campos de uma classe têm nomes únicos; um campo não pode repetir o nome de um campo de qualquer ancestral. |
| OO-3 | Métodos de uma classe têm nomes únicos (sem sobrecarga). |
| OO-4 | Uma sobreescrita exige **mesmo nome, mesma lista de tipos de parâmetros** e tipo de retorno igual ou subtipo do original. |
| OO-5 | `new C()` tem tipo `C`; `this` tem o tipo da classe que o contém. |
| OO-6 | `e.f` exige que o tipo estático de `e` seja uma classe que declare `f` (nela ou em ancestral). |
| OO-7 | `e.m(a₁…aₙ)`: `m` deve existir no tipo estático de `e`; aridade igual; cada argumento atribuível ao parâmetro; resultado é o tipo declarado. |
| OO-8 | `S` é atribuível a `T` se `S == T` ou `S` é subclasse de `T`. Vale para atribuição, argumentos e `return`. |
| OO-9 | Em método não `void`, `return expr;` com expr atribuível ao tipo de retorno; em `void`, só `return;`. |
| OO-10 | `main` não pode conter `return` com valor, e não pode declarar métodos. |
| OO-11 | Um parâmetro ou local não pode repetir o nome de um campo visível (evita ambiguidade silenciosa). |

`print(x)` aceita qualquer tipo: primitivos imprimem o literal; objetos imprimem
`Classe{ campo=valor, … }`, o que torna o polimorfismo visível na saída.

## 6. Erros específicos

| Código | Situação |
| --- | --- |
| E3101 | classe duplicada |
| E3102 | ciclo em `extends` |
| E3103 | campo duplicado ou campo escondendo campo do ancestral |
| E3104 | método duplicado (sobrecarga não suportada) |
| E3105 | sobreescrita incompatível (parâmetros ou retorno) |
| E3106 | acesso a campo inexistente no tipo estático |
| E3107 | método inexistente, aridade errada ou argumento incompatível |
| E3108 | atribuição entre tipos não relacionados |
| E3109 | `this` fora de método |
| E3110 | `return` incompatível ou ausente em método não `void` |
| E4101 | chamada de método sobre `undef` |
| E4102 | campo lido antes de receber valor |
| E4103 | método não `void` terminou sem `return` |

## 7. Polimorfismo e sobreescrita: como demonstrar

Três programas em `examples/oo/` (criados nos tickets de OO):

1. `override.clite` — subclasse troca a implementação e o mesmo objeto responde
   diferente conforme o tipo estático usado.
2. `polimorfismo.clite` — array de referências? **não**: uma sequência de
   variáveis de tipos diferentes apontando para objetos e chamadas repetidas,
   mostrando o despacho pela classe dinâmica.
3. `heranca_campos.clite` — campo declarado na superclasse, usado pela
   subclasse e por `main`.

Cada programa tem uma saída esperada em `tests/conformance/` e roda no CI.

## 8. Riscos e mitigação

| Risco | Mitigação |
| --- | --- |
| Crescer a gramática antes de estabilizar a v1 | v2 só começa com a suíte de conformidade v1 verde |
| Ambiguidade `Id(` (chamada × cast) | casts só para tipos reservados; `Id(` é sempre chamada |
| `return` no meio de `while`/`if` | avaliador propaga uma exceção interna `ReturnSignal` |
| Despacho errado por nome | sem sobrecarga, o nome identifica o método; teste de override cobre |
| Escopo confuso | regra OO-11 proíbe colisão campo × local × parâmetro |
| Regressão na v1 | toda mudança OO roda a suíte inteira, incluindo os programas v1 |

## 9. Ordem de implementação

1. Gramática e regras de tipo (este documento) — ticket `docs: 027`.
2. Léxico e parser de classes (sem execução) — `feat: 028`.
3. AST, tabela de símbolos e hierarquia — `feat: 029`.
4. `new`, campos, `this`, chamada de método — `feat: 030`.
5. Verificação de tipos OO e override — `feat: 031`.
6. Despacho dinâmico — `feat: 032`.
7. Programas e testes de polimorfismo — `feat: 033`.
