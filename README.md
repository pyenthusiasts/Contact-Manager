# Contact Manager v2.0

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![CI](https://github.com/pyenthusiasts/Contact-Manager/workflows/CI/badge.svg)](https://github.com/pyenthusiasts/Contact-Manager/actions)

A professional, feature-rich Python-based contact management system with a clean command-line interface, data persistence, and comprehensive validation. Perfect for learning Python development best practices or managing your contacts efficiently.

**[Features](#features)** | **[Installation](#installation)** | **[Usage](#usage)** | **[Development](#development)** | **[Contributing](#contributing)**

## Features

### Core Functionality
- **Add Contacts**: Create contacts with name, email, phone, address, and notes
- **Search Contacts**: Fast search by name, email, or phone number (case-insensitive, partial matching)
- **Display Contacts**: View all contacts in a formatted list
- **Update Contacts**: Modify existing contact information
- **Delete Contacts**: Remove contacts with confirmation
- **Export Contacts**: Export to JSON or CSV format
- **Statistics**: View summary statistics about your contacts

### Technical Features
- **Data Persistence**: Automatic saving/loading from JSON storage
- **Input Validation**: Email and phone number validation with helpful error messages
- **Error Handling**: Comprehensive error handling throughout
- **Modular Architecture**: Clean separation of concerns (models, manager, UI, storage, validation)
- **Type Hints**: Full type annotations for better code quality
- **Unit Tests**: Comprehensive test coverage with pytest
- **No External Dependencies**: Uses only Python standard library (except dev tools)

## Installation

### Option 1: Clone and Run (Recommended for Development)

```bash
# Clone the repository
git clone https://github.com/pyenthusiasts/Contact-Manager.git
cd Contact-Manager

# Run directly (no installation needed)
python run.py
```

### Option 2: Install as Package

```bash
# Clone the repository
git clone https://github.com/pyenthusiasts/Contact-Manager.git
cd Contact-Manager

# Install in development mode
pip install -e .

# Run from anywhere
contact-manager
```

### Option 3: Install from Source

```bash
# Clone and install
git clone https://github.com/pyenthusiasts/Contact-Manager.git
cd Contact-Manager
pip install .

# Run
contact-manager
```

### Running as a Module

```bash
# From the project directory
python -m contact_manager
```

### Using Docker

```bash
# Build image
docker build -t contact-manager .

# Run container
docker run -it --rm -v $(pwd)/data:/app/data contact-manager

# Or use docker-compose
docker-compose up
```

### Quick Setup Script

```bash
# Unix/Linux/macOS
./scripts/setup_dev.sh

# Windows
scripts\setup_dev.bat
```

## Usage

### Interactive Menu

When you run the application without arguments, you'll see an interactive menu:

```
==================================================
         CONTACT MANAGER v2.0
==================================================
1.  Add New Contact
2.  Search Contacts
3.  Display All Contacts
4.  Update Contact
5.  Delete Contact
6.  Export Contacts
7.  View Statistics
8.  Exit
==================================================
```

### Examples

#### 1. Adding a Contact

```
Enter your choice (1-8): 1

--- Add New Contact ---
Enter name: John Doe
Enter email: john.doe@example.com
Enter phone number: 123-456-7890
Enter address (optional): 123 Main Street, New York, NY 10001
Enter notes (optional): Important client from ABC Corp

Contact 'John Doe' added successfully!
```

#### 2. Searching for Contacts

Search supports partial matching and is case-insensitive:

```
Enter your choice (1-8): 2

--- Search Contacts ---
Enter search query (name/email/phone): john

Found 2 contact(s):
--------------------------------------------------------------------------------
1. Name: John Doe, Email: john.doe@example.com, Phone: 123-456-7890, Address: 123 Main Street, New York, NY 10001, Notes: Important client from ABC Corp
2. Name: Johnny Smith, Email: johnny@example.com, Phone: 555-1234
--------------------------------------------------------------------------------
```

#### 3. Displaying All Contacts

```
Enter your choice (1-8): 3

================================================================================
Contacts List (5 total)
================================================================================

1. Name: John Doe, Email: john.doe@example.com, Phone: 123-456-7890, Address: 123 Main Street, New York, NY 10001
2. Name: Jane Smith, Email: jane@example.com, Phone: 987-654-3210
...

================================================================================
```

#### 4. Updating a Contact

```
Enter your choice (1-8): 4

--- Update Contact ---
Enter email of contact to update: john.doe@example.com

Current details: Name: John Doe, Email: john.doe@example.com, Phone: 123-456-7890

Enter new values (press Enter to keep current value):
Name [John Doe]: John M. Doe
Email [john.doe@example.com]:
Phone [123-456-7890]: +1-123-456-7890
Address [123 Main Street, New York, NY 10001]:
Notes [Important client from ABC Corp]: VIP client

Contact 'John M. Doe' updated successfully!
```

#### 5. Deleting a Contact

```
Enter your choice (1-8): 5

--- Delete Contact ---
Enter email of contact to delete: old@example.com

Contact to delete: Name: Old Contact, Email: old@example.com, Phone: 111-1111
Are you sure? (yes/no): yes

Contact 'Old Contact' deleted successfully!
```

#### 6. Exporting Contacts

Export to JSON:
```
Enter your choice (1-8): 6

--- Export Contacts ---
Supported formats: JSON (.json), CSV (.csv)
Enter export file path: exports/my_contacts.json

Contacts exported successfully to 'exports/my_contacts.json'!
```

Export to CSV:
```
Enter export file path: exports/contacts.csv

Contacts exported successfully to 'exports/contacts.csv'!
```

#### 7. View Statistics

```
Enter your choice (1-8): 7

--- Contact Statistics ---
Total Contacts: 15
Contacts with Address: 10
Contacts with Notes: 5
```

### Command-Line Interface

Contact Manager also supports non-interactive CLI usage:

```bash
# Add a contact
contact-manager add "John Doe" john@example.com "555-1234" --address "123 Main St" --notes "Client"

# Search contacts
contact-manager search john

# List all contacts
contact-manager list

# Delete a contact
contact-manager delete john@example.com --force

# Export contacts
contact-manager export contacts.csv

# View statistics
contact-manager stats

# Specify custom storage location
contact-manager --storage ~/my-contacts.json list

# Enable debug logging
contact-manager --log-level DEBUG --log-file app.log
```

### Using Makefile

For development tasks:

```bash
# Show all available commands
make help

# Install for development
make install-dev

# Run tests
make test

# Run tests with coverage
make test-cov

# Format code
make format

# Run linters
make lint

# Type checking
make type-check

# Clean generated files
make clean

# Generate demo data
make demo

# Build Docker image
make docker-build

# Run all checks (clean, install, lint, test)
make all
```

## Project Structure

```
Contact-Manager/
├── .github/
│   ├── workflows/
│   │   └── ci.yml               # GitHub Actions CI/CD
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md        # Bug report template
│   │   └── feature_request.md   # Feature request template
│   └── pull_request_template.md # PR template
├── src/
│   └── contact_manager/
│       ├── __init__.py          # Package initialization
│       ├── __main__.py          # Entry point for -m flag
│       ├── models.py            # Contact data model
│       ├── validation.py        # Input validation utilities
│       ├── storage.py           # Data persistence layer
│       ├── manager.py           # Contact management logic
│       ├── ui.py                # Interactive user interface
│       ├── cli.py               # Command-line interface
│       └── logger.py            # Logging configuration
├── tests/
│   ├── __init__.py
│   ├── test_models.py           # Model tests
│   ├── test_validation.py       # Validation tests
│   └── test_manager.py          # Manager tests
├── scripts/
│   ├── generate_demo_data.py    # Demo data generator
│   ├── setup_dev.sh             # Dev setup (Unix)
│   └── setup_dev.bat            # Dev setup (Windows)
├── legacy/
│   └── contact_manager_v1.py    # Original implementation
├── data/                        # Auto-created for storing contacts
│   └── contacts.json
├── run.py                       # Convenience script to run app
├── setup.py                     # Package installation script
├── pyproject.toml               # Modern Python project config
├── requirements.txt             # Core dependencies
├── requirements-dev.txt         # Development dependencies
├── Makefile                     # Development tasks automation
├── Dockerfile                   # Docker container definition
├── docker-compose.yml           # Docker Compose configuration
├── .dockerignore                # Docker ignore rules
├── pytest.ini                   # Pytest configuration
├── .flake8                      # Flake8 linter config
├── .pre-commit-config.yaml      # Pre-commit hooks
├── .gitignore                   # Git ignore rules
├── CONTRIBUTING.md              # Contribution guidelines
├── CODE_OF_CONDUCT.md           # Code of conduct
├── SECURITY.md                  # Security policy
├── CHANGELOG.md                 # Version history
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## Development

### Running Tests

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run all tests
pytest

# Run with coverage
pytest --cov=contact_manager --cov-report=html

# Run specific test file
pytest tests/test_models.py

# Run with verbose output
pytest -v
```

### Code Quality

The project follows Python best practices:
- **PEP 8** style guidelines
- **Type hints** throughout the codebase
- **Docstrings** for all classes and functions
- **Comprehensive error handling**
- **Modular architecture** with clear separation of concerns
- **Unit tests** with high coverage

### Input Validation

#### Email Validation
- Validates proper email format (user@domain.com)
- Checks for @ symbol and valid domain
- Case-insensitive

#### Phone Validation
Accepts various phone number formats:
- `123-456-7890`
- `(123) 456-7890`
- `123.456.7890`
- `1234567890`
- `+1 123 456 7890`
- International formats with 10-15 digits

## Data Storage

Contacts are automatically saved to `data/contacts.json` in the following format:

```json
[
  {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "123-456-7890",
    "address": "123 Main St",
    "notes": "Important client",
    "created_at": "2024-01-15T10:30:00.000000",
    "updated_at": "2024-01-15T10:30:00.000000"
  }
]
```

### Export Formats

**JSON**: Full contact information including timestamps
**CSV**: Simplified format (name, email, phone, address, notes)

## Requirements

- **Python**: 3.8 or higher
- **Core**: No external dependencies (uses standard library only)
- **Development**: pytest, pytest-cov (for testing)

## Architecture Highlights

### Models (`models.py`)
- **Contact dataclass**: Immutable data structure with validation
- Automatic timestamp tracking (created_at, updated_at)
- Conversion to/from dictionary for serialization
- Input validation on initialization and updates

### Validation (`validation.py`)
- Email validation using regex
- Phone number validation with multiple format support
- Input sanitization utilities

### Storage (`storage.py`)
- JSON-based persistence
- Export to JSON and CSV formats
- Automatic directory creation
- Error handling for file operations

### Manager (`manager.py`)
- CRUD operations (Create, Read, Update, Delete)
- Duplicate email detection
- Search with partial matching
- Statistics generation
- Automatic persistence on changes

### UI (`ui.py`)
- Interactive command-line interface
- Input validation and error handling
- Keyboard interrupt handling (Ctrl+C)
- Clear, formatted output

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the Repository**
   ```bash
   git clone https://github.com/your-username/Contact-Manager.git
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow existing code style
   - Add tests for new features
   - Update documentation as needed

4. **Run Tests**
   ```bash
   pytest
   ```

5. **Commit Your Changes**
   ```bash
   git commit -m "Add: feature description"
   ```

6. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

### Development Guidelines

- Write tests for all new features
- Maintain test coverage above 80%
- Follow PEP 8 style guidelines
- Add type hints to all functions
- Document all public APIs
- Handle errors gracefully

## Roadmap

Potential future enhancements:

- [ ] GUI version using Tkinter or PyQt
- [ ] Import contacts from CSV/JSON/vCard
- [ ] Contact groups/categories
- [ ] Birthday reminders
- [ ] Multiple phone numbers per contact
- [ ] Photo/avatar support
- [ ] Contact merging (duplicate detection)
- [ ] Backup and restore functionality
- [ ] Search filters (by date, category, etc.)
- [ ] RESTful API for web integration
- [ ] Database support (SQLite, PostgreSQL)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### Version 2.0.0 (2024)
- Complete rewrite with modular architecture
- Added data persistence with JSON storage
- Implemented comprehensive input validation
- Added update and delete functionality
- Added export feature (JSON and CSV)
- Added search with partial matching
- Added contact statistics
- Added optional fields (address, notes)
- Added timestamps for contact tracking
- Implemented comprehensive error handling
- Added full test suite with pytest
- Added type hints throughout
- Improved documentation

### Version 1.0.0 (Initial Release)
- Basic contact management
- Add, search, and display contacts
- Simple command-line interface

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/pyenthusiasts/Contact-Manager/issues) page
2. Create a new issue with detailed information
3. Include your Python version and operating system

## Acknowledgments

- Built with Python 3
- Inspired by the need for a simple, educational contact management system
- Perfect for learning Python development best practices

---

**Made with Python** | [GitHub](https://github.com/pyenthusiasts/Contact-Manager) | [Report Bug](https://github.com/pyenthusiasts/Contact-Manager/issues) | [Request Feature](https://github.com/pyenthusiasts/Contact-Manager/issues)
