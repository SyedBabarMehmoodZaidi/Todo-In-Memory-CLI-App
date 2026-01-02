# Service Interface: TodoManager

The `TodoManager` acts as the service layer/repository for Phase I.

## Methods

### `add_task(title: str) -> Task`
- **Input**: `title` (string)
- **Output**: The created `Task` object
- **Errors**: `ValueError` if title is empty

### `list_tasks() -> list[Task]`
- **Input**: None
- **Output**: List of all `Task` objects currently in memory

### `update_task(task_id: int, new_title: str) -> Task`
- **Input**: `task_id` (int), `new_title` (str)
- **Output**: The updated `Task` object
- **Errors**: `KeyError` if ID not found, `ValueError` if new title invalid

### `delete_task(task_id: int) -> None`
- **Input**: `task_id` (int)
- **Output**: None
- **Errors**: `KeyError` if ID not found

### `toggle_task(task_id: int) -> Task`
- **Input**: `task_id` (int)
- **Output**: The toggled `Task` object
- **Errors**: `KeyError` if ID not found
