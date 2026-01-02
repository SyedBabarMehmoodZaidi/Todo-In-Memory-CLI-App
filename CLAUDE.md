# Todo-In-Memory-CLI-App Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-01-02

## Active Technologies

- Python 3.13+
- UV (Package Manager)
- Pytest (Unit Testing)

## Project Structure

```text
src/
└── app/
    ├── models/          # Task dataclass
    ├── services/        # TodoManager logic
    └── ui/              # Console helpers & Loop
tests/
└── unit/                # TodoManager tests
main.py                  # Entry point
```

## Commands

- `uv run main.py`: Start the application
- `uv run pytest`: Run unit tests
- `uv init`: Initialize project environment
- `uv add [dependency]`: Add new dependencies

## Code Style

- Follow PEP 8 guidelines.
- Use type hints for all function signatures and variable declarations.
- Use `dataclasses` for domain models.
- Implement robust input validation (e.g., try-except blocks for numeric input).

## Recent Changes

- **001-todo-cli-phase1**: Initial architecture setup with layered design (Model-Service-UI).

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
