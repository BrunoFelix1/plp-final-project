# Documentação do projeto

Comece por aqui. A ordem abaixo também é a ordem de leitura sugerida para quem
vai implementar ou revisar.

| Documento | Para quê |
| --- | --- |
| [01-linguagem-clite.md](01-linguagem-clite.md) | gramática, tokens, precedência, tipos e semântica da v1 — **fonte da verdade** |
| [02-extensao-oo.md](02-extensao-oo.md) | gramática, tipos e modelo de execução da v2 (classes, herança, polimorfismo, override) |
| [03-arquitetura-frontend.md](03-arquitetura-frontend.md) | fases, pacotes, mapa do Apêndice A (Java) para Python, erros, CLI e testes |
| [04-plano-de-aprendizado.md](04-plano-de-aprendizado.md) | cronograma, milestones, trilhas paralelas e ritual de estudo |
| [05-decisoes.md](05-decisoes.md) | ADRs resumidos: o que foi decidido, alternativas e o que ainda precisa de confirmação |
| [06-casos-dificeis.md](06-casos-dificeis.md) | catálogo de entradas traiçoeiras e o comportamento esperado |
| [agents/ticket-format.md](agents/ticket-format.md) | formato obrigatório de ticket (humano ou LLM) |
| [agents/pull-request.md](agents/pull-request.md) | formato obrigatório de pull request |
| [agents/sdd-conciso.md](agents/sdd-conciso.md) | regra de saída curta para todos os comandos do Spec-Kit |

## Regra de manutenção

1. Mudou a gramática? Atualize `01` (gramática **implementada**) **no mesmo PR**
   que o parser. `02` só muda se o desenho-alvo da v2 mudar.
2. Tomou uma decisão nova? Adicione um `D-NN` em `05`.
3. Descobriu um caso difícil? Adicione em `06` e crie o teste.
4. Ticket e PR seguem os formatos de `agents/`; o CI e a revisão cobram isso.

## Jornadas

- [Jornada inicial do desenvolvedor](../jornadas/jornada-inicial-desenvolvedor.html)
  — 30 min, HTML interativo com progresso e anotações locais.
