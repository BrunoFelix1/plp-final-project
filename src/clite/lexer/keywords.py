# ================================================= #
# KEYWORDS - Palavras reservadas da linguagem CLite
# Ticket 005 - Tokens e palavras reservadas
# ================================================= #

# ================================================= #
# Imports
# ================================================= #
# Tag --> Classe que define as categorias dos tokens.
# Importada do modulo create_tags.py.
#
# Utilizamos essa classe para associar cada palavra
# reservada a sua respectiva categoria.
# ================================================= #

from clite.lexer.tags import Tag

# ================================================= #
# Definicao das palavras reservadas
# ================================================= #
# KEYWORDS --> Dicionario que armazena as palavras
# reservadas da linguagem CLite.
#
# dict[str, Tag] --> Define os tipos do dicionario:
# str --> Chave que representa o texto da palavra.
# Tag --> Valor que representa a categoria do token.
#
# Exemplo:
# "int": Tag.INT --> Associa "int" a categoria INT.
# "while": Tag.WHILE --> Associa "while" a categoria WHILE.
#
# As palavras sao diferenciadas por letras maiusculas
# e minusculas. Exemplo: "int" e diferente de "INT".
# ================================================= #

KEYWORDS: dict[str, Tag] = {
    # ================================================= #
    # Palavras reservadas - Nucleo CLite
    # ================================================= #
    # Representam os tipos, valores booleanos,
    # estruturas condicionais e de repeticao.
    # ================================================= #
    "int": Tag.INT,
    "bool": Tag.BOOL,
    "float": Tag.FLOAT,
    "char": Tag.CHAR,
    "true": Tag.TRUE,
    "false": Tag.FALSE,
    "if": Tag.IF,
    "else": Tag.ELSE,
    "while": Tag.WHILE,
    "main": Tag.MAIN,
    # ================================================= #
    # Palavras reservadas - Extensao OO
    # ================================================= #
    # OO --> Orientacao a Objetos.
    #
    # Essas palavras sao reservadas antecipadamente
    # para a extensao OO planejada para CLite.
    # ================================================= #
    "class": Tag.CLASS,
    "extends": Tag.EXTENDS,
    "new": Tag.NEW,
    "this": Tag.THIS,
    "return": Tag.RETURN,
    "void": Tag.VOID,
    "print": Tag.PRINT,
}


# ================================================= #
# Verificacao de palavras reservadas
# ================================================= #
# def --> Declara uma funcao em Python.
# is_reserved --> Nome da funcao que verifica se uma
# palavra pertence ao conjunto de palavras reservadas.
#
# palavra: str --> Recebe uma string como parametro.
# -> bool --> Indica que a funcao retorna um booleano.
#
# palavra in KEYWORDS --> Consulta se a palavra existe
# entre as chaves do dicionario.
#
# True --> A palavra e reservada.
# False --> A palavra nao e reservada.
# ================================================= #


def is_reserved(palavra: str) -> bool:
    return palavra in KEYWORDS
