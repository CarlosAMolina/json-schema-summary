install:
	uv sync
	uvx pre-commit install

mypy:
	uv run mypy json_schema_summary

pre-commit:
	uvx pre-commit run --all-files

ruff-check:
	uv run ruff check .

ruff-fix:
	uv run ruff check . --fix

ruff-fix-unsafe:
	uv run ruff check . --fix --unsafe-fixes

ruff-format:
	uv run ruff format

run:
	uv run python -m json_schema_summary.main tests/fake/contacts.json

test:
	uv run pytest
