"""Testes dos nós da AST do núcleo (ticket 009; docs/01 §6).

Cobrem construção, igualdade estrutural e imutabilidade (D-02: nós são
dados puros; nenhuma lógica de execução ou de tipos).
"""

import dataclasses

import pytest

from clite.ast import nodes

# Valores de amostra: literais > 1 viram constantes nomeadas (regra de
# números mágicos); 0 e 1 são identidades estruturais liberadas.
SAMPLE_SIZE = 10
SAMPLE_FLOAT = 0.5
SAMPLE_LINE = 3
SAMPLE_COLUMN = 7


def _issue_example_tree() -> nodes.Assign:
    """Árvore-exemplo da issue #9: ``x = x + 1``."""
    return nodes.Assign(
        target=nodes.VarRef(name="x"),
        source=nodes.Binary(
            op="+",
            left=nodes.VarRef(name="x"),
            right=nodes.IntLiteral(value=1),
        ),
    )


def _all_core_nodes() -> list[object]:
    """Um espécime de cada nó de ``docs/01`` §6 (17 classes)."""
    return [
        nodes.Program(declarations=[], commands=[nodes.Skip()]),
        nodes.VarDecl(name="x", type="int"),
        nodes.ArrayDecl(name="v", type="int", size=SAMPLE_SIZE),
        nodes.Skip(),
        nodes.Block(commands=[nodes.Skip()]),
        nodes.Assign(target=nodes.VarRef(name="x"), source=nodes.IntLiteral(value=1)),
        nodes.If(test=nodes.BoolLiteral(value=True), then=nodes.Skip()),
        nodes.If(
            test=nodes.BoolLiteral(value=True),
            then=nodes.Skip(),
            else_branch=nodes.Skip(),
        ),
        nodes.While(test=nodes.BoolLiteral(value=True), body=nodes.Skip()),
        nodes.VarRef(name="x"),
        nodes.ArrayRef(name="v", index=nodes.IntLiteral(value=0)),
        nodes.Binary(
            op="+",
            left=nodes.IntLiteral(value=1),
            right=nodes.IntLiteral(value=0),
        ),
        nodes.Unary(op="-", operand=nodes.IntLiteral(value=1)),
        nodes.Convert(target_type="float", operand=nodes.IntLiteral(value=1)),
        nodes.IntLiteral(value=1),
        nodes.FloatLiteral(value=SAMPLE_FLOAT),
        nodes.BoolLiteral(value=True),
        nodes.CharLiteral(value="x"),
    ]


_ALL_NODES = _all_core_nodes()
_NODE_IDS = [type(node).__name__ for node in _ALL_NODES]


@pytest.mark.parametrize("node", _ALL_NODES, ids=_NODE_IDS)
def test_constructs_every_core_node(node: nodes.Assign) -> None:
    """Cada nó de §6 é construído sem erro."""
    assert node is not None


@pytest.mark.parametrize("node", _ALL_NODES, ids=_NODE_IDS)
def test_rebuilt_node_compares_equal(node: nodes.Assign) -> None:
    """Igualdade estrutural: reconstruir com os mesmos campos dá nó igual."""
    assert dataclasses.replace(node) == node


def test_issue_example_tree_builds_and_compares_equal() -> None:
    """A árvore-exemplo da issue #9 constrói e é igual a si mesma."""
    assert _issue_example_tree() == _issue_example_tree()


def test_changed_field_makes_nodes_unequal() -> None:
    """Mudar um campo de nível superior torna os nós diferentes."""
    assert nodes.VarRef(name="x") != nodes.VarRef(name="y")


def test_changed_nested_field_makes_trees_unequal() -> None:
    """Mudar um campo aninhado torna as árvores diferentes."""
    changed = dataclasses.replace(_issue_example_tree(), target=nodes.VarRef(name="y"))
    assert _issue_example_tree() != changed


@pytest.mark.parametrize("node", _ALL_NODES, ids=_NODE_IDS)
def test_frozen_nodes_reject_attribute_writes(node: nodes.Assign) -> None:
    """Todo nó é imutável: escrever atributo levanta FrozenInstanceError."""
    field_name = "qualquer_atributo"
    with pytest.raises(dataclasses.FrozenInstanceError):
        setattr(node, field_name, None)


@pytest.mark.parametrize("node", _ALL_NODES, ids=_NODE_IDS)
def test_position_defaults_to_uninformed_zero(node: nodes.Assign) -> None:
    """Sem posição informada, todo nó carrega o padrão ``0`` (não informado)."""
    assert node.line == 0
    assert node.column == 0


def test_explicit_position_is_preserved() -> None:
    """Posição explícita informada na construção é preservada no nó."""
    node = nodes.VarRef(name="x", line=SAMPLE_LINE, column=SAMPLE_COLUMN)
    assert node.line == SAMPLE_LINE
    assert node.column == SAMPLE_COLUMN
