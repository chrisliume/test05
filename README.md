# test05

A Python application scaffold with a clean project structure, automated tooling, and development best practices.

## Prerequisites

- Python 3.11 or higher
- pip (included with Python)
- GNU Make (optional, for convenience commands)

## Local Setup

Follow these steps to get a working development environment from scratch.

### 1. Verify Python version

This project requires **Python 3.11+**. Confirm your version:

```bash
python3 --version   # must be 3.11 or higher
```

### 2. Clone the repository

```bash
git clone https://github.com/chrisliume/test05.git
cd test05
```

### 3. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux / macOS
# On Windows: .venv\Scripts\activate
```

### 4. Install dependencies

With Make (recommended):

```bash
make install
```

Or manually:

```bash
pip install -e ".[dev]"
```

This installs the project in editable mode along with development dependencies (pytest, ruff, etc.).

### 5. Run the application

Via the installed entry point:

```bash
test05
```

Or as a Python module:

```bash
python -m src.main
# or
make run
```

### 6. Verify the setup

Run the test suite to confirm everything works:

```bash
make test
# or
pytest
```

If all tests pass, your environment is ready for development.

## Testing

Tests live in the `tests/` directory and are discovered automatically by pytest:

```bash
make test
# or
pytest
```

## Linting and Formatting

Check code style with ruff:

```bash
make lint
```

Auto-format code:

```bash
make format
```

## Project Structure

```
test05/
├── src/
│   ├── __init__.py
│   └── main.py          # Application entry point
├── tests/
│   ├── __init__.py
│   └── test_main.py     # Unit tests
├── Makefile             # Development convenience commands
├── pyproject.toml       # Project metadata and tool configuration
└── README.md
```

## Contributing

1. Create a feature branch from `main`.
2. Make your changes and add tests for new functionality.
3. Run `make lint` and `make test` to ensure code quality.
4. Commit with clear, descriptive messages.
5. Open a pull request against `main`.

### Guidelines

- Keep pull requests focused on a single concern.
- All new code should have corresponding tests.
- Follow existing code style — ruff enforces formatting and linting rules.
- Ensure all tests pass before requesting review.