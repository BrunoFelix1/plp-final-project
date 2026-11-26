"""Testes da tabela de operadores e pontuação do CLite (ticket 007)."""

import pytest

from clite.lexer.lexer import Lexer, LexicalError
from clite.lexer.operators import OPERATORS
from clite.lexer.tags import Tag
from clite.lexer.tokens import Token

SECOND_LINE = 2
SECOND_COLUMN = 2
THIRD_COLUMN = 3
FOURTH_COLUMN = 4
OPERATOR_COUNT = 17
PUNCTUATION_COUNT = 6

# Os 23 lexemas de docs/01 §4.2, escritos à mão para não depender da tabela testada.
EXPECTED_LEXEMES = [
    ("=", Tag.ASSIGN),
    ("==", Tag.EQUAL),
    ("!=", Tag.NOT_EQUAL),
    ("<", Tag.LESS_THAN),
    ("<=", Tag.LESS_EQUAL),
    (">", Tag.GREATER_THAN),
    (">=", Tag.GREATER_EQUAL),
    ("+", Tag.PLUS),
    ("-", Tag.MINUS),
    ("*", Tag.STAR),
    ("/", Tag.SLASH),
    ("%", Tag.PERCENT),
    ("!", Tag.NOT),
    ("&&", Tag.LOGICAL_AND),
    ("||", Tag.LOGICAL_OR),
    ("[", Tag.LBRACKET),
    ("]", Tag.RBRACKET),
    (";", Tag.SEMICOLON),
    (",", Tag.COMMA),
    ("{", Tag.LBRACE),
    ("}", Tag.RBRACE),
    ("(", Tag.LPAREN),
    (")", Tag.RPAREN),
]


def scan_all(source: str) -> list[Token]:
    """Varre o fonte até o EOF, devolvendo os tokens sem o EOF."""
    lexer = Lexer(source)
    tokens: list[Token] = []
    while True:
        token = lexer.scan()
        if token.tag is Tag.EOF:
            return tokens
        tokens.append(token)


def tags_of(source: str) -> list[Tag]:
    return [token.tag for token in scan_all(source)]


def test_expected_list_has_all_documented_lexemes() -> None:
    assert len(EXPECTED_LEXEMES) == OPERATOR_COUNT + PUNCTUATION_COUNT


def test_table_has_exactly_the_documented_lexemes() -> None:
    assert dict(EXPECTED_LEXEMES) == OPERATORS


@pytest.mark.parametrize(("lexeme", "tag"), EXPECTED_LEXEMES)
def test_each_lexeme_is_a_single_token(lexeme: str, tag: Tag) -> None:
    assert scan_all(lexeme) == [Token(tag, lexeme, 1, 1)]


@pytest.mark.parametrize("lexeme", ["==", "!=", "<=", ">=", "&&", "||"])
def test_composite_operator_is_one_token(lexeme: str) -> None:
    tokens = scan_all(f"a{lexeme}b")
    assert [token.lexeme for token in tokens] == ["a", lexeme, "b"]
    assert tokens[1].column == SECOND_COLUMN


def test_broken_operator_is_two_tokens() -> None:
    assert tags_of("a < = b") == [Tag.IDENT, Tag.LESS_THAN, Tag.ASSIGN, Tag.IDENT]


def test_assign_and_equal_are_distinct() -> None:
    assert tags_of("x = y == z") == [
        Tag.IDENT,
        Tag.ASSIGN,
        Tag.IDENT,
        Tag.EQUAL,
        Tag.IDENT,
    ]


def test_triple_equal_is_equal_then_assign() -> None:
    assert tags_of("===") == [Tag.EQUAL, Tag.ASSIGN]


def test_not_and_not_equal_are_distinct() -> None:
    assert tags_of("!a != b") == [Tag.NOT, Tag.IDENT, Tag.NOT_EQUAL, Tag.IDENT]


def test_slash_is_division_and_double_slash_is_comment() -> None:
    assert tags_of("a/b") == [Tag.IDENT, Tag.SLASH, Tag.IDENT]
    assert tags_of("a / b") == [Tag.IDENT, Tag.SLASH, Tag.IDENT]
    assert tags_of("a//b") == [Tag.IDENT]


def test_minus_is_never_part_of_a_literal() -> None:
    assert tags_of("-1") == [Tag.MINUS, Tag.INT_LITERAL]


def test_operator_between_numbers() -> None:
    assert tags_of("1+2") == [Tag.INT_LITERAL, Tag.PLUS, Tag.INT_LITERAL]


def test_whitespace_does_not_change_the_token_sequence() -> None:
    assert tags_of("a<b") == tags_of("a < b")


def test_punctuation_in_a_declaration() -> None:
    assert tags_of("int v[3];") == [
        Tag.INT,
        Tag.IDENT,
        Tag.LBRACKET,
        Tag.INT_LITERAL,
        Tag.RBRACKET,
        Tag.SEMICOLON,
    ]


@pytest.mark.parametrize(
    ("source", "column"),
    [("&", 1), ("|", 1), ("a & b", THIRD_COLUMN), ("a | b", THIRD_COLUMN)],
)
def test_isolated_symbol_fails_with_e1002(source: str, column: int) -> None:
    lexer = Lexer(source)
    with pytest.raises(LexicalError) as info:
        while lexer.scan().tag is not Tag.EOF:
            pass
    assert info.value.code == "E1002"
    assert (info.value.line, info.value.column) == (1, column)


@pytest.mark.parametrize(
    ("source", "composite"),
    [("&&&", Tag.LOGICAL_AND), ("|||", Tag.LOGICAL_OR)],
)
def test_triple_symbol_is_composite_then_e1002(source: str, composite: Tag) -> None:
    lexer = Lexer(source)
    assert lexer.scan().tag is composite
    with pytest.raises(LexicalError) as info:
        lexer.scan()
    assert info.value.code == "E1002"
    assert (info.value.line, info.value.column) == (1, THIRD_COLUMN)


@pytest.mark.parametrize("source", ["@", "#", "."])
def test_other_unknown_characters_keep_e1001(source: str) -> None:
    with pytest.raises(LexicalError) as info:
        Lexer(source).scan()
    assert info.value.code == "E1001"
    assert (info.value.line, info.value.column) == (1, 1)


def test_e1002_message_follows_project_format() -> None:
    with pytest.raises(LexicalError) as info:
        scan_all("a & b")
    assert str(info.value).startswith("erro E1002 (linha 1, coluna 3): ")


def test_operator_position_after_a_newline() -> None:
    tokens = scan_all("a\n  <=")
    assert (tokens[1].line, tokens[1].column) == (SECOND_LINE, THIRD_COLUMN)


def test_column_after_composite_operator() -> None:
    tokens = scan_all("a<=b")
    assert tokens[-1].column == FOURTH_COLUMN
