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
uv run pytest tests/unit/... -q   # teste do ticket
make check                        # lint + tipos + testes
make magic                        # números mágicos no código Python
```

Resultado: `__ passed` em `__ s`.

Marque cada item com evidência:

- [ ] **Comandos passaram.** Rode os três comandos e cole o resultado real; o
      `make check` precisa terminar verde.
- [ ] **O teste novo falha sem a implementação.** Desative temporariamente a
      mudança e rode o teste do ticket; ele deve falhar pelo motivo esperado,
      não por erro de import ou sintaxe. Evidência: nome do teste e mensagem.
- [ ] **Caso de erro coberto.** Localize no ticket o erro esperado (ex.:
      `E3003`, linha 4, coluna 9) e confirme que o teste verifica código, linha
      e coluna, não só o texto. Evidência: nome do teste e asserção.

## Checklist

- [ ] **Escopo:** o diff contém apenas o ticket.
      Como verificar: `git diff --stat main...HEAD` e compare com “Arquivos que
      toca” no ticket; mudança extra vira outro ticket/PR.
- [ ] **Gramática documentada:** se o parser ou a gramática mudou, `docs/01` foi
      atualizado no mesmo PR; `docs/02` só se o desenho-alvo da v2 mudou.
      Como verificar: procure `docs/01-linguagem-clite.md` no diff e confira a
      produção alterada.
- [ ] **Sem código de depuração:** não há `print`, `breakpoint`, código morto ou
      `TODO` órfão.
      Como verificar: `uv run ruff check .` e busque `print(`, `breakpoint` e
      `TODO` no diff.
- [ ] **Tipagem:** `uv run mypy src` passa sem erro.
      Como verificar: rode o comando; se o diff introduzir `Any`, confirme a
      justificativa em “Riscos e decisões”.
- [ ] **Sem números mágicos:** `make magic` passa e constantes têm nomes
      legíveis.
      Como verificar: rode o comando e revise os nomes das constantes no diff.
- [ ] **Board:** o card do ticket está em **In Review**.
      Como verificar: abra o board e confirme a coluna e o número do ticket.

## Aprendizado (3 linhas)

- O que eu entendi de novo sobre linguagens/compilação:
- O que foi mais difícil:
- O que eu testaria diferente na próxima vez:

## Riscos e decisões

- 
