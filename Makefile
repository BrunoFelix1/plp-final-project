.DEFAULT_GOAL := help
PY := uv run

.PHONY: help install lint format types test test-cov check clean

help: ## Mostra os comandos disponíveis
	@grep -hE '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Sincroniza o ambiente e instala os hooks de pre-commit
	uv sync
	$(PY) pre-commit install

lint: ## Analisa estilo e possíveis bugs
	$(PY) ruff check .

format: ## Formata o código
	$(PY) ruff format .
	$(PY) ruff check --fix .

types: ## Checagem estática de tipos
	$(PY) mypy src

test: ## Executa os testes unitários
	$(PY) pytest

test-cov: ## Executa os testes com relatório de cobertura
	$(PY) pytest --cov --cov-report=term-missing

check: lint types test ## Executa lint, tipos e testes (mesmo conjunto do CI)

clean: ## Remove caches locais
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
