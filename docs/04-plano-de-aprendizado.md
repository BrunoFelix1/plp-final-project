# Plano de aprendizado e cronograma

> Entrega final: **06/12/2026**. Início do planejamento: 17/11/2026.
> O cronograma é curto de propósito: cada ticket precisa caber em uma sessão de
> estudo de 1–2 h e terminar com a `main` verde.

## 1. Princípio: aprender > entregar

O objetivo prioritário é **entender como uma linguagem é construída**. Por
isso, cada ticket segue o mesmo ritual:

1. **Ler** o trecho indicado do livro (15–20 min).
2. **Explicar em voz alta** o conceito antes de abrir o editor.
3. **Implementar** a menor fatia que faz um teste passar.
4. **Rodar** o comando de teste do ticket e ver falhar / passar.
5. **Quebrar de propósito** uma entrada e observar a mensagem de erro.
6. **Escrever** no PR, em 3 linhas, o que aprendeu.

Se o passo 2 não sai, o ticket não está pronto para começar: peça uma sessão de
estudo ou divida o ticket.

## 2. Trilhas paralelas

Os tickets foram desenhados para permitir três trilhas simultâneas:

| Trilha | Conteúdo | Tickets típicos |
| --- | --- | --- |
| **A — Linguagem** | lexer → parser → tipos → execução | `feat:` ímpares do núcleo |
| **B — Qualidade** | testes, CI, erros, cobertura | `chore:` e parte dos `feat:` de teste |
| **C — Conhecimento** | gramática, decisões, manual, demos | `docs:` |

Regra de ouro: **duas trilhas nunca editam o mesmo arquivo ao mesmo tempo**. O
campo “Paralelismo” de cada ticket lista os arquivos que ele toca.

## 3. Cronograma por milestone

### M1 · Fundação e léxico — até 21/11/2026

| # | Ticket | Conceito |
| --- | --- | --- |
| 001 | bootstrap Python/uv/CI | ambiente reprodutível |
| 002 | gramática de referência e glossário | sintaxe concreta × abstrata |
| 003 | arquitetura do front-end | fases do compilador |
| 004 | esqueleto de pacotes e CLI | fronteiras entre fases |
| 005 | tokens e palavras reservadas | token, lexema, palavra reservada |
| 006 | scanner de identificadores, literais e comentários | maior casamento, autômato |
| 007 | tabela de operadores e pontuação | tokens compostos |
| 008 | CLI `tokens` e golden tests | teste de lexer sem parser |

**Demo do milestone:** `clite tokens` em um programa com `while`, `<=`, `3.14`,
`// comentário` e um erro léxico proposital.

Leitura: Tucker 2.3.1 e 2.4; *Compiladores* 1.2–1.3 e 3.1–3.3 (seções de lexer).

### M2 · Núcleo executável — até 26/11/2026

| # | Ticket | Conceito |
| --- | --- | --- |
| 009 | AST base e expressões | sintaxe abstrata |
| 010 | parser de expressões | precedência, associatividade, recursão |
| 011 | parser de declarações e comandos | gramática LL(1), `else` pendente |
| 012 | tabela de símbolos | escopo único de CLite |
| 013 | checagem de tipos de expressões | regras A.5–A.6 |
| 014 | checagem de tipos de comandos | regras A.3–A.4 |
| 015 | avaliador de expressões | estado, `undef`, curto-circuito |
| 016 | executor de comandos | semântica operacional |
| 017 | CLI `run` e `--dump-state` | programa de ponta a ponta |
| 018 | arrays | tamanho fixo, limites |

**Demo do milestone:** programa que calcula média com `while`, array e `if`.

Leitura: Tucker 3.3, 6.1–6.3, 8.2; Apêndice A.1–A.4; *Compiladores* 2.5–2.8 e
Apêndice A.2–A.8.

### M3 · Conformidade — até 01/12/2026

| # | Ticket | Conceito |
| --- | --- | --- |
| 019 | erros diagnósticos com códigos | posição e recuperação |
| 020 | suíte de conformidade v1 | teste de ponta a ponta |
| 021 | conversões `int`/`float`/`char` | coerção explícita |
| 022 | semântica de `&&`, `\|\|`, comparadores | avaliação preguiçosa |
| 023 | propriedades do lexer | teste baseado em propriedades |
| 024 | gate de cobertura no CI | qualidade mensurável |
| 025 | relatório de lacunas da gramática | decisão documentada |

**Demo do milestone:** `make check` verde + 10 programas de conformidade,
incluindo 5 casos de erro com código e linha.

Leitura: Tucker 2.5–2.6 (semântica), 6.3; Apêndice A.3–A.4.

### M4 · Orientação a objetos — até 04/12/2026

| # | Ticket | Conceito |
| --- | --- | --- |
| 026 | gramática e tipos de CLite-OO | projeto de linguagem |
| 027 | lexer/parser de classes | extensão incremental |
| 028 | AST e hierarquia de classes | tabela de símbolos com herança |
| 029 | `new`, campos, `this`, chamadas | modelo de objetos |
| 030 | checagem de tipos OO e override | subtipagem |
| 031 | despacho dinâmico | polimorfismo |
| 032 | demos e testes OO | prova comportamental |

**Demo do milestone:** `Animal`/`Cachorro` imprimindo `0`, `1`, `1`.

Leitura: Tucker caps. 10–11 (funções e OO), 12 (abstração); Apêndice A.5;
*Compiladores* 6.3–6.5 (verificação de tipos).

### M5 · Entrega — até 06/12/2026

| # | Ticket | Conceito |
| --- | --- | --- |
| 033 | CLI `parse`/`check` legível | árvore como artefato |
| 034 | manual da linguagem e tutorial | comunicação técnica |
| 035 | release v1.0.0 e demo final | empacotamento |
| 036 | QA final e checklist | fechamento |

**Demo final:** rodar os programas de `examples/`, mostrar AST, erro léxico,
erro de tipo, erro de execução e polimorfismo.

## 4. Ritmo semanal sugerido

| Dia | Foco |
| --- | --- |
| Seg–Ter | tickets da trilha A (implementação) |
| Qua | trilha B (testes, CI, dívidas) |
| Qui | trilha C (documentação) + revisão de PRs |
| Sex | integração, demo do milestone, planejamento da semana |
| Sáb/Dom | folga ou recuperação de atraso |

## 5. Definição de pronto (por ticket)

- [ ] Teste novo falha antes e passa depois (ou teste de conformidade).
- [ ] `uv run pytest`, `uv run ruff check .` e `uv run mypy src` passam.
- [ ] `docs/01` atualizado quando a gramática mudou (implementação); `docs/02`
      só se o desenho-alvo da v2 mudou.
- [ ] PR preenchido com o comando de teste e o aprendizado em 3 linhas.
- [ ] Ticket movido no board: Backlog → To Do → In Progress → In Review →
      Ready for QA → In QA → Released.

## 6. Checkpoints de risco

| Data | Checkpoint | Ação se atrasar |
| --- | --- | --- |
| 21/11 | léxico pronto | cortar `docs:` não essenciais |
| 26/11 | núcleo executa um programa | cortar arrays para M3 |
| 01/12 | v1 congelada | congelar v1 e começar OO só com o essencial |
| 04/12 | OO com polimorfismo | reduzir demos a um programa |
| 06/12 | entrega | usar o buffer de QA |

## 7. O que treinar em cada conceito

| Conceito | Pergunta que você deve saber responder |
| --- | --- |
| Token × lexema | `whilea` é o quê? Por quê? |
| Maior casamento | por que `<=` não pode virar `<` `=`? |
| LL(1) | por que `else` pendente é resolvido “colando no `if` mais próximo”? |
| Precedência | por que `2 + 3 * 4` vale 14 e não 20? |
| AST × árvore de análise | por que a AST não tem nó para `;`? |
| Tabela de símbolos | por que CLite não precisa de escopo de bloco? |
| Tipos | por que `float x; x = 1;` é erro? |
| `undef` | por que ler antes de atribuir “não tem significado”? |
| Despacho dinâmico | por que `a.fala()` imprime 1 no exemplo do `Cachorro`? |
| Override × overload | qual a diferença de assinatura? |
