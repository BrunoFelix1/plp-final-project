# Formato de ticket

> Vale para tickets abertos por pessoas e por LLMs. O `@ticket-writer` e a
> skill `clite-ticket` usam este arquivo como única fonte do formato.

Um ticket existe para uma pessoa conseguir **ler, entender, implementar e
verificar** um incremento pequeno. Se não cabe em uma sessão de 1–2 h, divida.

## Template

````markdown
<!-- Título: <tipo>: <NNN> - <slug em minúsculas> -->

## Objetivo

Uma ou duas frases: o que passa a funcionar e por quê.

## Conceito

**Conceito implementado:** [nome do conceito, ex.: “maior casamento”].
[2–4 linhas: o que é, por que importa e o que este ticket concretiza.]
É a parte que o desenvolvedor deve conseguir explicar em voz alta.

## Pronto quando

- [ ] Comportamento observável 1.
- [ ] Comportamento observável 2.
- [ ] Caso de erro coberto com código e linha.
- [ ] `make check` verde.

## Verificação técnica

```bash
uv run pytest tests/unit/test_xxx.py -q   # teste do ticket
make check                                # suíte completa
```

- [ ] O teste novo falha antes da implementação.
- [ ] O caso de erro é verificado por código e posição.

## Paralelismo

- **Pode rodar em paralelo com:** `feat: 006`, `feat: 007` (arquivos disjuntos).
- **Não rode junto de:** `feat: 010` (mesmo `parser.py`).
- **Arquivos que toca:** `src/clite/lexer/tokens.py`, `tests/unit/test_tokens.py`.

## Fora de escopo

- O que este ticket não entrega (1–3 itens).

## Depende de

- #N (`feat: 005 - ...`) — ou “Nenhum”.

## Leitura

- Tucker e Noonan, §2.3.1 — Sintaxe Léxica.
- *Compiladores*, §3.4 — Reconhecimento de tokens (opcional).
- `docs/01-linguagem-clite.md` §4.
````

## Regras

1. **Título:** `<tipo>: <NNN> - <slug>`, com `feat:`, `fix:`, `docs:` ou
   `chore:`. O número é a ordem de implementação e nunca é reutilizado.
2. **Tamanho:** até ~15 linhas de prosa. Checklist com 3–5 itens em “Pronto
   quando”. Se precisar de mais, divida.
3. **Um requisito por ticket.** “Implementar o interpretador” não é ticket;
   “avaliar expressões binárias” é.
4. **Conceito e leitura obrigatórios:** todo ticket nomeia o conceito
   implementado (2–4 linhas) e cita **pelo menos uma referência de livro** com
   capítulo e seção. Sem isso, o ticket não está pronto para implementar.
5. **Verificação explícita:** sempre um comando que a pessoa consegue rodar e um
   resultado esperado.
6. **Paralelismo obrigatório:** diga com quais tickets pode rodar junto e quais
   arquivos toca. Se houver dúvida, assuma que **não** pode.
7. **Sem pontos de história** e sem estimativa em horas. O tamanho é `size/S`
   (até ~2 h) ou `size/M` (até ~4 h); tickets `M` devem ser candidatos a split.
8. **Sem copiar conteúdo do repositório.** Referencie `docs/01`, `docs/02`,
   `docs/06` e o livro.
9. **Idioma:** português, presente, concreto. Identificadores técnicos podem
   aparecer no corpo técnico.
10. **Mudou a gramática?** Inclua em “Pronto quando” a atualização de `docs/01`
    no mesmo PR. Em ticket de OO, isso é obrigatório: a gramática implementada
    não pode ficar atrás do parser.

## Labels

| Grupo | Valores |
| --- | --- |
| Tipo | `feat`, `fix`, `docs`, `chore` |
| Área | `lexer`, `parser`, `ast`, `types`, `interpreter`, `oo`, `infra`, `docs` |
| Tamanho | `size/S`, `size/M` |
| Fluxo | `ready-for-agent`, `ready-for-human` |

## Fluxo no board

```text
Backlog → To Do → In Progress → In Review → Ready for QA → In QA → Released
```

- Todo ticket nasce em **Backlog**.
- Só entra em **To Do** depois que uma pessoa leu o objetivo e o “Pronto
  quando” e marcou `ready-for-agent` ou `ready-for-human`.
- **In Review** = PR aberto; **Ready for QA** = merge na `main`; **In QA** =
  alguém está executando o roteiro; **Released** = verificado e demonstrado.

## Exemplo (resumido)

```markdown
<!-- Título: feat: 006 - reconhecer identificadores e números inteiros -->

## Objetivo

Fazer o lexer transformar `abc`, `abc123` e `42` nos tokens corretos, com linha
e coluna, para que o parser possa consumi-los.

## Conceito

**Conceito implementado:** maior casamento. O lexer sempre consome a maior
sequência válida; por isso `whilea` é identificador, não palavra-chave seguida
de identificador. Isso evita depender de espaço em branco para separar tokens.

## Pronto quando

- [ ] `abc` → `IDENTIFIER("abc")`.
- [ ] `abc123` → `IDENTIFIER("abc123")`.
- [ ] `42` → `INT_LITERAL(42)`.
- [ ] `12a` → erro léxico `E1002` na coluna do `a`.

## Verificação técnica

```bash
uv run pytest tests/unit/lexer/test_identifiers.py -q
```

## Paralelismo

- **Pode rodar em paralelo com:** `feat: 007` (outro arquivo do lexer).
- **Arquivos que toca:** `src/clite/lexer/lexer.py`, `tests/unit/lexer/`.

## Fora de escopo

- Números float, palavras reservadas e operadores.

## Depende de

- #12 (`feat: 005 - tokens e palavras reservadas`).

## Leitura

- Tucker e Noonan, §2.3.1 — Sintaxe Léxica.
- Compiladores, §3.4 — Reconhecimento de tokens.
- `docs/01-linguagem-clite.md` §4.
```
