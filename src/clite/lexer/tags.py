# ================================================= #
# TAGS - Categorias dos tokens da linguagem CLite
# Ticket 005 - Tokens e palavras reservadas
# ================================================= #

# ================================================= #
# Imports
# ================================================= #
# IntEnum --> Permite criar enumeracoes cujos valores
# sao representados por numeros inteiros.
# ================================================= #

from enum import IntEnum

# ================================================= #
# Definicao das categorias dos tokens
# ================================================= #
# class --> Declara uma classe em Python.
# Tag --> Nome da classe que representa as categorias.
# IntEnum --> Classe base utilizada para criar a enumeracao.
#
# Nessa class, estamos criando uma classe chamada Tag
# que herda de IntEnum.
#
# Isso significa que cada atributo definido dentro
# da classe sera um membro da enumeracao.
#
# Exemplo:
# Tag.INT.name --> Retorna "INT".
# Tag.INT.value --> Retorna 260.
# ================================================= #


class Tag(IntEnum):
    # ================================================= #
    # Identificadores e literais
    # ================================================= #
    # Os valores comecam em 256 por uma convencao comum
    # em implementacoes de compiladores.
    # Os valores de 0 a 255 representam a faixa de bytes,
    # frequentemente associada aos codigos ASCII.
    # ================================================= #
    # IDENT --> Identificador de variavel ou outro nome permitido.
    # INT_LITERAL --> Literal inteiro.
    # FLOAT_LITERAL --> Literal de ponto flutuante.
    # CHAR_LITERAL --> Literal de caractere.
    # ================================================= #

    IDENT = 256
    INT_LITERAL = 257
    FLOAT_LITERAL = 258
    CHAR_LITERAL = 259

    # ================================================= #
    # Palavras reservadas - Nucleo CLite
    # ================================================= #
    # Palavras reservadas possuem significados especificos
    # na linguagem e nao podem ser usadas como identificadores.
    # ================================================= #
    # INT --> Declara um tipo inteiro.
    # BOOL --> Declara um tipo booleano.
    # FLOAT --> Declara um tipo de ponto flutuante.
    # CHAR --> Declara um tipo caractere.
    # TRUE --> Literal booleano verdadeiro.
    # FALSE --> Literal booleano falso.
    # IF_STATEMENT --> Estrutura condicional.
    # ELSE --> Alternativa da estrutura condicional.
    # WHILE --> Estrutura de repeticao.
    # MAIN --> Ponto de entrada do programa CLite.
    # ================================================= #

    INT = 260
    BOOL = 261
    FLOAT = 262
    CHAR = 263
    TRUE = 264
    FALSE = 265
    IF_STATEMENT = 266
    ELSE = 267
    WHILE = 268
    MAIN = 269

    # ================================================= #
    # Palavras reservadas - Extensao OO
    # ================================================= #
    # OO --> Orientacao a Objetos.
    #
    # Essas palavras fazem parte da extensao orientada
    # a objetos planejada para a linguagem CLite.
    #
    # Mesmo que ainda nao sejam utilizadas no nucleo,
    # elas ja sao reservadas para implementacoes futuras.
    # ================================================= #
    # CLASS --> Declara uma classe.
    # EXTENDS --> Define heranca entre classes.
    # NEW --> Cria uma nova instancia de uma classe.
    # THIS --> Referencia o objeto atual.
    # RETURN --> Retorna um valor ou encerra a execucao
    # VOID --> Indica que um metodo nao retorna valor.
    # PRINT --> Instrucao utilizada para apresentar
    # ================================================= #

    CLASS = 270
    EXTENDS = 271
    NEW = 272
    THIS = 273
    RETURN = 274
    VOID = 275
    PRINT = 276

    # ================================================= #
    # Operadores
    # ================================================= #
    # Operadores representam atribuicoes, comparacoes,
    # calculos matematicos e operacoes logicas.
    #
    # Cada operador possui uma categoria especifica
    # para que o lexer consiga diferencia-los.
    # ================================================= #
    # ASSIGN --> Operador de atribuicao (=).
    # EQUAL --> Operador de igualdade (==).
    # NOT_EQUAL --> Operador de diferenca (!=).
    # LESS_THAN --> Operador menor que (<).
    # LESS_EQUAL --> Operador menor ou igual (<=).
    # GREATER_THAN --> Operador maior que (>).
    # GREATER_EQUAL --> Operador maior ou igual (>=).
    # PLUS --> Operador de adicao (+).
    # MINUS --> Operador de subtracao ou negacao (-).
    # STAR --> Operador de multiplicacao (*).
    # SLASH --> Operador de divisao (/).
    # PERCENT --> Operador de resto da divisao (%).
    # NOT --> Operador de negacao logica (!).
    # LOGICAL_AND --> Operador logico E (&&) -->Retorna verdadeiro quando as duas condicoes
    # LOGICAL_OR --> Operador logico OU (||).
    # ================================================= #

    ASSIGN = 277
    EQUAL = 278
    NOT_EQUAL = 279
    LESS_THAN = 280
    LESS_EQUAL = 281
    GREATER_THAN = 282
    GREATER_EQUAL = 283
    PLUS = 284
    MINUS = 285
    STAR = 286
    SLASH = 287
    PERCENT = 288
    NOT = 289
    LOGICAL_AND = 290
    LOGICAL_OR = 291

    # ================================================= #
    # Pontuacao
    # ================================================= #
    # Os simbolos de pontuacao organizam a estrutura
    # do codigo-fonte da linguagem CLite.
    #
    # L --> Left: abertura ou lado esquerdo.
    # R --> Right: fechamento ou lado direito.
    # ================================================= #
    # SEMICOLON --> Ponto e virgula (;).
    # COMMA --> Virgula (,).
    # LBRACE --> Chave de abertura ({).
    # RBRACE --> Chave de fechamento (}).
    # LPAREN --> Parentese de abertura (().
    # RPAREN --> Parentese de fechamento ()).
    # LBRACKET --> Colchete de abertura ([).
    # RBRACKET --> Colchete de fechamento (]).
    # ================================================= #

    SEMICOLON = 292
    COMMA = 293
    LBRACE = 294
    RBRACE = 295
    LPAREN = 296
    RPAREN = 297
    LBRACKET = 298
    RBRACKET = 299

    # ================================================= #
    # Fim do arquivo
    # ================================================= #
    # EOF --> End Of File, ou seja, fim do arquivo.
    # ================================================= #

    EOF = 300
