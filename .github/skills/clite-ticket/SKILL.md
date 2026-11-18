---
name: Tickets CLite
description: Criar e revisar tickets do projeto CLite no formato obrigatório, com paralelismo, labels e milestone. Use ao abrir issue por pessoa ou LLM.
---

# Tickets CLite

Formato: `docs/agents/ticket-format.md`. Board: GitHub Projects v2 do projeto.

## Passos

1. Procure duplicata:
   ```bash
   gh issue list --repo BrunoFelix1/plp-final-project --search "termo"
   gh issue list --repo BrunoFelix1/plp-final-project --state all --limit 100
   ```
2. Escolha o próximo `NNN` livre (ordem de implementação, não reutilize).
3. Defina tipo (`feat:`, `fix:`, `docs:`, `chore:`) e slug curto.
4. Preencha o template: objetivo, conceito, pronto quando, verificação,
   paralelismo, fora de escopo, depende de, leitura.
5. Crie com `--body-file`:
   ```bash
   gh issue create --repo BrunoFelix1/plp-final-project \
     --title "feat: 006 - reconhecer identificadores" \
     --body-file /tmp/ticket.md \
     --label feat --label lexer --label size/S \
     --milestone "M1 · Fundação e léxico"
   ```
6. Adicione ao board e deixe em **Backlog**.
7. Atualize o milestone conforme `docs/04-plano-de-aprendizado.md`.

## Checklist antes de abrir

- [ ] Cabe em 1–2 h.
- [ ] 3–5 itens em “Pronto quando”.
- [ ] Nomeia o conceito implementado e cita ao menos um livro com seção.
- [ ] Se muda a gramática, `docs/01` está no “Pronto quando”.
- [ ] Comando de verificação executável.
- [ ] Caso de erro coberto.
- [ ] Paralelismo e arquivos tocados declarados.
- [ ] Dependências com `#N`.
- [ ] Sem pontos de história.

## Regras do board

- Ticket novo: **Backlog**.
- `ready-for-agent`/`ready-for-human` só após leitura humana.
- In Review = PR aberto; Ready for QA = merge; In QA = em verificação;
  Released = demonstrado.
