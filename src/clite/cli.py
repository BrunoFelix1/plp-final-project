# ================================================= #
# CLI - Interface de linha de comando CLite
# Ticket 004 - Esqueleto de pacotes e CLI
# ================================================= #

# Perguntinhas bestas... ========================== #
# Vem de onde ? para que serve esses imports?
# ================================================= #
# argparse --> Para receber, interpretar e validar os argumentos passados pelo usuário no terminal.
# sys --> Permite acessar informações e recursos relacionados à execução do programa Python.
import argparse
import sys

# pathlib import Path --> Para trabalhar com caminhos de arquivos e diretórios de maneira orientada a objetos.
from pathlib import Path


# ================================================= #
# Configuracao dos argumentos
# def --> Declara uma função em Python
# criar_parser --> 	Nome da função
# () --> Indica que ela não recebe parâmetros
# -> | Indica o tipo de retorno esperado
# argparse.ArgumentParser --> Classe do objeto que a função retornará
# : --> Inicia o bloco de instruções
# ================================================= #
def criar_parser() -> argparse.ArgumentParser:
    # ================================================= #
    # ArgumentParser --> objeto que sabe interpretar os argumentos fornecidos pelo o usuario no terminal
    # Criando um objeto --> instanciando um objeto --> parâmetro prog="clite"
    # ================================================= #
    parser = argparse.ArgumentParser(
        prog="clite",
        description="Interpretador da linguagem CLite",
    )
    # ================================================= #
    # parser.add_subparsers() é um método da biblio. argparse utilizado para criar subcomandos.
    # cada :
    # clite tokens
    # clite parse
    # clite check
    # clite run
    # --> Cada um representa uma funcionalidade diferente do interpretador.
    # ================================================= #
    subparsers = parser.add_subparsers(
        dest="comando",
        required=True,
    )
    for comando in ("tokens", "parse", "check", "run"):
        # ================================================= #
        #
        # Em cada iteração, o programa executa esse comando abaixo:
        # ================================================= #
        subparser = subparsers.add_parser(
            comando,
            help=f"Executa a etapa {comando} da linguagem CLite",
        )
        subparser.add_argument("arquivo", type=Path)

    return parser


# ================================================= #
# Validacao do arquivo
# ================================================= #


# ================================================= #
# arquivo: Path dentro do () --> a função recebe um caminho representado por um objeto Path
# -> bool --> vai retornar um valor boleano. Um valor boleano é um true ou false
# ================================================= #
def validar_arquivo(arquivo: Path) -> bool:
    # ================================================= #
    # vamos começar em partes:
    # arquivo.is_file() --> verifica se o caminho aponta para um arquivo regular existente.
    # ================================================= #
    if not arquivo.is_file():
        # ================================================= #
        # É uma f-string. --> O Python substitui {arquivo} pelo valor do caminho recebido.
        # file=sys.stderr --> Direciona a mensagem para o fluxo de erros do processo.
        # ================================================= #
        print(
            f"erro: arquivo não encontrado: {arquivo}",
            file=sys.stderr,
        )
        return False

    return True


# ================================================= #
# Execucao dos comandos
# ================================================= #


# ================================================= #
# A função retorna um inteiro.  type , int é um inteiro
#
# ================================================= #
def executar_comando() -> int:
    # ================================================= #
    # Mas por que estamos retornando 2 --> Porque o ticket 004 define que, enquanto os comandos não estiverem implementados, a CLI deverá
    # apresentar: E9000 não implementado, E devolver o código de saída 2.
    #
    # ================================================= #
    print("E9000 não implementado", file=sys.stderr)
    return 2
