"""Teste de fumaça do esqueleto: garante que o pacote instala e importa.

Não valida comportamento da linguagem — isso é papel dos testes de cada ticket.
"""

import clite


def test_pacote_importa() -> None:
    assert clite.__version__
