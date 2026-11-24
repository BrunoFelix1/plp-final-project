"""Detecta números mágicos no código Python que implementa o interpretador."""

from __future__ import annotations

import argparse
import ast
import re
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path

ALLOWED_VALUES = frozenset({0, 1})
CONSTANT_NAME = re.compile(r"^[A-Z][A-Z0-9_]*$")
ALLOW_MARKER = "# magic: allow"
DEFAULT_TARGETS = ("src", "tests", "tools", "scripts")
SKIP_DIRECTORIES = frozenset(
    {".git", ".venv", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
)
EXIT_OK = 0
EXIT_FINDINGS = 1
MIN_INDEX = 0
LINE_INDEX_OFFSET = 1
MIN_CONSTANT_NAME_LENGTH = 3


@dataclass(frozen=True)
class Finding:
    """Um número mágico encontrado no código."""

    path: Path
    line: int
    column: int
    value: int | float

    def format(self) -> str:
        """Formata o achado para exibição no terminal."""
        return (
            f"{self.path}:{self.line}:{self.column}: número mágico {self.value!r}; "
            "atribua a uma constante com nome significativo (sem letras únicas)"
        )


def _is_constant_target(target: ast.AST) -> bool:
    return (
        isinstance(target, ast.Name)
        and len(target.id) >= MIN_CONSTANT_NAME_LENGTH
        and bool(CONSTANT_NAME.match(target.id))
    )


def _in_constant_assignment(ancestors: Sequence[ast.AST]) -> bool:
    for node in reversed(ancestors):
        if isinstance(node, ast.Assign):
            return all(_is_constant_target(target) for target in node.targets)
        if isinstance(node, ast.AnnAssign):
            return _is_constant_target(node.target)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            return False
    return False


def _line_allows(source_lines: Sequence[str], line: int) -> bool:
    index = line - LINE_INDEX_OFFSET
    return MIN_INDEX <= index < len(source_lines) and ALLOW_MARKER in source_lines[index]


def _collect(
    node: ast.AST,
    ancestors: list[ast.AST],
    source_lines: Sequence[str],
    path: Path,
    findings: list[Finding],
) -> None:
    if (
        isinstance(node, ast.Constant)
        and isinstance(node.value, (int, float))
        and not isinstance(node.value, bool)
        and node.value not in ALLOWED_VALUES
        and not _in_constant_assignment(ancestors)
        and not _line_allows(source_lines, node.lineno)
    ):
        findings.append(Finding(path, node.lineno, node.col_offset, node.value))

    for child in ast.iter_child_nodes(node):
        _collect(child, [*ancestors, node], source_lines, path, findings)


def find_magic_numbers_in_source(source: str, *, path: Path) -> list[Finding]:
    """Analisa um fonte e devolve os números mágicos encontrados."""
    tree = ast.parse(source, filename=str(path))
    findings: list[Finding] = []
    _collect(tree, [], source.splitlines(), path, findings)
    return findings


def _iter_python_files(path: Path) -> Iterable[Path]:
    if path.is_file():
        if path.suffix == ".py":
            yield path
        return

    if not path.exists():
        return

    for candidate in path.rglob("*.py"):
        if any(part in SKIP_DIRECTORIES for part in candidate.parts):
            continue
        yield candidate


def find_magic_numbers(paths: Iterable[Path]) -> list[Finding]:
    """Analisa arquivos e diretórios e agrega os achados."""
    findings: list[Finding] = []
    for path in paths:
        for file_path in _iter_python_files(path):
            source = file_path.read_text(encoding="utf-8")
            findings.extend(find_magic_numbers_in_source(source, path=file_path))
    return findings


def main(argv: Sequence[str] | None = None) -> int:
    """Executa a verificação pela linha de comando."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=list(DEFAULT_TARGETS))
    args = parser.parse_args(argv)

    findings = find_magic_numbers(Path(path) for path in args.paths)
    for finding in findings:
        print(finding.format())

    if findings:
        print(f"{len(findings)} número(s) mágico(s) encontrado(s).")
        return EXIT_FINDINGS

    print("Nenhum número mágico encontrado.")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
