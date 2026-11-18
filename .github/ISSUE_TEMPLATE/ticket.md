---
name: Ticket CLite
about: Ticket pequeno e verificável, no formato do projeto (pessoa ou LLM)
title: "feat: NNN - "
labels: []
assignees: []
---

<!--
  Formato obrigatório: docs/agents/ticket-format.md
  Título: tipo: NNN - slug (feat, fix, docs, chore)
  Máximo ~15 linhas de prosa. Se não couber em 1–2 h, divida.
-->

## Objetivo

<!-- O que passa a funcionar e por quê, em 1–2 frases. -->

## Conceito

**Conceito implementado:** <!-- nome do conceito -->
<!-- 2–4 linhas: o que é, por que importa e o que este ticket concretiza. -->

## Pronto quando

- [ ] Comportamento observável 1.
- [ ] Comportamento observável 2.
- [ ] Caso de erro com código e linha.
- [ ] `make check` verde.

## Verificação técnica

```bash
uv run pytest tests/... -q
make check
```

## Paralelismo

- **Pode rodar em paralelo com:** <!-- feat: NNN ... ou "Nenhum" -->
- **Não rode junto de:** <!-- feat: NNN (motivo) -->
- **Arquivos que toca:** <!-- caminhos -->

## Fora de escopo

<!-- 1–3 itens -->

## Depende de

<!-- #N — ou "Nenhum" -->

## Leitura

<!-- Pelo menos uma referência de livro com capítulo/seção: Tucker e Noonan §..., Compiladores §... -->
<!-- Referências internas: docs/01 §..., docs/02 §..., docs/06 §... -->
