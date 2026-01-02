from dataclasses import dataclass

@dataclass
class Task:
    """Represents a single todo item in the system."""
    id: int
    title: str
    is_completed: bool = False
