#!/bin/bash
# Development environment setup script

set -e

echo "=================================="
echo "Contact Manager - Development Setup"
echo "=================================="
echo

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Check if Python >= 3.8
required_version="3.8"
if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "Error: Python 3.8 or higher is required"
    exit 1
fi

# Create virtual environment
echo
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created"
else
    echo "Virtual environment already exists"
fi

# Activate virtual environment
echo
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo
echo "Upgrading pip..."
pip install --upgrade pip

# Install package in editable mode with dev dependencies
echo
echo "Installing Contact Manager with development dependencies..."
pip install -e ".[dev]"
pip install -r requirements-dev.txt

# Install pre-commit hooks
echo
echo "Setting up pre-commit hooks..."
pre-commit install

# Create data directory
echo
echo "Creating data directory..."
mkdir -p data

echo
echo "=================================="
echo "Setup complete!"
echo "=================================="
echo
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo
echo "To run the application:"
echo "  python run.py"
echo
echo "To run tests:"
echo "  make test"
echo
echo "To see all available commands:"
echo "  make help"
echo
echo "Happy coding!"
