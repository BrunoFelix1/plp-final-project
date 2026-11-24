"""Testes do verificador de números mágicos."""

from pathlib import Path

from tools.magic_numbers import Finding, find_magic_numbers, find_magic_numbers_in_source

REPO_ROOT_DEPTH = 2
MAGIC_VALUE = 42
EXPECTED_ONE = 1
EXAMPLE_NAME = "exemplo.py"
CONSTANT_SOURCE = "MAX_SIZE = 42\n"
SINGLE_LETTER_SOURCE = "X = 42\n"
MAGIC_SOURCE = "def f():\n    return 42\n"
ALLOW_SOURCE = "def f():\n    return 42  # magic: allow\n"
INDEX_SOURCE = "def first(values):\n    return values[0]\n"
CLITE_SOURCE = "int main() { int x; x = 42; }\n"
CLITE_NAME = "programa.clite"


def _findings_for(source: str, tmp_path: Path) -> list[Finding]:
    path = tmp_path / EXAMPLE_NAME
    path.write_text(source, encoding="utf-8")
    return find_magic_numbers_in_source(source, path=path)


def test_detecta_numero_magico(tmp_path: Path) -> None:
    findings = _findings_for(MAGIC_SOURCE, tmp_path)
    assert len(findings) == EXPECTED_ONE
    assert findings[0].value == MAGIC_VALUE


def test_permite_constante_nomeada(tmp_path: Path) -> None:
    assert _findings_for(CONSTANT_SOURCE, tmp_path) == []


def test_rejeita_constante_com_letra_unica(tmp_path: Path) -> None:
    findings = _findings_for(SINGLE_LETTER_SOURCE, tmp_path)
    assert len(findings) == EXPECTED_ONE


def test_permite_marcador_de_excecao(tmp_path: Path) -> None:
    assert _findings_for(ALLOW_SOURCE, tmp_path) == []


def test_permite_zero_como_indice(tmp_path: Path) -> None:
    assert _findings_for(INDEX_SOURCE, tmp_path) == []


def test_ignora_programas_clite(tmp_path: Path) -> None:
    path = tmp_path / CLITE_NAME
    path.write_text(CLITE_SOURCE, encoding="utf-8")
    assert find_magic_numbers([path]) == []


def test_repositorio_sem_numeros_magicos() -> None:
    root = Path(__file__).resolve().parents[REPO_ROOT_DEPTH]
    targets = [root / "src", root / "tests", root / "tools", root / "scripts"]
    findings = find_magic_numbers(targets)
    assert findings == [], "\n".join(finding.format() for finding in findings)
