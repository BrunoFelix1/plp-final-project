"""Tabela de símbolos: escopos, declarações e mapas de tipos (Apêndice A.3).

Escopo único (D-06): blocos não criam escopo; o mapa é plano, nome →
declaração, em ordem de inserção.
"""

from __future__ import annotations

from clite.ast import nodes

# Códigos E3xxx desta fatia (docs/06 §3; formato em docs/03 §5).
ERROR_CODE_UNDECLARED = "E3001"
ERROR_CODE_DUPLICATE = "E3002"


class SemanticError(Exception):
    """Erro semântico com código e posição no fonte (D-12; padrão da LexicalError)."""

    def __init__(self, line: int, column: int, message: str, code: str) -> None:
        self.code = code
        self.line = line
        self.column = column
        self.message = message
        super().__init__(f"erro {self.code} (linha {line}, coluna {column}): {message}")


class SymbolTable:
    """Mapa plano nome → declaração, em escopo único (D-06)."""

    def __init__(self) -> None:
        self._declarations: dict[str, nodes.Declaration] = {}

    def declare(self, declaration: nodes.Declaration) -> None:
        """Registra a declaração; segundo registro do mesmo nome gera E3002."""
        if declaration.name in self._declarations:
            raise SemanticError(
                declaration.line,
                declaration.column,
                f"nome '{declaration.name}' já declarado",
                ERROR_CODE_DUPLICATE,
            )
        self._declarations[declaration.name] = declaration

    def lookup(self, name: str, line: int = 0, column: int = 0) -> nodes.Declaration:
        """Devolve a declaração registrada; nome ausente gera E3001."""
        if name not in self._declarations:
            raise SemanticError(
                line,
                column,
                f"variável '{name}' não declarada",
                ERROR_CODE_UNDECLARED,
            )
        return self._declarations[name]

    @property
    def declarations(self) -> list[nodes.Declaration]:
        """Cópia defensiva, em ordem de inserção (contrato com o checker)."""
        return list(self._declarations.values())
