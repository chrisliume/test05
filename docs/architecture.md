# Architecture

This document describes the project structure, module responsibilities, and data flow for `test05`.

## High-Level Overview

```
┌─────────────────────────────────────────────────────────┐
│                     Entry Points                         │
│  CLI (`test05`) ──► src.main:main()                     │
│  Module (`python -m src.main`) ──► src.main:main()      │
└─────────────────────────────────────────────────────────┘
```

`test05` is a Python application scaffold designed for incremental development. It provides a minimal running application with full tooling infrastructure (linting, testing, CI) already in place.

## Project Structure

```
test05/
├── src/                     # Application source code
│   ├── __init__.py          # Package marker
│   └── main.py              # Application entry point and core logic
├── tests/                   # Test suite
│   ├── __init__.py          # Package marker
│   └── test_main.py         # Unit tests for main module
├── config/                  # Configuration files (runtime settings)
├── docs/                    # Documentation
│   └── architecture.md      # This file
├── .github/workflows/       # CI/CD pipeline definitions
│   └── ci.yml               # Lint and test workflow
├── Makefile                 # Developer convenience commands
├── pyproject.toml           # Project metadata, dependencies, tool config
└── .pre-commit-config.yaml  # Git hook configuration
```

## Module Responsibilities

### `src/` — Application Code

| Module     | Responsibility                                                        |
|------------|-----------------------------------------------------------------------|
| `main.py`  | Application entry point. Defines `main()` which is the CLI function.  |

As the project grows, new modules should be added under `src/` with clear single-responsibility boundaries. Import the package as `src.<module>`.

### `tests/` — Test Suite

| Module         | Responsibility                          |
|----------------|----------------------------------------|
| `test_main.py` | Verifies `main()` output and behavior. |

Tests follow pytest conventions. Each `src/` module should have a corresponding `tests/test_<module>.py` file.

### `config/` — Configuration

Reserved for runtime configuration files (e.g., YAML/TOML settings, environment templates). Currently empty; populated as the application gains configurable behavior.

## Data Flow

The current application follows a simple linear flow:

```
CLI invocation
    │
    ▼
src.main:main()
    │
    ▼
stdout (output to user)
```

As the application grows, the expected pattern is:

```
CLI invocation
    │
    ▼
src.main:main()          ← parses arguments, orchestrates workflow
    │
    ├──► config/         ← loads runtime configuration
    │
    ├──► src.<module>    ← delegates to domain-specific modules
    │
    └──► stdout/files    ← produces output
```

## Tooling & Automation

### Build System

- **Hatchling** — builds and packages the project (`pyproject.toml`)
- **Entry point** — `test05` CLI command maps to `src.main:main`

### Code Quality

- **Ruff** — linting and formatting (replaces flake8, isort, black)
- **Pre-commit hooks** — run ruff checks automatically before each commit

### Testing

- **Pytest** — test runner, discovers tests in `tests/` directory
- Tests run locally via `make test` and in CI on every push/PR

### CI/CD

GitHub Actions (`.github/workflows/ci.yml`) runs two jobs on every push to `main` and on pull requests:

1. **lint** — installs dependencies, runs `ruff check`
2. **test** — installs dependencies, runs `pytest`

## Design Principles

1. **Flat module layout** — all application code lives directly under `src/`; avoid deep nesting until complexity warrants it.
2. **Single entry point** — `main()` is the sole orchestrator; other modules expose functions, not scripts.
3. **Test parity** — every `src/` module has a matching test file.
4. **Tooling over convention** — formatting and lint rules are enforced by ruff, not by review comments.

## Extending the Architecture

When adding new functionality:

1. Create a new module under `src/` (e.g., `src/parser.py`).
2. Add a corresponding test file (`tests/test_parser.py`).
3. Wire it into `main()` or expose a new entry point in `pyproject.toml`.
4. If the module needs configuration, add a file under `config/` and load it at startup.
