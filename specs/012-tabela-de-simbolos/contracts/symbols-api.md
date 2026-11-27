# Contrato de API: `clite.symbols` (ticket 012)

Contrato interno (biblioteca Python, sem interface externa). Consumidores
previstos: `clite.semantic.checker` (#13/#14) e testes unitários.

## Erro

```python
class SemanticError(Exception):
    code: str      # "E3001" | "E3002" (constantes nomeadas no módulo)
    line: int      # 1-based; 0 = não informado
    column: int    # 1-based; 0 = não informado
    message: str   # em português, uma linha

    def __init__(self, line: int, column: int, message: str, code: str) -> None:
        # code é obrigatório: cada gatilho tem código específico (E3001, E3002).
        # str(erro) == f"erro {code} (linha {line}, coluna {column}): {message}"
```

Constantes do módulo: `ERROR_CODE_UNDECLARED = "E3001"`,
`ERROR_CODE_DUPLICATE = "E3002"`.

## Tabela

```python
class SymbolTable:
    def declare(self, declaration: VarDecl | ArrayDecl) -> None:
        """Registra a declaração; nome já presente ->
        SemanticError("E3002", nó.line, nó.column). Registro que falha
        não persiste."""

    def lookup(self, name: str, line: int = 0, column: int = 0) -> VarDecl | ArrayDecl:
        """Devolve a declaração registrada; nome ausente ->
        SemanticError("E3001", line, column)."""

    @property
    def declarations(self) -> list[VarDecl | ArrayDecl]:
        """Cópia defensiva, em ordem de inserção."""
```

## Regras de contrato

- `declare`/`lookup` não mutam nós da AST (D-02) e não dependem de lexer/parser.
- Tipos circulam como literais `CliteType` dos nós (research D3).
- Mensagens em português, uma linha, sem stack trace (D-12, docs/03 §5).
- `SemanticError` será absorvida pela hierarquia da #19: quem captura deve
  decidir pelos atributos (`code`, `line`, `column`), nunca por `str()`.
- Escopo único: nenhuma operação de "entrar/sair de bloco" (D-06).
