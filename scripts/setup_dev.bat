@echo off
REM Development environment setup script for Windows

echo ==================================
echo Contact Manager - Development Setup
echo ==================================
echo.

REM Check Python version
echo Checking Python version...
python --version
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in PATH
    exit /b 1
)

REM Create virtual environment
echo.
echo Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)

REM Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install package in editable mode with dev dependencies
echo.
echo Installing Contact Manager with development dependencies...
pip install -e ".[dev]"
pip install -r requirements-dev.txt

REM Install pre-commit hooks
echo.
echo Setting up pre-commit hooks...
pre-commit install

REM Create data directory
echo.
echo Creating data directory...
if not exist "data" mkdir data

echo.
echo ==================================
echo Setup complete!
echo ==================================
echo.
echo To activate the virtual environment, run:
echo   venv\Scripts\activate.bat
echo.
echo To run the application:
echo   python run.py
echo.
echo To run tests:
echo   pytest
echo.
echo Happy coding!
