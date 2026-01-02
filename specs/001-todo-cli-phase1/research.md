# Research: In-Memory Python Console Todo App (Phase I)

## Technical Stack Decisions

### Decision: Python 3.13+ with UV
- **Rationale**: User explicitly requested Python 3.13+ and UV for dependency management. UV is high-performance and ensures reproducible environments.
- **Alternatives considered**: Standard `venv` / `pip` (rejected due to speed/modernity requirements).

### Decision: Architecture Layers
- **Decision**:
  - **Domain Layer**: dataclasses for `Task`.
  - **Service Layer**: `TodoManager` for business logic.
  - **UI Layer**: `ConsoleApp` for CLI loop and I/O.
- **Rationale**: Follows the user's architectural guidance and ensures Principle IV (Extensibility) by decoupling logic from UI.
- **Alternatives considered**: Single-file script (rejected due to Principle V: Maintainability).

### Decision: In-Memory Storage
- **Decision**: Simple `dict` mapping IDs to `Task` objects.
- **Rationale**: Meets Principle III (Performance) and Constraint (In-memory storage only). Dictionary lookups are $O(1)$.
- **Alternatives considered**: `list` (rejected because ID lookup would be $O(n)$).

## Best Practices
- Use `type hints` throughout for Principle V (Maintainability).
- Implement robust input validation in the UI layer to prevent crashing (Principle II: Reliability).
- Follow PEP 8 via `ruff` or similar linting integrated with UV.
