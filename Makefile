.PHONY: help run build patch minor major pub test lint

help:
	@echo "Available commands:"
	@echo "  make run   - Run the tool locally"
	@echo "  make build - Build the package"
	@echo "  make test  - Run tests"
	@echo "  make lint  - Run linters"

run:
	python3 -m src.selfhost.main

build:
	python3 -m build

test:
	pytest

lint:
	ruff check .
