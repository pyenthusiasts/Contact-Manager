.PHONY: help install install-dev test test-cov lint format type-check clean run docker-build docker-run pre-commit

# Variables
PYTHON := python3
PIP := $(PYTHON) -m pip
PYTEST := $(PYTHON) -m pytest
BLACK := $(PYTHON) -m black
ISORT := $(PYTHON) -m isort
FLAKE8 := $(PYTHON) -m flake8
MYPY := $(PYTHON) -m mypy

help:  ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install the package
	$(PIP) install -e .

install-dev:  ## Install package with development dependencies
	$(PIP) install -e ".[dev]"
	$(PIP) install -r requirements-dev.txt
	pre-commit install

test:  ## Run tests
	$(PYTEST) tests/ -v

test-cov:  ## Run tests with coverage
	$(PYTEST) tests/ -v --cov=contact_manager --cov-report=html --cov-report=term

test-watch:  ## Run tests in watch mode
	$(PYTEST) tests/ -v --looponfail

lint:  ## Run all linters
	$(FLAKE8) src tests
	$(BLACK) --check src tests
	$(ISORT) --check-only src tests

format:  ## Format code with black and isort
	$(BLACK) src tests
	$(ISORT) src tests

type-check:  ## Run type checking with mypy
	$(MYPY) src --ignore-missing-imports

security:  ## Run security checks
	bandit -r src -ll

clean:  ## Clean up generated files
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/ .mypy_cache/

run:  ## Run the application
	$(PYTHON) run.py

demo:  ## Generate demo data
	$(PYTHON) scripts/generate_demo_data.py

docker-build:  ## Build Docker image
	docker build -t contact-manager:latest .

docker-run:  ## Run Docker container
	docker run -it --rm -v $(PWD)/data:/app/data contact-manager:latest

docker-compose-up:  ## Start services with docker-compose
	docker-compose up -d

docker-compose-down:  ## Stop services with docker-compose
	docker-compose down

pre-commit:  ## Run pre-commit hooks on all files
	pre-commit run --all-files

build:  ## Build distribution packages
	$(PYTHON) -m build

check-build:  ## Check built packages
	twine check dist/*

publish-test:  ## Publish to TestPyPI
	twine upload --repository testpypi dist/*

publish:  ## Publish to PyPI
	twine upload dist/*

docs:  ## Generate documentation
	@echo "Documentation generation not yet implemented"

coverage-report:  ## Generate and open coverage report
	$(PYTEST) tests/ --cov=contact_manager --cov-report=html
	@echo "Opening coverage report..."
	@python -m webbrowser htmlcov/index.html 2>/dev/null || open htmlcov/index.html 2>/dev/null || xdg-open htmlcov/index.html 2>/dev/null || true

all: clean install-dev lint test  ## Run clean, install-dev, lint, and test

.DEFAULT_GOAL := help
