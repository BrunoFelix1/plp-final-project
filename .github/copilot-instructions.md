# Instruções para GitHub Copilot

Leia `AGENTS.md` e os documentos de `docs/` antes de sugerir código. Este
repositório implementa a linguagem **CLite** (Tucker e Noonan) em Python,
seguindo as fases do front-end do Apêndice A de *Compiladores*.

## Regras que não podem ser violadas

1. **Gramática é contrato.** `docs/01-linguagem-clite.md` e
   `docs/02-extensao-oo.md` são a fonte da verdade. Mudança de gramática
   atualiza o documento no mesmo PR.
2. **Sem dependências de runtime.** Python 3.12+ e biblioteca padrão. O parser
   é escrito à mão.
3. **Tipagem estrita** em `src/` (`mypy --strict`), lint com `ruff`.
4. **Teste primeiro.** Todo comportamento novo tem teste; erros são verificados
   por código (`E1xxx`–`E4xxx`), linha e coluna.
5. **Uma fase por vez.** `lexer → parser → ast → semantic → interpreter`. Não
   antecipe OO antes de a v1 estar verde.
6. **Tickets pequenos.** Formato em `docs/agents/ticket-format.md`; PR em
   `docs/agents/pull-request.md`, sempre com `make check` executado.
7. **Saída SDD curta.** Specs, planos e tasks gerados por `/speckit-*` têm no
   máximo 1 página, em tabelas/checklists.

## Comandos

```bash
uv sync
uv run pytest -q
uv run ruff check . && uv run mypy src
make check
```

## Onde cada coisa vive

| Assunto | Arquivo |
| --- | --- |
| gramática v1 | `docs/01-linguagem-clite.md` |
| gramática v2 (OO) | `docs/02-extensao-oo.md` |
| arquitetura e mapa do Apêndice A | `docs/03-arquitetura-frontend.md` |
| cronograma e milestones | `docs/04-plano-de-aprendizado.md` |
| decisões | `docs/05-decisoes.md` |
| casos difíceis | `docs/06-casos-dificeis.md` |
| agentes | `.github/agents/` |
| skills | `.github/skills/` |

## Estilo

- Mensagens e comentários em português; identificadores em inglês.
- Funções pequenas, nomes explícitos, sem abreviações obscuras.
- Nada de `eval`, `exec`, `print` de depuração ou código morto.
- Explique o conceito no PR em 3 linhas: o objetivo é aprender.
