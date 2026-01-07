from sqlmodel import Session, select
from typing import List, Optional
from uuid import UUID
from ..models import Todo, User
from ..schemas import TodoCreate, TodoUpdate

def create_todo(session: Session, todo: TodoCreate, user_id: UUID) -> Todo:
    """Create a new todo for a user."""
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        priority=todo.priority,
        user_id=user_id
    )
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

def get_todo_by_id(session: Session, todo_id: UUID, user_id: UUID) -> Optional[Todo]:
    """Get a specific todo by ID for a user."""
    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
    return session.exec(statement).first()

def get_todos_for_user(session: Session, user_id: UUID, completed: Optional[bool] = None) -> List[Todo]:
    """Get all todos for a user, optionally filtered by completion status."""
    statement = select(Todo).where(Todo.user_id == user_id)

    if completed is not None:
        statement = statement.where(Todo.is_completed == completed)

    statement = statement.order_by(Todo.created_at.desc())
    return session.exec(statement).all()

def update_todo(session: Session, todo_id: UUID, todo_update: TodoUpdate, user_id: UUID) -> Optional[Todo]:
    """Update a todo for a user."""
    db_todo = get_todo_by_id(session, todo_id, user_id)
    if not db_todo:
        return None

    # Update fields if they are provided
    for field, value in todo_update.model_dump(exclude_unset=True).items():
        setattr(db_todo, field, value)

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

def delete_todo(session: Session, todo_id: UUID, user_id: UUID) -> bool:
    """Delete a todo for a user."""
    db_todo = get_todo_by_id(session, todo_id, user_id)
    if not db_todo:
        return False

    session.delete(db_todo)
    session.commit()
    return True

def toggle_todo_completion(session: Session, todo_id: UUID, user_id: UUID) -> Optional[Todo]:
    """Toggle the completion status of a todo."""
    db_todo = get_todo_by_id(session, todo_id, user_id)
    if not db_todo:
        return None

    db_todo.is_completed = not db_todo.is_completed
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo