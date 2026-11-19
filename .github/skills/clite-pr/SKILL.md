---
name: Pull Requests CLite
description: Abrir e revisar pull requests do CLite no formato do projeto, sempre com o comando de teste executado. Use antes de criar ou aprovar um PR.
---

# Pull Requests CLite

Formato: `docs/agents/pull-request.md`.

## Regra obrigatória

Todo PR executa e reporta:

```bash
make check
```

Sem o resultado, não há merge — nem em PR de documentação.

## Passos

1. Atualize a `main` e crie a branch `tipo/NNN-slug`.
2. **Antes de abrir, rode os testes locais**: `make check` (no Windows, os
   comandos `uv run` equivalentes). Se falhar, não abra o PR.
3. Preencha o template com o que for possível:
   - `Closes #N`
   - o que mudou (2–4 bullets de comportamento)
   - como verificar + resultado real (`__ passed`)
   - checklist
   - rascunho do aprendizado em 3 linhas, marcado para revisão humana
   - riscos/decisões
4. Abra:
   ```bash
   gh pr create --repo BrunoFelix1/plp-final-project \
     --title "feat: reconhecer identificadores" \
     --body-file /tmp/pr.md --base main
   ```
5. Mova o card para **In Review**.
6. Após merge: **Ready for QA**, com o comando de QA no ticket.

O que depender de julgamento humano deve ficar como “a preencher”; não invente.

## Checklist de revisão

- [ ] Cobre o “Pronto quando” do ticket.
- [ ] Teste novo falha sem a implementação.
- [ ] Erros com código + linha/coluna.
- [ ] Gramática e docs atualizados juntos.
- [ ] Sem código morto, `TODO` órfão ou `Any` injustificado.
- [ ] Sem regressão nos programas de `examples/`.
- [ ] Comando de teste colado no PR.

## Proibições

- PR com dois tickets.
- Merge com CI vermelho.
- Aprovar PR de LLM sem revisão humana.
