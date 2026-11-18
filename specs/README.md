# Specs (Spec-Driven Development)

Cada feature especificada com `/speckit.specify` (Copilot) ou
`/speckit.specify` (OpenCode) cria uma pasta aqui:

```text
specs/
└── 001-lexer-basico/
    ├── spec.md
    ├── plan.md
    ├── tasks.md
    └── converge.md
```

## Regras

- Nome em kebab-case, prefixo numérico na ordem de implementação.
- Spec, plano e tasks com **no máximo 1 página** cada
  (`docs/agents/sdd-conciso.md`).
- Cada task aponta para um ticket `tipo: NNN` do board ou propõe um novo no
  formato de `docs/agents/ticket-format.md`.
- Não repita a gramática de `docs/01`/`docs/02`; referencie.
- A spec não substitui o ticket: ela explica o quê e por quê; o ticket recorta a
  fatia verificável.

## Fluxo

```text
/speckit.specify → /speckit.plan → /speckit.tasks → /speckit.implement → /speckit.converge
```

Guia completo: `SPECKIT-USAGE.md`.
