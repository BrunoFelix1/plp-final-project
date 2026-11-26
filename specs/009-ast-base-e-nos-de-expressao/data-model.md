# Data Model: AST base e nós de expressão

Meia página. Entidade única: **Nó** — unidade imutável da árvore, com campos de
domínio + `line: int = 0` + `column: int = 0`. Composição forma a árvore; sem
estado, sem transições.

## Nós (`src/clite/ast/nodes.py`, todos `frozen=True`)

| Nó | Campos | Origem §6 |
| --- | --- | --- |
| `Program` | `declarations: list[Declaration]`, `commands: list[Command]` | Programa(declarações, comandos) |
| `VarDecl` | `name: str`, `type: CliteType` | VarDecl(nome, tipo) |
| `ArrayDecl` | `name: str`, `type: CliteType`, `size: int` | ArrayDecl(nome, tipo, tamanho) |
| `Skip` | — | Skip |
| `Block` | `commands: list[Command]` | Bloco(Comandos) |
| `Assign` | `target: VarRef \| ArrayRef`, `source: Expression` | Atribuição(alvo, fonte) |
| `If` | `test: Expression`, `then: Command`, `else_branch: Command \| None = None` | Condicional(teste, então, senão?) |
| `While` | `test: Expression`, `body: Command` | Laço(teste, corpo) |
| `VarRef` | `name: str` | VarRef(nome) |
| `ArrayRef` | `name: str`, `index: Expression` | ArrayRef(nome, índice) |
| `Binary` | `op: str`, `left: Expression`, `right: Expression` | Binário(op, esq, dir) |
| `Unary` | `op: str`, `operand: Expression` | Unário(op, termo) |
| `Convert` | `target_type: CliteType`, `operand: Expression` | Conversão(tipo, termo) |
| `IntLiteral` / `FloatLiteral` / `BoolLiteral` / `CharLiteral` | `value: int / float / bool / str` | IntValor…CharValor |

## Aliases de união (só tipos)

- `CliteType = Literal["int", "float", "char", "bool"]`
- `Declaration = VarDecl | ArrayDecl`
- `Command = Skip | Block | Assign | If | While`
- `Expression = VarRef | ArrayRef | Binary | Unary | Convert | IntLiteral | FloatLiteral | BoolLiteral | CharLiteral`

## Regras de validação

- Nenhuma em runtime: tipos garantidos estaticamente (`mypy --strict`); a
  semântica valida nomes, índices e conversões depois (D-07 é regra do checker).
- Igualdade: estrutural, recursiva (dataclass `eq`).
- Imutabilidade: qualquer atribuição levanta `FrozenInstanceError`.
