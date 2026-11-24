# Formato de pull request

> Vale para PRs abertos por pessoas e por LLMs. O template do GitHub
> (`.github/pull_request_template.md`) espelha este arquivo.

## Regra de ouro

**Todo PR declara e executa o comando de teste.** Sem a execução, o merge na
`main` não acontece — nem para PR de documentação.

```bash
make check
```

`make check` roda `ruff check`, `mypy src` e `pytest`. Para um recorte mais
rápido durante o desenvolvimento, use o comando específico do ticket e rode
`make check` antes de pedir revisão.

## Quando o pedido é de uma LLM

1. **Rode os testes locais antes de abrir o PR**: `make check` (no Windows, os
   quatro comandos `uv run ...`).
2. Só abra o PR se os testes passarem. Se falharem, corrija ou relate; **não
   abra PR vermelho**.
3. Crie o PR com `Closes #N`, título semântico e o template abaixo.
4. Preencha o que for possível: mudanças, comando de verificação com o resultado
   real, checklist e riscos.
5. No que depender de julgamento humano (ex.: “aprendizado em 3 linhas”), escreva
   “a preencher”; não invente.
6. Mova o card para **In Review**. **Não faça merge.**

## Template

````markdown
## Ticket

Closes #N

## O que mudou

- 2 a 4 bullets, focados no comportamento, não em arquivos.

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

- Mudança de comportamento, decisão nova (D-NN) ou “Nenhum”.
````

## Regras

1. **Um ticket por PR.** Se o PR resolve dois tickets, divida.
2. **Título do PR:** mesmo formato do ticket, sem o número de issue:
   `feat: reconhecer identificadores e números inteiros`.
3. **Branch:** `tipo/NNN-slug`, criada a partir da `main` atualizada.
4. **Commits:** imperativo, em português, com o código do ticket quando útil
   (`feat: 006 adiciona scanner de identificadores`).
5. **Tamanho:** até ~400 linhas alteradas. Acima disso, justifique ou divida.
6. **Review:** pelo menos uma revisão humana. PR de LLM não aprova PR de LLM.
7. **Merge:** squash, mantendo o título do PR; a `main` precisa estar verde.
8. **Após o merge:** mover o card para **Ready for QA** e escrever no ticket o
   comando que o QA deve rodar.
9. **Itens verificáveis:** todo item de checklist deve dizer **o que conferir**
   e **como conferir**. Não use itens vagos como “tipagem ok” ou “testes ok”.

## Checklist de revisão (para quem revisa)

- [ ] O comportamento descrito no ticket está coberto por teste.
- [ ] A gramática implementada corresponde a `docs/01`/`docs/02`.
- [ ] Mensagens de erro têm código e posição.
- [ ] O PR executou o comando de teste e o resultado está colado.
- [ ] Não há regressão silenciosa em programas de `examples/`.

## PRs de documentação

Também precisam de `make check` (ele valida que nada quebrou) e do checklist.
Não precisam de teste novo, mas precisam dizer **qual documento** foi alterado e
**por quê**.

## PRs de correção (`fix:`)

Além do template, incluem:

- a entrada que reproduz o bug;
- o comportamento errado observado;
- o teste de regressão adicionado.

Se o bug veio de um caso não catalogado, adicione a linha em
`docs/06-casos-dificeis.md`.
