# test05

A Python application scaffold with a clean project structure, automated tooling, and development best practices.

## Prerequisites

- Python 3.11 or higher
- pip (included with Python)
- GNU Make (optional, for convenience commands)

## Installation

Clone the repository and install in development mode:

```bash
git clone https://github.com/chrisliume/test05.git
cd test05
make install
```

This installs the project in editable mode along with development dependencies (pytest, etc.).

If you prefer not to use Make:

```bash
pip install -e ".[dev]"
```

## Usage

Run the application via the installed entry point:

```bash
test05
```

Or run directly as a module:

```bash
python -m src.main
# or
make run
```

## Testing

Run the test suite:

```bash
make test
```

Or invoke pytest directly:

```bash
pytest
```

Tests live in the `tests/` directory and are discovered automatically by pytest.

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