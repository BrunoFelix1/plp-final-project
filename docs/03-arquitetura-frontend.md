# Arquitetura: um front-end completo em Python

> Base: *Compiladores: Princípios, Técnicas e Ferramentas*, cap. 1 (o que é o
> front-end) e Apêndice A (um front-end completo). O Apêndice A é escrito em
> Java, com os pacotes `main`, `lexer`, `symbols`, `parser` e `inter`; aqui os
> mesmos conceitos aparecem em Python.

## 1. O que o livro chama de front-end

O capítulo 1 divide a tradução de um programa em **análise** (front-end) e
**síntese** (back-end):

| Front-end (análise) | Back-end (síntese) |
| --- | --- |
| análise léxica → tokens | otimização |
| análise sintática → árvore | geração de código |
| análise semântica → verificação de tipos | alocação de registradores |
| representação intermediária | código de máquina |

O Apêndice A implementa exatamente as três primeiras fases e para na
representação intermediária (código de três endereços). **Nosso projeto troca a
geração de código por avaliação direta da AST.** Continuamos sendo um front-end
completo — e ganhamos um interpretador executável, que é o objetivo didático.

```text
cli.py (entrada: `clite tokens|parse|check|run`)
      │
programa.clite
      │
      ▼
┌─────────────┐   Token(tag, lexema, linha, coluna)
│   Lexer     │ ───────────────────────────────────────┐
└─────────────┘ lexer/                                 │
      ▲                                                ▼
      │                                        ┌─────────────┐
   caracteres                                  │   Parser    │  parser/
                                               └─────────────┘
                                                      │ AST (ast/)
                                                      ▼
                                          ┌────────────────────────┐
                                          │ Semantic (TypeChecker) │  semantic/
                                          └────────────────────────┘  ← tabela de símbolos
                                                      │                 (symbols.py, types.py)
                                                      │ AST validada
                                                      ▼
                                               ┌─────────────┐
                                               │ Interpret.  │  interpreter/
                                               └─────────────┘  ← estado (values.py)
                                                      │
                                                      ▼
                                                print / estado final

errors.py: usado por todas as fases (E1xxx léxico … E4xxx execução, ver §5)
```

## 2. Mapa Apêndice A → Python

| Java (Apêndice A) | Python (este projeto) | Papel |
| --- | --- | --- |
| `main.Main` | `clite/cli.py` | ponto de entrada, escolhe a fase e o arquivo |
| `lexer.Tag` | `clite/lexer/tags.py` | constantes inteiras dos tokens |
| `lexer.Token`, `Word`, `Num`, `Real` | `clite/lexer/tokens.py` | token genérico, palavra/identificador, números |
| `lexer.Lexer` | `clite/lexer/lexer.py` | varredura, palavras reservadas, linha/coluna |
| `symbols.Type`, `Env`, `Array` | `clite/types.py`, `clite/symbols.py`, `clite/values.py` | tipos, escopos, arrays |
| `parser.Parser` | `clite/parser/parser.py` | descendente recursivo, um método por não-terminal |
| `inter.Node`, `Expr`, `Stmt` | `clite/ast/nodes.py` | hierarquia da sintaxe abstrata |
| `inter.Id`, `Access`, `Set`, `Seq`, `If`, `While`, `And`, `Or`, `Not`, `Rel`, `Arith`, `Unary`, `Constant` | `clite/ast/nodes.py` | nós concretos |
| `inter.Type` (conversões) | `clite/ast/nodes.py` + `clite/semantic/` | `int()`, `float()`, `char()` |
| métodos `check`/`gen` dos nós | `clite/semantic/checker.py` e `clite/interpreter/evaluator.py` | duas passadas sobre a mesma AST |

O Apêndice A concentra tipo e geração de código **em cada nó** (abordagem
orientada a objeto). Aqui usamos **visitantes** (`TypeChecker` e `Evaluator`)
sobre nós que são dados puros. Vantagens: a AST fica pequena, as fases ficam
visíveis e cada uma pode ser testada isoladamente. Ver D-02. O próprio Apêndice A
chama isso de abordagem orientada a objeto × orientada a fase: a primeira facilita
incluir construções; a segunda, que adotamos, facilita incluir ou mudar fases.

## 3. Estrutura de pacotes

```text
src/clite/
├── __init__.py
├── cli.py                 # `clite run|tokens|parse|check`
├── errors.py              # CliteError e subclasses; códigos E1xxx–E4xxx
├── types.py               # IntType, BoolType, FloatType, CharType, VoidType, ClassType
├── values.py              # IntValue, BoolValue, FloatValue, CharValue, Undef, ObjectValue
├── symbols.py             # Scope, SymbolTable, ClassInfo, MethodInfo
├── lexer/
│   ├── tags.py            # Tag.IF_STATEMENT, Tag.INT, ...
│   ├── tokens.py          # Token, Keyword, Identifier, IntLiteral, ...
│   └── lexer.py           # Lexer.scan() -> Token
├── parser/
│   └── parser.py          # Parser.program(), declaration(), statement(), expression()...
├── ast/
│   └── nodes.py           # dataclasses: Program, VarDecl, Assign, If, While, Binary, ...
├── semantic/
│   └── checker.py         # TypeChecker.check(program) -> CheckedProgram
└── interpreter/
    └── evaluator.py       # Evaluator.run(program) -> State
```

O esqueleto já existe com `__init__.py` e docstrings; cada ticket preenche uma
fronteira por vez.

## 4. Contratos entre as fases

### 4.1 Lexer → Parser

Todo token tem `tag`, `lexeme`, `line`, `column`. Tokens compostos (`<=`, `&&`)
são um único token. O parser nunca olha caracteres: só tokens. É isso que
permite testar a gramática com uma lista de tokens, como sugere o professor.

### 4.2 Parser → AST

Cada não-terminal tem um método (`parse_program`, `parse_statement`, …). Erros
sintáticos usam o token corrente e a mensagem “esperava X, encontrei Y”. A AST
não guarda tokens, só posição (`line`, `column`) para relatórios.

### 4.3 AST → TypeChecker

O checker percorre a AST com um `TypeContext`:

- **globais** (v2): classes, campos, assinaturas de métodos;
- **locais**: variáveis de `main` ou (v2) de um método;
- **retorno** (v2): tipo de retorno do método corrente;
- **classe corrente** (v2): para `this` e para resolver campos.

Na v1 só existem as variáveis de `main`, num escopo único (D-06).

Saída: a mesma AST anotada com `static_type` em cada expressão, ou uma lista de
erros. Nenhuma execução acontece se houver erro de tipo.

### 4.4 AST → Interpretador

O estado de execução tem:

- `frames`: pilha de ambientes (main, chamada de método); na v1, um único
  ambiente com as variáveis de `main` (D-06);
- `heap` (v2): objetos alocados por `new`;
- `output`: linhas produzidas por `print`.

O avaliador devolve um valor para expressões e um estado para comandos. (v2)
`return` é implementado com uma exceção interna `ReturnSignal`, capturada pela
chamada de método. Erros de execução (divisão por zero, índice inválido, `undef`) viram
`RuntimeCliteError` com linha/coluna.

## 5. Estratégia de erros

| Fase | Código | Exemplo |
| --- | --- | --- |
| Léxico | `E1xxx` | caractere inesperado, float malformado, `&` ou `\|` isolado (`E1002`), comentário aberto |
| Sintático | `E2xxx` | `;` ausente, `else` órfão, `a < b < c` |
| Semântico | `E3xxx` | variável não declarada, tipo incompatível, override inválido |
| Execução | `E4xxx` | divisão por zero, índice fora, uso de `undef` |

Formato de mensagem (uma linha, legível por humano e por teste):

```text
erro E3001 (linha 4, coluna 9): variável 'x' não declarada
```

Regras:

- o lexer para no primeiro erro léxico (não há como continuar com segurança);
- o parser para no primeiro erro, mas a CLI aceita `--max-errors N` no futuro;
- o checker coleta todos os erros de tipo antes de abortar;
- a mensagem sempre inclui linha e coluna e nunca mostra stack trace.

## 6. CLI

```text
clite tokens  programa.clite     # lista tokens (tag, lexema, linha:coluna)
clite parse   programa.clite     # mostra a AST em formato de árvore
clite check   programa.clite     # só verifica tipos
clite run     programa.clite     # executa; imprime o que `print` produzir
clite run     programa.clite --dump-state   # estado final das variáveis
```

Códigos de saída: `0` sucesso, `1` erro de programa (léxico/sintático/tipo),
`2` erro de uso da CLI.

## 7. Testes

| Nível | O que cobre | Como |
| --- | --- | --- |
| Unidade | lexer, parser, checker, avaliador isolados | `pytest tests/unit/` |
| Conformidade | programas `.clite` completos com saída esperada | `pytest -m conformance` |
| Erros | programas inválidos com código e linha esperados | casos em `tests/errors/` |
| Propriedades | invariantes do lexer (espaço não muda tokens, maior casamento) | Hypothesis |
| Regressão | todo bug corrigido vira teste | PR obrigatório |

A suíte de conformidade é a “prova” de que a linguagem implementada corresponde
à gramática documentada. Cada programa tem um cabeçalho com a saída esperada ou
um arquivo `.out` irmão.

## 8. Não objetivos

- gerar código de máquina ou bytecode;
- otimizar;
- IDE, *language server* ou *debugger* gráfico;
- compatibilidade com C real;
- desempenho. Clareza didática vence.
