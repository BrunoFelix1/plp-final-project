# Decisões de projeto (ADRs resumidos)

> Cada decisão tem: contexto, escolha, alternativas e consequência.
> **Status:** todas as decisões D-01 a D-15 foram aceitas pelo mantenedor em
> **17/11/2026**. Revisões futuras exigem um novo `D-NN` ou emenda à
> constituição, com justificativa.

## Índice

| ID | Decisão | Escolha | Status |
| --- | --- | --- | --- |
| D-01 | Palavras-chave | inglês (`if`, `else`, `while`, `true`, `false`) | Aceita |
| D-02 | Estrutura da AST | dados puros + visitantes | Aceita |
| D-03 | Palavras reservadas da v2 | reservadas desde a v1 | Aceita |
| D-04 | Observabilidade | instrução `print(expr);` | Aceita |
| D-05 | Stack | Python 3.12 + uv + pytest + ruff + mypy | Aceita |
| D-06 | Escopo | único (sem escopo de bloco) | Aceita |
| D-07 | Conversão `bool(x)` | rejeitada | Aceita |
| D-08 | Operador `%` | resto inteiro, proibido em float | Aceita |
| D-09 | Objetos | referência; campos `undef` | Aceita |
| D-10 | Construtores | fora de escopo | Aceita |
| D-11 | Arrays | só primitivos, tamanho literal | Aceita |
| D-12 | Erros | léxico/sintático param; tipos acumulam | Aceita |
| D-13 | Board | GitHub Projects v2 por usuário, vinculado ao repo | Aceita |
| D-14 | Licença | MIT | Aceita |
| D-15 | Funções de topo (A.5) | fora de escopo | Aceita |

---

## D-01 · Palavras-chave em inglês

**Contexto.** A tradução brasileira de Tucker e Noonan substitui palavras-chave
por `se`, `senão`, `enquanto`, `verdadeiro`, `falso` na Figura 2.7, mas a
listagem de tokens da Seção 2.3.1 e o Apêndice A usam `if`, `else`, `while`,
`true`, `false`. A tradução é inconsistente consigo mesma.

**Escolha.** Implementar o conjunto lexical da Seção 2.3.1 / Apêndice A:
`bool char else false float if int main true while`. A gramática em
`docs/01-linguagem-clite.md` já está nessa forma.

**Alternativas.** (a) traduzir tudo para português — fica mais distante do
código-fonte do livro e de C; (b) aceitar as duas formas — duplica reservadas e
cria ambiguidade de mensagens.

**Consequência.** Programas do livro que usam `se`/`enquanto` precisam de
tradução. É um exercício de 1 minuto e reforça a diferença entre léxico e
semântica.

---

## D-02 · AST como dados + visitantes

**Contexto.** O Apêndice A coloca `check` e `gen` em cada nó (abordagem
orientada a objeto). Um interpretador em Python pode fazer o mesmo com
`dataclasses` + métodos ou separar as fases em visitantes.

**Escolha.** Nós são `dataclass` imutáveis, sem lógica. `TypeChecker` e
`Evaluator` são visitantes. A AST carrega `line`/`column`.

**Por quê.** Fases testáveis isoladamente; adicionar um nó não obriga a mexer em
duas fases no mesmo arquivo; o paralelismo entre tickets fica trivial.

**Alternativa descartada.** Métodos `check`/`eval` nos nós: mais fiel ao livro,
porém mistura responsabilidades e dificulta que duas pessoas trabalhem em
léxico/parser e tipos ao mesmo tempo.

---

## D-03 · Reservar as palavras da v2 desde a v1

**Contexto.** A extensão OO adiciona `class`, `extends`, `new`, `this`,
`return`, `void` e `print`. Se elas forem identificadores válidos na v1, todo
programa que as use quebra na v2.

**Escolha.** Já na v1, essas palavras são reservadas e produzem erro léxico se
usadas como nome. A tabela de reservadas é única e testada.

**Alternativa.** Reservar só na v2 e aceitar a quebra — didaticamente mostra
evolução de linguagem, mas custa retrabalho nos testes de conformidade.

**Consequência.** O lexer da v1 conhece palavras que o parser ainda não usa. É
uma dívida pequena e documentada; o teste `test_reserved_words` cobre a lista.

---

## D-04 · `print(expr);` como instrução nativa

**Contexto.** CLite não tem entrada/saída. Sem saída, é impossível demonstrar
polimorfismo ou comparar programas de conformidade de forma legível.

**Escolha.** Adicionar a instrução `print(Expressão);`, fora da gramática de
Tucker, tratada como extensão de observabilidade. Ela aceita qualquer tipo e
imprime uma linha. Não é função: não retorna valor.

**Alternativas.** (a) CLI imprime o estado final (`--dump-state`) — insuficiente
para laços e chamadas; (b) comparar apenas estado interno nos testes — não
serve para demonstração em sala; (c) `assert` embutido — menos didático.

**Consequência.** O interpretador não é 100% CLite puro. Isso fica explícito no
manual e nos programas de exemplo. Um teste garante que `print` não pode ser
usada como expressão.

---

## D-05 · Stack

**Escolha.** Python 3.12+, `uv` para ambiente e lock, `pytest` (+ `pytest-cov`,
`hypothesis`), `ruff` (lint + format), `mypy --strict` em `src`, `pre-commit`,
GitHub Actions. Zero dependências de runtime.

**Por quê.** Tudo open source, rápido de instalar, padrão de mercado e sem
distrair do objetivo (a linguagem). Nenhuma biblioteca de parser: o parser é
escrito à mão, porque é ele que precisamos entender.

---

## D-06 · Escopo único

**Escolha.** Blocos não criam escopo, como no Apêndice A.3: todas as variáveis
de `main` pertencem a um único mapa; em métodos, parâmetros e locais formam o
escopo do método.

**Consequência.** `int main() { int x; { int x; } }` é erro de duplicidade —
diferente de C. Documentado e testado.

---

## D-07 · `bool(x)` rejeitado

A gramática permite `Tipo ( Expressão )` para qualquer tipo, mas as regras de
significado só definem `int`, `float` e `char`. Implementar `bool()` inventaria
semântica (0 = falso?) e contraria a decisão de CLite de não ter verdade
“truthy”. Erro `E3007` com mensagem explícita.

---

## D-08 · `%`

A gramática inclui `%`, mas as regras A.8 não o descrevem. Escolha: resto da
divisão inteira com sinal do dividendo (como C/Java) e erro de tipo se algum
operando for `float`. Documentado em `docs/01` §4 e testado.

---

## D-09 · Objetos por referência

Atribuir um objeto copia a referência; duas variáveis podem apontar para o mesmo
objeto. Campos nascem `undef`; ler antes de atribuir é `E4102`. Não há `null`.

**Alternativa descartada.** Copiar o objeto na atribuição (value semantics):
torna polimorfismo e aliasing irrelevantes e é menos parecido com Java, que é a
referência mental dos alunos.

---

## D-10 · Sem construtores

`new C()` não executa código do usuário. O programa inicializa campos
explicitamente. Construtores exigem resolução de chamada, `super` implícito,
ordem de inicialização e novas regras de tipo — escopo grande para o prazo.

**Alternativa.** Um “construtor padrão” que zera campos: descartado, porque
`undef` é parte do ensino de semântica.

---

## D-11 · Arrays

- tamanho é literal inteiro positivo (`int v[10];`);
- só arrays de tipos primitivos;
- acesso `v[i]` e atribuição `v[i] = x;` apenas com o nome do array;
- índice fora de faixa é erro de execução;
- não há arrays multidimensionais nem `length`.

---

## D-12 · Política de erros

Léxico e sintático param na primeira falha; o checker acumula erros de tipo;
execução para no primeiro erro. Toda mensagem sai como
`erro E<NNNN> (linha L, coluna C): texto`, sem stack trace.

---

## D-13 · Board

GitHub Projects v2 no nível do usuário `BrunoFelix1`, vinculado ao repositório
`BrunoFelix1/plp-final-project`. Colunas: Backlog, To Do, In Progress, In Review,
Ready for QA, In QA, Released. O campo nativo `Status` é reconfigurado.

**Alternativa.** Project no nível da organização: o repositório é de usuário, não
de organização; um project de repositório não existe no Projects v2.

---

## D-14 · Licença MIT

Projeto acadêmico e aberto. MIT permite reuso em portfólio e em sala. Se a
disciplina exigir outra licença ou nenhuma, é uma linha para trocar.

---

## D-15 · Funções de topo e globais (A.5)

O Apêndice A.5 acrescenta funções e variáveis globais, mas o pedido do projeto é
OO. Métodos cobrem chamada, parâmetros, retorno e escopo. Funções de topo
ficariam como segundo mecanismo de chamada, com regras de unicidade e escopo
adicionais, sem contribuir para o objetivo de OO.

**Consequência.** `return` existe apenas dentro de métodos; `main` é `int` mas
não retorna valor (compatível com o núcleo).

---

## Registro de aceitação

Em **17/11/2026**, o mantenedor do projeto aceitou as decisões **D-01 a D-15**
como estão descritas neste documento. Isso inclui, explicitamente:

| Decisão | Efeito prático |
| --- | --- |
| D-01 | palavras-chave em inglês (`if`, `else`, `while`, `true`, `false`) |
| D-03 | palavras da v2 reservadas já na v1 |
| D-04 | `print(expr);` como instrução nativa de observabilidade |
| D-10 | sem construtores definidos pelo usuário |
| D-14 | licença MIT |
| D-15 | sem funções de topo e variáveis globais do Apêndice A.5 |

A partir desta data, mudar qualquer uma delas exige:

1. um novo registro `D-NN` com contexto, alternativas e consequência; ou
2. uma emenda à constituição (`.specify/memory/constitution.md`), com
   justificativa no PR.

Os documentos de gramática (`docs/01` e `docs/02`) e os tickets que citam essas
decisões já estão alinhados com a versão aceita.
