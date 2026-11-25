"""Testes do analisador lexical do CLite (ticket 006)."""

import pytest

from clite.lexer.lexer import Lexer, LexicalError
from clite.lexer.tags import Tag
from clite.lexer.tokens import Token

SECOND_LINE = 2
COLUMN_AFTER_TAB = 5
SECOND_CHARACTER_COLUMN = 2
SECOND_DOT_COLUMN = 4


def scan_all(source: str) -> list[Token]:
    """Varre o fonte até o EOF, devolvendo todos os tokens."""
    lexer = Lexer(source)
    tokens: list[Token] = []
    while True:
        token = lexer.scan()
        tokens.append(token)
        if token.tag is Tag.EOF:
            return tokens


def first_token(source: str) -> Token:
    """Devolve apenas o primeiro token do fonte."""
    return Lexer(source).scan()


def test_identifier_and_position() -> None:
    tokens = scan_all("abc abc123")
    assert [token.tag for token in tokens] == [Tag.IDENT, Tag.IDENT, Tag.EOF]
    assert [token.lexeme for token in tokens] == ["abc", "abc123", ""]
    assert (tokens[0].line, tokens[0].column) == (1, 1)
    assert (tokens[1].line, tokens[1].column) == (1, COLUMN_AFTER_TAB)


def test_maximal_munch_keeps_reserved_prefix_in_identifier() -> None:
    token = first_token("whilea")
    assert token.tag is Tag.IDENT
    assert token.lexeme == "whilea"


def test_reserved_words_become_keywords() -> None:
    tags = [token.tag for token in scan_all("while int print true false")]
    assert tags == [Tag.WHILE, Tag.INT, Tag.PRINT, Tag.TRUE, Tag.FALSE, Tag.EOF]


def test_reserved_words_are_case_sensitive() -> None:
    token = first_token("While")
    assert token.tag is Tag.IDENT
    assert token.lexeme == "While"


def test_integers_and_floats() -> None:
    tokens = scan_all("42 3.14 5.0 0.5")
    assert [token.tag for token in tokens] == [
        Tag.INT_LITERAL,
        Tag.FLOAT_LITERAL,
        Tag.FLOAT_LITERAL,
        Tag.FLOAT_LITERAL,
        Tag.EOF,
    ]
    assert [token.lexeme for token in tokens] == ["42", "3.14", "5.0", "0.5", ""]


def test_char_literals_keep_quotes() -> None:
    tokens = scan_all("'a' ' '")
    assert [token.tag for token in tokens] == [
        Tag.CHAR_LITERAL,
        Tag.CHAR_LITERAL,
        Tag.EOF,
    ]
    assert tokens[0].lexeme == "'a'"
    assert tokens[1].lexeme == "' '"


def test_slash_inside_char_is_not_comment() -> None:
    token = first_token("'/'")
    assert token.tag is Tag.CHAR_LITERAL
    assert token.lexeme == "'/'"


def test_whitespace_and_lines() -> None:
    tokens = scan_all("abc\tdef\nghi")
    assert [token.lexeme for token in tokens] == ["abc", "def", "ghi", ""]
    assert [(token.line, token.column) for token in tokens[:-1]] == [
        (1, 1),
        (1, COLUMN_AFTER_TAB),
        (SECOND_LINE, 1),
    ]


def test_comment_until_end_of_line() -> None:
    tokens = scan_all("abc // x = 1;\ndef")
    assert [token.lexeme for token in tokens] == ["abc", "def", ""]
    assert tokens[1].line == SECOND_LINE


def test_comment_without_trailing_newline() -> None:
    tokens = scan_all("abc // fim")
    assert [token.lexeme for token in tokens] == ["abc", ""]


def test_eof_is_stable() -> None:
    lexer = Lexer("")
    first = lexer.scan()
    second = lexer.scan()
    assert first.tag is Tag.EOF
    assert first.lexeme == ""
    assert second == first


@pytest.mark.parametrize(
    ("source", "column"),
    [("5.", SECOND_CHARACTER_COLUMN), (".5", 1)],
)
def test_incomplete_float_fails_at_dot(source: str, column: int) -> None:
    with pytest.raises(LexicalError) as info:
        first_token(source)
    assert info.value.code == "E1001"
    assert (info.value.line, info.value.column) == (1, column)


@pytest.mark.parametrize("source", ["''", "'ab'"])
def test_invalid_char_fails_at_opening_quote(source: str) -> None:
    with pytest.raises(LexicalError) as info:
        first_token(source)
    assert (info.value.line, info.value.column) == (1, 1)


@pytest.mark.parametrize("source", ["@", ";", "+", "("])
def test_unknown_character_fails(source: str) -> None:
    with pytest.raises(LexicalError) as info:
        first_token(source)
    assert info.value.code == "E1001"
    assert (info.value.line, info.value.column) == (1, 1)


def test_second_dot_fails_after_valid_float() -> None:
    lexer = Lexer("1.2.3")
    first = lexer.scan()
    assert first.tag is Tag.FLOAT_LITERAL
    assert first.lexeme == "1.2"
    with pytest.raises(LexicalError) as info:
        lexer.scan()
    assert (info.value.line, info.value.column) == (1, SECOND_DOT_COLUMN)


def test_error_message_follows_project_format() -> None:
    with pytest.raises(LexicalError) as info:
        first_token("5.")
    assert str(info.value).startswith("erro E1001 (linha 1, coluna 2): ")
