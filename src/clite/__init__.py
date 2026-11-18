"""CLite — interpretador da linguagem CLite escrito em Python.

Este pacote é um esqueleto de estudo. Cada subpacote corresponde a uma fase do
front-end descrita no Apêndice A de *Compiladores: Princípios, Técnicas e
Ferramentas*:

``lexer``       fluxo de caracteres → fluxo de tokens
``parser``      fluxo de tokens → árvore de sintaxe abstrata (AST)
``semantic``    verificação de tipos e resolução de nomes
``interpreter`` avaliação da AST sobre um estado (variáveis e objetos)

Os documentos em ``docs/`` são a fonte da verdade da gramática e das decisões.
"""

__version__ = "0.0.0"
