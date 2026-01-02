from src.app.services.todo_manager import TodoManager
from src.app.ui.console_ui import ConsoleUI

def main():
    """Main entry point for the todo app."""
    todo_manager = TodoManager()
    ui = ConsoleUI(todo_manager)

    print("Welcome to the Todo App!")
    print("Commands: 'add', 'list', 'update', 'complete', 'delete', 'quit'")

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command == "quit" or command == "exit":
            print("Goodbye!")
            break
        elif command == "list":
            ui.display_tasks()
        elif command == "add":
            ui.add_task_prompt()
        elif command == "update":
            ui.update_task_prompt()
        elif command == "complete" or command == "toggle":
            ui.toggle_task_prompt()
        elif command == "delete":
            ui.delete_task_prompt()
        elif command == "help":
            ui.show_help()
        else:
            print("Unknown command. Type 'help' for available commands.")

if __name__ == "__main__":
    main()
