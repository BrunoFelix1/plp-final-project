# Jornadas

Roteiros guiados para conhecer e evoluir o projeto. Cada jornada é um HTML
autocontido: abre no navegador, não precisa de servidor e salva o progresso e as
anotações no `localStorage`.

| Jornada | Tempo | Para quem | Arquivo |
| --- | --- | --- | --- |
| Jornada inicial do desenvolvedor | 30 min | quem acabou de entrar no projeto | [`jornada-inicial-desenvolvedor.html`](jornada-inicial-desenvolvedor.html) |

## Como usar

```bash
xdg-open jornadas/jornada-inicial-desenvolvedor.html   # Linux
open jornadas/jornada-inicial-desenvolvedor.html       # macOS
```

- Marque cada passo; o medidor no topo mostra o progresso.
- Use **Anotar** para registrar o que não bateu ou o que quer investigar depois.
- O botão **Desmarcar tudo** limpa passos e anotações deste navegador.
- Os links abrem o board e os documentos renderizados no GitHub.

## O que a jornada inicial cobre

1. Contexto: o que é CLite, por que o projeto existe e qual é o pipeline.
2. Mapa do repositório: onde cada fase mora e onde procurar.
3. Board e milestones: colunas, 36 tickets, prazos e trabalho paralelo.
4. Conceitos: tokens, gramática, AST, tipos, semântica e OO, incluindo a regra
   de que a gramática implementada em `docs/01` é atualizada em cada ticket OO.
5. Método: como aprender enquanto implementa (ritual, ticket, PR, pronto).
6. Primeiro movimento: escolher ticket, criar branch e definir as próximas 2 h.

## Criar uma nova jornada

1. Copie `jornada-inicial-desenvolvedor.html` para `jornadas/<slug>.html`.
2. Troque o `storageKey` no objeto `GUIDE` (ex.: `clite-jornada-lexer-v1`).
3. Ajuste `scenes`: cada passo é `[id, ação, “você vê”, opcional]`.
4. Mantenha o tempo total explícito no topo e uma média de 1–2 min por passo.
5. Adicione a nova linha na tabela acima e linke no `README.md` se for pública.
