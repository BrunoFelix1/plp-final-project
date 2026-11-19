# Constituição do CLite

**Versão:** 1.1.0 · **Ratificada em:** 17/11/2026 · **Última emenda:** 18/11/2026

Projeto acadêmico de um interpretador para a linguagem CLite, em Python, com
extensão orientada a objetos. Esta constituição vale para toda spec, plano e
implementação; um plano que a violar precisa registrar a violação e justificá-la.

## Princípios

### I. Aprendizado primeiro (NÃO NEGOCIÁVEL)

Toda decisão prioriza o entendimento do desenvolvedor. Código precisa ser
legível, dividido por fase e acompanhado do conceito que exercita. Otimização de
desempenho e esperteza sintática não são objetivos.

### II. Fidelidade à gramática documentada

`docs/01-linguagem-clite.md` e `docs/02-extensao-oo.md` são a fonte da verdade.
Nenhuma implementação pode divergir sem que o documento mude no mesmo PR.
Mudança de gramática sempre precede o código que a implementa.

### III. Fatias verticais pequenas

Cada incremento cabe em um ticket e em um PR revisável, com a `main` sempre
verde. É proibido acumular léxico, parser e interpretador em um único PR. O
trabalho paralelo é explicitamente declarado nos tickets.

### IV. Teste como especificação

Todo comportamento novo tem teste que falha antes e passa depois. Programas
`.clite` de conformidade provam a linguagem de ponta a ponta. Casos de erro são
testados por código, linha e coluna.

### V. Python padrão, tipado e sem dependências de runtime

Python 3.12+, biblioteca padrão apenas. `mypy --strict` em `src/`, `ruff` para
estilo, `pytest` para testes. Nenhuma biblioteca de parser ou lexer: a graça é
construir o front-end.

### VI. Escopo controlado

A v1 (núcleo) precisa estar completa e verde antes da v2 (OO). A v2 cobre
classes, herança, polimorfismo e sobreescrita, e nada além: sem classe abstrata,
reflexão, construtores, sobrecarga, `null` ou funções de topo sem emenda nesta
constituição.

### VII. Documentação operacional

Tickets e PRs seguem `docs/agents/ticket-format.md` e
`docs/agents/pull-request.md`. Todo PR declara e executa o comando de teste.

## Princípios técnicos

Estes princípios complementam os princípios I–VII e têm prioridade sobre
preferências de estilo. Em caso de conflito, vale o mais restritivo.

### T0. Regra de ouro: edição cirúrgica (P0)

- É **proibido** reformatar linhas de código existentes.
- É **proibido** ajustar espaços, indentação ou quebrar linhas que já existiam.
- Altere **apenas** as linhas estritamente necessárias para a nova funcionalidade.
- Se a ferramenta sugerir mudanças estéticas colaterais, **cancele** e use uma
  edição menor e mais precisa.
- Apenas linhas novas ou alteradas podem ser formatadas, respeitando **80 a 100
  colunas** (o projeto usa 100; ver `pyproject.toml`).
- Prefira substituições pequenas e exatas para preservar o código existente.

Esta regra tem prioridade **P0** e vale para todos os arquivos do projeto.

### T1. SOLID e qualidade de código

- **SRP:** uma razão para mudar; responsabilidade focada e baixo acoplamento.
- **OCP:** estenda por abstração; aberto para extensão, fechado para modificação.
- **LSP:** subtipos substituíveis sem quebrar contratos.
- **ISP:** interfaces focadas; o cliente não depende do que não usa.
- **DIP:** dependa de abstrações, não de implementações concretas.

Requisitos de código:

- Python 3.12+; use `@dataclass(frozen=True)` quando o dado for imutável.
- Contratos com `Protocol` ou ABC e injeção por parâmetro; evite herança
  profunda e metaclasses.
- Sem threads ou concorrência no interpretador: a execução é single-threaded.
- Use geradores e compreensões quando deixarem o código mais legível; não force.
- Padrões de projeto só quando esclarecerem o porquê; explique a escolha no PR.
- **DRY:** procure função existente antes de criar outra.
- **KISS:** evite over-engineering.
- **80–100 colunas** por linha; nunca reformate linhas existentes (T0).
- Métodos com no máximo 20 linhas e nomes que revelam intenção.
- Comentários explicam **por quê**, não **o quê**.
- Complexidade ciclomática <10; aninhamento ≤3; sem duplicação.

**Onde isso é crítico:** `src/clite/lexer`, `parser`, `ast`, `semantic` e
`interpreter`. Antes de criar uma função, procure no módulo da fase e em
`symbols.py`, `types.py`, `values.py` e `errors.py`. As fronteiras entre fases
estão em `docs/03-arquitetura-frontend.md`.

Exemplos mínimos em Python:

```python
from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True)
class Report:
    data: bytes

class PDFExporter:
    def export(self, report: Report) -> bytes: ...

class Discount(Protocol):
    def apply(self, value: float) -> float: ...

class VIPDiscount:
    def apply(self, value: float) -> float: ...

class Checkout:
    def __init__(self, discount: Discount) -> None:
        self._discount = discount
```

### T2. TDD: Red–Green–Refactor

Ciclo obrigatório:

1. **RED:** escreva o teste que falha antes de implementar. Sem teste falhando,
   não há implementação.
2. **GREEN:** implemente o mínimo para passar, sem refatorar.
3. **REFACTOR:** melhore com SOLID e as métricas de T1, mantendo os testes
   verdes.

Cobertura: **80% mínimo** e **100% nos caminhos críticos** (maior casamento,
precedência, regras A.1–A.6, limites de array e despacho dinâmico).

Tipos de teste:

- **Unidade:** lógica isolada, um comportamento por teste;
- **Conformidade:** programas `.clite` de ponta a ponta com saída esperada;
- **Erros:** código, linha e coluna esperados.

Ferramentas: `pytest`, `pytest-cov` e `Hypothesis`. Não há suíte E2E de web nem
containers: o produto é um interpretador de linha de comando. Os testes rodam em
sequência e devem ser rápidos; concorrência não é requisito.

Estrutura da task:

- **RED:** teste nomeado `test_<comportamento>_quando_<condição>`, ligado ao
  “Pronto quando” do ticket.
- **GREEN:** código mínimo; sem refatoração.
- **REFACTOR:** checklist de T1; sem mudar comportamento.

O formato do ticket e o ritual de aprendizado estão em
`docs/agents/ticket-format.md` e `docs/04-plano-de-aprendizado.md`.

## Saída de comandos SDD

Specs, planos, tasks, checklists e relatórios gerados por comandos SDD devem ser
**sucintos, resumidos e objetivos**: meta de 70 linhas por artefato; se passar
de 100, seja mais conciso, em tabelas e checklists em vez de prosa, sem repetir
`docs/`, `AGENTS.md` ou tickets. Explique o conceito que está sendo implementado.

## Restrições técnicas

- Sem dependências de runtime; dependências de desenvolvimento ficam no grupo
  `dev` do `pyproject.toml`.
- Erros sempre com código (`E1xxx`–`E4xxx`), linha e coluna, em português.
- Nós da AST são dados; checagem e avaliação ficam em visitantes.
- O fluxo é unidirecional: `lexer → parser → ast → semantic → interpreter`.
- Linhas novas ou alteradas: **80–100 colunas**. Linhas existentes não são
  reformatadas (T0).
- Testes com `pytest`; cobertura mínima de 80% e 100% nos caminhos críticos
  (T2). Sem threads ou concorrência no interpretador.

## Fluxo de desenvolvimento

1. Ticket pequeno no board, com objetivo, conceito e verificação.
2. Branch `tipo/NNN-slug` e `specify` antes de codar (AGENTS.md §5).
3. **RED → GREEN → REFACTOR** (T2).
4. `make check` verde, incluindo lint, tipos e testes.
5. PR no formato do projeto, com `Closes #N` e comando de teste executado.
6. Revisão humana; merge squash; card para QA.

## Governança

- Emendas exigem PR que atualize esta constituição e registre a justificativa.
- Enquanto o projeto for acadêmico, o mantenedor do repositório aprova emendas.
- Decisões técnicas que afetam a linguagem também viram `D-NN` em
  `docs/05-decisoes.md`.
