import pytest
from src.app.models.task import Task
from src.app.services.todo_manager import TodoManager

def test_add_task(todo_manager):
    """Tests that a task can be added successfully."""
    task = todo_manager.add_task("Learn SDD")
    assert task.id == 1
    assert task.title == "Learn SDD"
    assert not task.is_completed
    assert len(todo_manager.list_tasks()) == 1

def test_add_task_empty_title(todo_manager):
    """Tests that adding a task with an empty title raises ValueError."""
    with pytest.raises(ValueError, match="Task title cannot be empty."):
        todo_manager.add_task("")
    with pytest.raises(ValueError, match="Task title cannot be empty."):
        todo_manager.add_task("   ")

def test_list_tasks(todo_manager):
    """Tests that list_tasks returns all added tasks."""
    todo_manager.add_task("Task 1")
    todo_manager.add_task("Task 2")
    tasks = todo_manager.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"

def test_update_task(todo_manager):
    """Tests that a task can be updated successfully."""
    task = todo_manager.add_task("Learn SDD")
    updated_task = todo_manager.update_task(task.id, "Master SDD")
    assert updated_task.id == task.id
    assert updated_task.title == "Master SDD"
    assert not updated_task.is_completed  # Should preserve completion status

def test_update_task_invalid_id(todo_manager):
    """Tests that updating a non-existent task raises KeyError."""
    with pytest.raises(KeyError, match="Task with ID 999 does not exist."):
        todo_manager.update_task(999, "New title")

def test_update_task_empty_title(todo_manager):
    """Tests that updating a task with an empty title raises ValueError."""
    task = todo_manager.add_task("Learn SDD")
    with pytest.raises(ValueError, match="Task title cannot be empty."):
        todo_manager.update_task(task.id, "")
    with pytest.raises(ValueError, match="Task title cannot be empty."):
        todo_manager.update_task(task.id, "   ")

def test_toggle_task(todo_manager):
    """Tests that a task can be toggled successfully."""
    task = todo_manager.add_task("Learn SDD")
    assert not task.is_completed
    toggled_task = todo_manager.toggle_task(task.id)
    assert toggled_task.is_completed
    # Toggle again to make sure it works both ways
    toggled_back_task = todo_manager.toggle_task(task.id)
    assert not toggled_back_task.is_completed

def test_toggle_task_invalid_id(todo_manager):
    """Tests that toggling a non-existent task raises KeyError."""
    with pytest.raises(KeyError, match="Task with ID 999 does not exist."):
        todo_manager.toggle_task(999)

def test_delete_task(todo_manager):
    """Tests that a task can be deleted successfully."""
    task = todo_manager.add_task("Learn SDD")
    assert len(todo_manager.list_tasks()) == 1
    todo_manager.delete_task(task.id)
    assert len(todo_manager.list_tasks()) == 0

def test_delete_task_invalid_id(todo_manager):
    """Tests that deleting a non-existent task raises KeyError."""
    with pytest.raises(KeyError, match="Task with ID 999 does not exist."):
        todo_manager.delete_task(999)

@pytest.fixture
def todo_manager():
    """Fixture to provide a clean TodoManager instance for each test."""
    return TodoManager()
