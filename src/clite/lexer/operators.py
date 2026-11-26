"""Tabela de operadores e pontuação do CLite (ticket 007, docs/01 §4.2).

A tabela é o contrato único entre o léxico e a gramática concreta: o scanner a
consulta e não repete nenhum lexema (Tucker e Noonan, §2.3.1).
"""

from clite.lexer.tags import Tag

OPERATORS: dict[str, Tag] = {
    # Operadores de atribuição, comparação e lógica.
    "=": Tag.ASSIGN,
    "==": Tag.EQUAL,
    "!=": Tag.NOT_EQUAL,
    "<": Tag.LESS_THAN,
    "<=": Tag.LESS_EQUAL,
    ">": Tag.GREATER_THAN,
    ">=": Tag.GREATER_EQUAL,
    "&&": Tag.LOGICAL_AND,
    "||": Tag.LOGICAL_OR,
    "!": Tag.NOT,
    # Operadores aritméticos.
    "+": Tag.PLUS,
    "-": Tag.MINUS,
    "*": Tag.STAR,
    "/": Tag.SLASH,
    "%": Tag.PERCENT,
    # Colchetes (acesso a arrays) e pontuação.
    "[": Tag.LBRACKET,
    "]": Tag.RBRACKET,
    ";": Tag.SEMICOLON,
    ",": Tag.COMMA,
    "{": Tag.LBRACE,
    "}": Tag.RBRACE,
    "(": Tag.LPAREN,
    ")": Tag.RPAREN,
}

# Maior lexema da tabela: define quantos caracteres o scanner precisa olhar.
MAX_LEXEME_LENGTH = max(len(lexeme) for lexeme in OPERATORS)

# Primeiro caractere de um composto que não é lexema sozinho (hoje, `&` e `|`),
# associado ao composto esperado. Derivado da tabela para não duplicar lexemas.
ISOLATED_PREFIXES: dict[str, str] = {
    lexeme[0]: lexeme for lexeme in OPERATORS if len(lexeme) > 1 and lexeme[0] not in OPERATORS
}
