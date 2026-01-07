from sqlmodel import Session, select
from typing import Optional
import re
from ..models import User
from ..schemas import UserCreate

def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def get_user_by_email(session: Session, email: str) -> Optional[User]:
    """Get a user by email."""
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()

def check_email_exists(session: Session, email: str) -> bool:
    """Check if a user with the given email already exists."""
    user = get_user_by_email(session, email)
    return user is not None

def validate_user_data(user_data: UserCreate) -> list[str]:
    """Validate user data and return list of error messages."""
    errors = []

    # Validate email format
    if not validate_email(user_data.email):
        errors.append("Invalid email format")

    # Check password length
    if len(user_data.password) < 8:
        errors.append("Password must be at least 8 characters long")

    return errors