"""Analisador lexical do CLite: converte texto em tokens (ticket 006).

O scanner implementa maior casamento sobre um autômato finito: consome a maior
sequência válida antes de classificar o token (Tucker e Noonan, §3.2.2).
"""

import string
from collections.abc import Callable

from clite.lexer.keywords import KEYWORDS
from clite.lexer.operators import ISOLATED_PREFIXES, MAX_LEXEME_LENGTH, OPERATORS
from clite.lexer.tags import Tag
from clite.lexer.tokens import Token

WHITESPACE = " \t\r\n"
NEWLINE = "\n"
SLASH = "/"
DOT = "."
QUOTE = "'"
EOF_LEXEME = ""
INITIAL_LINE = 1
INITIAL_COLUMN = 1
ERROR_CODE = "E1001"
ERROR_CODE_ISOLATED_OPERATOR = "E1002"
LETTERS = string.ascii_letters
DIGITS = string.digits


class LexicalError(Exception):
    """Erro léxico com código e posição no fonte (D-12)."""

    def __init__(self, line: int, column: int, message: str, code: str = ERROR_CODE) -> None:
        self.code = code
        self.line = line
        self.column = column
        self.message = message
        super().__init__(f"erro {self.code} (linha {line}, coluna {column}): {message}")


class Lexer:
    """Varre um fonte CLite e devolve um token por chamada de ``scan``."""

    def __init__(self, source: str) -> None:
        self._source = source
        self._index = 0
        self._line = INITIAL_LINE
        self._column = INITIAL_COLUMN

    def scan(self) -> Token:
        """Devolve o próximo token; emite ``EOF`` de forma estável no fim."""
        self._skip_trivia()
        if self._at_end():
            return Token(Tag.EOF, EOF_LEXEME, self._line, self._column)
        char = self._peek()
        if char in LETTERS:
            return self._scan_word()
        if char in DIGITS:
            return self._scan_number()
        if char == QUOTE:
            return self._scan_char()
        if char == DOT:
            raise LexicalError(self._line, self._column, "float exige dígito antes do ponto")
        return self._scan_symbol()

    def _scan_symbol(self) -> Token:
        line, column = self._line, self._column
        for length in range(MAX_LEXEME_LENGTH, 0, -1):
            lexeme = self._source[self._index : self._index + length]
            if lexeme in OPERATORS:
                for _ in lexeme:
                    self._advance()
                return Token(OPERATORS[lexeme], lexeme, line, column)
        char = self._peek()
        if char in ISOLATED_PREFIXES:
            message = f"{char!r} isolado; o operador é {ISOLATED_PREFIXES[char]!r}"
            raise LexicalError(line, column, message, ERROR_CODE_ISOLATED_OPERATOR)
        raise LexicalError(line, column, f"caractere inesperado: {char!r}")

    def _scan_word(self) -> Token:
        line, column = self._line, self._column
        lexeme = self._take_while(_is_word_char)
        return Token(KEYWORDS.get(lexeme, Tag.IDENT), lexeme, line, column)

    def _scan_number(self) -> Token:
        line, column = self._line, self._column
        lexeme = self._take_while(_is_digit)
        if self._at_end() or self._peek() != DOT:
            return Token(Tag.INT_LITERAL, lexeme, line, column)
        if not self._next_is_digit():
            raise LexicalError(self._line, self._column, "float exige dígito depois do ponto")
        lexeme += self._advance()
        lexeme += self._take_while(_is_digit)
        return Token(Tag.FLOAT_LITERAL, lexeme, line, column)

    def _scan_char(self) -> Token:
        line, column = self._line, self._column
        self._advance()
        if self._at_end():
            raise LexicalError(line, column, "literal de caractere não fechado")
        char = self._peek()
        if char == QUOTE:
            raise LexicalError(line, column, "literal de caractere vazio")
        if not (char.isascii() and char.isprintable()):
            raise LexicalError(line, column, "literal de caractere exige caractere imprimível")
        self._advance()
        if self._at_end() or self._peek() != QUOTE:
            raise LexicalError(line, column, "literal de caractere exige exatamente um caractere")
        self._advance()
        return Token(Tag.CHAR_LITERAL, f"{QUOTE}{char}{QUOTE}", line, column)

    def _skip_trivia(self) -> None:
        while not self._at_end():
            if self._peek() in WHITESPACE:
                self._advance()
                continue
            if self._peek() == SLASH and self._peek_next() == SLASH:
                self._take_while(lambda char: char != NEWLINE)
                continue
            return

    def _take_while(self, predicate: Callable[[str], bool]) -> str:
        start = self._index
        while not self._at_end() and predicate(self._peek()):
            self._advance()
        return self._source[start : self._index]

    def _next_is_digit(self) -> bool:
        next_char = self._peek_next()
        return next_char != "" and next_char in DIGITS

    def _peek(self) -> str:
        return self._source[self._index]

    def _peek_next(self) -> str:
        next_index = self._index + 1
        if next_index >= len(self._source):
            return ""
        return self._source[next_index]

    def _advance(self) -> str:
        char = self._source[self._index]
        self._index += 1
        if char == NEWLINE:
            self._line += 1
            self._column = INITIAL_COLUMN
        else:
            self._column += 1
        return char

    def _at_end(self) -> bool:
        return self._index >= len(self._source)


def _is_digit(char: str) -> bool:
    return char in DIGITS


def _is_word_char(char: str) -> bool:
    return char in LETTERS or char in DIGITS
