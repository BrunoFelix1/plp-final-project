# ================================================= #
# TESTES - Tokens e palavras reservadas CLite
# Ticket 005
# ================================================= #

# ================================================= #
# Imports
# ================================================= #
# pytest --> Framework utilizado para testes automatizados.
# FrozenInstanceError --> Excecao gerada quando tentamos
# alterar um atributo de uma dataclass congelada.
# ================================================= #

from dataclasses import FrozenInstanceError

import pytest

from clite.lexer.keywords import KEYWORDS, is_reserved
from clite.lexer.tags import Tag
from clite.lexer.tokens import Token

# ================================================= #
# Teste das categorias dos tokens
# ================================================= #
# Verifica se os valores numericos das tags sao unicos.
# ================================================= #


def test_tags_unicas() -> None:
    valores = [tag.value for tag in Tag]

    assert len(valores) == len(set(valores))


# ================================================= #
# Teste das palavras reservadas
# ================================================= #
# parametrize --> Executa o mesmo teste para cada
# palavra presente no dicionario KEYWORDS.
# ================================================= #


@pytest.mark.parametrize("palavra", list(KEYWORDS))
def test_palavras_reservadas(palavra: str) -> None:
    assert is_reserved(palavra)


# ================================================= #
# Teste de palavras nao reservadas
# ================================================= #


@pytest.mark.parametrize(
    "palavra",
    ["idade", "contador", "whilea", "INT", "x1"],
)
def test_palavras_nao_reservadas(palavra: str) -> None:
    assert not is_reserved(palavra)


# ================================================= #
# Teste de associacao das palavras com suas tags
# ================================================= #


def test_associacao_keywords() -> None:
    assert KEYWORDS["int"] == Tag.INT
    assert KEYWORDS["while"] == Tag.WHILE
    assert KEYWORDS["class"] == Tag.CLASS


# ================================================= #
# Teste de igualdade entre tokens
# ================================================= #
# Dois tokens sao iguais quando todos os atributos
# possuem os mesmos valores.
# ================================================= #


def test_igualdade_tokens() -> None:
    token_a = Token(Tag.INT, "int", 1, 1)
    token_b = Token(Tag.INT, "int", 1, 1)

    assert token_a == token_b


# ================================================= #
# Teste de tokens diferentes
# ================================================= #


def test_tokens_diferentes() -> None:
    token_a = Token(Tag.INT, "int", 1, 1)
    token_b = Token(Tag.IDENT, "idade", 1, 5)

    assert token_a != token_b


# ================================================= #
# Teste de representacao textual do token
# ================================================= #
# repr --> Retorna uma representacao do objeto.
# ================================================= #


def test_representacao_token() -> None:
    token = Token(Tag.INT, "int", 1, 1)

    representacao = repr(token)

    assert "Token(" in representacao
    assert "int" in representacao
    assert "line=1" in representacao
    assert "column=1" in representacao


# ================================================= #
# Teste de imutabilidade do token
# ================================================= #
# frozen=True --> Impede alteracoes diretas
# nos atributos depois da criacao do objeto.
# ================================================= #


def test_token_imutavel() -> None:
    token = Token(Tag.INT, "int", 1, 1)

    with pytest.raises(FrozenInstanceError):
        token.lexeme = "float"  # type: ignore[misc]
