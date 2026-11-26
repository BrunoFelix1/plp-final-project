"""Testes da CLI `clite tokens` e dos goldens do léxico (ticket 008)."""

from pathlib import Path

import pytest

from clite.__main__ import main
from clite.cli import EXIT_OK, EXIT_PROGRAM_ERROR, EXIT_USAGE_ERROR

REPO_ROOT_DEPTH = 2
MIN_GOLDEN_FILES = 3
REPO_ROOT = Path(__file__).resolve().parents[REPO_ROOT_DEPTH]
EXAMPLES = REPO_ROOT / "examples" / "lexico"
GOLDEN = REPO_ROOT / "tests" / "golden" / "lexer"
TOKEN_GOLDENS = sorted(path.stem for path in GOLDEN.glob("*.tokens"))
ERROR_GOLDENS = sorted(path.stem for path in GOLDEN.glob("*.err"))


def run_cli(args: list[str], capsys: pytest.CaptureFixture[str]) -> tuple[int, str, str]:
    """Roda a CLI e devolve (exit code, stdout, stderr)."""
    code = main(args)
    captured = capsys.readouterr()
    return code, captured.out, captured.err


def tokens_of(
    source: str, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> tuple[int, str, str]:
    program = tmp_path / "programa.clite"
    program.write_text(source, encoding="utf-8")
    return run_cli(["tokens", str(program)], capsys)


def test_one_line_per_token(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    code, out, err = tokens_of("int x;", tmp_path, capsys)
    assert code == EXIT_OK
    assert out == "INT int 1:1\nIDENT x 1:5\nSEMICOLON ; 1:6\n"
    assert err == ""


def test_empty_file_prints_nothing(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert tokens_of("", tmp_path, capsys) == (EXIT_OK, "", "")


def test_eof_is_not_printed(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    _, out, _ = tokens_of("x", tmp_path, capsys)
    assert "EOF" not in out


def test_output_is_deterministic(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    first = tokens_of("a <= b // fim", tmp_path, capsys)
    second = tokens_of("a <= b // fim", tmp_path, capsys)
    assert first == second


def test_char_literal_keeps_quotes_and_space(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    _, out, _ = tokens_of("' '", tmp_path, capsys)
    assert out == "CHAR_LITERAL ' ' 1:1\n"


@pytest.mark.parametrize(
    ("source", "code"),
    [("a @ b", "E1001"), ("a & b", "E1002")],
)
def test_lexical_error_is_one_line_on_stderr(
    source: str, code: str, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    exit_code, out, err = tokens_of(source, tmp_path, capsys)
    assert exit_code == EXIT_PROGRAM_ERROR
    assert out == ""
    assert len(err.splitlines()) == 1
    assert err.startswith(f"erro {code} (linha 1, coluna 3): ")


def test_unreadable_file_is_a_usage_error(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    program = tmp_path / "binario.clite"
    program.write_bytes(b"\xff\xfe\x00")
    code, out, err = run_cli(["tokens", str(program)], capsys)
    assert code == EXIT_USAGE_ERROR
    assert out == ""
    assert "não foi possível ler" in err


@pytest.mark.parametrize("command", ["parse", "check", "run"])
def test_other_commands_are_still_not_implemented(
    command: str, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    program = tmp_path / "programa.clite"
    program.write_text("int x;", encoding="utf-8")
    code, out, err = run_cli([command, str(program)], capsys)
    assert code == EXIT_USAGE_ERROR
    assert out == ""
    assert "E9000 não implementado" in err


def test_there_are_at_least_three_goldens() -> None:
    assert len(TOKEN_GOLDENS) + len(ERROR_GOLDENS) >= MIN_GOLDEN_FILES


@pytest.mark.parametrize("name", TOKEN_GOLDENS)
def test_token_golden(name: str, capsys: pytest.CaptureFixture[str]) -> None:
    code, out, err = run_cli(["tokens", str(EXAMPLES / f"{name}.clite")], capsys)
    assert code == EXIT_OK
    assert err == ""
    assert out == (GOLDEN / f"{name}.tokens").read_text(encoding="utf-8")


@pytest.mark.parametrize("name", ERROR_GOLDENS)
def test_error_golden(name: str, capsys: pytest.CaptureFixture[str]) -> None:
    code, out, err = run_cli(["tokens", str(EXAMPLES / f"{name}.clite")], capsys)
    assert code == EXIT_PROGRAM_ERROR
    assert out == ""
    assert err == (GOLDEN / f"{name}.err").read_text(encoding="utf-8")
