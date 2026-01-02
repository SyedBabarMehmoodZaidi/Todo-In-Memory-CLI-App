from src.app.models.task import Task

class TodoManager:
    """Service layer and in-memory repository for tasks."""

    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str) -> Task:
        """Adds a new task to the store."""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")

        task = Task(id=self._next_id, title=title.strip())
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def list_tasks(self) -> list[Task]:
        """Returns a list of all tasks."""
        return list(self._tasks.values())

    def update_task(self, task_id: int, new_title: str) -> Task:
        """Updates the title of an existing task."""
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} does not exist.")

        if not new_title or not new_title.strip():
            raise ValueError("Task title cannot be empty.")

        task = self._tasks[task_id]
        updated_task = Task(id=task.id, title=new_title.strip(), is_completed=task.is_completed)
        self._tasks[task_id] = updated_task
        return updated_task

    def toggle_task(self, task_id: int) -> Task:
        """Toggles the completion status of a task."""
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} does not exist.")

        task = self._tasks[task_id]
        toggled_task = Task(id=task.id, title=task.title, is_completed=not task.is_completed)
        self._tasks[task_id] = toggled_task
        return toggled_task

    def delete_task(self, task_id: int) -> None:
        """Deletes a task by its ID."""
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} does not exist.")

        del self._tasks[task_id]
