# ================================================= #
# Imports
# ================================================= #
from pathlib import Path

from clite.__main__ import main

# ================================================= #
# Teste dos subcomandos
# ================================================= #


def test_comandos_reconhecidos(capsys) -> None:
    for comando in ("tokens", "parse", "check", "run"):
        resultado = main([comando, "inexistente.clite"])

        assert resultado == 2

    saida = capsys.readouterr()
    assert "arquivo não encontrado" in saida.err


# ================================================= #
# Teste de arquivo inexistente
# ================================================= #
def test_arquivo_inexistente(tmp_path: Path, capsys) -> None:
    arquivo = tmp_path / "inexistente.clite"

    resultado = main(["tokens", str(arquivo)])

    saida = capsys.readouterr()

    assert resultado == 2
    assert "arquivo não encontrado" in saida.err


# ================================================= #
# Teste de comando nao implementado
# ================================================= #


def test_comando_nao_implementado(tmp_path: Path, capsys) -> None:
    arquivo = tmp_path / "programa.clite"
    arquivo.write_text("int main() {}", encoding="utf-8")

    resultado = main(["tokens", str(arquivo)])

    saida = capsys.readouterr()

    assert resultado == 2
    assert "E9000 não implementado" in saida.err
