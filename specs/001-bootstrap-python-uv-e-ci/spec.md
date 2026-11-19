# Feature Specification: Bootstrap Python, uv e CI

**Feature Branch**: `chore/001-bootstrap-python-uv-e-ci`
**Created**: 2026-11-18 · **Status**: Ready for planning
**Ticket**: `chore: 001 - bootstrap-python-uv-e-ci` (#1)

<!--
  REGRA DO PROJETO: meta de 70 linhas; se passar de 100, seja mais conciso.
  Tabelas e checklists em vez de prosa. Explique o conceito que será implementado.
  Não repita docs/01, docs/02, AGENTS.md nem tickets. Cite.
  Leia .specify/memory/constitution.md antes de preencher.
-->

## Conceito

Ambiente reprodutível e automação de qualidade: as ferramentas de desenvolvimento
devem ser instaláveis por um comando e executadas de forma equivalente localmente
e no CI. Isso permite verificar cada fase futura do interpretador sem depender da
máquina de cada pessoa.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Validar o repositório (Priority: P1)

Como desenvolvedor, quero sincronizar o ambiente e executar a verificação de
qualidade para saber que o repositório está pronto para receber a linguagem.

**Why this priority**: todos os tickets seguintes dependem de uma base verificável.

**Independent Test**: `uv sync` seguido de `make check`.

**Acceptance Scenarios**:

1. **Given** um clone limpo, **When** a pessoa roda `uv sync`, **Then** o ambiente
   e o lockfile permitem instalar as dependências sem interação.
2. **Given** o ambiente sincronizado, **When** roda `make check`, **Then** lint,
   tipos e teste de fumaça passam.
3. **Given** um pull request para `main`, **When** o CI é acionado, **Then** ele
   repete as verificações de qualidade e testes do projeto.

---

### User Story 2 - [título] (Priority: P2)

[Opcional. Mesma estrutura, no máximo 3 histórias.]

### Edge Cases

- `uv sync --frozen` deve funcionar no CI usando o `uv.lock` versionado.
- O teste de fumaça deve falhar se o pacote raiz deixar de ser importável.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: O projeto MUST declarar Python 3.12+, dependências de desenvolvimento
  e configurações de pytest, ruff e mypy em um manifesto versionado.
- **FR-002**: O projeto MUST fornecer `make check` para executar lint, tipos e testes.
- **FR-003**: O CI MUST executar as verificações em pull requests direcionados a
  `main`, usando o lockfile.
- **FR-004**: O projeto MUST conter um teste de fumaça que importe `clite`.

### Key Entities

- **Ambiente de desenvolvimento**: conjunto versionado de ferramentas e versões
  que reproduz a validação local e remota.
- **Pipeline de qualidade**: sequência automatizada de lint, tipos e testes.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `uv sync` conclui sem erro e cria/reutiliza `.venv` a partir de
  `pyproject.toml` e `uv.lock`.
- **SC-002**: `make check` termina com código 0, executando ruff, mypy e pytest.
- **SC-003**: `.github/workflows/ci.yml` é acionado em pull requests para `main`
  e conclui as verificações sem depender de arquivos não versionados.

## Fora de escopo

- Implementar lexer, parser, AST, verificador ou interpretador.
- Publicar o pacote no PyPI ou configurar deploy.

## Assumptions e riscos

- Assume-se que o CI executa em Ubuntu e que `uv` é instalado pelo workflow.
- Risco: versões divergentes quebram a reprodução; mitigação: `uv.lock` e
  `uv sync --frozen`.
- Risco: uma ferramenta passa localmente e falha no CI; mitigação: mesmos checks
  declarados no Makefile e no workflow.

## Referências

- Ticket #1; `AGENTS.md` §3 e §5; `docs/03-arquitetura-frontend.md` §1.
- *Compiladores*, §1.2 — estrutura de um compilador e separação de fases.
