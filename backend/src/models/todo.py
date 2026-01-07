from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class TodoBase(SQLModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = Field(default=False)
    priority: int = Field(default=2, ge=1, le=3)  # 1: low, 2: medium, 3: high
    user_id: uuid.UUID

class Todo(TodoBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __repr__(self):
        return f"<Todo(id={self.id}, title={self.title}, user_id={self.user_id})>"