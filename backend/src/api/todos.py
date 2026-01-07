from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session
from typing import List, Optional
from uuid import UUID
from ..database import get_session
from ..models import Todo
from ..schemas import TodoCreate, TodoUpdate, TodoResponse
from ..services.todo_service import (
    create_todo, get_todo_by_id, get_todos_for_user,
    update_todo, delete_todo, toggle_todo_completion
)
from ..middleware.auth_middleware import AuthMiddleware
from uuid import UUID

router = APIRouter()
auth_middleware = AuthMiddleware()

@router.get("/", response_model=List[TodoResponse])
async def get_todos(
    completed: Optional[bool] = Query(None, description="Filter by completion status"),
    user_id: str = Depends(auth_middleware),
    session: Session = Depends(get_session)
):
    """Get all todos for the authenticated user."""
    user_uuid = UUID(user_id)
    todos = get_todos_for_user(session, user_uuid, completed)
    return todos

@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo_endpoint(
    todo: TodoCreate,
    user_id: str = Depends(auth_middleware),
    session: Session = Depends(get_session)
):
    """Create a new todo for the authenticated user."""
    user_uuid = UUID(user_id)

    # Validate input
    if not todo.title or len(todo.title.strip()) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title is required"
        )

    if todo.priority and (todo.priority < 1 or todo.priority > 3):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Priority must be between 1 and 3"
        )

    return create_todo(session, todo, user_uuid)

@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(
    todo_id: UUID,
    user_id: str = Depends(auth_middleware),
    session: Session = Depends(get_session)
):
    """Get a specific todo by ID."""
    todo = get_todo_by_id(session, todo_id, UUID(user_id))
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or doesn't belong to user"
        )
    return todo

@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo_endpoint(
    todo_id: UUID,
    todo_update: TodoUpdate,
    user_id: str = Depends(auth_middleware),
    session: Session = Depends(get_session)
):
    """Update a specific todo."""
    updated_todo = update_todo(session, todo_id, todo_update, UUID(user_id))
    if not updated_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or doesn't belong to user"
        )
    return updated_todo

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo_endpoint(
    todo_id: UUID,
    user_id: str = Depends(auth_middleware),
    session: Session = Depends(get_session)
):
    """Delete a specific todo."""
    success = delete_todo(session, todo_id, UUID(user_id))
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or doesn't belong to user"
        )
    return

@router.patch("/{todo_id}/toggle", response_model=TodoResponse)
async def toggle_todo_completion_endpoint(
    todo_id: UUID,
    user_id: str = Depends(auth_middleware),
    session: Session = Depends(get_session)
):
    """Toggle the completion status of a todo."""
    toggled_todo = toggle_todo_completion(session, todo_id, UUID(user_id))
    if not toggled_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or doesn't belong to user"
        )
    return toggled_todo