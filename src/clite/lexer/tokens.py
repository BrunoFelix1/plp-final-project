# ================================================= #
# TOKENS - Representacao dos tokens da linguagem CLite
# Ticket 005 - Tokens e palavras reservadas
# ================================================= #

# ================================================= #
# Imports
# ================================================= #

from dataclasses import dataclass

from clite.lexer.tags import Tag

# ================================================= #
# Definicao da estrutura de um Token
# ================================================= #
# @dataclass --> Decorador que gera automaticamente
# metodos para inicializar e representar os objetos.
#
# frozen=True --> Impede a alteracao direta dos
# atributos depois que o objeto foi criado.
#
# class --> Declara uma classe em Python.
# Token --> Representa uma unidade reconhecida pelo lexer.
# ================================================= #


@dataclass(frozen=True)
class Token:
    # ================================================= #
    # Atributos de um token
    # ================================================= #
    # tag: Tag --> Categoria do token, definida na classe Tag.
    # lexeme: str --> Texto original encontrado no programa.
    # line: int --> Numero da linha onde o token foi encontrado.
    # column: int --> Numero da coluna onde o token comeca.
    # ================================================= #

    tag: Tag
    lexeme: str
    line: int
    column: int
