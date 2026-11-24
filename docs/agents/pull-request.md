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
uv run pytest tests/unit/test_xxx.py -q   # teste do ticket
make check                                # suíte completa
```

Resultado: `__ passed` em `__ s`.

- [ ] Executei o comando acima e todos os testes passaram.
- [ ] O teste novo falha sem a implementação (quando aplicável).
- [ ] O caso de erro foi verificado (código + linha/coluna).

## Checklist

- [ ] O PR implementa **apenas** o ticket (sem melhorias de passagem).
- [ ] `docs/01` atualizado quando a gramática mudou; `docs/02` se o desenho-alvo
      da v2 mudou.
- [ ] Sem `print` de depuração, código morto ou `TODO` órfão.
- [ ] Sem números mágicos no código Python (`make magic`).
- [ ] Tipagem em `src/` sem `Any` injustificado.
- [ ] Ticket movido para **In Review** no board.

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
