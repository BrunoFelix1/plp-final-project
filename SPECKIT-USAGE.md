# Como usar Spec-Kit (SDD) neste projeto

> Spec-Kit é a ferramenta de **Spec-Driven Development** (SDD) usada aqui.
> Versão instalada: **v1.0.10**. Este documento é o guia do projeto CLite.

## 1. O separador muda por ferramenta

| Ferramenta | Separador | Exemplo |
| --- | --- | --- |
| GitHub Copilot | hífen (`-`) | `/speckit-specify` |
| OpenCode | ponto (`.`) | `/speckit.specify` |
| Claude Code | ponto (`.`) | `/speckit.specify` |

- O Copilot usa *skills* em `.github/skills/`, cujo nome exige hífen.
- O OpenCode usa comandos em `.opencode/commands/`, instalados com ponto.
- Não renomeie os comandos do OpenCode: eles se referenciam com ponto.

As duas integrações estão instaladas. `specify integration status` reporta
`unsafe-multi-install` por limitação do manifest do Copilot; os comandos
funcionam normalmente.

## 2. O que está instalado

| Item | Local |
| --- | --- |
| Constituição | `.specify/memory/constitution.md` |
| Templates | `.specify/templates/` |
| Scripts | `.specify/scripts/bash/` |
| Comandos OpenCode | `.opencode/commands/speckit.*.md` |
| Skills Copilot | `.github/skills/speckit-*/SKILL.md` |
| Artefatos por feature | `specs/<NNN>-<slug>/` |

## 3. Comandos

| Copilot | OpenCode | Para quê | Quando |
| --- | --- | --- | --- |
| `/speckit-constitution` | `/speckit.constitution` | criar/revisar princípios | uma vez, ou ao mudar regra do projeto |
| `/speckit-specify` | `/speckit.specify` | especificação da feature | antes de planejar |
| `/speckit-clarify` | `/speckit.clarify` | perguntas de desambiguação | opcional, antes do plano |
| `/speckit-plan` | `/speckit.plan` | plano técnico | depois da spec |
| `/speckit-checklist` | `/speckit.checklist` | checklist de qualidade | opcional |
| `/speckit-tasks` | `/speckit.tasks` | tasks acionáveis | depois do plano |
| `/speckit-analyze` | `/speckit.analyze` | consistência entre artefatos | antes de implementar |
| `/speckit-implement` | `/speckit.implement` | executar tasks | com ticket aprovado |
| `/speckit-converge` | `/speckit.converge` | ver o que falta | iterativo |
| `/speckit-taskstoissues` | `/speckit.taskstoissues` | transformar tasks em issues | quando as tasks virarem tickets |

## 4. Fluxo recomendado

```text
1. /speckit-specify     → descreva o comportamento desejado (sem código)
2. /speckit-clarify     → opcional, se houver ambiguidade
3. /speckit-plan        → plano técnico curto
4. /speckit-tasks       → checklist de tasks
5. /speckit-analyze     → opcional, checa consistência
6. /speckit-implement   → implementa, com teste
7. /speckit-converge    → confirma o que falta
```

O fluxo SDD **não substitui** o board. Cada task gerada deve apontar para um
ticket (`feat: NNN`) ou propor um novo no formato de
[`docs/agents/ticket-format.md`](docs/agents/ticket-format.md).

## 5. Regra de saída curta (obrigatória)

Todo artefato gerado por comando SDD deve ser **sucinto, resumido e objetivo**:
tabelas em vez de prosa, no máximo 1 página por artefato, sem repetir o que já
está no repositório. A regra completa está em
[`docs/agents/sdd-conciso.md`](docs/agents/sdd-conciso.md) e vale também para os
templates em `.specify/templates/`.

## 6. Estrutura dos artefatos

```text
specs/
└── 001-lexer-basico/
    ├── spec.md        # /speckit.specify
    ├── plan.md        # /speckit.plan
    ├── tasks.md       # /speckit.tasks
    └── converge.md    # /speckit.converge
```

Nomes em kebab-case, prefixo numérico na ordem de implementação. O número da
spec **não** precisa coincidir com o número do ticket, mas o vínculo deve
aparecer nos dois arquivos.

## 7. Exemplo aplicado ao CLite

```text
Você: /speckit.specify
"Quero que o lexer reconheça identificadores, inteiros, floats, booleanos e
char, com linha e coluna, usando maior casamento. Palavras reservadas não podem
ser identificadores."

Resultado: specs/001-lexer-basico/spec.md (≤ 1 página)
```

```text
Você: /speckit.plan

Resultado: plan.md com módulos, contratos Token/Lexer, estratégia de teste,
riscos e critérios de aceite — sem repetir docs/01.
```

```text
Você: /speckit.tasks

Resultado: checklist com IDs, arquivos e teste de cada task.
```

## 8. Constituição do projeto

O arquivo `.specify/memory/constitution.md` fixa os princípios que todo plano
deve respeitar:

1. aprendizado primeiro;
2. fidelidade à gramática documentada;
3. fatias verticais pequenas com `main` verde;
4. teste antes/depois em todo incremento;
5. Python padrão, sem dependência de runtime;
6. escopo controlado (OO limitado ao combinado).

Se um plano violar um princípio, o comando de plano deve registrar a violação e
justificar. Violação sem justificativa = plano recusado.

## 9. Solução de problemas

| Sintoma | Causa provável | Ação |
| --- | --- | --- |
| `/speckit.*` não aparece no OpenCode | comando não instalado | `specify integration status` e `specify integration install opencode --force` |
| `/speckit-*` não aparece no Copilot | skill ausente | `specify integration install copilot --force` |
| `unsafe-multi-install` | manifest do Copilot | ignorar; os comandos funcionam |
| `managed-files-modified` | templates do projeto foram enxugados de propósito | não rode `specify integration upgrade --force`; preserve os templates locais |
| Scripts falham no Windows | scripts Bash | use WSL/Git Bash ou rode os comandos manualmente |
| Artefato muito longo | template antigo | use os templates atuais e a regra de saída curta |

## 10. Documentação oficial

- <https://github.github.io/spec-kit/>
- <https://github.github.io/spec-kit/quickstart.html>
- <https://github.github.io/spec-kit/reference/agentic-sdd.html>

**Versão deste guia:** 1.0 · **Atualizado:** 17/11/2026
