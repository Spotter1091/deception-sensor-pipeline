# =====================================================
# Deception Analysis Platform
# Build Automation
# =====================================================

PYTHON := python
SRC := src
TESTS := tests

.PHONY: help install run test lint format typecheck clean all

help:
	@echo "Available commands:"
	@echo "  make install     Install project dependencies"
	@echo "  make run         Execute the analysis pipeline"
	@echo "  make test        Run the test suite"
	@echo "  make lint        Run Ruff static analysis"
	@echo "  make format      Format source code"
	@echo "  make typecheck   Run MyPy type checking"
	@echo "  make clean       Remove generated artifacts"
	@echo "  make all         Run formatting, linting, type checking and tests"

install:
	pip install -r requirements.txt

run:
	$(PYTHON) -m pipeline.main

test:
	pytest

lint:
	ruff check $(SRC) $(TESTS)

format:
	ruff format $(SRC) $(TESTS)
	black $(SRC) $(TESTS)

typecheck:
	mypy $(SRC)

clean:
	rm -rf derived
	mkdir -p derived
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
all: format lint typecheck test
