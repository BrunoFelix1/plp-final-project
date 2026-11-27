"""Nós da AST de CLite (docs/01 §6; Apêndice A.2 e A.5.2).

Dados puros e imutáveis (D-02): a AST carrega apenas a estrutura essencial
para as fases seguintes; checagem de tipos e avaliação ficam nos visitantes
``clite.semantic`` e ``clite.interpreter``. Pontuação e parênteses não viram
nó (Tucker e Noonan §2.5.1): só o que a semântica consome sobe para a árvore.

Todo nó carrega ``line``/``column`` (1-based) para os relatórios de erro; o
padrão ``0`` significa "não informado", permitindo construir árvores sem
posição (ex.: testes e construção programática).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

# Tipos primitivos declaráveis na v1 (docs/01 §6); a restrição é estática.
CliteType = Literal["int", "float", "char", "bool"]


@dataclass(frozen=True)
class IntLiteral:
    """Valor inteiro literal, ex.: ``42``."""

    value: int
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class FloatLiteral:
    """Valor de ponto flutuante literal, ex.: ``3.14``."""

    value: float
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class BoolLiteral:
    """Valor booleano literal: ``true`` ou ``false``."""

    value: bool
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class CharLiteral:
    """Valor caractere literal, ex.: ``'a'`` (um caractere imprimível)."""

    value: str
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class VarRef:
    """Referência a variável simples, ex.: ``x``."""

    name: str
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class ArrayRef:
    """Referência a elemento de array, ex.: ``v[i]``."""

    name: str
    index: Expression
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class Binary:
    """Operação binária: operador + dois operandos da mesma categoria."""

    op: str
    left: Expression
    right: Expression
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class Unary:
    """Operação unária prefixa: ``-`` ou ``!`` aplicado a um termo."""

    op: str
    operand: Expression
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class Convert:
    """Conversão explícita ``Tipo ( Expressão )``; a validação é semântica."""

    target_type: CliteType
    operand: Expression
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class VarDecl:
    """Declaração de variável simples, ex.: ``int x;``."""

    name: str
    type: CliteType
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class ArrayDecl:
    """Declaração de array de tamanho fixo; o tamanho é literal inteiro."""

    name: str
    type: CliteType
    size: int
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class Skip:
    """Comando vazio ``;``: presente como estrutura, sem efeito."""

    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class Block:
    """Sequência de comandos; não cria escopo (D-06)."""

    commands: list[Command]
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class Assign:
    """Atribuição: alvo é variável simples ou elemento de array."""

    target: VarRef | ArrayRef
    source: Expression
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class If:
    """Condicional; o ramo ``else`` é opcional (docs/01 §6, ``senão?``)."""

    test: Expression
    then: Command
    else_branch: Command | None = None
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class While:
    """Laço com teste no início: repete ``body`` enquanto ``test``."""

    test: Expression
    body: Command
    line: int = 0
    column: int = 0


@dataclass(frozen=True)
class Program:
    """Programa completo: declarações seguidas dos comandos de ``main``."""

    declarations: list[Declaration]
    commands: list[Command]
    line: int = 0
    column: int = 0


# Aliases de união: só tipos, sem lógica (D-02). Consumidores recebem uniões
# fechadas, o que permite despacho exaustivo nos visitantes futuros.
Declaration = VarDecl | ArrayDecl
Command = Skip | Block | Assign | If | While
Expression = (
    VarRef
    | ArrayRef
    | Binary
    | Unary
    | Convert
    | IntLiteral
    | FloatLiteral
    | BoolLiteral
    | CharLiteral
)
