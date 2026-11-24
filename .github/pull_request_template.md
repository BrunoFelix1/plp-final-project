<!-- Formato obrigatório: docs/agents/pull-request.md -->
<!-- LLM: rode `make check` antes de abrir; preencha o que for possível;
     use "a preencher" no que depender de julgamento humano. -->

## Ticket

Closes #

## O que mudou

- 
- 

## Como verificar

```bash
uv run pytest
make check
```

Resultado: `__ passed` em `__ s`.

- [ ] Executei o comando acima e todos os testes passaram.
- [ ] O teste novo falha sem a implementação (quando aplicável).
- [ ] O caso de erro foi verificado (código + linha/coluna).

## Checklist

- [ ] O PR implementa **apenas** o ticket.
- [ ] `docs/01` atualizado quando a gramática mudou; `docs/02` se o desenho-alvo
      da v2 mudou.
- [ ] Sem `print` de depuração, código morto ou `TODO` órfão.
- [ ] Sem números mágicos (`make magic`).
- [ ] Tipagem em `src/` sem `Any` injustificado.
- [ ] Ticket movido para **In Review** no board.

## Aprendizado (3 linhas)

- O que eu entendi de novo sobre linguagens/compilação:
- O que foi mais difícil:
- O que eu testaria diferente na próxima vez:

## Riscos e decisões

- 
