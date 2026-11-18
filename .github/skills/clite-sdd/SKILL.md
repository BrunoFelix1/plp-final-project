---
name: SDD CLite
description: Usar Spec-Kit no projeto CLite com saída curta e vínculo a tickets. Use ao rodar /speckit.* ou /speckit-*, ao criar spec/plan/tasks ou ao convergir implementação.
---

# SDD CLite

Guia completo: `SPECKIT-USAGE.md`. Regra de saída: `docs/agents/sdd-conciso.md`.
Constituição: `.specify/memory/constitution.md`.

## Separador

| Ferramenta | Comando |
| --- | --- |
| Copilot | `/speckit-specify` |
| OpenCode | `/speckit.specify` |

## Fluxo

```text
specify → (clarify) → plan → (checklist) → tasks → (analyze) → implement → converge
```

## Regra de saída (obrigatória)

- Máximo 1 página por artefato.
- Tabelas/checklists em vez de prosa.
- Não repetir `docs/`, `AGENTS.md` ou ticket; citar.
- Todo artefato tem: objetivo em 1 frase, critérios verificáveis, fora de escopo
  (1–3), riscos (≤ 3) e referências.
- Ao terminar o comando, responder só: artefato, caminho, 3 bullets e próximo
  comando.

## Vínculo com o board

- Cada task aponta para um ticket `tipo: NNN` existente ou propõe um novo no
  formato de `docs/agents/ticket-format.md`.
- Antes de `/speckit.implement`, confirme ticket aprovado e `make check` verde.
- `/speckit.taskstoissues` só cria issues sem duplicata e com milestone.

## Verificação

```bash
specify integration status
ls .opencode/commands/speckit.*.md
ls .github/skills/speckit-*/SKILL.md
```
