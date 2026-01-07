from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[int] = 2

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    priority: Optional[int] = None

class TodoResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: Optional[str]
    is_completed: bool
    priority: int
    created_at: datetime
    updated_at: datetime
    user_id: uuid.UUID

    class Config:
        from_attributes = True