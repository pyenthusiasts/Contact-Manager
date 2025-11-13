# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions CI/CD workflow for automated testing
- Pre-commit hooks configuration
- Code quality tools configuration (black, flake8, mypy, isort)
- Comprehensive development documentation (CONTRIBUTING.md)
- Security policy (SECURITY.md)
- Code of Conduct (CODE_OF_CONDUCT.md)
- Issue templates for bugs and feature requests
- Pull request template
- Dockerfile for containerization
- Logging support throughout the application
- CLI argument parsing for advanced usage
- Demo data generator script
- Development requirements file (requirements-dev.txt)
- Coverage configuration in pyproject.toml

### Changed
- Migrated package configuration to pyproject.toml (modern Python packaging)
- Enhanced .gitignore with more comprehensive rules

## [2.0.0] - 2024-11-13

### Added
- Complete project restructure with modern Python package layout
- Modular architecture with separate components:
  - `models.py` - Data models with validation
  - `validation.py` - Input validation utilities
  - `storage.py` - Persistence layer
  - `manager.py` - Business logic
  - `ui.py` - User interface
- Data persistence with JSON storage
- Automatic save/load functionality
- Update contact functionality
- Delete contact functionality with confirmation
- Export contacts to JSON format
- Export contacts to CSV format
- Search with partial matching (case-insensitive)
- Contact statistics viewer
- Optional contact fields (address, notes)
- Automatic timestamp tracking (created_at, updated_at)
- Comprehensive input validation:
  - Email format validation
  - Phone number validation (multiple formats)
  - Input sanitization
- Duplicate email detection
- Comprehensive error handling throughout
- Full test suite with pytest:
  - Model tests
  - Validation tests
  - Manager tests
- Type hints throughout the codebase
- Detailed docstrings for all public APIs
- Professional README with:
  - Multiple installation methods
  - Comprehensive usage examples
  - Architecture documentation
  - Development guidelines
- Setup.py for package installation
- Requirements.txt for dependencies
- Pytest.ini for test configuration
- Run.py convenience script
- MIT License

### Changed
- Migrated from monolithic script to modular package structure
- Improved user interface with better formatting
- Enhanced error messages for better user experience
- Contact model now uses dataclass for immutability
- Storage moved from in-memory to persistent JSON

### Deprecated
- Legacy single-file implementation (moved to legacy/)

### Security
- Added input sanitization for all user inputs
- Validated all email and phone formats
- Protected against empty/invalid data

## [1.0.0] - 2024-01-01

### Added
- Initial release
- Basic contact management functionality
- Add contacts (name, email, phone)
- Search contacts by name
- Display all contacts
- Simple command-line interface
- In-memory storage
- Basic input validation

---

## Version Naming

- **Major version** (X.0.0): Breaking changes or major feature additions
- **Minor version** (0.X.0): New features, backwards compatible
- **Patch version** (0.0.X): Bug fixes, minor improvements

## Links

- [PyPI](https://pypi.org/project/contact-manager/) (when published)
- [GitHub Repository](https://github.com/pyenthusiasts/Contact-Manager)
- [Issue Tracker](https://github.com/pyenthusiasts/Contact-Manager/issues)
- [Documentation](https://github.com/pyenthusiasts/Contact-Manager#readme)

[Unreleased]: https://github.com/pyenthusiasts/Contact-Manager/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/pyenthusiasts/Contact-Manager/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/pyenthusiasts/Contact-Manager/releases/tag/v1.0.0
