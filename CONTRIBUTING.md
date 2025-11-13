# Contributing to Contact Manager

First off, thank you for considering contributing to Contact Manager! It's people like you that make Contact Manager such a great tool.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How Can I Contribute?](#how-can-i-contribute)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Testing Guidelines](#testing-guidelines)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment
4. Create a new branch for your feature or bugfix
5. Make your changes
6. Run tests and linters
7. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git

### Setting Up Your Development Environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Contact-Manager.git
cd Contact-Manager

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install development dependencies
pip install -e ".[dev]"
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### Running the Application

```bash
# Run directly
python run.py

# Or as a module
python -m contact_manager
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=contact_manager --cov-report=html

# Run specific test file
pytest tests/test_models.py

# Run with verbose output
pytest -v
```

### Code Quality Checks

```bash
# Format code with black
black src tests

# Sort imports
isort src tests

# Lint with flake8
flake8 src tests

# Type check with mypy
mypy src

# Security check
bandit -r src
```

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include as many details as possible:

- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Provide specific examples
- Describe the behavior you observed and what you expected
- Include screenshots if relevant
- Note your environment (OS, Python version, etc.)

Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md).

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- Use a clear and descriptive title
- Provide a detailed description of the proposed feature
- Explain why this enhancement would be useful
- List any alternative solutions you've considered

Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md).

### Your First Code Contribution

Unsure where to begin? Look for issues labeled:

- `good first issue` - Simple issues for newcomers
- `help wanted` - Issues that need attention
- `bug` - Bug fixes
- `enhancement` - New features

### Pull Requests

1. Follow the [style guidelines](#style-guidelines)
2. Update documentation for any changed functionality
3. Add tests for new features
4. Ensure all tests pass
5. Update the CHANGELOG.md
6. Fill out the pull request template completely

## Style Guidelines

### Python Style Guide

We follow PEP 8 with some modifications:

- Line length: 100 characters (not 79)
- Use double quotes for strings
- Use type hints for all function parameters and return values
- Write docstrings for all public classes and functions

### Documentation Style

- Use Google-style docstrings
- Include type information in docstrings
- Provide examples for complex functions
- Keep explanations clear and concise

Example:

```python
def add_contact(self, contact: Contact) -> None:
    """
    Add a new contact to the list.

    Parameters
    ----------
    contact : Contact
        The contact to add.

    Raises
    ------
    ValueError
        If a contact with the same email already exists.

    Examples
    --------
    >>> manager = ContactManager()
    >>> contact = Contact("John Doe", "john@example.com", "123-456-7890")
    >>> manager.add_contact(contact)
    """
```

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests after the first line
- Use conventional commits format:

```
type(scope): subject

body

footer
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, missing semicolons, etc.
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

Example:
```
feat(manager): add bulk import functionality

- Add CSV import support
- Add validation for imported data
- Update documentation

Closes #123
```

## Pull Request Process

1. **Update Documentation**: Ensure README.md and other docs are updated
2. **Update Tests**: Add or modify tests as needed
3. **Run All Checks**: Ensure tests, linters, and type checks pass
4. **Update CHANGELOG**: Add your changes to CHANGELOG.md
5. **Fill PR Template**: Complete all sections of the pull request template
6. **Request Review**: Request review from maintainers
7. **Address Feedback**: Make requested changes promptly
8. **Squash Commits**: Squash related commits before merging (if requested)

### PR Checklist

Before submitting:

- [ ] Code follows style guidelines
- [ ] Self-reviewed the code
- [ ] Commented complex/hard-to-understand areas
- [ ] Updated documentation
- [ ] Added tests for new functionality
- [ ] All tests pass locally
- [ ] No new warnings introduced
- [ ] Updated CHANGELOG.md
- [ ] Rebased on latest main branch

## Testing Guidelines

### Writing Tests

- Write tests for all new features
- Maintain at least 80% code coverage
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern
- Use fixtures for common setup

Example:

```python
def test_add_contact_with_duplicate_email_raises_error(manager, sample_contact):
    """Test that adding a duplicate email raises ValueError."""
    # Arrange
    manager.add_contact(sample_contact)
    duplicate = Contact("Jane", "john@example.com", "987-654-3210")

    # Act & Assert
    with pytest.raises(ValueError, match="already exists"):
        manager.add_contact(duplicate)
```

### Test Organization

- One test file per source file
- Group related tests in classes
- Use fixtures for reusable test data
- Mock external dependencies

## Code Review Process

All submissions require review. We use GitHub pull requests for this purpose:

1. Maintainers will review your code
2. They may request changes
3. Make the requested changes and push to your branch
4. Once approved, a maintainer will merge your PR

### What We Look For

- Code quality and style
- Test coverage
- Documentation completeness
- Performance implications
- Security considerations
- Backward compatibility

## Community

- Be welcoming and friendly
- Be patient and respectful
- Give constructive feedback
- Accept constructive criticism gracefully
- Focus on what is best for the community

## Questions?

Feel free to:

- Open an issue for questions
- Start a discussion in GitHub Discussions
- Reach out to maintainers

## Recognition

Contributors will be recognized in:

- The project's README
- Release notes
- The contributors page

Thank you for contributing to Contact Manager! 🎉
