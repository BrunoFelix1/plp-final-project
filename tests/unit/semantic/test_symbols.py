"""Testes da tabela de símbolos do núcleo (ticket 012; Tucker §4.4, Apêndice A.3).

Cobrem registro, resolução, duplicidade (E3002), nome inexistente (E3001) e a
lista de declarações exposta ao checker, com escopo único (D-06).
"""

import pytest

from clite.ast import nodes
from clite.symbols import SemanticError, SymbolTable

# Posições de amostra: constantes nomeadas (regra de números mágicos).
FIRST_DECLARATION_LINE = 3
FIRST_DECLARATION_COLUMN = 5
SECOND_DECLARATION_LINE = 4
SECOND_DECLARATION_COLUMN = 9
REFERENCE_LINE = 2
REFERENCE_COLUMN = 5
ARRAY_SIZE = 10


def test_declare_and_lookup_when_variable_registered() -> None:
    """Declaração registrada é a mesma devolvida pela busca (US1)."""
    declaracao = nodes.VarDecl(
        name="x", type="int", line=FIRST_DECLARATION_LINE, column=FIRST_DECLARATION_COLUMN
    )
    tabela = SymbolTable()

    tabela.declare(declaracao)

    assert tabela.lookup("x") is declaracao


def test_declare_and_lookup_when_array_registered() -> None:
    """Array registrado é o mesmo devolvido pela busca (US1)."""
    declaracao = nodes.ArrayDecl(
        name="v",
        type="int",
        size=ARRAY_SIZE,
        line=FIRST_DECLARATION_LINE,
        column=FIRST_DECLARATION_COLUMN,
    )
    tabela = SymbolTable()

    tabela.declare(declaracao)

    assert tabela.lookup("v") is declaracao


def test_declare_duplicate_when_name_repeated() -> None:
    """Segunda declaração do mesmo nome gera E3002 na posição dela (US2)."""
    tabela = SymbolTable()
    primeira = nodes.VarDecl(
        name="x", type="int", line=FIRST_DECLARATION_LINE, column=FIRST_DECLARATION_COLUMN
    )
    tabela.declare(primeira)
    segunda = nodes.VarDecl(
        name="x", type="int", line=SECOND_DECLARATION_LINE, column=SECOND_DECLARATION_COLUMN
    )

    with pytest.raises(SemanticError) as erro:
        tabela.declare(segunda)

    assert erro.value.code == "E3002"
    assert erro.value.line == SECOND_DECLARATION_LINE
    assert erro.value.column == SECOND_DECLARATION_COLUMN
    assert str(erro.value) == "erro E3002 (linha 4, coluna 9): nome 'x' já declarado"
    assert tabela.lookup("x") is primeira


def test_declare_duplicate_when_array_repeated() -> None:
    """Array com nome repetido também gera E3002 (US2)."""
    tabela = SymbolTable()
    tabela.declare(
        nodes.ArrayDecl(
            name="v",
            type="int",
            size=ARRAY_SIZE,
            line=FIRST_DECLARATION_LINE,
            column=FIRST_DECLARATION_COLUMN,
        )
    )

    with pytest.raises(SemanticError):
        tabela.declare(
            nodes.ArrayDecl(
                name="v",
                type="int",
                size=ARRAY_SIZE,
                line=SECOND_DECLARATION_LINE,
                column=SECOND_DECLARATION_COLUMN,
            )
        )


def test_declare_duplicate_when_type_differs() -> None:
    """Trocar o tipo não contorna a unicidade: `float x` após `int x` é E3002 (US2)."""
    tabela = SymbolTable()
    tabela.declare(
        nodes.VarDecl(
            name="x", type="int", line=FIRST_DECLARATION_LINE, column=FIRST_DECLARATION_COLUMN
        )
    )

    with pytest.raises(SemanticError):
        tabela.declare(
            nodes.VarDecl(
                name="x",
                type="float",
                line=SECOND_DECLARATION_LINE,
                column=SECOND_DECLARATION_COLUMN,
            )
        )


def test_declare_duplicate_when_declared_in_distinct_blocks() -> None:
    """Blocos não criam escopo (D-06): mesmo nome em outro bloco é E3002 (US2)."""
    tabela = SymbolTable()
    tabela.declare(
        nodes.VarDecl(
            name="x", type="int", line=FIRST_DECLARATION_LINE, column=FIRST_DECLARATION_COLUMN
        )
    )

    with pytest.raises(SemanticError):
        tabela.declare(
            nodes.VarDecl(
                name="x", type="int", line=SECOND_DECLARATION_LINE, column=SECOND_DECLARATION_COLUMN
            )
        )


def test_lookup_missing_when_position_given() -> None:
    """Busca de nome não registrado gera E3001 com a posição da referência (US3)."""
    tabela = SymbolTable()

    with pytest.raises(SemanticError) as erro:
        tabela.lookup("x", line=REFERENCE_LINE, column=REFERENCE_COLUMN)

    assert erro.value.code == "E3001"
    assert erro.value.line == REFERENCE_LINE
    assert erro.value.column == REFERENCE_COLUMN
    assert str(erro.value) == "erro E3001 (linha 2, coluna 5): variável 'x' não declarada"


def test_lookup_missing_when_no_position() -> None:
    """Busca sem posição informada gera E3001 com (0, 0), padrão da AST (US3)."""
    tabela = SymbolTable()

    with pytest.raises(SemanticError) as erro:
        tabela.lookup("x")

    assert (erro.value.line, erro.value.column) == (0, 0)


def test_declarations_list_when_three_declarations() -> None:
    """Lista exposta preserva a ordem de inserção e é cópia defensiva (US3)."""
    tabela = SymbolTable()
    declaracoes = [
        nodes.VarDecl(
            name="x", type="int", line=FIRST_DECLARATION_LINE, column=FIRST_DECLARATION_COLUMN
        ),
        nodes.ArrayDecl(
            name="v",
            type="int",
            size=ARRAY_SIZE,
            line=FIRST_DECLARATION_LINE,
            column=FIRST_DECLARATION_COLUMN,
        ),
        nodes.VarDecl(
            name="y", type="bool", line=SECOND_DECLARATION_LINE, column=SECOND_DECLARATION_COLUMN
        ),
    ]
    for declaracao in declaracoes:
        tabela.declare(declaracao)

    assert tabela.declarations == declaracoes

    tabela.declarations.clear()

    assert len(tabela.declarations) == len(declaracoes)


def test_empty_table_when_lookup() -> None:
    """Tabela vazia: busca gera E3001 e a lista devolvida é vazia (US3)."""
    tabela = SymbolTable()

    with pytest.raises(SemanticError):
        tabela.lookup("x", line=REFERENCE_LINE, column=REFERENCE_COLUMN)

    assert tabela.declarations == []
