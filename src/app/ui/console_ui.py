from src.app.services.todo_manager import TodoManager
from src.app.models.task import Task

class ConsoleUI:
    """Console user interface for the todo app."""

    def __init__(self, todo_manager: TodoManager):
        self.todo_manager = todo_manager

    def display_tasks(self):
        """Display all tasks in a formatted way."""
        tasks = self.todo_manager.list_tasks()
        if not tasks:
            print("No tasks found.")
            return

        print("\nYour Todo List:")
        print("-" * 40)
        for task in tasks:
            status = "[Completed]" if task.is_completed else "[Pending]"
            print(f"{task.id}. {status} {task.title}")
        print("-" * 40)

    def add_task_prompt(self):
        """Prompt user for task title and add it."""
        title = input("Enter task title: ").strip()
        if not title:
            print("Task title cannot be empty.")
            return
        try:
            task = self.todo_manager.add_task(title)
            print(f"Added task: {task.title} (ID: {task.id})")
        except ValueError as e:
            print(f"Error: {e}")

    def update_task_prompt(self):
        """Prompt user for task ID and new title to update a task."""
        try:
            task_id_input = input("Enter task ID to update: ").strip()
            if not task_id_input:
                print("Task ID cannot be empty.")
                return
            task_id = int(task_id_input)
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        new_title = input("Enter new title: ").strip()
        if not new_title:
            print("Task title cannot be empty.")
            return

        try:
            task = self.todo_manager.update_task(task_id, new_title)
            print(f"Updated task: {task.title} (ID: {task.id})")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def toggle_task_prompt(self):
        """Prompt user for task ID to toggle its completion status."""
        try:
            task_id_input = input("Enter task ID to toggle: ").strip()
            if not task_id_input:
                print("Task ID cannot be empty.")
                return
            task_id = int(task_id_input)
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        try:
            task = self.todo_manager.toggle_task(task_id)
            status = "completed" if task.is_completed else "pending"
            print(f"Toggled task to {status}: {task.title} (ID: {task.id})")
        except KeyError as e:
            print(f"Error: {e}")

    def delete_task_prompt(self):
        """Prompt user for task ID to delete."""
        try:
            task_id_input = input("Enter task ID to delete: ").strip()
            if not task_id_input:
                print("Task ID cannot be empty.")
                return
            task_id = int(task_id_input)
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return

        try:
            self.todo_manager.delete_task(task_id)
            print(f"Deleted task with ID: {task_id}")
        except KeyError as e:
            print(f"Error: {e}")

    def show_help(self):
        """Display help information for available commands."""
        print("\nAvailable commands:")
        print("  add      - Add a new task")
        print("  list     - List all tasks")
        print("  update   - Update a task's title")
        print("  complete - Toggle a task's completion status")
        print("  delete   - Delete a task")
        print("  help     - Show this help message")
        print("  quit     - Exit the application")
